# cd4pe-slack_webhook
Send failed Puppet CD4PE Jobs to Slack

Currently, there is no native integrations for Slack messaging with CD4PE (Continuous Delivery for Puppet Enterprise). The script is to be placed in the "Job Commands" window.

The Slack webhook is using the [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Workflow-Builder). `Text` is used as a variable in the workflow builder and should be added for this to work.

The script.sh file is for running commands for cd4pe containers that are already built in. The main.py is a custom python container added to a CD4PE python in which it also determines the job ID and POSTs to a Slack webhook.

### Prerequisites
If running the job as a container, you may need to mount the cd4pe volume, although I believe this already happens automatically. To do this, in the Docker run arguments, add `-v /cd4pe_job_working_dir:/cd4pe_job_working_dir`
