# cd4pe-slack_webhook
Send failed Puppet CD4PE Jobs to Slack

Currently, there is no native integrations for Slack messaging with CD4PE (Continuous Delivery for Puppet Enterprise). The script is to be placed in the "Job Commands" window.

The Slack webhook is using the [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Workflow-Builder). `Text` is used as a variable in the workflow builder and should be added for this to work.
