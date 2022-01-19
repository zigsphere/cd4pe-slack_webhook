import sys
import os
from glob import glob
import requests
import json
from pathlib import Path
from yaml import safe_load

# Get job name from environment variable
# Set this env variable in the docker arguments (-e JOB=FOO). Also, in the job commands, enter NAME=FOO. 
# We are going to compare the env var with the text in the job.
JOB = os.getenv('JOB')

def check_duplicates_for_key(data: dict, paths: list):
  data_new = {}

  for path, values in data.items():
    filtered_values= []

    if path in paths:
      for item in values:
        if item in filtered_values:
          return True
        filtered_values.append(item)
  return False

if __name__ == '__main__':
  for directories in Path("/cd4pe_job_working_dir/").glob('*'):
    if "*" not in str(directories):
      try:
        with open(os.path.join(directories, "cd4pe_job/jobs/unix/JOB"), "r") as file:
          # Within the JOB file are the job commands. This checks the job commands and determines if matched text exists. If so, now we know which dir
          # name contains the job_id.
          if JOB in file.read(): 
            job_dir = str(directories)
      except FileNotFoundError as error:
        print(f"File cannot be read, {str(error)}")
        continue

  print(job_dir)
  job_id = job_dir.split("_")[6]
  print(job_id)
  with open('/repo/data/common.yaml', "r") as f: # Path to yaml file being parsed for particular key
    data = safe_load(f)

    if check_duplicates_for_key(data, ['foo']):
      url = "https://hooks.slack.com/workflows/XXXXXXXXXXXXX"
      payload = json.dumps({"text": "A failure occurred with CD4PE job: Yaml Parser - JobID: %s || https://cd4pe.domain.internal/cd4pe/puppet/jobs/%s" % (job_id, job_id) })
      headers = {
        'Content-Type': 'application/json'
      }

      response = requests.request("POST", url, headers=headers, data=payload)

      print(response.text)
      print('Duplicate firewall exists in SFTP YAML Configuration')
      sys.exit(1)
