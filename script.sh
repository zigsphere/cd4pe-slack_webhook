NAME="puppetfile-syntax-validate" # Set to anything here. Just the name of the job.
trap 'on_failure' ERR
on_failure() {
    ret=$?
    for i in $(ls /cd4pe_job_working_dir);
    do
      if [[ ! $i =~ "*" ]]; then
        if grep -q $NAME /cd4pe_job_working_dir/$i/cd4pe_job/jobs/unix/JOB; then
          jobid=$(echo $i | awk -F "_" '{print $4}')
          curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"A failure occurred with CD4PE job: control-repo-puppetfile-syntax-validate - JobID: $jobid || https://internal.cd4pe.domain.com/cd4pe/sre-puppet/jobs/$jobid \"}" https://hooks.slack.com/workflows/XXXXXX/XXXXX/XXXXX/XXXXXXXXXXXXXXXXXX
        fi
      fi
    done
    exit $ret
}

rake -f /Rakefile r10k:syntax # CD4PE job (replace with whatever you use as the command)
