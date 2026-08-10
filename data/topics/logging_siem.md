# Netskope Docs — Logging Siem
_Generated: 2026-08-10 08:34 UTC_
_Pages: 108_

---
## Configure a Custom Log Parser
**URL:** https://docs.netskope.com/en/configure-a-custom-log-parser/
**Last Modified:** 2025-08-31T01:50:04+00:00
**Scraped:** 2026-08-10T07:28:37.980803+00:00

Configure a Custom Log Parser - Netskope Technical Documentation
Configure a Custom Log Parser
You can configure a custom log parser if the predefined parsers do not extract events from your uploaded logs. You can customize your parser based on what you know about your logs. After creating a custom parser, it will appear on the Custom tab.
These are the primary steps to configuring a custom log parser:
Upload
Preparation
Extraction
Transformation
Name
To configure a custom parser using a log file:
On the Test/Create page, click
Create Custom Parser
.
On the Upload page, click
Select File
. Locate and select a log file, and then click
Upload
.
Click
Test
to process your log file. The results display on the Extracted Fields tab at the bottom of the page. You can use these bottom tabs to ensure that your log file data is being mapped correctly:
Extracted Fields: This tab shows the columns that are extracted from your log file.
Extracted Events: This tab shows the extracted events from your log file.
Rejections: This tab shows the rejected log line number, line, and reason.
Summary: This tab provides an overview of the total extracted lines, number of rejected lines, and the total uploaded lines.
Tip
The Test button and the bottom tabs display on all pages.
On the Preparation page, select and enter the needed information on these tabs:
Format: This tab opens with a default setting of CSV for format. To change the formatting, specify the following:
Log file type: Choose CSV, Delimited, Key-Value, or Hybrid.
Header in log: Specify whether the log has a header.
Header starts with: Enter the text string that start the header.
Line number: Enter the number of the starting line in the log.
Header delimiter: Choose the type of delimiter from the dropdown.
Pre-Filters: This tab allows you to pick data line patterns for your log file. Currently, the only supported Data Line Pattern is
80http443https
. In addition, you can define the Line/Header Patterns to discard, a regular expression that determines the log lines to discard.
Multi-Line Merge: Use this tab only if you have complex log files that contain lines that split into two lines. You can specify the following:
Multi-line delimiters: Delimiter between lines.
Log-line delimiter size: Delimiter size between log lines.
Log-line delimiter match: Delimiter match between log lines.
When finished, click
Next
.
On the Extraction page, identify the file structure, timestamp, and fields for your log file.
Structure: This tab allows you to specify the Field Delimiter (like comma, space, tab, colon, and so on), Field Enclosure (like double quotes, single quotes, or pipe character), and Line Enclosed Within (like square brackets, parenthesis, curly brackets, pipe character, or double quotes). Timestamp: This tab contains several fields that are important to mapping data correctly. The fields include:
Timestamp Maps To: Identifies the location (column header) of the timestamp in your log file and map it to this field.
Note
This is a required field and best practice is to map it to column 1.
Timestamp Format: In most cases you do not need to change a format except for some cases when the timestamp is in a unique epoch format, in which case you should select a format code like %H for the format field. Refer to the
Timestamp Format Codes
to see all the specific format codes. Enclosed Within: Select if the Timestamp is enclosed within square brackets, parenthesis, curly brackets, pipe character, or double quotes. Default Time Zone: Select your default GMT time zone for the log file.
Fields: For field mapping, verify the log header of each specific field, like Source IP (required), Source (Src) Port, Destination IP or Destination Host or URL (required), Destination Port (required if only
Destination IP or Destination Host is present), Action, and map them to the required field from Skope IT. For example, if the Source IP is in column 6, select column 6 from the dropdown list for the Source IP. Do this for all fields you want to map.
When finished, click
Next
.
Click
Test
to process your log file. The results display on the tabs at the bottom of the page.
Click
Finish
, enter a name for your custom parser, and then click
Save
.
Tip
Keep this Create Custom Parser window open if you want to create a Transformation Rule, which is explained in
Transformation
.
Timestamp Format Codes
Format Code
Description
Example
%a
Day of the week as locale’s abbreviated name
Wed
%A
Day of the week as locale’s full Name
Wednesday
%w
Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
3 for Wednesday
%d
Day of the month as a zero-padded decimal number
25
%b
Month as a locale’s abbreviated name
Dec
%B
Month as a locale’s full name
December
%m
Month as a zero-padded decimal number
12
%y
The year without the century as a zero-padded decimal number
15 or 2015
%Y
The year with the century as a decimal number
2015
%H
Hours on a 24-hour clock as a zero-padded decimal number
18
%I
Hours on a 12 hour clock
06
%p
Locale’s equivalent of AM or PM
PM
%M
Minutes as a zero-padded decimal number
15
%S
Seconds as a zero padded decimal number
30
%f
Microsecond as a decimal number, zero-padded on the left
000000
%z
UTC offset in the form +HHMM or -HHMM (empty string if the object is naive)
-0800
%Z
Timezone name like GMT( empty string if naive)
PST
%j
Day number of the year from the first of Jan as a zero-padded decimal number
359
%U
Week number of the year as a zero-padded number. All days in the first week preceding the first Sunday are considered to be week 0
51
%W
Week number of the year as a zero-padded number. All days in the first week preceding the first Monday are considered to be week 0
02 (a zero-padded number for single digit weeks) or 36
%c
Locale’s appropriate date and time representation
Wed Dec 25 18:15:30 2015
%x
Locale appropriate date
12/25/15
%X
Locale appropriate time
18:15:30
Create a Custom Header
Transformation
Key-Value Log Type
In this Topic
Configure a Custom Log Parser

---
## Discover Operational Technology in Device Intelligence
**URL:** https://docs.netskope.com/en/discover-operational-technology-in-netskope-iot-security/
**Last Modified:** 2025-08-31T01:47:50+00:00
**Scraped:** 2026-08-10T07:31:05.836008+00:00

Discover Operational Technology in Device Intelligence - Netskope Technical Documentation
Discover Operational Technology in Device Intelligence
Device Intelligence supports the discovery and security of devices in the operational technology (OT) network. The solution provides visibility into various OT activities seen in the network like cold restart, write variable, etc.
Note
This is a controlled General Availability feature. Contact your Netskope sales representative/support to enable this feature for your tenant.
Operational technology is hardware and software that detects or causes a change, through direct monitoring and/or control of industrial equipment, assets, processes and events. Industrial control systems (ICS) are a major segment of the operational technology sector. It comprises systems that are used to monitor and control industrial processes.
Industrial control systems (ICS) are often managed via a Supervisory Control and Data Acquisition (SCADA) system that provides a graphical user interface for operators to observe the status of a system.
Device Intelligence is an agent-less, non-intrusive solution that provides visibility of the devices and reduces the risk in the environment. In the OT network, the solution uses OT DNP3 and Modbus protocol traffic to discover SCADA devices like Master, Outstation, etc. Hyper-context is the device information that is defined for the discovered devices like, IP address, host name, make, model, OS, function, levels, etc. Device Intelligence categorizes the devices into three verticals, as enterprise, medical and industrial. Communication between the OT devices is captured as
activities
log.
In this Topic
Discover Operational Technology in Device Intelligence

---
## How to View “Netskope Audit Log Permissions – Read and Create” in Salesforce Profiles
**URL:** https://docs.netskope.com/en/how-to-view-netskope-audit-log-permissions-read-and-create-in-salesforce-profiles/
**Last Modified:** 2025-09-01T12:32:33+00:00
**Scraped:** 2026-08-10T07:32:36.118702+00:00

How to View “Netskope Audit Log Permissions – Read and Create” in Salesforce Profiles - Netskope Technical Documentation
How to View “Netskope Audit Log Permissions – Read and Create” in Salesforce Profiles
Once you have installed the Netskope Audit Reports App, you can create a custom view in Salesforce to identify the profiles that leverage the Netskope Audit Report app. With this view, the customer can identify the profiles that will trigger an audit event in the Netskope UI.
To create a custom view, follow the instructions below:
Log in
https://login.salesforce.com/
as an administrator.
On the top-right, click the
Gear icon > Setup
.
On the left navigation bar, go to
Administration > Users > Profiles
.
Beside the
All Profiles
dropdown list, click
Create New View
.
Under
Step 1 > View Name
, enter
Netskope Audit View
.
Under
Step 3 > Search
dropdown list, select
Object Permissions
and under
Available Settings
, select
Netskope Audit Log: Read
&
Netskope Audit Log: Create
.
Click
Save
.
On the
Profiles
page, click the
All Profiles
dropdown list and select
Netskope Audit View
.
Profiles will be listed along with the Netskope Audit Log: Read and Netskope Audit Log: Create permissions. The profiles that are ticked will trigger audit events in the Netskope UI.
In this Topic
How to View “Netskope Audit Log Permissions – Read and Create” in Salesforce Profiles

---
## How to Assign “Netskope Audit Log Permissions - Read and Create” to Salesforce Profiles
**URL:** https://docs.netskope.com/en/how-to-assign-netskope-audit-log-permissions-read-and-create-to-salesforce-profiles/
**Last Modified:** 2025-09-01T12:32:34+00:00
**Scraped:** 2026-08-10T07:32:37.300045+00:00

How to Assign “Netskope Audit Log Permissions - Read and Create” to Salesforce Profiles - Netskope Technical Documentation
How to Assign “Netskope Audit Log Permissions - Read and Create” to Salesforce Profiles
How to Assign “Netskope Audit Log Permissions – Read and Create” to Salesforce Profiles
Important
Netskope audit log permissions do not apply to the following profiles in Salesforce – Customer Portal, Customer Portal Manager, High Volume Customer Portal, Authenticated Website, Partner, and standard profiles.
Once you have installed the Netskope Audit Reports App, you can assign the Netskope Audit Log: Read and Netskope Audit Log: Create permissions to other Salesforce profiles too. To do so:
Log in
https://login.salesforce.com/
as an administrator.
On the top-right, click the
Gear icon > Setup
.
On the left navigation bar, go to
Administration > Users > Profiles
.
On the
Profiles
page, click the
All Profiles
dropdown list and select
Netskope Audit View
.
Profiles will be listed along with the Netskope Audit Log: Read and Netskope Audit Log: Create permissions. The profiles that are ticked will trigger audit events in the Netskope UI.
Select the checkbox beside
Action
.
Hover the mouse under
Netskope Audit Log: Read
for one of the profile names and double click the pencil icon.
The
Edit Netskope Audit Log: Read
window opens. Select the
Change the following setting: Netskope Audit Log: Read checkbox
and under
Apply changes to
, select
All 37 selected records
. Click
Save
.
Important
Netskope audit log permissions do not apply to the following profiles in Salesforce – Customer Portal, Customer Portal Manager, High Volume Customer Portal, Authenticated Website, Partner, and standard profiles.
Follow steps 5-7 for
Netskope Audit Log: Create
permission.
Ensure that the profile has the read and edit access for Netskope Audit Log. To do so:
On the left navigation bar, go to
Administration > Users > Profiles
.
On the
Profiles
page, click the
All Profiles
dropdown list and select
Netskope Audit View
.
Click all the profiles that have the Netskope Audit Log: Read or Create permission.
Note
You must follow steps c-f for each profile that has the Netskope Audit Log: Read or Create permission.
Scroll down to the
Custom Field-Level Security
section and click
View
beside
Netskope Audit Log
.
If the
Edit Access
checkboxes are not checked for all the field names, click
Edit
and under
Edit Access
select all the checkboxes. On selecting the
Edit Access
checkboxes, the
Read Access
checkboxes get selected too.
Important
You cannot select the
Edit Access
checkbox for
Created By
and
Last Modified By
fields.
Click
Save
.
In this Topic
How to Assign “Netskope Audit Log Permissions - Read and Create” to Salesforce Profiles

---
## Key-Value Log Type
**URL:** https://docs.netskope.com/en/key-value-log-type/
**Last Modified:** 2025-08-31T01:50:06+00:00
**Scraped:** 2026-08-10T07:33:07.174178+00:00

Key-Value Log Type - Netskope Technical Documentation
Key-Value Log Type
The key value log type has each field description within the field.
To create a log parser for key values:
On the Test/Create page, click
Create Custom Parser
.
On the Upload page, click
Select File
. Go to and select a log file, and then click
Upload
.
On the Preparation page, go to the Format tab. Select Key-Value for the Log File Type, and then click
Next
.
On the Extraction page, go to the Structure tab. Select comma from the Key-Value Delimiter dropdown list, and then select equal sign from the Separator For Key Value Fields. When finished, click
Next
.
On the Timestamp tab, enter a value, like Column 1, for the Timestamp Maps To field. Next, enter a Timestamp Format.
On the Fields tab, select an option for the Source IP (required), Source (Src) Port, Destination IP, Destination Port, Action,, and map them to the required field from Skope IT. For example, if the Source IP is in column 6, select column 6 from the dropdown list for the Source IP. Do this for all fields you want to map.
When finished, click
Next
.
Click
Test
to process your log file. The results display on the tabs at the bottom of the page.
Click
Finish
, enter a name for your custom parser, and then click
Save
.
In this Topic
Key-Value Log Type

---
## Upload Logs from Mac or Linux using SFTP
**URL:** https://docs.netskope.com/en/upload-logs-from-mac-or-linux-using-sftp/
**Last Modified:** 2025-08-31T01:50:04+00:00
**Scraped:** 2026-08-10T07:37:11.380304+00:00

Upload Logs from Mac or Linux using SFTP - Netskope Technical Documentation
Upload Logs from Mac or Linux using SFTP
Make sure your log files have the
.log
extension. If using an archive (zip), you can only have one log file per archive.
Download the private key from the Netskope Administrator interface.
You may need to change permissions of the private key file to restrict access. Enter this command to change permissions of the downloaded private key file:
chmod 600 customer_sshkey.key
Launch a terminal window and establish an SFTP connection to the Appliance IP
cd upload
Address, specifying the directory where the downloaded private key resides. Next enter this command using the username provided in the Admin UI on the
Log > Upload
page:
sftp -i /privatekey/customer_sshkey.key nstransfer@
<appliance IP address>
When connected, go to the
upload
directory (). Next, go to the directory for the device used for generating the log file in the first step. For example, if using Cisco IronPort, you would need to use the
cisco-wsa
directory (
cd cisco-wsa
). If using Blue Coat logs, go to ‘
proxysg-http-main
‘ (
cd proxysg-http-main
).
Upload the log file(s) using the
mput
command (
mput /logs/cisco-ironport.log
)
After the logs are uploaded, it will take some time for the system to parse the logs and show events in Skope IT. The larger the log files, the more time it will take.
In this Topic
Upload Logs from Mac or Linux using SFTP

---
## Upload Logs from Windows using SFTP
**URL:** https://docs.netskope.com/en/upload-logs-from-windows-using-sftp/
**Last Modified:** 2025-08-31T01:50:03+00:00
**Scraped:** 2026-08-10T07:37:13.747234+00:00

Upload Logs from Windows using SFTP - Netskope Technical Documentation
Upload Logs from Windows using SFTP
Make sure your log files have the
.log
extension. If using an archive (zip), you can only have one log file per archive.
You will need an SFTP client. If you are familiar with using private key files and/or have another PSFTP client, you can skip to step 5 below. To download a SFTP client, go to
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
and download the following files:
PSFTP: PuTTY SFTP client
PuTTY gen: PuTTY key generator
Download the private key from the Netskope tenant UI under
Settings > Risk Insights > Log > Upload
.
After you have the private key, you need to convert it to a format that PuTTy understands. To do this, launch the file
puttygen.exe
and click the Load button to select the private key file downloaded from the Netskope Administrator UI in step 3 above. Next click the Save Private Key button to convert the key file to a
.ppk
file that can be used for the PuTTY SFTP client. Remember the location for this key since we will need it in the next step.
From a command prompt, change to the directory where the converted
.ppk
key file resides, and then enter this command using the username provided in the Admin UI on the
Log > Upload
page:
psftp -i customerprivatekey.ppk nstransfer@
<appliance IP address>
When connected, go to the
upload
directory (
cd upload
). Next, go to the directory for the device used for generating the log file in the first step.
For example, if using Cisco IronPort, you would need to use the
cisco-wsa
directory (
cd cisco-wsa
).
If using Blue Coat logs, you would need to use the
proxysg-http-main
directory (
cd proxysg-http-main
).
If using a custom parser, use the directory named
custom-
<custom parser name>
, where
<custom parser name>
is the name on the Custom Tab in the Upload Log File dialog box in the Netskope UI (
Settings > Risk Insights > Log > Upload > Upload Logs
). In this case, the directory name would be
custom-test_1_parser
.
Upload the log file(s) using the
mput
command (
mput /logs/cisco-ironport.log
)
After the logs are uploaded, it will take some time for the system to parse the logs and show events in Skope IT. The larger the log files, the more time it will take.
In this Topic
Upload Logs from Windows using SFTP

---
## Upload Logs to the Netskope Cloud
**URL:** https://docs.netskope.com/en/upload-logs-to-the-netskope-cloud/
**Last Modified:** 2025-08-31T01:50:01+00:00
**Scraped:** 2026-08-10T07:37:14.916827+00:00

Upload Logs to the Netskope Cloud - Netskope Technical Documentation
Upload Logs to the Netskope Cloud
You can upload the log files from your enterprise web proxy, next generation firewall, and other devices directly to your tenant instance in the Netskope cloud either from the Netskope tenant UI or using SFTP.
Upload Logs to the Netskope Tenant UI
Upload Logs from Windows using SFTP
Upload Logs from Mac or Linux using SFTP
In this Topic
Upload Logs to the Netskope Cloud

---
## Action Logs
**URL:** https://docs.netskope.com/en/user-risk-exchange-action-logs/
**Last Modified:** 2026-02-05T19:31:52+00:00
**Scraped:** 2026-08-10T07:39:25.730193+00:00

Action Logs - Netskope Technical Documentation
Action Logs
Action logs are logs of actions performed on users or hosts. A write-access user can view and filter through action logs to view actions taken.
Go to
User Risk Exchange > Action Logs
.
The logs indicate the business rule which triggered the action and the time when this action was performed.
Clicking on any values in the Email/ID column will redirect to that record on Users/Hosts page.
In this Topic
Action Logs

---
## AWS CloudTrail Lake Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/aws-cloudtrail-lake-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:43:40+00:00
**Scraped:** 2026-08-10T07:39:30.495462+00:00

AWS CloudTrail Lake Plugin for Log Shipper - Netskope Technical Documentation
AWS CloudTrail Lake Plugin for Log Shipper
This document explains how to configure the AWS Cloudtrail Lake plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This integration allows ingestion of Netskope events and alerts into your CloudTrail event data store.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
The AWS account used must have access to the CloudTrail beta APIs.
Connectivity to the following host:
aws.amazon.com
.
CloudTrail Plugin Support
Event Support
Yes
Alert Support
Yes
WebTx Support
No
Workflow
Get your AWS Credentials and Create a Channel ARN.
Configure the AWS CloudTrail Lake Plugin.
Configure Log Shipper Business Rules for AWS CloudTrail Lake.
Configure Log Shipper SIEM mappings for AWS CloudTrail Lake.
Validate the AWS CloudTrail Lake plugin.
Click play to watch a video:
Get your AWS Credentials and Create a Channel ARN
You need your AWS credentials and Channel ARN to configure the CloudTrail Lake plugin.
Get your Access Key ID and Secret Access Key
Log in to AWS Console.
Click on the username (top right corner) and go to
Security Credentials
.
Click
Create Access Key
.
Copy the Access Key ID and Secret access key.
Create a Channel ARN
Log in to your AWS CloudTrail Console.
Go to
CloudTrail > Lake > Integrations
and click on
Add Integrations
.
Enter a name for the channel.
Select
Netskope
from the source dropdown.
For the delivery location, select
Create new event data store
, and enter a name. Select the Retention period.
In the Resource Policy, select
Add AWS account
to specify an AWS account ID to add as a principal in the policy (The accounts defined as principals in the resource policy can call the
PutAuditEvents
API to deliver events to your channel).
Add tags as required (Tags are used for managing the resources).
Click
Add integration.
Copy the value of Channel ARN.
Required Permissions
The user or role that you use to work with open audit events must have permissions to call the
PutAuditEvents
API. Apply a policy with the following permissions to the role. This policy statement allows access to create, manage, and delete event data stores in CloudTrail Lake, run and view queries and results, and load open audit events into CloudTrail.
Replace the
<Channel ARN>
with your Channel ARN.
{
    "Version":"2012-10-17",
    "Statement":[
       {
          "Effect":"Allow",
          "Action":"cloudtrail-data:PutAuditEvents",
          "Resource":"
<Channel ARN>
"
       }
    ]
 }
Configure the AWS CloudTrail Lake Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Click on the AWS CloudTrail Lake plugin box.
Enter and select these values:
Configuration Name: Unique name for the configuration.
Mapping: Select a valid Mapping. A Default Mapping for all plugins are available.
Use System Proxy: Enable if proxy is required for connectivity.
Transform the raw logs: For AWS CloudTrail Lake Plugin, this toggle needs to be always enabled.
Click
Next
.
Enter and select these values:
AWS Access Key ID (Public Key): AWS Access Key ID obtained previously.
AWS Secret Access Key (Private Key): AWS Secret Access Key obtained previously.
Channel ARN: Enter the Channel ARN obtained previously.
Add Additional Data: Whether to send unmapped fields as additional event data to the CloudTrail event data store or not.
Click
Save
.
Configure a Log Shipper Business Rule for AWS CloudTrail Lake
Go to
Log Shipper > Business Rules
.
Click
Create New Rule
.
Note
If you want all the events and alerts ingested into your SIEM Mapping, you can use the default ALL rule.
Enter a Rule Name and configure a query for business rules based on your requirement; when finished, click
Save
.
Configure a Log Shipper SIEM Mapping for AWS CloudTrail Lake
SIEM mapping enables the user to ingest the Netskope logs (alerts and events) to the third-party platform.
Note
Data ingestion to the third-party SIEM server will only start if the user has added SIEM Mappings.
Go to
Log Shipper > SIEM Mappings
.
Click
Add SIEM Mappings
.
Select the Source (Netskope plugin) and Destination (AWS CloudTrail Lake) plugins, and then select a Business Rule from the dropdown list.
Click
Save
.
Validate the AWS CloudTrail Lake Plugin
To validate that if the events has been pulled, transformed, and ingested from Cloud Exchange to CloudTrail Lake, you can check in Cloud Exchange and AWS CloudTrail Lake.
Cloud Exchange
Log in to Cloud Exchange.
Go to
Logging
.
Filter using a message contains
<<plugin_configuration_name>>
.
AWS Console
Log in to the AWS Console.
Go to
Cloud Trail > Lake
. Click on the
Editor
tab.
Copy the
Event data store ID
.
Enter this query (replace the
<EVENT DATA STORE ID>
with the previously copied ID, and the
<DATE TIME>
with your desired date time. Events created after this date time will be shown.) in the editor and click
Run
.
SELECT eventData FROM
<EVENT DATA STORE ID>
WHERE eventtime >='DATE TIME’
For example:
SELECT eventData FROM 58cfe6e1-093c-45da-a837-990bca613536 WHERE eventtime >='2022-07-14 18:00:00'
You can also filter results for a specific event/audit time with the following query (replace
<EVENT DATA STORE ID>
with your event data store ID and
<DATA_TYPE>
and
<SUB_TYPE>
with Netskope’s data type and subtype that you want to search.
SELECT * FROM
<EVENT DATA STORE ID>
WHERE eventData.eventSource = ‘netskope
<DATA_TYPE>
.
<SUB_TYPE>
’
For example:
SELECT * FROM 58cfe6e1-093c-45da-a837-990bca613536 WHERE eventData.eventSource = ‘netskopeevent.audit’
Scroll down to see the ingested events in the Query results tab.
Known Limitation for the AWS CloudTrail Lake Plugin
Alerts of the type
UBA
will not be ingested to AWS CloudTrail Lake event data store as it is not supported by the Source Destination
Netskope
present in the AWS CloudTrail Lake.
Troubleshooting the AWS CloudTrail Lake Plugin
If multiple alerts and events have the same ID, those alerts and events will not be ingested as Duplicate event IDs are not allowed in the event data stores.
In this Topic
AWS CloudTrail Lake Plugin for Log Shipper

---
## AWS S3 Events and Alerts Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/aws-s3-events-alerts-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:44:39+00:00
**Scraped:** 2026-08-10T07:39:35.552614+00:00

AWS S3 Events and Alerts Plugin for Log Shipper - Netskope Technical Documentation
AWS S3 Events and Alerts Plugin for Log Shipper
This document explains how to configure the AWS S3 Events, Alerts v1.2.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to fetch Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content) and Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status) from the Netskope Tenant.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
Amazon S3 bucket permissions to the IAM user.
ListBucket
CreateBucket
ListAllMyBuckets
GetBucketPolicy
GetBucketPublicAccessBlock
PutEncryptionConfiguration
PutBucketPublicAccessBlock
PutBucketPolicy
GetBucketLocation
PutObject
Connectivity to the following hosts: AWS S3 Bucket access.
AWS S3 Events, Alerts Plugin Support
This plugin is used to fetch Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content) and Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status) from the Netskope Tenant.
Data Type
Description
Event Support
Yes: Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status
Alert Support
Yes: DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content
WebTx Support
No
Permissions
Amazon S3 bucket permissions to the IAM user to send Events and Alerts data to buckets.
ListBucket
CreateBucket
ListAllMyBuckets
GetBucketPolicy
GetBucketPublicAccessBlock
PutEncryptionConfiguration
PutBucketPublicAccessBlock
PutBucketPolicy
GetBucketLocation
PutObject
API Details
List of APIs Used
This plugin uses Python libraries to create file objects in AWS S3.
Library
: The AWS SDK for Python (Boto3)
Usage: The AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
Create a Client
s3_client = boto3.client(
"s3",
aws_access_key_id=self.aws_public_key,
aws_secret_access_key=self.aws_private_key,
aws_session_token=self.aws_session_token,
region_name=self.region_name,
config=Config(proxies=self.proxy, user_agent=self.useragent),
)
Create a Bucket
bucket = s3_client.create_bucket(
Bucket=bucket_name,
CreateBucketConfiguration=location,
)
Upload to File to the Bucket
s3_client.upload_file(
file_name,
bucket_name,
object_name,
)
Get an AWS Resource
s3_resource = boto3.resource(
"s3",
aws_access_key_id=self.aws_public_key,
aws_secret_access_key=self.aws_private_key,
region_name=self.region_name,
config=Config(proxies=self.proxy, user_agent=self. user-agent),
)
Performance Matrix
This performance reading is for a Large Stack CE tested on these VM specifications. These readings are added with the consideration that it will ingest around 10K file size in 30 seconds.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Events, Alerts ingested to third-party SIEM
~ 200K EPM
User Agent
User-Agent: APN/1.1 (ahq9d89xj9gspapczzdb59goq)
Workflow
Generate required credentials for AWS S3 bucket access.
Create an S3 Bucket and Policy.
Generate Private Key, Certificate Body, Password Phrase, Profile ARN, Role ARN, Trust Anchor ARN if using AWS IAM Role Anywhere.
Configure the AWS S3 Events, Alerts plugin.
Configure Log Shipper Business Rules for the AWS S3 Events, Alerts plugin.
Configure Log Shipper SIEM mappings for the AWS S3 Events, Alerts plugin.
Validate the AWS S3 Events, Alerts plugin.
Watch a Video
Click play to watch a video.
Create AWS S3 Source Bucket
This bucket will be used in the AWS S3 Source Bucket configuration parameter while configuring the plugin.
To Create a Bucket and Set the required policies, log in to the AWS console.
From
All Services
, select
S3
or search for
S3
in the search bar.
Click
Create Bucket
.
Enter Bucket Name, scroll down, and click
Create Bucket
. Example:
netskope-ce-source-bucket
.
Search for your bucket and click on the bucket name to open it.
Click
Permissions
to open the permission tab and to set the policy.
Click
Edit
in the
Block public access (bucket settings)
section. Uncheck all checkboxes and click
Save Changes
. You’ll be asked for confirmation; confirm it and click
Confirm
.
Under the
Permissions
tab in the bucket, click
Edit
in the
Bucket Policy
section.
Click
Policy generator
.
Select
S3 Bucket policy
as the policy type, add statement details, and generate the policy:
Replace the
<user-arn>
with the user ARN used for accessing the source bucket and
<bucket-name>
with the source bucket created above. Sample
<user-arn>
: arn:aws:iam::7111xxxxxxxx:user/xxxxxxxx, and
<bucket-name>
: netskope-ce-source-bucket
Select Type of Policy: S3 Bucket Policy
Effect: Allow
Principal:
<user-arn>
Actions:
GetBucketAcl
GetBucketPolicy
ARN: arn:aws:s3:::
<bucket-name>
Click
Add Statement
.
Scroll back up and add another statement.
Select Type of Policy: S3 Bucket Policy
Effect: Allow
Principal:
<user-arn>
Actions:
PutObject
PutObjectAcl
ARN: arn:aws:s3:::
<bucket-name>
/*
Click
Add Statement
.
Click
Generate Policy
. Make sure to copy the policy generated in this step because it will be used in the next step to attach in the source bucket.
Add this policy to the Textbox. Scroll to the bottom and click
Save Changes
.
Create a Bucket Policy
Search for
IAM
in the search box, and in the left panel, click
Policies
.
Click
Create Policy
.
On the
JSON
tab, enter this policy. Click
Next: Tags
, and click
Next: Review
.
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": [
"s3:GetBucketPublicAccessBlock",
"s3:PutEncryptionConfiguration",
"s3:PutBucketPublicAccessBlock",
"s3:ListAllMyBuckets",
"s3:PutBucketPolicy",
"s3:CreateBucket",
"s3:ListBucket",
"s3:GetBucketPolicy",
"s3:GetBucketLocation"
"s3:PutObject"
],
"Resource": "*"
}
]
}
Enter a Name and click
Create Policy
.
Attach this policy to the user. Go to
IAM > Users
and select the user for which you want to attach a policy. Click
Add permissions
, and click
Add permissions
again.
Select
Attach policies directly
under Permissions, and then search for and select the policy created in the previous step for the source queue.
Click
Next
and then click
Add permissions
. A policy will be attached to the user.
Plugin Authentication Methods
IAM Role Anywhere Configuration
Prerequisites
The
AWS Certificate Manager
service is required to be enabled to authenticate the plugin using the
AWS IAM Roles Anywhere
Authentication Method.
Note
Make sure you create the Private Certificate Authority, Trust Anchor, and Profile in the same region in which your AWS S3 Source Bucket resides.
Create an IAM Policy
This Policy contains the required permissions for creating a Private CA Certificate (including Permissions for creating a Trust Anchor and Profile) and using IAM Roles Anywhere.
Go to
Policy Generator
and click
Add Statement
to generate a policy.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Private Certificate Authority
Actions:
CreateCertificateAuthority
DescribeCertificateAuthority
GetCertificate
GetCertificateAuthorityCertificate
GetCertificateAuthorityCsr
ImportCertificateAuthorityCertificate
IssueCertificate
ListCertificateAuthorities
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management (IAM)
Actions:
AttachRolePolicy
CreateAccessKey
CreateRole
DeleteRole
PassRole
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Certificate Manager
Actions:
DescribeCertificate
ExportCertificate
GetCertificate
ListCertificates
ListTagsForCertificate
RequestCertificate
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management Roles Anywhere
Actions:
CreateProfile
CreateTrustAnchor
GetProfile
GetTrustAnchor
ListProfiles
ListTrustAnchors
ARN: *
Click
Add Statement
.
Click
Generate Policy
.
Copy the Policy as it is used in the next step for creating the policy required for creating the Private CA certificates.
Go to the AWS Console and select
IAM
from All Services. Click
Policies
from the left panel, and click
Create Policy
.
Copy the policy to the JSON tab, and then click on
Next: Tags
and
Next: Review.
.
Enter a name, like
netskope-ce-rolesAnywhere-policy
, and click
Save Changes
.
Create a Private Certificate Authority
Log in to AWS Console.
Search for
Certificate Manager
.
Click
AWS Private CA
.
Click
Create a private CA
.
Select
General-purpose
for Mode Options.
Select
Root
for CA Type Options.
Enter the Organization (O).
Select
RSA 2048
for Key Algorithm Options.
Add tags
if any (optional).
Enable the checkbox in the
CA permissions options
section.
Enable the checkbox in the
Pricing
section.
Click
Create
to create the CA certificate.
From
Actions
, select
Install
.
Click
Confirm and Install
.
Create a Trust Anchor
Search for the
IAM
service, and go to
Roles
under
Access management
. Scroll down to
Roles Anywhere
and select
Manage
.
Click
Create a Trust anchor
.
Enter the Trust anchor name, like
netskope-ce-trust-anchor
.
Select
AWS Certificate Manager Private CA
(created in the previous steps) as a Certificate authority (CA) source.
Add tags if required.
Click
Create a trust anchor
.
Click on the created Trust Anchor and copy the Trust Anchor ARN.
Create an IAM Role
Go to IAM services in the AWS Console.
Click
Role
under
Access management
.
Click
Create Role
.
For the Trusted entity type, select
Custom Trust Policy
.
Replace the Custom trust Policy with the below given Trust Policy – this policy contains the permissions for using the Roles Anywhere service:
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": [
"rolesanywhere.amazonaws.com"
]
},
"Action": [
"sts:AssumeRole",
"sts:TagSession",
"sts:SetSourceIdentity"
]
}
]
}
Click
Next
.
In the
Permissions
policies, select the previously created Bucket Policy.
Click
Next
.
Provide a Role name, like
netskope-ce-roleAnywhere
, and add a Description for the role.
Click
Create role
.
Make a note of the
Role ARN
as this will be required in the Plugin configuration parameter:
Role ARN
for the authentication method AWS IAM Roles Anywhere.
Create a Profile
Select
Roles
under
Access management
.
Scroll down to Roles Anywhere and click
Manage
.
Expand the Setup steps.
Click
Step 2: Configure roles
.
Click
Configure a profile
.
Enter a Profile name, like
netskope-ce-profile
.
Select the role created in
Create IAM Role
section (
netskope-ce-roleAnywhere
).
Remove the
Inline Policy
.
Click
Create profile
.
Click on the created Profile and copy the Profile ARN.
Request a Private Certificate
Go to
AWS Certificate Manager > Request certificate
.
Select
Request a private certificate
.
Click
Next
.
Select the Certificate authority created in the previous steps.
Provide a domain name in the Fully Qualified Domain Name field, like
netskope-ce.com
.
Select
RSA 2048
for the Key algorithm.
Add tags if required.
Acknowledge the Certificate renewal permissions.
Click
Request
.
Go to
List certificates
from the navigation pane of AWS Certificate Manager.
Select the certificate created previously.
Click
Export
.
Enter the
passphrase.
Make a note of the passphrase as it will be required for the Configuration of the AWS S3 Plugin using the
AWS IAM Roles Anywhere
Authentication method.
Click
Generate PEM Encoding
.
Download all the
Certificates
because they won’t be visible again. For new certificates, you will need to Export it again. For More Info visit
AWS IAM Role Anywhere
Deployed on AWS Configuration
Create a Role
Go to
IAM
services in the AWS Console.
Click
Create role
.
Select the
AWS Service
.
For Use Case, select
EC2
.
Click
Next
.
Select the permission policy created in your Bucket Policy.
Click
Next
.
Enter a Role Name, like
netskope-ce-instance-role
, and add a Description.
Click
Create Role
.
Assign a Role to an EC2 Instance
Open your EC2 instance console.
Click
Instances
under
Instances
.
Go to
Action > Security > Modify IAM Role
.
Select the Role that you created previously (like
netskope-ce-instance-role
).
Click
Update IAM Role
.
Assign a Role to a Fargate Instance
Open your CFN script.
Get the
ExistingECSTaskRole
Parameter value if present.
Go to
IAM > Roles
.
Search for the
ExistingECSTaskRole
parameter value. Otherwise, search for
NetskopeCloudExchangeTaskRole-<CFN name>
and select the role.
Attach the previously created Create Bucket Policy to this role.
Click
Add permission > Attach policies
.
Search and select the bucket policy previously created (
netskope-ce-s3-policy
).
Click
Add permissions
.
Assign the Role to a K8s Instance
Open your Role created for ServiceAccount while creating K8s instance.
Attach the Bucket policy created previously.
Configure the AWS S3 Events, Alerts Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
AWS S3 Events, and Alerts v1.2.0 (CLS)
plugin box.
Enter a Configuration Name.
Click
Next
and enter the Configuration Parameters:
Authentication Method
:
Select the method to be used for authentication (Deployed on AWS/AWS IAM Roles Anywhere)
Private Key:
Private Key for decrypting the AWS Private CA Certificate. Required for AWS IAM Roles Anywhere authentication type.
Certificate Body:
Certificate Body for AWS Public/Private CA Certificate. Required for AWS IAM Roles Anywhere authentication type.
Password Phrase:
Password Phrase for decrypting the CA Certificate. Required for AWS IAM Roles Anywhere authentication type.
Profile ARN:
AWS Profile ARN for AWS client authentication. Required for AWS IAM Roles Anywhere authentication type
.
Role ARN:
AWS Role ARN for AWS client authentication. Required for AWS IAM Roles Anywhere authentication type.
Trust Anchor ARN:
AWS Trust Anchor ARN for AWS client authentication. Required for AWS IAM Roles Anywhere authentication type.
AWS S3 Bucket Region Name:
AWS S3 Bucket Region Name from where to get the AWS S3 Bucket. Make sure that the region name matches the region in the Profile ARN and Trust Anchor ARN.
AWS S3 Bucket Name:
AWS S3 Bucket Name in which the data object will be stored.
Click
Save
. Your plugin configuration will be available on the
Cloud Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for AWS S3 Events, Alerts
In Log Shipper, go to the
Business Rules
.
By default there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
Click
Save
.
Configure a SIEM Mapping for AWS S3 Events, Alerts
Go to
SIEM Mappings
and click
Add SIEM Mapping
.
Select the Source plugin (Netskope CLS), the Destination plugin (AWS S3 Events, Alerts), your business rule, and click
Save
.
After the SIEM mapping is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the AWS platform.
Validate the AWS S3 Events, Alerts Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant.
Go to
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow, on Netskope Cloud Exchange.
Go to
Logging
and search for ingested events with the filter
“message contains ingested”
.
The ingested logs will be filtered.
To validate the push from the AWS S3 platform:
Go to AWS S3. On the Search bar, search for and select
Buckets
.
Search the bucket you used while creating the plugin.
Click on the bucket name.
Note
The folder structure will be like alerts/feedname/year/month/day/hour/filename.gz
Example:
awsdemobucket/alerts/feedname=Malware/year=2023/month=11/day=30/hour=9/1701336881_139977276685128.txt
After downloading the file, the alert/event will look like this:
Troubleshooting the AWS S3 Events, Alerts Plugin
Facing issues in the existing plugin configuration after the plugin update
If you’ve recently updated your AWS S3 plugin, there might be an issue where editing the existing plugin configuration leads to a blank Cloud Exchange interface. This problem may occur in Cloud Exchange versions 4.2.0 and 5.0.0 if users try to modify the plugin configuration after the update and navigate to the Configuration Parameters page.
Here’s what you can do on your Cloud Exchange version:
For version 4.2.0, 5.0.0: The only solution available is to delete the current plugin configuration and set up a new one from scratch.
Facing issues while configuring the new plugin
If you’re creating a new plugin with AWS IAM Roles Anywhere and face an error of 400, the root cause for not being able to save the plugin can be found in the logging section when expanding the logs
What to do
:
While expanding the log, you can see
At least one of the Trust Anchor ARN, Role ARN, and Profile ARN has a different account ID
, so you would have to check that the provided parameters are generated from the same account and have the same region.
In this Topic
AWS S3 Events and Alerts Plugin for Log Shipper

---
## AWS S3 WebTx Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/aws-s3-webtx-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:30:02+00:00
**Scraped:** 2026-08-10T07:39:37.995710+00:00

AWS S3 WebTx Plugin for Log Shipper - Netskope Technical Documentation
AWS S3 WebTx Plugin for Log Shipper
This document explains how to configure the AWS S3 WebTx plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin allows pushing web transactions data into AWS S3 buckets.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope LogStreaming
or
Azure Netskope LogStreaming
plugin already configured.
AWS S3 credentials with create/read/write buckets permissions. Obtain your AWS S3 Access key ID and Secret Access Key with permission to read/write on specific buckets or permission to create buckets before proceeding.
Amazon S3 bucket permissions to the IAM user.
ListBucket
CreateBucket
ListAllMyBuckets
GetBucketPolicy
GetBucketPublicAccessBlock
PutEncryptionConfiguration
PutBucketPublicAccessBlock
PutBucketPolicy
Note
Verify your bucket permissions are secure and not set up for open public access. Only allow access to your cloud storage instance from your Cloud Exchange Host and any other addresses that need access.
AWS S3 WebTx Plugin Support
The AWS S3 WebTx plugin support is:
Data Type
Support
Events
No
Alerts
No
WebTx
Yes  (via Netskope LogStreaming)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope LogStreaming
or
Azure Netskope LogStreaming
plugin.
Permissions
Amazon S3 bucket permissions to the IAM user to send WebTx (via Netskope LogStreaming) data to buckets.
API Details
List of APIs Used
This plugin uses Python libraries to create file objects in AWS S3.
Library: The AWS SDK for Python (Boto3)
Usage: The AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
Create the Client
s3_client = boto3.client(
                "s3",
                aws_access_key_id=self.aws_public_key,
                aws_secret_access_key=self.aws_private_key,
                aws_session_token=self.aws_session_token,
                region_name=self.region_name,
                config=Config(proxies=self.proxy, user_agent=self.useragent),
              )
Create a Bucket
bucket = s3_client.create_bucket(
               Bucket=bucket_name,
               CreateBucketConfiguration=location,
             )
Upload a File into the Bucket
s3_client.upload_file(
                file_name,
                bucket_name,
                object_name,
            )
Get an AWS Resource
s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=self.aws_public_key,
                aws_secret_access_key=self.aws_private_key,
                region_name=self.region_name,
                config=Config(proxies=self.proxy, user_agent=self.useragent),
            )
User Agent
The user-agent added in this plugin is in the following format
netskope-ce-
<ce_version>
-
<module>
-
<plugin_name>
-v
<plugin_version>
For example:
Netskope-ce-5.0.0-cls-aws_s3_webtx-v1.2.0
Workflow
Create a bucket, a bucket policy, and configure an authentication method.
Configure the AWS S3 WebTx plugin.
Configure Log Shipper Business Rules for AWS S3 WebTx.
Configure Log Shipper Log Delivery for AWS S3 WebTx.
Validate the AWS S3 WebTx plugin.
Click play to watch a video.
Create an AWS S3 Bucket and Bucket Policy
Create an AWS S3 Bucket
To create bucket and set required policies, go to your AWS console and log in.
From All Services, select
S3
.
Click
Create Bucket
.
Enter a Bucket Name, scroll to the bottom, and click
Create Bucket
.
Search for your bucket and click on the bucket name to open it.
Click on
Permission
to open the permission tab and to set a policy.
Click
Edit
. Under Block public access (bucket settings), uncheck all checkboxes and click
Save Changes
. When prompted for a confirmation, confirm it, and then click
Confirm
.
Under the
Permissions
tab, click
Edit
in the Bucket Policy section.
Click
Policy Generator
.
Select
S3 Bucket Policy
as policy type for Step 1, and
Add Statement
details for Step 2, and then click
Generate Policy
.
Select Type of Policy: S3 Bucket Policy
Effect: Allow
Principal:
<user-arn>
Actions:
GetBucketAcl
GetBucketPolicy
ARN:
arn:aws:s3:::
<bucket-name>
Click
Add Statement
.
Select Type of Policy: S3 Bucket Policy
Effect: Allow
Principal:
<user-arn>
Actions:
PutObject
PutObjectAcl
ARN:
arn:aws:s3:::
<bucket-name>
/*
. Be sure to add
/*
after the second bucket name.
Click
Add Statement
Click
Generate Policy
. Make sure to copy the policy generated in this step as it will be used in the next step to attach in the source bucket.
Add this policy to this textbox.
{
    "Id": "<policy ID>",
    "Version": "<version>",
    "Statement": [
        {
            "Sid": "<statement ID>",
            "Action": [
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::<bucket-name>",
            "Principal": {
                "AWS": [
                    "<user-arn>"
                ]
            }
        },
        {
            "Sid": "<statement ID>",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::<bucket-name>/*",
            "Principal": {
                "AWS": [
                    "<user-arn>"
                ]
            }
        }
    ]
}
Scroll to the bottom and click
Save Changes
.
Create a Bucket Policy
A Policy is required for accessing the source bucket by the plugin.
Go to
Policy Generator
.
Replace the
<bucket-name>
with the AWS S3 Source Bucket created previously. (
netskope-ce-source-bucket
).
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: Amazon S3
Actions: ListAllMyBuckets
ARN:
*
Click
Add Statement
.
Scroll back up and add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: Amazon S3
Actions:
GetBucketAcl
GetBucketPolicy
GetBucketLocation
ARN:
arn:aws:s3:::<bucket-name>
Click
Add Statement
.
Scroll back up and add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: Amazon S3
Actions:
PutObject
PutObjectAcl
ARN:
arn:aws:s3:::<bucket-name>
Click
Add Statement
.
Click
Generate Policy
. Make sure to copy the policy generated in this step as it will be used in the next step to create a policy that will be attached to the user for accessing the source bucket.
Go to AWS Console and select
IAM
from
All Services
.
Click
Policies
in the left panel, and then click
Create Policy
.
Paste the policy created in the previous step to the JSON tab, and then click
Next:Tags
and
Next:Review
.
Enter a name (like
netskope-ce-s3-policy
).
Click
Create Policy
.
Attach this policy to the user following these steps:
Go to
IAM > Users
. Select the user on which you want to attach a policy, and click
Add permissions
, and then click
Add permissions
from the dropdown.
Select
Attach policies directly
under Permissions, and then search for and select the policy created in the previous step (
netskope-ce-s3-policy
).
Click
Next
and then click
Add permissions
. A Policy will be attached to the user.
Plugin Authentication Methods
IAM Role Anywhere Configuration
Prerequisites
The
AWS Certificate Manager
service is required to be enabled to authenticate the plugin using the
AWS IAM Roles Anywhere
Authentication Method.
Note: Make sure you create the Private Certificate Authority, Trust Anchor, and Profile in the same region in which your AWS S3 Source Bucket resides.
Create an IAM Policy
This Policy contains the required permissions for creating a Private CA Certificate (including Permissions for creating a Trust Anchor and Profile) and using IAM Roles Anywhere.
Go to
Policy Generator
and click
Add Statement
to generate a policy.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Private Certificate Authority
Actions:
CreateCertificateAuthority
DescribeCertificateAuthority
GetCertificate
GetCertificateAuthorityCertificate
GetCertificateAuthorityCsr
ImportCertificateAuthorityCertificate
IssueCertificate
ListCertificateAuthorities
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management (IAM)
Actions:
AttachRolePolicy
CreateAccessKey
CreateRole
DeleteRole
PassRole
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Certificate Manager
Actions:
DescribeCertificate
ExportCertificate
GetCertificate
ListCertificates
ListTagsForCertificate
RequestCertificate
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management Roles Anywhere
Actions:
CreateProfile
CreateTrustAnchor
GetProfile
GetTrustAnchor
ListProfiles
ListTrustAnchors
ARN: *
Click
Add Statement
.
Click
Generate Policy
.
Copy the Policy as it is used in the next step for creating the policy required for creating the Private CA certificates.
Go to the AWS Console and select
IAM
from
All Services
. Click
Policies
from the left panel, and click
Create Policy
.
Copy the policy to the JSON tab, and then click on
Next: Tags
and
Next: Review.
Enter a name, like netskope-ce-rolesAnywhere-policy, and click
Save Changes
.
Create a Private Certificate Authority
Log in to AWS Console.
Search for
Certificate Manager
.
Click
AWS Private CA
.
Click
Create a private CA
.
Select
General-purpose
for
Mode Options
.
Select
Root
for
CA type options
.
Enter the Organization (O).
Select
RSA 2048
for
Key algorithm options
.
Add tags
if any (optional).
Enable the checkbox in the
CA permissions options
section.
Enable the checkbox in the
Pricing
section.
Click
Create
to create the CA certificate.
From
Actions
, select
Install
.
Click
Confirm and Install
.
Create a Trust Anchor
Search for the
IAM
service, and go to
Roles
under
Access management
. Scroll down to
Roles Anywhere
and select
Manage
.
Click
Create a Trust anchor
.
Enter the Trust anchor name, like
netskope-ce-trust-anchor
.
Select
AWS Certificate Manager Private CA
(created in the previous steps) as a
Certificate authority (CA) source
Add tags if required.
Click
Create a trust anchor
.
Click on the created
Trust Anchor
and copy the
Trust Anchor ARN
.
Create an IAM Role
Go to IAM services in the AWS Console.
Click
Role
under
Access management
.
Click
Create Role
.
For the Trusted entity type, select
Custom Trust Policy
.
Go to
Policy Generator
.
Replace the Custom trust Policy with the below Trust Policy; this policy contains the permissions for using the roles anywhere service:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "rolesanywhere.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetSourceIdentity"
            ]
        }
    ]
}
Click
Next
.
In the
Permissions
policies, select the previously created Bucket Policy.
Click
Next
.
Provide a Role name, like
netskope-ce-roleAnywhere
, and add a Description for the role.
Click
Create role
.
Make a note of the
Role ARN
as this will be required in the Plugin configuration parameter:
Role ARN
for the authentication method
AWS IAM Roles Anywhere
.
Create a Profile
Select
Roles
under
Access management
.
Scroll down to
Roles Anywhere
and click
Manage
.
Expand the
Setup steps
.
Click
Step 2: Configure roles
.
Click
Configure a profile
.
Enter a Profile name, like netskope-ce-profile.
Select the role created in
Create IAM Role
section: netskope-ce-roleAnywhere.
Remove the
Inline Policy
.
Click
Create profile
.
Click on the created
Profile
and copy the
Profile ARN
.
Request a Private Certificate
Go to
AWS Certificate Manager > Request certificate
.
Select
Request a private certificate
.
Click
Next
.
Select the Certificate authority created in the previous steps.
Provide a domain name in the Fully qualified domain name field, like
netskope-ce.com
.
Select
RSA 2048
for the
Key algorithm
.
Add tags if required.
Acknowledge the Certificate renewal permissions.
Click
Request
.
Go to
List certificates
from the navigation pane of AWS Certificate Manager.
Select the certificate created previously.
Click
Export
.
Enter the
passphrase.
Make a note of the passphrase as it will be required for the Configuration of the AWS S3 Plugin using the
AWS IAM Roles Anywhere
Authentication method.
Click
Generate PEM Encoding
.
Download all the
Certificates
because they won’t be visible again. For new certificates, you will need to Export it again.
For More Info visit
AWS IAM Role Anywhere
Deployed on AWS Configuration
Create a Role
Go to
IAM
services in the AWS Console.
Click
Create role
.
Select the
AWS Service
.
For Use case, select
EC2
.
Click
Next
.
Select the permission policy created in your Bucket Policy.
Click
Next
.
Enter a Role Name, like netskope-ce-instance-role, and add a Description.
Click
Create Role
.
Note:
For this configuration, both Netskope instance and S3 Bucket should be in the same region.
Assign a Role to an EC2 Instance
Open your EC2 instance console.
Click
Instances
under
Instances
.
Go to
Action > Security > Modify IAM Role
.
Select the Role that you created previously (like netskope-ce-instance-role).
Click
Update IAM Role
.
Assign a Role to a Farget Instance
Open your CFN script.
Get the
ExistingECSTaskRole
Parameter value if present.
Go to
IAM > Roles
.
Search for the
ExistingECSTaskRole
parameter value. Otherwise, search for
NetskopeCloudExchangeTaskRole-<CFN name>
and select the role.
Attach the previously created Create Bucket Policy to this role.
Click
Add permission > Attach policies
.
Search and select the bucket policy previously created (netskope-ce-s3-policy).
Click
Add permissions
.
Assign the Role to a K8s Instance
Open your Role created for ServiceAccount while creating K8s instance.
Attach the Bucket policy created previously.
Configure the AWS S3 WebTX Plugin
In Cloud Exchange, go to
Settings
>
Plugin Store
.
Search for and select the
AWS S3 WebTx v1.2.0 (CLS)
plugin.
Enter a
Configuration Name
.
Click
Next
.
Enter these Configuration Parameters:
Authentication Method:
Select the method to be used for authentication (Deployed on AWS/AWS IAM Roles Anywhere)
Private Key:
Private Key for decrypting the AWS Private CA Certificate. Required for ‘AWS IAM Roles Anywhere’ authentication type.
Certificate Body:
Certificate Body for AWS Public/Private CA Certificate. Required for ‘AWS IAM Roles Anywhere’ authentication type.
Password Phrase:
Password Phrase for decrypting the CA Certificate. Required for ‘AWS IAM Roles Anywhere’ authentication type.
Profile ARN:
AWS Profile ARN for AWS client authentication. Required for ‘AWS IAM Roles Anywhere’ authentication type
.
Role ARN:
AWS Role ARN for AWS client authentication. Required for ‘AWS IAM Roles Anywhere’ authentication type.
Trust Anchor ARN:
AWS Trust Anchor ARN for AWS client authentication. Required for ‘AWS IAM Roles Anywhere’ authentication type.
AWS S3 Bucket Region Name:
AWS S3 Bucket Region Name from where to get the AWS S3 Bucket. Make sure that the region name matches the region in the Profile ARN and Trust Anchor ARN.
AWS S3 Bucket Name:
AWS S3 Bucket Name in which the data object will be stored.
Maximum File Size (in MBs):
Maximum size of WebTx data object to be stored in the bucket. (Value should be between 1 to 100.)
Maximum Duration (in Seconds):
Maximum duration after which the WebTx data object should be stored in the bucket.
Click
Save
. Your new plugin will be available on the
Cloud Log Shipper > Plugins
page.
Configure Log Shipper Log Delivery for AWS S3 WebTx
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (AWS Netskope LogStreaming or Azure Netskope LogStreaming), Destination plugin (AWS S3 WebTx), and click
Save
.
After the Log Delivery configuration is added the data will start to be pulled from the Netskope tenant, transformed, and ingested into the AWS S3 buckets.
Validate the AWS S3 WebTx Plugin
To validate the plugin workflow in Cloud Exchange.
Go to Logging and Search for ingested events with the filter “message contains ingested”.
The ingested logs will be filtered.
To validate the push from the AWS S3 platform, follow these steps:
Go to AWS S3. In the Search bar, search for and click on
Buckets
.
Search the bucket you used while creating the plugin.
Click on the bucket name.
Note:
The folder structure will be like webtx/feedversion/year/month/day/hour/filename.gz
Example:
Webtxdemobucket/webtx/feedname=2.0.0/year=2023/month=11/day=30/hour=9/1701336881_139977276685128.gz
Troubleshooting the S3 WebTx Plugin
Facing issues in the existing plugin configuration after the plugin update
If you’ve recently updated your AWS S3 plugin, there might be an issue where editing the existing plugin configuration leads to a blank CE interface. This problem may occur in CE versions 4.2.0 and 5.0.0 if users try to modify the plugin configuration after the update and navigate to the Configuration Parameters page.
Here’s what you can do on your CE version:
What to do
:
For version 4.2.0, 5.0.0: The only solution available is to delete the current plugin configuration and set up a new one from scratch.
Facing issues while configuring the new plugin
If you’re creating a new plugin with AWS IAM Roles Anywhere and face an error of 400.
The root cause for not being able to save the plugin can be found in the logging section when expanding the logs
What to do
:
Here while expanding the logger, we can see “At least one of the Trust Anchor ARN, Role ARN, and Profile ARN has a different account ID” – so we would have to check that the provided parameters are generated from the same account and have the same region.
In this Topic
AWS S3 WebTx Plugin for Log Shipper

---
## Google Chronicle Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/chronicle-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:52:35+00:00
**Scraped:** 2026-08-10T07:39:46.678280+00:00

Google Chronicle Plugin for Log Shipper - Netskope Technical Documentation
Google Chronicle Plugin for Log Shipper
This document explains how to configure the Chronicle v3.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to deliver alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Anomaly, Legal Hold) and events (Page, Application, Audit, Infrastructure, Network, Incident) data to Google Chronicle platform. The plugin supports sharing of UDM and JSON formatted data. The required API keys are linked to customers and are provided by your Google Chronicle representative.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Chronicle account. Obtain your Chronicle Base URL, Service Account Key, and Customer ID from your Chronicle representative before proceeding.
Connectivity to the following hosts (one of these Regional URLs):
USA: https://malachiteingestion-pa.googleapis.com/
EU: https://europe-malachiteingestion-pa.googleapis.com/
ASIA: https://asia-southeast1-malachiteingestion-pa.googleapis.com/
Other Custom URLs you have.
Get the Chronicle service account Key. Reach out to the Chronicle team to get a service account with the following scope: https://www.googleapis.com/auth/malachite-ingestion.
Google Chronicle Plugin Support
The Google Chronicle plugin is used to ingest all the Alert and Events in UDM and JSON format. Ingestion of WebTx and Syslog CE Log data is not supported.
Data Type
Support
Alerts
Yes (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Watchlist, Quarantine, Remediation, UBA, CTEP, Anomaly, Legal Hold)
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident)
WebTx
No
Syslog CE Logs
No
API Details
List of APIs Used
API Endpoint
Method
Use Case
/v2/udmevents:batchCreate
POST
Ingest UDM events
/v2/unstructuredlogentries:batchCreate
POST
Ingest Unstructured logs
Ingest UDM Events
API Endpoint:
<Base URL>
/v2/udmevents:batchCreate
Method:
POST
Body
{
"customer_id": "c8c65bfa-5f2c-*********9-64bb7b939f2c",
"events": [
{
"metadata": {
"event_timestamp": "2019-10-22T12:00:00.000Z",
"event_type": "USER_LOGIN",
"product_name": "Acme SSO",
"vendor_name": "Acme"
},
"principal": {
"ip": [
"10.1.2.3"
]
},
"target": {
"application": "Acme Connect",
"user": {
"user_display_name": "Mary Jane",
"userid": "mary@altostrat.com"
}
},
"extensions": {
"auth": {
"type": "MACHINE",
"mechanism": [
"NETWORK"
]
}
}
},
]
}
Sample API Response
Status Code: 200 (Success)
Ingest Unstructured logs
API Endpoint:
<Base URL>
/v2/unstructuredlogentries:batchCreate
Method:
POST
Body
{
  "customer_id": "c8c65bfa-5f2c-42d4-9189-64bb7b939f2c",
  "log_type": "BIND_DNS",
  "labels" : [
    {
      "key" : "key_name_one",
      "value" : "value_one"
    },
    {
      "key" : "key_name_two",
      "value" : "value_two"
    }
  ]
  "entries": [
    {
      "log_text": "26-Feb-2019 13:35:02.187 client 10.120.20.32#4238: query: altostrat.com IN A + (203.0.113.102)",
      "ts_epoch_microseconds": 1551188102187000
    },
    {
      "log_text": "26-Feb-2019 13:37:04.523 client 10.50.100.33#1116: query: examplepetstore.com IN A + (203.0.113.102)",
    },
    {
      "log_text": "26-Feb-2019 13:39:01.115 client 10.1.2.3#3333: query: www.example.com IN A + (203.0.113.102)"
    }
  ];
}
Sample API Response
Status Code: 200 (Success)
This plugin uses Python libraries to authenticate with the Chronicle Ingestion API.
Library: Google Authentication library for Python (google-auth).
Usage: Google Authentication library for Python (google-auth) to authenticate to Google APIs.
Create a New Session with Credentials
SCOPES = ['https://www.googleapis.com/auth/malachite-ingestion']
credentials = (
service_account.Credentials.from_service_account_info(
json.loads(self.configuration["service_account_key"]),
scopes=SCOPES,
)
)
self.http_session = request.AuthorizedSession(credentials)
Chronicle API Request
response = self.http_session.request(
"POST",
url,
headers=headers,
json=payload,)
Performance Matrix
This performance reading is conducted on a Large Stack with these VM specifications. These readings factor that it will ingest around 10K events in 13 seconds to the Google Chronicle platform.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to Google Chronicle platform
~200K EPM
User Agent
netskope-ce-6.0.0-cls-google-chronicle-v3.0.0
Workflow
Get your credentials for Chronicle.
Configure the Chronicle Plugin.
Configure Log Shipper Business Rules for Chronicle.
Configure Log Shipper SIEM Mappings for Chronicle.
Validate the Chronicle plugin.
Watch a Video
Click play to watch a video.
Configure the Google Chronicle Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Google Chronicle v3.0.0 (CLS)
plugin box.
Add a plugin configuration name and make sure you have the
Chronicle Default Mappings
file selected. Make sure to keep Format as
UDM
to ingest the data in the UDM format, and change it to
JSON
to ingest data in JSON format.
Click
Next
and enter the Configuration Parameters:
Region
: The Chronicle region where the customer account is provisioned.
Custom Region URL
: Custom region base URL; required only if
Custom Region
is selected for Region.
Service Account Key
: Service Account Credentials (provided by your Chronicle team).
Customer ID
: Unique identifier, corresponding to your Chronicle instance.
Log Source Identifier:
This will be added as a namespace to all the JSON formatted data. The log source identifier should not contain whitespaces.
Click
Save
. Your new plugin configuration will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for Google Chronicle
In Log Shipper, go to the
Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding a rule name and desired filter(s).
Configure Log Shipper Log Delivery for Google Chronicle
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (Netskope CLS), Destination plugin (Chronicle Demo), a business rule, and click
Save
.
After the Log Delivery is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Google Chronicle platform.
Validate the Google Chronicle Plugin
You can validate the plugin in both Cloud Exchange and Google Chronicle.
Validate the Pull
To validate the pulling of Events and Alerts from the Netskope tenant, go to
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events and Alerts with the filter
message contains ingested
. The ingested logs will be shown.
To validate the push in Google Chronicle:
Log in to Google Chronicle.
Go to
Investigate > SIEM Search
.
Set Start Time (UTC) and End Time (UTC) according to your needs. And add a query to search ingested alerts/events. Click
Search
.
Note
Use metadata.log_types = “NETSKOPE_ALERT_V2” for filtering data ingested in JSON format and use metadata.log_types = “UDM” for filtering data ingested in UDM format.
Sample ingested Events in JSON format:
Sample ingested Events in UDM format:
Click
Event Viewer
to see details in the log.
Note
Make sure you select the correct timeframe while filtering ingested data.
You will be able to see the ingested data.
Sample ingested Events/Alerts in UDM format:
Sample ingested Alerts in JSON format:
Troubleshooting the Google Chronicle Plugin
Unable to configure the Google Chronicle Plugin
If you are unable to configure the Google Chronicle Plugin, or get an authentication error in logs, it may be due to one of these reasons:
Provided incorrect Customer ID.
Provided incorrect Service Account Key.
Provided incorrect Service Account Key format.
What to do:
Make sure to provide the correct Customer ID that is provided from your Chronicle representative, according to the region selected.
Make sure to provide the correct Service Account Key according to the region selected.
Make sure to provide the correct format of Service Account Key.
Getting an Error in logs related to authentication after Configuring the Google Chronicle Plugin
If you are getting authentication errors in logs, it may be due to one of these reasons:
Provided incorrect Service Account Key.
Provided incorrect Service Account Key format.
What to do:
Make sure to provide the correct Service Account Key according to the region selected.
Make sure to provide the correct format of Service Account Key.
Unable to filter the ingested Alerts/Events in Chronicle
If you are unable to filter the ingested Alerts/Events on Chronicle platform, then check if a wrong filter or wrong time range is being used.
What to do:
The ingested alerts or events may not be immediately visible on the Chronicle UI, as ingestion and processing can take some time. So, wait for some time and then refer to the
Validate the Push
section to filter the alerts/events. It is necessary to use the correct time range based on ingestion time while filtering the events or alerts.
Unable to ingest data in Google Chronicle
If you are unable to ingest data on the Google Chronicle platform and getting this error, then check the below reason.
If you received an error message like displayed in the below image while ingesting data on the Google Chronicle 2.0.2 version, then go to
What to do
below.
What to do:
To resolve this error, make sure you have upgraded to the latest version of the Google Chronicle plugin, like 2.2.0.
Format parameter shows CEF instead of UDM after upgrading the plugin to v3.0.0
If you are using Cloud Exchange v6.0.0 and upgrade the plugin to the latest version (v3.0.0), you can check the Format parameter by editing the plugin.
What to do:
Edit the plugin and select the Format as
UDM
, and then save the plugin.
Known Behaviors
Alert ingested from Cloud Exchange will be classified as Event on Google Chronicle. You can see the same in the below screenshot:
This plugin only supports ingestion of Alerts/Events listed under
Plugin Scope
section.
Ingestion of these Netskope Alerts and Events are not supported by this plugin:
Alert Types
: Device, Content
Event Types
: Endpoint, Client Status
The ingested alerts or events may not be immediately visible on the Chronicle UI, as ingestion and processing can take some time. It was observed that if we ingest data in large numbers, then it may take a few hours to reflect on the Chronicle UI.
In this Topic
Google Chronicle Plugin for Log Shipper

---
## Configure 3rd-party Log Shipper Plugins
**URL:** https://docs.netskope.com/en/configure-3rd-party-log-shipper-plugins/
**Last Modified:** 2026-03-21T02:04:02+00:00
**Scraped:** 2026-08-10T07:39:56.371684+00:00

Configure 3rd-party Log Shipper Plugins - Netskope Technical Documentation
Configure 3rd-party Log Shipper Plugins
Only write-access users can configure Log Shipper plugins. Log Shipper comes with the library of supported plugins. Plugins can be easily configured to ingest logs into multiple 3rd-party SIEM platforms by following the applicable plugin guide.
You can also disable, enable, or delete existing plugin configurations. Log Shipper can be configured with multiple plugins to the same system for different workflows from either the same Netskope tenant or multiple Netskope tenants.
AWS CloudTrail Lake Plugin for Log Shipper
AWS LogStreaming Plugin for Log Shipper
AWS S3 Events and Alerts Plugin for Log Shipper
AWS S3 WebTx Plugin for Log Shipper
AWS Security Lake Plugin for Log Shipper
AWS SQS Plugin for Log Shipper
Azure Netskope Log Streaming Plugin for Log Shipper
Bitsight ThirdPartyTrust Plugin for Log Shipper
Cloud Exchange Logs Plugin for Log Shipper
CrowdStrike LogScale Plugin for Log Shipper
CrowdStrike Next-Gen SIEM Plugin for Log Shipper
Darktrace Plugin for Log Shipper
Databricks Plugin for Log Shipper
Datadog Plugin for Log Shipper
Elastic Plugin for Log Shipper
FortiSIEM Plugin for Log Shipper
Google Chronicle Plugin for Log Shipper
Google Cloud SCC Plugin for Log Shipper
Google Cloud Storage Plugin for Log Shipper
Kafka Plugin for Log Shipper
Local Export Plugin for Log Shipper
Microsoft Azure Event Hubs Plugin for Log Shipper
Microsoft Azure Log Analytics Plugin for Log Shipper
Microsoft Azure Monitor Plugin for Log Shipper
Microsoft Azure Storage Plugin for Log Shipper
Microsoft Defender for Cloud Apps Plugin for Log Shipper
Microsoft Sentinel Plugin for Log Shipper
Netskope Borderless WAN Plugin for Log Shipper
QRadar Plugin for Log Shipper
Rapid7 Plugin for Log Shipper
Scality Plugin for Log Shipper
Secureworks Plugin for Log Shipper
Syslog Plugin for Log Shipper
In this Topic
Configure 3rd-party Log Shipper Plugins

---
## Configure Log Shipper Log Delivery
**URL:** https://docs.netskope.com/en/configure-log-shipper-siem-mappings/
**Last Modified:** 2025-10-31T05:13:27+00:00
**Scraped:** 2026-08-10T07:40:15.762900+00:00

Configure Log Shipper Log Delivery - Netskope Technical Documentation
Configure Log Shipper Log Delivery
A write-access user can configure Log Delivery to ingest the events and alerts from a Netskope tenant into their SIEM platform. A write-access user should configure Netskope and SIEM destination plugin, and also configure a business rule if they plan to ingest only selective alerts and events.
Go to
Log Shipper > Log Delivery
.
Here, Total Logs Sent and Total WebTx Sent will indicate the number of logs/webtx getting ingested to Destination Configuration. Count will be based on the Destination Configuration.
Click
Add Log Delivery
.
Select a Source Configuration, Destination Configuration and Business Rule.
Click
Save
.
Note
As soon as the Log Delivery is saved, Cloud Exchange will do a historical pull for events (default period: 1 hour) and alerts (default period: 7 days).
To get historical pull data, click the
Pull Historial Data
icon from the
Log Delivery
actions.
Select Historical From: To date with date time from calender and click on
Pull
.
Now all the incoming alerts and events with historical data should be ingested into your destination configuration.
In this Topic
Configure Log Shipper Log Delivery

---
## Elastic Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/elastic-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:52:10+00:00
**Scraped:** 2026-08-10T07:40:58.711788+00:00

Elastic Plugin for Log Shipper - Netskope Technical Documentation
Elastic Plugin for Log Shipper
This document explains how to configure the Elastic v2.3.0 plugin in the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP) and Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint) in ECS (Elastic Common Schema) and JSON formats to the Elastic platform. For details on Elastic Agent deployment, refer to the
documentation
.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
Your Elastic server (Filebeat) TCP Server address and port.
Connectivity to the following host: Elastic Server.
Note
This plugin does not support sending WebTx logs to Elastic.
Elastic Plugin Support
Elastic plugin is used to ingest all the Alert, Events in ECS and JSON format on Discover tab of Elastic.
Type
Description
Alerts Support
Yes (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Watchlist, Quarantine, Remediation, UBA, CTEP)
Event Support
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint)
WebTx Support
Not Supported
CE Logs
Not Supported
Permissions
Ports used in Netskope Integration on Elastic should be accessible via Cloud Exchange.
API Details
The plugin utilizes python’s
socket
library to establish a connection with the Elastic server.
Specifically, the plugin uses the socket.connect method to initiate the connection using the
socket.AF_INET
and
socket.SOCK_STREAM
protocols. This guarantees that the connection made to the server is reliable and stream-oriented.
In addition to this, the plugin leverages the
socket.sendall
method to transmit logs to the Elastic server. This method ensures that all data is sent successfully before returning.
Performance Matrix
This performance reading is conducted on a Large Stack CE with the below-mentioned VM specifications. The below readings are added with the consideration that it will ingest around 10K alerts and events in ~80 seconds to the Elastic platform.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to third-party SIEM
~200K EPM
Workflow
Configure a Netskope integration in Elastic.
Configure the Elastic plugin.
Configure a Log Shipper Business Rule for Elastic.
Configure Log Shipper SIEM Mappings for Elastic.
Validate the Elastic plugin.
Click play to watch a video.
Configure a Netskope Integration in Elastic
Log in to Elastic.
Search for and select
Integrations
.
Search for
Netskope
and click on the
Netskope
box.
Click
Add Netskope
.
Expand the dropdown menu.
If the Elastic server and the deployment location of Cloud Exchange match, keep the Listen Address to localhost. Otherwise, add 0.0.0.0 in the Listen Address. Change the Listen port based on your requirements. Make sure that the configured port will be accessible to Cloud Exchange.
Enable the
Preserve original event
toggle for Netskope Alerts and Netskope Events.
If you want to add a custom tag, then click
Advanced options
and add the tag.
Click
Save and continue
.
Click
Save and deploy changes
.
The Integration policy that was just created will appear under the Integration Policies.
If you want to ingest the data in JSON format, then follow these steps to deploy the integration.
Search for and select
Integrations
.
Search for
TCP
and click on the
Custom TCP Logs
box.
Click
Add Custom TCP Logs
.
Expand the dropdown menu.
If the Elastic server and the deployment location of Cloud Exchange match, keep the Listen Address to localhost. Otherwise, add 0.0.0.0 in the Listen Address.
Click
Save and continue
.
Click
Save and deploy changes
.
The Integration policy that has been newly created will appear under the Integration Policies tab.
Configure the Elastic Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and select the
CLS Elastic
box.
Add the plugin configuration name, and make sure you have the Elastic Default Mappings (recommended) file selected.
Disable the toggle button to transform the logs if you want to ingest the data in JSON; keep it enabled if you want to ingest the data in ECS format. Click
Next
.
Enter values for these parameters:
Server Address: IP address of Elastic server in which data will be ingested.
Server Port: The TCP port used while creating the integration policy on Elastic.
Click
Save
. This new plugin will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for Elastic
In Cloud Exchange, go to
Log Shipper > Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific types of alerts or events, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
Click
Save
.
Configure Log Shipper SIEM Mappings for Elastic
In Cloud Exchange, go to
Log Shipper > SIEM Mappings
and click
Add SIEM Mappings
.
Select the Source plugin (Netskope CLS), Destination plugin (Elastic), and your business rule, and then click
Save
.
After the SIEM mapping is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Elastic platform.
Validate the Elastic Plugin
Validate the Pull
Go to the
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events and Alerts with the filter
message contains ingested
. The ingested logs will be filtered.
To validate the push in Elastic:
Log in to Elastic.
Search for and select
Discover
.
Search for
data_stream.dataset : “netskope.alerts” or data_stream.dataset : “netskope.events”
and click
Update
. Or search for tags :
“<the tag that was added while configuring the Netskope integration>
”
JSON Format
Troubleshooting the Elastic Plugin
If you encounter difficulties saving the Elastic plugin
Despite entering all parameters and clicking
Save
, an error may occur, possibly due to the following reason:
The server/port configuration may differ from the specified settings (Cloud Exchange/Elastic).
Go to the Elastic Platform and search for
Integrations
. Go to Installed integrations, click on the
Netskope card > Integration policies
, and then click on Integration policy (the configuration you have used).
Make sure both are the same.
Known Behavior
If you encounter any of the following errors during ingestion, it may be due to socket-related issues. We have identified an unresolved problem on the Elastic side.
For more information, please refer to:
JSON Parse Exception – Illegal Character (Ctrl Char)
Processor ‘json’ with tag ‘json_message’ failed with message ‘Unexpected character (‘*’ (code 42)): expected a valid value (JSON String, Number, Array, Object or token ‘null’, ‘true’ or ‘false’)\n at [Source: (org.elasticsearch.common.io.stream.ByteBufferStreamInput); line: 1, column: 2]’
Processor ‘json’ with tag ‘json_message’ failed with message ‘Illegal character ((CTRL-CHAR, code 3)): only regular white space (\\\\r, \\\\n, \\\\t) is allowed between tokens\\n at [Source: (org.elasticsearch.common.io.stream.ByteBufferStreamInput); line: 1, column: 2]’
Processor ‘json’ with tag ‘json_message’ failed with message ‘Invalid UTF-8 start byte 0xbf\\n at [Source: (org.elasticsearch.common.io.stream.ByteBufferStreamInput); line: 1, column: 3]’
Known Limitation
The existing CLS Elastic (ELK) plugin does not currently support WebTx data ingestion. This is because the existing Elastic Netskope integration, to which we send logs, only supports Alerts and Events. Therefore, we cannot add support for WebTx in the current plugin. For WebTx support, the Elastic team would need to update their Netskope integration.
As a workaround to this issue, the Syslog plugin can be used to send WebTx data to Elastic using the Custom TCP Logs integration. This method will send raw logs, not ECS-transformed logs. Follow these steps to configure the Custom TCP logs integration in Elastic.
In Elastic, go to
Integrations
and search for
Custom TCP Logs
integration.
Click
Add Custom TCP Logs
located in the top right corner.
Provide the name and description for the integration.
Make sure
Custom TCP Logs
is enabled. Expand it and enter the Listen Address, Listen Port and Dataset Name. Also provide the Tags for filtering the ingested logs, and then click
Save and continue
.
After this is done, configure the
CLS Syslog
plugin from Netskope CE.
Note that if you have an On-Premises setup for Elastic, make sure to provide the Listen Address as 0.0.0.0. When adding the port make sure the port is exposed.
In this Topic
Elastic Plugin for Log Shipper

---
## Google Cloud Storage Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/google-cloud-storage-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:54:35+00:00
**Scraped:** 2026-08-10T07:41:08.380662+00:00

Google Cloud Storage Plugin for Log Shipper - Netskope Technical Documentation
Google Cloud Storage Plugin for Log Shipper
This document explains how to configure Google Cloud Storage with Log Shipper in the Netskope Cloud Exchange platform. This integration allows pushing web transactions into cloud storage.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netksope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
Google Cloud Platform credentials with specified roles on a particular project.
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Verify your Google Cloud Storage instance permissions are secure and not set up for open public access. Only allow access to your cloud storage instance from your Cloud Exchange Host and any other addresses that need access.
Workflow
Get your Google Cloud Platform Key.
Configure the GCP Cloud Storage plugin.
Configure Log Shipper Log Delivery for GCP Cloud Storage.
Validate the Google Cloud Storage plugin.
Get your Google Cloud Platform Key
Go to Google Cloud Platform at
https://console.cloud.google.com/
.
Select your Project from and click
Open
.
Go to
IAM & Admin Service Accounts
.
Click
+ Create Service Account
.
Enter a Service account name and Service account description. Click on
Create and Continue
.
Click
Continue
.
Click
Done
.
Click the 3 dots under Action.
Click
Manage Keys
.
Click
Add Key
and then
Create new key
.
Select
JSON
and click
Create
to download the key to your local device.
Configure the GCP Cloud Storage Plugin
In Cloud Exchange, go to
Settings > Plugin Store.
Search for and select the
Google Cloud Storage v1.0.0 (CLS)
plugin.
Enter a Configuration Name.
Click
Next
.
Enter Key File from Google Cloud Storage account.
Enter a globally unique Bucket Name.
Select a Region Name from the dropdown (The location used for storing objects).
If you want to know more about buckets regions, refer to:
https://cloud.google.com/storage/docs/locations
.
Select a Storage Class from the dropdown (Based on your GCP storage class cost).
If you want to know more about storage class, refer to:
https://cloud.google.com/storage/docs/storage-classes
.
Enter an Object Prefix. The Object Prefix is used for creating the file name prefix)
Enter a Maximum File Size (in MBs, Value should be between 0 to 100). Default value will be 10 MB.
Enter a Maximum Duration (in Seconds, and the Value should be positive integer).
Click
Save
.
Configure Log Shipper Log Delivery for GCP Cloud Storage
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
Select a Source Configuration and Destination Configuration.
Click
Save
.
Validate the GCP Cloud Storage Plugin
To validate the plugin workflow, you can check from Netskope Cloud Exchange and from Google Cloud Platform.
Validate in Netskope Cloud Exchange
Go to
Logging.
Validate in Google Cloud Platform
Open the GCP Console (
https://console.cloud.google.com/
).
Search Cloud Storage and click on your Project.
Search
Bucket Name
you provided when you configured
Google Cloud Storage
Plugin.
Click
Bucket Name
and files pushed into GCP will be seen and by clicking on the file it shows the
Download
option to view the content locally.
In this Topic
Google Cloud Storage Plugin for Log Shipper

---
## Google Cloud SCC Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/google-cloud-scc-plugin-for-log-shipper/
**Last Modified:** 2026-05-28T22:06:32+00:00
**Scraped:** 2026-08-10T07:41:09.603012+00:00

Google Cloud SCC Plugin for Log Shipper - Netskope Technical Documentation
Google Cloud SCC Plugin for Log Shipper
This document explains how to configure your Google Cloud SCC plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This integration allows ingestion of Netskope alerts and events into your Goggle Cloud SCC tenant in JSON format.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
Google Cloud Platform credentials with specified roles on a particular project.
Connectivity to the following host: Google Cloud SCC (https://console.cloud.google.com/)
Note
Verify your Google Cloud SCC instance permissions are secure and not set up for open public access. Only allow access to your cloud storage instance from your Cloud Exchange Host and any other addresses that need access.
Google Cloud SCC Plugin Support
Google Cloud SCC plugin is used to ingest all the Alert and Events in JSON format.
Alerts Support
Yes
Event Support
Yes
WebTx Support
NA
Permissions
The following permissions are required for the service account at the organization level.
Security Center Source Editor
Security Center Findings Editor
Resource Manager get projects (Role: Browser)
here
API Details
This plugin uses Python libraries to authenticate with the Google Cloud API.
Library: Google Authentication library for Python (google-auth).
Usage: Google Authentication library for Python (google-auth) to authenticate to Google APIs.
Create a new session with credentials
self.gcp_scope = ["https://www.googleapis.com/auth/cloud-platform"]
self.creds = (
                service_account.Credentials.from_service_account_info(
                    json.loads(self.configuration["key_file"])
                )
            )
scoped = self.creds.with_scopes(self.gcp_scope)
self.gcp_session = request.AuthorizedSession(scoped)
self.gcp_session.proxies = self.proxy
Google Cloud GET API Request
response = self.gcp_session.get(
                url,
                headers=headers,
                params=params
)
Google Cloud POST API Request
response = self.gcp_session.post(
               url,
               params=param,
               json=data,
               headers=headers
)
Resource Manager API
API Endpoint
Method
Use Case
/v1/projects/{projectId}
GET
Retrieves the Project identified by the specified projectId.
The Base URL
https://cloudresourcemanager.googleapis.com
is the same for all Resource Manager APIs.
Get Project
API Endpoint:
<Base URL>/v1/projects/{projectId}
Method:
GET
Sample API Response:
{
  "projectNumber": "",
  "projectId": "",
  "lifecycleState": "ACTIVE",
  "name": "projectName",
  "createTime": "2024-04-04T10:01:07.553347Z",
  "parent": {
    "type": "organization",
    "id": ""
  }
}
Security Command Center APIs
API Endpoint
Method
Use Case
/v1/organizations/{organizationId}/sources/{sourceId}/findings
GET
Lists an organization or source’s findings.
/v1/organizations/{organizationId}/sources/{sourceId}/findings
POST
Creates a finding. The corresponding source must exist for finding creation to succeed.
/v1/organizations{organizationId}/sources/{sourceId}
GET
Get a source.
/v1/organizations/{organizationId}/sources/{sourceId}
POST
Creates a source.
The Base URL
https://securitycenter.googleapis.com
is the same for all Security Command Center APIs.
List Findings
API endpoint:
<Base URL>/v1/organizations/{organizationId}/sources/{sourceId}/findings
Method:
GET
Sample API Response:
{
  "listFindingsResults": [
    {
      "finding": {
        "name": "organizations//sources//findings/00087f8800a911ef94c60242c0a8f104",
        "parent": "organizations//sources/",
        "resourceName": "//cloudresourcemanager.googleapis.com/projects/",
        "state": "ACTIVE",
        "category": "ctep",
        "externalUri": "https://drive.google.com/open?id=14WLyjF82rGg",
        "sourceProperties": {
          "cci": "29",
          "timestamp": "1713791120",
          "url": "https://drive.google.com/open?id=14WLyjF82rGg",
          "alert_type": "ctep",
          "tenant_name": "CLS"
        },
        "securityMarks": {
          "name": "organizations//sources//findings/00087f8800a911ef94c60242c0a8f104/securityMarks"
        },
        "eventTime": "2024-04-22T13:05:20Z",
        "createTime": "2024-04-22T13:05:34.141Z",
        "canonicalName": "projects//sources//findings/00087f8800a911ef94c60242c0a8f104",
        "mute": "MUTED",
        "muteUpdateTime": "2024-04-22T13:05:35.371Z",
        "muteInitiator": "Muted by mute rule organizations//muteConfigs/rule8",
        "contacts": {
          "security": {
            "contacts": [
              {
                "email": "systems@abc.com"
              }
            ]
          },
          "technical": {
            "contacts": [
              {
                "email": "systems@abc.com"
              }
            ]
          }
        },
        "parentDisplayName": "test"
      },
      "resource": {
        "name": "//cloudresourcemanager.googleapis.com/projects/",
        "projectName": "//cloudresourcemanager.googleapis.com/projects/",
        "projectDisplayName": "",
        "parentName": "//cloudresourcemanager.googleapis.com/organizations/",
        "parentDisplayName": "abc.com",
        "type": "google.cloud.resourcemanager.Project",
        "displayName": "",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "organization": "organizations/",
        "service": "cloudresourcemanager.googleapis.com",
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/",
              "displayName": ""
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/"
            }
          ]
        },
        "resourcePathString": "organizations//projects/"
      }
    }
  ],
  "readTime": "2024-04-22T13:31:00.144Z",
  "nextPageToken": "CsoD3cy7qgAx8Qqf…",
  "totalSize": 22210
}
Create Finding
API endpoint:
<Base URL>/v1/organizations/{organizationId}/sources/{sourceId}/findings
Method:
POST
Body:
{
  "name": "/findings/00087f8800a911ef94c60242c0a8f104",
  "parent": "",
  "resourceName": "//cloudresourcemanager.googleapis.com/projects/",
  "state": "ACTIVE",
  "category": "ctep",
  "eventTime": "2024-04-10T07:19:30Z",
  "createTime": "2024-04-10T07:19:31.208001Z",
   …
}
Sample API Response:
{
  "name": "organizations//sources//findings/00087f8800a911ef94c60242c0a8f104",
  "parent": "organizations//sources/",
  "resourceName": "//cloudresourcemanager.googleapis.com/projects/",
  "state": "ACTIVE",
  "category": "ctep",
  "securityMarks": {
    "name": "organizations//sources//findings/00087f8800a911ef94c60242c0a8f104/securityMarks"
  },
  "eventTime": "2024-04-10T07:19:30Z",
  "createTime": "2024-04-22T05:46:05.439Z",
  "canonicalName": "projects//sources//locations/global/findings/00087f8800a911ef94c60242c0a8f104",
  "mute": "MUTED",
  "muteUpdateTime": "2024-04-22T05:46:06.580Z",
  "muteInitiator": "Muted by mute rule organizations//muteConfigs/rule8",
  "contacts": {
    "security": {
      "contacts": [
        {
          "email": "systems@crestdatasys.com"
        }
      ]
    },
    "technical": {
      "contacts": [
        {
          "email": "systems@crestdatasys.com"
        }
      ]
    }
  },
  "parentDisplayName": "test"
}
Get a Source
API endpoint:
<Base URL>/v1/organizations{organizationId}/sources/{sourceId}
Method:
GET
Sample API Response:
{
  "name": "organizations//sources/",
  "displayName": "Source Name",
  "description": "Source description"
}
Create a Source
API Endpoint:
<Base URL>/v1/organizations{organizationId}/sources/{sourceId}
Method:
POST
Body
:
{
  "name": "Name of source",
  "displayName": "Unique name of the source",
  "description": "Description of the source"
}
Sample API Response:
{
"name": "organizations/<org_id>/sources/<source_id>",
"displayName": "Unique source Name",
"description": "Source description"
}
User Agent
Netskope-ce-5.0.1-cls-google-cloud-scc-v2.1.0
Workflow
Create a Google Cloud SCC service account.
Configure the Google Cloud SCC Plugin.
Configure the Log Shipper Business Rules for Google Cloud SCC.
Configure Log Shipper SIEM Mappings for Google Cloud SCC.
Validate the Google Cloud SCC plugin.
Click play to watch a video.
Create a Google Cloud SCC Service Account
Log in to Google Cloud Platform.
Go to
IAM & Admin > Service Accounts
.
Click
+ Create Service Account
.
Enter a Service account name and Service account description, and then click
Create and Continue
.
Add the required permissions.
Click
Continue
.
Click
Done
.
Click the 3 dots under Action.
Click
Manage Keys
.
Click
Add Key
and then click
Create new key
.
Select
JSON
and click
Create
to download the key to your local device.
Go to
https://cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.sources/create
Click
Try It.
Enter Parent and Request Body data, check
Google OAuth 2.0
and
API Key
, and then click
Execute
.
Note the Saved Source ID specified in name in the response.
Configure the Google Cloud SCC Plugin
In Cloud Exchange, go to
Settings > Plugins.
Search for and select the
Google Cloud SCC
box to open the plugin creation pages.
Enter a Configuration Name, and make sure the default Google Cloud SCC mapping file is selected.
Disable the toggle button to transform the logs in order to ingest the data in JSON format.
Click
Next
.
Enter values for these parameters:
Organization ID: Organization ID of GCP in which data will be ingested.
Source ID: Organization ID of GCP in which data will be ingested.
Key File: Service Account Key file of GCP.
Click
Save
. Your plugin will appear on the Cloud Log Shipper > Plugins page.
Configure the Log Shipper Business Rules for Google Cloud SCC
Go to
Log Shipper > Business Rules.
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific types of alerts or events, click
Create New Rule
and configure a new business rule by adding a rule name and selecting filters.
Click
Save
.
Configure Log Shipper SIEM Mappings for Google Cloud SCC
Go to
Log Shipper > SIEM Mappings
and click
Add SIEM Mapping
.
Select a Source Configuration, Business Rule, and Destination Configuration.
Click
Save
.
Validate the Google Cloud SCC Plugin
Validate the Pull
To validate the pulling of Events and Alerts from the Netskope tenant:
Go to
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the push in Cloud Exchange, go to
Logging
and search for ingested Events, Alerts with the filter message contains
ingested.
The ingested logs will be filtered.
To validate the push in Google Cloud SCC:
Log in to Google Cloud Platform.
Click
Findings
.
Select
Show inactive
and
Show muted
.
Click on any Event or Alert.
Click
Source Properties
.
Another way to check is click
JSON
and under Source Properties, you can find the data.
Troubleshooting
If you encounter difficulties while upgrading the Google Cloud SCC plugin
Despite having all parameters and clicking the save button, an error may occur, possibly due to the toggle for transforming the logs being enabled, instead of being disabled.
What to do:
Go to
Log Shipper > Plugin
s page.
Edit the Google Cloud SCC plugin and disable the toggle to transform logs.
Click
Save
.
Enable the plugin.
In this Topic
Google Cloud SCC Plugin for Log Shipper

---
## Logging
**URL:** https://docs.netskope.com/en/logging/
**Last Modified:** 2025-10-31T01:16:14+00:00
**Scraped:** 2026-08-10T07:41:27.528519+00:00

Logging - Netskope Technical Documentation
Logging
An Admin and User can view and search audit logs. Audit logs track significant events that occur during the operation of Cloud Exchange. Logs provide important information for troubleshooting if any abnormal behaviors and errors occur. Audit logs can be searched through in the Cloud Exchange UI, and you can export the logs to a local system.
Go to
Settings
>
Logging
in the left panel.
Logs entries are displayed. By Default, log entries are sorted in descending order of occurrence.
Filters can be set to search for specific log entries. The filter parameters are listed here:
Field
Description
Filter operators
Message
Log message.
Is equal, Is Empty and contains (Regex also supported).
Type
Log type (info, warning, error).
any in, not in operator (Multiselect)
Error Code
Error code for particular error message.
Is equal, Is Empty and contains (Regex also supported).
Details
Detailed explanation of log message.
Is equal, Is Empty and contains (Regex also supported).
Created At
Time at which log is created.
!=, <, >, >=
Resolution
In the case of an error, users can perform the mentioned actions to troubleshoot and resolve the issue.
Is equal, Is Empty and contains (Regex also supported).
You can also export the logs by clicking
Export
.
Keep Alive Log Message
This feature checks the health of our Cloud Exchange services regularly and creates a message to let us know if everything is okay or if there’s a problem. You can send this particular log to your SIEM (Security Information and Event Management) and monitor the status of their Cloud Exchange services.
In this Topic
Logging

---
## Log Shipper Module
**URL:** https://docs.netskope.com/en/log-shipper-module/
**Last Modified:** 2025-10-31T19:56:27+00:00
**Scraped:** 2026-08-10T07:41:29.998587+00:00

Log Shipper Module - Netskope Technical Documentation
Log Shipper Module
Log Shipper is a logging service that pulls all or a subset of customer tenant events and alerts logs and sends them in a customized, customer-selected format to its SIEM and datalake(s) using either the mapping wizard or the raw editor. Use either tool to add or remove fields, change mappings, change field headers, transform field extended attributes, or insert static placeholders to meet your specific log requirements.
Click play to learn how to set up Log Shipper.
Log Shipper Global Settings
Only Admins can change Log Shipper Global Settings. Go to
Settings > Log Shipper
. There are two tabs: General and Mappings.
On the General tab, you can retry configuration for log delivery from Log Shipper to a destination SIEM.
Default (3 Retries):
In the event of a failed log delivery from Log Shipper to a destination SIEM, Log Shipper will initiate 3 attempts to push the logs to the destination SIEM.
If ALL 3 retry attempts FAIL, the corresponding batch of logs will be discarded by Log Shipper.
Retry till Successful Delivery
: Unlimited retries till successful delivery of logs.
This may impact overall Cloud Exchange performance, including other Cloud Exchange modules likeTicket Orchestrator, Threat Exchange, etc.
In the event of a failed log delivery from Log Shipper to a destination SIEM, Log Shipper will indefinitely retry till successful log delivery to the destination SIEM.
UTF-8 encoding:
Enable UTF-8 encoding for Alerts, Events, and WebTx to ensure seamless handling of UTF-8 encoded data. By default, this feature is disabled.
Use the Mapping tab to manage your Log Shipper Mapping files.
You can also create a new mapping file to be invoked by a configured plugin as an alternative to the defaults provided. In the Wizard view, you can modify the mapping file to enable the addition, deletion, or modification of new fields to the default.
Note
AWS S3, Microsoft Azure Cloud Storage (Azure Blob), and Google Cloud SCC (Google GCS) plugins for WebTx logs can
not
be edited. These plugins push the original .gzip files obtained from Netskope to the cloud service providers without decompressing or modifying the content.
Click
Add Mapping File
button (or the Copy icon) from any of the default mapping file.
Enter a Name.
Select the Wizard radio button.
From the Alerts/Event tab, expand the Alert/Event row. Target Field specifies the destination field name to which the data will be mapped or transmitted. Transformation defines the type of data conversion or transformation applied to the Netskope field before it is transmitted to the target field. Netskope field Indicates the source field from the Netskope data that will be mapped to the target field. Default Value means If the source value is empty, this default value will be sent to the target field instead.
From Header expand, select the Netskope field for each Target field & Edit Default value if required. The new fields coming from new alerts/events will be added in Netskope field. The newly available fields will also be shown in notifications as well as in Netskope CE logs.
You can delete the alert/event value row from wizard by clicking on Delete icon which are not required
You can also delete a target field as well by clicking on Delete icon.
From Extension expand, select a Transformation for each Target field & Enter Default value.
Delete the alert value & Target field value row as well from Delete icon. Click
Extension Expand
.
Add a New Alert/event field on clicking Add Alert Field.
Enter a Field name & click
Add
.
Enter New added Alert field and add Target field & default value for respected Netskope field mapping & click on Add button.
Click WebTx the tab and select Header & Extensions Target fields with respected Netskope field, and also can delete the same as above. You can delete the WebTx field by clicking Delete.
Click on Editor radio button to add/edit/delete the Event & alert name from window format.
Click
Save
.
You can download the custom or default mapping file from the download icon from list & can upload the same from Load from file option on Create mapping file window and click
Save
.
You can enable the toggle button displayed in the CLS plugin configuration (which are supporting this functionality to send the data in JSON to the SIEM) to send the data in JSON format without transforming the data using Default Mapping file. There is a functionality to send specific fields only to the target SIEM, user can select the number of fields they want to send using the CLS Mapping wizard.
When you select the JSON option for sending data and do not specify any Netskope fields, all available Netskope field data will be sent to the destination by default. However, if you choose specific Netskope fields, only those selected fields will be included in the data sent to the destination.
Configure 3rd-party Log Shipper Plugins
Update Configured Log Shipper Plugins
Manage Log Shipper Business Rules
Configure Log Shipper Log Delivery
Log Shipper Syslog Mapping
Log Shipper Custom Plugin Developers Guide
In this Topic
Log Shipper Module

---
## Logs
**URL:** https://docs.netskope.com/en/logs/
**Last Modified:** 2025-10-31T01:27:09+00:00
**Scraped:** 2026-08-10T07:41:31.173985+00:00

Logs - Netskope Technical Documentation
Logs
An Admin can set the default log level that will be used.
Click
Settings
in the main menubar.
Click
General,
and then
Logs.
Select a log level value from the dropdown list, and then specify how often to delete the logs.
The new type of log called
debug log
has been added to Cloud Exchange. Debug logs are used by developers and technical support teams to investigate and troubleshoot issues within Cloud Exchange. The default log message type should be set to
Info
.
Define the duration of Statistics you want to keep. Only the statistics that are older than the number of days specified will be deleted during an automatic cleanup.
Click
Save.
In this Topic
Logs

---
## Manage Log Shipper Business Rules
**URL:** https://docs.netskope.com/en/manage-log-shipper-business-rules/
**Last Modified:** 2025-10-31T05:03:29+00:00
**Scraped:** 2026-08-10T07:41:33.537893+00:00

Manage Log Shipper Business Rules - Netskope Technical Documentation
Manage Log Shipper Business Rules
Only write-access users can manage Log Shipper Business Rules.
View Log Shipper Business Rules
Go to
Log Shipper > Business Rules
to view business rules in list view or grid view, and toggle the view between grid and list views using the button besides the Refresh button.
You can also expand each folder to see the business rules in that folder. User can also delete the whole folder of business rules which will delete all the business rules in that folder.
Create Log Shipper Business Rules
A write-access user can create business rules to filter out the logs they want to ingest in their SIEM platforms. A default business rule with name
All
is provided out of the box which matches all the alerts and events.
Go to
Log Shipper > Business Rules
.
Click
Create New Rule
.
Enter a rule name.
Select or enter a query in the alert/event filter. At least one filter must be selected.
Enter the folder name that you want to add it to, or you can select an existing folder. At max you can go up to 3 level of hierarchy.
Click
Save
.
Cloud Exchange automatically detects the data type (string, number, or boolean) of incoming fields and adjusts operators based on new data type across all Cloud Exchange filter views accordingly upon data retrieval. Other data types, such as list, dictionary, and datetime, are not supported.
Perform an Action on a Log Shipper Business Rule
A write-access user can manage all the business rules from a single place on the platform on the Log Shipper Business Rules page, and can clone or edit a business rule, or delete the business rule from this page in the Action column.
Clone a Log Shipper Business Rule
To clone the entire business rule, select the Clone icon on the rule, name the rule, and click
Save
.
Edit a Log Shipper Business Rule
To edit a business rule, select the Pencil icon and modify the business rule. When finished, click
Save
.
Delete a Log Shipper Business Rule
To delete a business rule, select the Trash icon on the rule and confirm the action.
In this Topic
Manage Log Shipper Business Rules

---
## Microsoft Sentinel Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/microsoft-azure-sentinel-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:38:02+00:00
**Scraped:** 2026-08-10T07:41:44.545249+00:00

Microsoft Sentinel Plugin for Log Shipper - Netskope Technical Documentation
Microsoft Sentinel Plugin for Log Shipper
This document explains how to configure the v3.0.3 Microsoft Sentinel plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin ingests Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint), and WebTx data (uncompressed) into the Microsoft Azure Sentinel platform. It only supports the ingestion of JSON-formatted logs. You need Log Analytics Workspace on the Microsoft Azure platform to access the plugin.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
Connectivity to the following hosts:
https://portal.azure.com/
Log Analytics Workspace on the Microsoft Azure platform
Microsoft Sentinel Plugin Support
The Microsoft Sentinel plugin is used to ingest Netskope Events, Netskope Alerts data and WebTx data in JSON format to Microsoft Sentinel.
Data Type
Support
Events
Yes: Page, Application, Audit, Infrastructure, Network, Incident, Endpoint
Alerts
Yes: DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA
CE Logs
Not supported
WebTx
Yes (uncompressed, via Netskope Log Streaming)
Note:
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Permissions
Requires a Microsoft Sentinel Account with Log Analytics workspace access.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/api/logs
POST
Send log data to Log Analytics with the HTTP Data Collector
API Endpoint:
https://
{CustomerID}
.
<Azure_Analytics_Domain>
/
<Resource>
?api-version=2016-04-01
Method:
POST
Parameters:
api-version=2016-04-01
Headers:
Content-Type: application/json
Log-Type: Netskope_Alerts1
x-ms-date: Wed, 06 Dec 2023 06:46:41 GMT
Authorization: SharedKey
<WorkspaceID>
:
<Signature>
Request Body
{
	  "key1": "value1",
	  "key2": "value2",
	  "key3": "value3",
	  "key4": "value4”
}
Sample API Response
200 OK
Performance Matrix
This performance reading is for a Large Cloud Exchange Stack tested with these VM specifications. The below readings are added with the consideration that it will ingest around 10K logs in 11 seconds for Alerts and Events.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Events, Alerts ingested to Microsoft Sentinel
200K EPM
User Agent
The user agent added in this plugin in the following format:
netskope-ce-
<ce_version>
-
<module>
-
<plugin_name>
-v
<plugin_version>
For example:
Netskope-ce-5.1.0-cls-microsoft-azure-sentinel-v3.0.3
Workflow
Get your Microsoft Sentinel Workspace ID and Primary Key.
Configure the Microsoft Sentinel plugin.
Configure a Log Shipper Business Rules.
Configure the Log Shipper SIEM Mappings.
Validate the plugin.
Click play to watch a video.
Get your Azure Sentinel Workspace ID and Primary Key
Log in to the Entra ID
portal
.
Click
Microsoft Sentinel
.
Click
Create
on the Microsoft Sentinel page.
Click
Create a new workspace.
Select a Resource Group, enter a Name, and select your Region. Click
Review + Create
.
Click
Create
.
The workspace will be created; it will take a few seconds to deploy. After deployment succeeds, click
Refresh
. Click on the Workspace that you created and click
Add
.
It will take a few seconds to add the workspace.
After successfully adding a workspace, go to
Home > Log Analytics workspaces
.
Click on the workspace name that you created.
Click
Settings > Agents
.
Click
Log Analytics agent instructions
.
Under Logs Analytics agent instruction, copy the Workspace ID and Primary Key. These are needed to configure the plugin.
Configure the Microsoft Sentinel Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Microsoft Azure Sentinel v3.0.3 (CLS)
plugin.
Enter these parameters:
Configuration Name
: Create a unique name for the configuration.
Mapping
: Use the default mapping file.
Transform the raw logs
: Disable if you need to send Raw Data. (Default: It will be enabled and send Transformed data).
Use System Proxy
: Enable if the proxy is required for communication.
Click
Next
and enter the Configuration Parameters:
Azure Log Analytics Domain
: Domain name for your Azure Log Analytics. For example,
ods.opinsights.azure.com
,
ods.opinsights.azure.us
, etc.
Workspace ID
: The unique identifier of your Microsoft Sentinel workspace.
Primary Key
: The authentication key for your Microsoft Sentinel workspace.
Alerts Log Type Name
: Custom Log Type name for alerts. Based on this name, a schema for alerts will be created in Log Analytics Workspace with suffix
_CL
. Note that the value
Netskope_Alerts
or
Netskope_Alerts_CL
for this parameter matches the Netskope published playbooks in the Microsoft marketplace. In this log type,
_CL
will automatically be appended from Microsoft.
<
Events Log Type Name
: Custom Log Type name for events. Based on this name, a schema for events will be created in Log Analytics Workspace with suffix
_CL
. Note that the value
Netskope_Events
or
Netskope_Events_CL
for this parameter matches the Netskope published playbooks in the Microsoft marketplace. In this log type,
_CL
will automatically be appended from Microsoft.
WebTX Log Type Name
: Custom Log Type name for web transactions. Based on this name, a schema for web transactions will be created in Log Analytics Workspace with suffix
_CL
. Note that the value
Netskope_WebTx
or
Netskope_WebTX_CL
for this parameter matches the Netskope published playbooks in the Microsoft marketplace. In this log type,
_CL
will automatically be appended from Microsoft.
Click
Save
.
Configure Log Shipper Business Rules for Microsoft Sentinel
Skip this step if you do not want to filter out alerts or events before ingestion.
Go to
Log Shipper > Business Rules.
Click
Create New Rule
.
Note
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, create a new Business Rule.
If creating a new rule, enter a Rule Name and select the filters to use.
Click
Save
.
Configure the Log Shipper Log Delivery for Microsoft Sentinel
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (CLS Netskope), and Destination plugin (CLS Microsoft Azure Sentinel), select a business rule, and then click
Save
.
For ingestion of WebTx, select the Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming), the Destination plugin (CLS Microsoft Azure Sentinel), and then click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant and ingested into the Azure Sentinel platform.
Validate the Microsoft Sentinel Plugin
To validate the plugin workflow, you can check from Netskope Cloud Exchange and from the Microsoft Sentinel instance.
Validate the Pull
Go to
Logging
, and search for the
message contains
pulled
logs.
Validate the Push
To validate the plugin workflow in Netskope Cloud Exchange:
Go to
Logging
and search for ingested events with the filter
message contains ingested
.
The ingested logs will be filtered.
To validate the push in the Azure platform:
Log in to the Entra ID
portal
.
Go to the Log Analytics workspace,  and click on the workspace that you have created.
You can filter the logs using the schema name used in the plugin example:
Netskope_Alerts_CL | where alert_type_s contains “dlp”
To verify the Events data filter the logs using the schema name:
Netskope_Events_CL
.
To verify the Webtx data filter the logs using the schema name:
Netskope_WebTX_CL
.
Troubleshooting the Microsoft Sentinel Plugin
If a user is not able to configure the Microsoft Sentinel plugin
If you are not able to configure the plugin it might be due to invalid plugin credentials provided.
What to do:
Check the Workspace ID and Primary key added in the plugin configuration with the Workspace ID and Primary Key on the Sentinel Portal. Also make sure that the workspace is not deleted on Sentinel.
If data is not ingested from Cloud Exchange
Data is not ingested from Cloud Exchange to the platform. If this is the case it might be due to one of the following:
Data is not pulled from the Source plugin.
Data is not present on the Source plugin for the provided initial range.
What to do:
If your data is not pulled from Cloud Exchange, go to the logging page and check the logs, there will be a log like mentioned below, related to readtimeout. Wait for the error to be resolved, and check the issue from the source plugin side.
Check on the tenant from which date the data is present and provide that number while configuring the tenant in Cloud Exchange.
If ingested data is not reflected on the Microsoft Azure Sentinel plugin
Ingestion logs are received but the data is not reflected on the platform. If this is the case it might be due to one of the following:
Workspace is newly created
Logs are being checked in the wrong Workspace
File name for ingested data is wrong while searching
What to do:
If your data is not reflected check above options, If the workspace is newly created and data is ingested for the first time it might take a few minutes for the data to be reflected on the platform.
Check the workspace in which you are ingesting the logs.
If that is not the case then check the file name or search query that you are using for data verification. You can check the file name in the plugin configuration.
Make sure to add the
_CL
in the table name while filtering the data on Sentinel, as Sentinel adds the above suffix for all the file names when data is ingested, else you won’t be able to see any ingested logs.
In this Topic
Microsoft Sentinel Plugin for Log Shipper

---
## Microsoft Azure Storage Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/microsoft-azure-storage-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:56:26+00:00
**Scraped:** 2026-08-10T07:41:45.735179+00:00

Microsoft Azure Storage Plugin for Log Shipper - Netskope Technical Documentation
Microsoft Azure Storage Plugin for Log Shipper
This document explains how to configure Azure Cloud Storage with the Log Shipper module of the Netskope Cloud Exchange platform. This integration allows pushing the WebTx data and creating blobs inside the container in Azure Blob Storage.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
An Azure Cloud instance.
Note
Verify your Azure Blob instance permissions are secure and not set up for open public access. Only allow access to your cloud storage instance from your Cloud Exchange Host and any other addresses that need access.
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Workflow
Configure an Azure Cloud account.
Configure the Azure Cloud Storage plugin.
Configure Log Shipper Log Delivery.
Validate the plugin.
Click play to watch a video.
Configure an Azure Cloud Storage Account
Go to your Azure instance
https://portal.azure.com/
.
Log in to your Azure Cloud instance.
Click on
Storage Accounts
, Click
+ Create
and provide a unique Storage Account name, and then click on
Review + Create.
Shortly, a Storage Account will be created and deployment will be completed.
Click on
Home
, and go to
Storage Accounts
, Search for your storage account.
In the left pane, under
Security + networking
, click on
Access Keys
and copy the
connection string
, it will be required when configuring the Azure Cloud plugin.
Configure the Azure Cloud Storage Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Azure Cloud Storage v1.0.1 (CLS)
plugin.
Enter a Configuration Name.
Click
Next
.
Enter your Azure Connection String, Container Name, Object Prefix, Minimum File Size, and Minimum Duration.
Container names must start with a letter or number, and can contain only letters, numbers, and the dash character.
Every dash character must be immediately preceded and followed by a letter or number; consecutive dashes are not permitted in container names.
All letters in a container name must be lowercase.
Container names must be from 3 through 63 characters long.
Click
Save
.
Configure a Log Shipper Log Delivery for Azure Storage
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming) and Destination plugin (Microsoft Azure Storage.)
Click
Save
.
Validate the Azure Storage Plugin
To validate the configuration, you must have Azure instance and/or SIEM mappings.
Validate in Netskope Cloud Exchange
Go to
Logging.
Logs will be seen regarding File name and data ingested into Azure.
Validate the Storage Plugin in Azure:
In your Azure instance From Storage accounts.
Go to
Storage Accounts
and search your storage account from the list.
In the left pane, under
Data Storage,
click on
Containers.
The container name which has been given while configuring the plugin would be seen in the list. If the Container has already been there, files will be appended, else a new Container would be created and then files will be pushed.
Click on a
Container Name
and files pushed into Azure will be seen, and by clicking on the file, the
Download
option appears to view the content locally.
In this Topic
Microsoft Azure Storage Plugin for Log Shipper

---
## Microsoft Azure Monitor Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/microsoft-azure-monitor-plugin-for-log-shipper/
**Last Modified:** 2026-04-06T23:55:20+00:00
**Scraped:** 2026-08-10T07:41:46.964464+00:00

Microsoft Azure Monitor Plugin for Log Shipper - Netskope Technical Documentation
Microsoft Azure Monitor Plugin for Log Shipper
This document explains how to configure the Microsoft Azure Monitor v2.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status). The data will be ingested in the Microsoft Azure Monitor Log Analytics Workspace table. This plugin supports ingestion in CEF and JSON format.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
The Microsoft Azure Application’s Tenant ID, Client ID and Client Secret.
A Microsoft Azure Log Analytic Workspace.
A Microsoft Azure Monitor Data Collection Endpoint.
A Microsoft Azure Monitor Data Collection Rule.
Connectivity to the following host:
https://portal.azure.com/
.
Microsoft Azure Monitor Plugin Support
This plugin supports ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status). The data will be ingested in the Microsoft Azure Monitor Log Analytics Workspace table. This plugin supports ingestion in CEF and JSON format.
Data Type
Support
Event Support
Yes
Alert Support
Yes
WebTx Support
No
Permissions
Requires an Azure Account with Monitor access.
API Details
List of APIs Used
API Endpoint
Method
Use case
/{tenant_id}/oauth2/v2.0/token
POST
Generate access token
{dce_uri}/dataCollectionRules/{dcr_immutable_id}/streams/Custom-{custom_log_table_name}?api-version=2023-01-01
POST
Ingest data
Generate Token
API Endpoint:
https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token
Method:
POST
Headers
Key
Value
Content-Type
application/x-www-form-urlencoded
User-Agent
netskope-ce-6.0.1-cls-microsoft-azure-monitor-v2.0.0
Body:
{
"client_id": "
<client_id>
",
"client_secret": "<application_secret>",
"scope": "https://monitor.azure.com/.default",
"grant_type": "client_credentials",
}
Sample API Response
{
"token_type": "Bearer",
"expires_in": 3599,
"ext_expires_in": 3599,
"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InNNMV95QXhWOEdWNHlOLUI2ajJ4em1pazVBbyIsImtpZCI6InNNMV95QXhWOEdWNHlOLUI2ajJ4em1pazVBbyJ9.eyJhdWQiOiJodHRwczovL21vbml0b3IuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZTA0MDU2MDYtNmMw…."
}
Ingest data
API Endpoint:
{dce_uri}/dataCollectionRules/{dcr_immutable_id}/streams/Custom-{custom_log_table_name}?api-version=2023-01-01
Method:
POST
Headers
Key
Value
Authorization
Bearer
<access_token>
Content-Type
application/json
User-Agent
netskope-ce-6.0.1-cls-microsoft-azure-monitor-v2.0.0
Request Body:
{
"RawData": "ID=a39cdxxxx5caexx52fd47a6a cnt=1 device=qP7NPtp5bTHzxxxxdho_AA0B8A97-xxxx-xxxx-AF0E-xxxxxx deviceExternalId=xxxxxx-9798-B907-xxxx-6029DF2F6EB2 dvchost=VMware, Inc. hostname=XXXXX-GNO7JR8 managementId=null os=0 osVersion=10.0.19045 slat=0.0 slong=0.0 smac=xx:0C:29:xx:F7:A1 suid=xxxxPtp5bTHzcR69xxxx suser=abc@test.ai timestamp=0",
"Application": "Netskope CE",
"DataType": "<data_type>",
"SubType": "<sub_type>",
"TimeGenerated": "2025-05-05 17:56:57.823408"
}
Sample API Response:
204 No Content
Performance Matrix
This performance reading is for a Large Stack CE tested on the below-mentioned VM specifications. The below readings are added with the consideration that it will ingest around 10K file size in 2 seconds for Events, Alerts.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Events, Alerts ingested to third-party SIEM
300K EPM
User Agent
netskope-ce-6.0.1-cls-microsoft-azure-monitor-v2.0.0
Workflow
Configure a Log Analytics Workspace.
Configure an Application and get your Tenant ID, Application ID and Client Secret.
Configure a Data Collection Endpoint and get your DCE URI.
Configure a Basic Table in Log Analytics Workspace and get your Data Collection Rule Immutable ID.
Assign a Permission to DCR and DCE.
Configure the Microsoft Azure Monitor plugin.
Configure a Log Shipper Business Rule for Microsoft Azure Monitor.
Configure Log Shipper Log Delivery for Microsoft Azure Monitor.
Validate the Microsoft Azure Monitor plugin.
Watch a Video
Click play to watch a video.
Configure a Log Analytics Workspace
Log in to
Azure
and go to
Log Analytics Workspace
.
Click
Create Tab
.
Select Subscription, and then select an existing Resource Group (or create a new one).
Enter a name for your Log Analytics Workspace, select a region, and then click
Next > Next > Create
.
Configure an Application and get your Tenant ID, Application ID and Client Secret
Log in to Azure with an account that has a Global Administrator role.
Go to
Azure App Registration > New Registration
.
In the registration form, enter a name for your application, and then click
Register
.
Make a copy of the Tenant ID and Application (client) ID on the application page.
Click
Add a Certificate or Secret
, and then click
New client secret
to generate a Client secret. Add a description and Expire time, and then click
Add
.
Copy the value of Secret, as it will only be displayed once.
Configure a Data Collection Endpoint and get your DCE URI
Go to Azure Home and click
Monitor
from the Azure services.
Click
Data Collection Endpoints
on the left panel, and then click
Create
.
Enter a name for the Data collection Endpoint, select a Subscription and Resource Group, select a region (make sure that this region is the region of your Log Analytics Workspace), and then click
Review + create
.
On the Overview tab, copy the Logs Ingestion that will be your Data Collection Endpoint DCE URI.
Configure a Basic Table in Log Analytics Workspace and get your Data Collection Rule Immutable ID
A Custom Log Analytics Table requires sample data to be uploaded in order to create a JSON file on your system with the following content:
[
{
"RawData": {},
"Application":  "",
"DataType": "",
"SubType": "",
"TimeGenerated": "2022-11-01 12:00:00.576165"
}
]
On the Azure home tab, go to Log Analytics Workspace, select the workspace created previously, select
Tables
. Click
Create
and select
New Custom log (DCR based)
.
Enter a name for the table.
For Data Collection Rule, click
Create a new data collection rule
, and then select a Subscription and Resource Group from the dropdown lists. Enter the region for your Log Analytics Workspace, and click
Done
. Make sure to keep Table plan as Basic.
The new Data Collection Rule will be selected in the Data collection rule field. Click
Next
.
On the Schema and Transformation tab, click Browse for Files and select the sample data JSON file you created previously.
Click
Next
and then click
Create
.
A Custom Log Table will be created with the suffix
_CL
.
Note
Here we are changing the table Plan from Analytics to Basic because the Basic log data plan lets you save on the cost of ingesting, and storing high-volume verbose logs in your Log Analytics workspace for debugging, troubleshooting, and auditing.If table plan is not changed and kept as Analytics, the Logs will still be ingested in the Table without any issue.The Analytics table has a configurable retention period from 30 days to 730 days. The Basic table has Retention fixed at eight days.Basic Logs tables retain data for eight days. When you change an existing table’s plan to Basic Logs, Azure archives data that’s more than eight days old, but still within the table’s original retention period.
To get the Data Collection Immutable ID, go to Home, select
Monitor
from the
Azure Services > Data Collection Rules
, and then select the DCR you created while creating the Custom Table.
In the Overview tab, click
JSON View
from the top right corner, and copy the Immutable ID.
Assign a Permission to DCR and DCE
On the Azure Home page, go to
Monitor > Data Collection Endpoint
and select the Endpoint created previously.
Select
Access control (IAM)
and click
Add role assignment
.
From the list of roles, select
Monitoring Metrics Publisher
and click
Next
.
Select a User, group, or service principal for which to assign access.
Click
Select Members
and search for the Application you created in the search box, and then select it.
Click
Review + assign
.
Repeat these same steps to assign permissions to the DCR (Data Collection Rule).
Configure the Microsoft Azure Monitor Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Microsoft Azure Monitor v2.0.0 CLS)
plugin.
Enter a Configuration Name a select a valid Mapping. (Default Mappings for all plugins are available. If you want to create a new mapping, go to
Settings > Log Shipper > Mappings
).
Transform the raw logs is enabled by default, which will transform the raw data on the basis of the Mapping file. Turn it off if you want to send Raw data directly to Azure Monitor.
Click
Next
and enter the Configuration Parameters:
Directory (tenant) ID:
Directory (tenant) ID of your AzureAD Application.
Application (client) ID:
Application (client) ID of your AzureAD Application.
Client Secret:
Client Secret of your AzureAD Application.
DCE URI:
URI of the Data Collector Endpoint.
DCR Immutable ID:
Immutable ID of the Data Collection Rule.
Custom Log Table Name:
Custom Log Table name for ingesting data. Make sure that the Table exists in your Log Analytics Workspace.
Log Source Identifier:
This will be added in Application field of the Custom Log Table.
Click
Save
.
Configure a Log Shipper Business Rule for Microsoft Azure Monitor
In Log Shipper, go to
Business Rules
and click
Create New Rule
.
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
Enter a Folder Name, if any.
Click
Save
.
Configure Log Shipper Log Delivery
(SIEM Mappings)
for Azure Monitor
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select a Source Configuration, Destination Configuration, and Business Rule.
Click
Save
.
After the SIEM mapping is added, the data will start to be pulled from the Netskope tenant and ingested into the Azure Monitor platform.
Validate the Microsoft Azure Monitor Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant.
Go to
Logging
in Cloud Exchange and search for the pulled logs with the filter:
message contain pulled
.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and search for ingested events with the filter:
message contains ingested
. The ingested logs will be filtered.
To validate in Log Analytics Workspace:
In the Azure portal, go to
Log Analytics Workspace
, select the Log Analytics Workspace that you created, and select
Logs
under the General Category on the left panel.
Enter the Custom Log Table Name in the query editor and click
Run
. You can select the Time Range from the top to filter out logs.
You can verify the events/alerts by expanding:
Also, here are the ingested alerts/events in JSON format:
Troubleshooting
If receive error code 403 while configuring the plugin in toast and log message
Ensure that you have the correct permissions for your application to the DCR. Check if you have assigned permissions to the correct Data Collection endpoint as described above. It may take up to 30 minutes to reflect the assigned permissions.
Difficulties in saving the Microsoft Azure Monitor plugin
Despite entering all parameters and clicking the Save button, an error may occur, possibly due to the configuration differs from the specified settings.
What to do:
It could be because of incorrect configuration parameters, just follow the steps in the
Configure a Log Analytics Workspace
.
Not able to see the events on the Microsoft Azure Monitor
Even after successful ingestion of the events, not able to see the events ingested from the plugin. This could be due to one of these reasons:
Incorrect query provided in Log searching.
No events are ingested in the platform.
Or the data you are looking for is outside of the searching Time Range.
What to do:
Check events are ingested in a longer time range.
Check if you have provided the correct query in Log searching.
Check for the logs on the Cloud Exchange for the ingested events.
In this Topic
Microsoft Azure Monitor Plugin for Log Shipper

---
## Microsoft Defender for Cloud Apps Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/microsoft-defender-for-cloud-apps-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:56:56+00:00
**Scraped:** 2026-08-10T07:41:50.626122+00:00

Microsoft Defender for Cloud Apps Plugin for Log Shipper - Netskope Technical Documentation
Microsoft Defender for Cloud Apps Plugin for Log Shipper
This document explains how to configure the Microsoft Defender for Cloud Apps v2.1.1 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin enables you to ingest Netskope Events (Page, Application) in CEF format from the Netskope Tenant to Microsoft Defender for Cloud Apps using Cloud Exchange via the Microsoft Defender for Cloud Apps plugin. The plugin doesn’t support ingesting data in JSON format.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Microsoft Defender for Cloud Apps instance.
Connectivity to the following hosts:
https://security.microsoft.com
and
/
https://portal.azure.com/
Note
Verify your Microsoft Defender instance permissions are secure and not set up for open public access. Only allow access to your cloud storage instance from your Cloud Exchange Host and any other addresses that needs access.
Microsoft Defender for Cloud Apps Plugin Support
This plugin is used to ingest events of type Application and Page to the Governance log page of the Microsoft Defender platform. This plugin
does not support the ingestion of Netskope Alerts and WebTx transactions to the Microsoft Defender platform. The plugin only supports ingesting data in CEF format, sending data in JSON format is not supported.
Data Type
Support
Events
Page
Application
Alerts
Not supported
Logs
Not supported
WebTx
Not supported
Permissions
These permissions are needed for the plugin to configure the Microsoft Defender for Cloud App plugin.
Cloud Discovery Global Admin role required to access Microsoft Defender for Cloud App Instance
Microsoft App Security for OAuth 2.0 (Application context)
Discovery.manage
Discovery.read
API Details
List of APIs Used
API Endpoint
Method
Use Case
/oauth2/v2.0/token
POST
Generate Token
/api/v1/discovery/upload_url/
GET
Initiate file upload – Cloud Discovery API
<initiate_file_upload_response_url>
PUT
Perform file upload – Cloud Discovery API
(obtained from “Initiate file upload”)
/api/v1/discovery/done_upload/
POST
Finalize file upload – Cloud Discovery API
Generate Token
API Endpoint:
https://login.microsoftonline.com/
<tenant_id>
/oauth2/v2.0/token
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cls-microsoft-defender-for-cloud-apps-v2.1.1
Content-Type
application/x-www-form-urlencoded
Payload
Parameter
Value
grant_type
client_credentials
client_id
client_id
client_secret
client_secret
scope
05a65629-4c1b-48c1-a78b-804c4abdd4af/.default
Sample API Response
{
    "token_type": "Bearer",
    "expires_in": 3599,
    "ext_expires_in": 3599,
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiIwNWE2R1QVRFcTkxSzk5QUFBLiIsInJvbGVzIjpbImRpc2NvdmVyeS5tYW5hZ2UiXSwic3ViIjoiNzljMEHIywny8JmtEONTPUcOahramZDIYLL8JBGvUH5V-ebPIrAOnCZGvwcbYbVZy7joFwmjeIK22Er_4eCVDXDAzAWuF5uD-KFZp7DkZNSR06i7OD-Yo6YiGEzAP5fMW8anHREJDwh0OtkMn5GRf15ccuhBhNlGiT17uPNzAct*************************************5_DsDgVK109p1yVTrGTw"
}
Initiate File Upload
API Endpoint:
https://
<tenant_id>
.
<tenant_region>
.contoso.com/api/v1/discovery/upload_url/?filename=my_discovery_file.txt&source=GENERIC_CEF
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cls-microsoft-defender-for-cloud-apps-v2.1.1
Authorization
Bearer
<token>
Accept
application/json
Payload
Parameter
Value
source
GENERIC_CEF
filename
140351985108800-ingestion_file.txt
Sample API Response
{
    "url": "https://prod5usw2console1.blob.core.windows.net/discovery-logs/2023-11/115979866_1701326176744_GENERIC_CEF_140351985108800-ingestion_file.txt?se=2023-12-01T06%3A36%3A16Z&sp=w&sv=2014-02-14&sr=b&sig=7EjuI4qdniikC5ehECtNzjjiaHFQ0FMix5Y1sPDDfhs=",
    "provider": "azure"
}
Perform a File Upload
API Endpoint:
https://
<initiate_file_upload_response_url>
Method:
PUT
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cls-microsoft-defender-for-cloud-apps-v2.1.1
x-ms-blob-type
BlockBlob
Accept
application/json
Payload
N/A
Sample API Response
Status: 201 created
Finalize a File Upload
API Endpoint:
https://
<tenant_id>
.
<tenant_region>
.contoso.com/api/v1/discovery/done_upload/
Method:
GET
Request Body:
{
"uploadUrl":"",
"inputStreamName":""
}
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cls-microsoft-defender-for-cloud-apps-v2.1.1
Authorization
Bearer
<token>
Accept
application/json
Content-Type
application/json
Payload
Parameter
Value
source
GENERIC_CEF
filename
140351985108800-ingestion_file.txt
Sample API Response
{
    "success": true,
    "inputStreamId": "6166e2d26e047397777e71e8",
    "taskId": "656830c12339fba78191038a"
}
Performance Matrix
This performance reading is conducted on a Large Cloud Exchange Stack with these VM specifications. These readings are added with the consideration that it will ingest around 10K events in 3 seconds to the Microsoft Defender for Cloud Apps platform.
Description
Specification
Stack Size
Large
CPU: 16 Cores
RAM: 32 GB
Events ingested to Microsoft Defender for Cloud Apps SIEM
200K EPM
User Agent
netskope-ce-5.0.1-cls-microsoft-defender-for-cloud-apps-v2.1.1
Workflow
Generate the API Token Legacy method.
Generate the Client ID, Tenant ID, and Client Secret for OAuth method.
Create a Data Source.
Configure the Microsoft Defender for Cloud Apps plugin.
Add a Log Shipper Business Rules.
Add a Log Shipper SIEM mappings.
Validate the plugin.
Watch a Video
Click play to watch a video.
Generate the API Token for the Legacy Method (API Token)
Follow the below steps to generate the API Token. You can also refer to this
documentation
to generate the token.
In the Microsoft Defender portal, select
Settings
.
Click
Cloud Apps
.
Under System, click
API tokens
.
Click
Add token
.
Provide a name to identify the token, and click
Generate
.
Copy the token value and save it to use to configure the plugin. If you lose it, you need to regenerate the token. The token has the privileges of the user who issued it. For example, a security reader can’t issue a token that can alter data.
You can filter the tokens by status: Active, Inactive, or Generated.
Generated: Tokens that have never been used.
Active: Tokens that were generated and used within the past seven days.
Inactive: Tokens that were used but there was no activity in the last seven days.
After you generate a new token, you’ll be provided with a new URL to use to access the Defender for Cloud Apps portal.
Generate the Client ID, Tenant ID, and Client Secret for OAuth 2.0 (Application context)
Follow the below steps to generate the Client ID, Tenant ID, and Client Secret for configuring the Microsoft Defender for Cloud Apps plugin using the OAuth 2.0 (Application context).
Log in to your Microsoft
Azure
portal.
Search for and select
App registrations
.
Click
New registration
.
Enter your Application Name and click
Register
.
Save the Client ID and Tenant ID to use it in your plugin configuration.
Click
Certificate and secrets
to generate the Secret ID.
Click
New client secret
, enter the description and expiration time, and then click
Add
.
Copy the Value in the Client Secret field; make sure to store the Client value safe, as it won’t be visible again.
Click
API permissions
from the left panel.
Click
Add permission
to provide the necessary permission for ingesting the data.
Go to
APIs my organization uses
, search for the Microsoft Cloud App Security, and then click it.
Select
Application permissions
.
Select the
discovery.manage
and
discovery.read
permissions and then click
Add permission
.
Make sure to provide the admin consent.
Create a Data Source
In Microsoft Defender, go to
Settings > Cloud Apps
.
Under Cloud Discovery, click
Automatic log upload
.
Click
Add data source
.
Enter the name of the data source, select
Generic CEF log
for Source, and
Syslog – TCP
for Receiver type. Click
Add
.
Configure the Microsoft Defender for Cloud Apps Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and select the
Microsoft Defender for Cloud Apps v2.1.1 (CLS)
plugin box.
Enter a configuration name, and make sure the Microsoft Defender for Cloud Apps Default Mapping is selected. Disable the toggle button to transform the logs to ingest the data in JSON format, or keep it enabled if you want to ingest the data in CEF format.
Click
Next
, and then enter the Confirmation Parameters:
For Legacy Method (API Token)
Portal URL: URL for your Microsoft Defender for Cloud Apps platform (without https://).
Authentication Method: Legacy Method (API Token).
API Token: API token for authentication in the Microsoft Defender for Cloud Apps portal. The API token can be generated from the
Settings > Cloud Apps > API Tokens
page. The API token is required only if the Legacy Method (API Token) method is selected.
Data Source: The data source where traffic logs from Log Shipper are to be uploaded. The data source can be found at
Settings > Cloud Apps > Cloud Discovery > Automatic Log Upload
.
For OAuth 2.0 Method (Application context)
Portal URL: URL for your Microsoft Defender for Cloud Apps platform (without https://).
Authentication Method: OAuth 2.0 (Application context).
Client ID: Client ID of your Azure application. The Client ID can be found from
App registrations > App Name > Overview
page. This is required only if the OAuth 2.0 (Application context) method is selected.
Tenant ID: Tenant ID of your Azure application. The Tenant ID can be found from
App registrations > App Name > Overview
page. It is required only if the ‘OAuth 2.0 (Application context)’ method is selected.
Client Secret: Client Secret of your Azure application. The Client Secret can be generated from
App registrations > App Name > Certificates & secrets
page. This is required only if the OAuth 2.0 (Application context) method is selected.
Data Source: The data source where traffic logs from CLS are to be uploaded. The data source can be found at
Settings > Cloud Apps > Cloud Discovery > Automatic Log Upload
.
Click
Save
. Plugin configuration will be available on the
Cloud Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for Microsoft Defender
Go to
Log Shipper > Business Rules
.
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
When finished, click
Save
.
Configure a Log Shipper SIEM Mapping for Microsoft Defender
Go to
Log Shipper > SIEM Mappings
and click
Add SIEM Mapping
.
Select the Source plugin (Netskope CLS), Destination plugin (Microsoft Defender for Cloud Apps), and a business rule, and then click
Save
.
After the SIEM mapping is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Microsoft Defender for Cloud Apps platform.
Validate the Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant.
Go to
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and search for ingested events with the filter
message contains ingested
, and the ingested logs will be filtered.
To validate the push on the Microsoft Defender platform:
Go to Microsoft Defender for Cloud Apps Platform.
On the left panel, under
Cloud apps
, click
Governance log
.
Check the files to verify the ingested data is listed.
Go to
Settings > Cloud apps > Automatic log upload
. Verify the count of the data source that you have provided while configuring the plugin.
To view the extracted users from the logs, go to
Home > Cloud Discovery
.
Troubleshooting the Microsoft Defender for Cloud Apps Plugin
Receiving the certificate verification failed error while ingesting the indicators
If you encounter any error with error code “CLS_1005” while ingesting the events after setting up SIEM mapping from Netskope to Microsoft Defender for Cloud Apps.
It might be due to the Microsoft Defender for Cloud Apps Portal URL being blocked on your machine.
What to do:
To resolve this issue, contact your IT support team for assistance to unblock your URL.
Facing issues in the existing plugin configuration after the plugin update
If you have an existing Microsoft Defender for Cloud Apps plugin configured, you might face the below issue after you update your Microsoft Defender for Cloud Apps plugin:
CE goes blank while editing the existing plugin configuration
.
It is possible to encounter this issue in CE 4.2.0 and CE 5.0.0 if the existing plugin configuration is edited after the user goes on the Configuration Parameters page post the plugin update.
What to do:
Verify your CE version and accordingly follow the below-mentioned workarounds.
For 4.2.0:
The only solution for 4.2.0 is to delete the existing plugin configuration and create a new one.
For 5.0.0:
If the plugin hasn’t already been updated, make sure to follow the below steps and save the plugin configuration while updating, not skip it.
If you are using the
Legacy Method (API Token)
and want to continue using the Legacy Method, make sure your Authentication Method dropdown has
Legacy Method (API Token)
selected before you save the configuration in the plugin update on the Plugin Repository page.
If you want to use the
OAuth 2.0 (Application context)
method, make sure to select it in the Authentication Methods dropdown and provide all configuration parameters. Do not skip.
Either way one of the solutions for any of the methods during the plugin update on the Plugin Repository page is to save the plugin update and not skip it.
If you have already updated the plugin and have selected skip while updating the plugin, delete the existing plugin configuration and configure a new Microsoft Defender for Cloud Apps plugin.
Receiving the File Upload error while ingesting the events to the Microsoft Defender for Cloud Apps platform
If the plugin is configured correctly and yet the below error is received, it means that the Data Source provided in the plugin configuration is not available on the Microsoft Defender for Cloud Apps platform.
What to do:
Go to your Microsoft Defender for Cloud Apps platform.
Go to the Automatic Log upload from
Settings > Cloud Apps > Cloud Discovery
.
Search for the Data Source name used in the plugin configuration. If the data source name is not found, create a new Data Source.
If the Data Source name is available, make sure the exact data source name is used.
Difficulty in tracking the ingested data
If any of the data ingestion is hard to track due to multiple files created on the Microsoft Defender platform, you can simply search the file name.
What to do:
Go to
Logging
in Cloud Exchange and check the API Request logs from the Microsoft Defender for Cloud Apps plugin. The logs have the file name that would be created on the Microsoft Defender for Cloud Apps platform for ingested data. Copy the file name and search for the file on the Microsoft Defender for Cloud Apps platform in the Governance Log under Cloud apps.
Limitations
There is one limitation imposed by Microsoft Defender for Cloud Apps: it can only transmit files with a maximum size of 64 MB. If this limit is exceeded, an error indicating that the file is larger than 64 MB will be encountered in the plugin while ingesting the data.
There is a limitation regarding the
data retention
on the Microsoft Defender for Cloud Apps: If the ingested data is older than 90 days, it will show a failed status on the Governance Log page where the events are ingested.
In this Topic
Microsoft Defender for Cloud Apps Plugin for Log Shipper

---
## Rapid7 Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/rapid7-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:42:45+00:00
**Scraped:** 2026-08-10T07:42:33.299889+00:00

Rapid7 Plugin for Log Shipper - Netskope Technical Documentation
Rapid7 Plugin for Log Shipper
This document explains how to configure your Rapid7 v3.1.1 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (Anomaly, Legal Hold, Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Quarantine, Remediation, UBA, Watchlist, CTEP), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint), Web Transaction data, and CE logs (Debug, Information, Error, Warning) to Rapid7 in JSON and CEF format.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming plugin
already configured (for pulling WebTx from the Netskope Log Streaming plugins)
A Netskope Cloud Exchange tenant with the
Syslog for CE
plugin already configured (for pulling CE logs).
A Rapid7 server.
Connectivity to the following host:
https://insight.rapid7.com/
.
Rapid7 Plugin Support
The Rapid7 plugin is used to ingest all the Alert, Events, WebTx (via Netskope LogStreaming), and CE Logs in JSON and CEF format to the specified Rapid7 server.
Data Type
Support
Events
Yes (Audit, Application, Infrastructure, Network, Incident, Page, Endpoint) The ingestion of the Endpoint event type is supported starting with Cloud Exchange version 5.1.0.
Alerts
Yes (Anomaly, Legal Hold, DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA)
WebTx Logs
Yes (via Netskope Log Streaming)
Syslog CE Logs
Yes (Info, Debug, Warning, Error)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
The ingestion of Endpoint event type is supported from Cloud Exchange version 5.1.0.
API Details
The plugin uses a logging 3rd-party library to push the data to the Syslog collector.
Library: logging
This module defines functions and classes which implement a flexible event-logging system for applications and libraries.
The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.
Refer to the official documentation for more information on the logging library:
https://docs.python.org/3/library/logging.html
.
List of Methods Used
Method:
logging.getLogger(name=None)
Return a logger with the specified name or, if the name is None, return a logger which is the root logger of the hierarchy
All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
Method:
setLevel(level)
Sets the threshold for this logger to level. Logging messages that are less severe than the level will be ignored; logging messages that have a severity level or higher will be emitted by whichever handler or handlers service this logger, unless a handler’s level has been set to a higher severity level than the level.
Method:
handlers
The list of handlers is directly attached to this logger instance.
Note that this attribute should be treated as read-only; it is normally changed via the addHandler() and removeHandler() methods, which use locks to ensure thread-safe operation.
Method:
addHandler(hdlr)
: Adds the specified handler
hdlr
to this logger.
Method:
removeHandler(hdlr)
: Removes the specified handler
hdlr
from this logger.
Performance Matrix
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to SIEM
~200K EPM
Workflow
Create a collector and event source on Rapid7.
Configure the Rapid7 plugin.
Configure a Log Shipper Business Rule for Rapid7.
Configure Log Shipper Log Delivery for Rapid7.
Validate the Rapid7 plugin.
Click play to watch a video.
Get your Rapid7 Server and Port Information
Go to your Rapid7 instance at
https://insight.rapid7.com
.
Log in to Rapid7.
Click
Data Collection
,
Collectors
and then click
Download Collector
. Download the Collector for your OS.
Install the Collector on your machine. (Installation Steps:
Collector Installation and Deployment | InsightIDR Documentation
)
Click
Data Collection
,
Event Sources
, and then click
Add Event Source
.
Search for and select the
Rapid7 Custom Logs
box.
Name the Event Source and select the Collector you have activated. Enter a Port Number and select a Protocol.
Click
Save
.
Click
Data Collection Management
, and then
Event Sources
to see the configured Event Source.
Copy the server IP and port number. You will need these to configure the Rapid7 plugin.
Configure the Rapid7 Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Rapid7 v3.1.1 (CLS)
plugin.
Enter a Configuration Name and make sure you have the Rapid7 Default Mapping file selected. If you need custom mapping, click
Create New Mapping
. For JSON format, disable
the logs will be transformed
toggle.
Click
Next
.
Select and enter these parameters:
Rapid7 Server
: IP address/FQDN of the Rapid7 server where data will be ingested.
Rapid7 Protocol
: Protocol to be used while ingesting data.
Rapid7 Port
: Configured Event Source port on Rapid7.
Rapid7 Certificate
: The certificate is required only for the TLS protocol.Log Source Identifier: The prefix to be added for the logs.
Click
Save
. This plugin configuration will be available on the
Log Shipper > Plugins
page.
Configure Log Shipper Business Rules for Rapid7
Go to
Log Shipper > Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Enter a Rule Name and select the filters to use. Enter a
Folder Name
if any.
Click
Save
.
Configure Log Shipper SIEM Mappings for Rapid7
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (CLS Netskope), Destination plugin (CLS Rapid7), and a business rule.
For WebTx, select the Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming), and Destination plugin (CLS Rapid7).
For Logs sharing, select the Source plugin (CLS Syslog for CE), and Destination plugin (CLS Rapid7).
Click
Save
.
After the Log Delivery configuation is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Rapid7 platform.
Validate the Rapid7 Plugin
Validate the Pull
To validate the pulling of Events, Alerts, logs, and Webtx from the Netskope tenant, go to
Logging
and search for the pulled logs.
Validate the Push
To validate on Cloud Exchange, go to
Logging
and search for ingested Events, Alerts, WebTx, and Logs with the filter
message contains ingested
. The ingested logs will be filtered.
To validate the push on the Rapid7, log in to the Rapid7 platform and click
Log Search
. Search the logs by filtering from time range. Here are screenshots of data ingested in CEF format.
Here are screenshots of data ingested in JSON format.
Troubleshooting the Rapid7 Plugin
An error occurred while configuring the Rapid7 Plugin
Despite entering all parameters and clicking the
Save
button, an error may occur, possibly due to one of these reasons:
The server/port configuration may differ from the specified settings (Netskope CE/Rapid7)
The port is not exposed on the Rapid server.
What to do
:
In Rapid7, go to
Data Collection> Event Sources
and check the Port of the Event Source.
Expose the Port on the Rapid7 server.
Error occurred while ingesting data from CE to Rapid7
If you are unable to push alerts/events/logs/
webtx[via Netskope LogStreaming]
data on the Rapid7 platform, it could be due to one of these reasons:
Port is deleted/disabled on the Rapid7 platform.
Event Source has been stopped on the Rapid7 platform.
What to do
:
Make sure the port is present and enabled. If not, create a new port.
Make sure that Event Source is running.
If ingested data is not reflected on the Rapid7 Platform
If you are unable to view alerts/events/logs/webtx data on the Rapid7 platform, it could be due to one of these reasons.
The filter is not correct on the Rapid platform.
There might be any error, but UDP is selected in the Port while configuring the Rapid7 plugin.
What to do
:
Make sure Data is searched using the correct filter/time range.
Make sure to select the TCP port to see if there is any issue.
In this Topic
Rapid7 Plugin for Log Shipper

---
## QRadar Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/qradar-plugin-for-log-shipper/
**Last Modified:** 2026-05-28T03:45:39+00:00
**Scraped:** 2026-08-10T07:42:34.498491+00:00

QRadar Plugin for Log Shipper - Netskope Technical Documentation
QRadar Plugin for Log Shipper
This document explains how to configure your QRadar integration with the Log Shipper module of the Netskope Cloud Exchange platform. This integration allows pushing alerts, events, and WebTx from Netskope to the QRadar platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
A QRadar instance.
Note
Verify your QRadar instance permissions are secure and not set up for open public access. Only allow access to your cloud storage instance from your Cloud Exchange Host and any other addresses that need access.
QRadar Plugin Support
Data Type
Support
Events
Yes
Alerts
Yes
WebTx
Yes (via Netskope Log Streaming)
Logs
Yes
All Netskope events, alert logs, and web transaction logs will be shared.
Note
Incident event type is supported from Core version 4.1.0.
CTEP alert type will be supported from Core version 4.2.0
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
API Details
The plugin uses a
logging
third-party library to push the data to the Syslog collector.
Refer to the official documentation for more information on the logging library.
https://docs.python.org/3/library/logging.html
Performance Matrix
Logs Ingested
Time Taken
9940000
2 hours
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Alerts/Events
~ 6 MBps
Workflow
Configure your QRadar Server, Port, and TLS Certificate information.
Configure the QRadar Plugin.
Configure Log Shipper Business Rules for QRadar.
Configure Log Shipper Log Delivery for QRadar.
Configure the WebTx Mappings (optional).
Validate the QRadar plugin.
Click play to watch a video.
Configure your QRadar Server, Port, and TLS Certificate Information
To create a log source in QRadar (through a Log Source Management app) for ingesting data with TCP/UDP/TLS protocol from Netskope, perform following steps:
Download and install the Netskope Security Cloud DSM from
here
Go to the Log Source Management App via the Admin Panel.
When a separate window opens, click
+ New Log Source
.
Select
Netskope
for the Log Source type.
For receiving data sent through TCP/UDP protocol from Log Shipper, select protocol type as
Syslog
; for receiving data sent through TLS select protocol type as
TLS Syslog
.
Note
The Default port for TCP/UDP (Syslog) in QRadar is 514, and for TLS Syslog is 6514.
For more information, refer:-
https://www.ibm.com/docs/en/qsip/7.4?topic=qradar-port-usage
In the section under Configure Log Source parameters, enter the name of the log source, keep the log source enabled, and the Coalescing events checkbox disabled.
In the section under Configure the protocol parameters, enter a Log Source Identifier, like
netskopece
.
Once you have successfully deployed a log source after that take the TLS certificate by running the command (
cat /opt/qradar/conf/trusted_certificates/syslog-tls.cert
) from the QRadar VM where the log source is deployed. This TLS certificate is required while configuring QRadar Plugin with TLS Protocol.
For the field Max Payload Length, we have observed that events are getting truncated even if we set the value to maximum, like
32768
, in this field. To avoid truncation of payload, we recommend changing payload length by following the steps given
here.
Click
Skip Test
and then
Finish
. Next, deploy a log source.
Deploy Log Source
Click
Deploy Changes
.
Configure the QRadar Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
QRadar
box to open the plugin creation pages.
Enter a Configuration Name.
Select a valid Mapping. (Default Mapping for all plugins are available.
Transform the raw logs: If enabled, Raw logs will be transformed using selected mapping file, else raw logs will be sent to SIEM. The ingestion may be affected if the SIEM does not accept raw logs format.
Click
Next
and enter a QRadar Server, select a QRadar Format and QRadar Protocol, and then enter your QRadar Port and QRadar Certificate information.
Enter the information for yourQRadar Server, select the QRadar Format and QRadar Protocol, and then enter QRadar Port and QRadar Certificate.
Enter a Log Source Identifier. The Default value would be
netskopece
. The Log Source Identifier should not contain the whitespaces. This will be added as a prefix to all logs.
Click
Save
.
Configure Log Shipper Business Rules for QRadar
Go to
Log Shipper > Business Rules.
Click
Create New Rule
.
Enter a Rule Name and select the filters to use.
Click
Save
.
Configure Log Shipper Log Delivery for QRadar
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery
Configuration
.
For alerts and events, select the Source plugin (Netskope CLS), Destination plugin (Datadog), a business rule, and then click
Save
.
For WebTX select Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming), Destination plugin (CLS Datadog)
, a business rule, and then click
Save
.
Validate the QRadar Plugin
To validate the plugin workflow, you can check from Netskope Cloud Exchange and from your QRadar instance.
Validate in Netskope Cloud Exchange
Go to
Logging.
Validate in QRadar
Go to your QRadar instance.
Click
Log Activity
.
Apply filters to see specific logs.
You can see all logs there.
In this Topic
QRadar Plugin for Log Shipper

---
## Secureworks Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/secureworks-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T03:48:19+00:00
**Scraped:** 2026-08-10T07:42:49.843667+00:00

Secureworks Plugin for Log Shipper - Netskope Technical Documentation
Secureworks Plugin for Log Shipper
This document explains how to configure your Secureworks Taegis XDR instance with the Cloud Log Shipper module of the Netskope Cloud Exchange platform.
For Secureworks documentation, go to:
https://docs.ctpx.secureworks.com/integration/connectCloud/netskope/
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming plugin
already configured (for pulling WebTx from the Netskope Log Streaming plugins).
A Secureworks instance.
Connectivity to the following host:
https://ctpx.secureworks.com/
.
Secureworks Plugin Support
This integration supports:
Events
Alerts
WebTx (via Netskope Log Streaming)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Workflow
Get your Secureworks Collector Information.
Configure the Secureworks plugin.
Configure the Log Shipper Business Rules for Secureworks.
Configure Log Shipper Log Delivery for Secureworks.
Validate the  Secureworks plugin.
To watch a demo, click play.
Get your Secureworks Collector Information
Go to your Secureworks instance:
https://ctpx.secureworks.com/login
Enter your login credentials.
Select your tenant from the top bar (highlighted below):
Go to
Integrations > Data Collectors
.
Click
Add Collector
to create a collector. Mainly, two types of collector can be created, on-premises and cloud-hosted.
Click
Next
and add the required details.
Click
Create Collector
.
Download the .ova file and follow the
Network Collector installation
instructions. After successful installation, the collector status will be online.
Click on the created collector and copy the IP Address. You will need this IP address as Secureworks Server in Netskope CLS configuration
To use the collector on TLS, go to
Applications >TLS enabled Syslog
.
Click
Settings > Configure
.
Select the port
6514
from the dropdown.
Follow the steps
TLS Enabled Syslog Docs.
to get the TLS certificates.
Upload the PKCS12 file, enter your password, and click
Save
.
Communication from Netskope to Secureworks will be successful on port 6514.
Configure the Secureworks Plugin
In Cloud Exchange, go to
Setting > Plugin Store
.
Search for and select the
Secureworks v1.0.0 (CLS)
plugin.
Enter a Configuration Name.
Select a valid
Mapping
. (Default Mappings for all plugins are available.)
Click
Next
.
Enter your Collector IP address for the Secureworks Server, select the Secureworks Format and Secureworks Protocol, and then enter the Secureworks Port and Secureworks Certificate.
Enter a Log Source Identifier. The Default value would be
netskopece
. The Log Source Identifier should not contain whitespaces. This will be added as a prefix to all logs.
Click
Save
.
Configure Log Shipper Business Rules for Secureworks
Go to
Log Shipper > Business Rules
.
Click
Create New Rule
.
Enter a Rule Name and select the filters to use.
Click
Save
.
Configure Log Shipper Log Delivery for Secureworks
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (Netskope CLS), Destination plugin (CLS Secureworks), your business rule, and then click
Save
.
For WebTx, select the Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming), and Destination plugin (CLS Secureworks), your business rule, and then click
Save
.
Validate the Secureworks Plugin
To validate the plugin workflow, you can check in Netskope Cloud Exchange and in your Secureworks instance.
Validate in Netskope Cloud Exchange
Go to
Logging.
Validate in Secureworks
There are two ways:
Go to
Integrations > Data Sources
.
You can also check the same from
Integrations > Data Collectors
. Thereafter, click on your data collector and enter the required query to search the data.
To validate the Raw data user, go to Advanced search and write the query per the suggestions on the left.
In this Topic
Secureworks Plugin for Log Shipper

---
## Syslog Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/syslog-plugin-for-log-shipper/
**Last Modified:** 2026-07-17T21:39:09+00:00
**Scraped:** 2026-08-10T07:43:10.062896+00:00

Syslog Plugin for Log Shipper - Netskope Technical Documentation
Syslog Plugin for Log Shipper
Release Notes
4.1.2
Changed
Updated WebTx mappings to support Transaction Events universal field updates.
Fixed
Fixed ingestion for selected fields in JSON format.
4.1.1
Added
Added support for skipping the priority from the JSON-formatted data.
4.1.0
Added
Added support for skipping the timestamp and log source identifier fields in JSON-formatted data.
Updated the mappings for Network events and Audit events.
4.0.1
Fixed
Fixed CEF transformation for nested JSON fields in data.
4.0.0
Added
Added support for invoking mapping validation separately.
Changed
Enhanced the efficiency of database interactions.
3.3.0
Added
Added support for the content and device alert type.
Added support for clientstatus and BWAN events.
3.2.2
Added
Enhancement in the error handling.
Added support for the endpoint event type. To pull and ingest this event type update your CE version to 5.1.0.
3.2.1
Added
Added support for JA3 fields in WebTx and Application events.
3.2.0
Added
Added the RFC fields prefix in the JSON formatted data.
Added support to send Debug logs.
3.1.0
Added
Added support for WebTx JSON format to send specific fields to SIEM platform.
3.0.0
Added
Added Support for the incident event type. To pull and ingest this event type update your CE version to 4.1.0.
Added Support for the CTEP alert type. To pull and ingest this alert type update your CE version to 4.2.0.
Added support for WebTx format3.
Changed
Changed error logs to warning if a single field is skipped.
Fixed
Fixed JSON format of raw data.
Removed
Removed priority from the Syslog message for the logs that are not transformed in CEF.
2.0.1
Added
Added Incident ID mapping field in all alerts and events.
2.0.0
Added
Added support to send raw data to the SIEM Platform.
1.2.2
Fixed
Fixed Severity mappings for Audit events.
1.2.1
Added
Added support for Syslog service plugin for Netskope CE.
1.2.0
Added
Added Log Source Identifier as configurable field.
1.1.1
Added
Updated WebTx mappings.
1.1.0
Added
Support for web transaction logs ingestion.
Removed
Valid extensions from plugin configuration.
Transformations from the plugin.
1.0.0
Added
Initial release.
This document explains how to configure the Syslog v4.1.2 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status), BWAN Events (Authentication, Audit, Client, Gateway, System), WebTx and Logs (Debug, Information, Error, Warning). The data will be ingested in the SIEM platform. This plugin supports ingestion in CEF and JSON format.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
BWAN plugin
already configured.
The
AWS Log Streaming plugin
and
Azure Log Streaming plugin
already configured, for ingesting alerts, events and WebTx from the Netskope Log Streaming plugin.
A Splunk instance.
Connectivity to a syslog server.
Note
Endpoint event type requires minimum CE version to be 5.1.0. BWAN events, Events of type Client Status, and Alerts of type Device and Content requires minimum CE version to be 5.1.1.
Syslog Plugin Support
The Syslog plugin is used to ingest all the Alert, Events, WebTx, and Syslog CE Logs in CEF and JSON format to the specified syslog server. This plugin also supports ingestion of alerts, events and WebTx from the Netskope Log Streaming plugins.
Data Type
Support
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status)
Alerts
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content)
Syslog CE Logs
Yes (Info, Error, Warning, Debug)
BWAN Events
Yes (Authentication, Audit, Client, Gateway, System)
WebTx
Yes (via Netskope LogStreaming)
API Details
The plugin uses a logging third-party library to push the data to the Syslog collector.
Library: logging
This module defines functions and classes which implement a flexible event-logging system for applications and libraries.
The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.
Refer to the official documentation for more information on the logging library:
https://docs.python.org/3/library/logging.html
.
List of Methods Used
Method:
logging.getLogger(name=None)
Return a logger with the specified name or, if the name is None, return a logger which is the root logger of the hierarchy
All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
Method:
setLevel(level)
Sets the threshold for this logger to level. Logging messages that are less severe than the level will be ignored; logging messages that have a severity level or higher will be emitted by whichever handler or handlers service this logger, unless a handler’s level has been set to a higher severity level than the level.
Method:
handlers
The list of handlers is directly attached to this logger instance.
Note:
This attribute should be treated as read-only; it is normally changed via the addHandler() and removeHandler() methods, which use locks to ensure thread-safe operation.
Method:
removeHandler(hdlr
):
Removes the specified handler
hdlr
from this logger.
Method:
addHandler(hdlr)
:
Adds the specified handler
hdlr
to this logger.
Performance Matrix
This performance reading was conducted on a Large Stack in Cloud Exchange with these VM specifications. These readings are added with the consideration that it will ingest around 10k Netskope alerts/events in 2 seconds to the SIEM.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to SIEM
~200k EPM
WebTx (via Netskope LogStreaming) ingested to SIEM (uncompressed)
~165k EPM
Performance for Alerts/Events was conducted using the Netskope Log Shipper plugin, and for WebTx, the Azure Netskope Log Streaming plugin was used.
Workflow
Create a Data Input on Splunk.
Configure the Syslog Plugin for the Splunk integration.
Configure a Log Shipper Business Rule for the Splunk integration.
Configure Log Shipper Log Delivery for the Splunk integration.
Validate the Syslog with Splunk plugin.
Watch a Video
Click play to watch a video:
Create a Data Input on Splunk
Follow the steps in this
Document
to install Splunk.
Log in to the Splunk instance.
From the dashboard, go to
Settings > Data inputs
.
Click
Add new
for the TCP input.
Add your port and click
Next
. Note that the selected port must be exposed on the host machine to ingest the data to Data inputs.
Select the Source type if you already have any, or click
New
to create a new Source type.
Enter the Source type. Select the Source Type Category based on your requirement, or keep it as it is.
Scroll down to Index. If you already have any index that you want to use. Select it from the Index dropdown; otherwise, click
Create a new index
. Add an Index Name, and click
Save
, and then click
Review
.
Review all details and click
Submit
.
Click
Start Searching
.
Configure the Syslog Plugin for the Splunk Integration
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Syslog v4.1.2 (CLS)
plugin.
Enter a plugin configuration name and make sure you have the Syslog Default Mapping file selected if you want to use CEF format.
To ingest data in JSON format, select format as
JSON
under Basic Information.
Click
Next
and enter the Configuration Parameters:
Syslog server:
IP address/FQDN of the Syslog server where the data will be ingested.
Syslog Protocol
:  Protocol to be used while ingesting data.
Syslog Port:
The port used while creating the Data input configuration on Splunk.
Syslog Certificate:
Certificate is required only for TLS protocol.
Log source Identifier:
The identifier added as a prefix to all the logs.
Exclude Timestamp Field:
Select
Yes
to ingest the data without the timestamp field. This option is only applicable to JSON-formatted data.
Exclude Log Source Identifier Field:
Select
Yes
to ingest the data without the Log Source Identifier field. This option is only applicable to JSON-formatted data.
Exclude Priority Field:
Select
Yes
to ingest the data without the priority field in the syslog message. This option is only applicable to JSON-formatted data.
If Exclude Priority Field is kept as
No
, then it will use the default priority as 14 (Info) for all data.
Click
Save
. The plugin configuration will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for the Splunk Integration
Go to the Business Rule page.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Click
Save
.
Configure Log Shipper Log Delivery for the Splunk Integration
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (CLS Netskope or any other source plugin), Destination plugin (CLS Syslog), your business rule, and click
Save
.
For WebTx, select the Source plugin (CLS Netskope WebTx) and Destination plugin (CLS Syslog).
For Logs sharing, select the Source plugin (CLS Cloud Exchange Logs) and Destination plugin (CLS Syslog).
After the Log Delivery is added, the data will start to be pulled from the Netskope tenant or source platform, then transformed and ingested into the Syslog platform.
Validate the Syslog with Splunk Plugin
Validate the Pull
To validate the pulling of Events, Alerts, logs, BWAN events and Webtx from the Netskope tenant.
Go to the
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events, Alerts, WebTx & Logs with the filter
“message contains ingested”
. The ingested logs will be filtered.
To validate the push on the Splunk:
Log in to Splunk Platform.
Click
Search & Reporting
.
Enter the source and Protocol along with: and port along with Log Source Identifier (Example:
source=”tcp:5001″ index=”syslogdemo” sourcetype=”dev” netskopece
)
Here are examples of ingested Alerts:
Here are examples of ingested Events:
This is how BWAN Events look from plugin to Splunk:
This is how Syslog for CE Logs look from plugin to Splunk:
This is how WebTx data look from plugin to Splunk:
This is how Data looks when shared in JSON from plugin to Splunk (unparsed format):
Here is how the data will look if ingested in JSON format without Timestamp and Log source identifier fields:
Below is how the data will look if ingested in JSON format without Priority Field:
Sample ingested data in JSON format with custom mapping having only selected fields:
Troubleshooting the Syslog Plugin
An error occurred while configuring the Syslog Plugin
Despite entering all parameters and clicking
Save
, an error may occur, possibly due to one of these reasons:
The server/port configuration may differ from the specified settings (Netskope CE/Splunk).
The port is not exposed on the Splunk server.
What to do
:
In the Splunk Platform, go to
Settings
and click
Data inputs > TCP
(whichever configuration you have used). Check that both are the same.
Expose the Port on the Splunk server.
Nested fields are not mapped properly while ingesting data via Syslog plugin
On the older versions of Syslog plugin, you will not be able to map the nested fields. This issue is resolved in the latest version of the Syslog plugin.
What to do:
Upgrade the Syslog plugin to Syslog v4.0.1 or above.
Note
Users will not be able to directly map any fields inside a list. They can only map the nested fields present inside a JSON value.
An error occurred while ingesting data from Cloud Exchange to Syslog
If you are unable to push alerts/events/logs/webtx data on the Syslog platform, then it could be due to one of these reasons:
Port is deleted/disabled on the Syslog platform.
Splunk server storage is full.
What to do
:
Make sure the port is present and enabled. If not, then create a new port.
Make sure to clean the event data if not necessary, or increase the storage of the Splunk server.
If ingested data is not reflected on the Syslog Platform
If you are unable to view alerts/events/logs/webtx data on the Syslog platform, it could be due to one of these reasons:
The filter is not correct on the Splunk platform.
There might be any error, but UDP is selected in the Port while configuring the syslog plugin, so ingested logs are not visible.
What to do
:
Make sure Data is searched using the correct filter.
Make sure to select the TCP port to check if there is any issue.
Webtx data skipped due to parser order of Configured Log Streaming or disabled x-cs-timestamp field
If the Webtx data is not ingested to the destination it may be due to incorrect mapping used while configuring the Syslog plugin or disabled x-cs-timestamp field. The default mappings for Syslog v4.1.2 are compatible with parser order 2.
What to do
:
Update the parser order of your Log Streaming on the Netskope tenant to
Parser order 2
, or use the custom mapping. To update the parser order:
Edit the WebTx stream then under Transaction Events, click
Manage Fields
, and change the parser order to
Parser order 2
.
Also, make sure that the x-cs-timestamp field is enabled
Network Event skipped due to unexpected type for Network Session ID field
If you are not able to get value for the Network session ID field, then it could be due to  using an old syslog plugin where the network session ID field is of number type.
What to do
:
Update to latest syslog plugin or update network session id field to string type to handle non-numeric data.
To update mapping, go to
Settings > Log Shipper
and clone the
Syslog Default Mappings
. Add a name for the cloned mapping.
Click
Events > Network > Extension > networkSessionId > Select Type “String”
, and then click
Save
.
Use the updated mapping file in plugin configuration.
Known Behavior
You may encounter escape characters in the ingested data due to several factors, such as accented characters (in English), characters of languages other than English, non-breaking spaces, newline characters, and other special formatting symbols.
Here, there are Japanese characters that were ingested, which looked like
\\u4ed5\\u4e8b
in the below log.
Example:
<14>Apr 07 09:32:56 alltypes CEF:0|Netskope|Mock Netskope Tenant|NULL|application|NULL|Unknown|act=Download appcategory=Cloud Storage applicationType=nspolicy browser=unknown
\\u4ed5\\u4e8b
cci=89 ccl=high device=Other dst=ef82::1a12:1234:1b12 os=unknown requestClientApplication=Box sourceServiceName=Box src=ef82::1a12:1234:1b12 suser=support@netskope.com timestamp=1743736484
Ingested content may have missing fields/data if you set the
Pull DLP Incident Forensics
field as
Yes
, or the content of any of the fields is very large.
We have observed that some of the fields are very large and they have length beyond the maximum length supported by the Netskope Cloud Exchange. Due to this, you may encounter the below warning and you may observe that the ingested event is incomplete as rest of the values will be skipped.
We tested the plugin using a Splunk instance for data ingestion and observed the following behavior:
When the Exclude timestamp field is set to Yes, the data is ingested using the current local timestamp.
When the Exclude timestamp field is set to No, the data is ingested using the current UTC timestamp.
In this Topic
Syslog Plugin for Log Shipper

---
## Update Configured Log Shipper Plugins
**URL:** https://docs.netskope.com/en/update-configured-log-shipper-plugins-2/
**Last Modified:** 2025-10-31T05:07:49+00:00
**Scraped:** 2026-08-10T07:43:23.726788+00:00

Update Configured Log Shipper Plugins - Netskope Technical Documentation
Update Configured Log Shipper Plugins
Only write-access users can update configured plugins.
A write-access user can edit, disable/enable and delete the configuration using options available on created configuration by selecting the edit icon (pencil), the disable icon (circle and slash), or the delete icon (trash).
In this Topic
Update Configured Log Shipper Plugins

---
## Get Log Upload Token
**URL:** https://docs.netskope.com/en/get-log-upload-token/
**Last Modified:** 2025-08-31T01:39:22+00:00
**Scraped:** 2026-08-10T07:45:51.819449+00:00

Get Log Upload Token - Netskope Technical Documentation
Get Log Upload Token
This endpoint returns the log upload token. Only the token parameter is needed.
POST https://
<tenant-URL>
/api/v1/uploadtoken
{    
    "token": "f32a973eddd7bc1602fc0f48dc0a"
}
In this Topic
Get Log Upload Token

---
## Import and Export CSA Custom Rules
**URL:** https://docs.netskope.com/en/import-and-export-csa-custom-rules/
**Last Modified:** 2025-08-31T01:39:40+00:00
**Scraped:** 2026-08-10T07:46:00.338318+00:00

Import and Export CSA Custom Rules - Netskope Technical Documentation
Import and Export CSA Custom Rules
Use this endpoint to manage the custom rules for CSA. Custom rules are the rules defined by domain specific language (DSL) specifications. This endpoint enables you to import and export your custom rules to and from the Netskope UI for use in profiles and policies. Whenever you change a rule, be sure to click
Apply Changes
in the Netskope UI. You can import or export up to 500 custom rules in one API call.
Request Endpoint
https://
<tenant-URL>
/api/v1/public_cloud/rules?token=
<token>
&
<parameters>
Import Custom Rules
Valid parameters include:
Key
Type
Value
Description
op
string
import
Operation performed.
rules
JSON array of object
{
"rule_name": "
<rule_name>
",
"description": "
<description_optional>
",
"remediation_steps": "
<remediation_optional>
",
"severity": "<Critical|High|Medium|Low>",
"code": "
<code>
",
"cloud_provider": "<aws|googlecloud|azure>"
}
List of rules to import.
cloud_provider
string
azure | aws | googlecloud
The IaaS platform provider.
rule_name
string
Required
Name of the custom rule.
description
string
Optional
Description of the custom rule.
remediation_steps
string
Optional
Remediation text for the rule.
severity
string
Critical | High | Low | Medium
Severity of the custom rule.
code
string
Ex:
RedShiftCluster should have LoggingEnabled eq true
DSL specification code.
modify_by
string
Ex:
admin@netskope.com
Email address
Example Import Request
POST 'https://
<tenant-URL>
/api/v1/public_cloud/rules?token=f39866cb86ab84a0208e9e1ee&op=import' --header 'Content-Type: application/json' --data-raw '{
    "rules": [
        {
            "rule_name": "AWS_C3",
            "description": "",
            "remediation_steps": "",
            "severity": "High",
            "code": "RedShiftCluster should have LoggingEnabled eq true",
            "cloud_provider": "aws"
        },
        {
            "rule_name": "AWS_C4",
            "description": "",
            "remediation_steps": "",
            "severity": "High",
            "code": "RedShiftCluster should have LoggingEnabled eq true",
            "cloud_provider": "aws"
        }
    ],
    "modify_by": "admin@netskope.com"
}'
Export Custom Rules
Valid parameters include:
Key
Type
Value
Description
op
string
export
Operation performed.
cloud_provider
string
azure | aws | googlecloud
The IaaS platform provider.
severity
string
Critical | High | Low | Medium
Severity of the custom rule.
state
string
Ex:
deployed
Filter with deployed rules.
Example Export Request
GET 'https://
<tenant-URL>
/api/v1/public_cloud/rules?token=f39866cb86ab84a0208e9e1ee&op=export&severity=Critical|High&cloud_provider=aws'
In this Topic
Import and Export CSA Custom Rules

---
## Set Log In Attempts
**URL:** https://docs.netskope.com/en/set-log-in-attempts-85093/
**Last Modified:** 2025-08-31T01:38:53+00:00
**Scraped:** 2026-08-10T07:46:57.238977+00:00

Set Log In Attempts - Netskope Technical Documentation
Set Log In Attempts
You can specify the number of log in attempts that can be allowed before the admin user is locked out of the UI. The default setting allows up to 5 failed login attempts.
To set log in attempts:
To change the default go to
Settings > Administration > Admins
.
On the top right-hand side, click the Tools icon to modify the allowed number of log in attempts.
Click
Save
.
In this Topic
Set Log In Attempts

---
## Set Log In Attempts
**URL:** https://docs.netskope.com/en/set-log-in-attempts/
**Last Modified:** 2025-09-01T12:45:32+00:00
**Scraped:** 2026-08-10T07:46:59.585948+00:00

Set Log In Attempts - Netskope Technical Documentation
Set Log In Attempts
You can specify the number of log in attempts that can be allowed before the admin user is locked out of the UI. The default setting allows up to 5 failed login attempts.
To set log in attempts:
To change the default go to
Settings > Administration > Admins
.
On the top right-hand side, click the Tools icon to modify the allowed number of log in attempts.
Click
Save
.
In this Topic
Set Log In Attempts

---
## Using the REST API v2 dataexport  Iterator Endpoints
**URL:** https://docs.netskope.com/en/using-the-rest-api-v2-dataexport-iterator-endpoints/
**Last Modified:** 2026-05-01T16:03:26+00:00
**Scraped:** 2026-08-10T07:47:38.988829+00:00

Using the REST API v2 dataexport Iterator Endpoints - Netskope Technical Documentation
Using the REST API v2 dataexport  Iterator Endpoints
The Netskope
dataexport
endpoints, also called
iterator
endpoints, provide a simplified way of consuming tenant log information. This article describes the best practices for consumption of this data.
Netskope recommends leveraging existing clients for SIEM integration where possible through the use of the following solutions:
Netskope Cloud Exchange: Log Shipper Module:
/en/netskope-cloud-exchange.html
Netskope Splunk Technical Add-on:
https://apps.splunk.com/app/3808/
Sumo Logic Netskope WebTx Source:
https://help.sumologic.com/docs/send-data/hosted-collectors/cloud-to-cloud-integration-framework/netskope-webtx-source/
If the aforementioned clients are insufficient, Netskope also provides a python SDK.
Python SDK for dataexport endpoints
https://pypi.org/project/netskopesdk/
How Do Iterator Endpoints Function
Through the use of an index, the Netskope platform tracks log consumption though a simplified operational workflow that replicates that often seen in web forums. When a consumer requests a page of data from the endpoint, Netskope delivers the requested data by writing an index as to the data provided. When the consumer has completed processing the requested page of data, the consumer simply requests the next page of data.
Each endpoint stores its own index value, which is provided by the consumer on query. This allows for easy parallelization of API calls across multiple endpoints concurrently.
Note
Multiple consumers leveraging the same endpoint and index concurrently is not supported and could result in the appearance of missing data on the consumer.
Iterator Query Structure
The endpoint query structure is very easy to construct.
https://
<tenant-URL>
/api/v2/
<endpoint>
/?operation=
<operation>
&index=
<index>
Supported Iterator Operations
epoch timestamp
: If an epoch timestamp is provided, this informs the Netskope endpoint to begin log consumption in one hour batches from this timestamp. You will need to use the Next operation to fetch more logs.
next
: The next operation value requests the next page of data from the Netskope endpoint.
resend
: If the consumer is unable to process the page of data provided, resend operation will issue a retry of the last page of data requested.
The
epoch timestamp
and
next
operations both update the Netskope stored index, where the
resend
operation asks for the prior page without updating the index.
Iterator Index
The index value for the iterator is a string value supplied by the consumer that is used by Netskope to store the page values. This index should be unique by the consumer to prevent data consumption challenges. The consumer may use the same index value across multiple endpoints without concern.
The index string is used for when more than one system is pulling logs. For example, you are using
​demo​
as the index and pull records 1-1000. The next time
​demo​
​ pulls logs, it will pull logs 1001-2000 (if pulling 1000 at a time).
If you leave it blank and have two systems pulling logs, the first system will pull logs 1-1000, and then when the second system pulled logs, it will get 1001-2000. This is not optimal.
If you have system1 (demo1) and system2 (demo2) pulling logs at the same time, each will get 1-1000 if using unique index strings.
Not using an index has the chance of “being reused”. If you define your own index, you can guarantee that only you have that index value and won’t lose records.
Page Size
Netskope Iterator endpoints deliver 10,000 record pages per API call.
Wait Time
Each iterator query will provide guidance in seconds how long to wait. This value is calculated based on the amount of data returned in your API call.
{
    "ok": 1,
    "result": [
        {
        }
    ],
    "wait_time": 5
Rate Limits
Using the response headers to manage rate limits to avoid 429 error messages is recommended.
RateLimit-Limit: Rate limits are applied by endpoint, and this value provides the number allowed per second
RateLimit-Remaining: The amount of queries supported before the interval resets before generating a 429 error message.
RateLimit-Reset: The time before the rate limits are reset, this value is in seconds.
HTTP/1.1 200 OK
....
RateLimit-Limit: 4
RateLimit-Remaining: 1
RateLimit-Reset: 1
...
If a Rate is exceeded, the headers will be extended, and the data payload will mention why the query returned a 429 error response.
Retry-After: This is the recommended wait time before retrying your query. This value is in seconds.
HTTP/1.1 429 Too Many Requests
...
RateLimit-Remaining: 0
RateLimit-Reset: 1
Retry-After: 1
RateLimit-Limit: 4
...
{
  "message":"API rate limit exceeded"
}
Example
Example of workflow using the iterator endpoint starting with the oldest record Netskope has.
Craft your query using the
operation=next
, and index value.
https://
<tenant-URL>
/api/v2/events/dataexport/events/alert?operation=next&index=demo
Review the
wait_time
attribute in the JSON response.
"wait_time": 5
Request the next page of data from the endpoint.
https://
<tenant-URL>
/api/v2/events/dataexport/events/alert?operation=next&index=demo
Repeat steps 2 and 3.
Error Response Codes
Error Code
User Action Required
Notes
403
Yes
Check the API V2 token is associated to the valid endpoint and its not expired. A Retry will solve the problem only after solving the token issue by following the
guidelines
.
409
No
Concurrency conflict and the request cannot be processed at this point of time. DataExport API V2 endpoints does not support downloading the same event type concurrently with same iterator index and the client is expected to validate the logic to pull the events is single threaded.
429
No
Too many request for the same tenant accessing the same endpoint. The Client is expected to honor the rate limit to avoid a 429 error, and as part of the response header, it carries the reset time in the header ratelimit-reset. The Client is expected to sleep/wait (ratelimit-reset ) to avoid the 429. The current rate limit is 4 req / second / endpoint.
5xx
No
Netskope is having a temporary server issue for one of these reasons:
DataBase Query timeout.
Server overloaded.
Internal DNS issues. Upon receiving 5xx error from Netskope Server, we recommended that you do a backoff of 5 seconds wait time before the next call.
Using the Client Status Iterator API
The Netskope Client periodically reports Client status to the Netskope backend to have visibility in the  tenant UI for different aspects of Clients. For example, status about user-initiated actions (enable/disable), installation/upgrade status, current tunnel status (Up/Down) etc. Users can check the Client status logs on the device page on the tenant UI.
Through the use of a Client status iterator, the Netskope platform tracks log consumption though a simplified operational workflow. When a consumer requests a page of Client status events from the endpoint, Netskope delivers the requested events, and writes an index with the watermark of events provided. When the consumer has completed processing the requested page of events, the consumer simply requests the next page.
The Client status iterator service provides a streaming API and these management APIs:
Create Iterator API: Allows you to create a new iterator. Call this API before sending requests for event logs.
Check Iterator Status API: Allows you to check whether the creation of an iterator is completed.
Delete Iterator API: Allows you to delete an existing iterator. Generally, this is used when you need to rename an iterator of a certain event type.
Event Fetch API: Allows you to request for event logs from an iterator. The response will be returned in CSV format.
Workflow
Here are examples of how to use the new APIs to request the Client status events:
Use Create Iterator API to create an iterator for Client status events.
POST https://my_test_tenant/api/v2/dataexport/iterator/my_test_index?eventtype=clientstatus
Use Check Iterator status API to check the creation status of the iterator until the status of the iterator is ready.
GET https://my_test_tenant/api/v2/dataexport/iterator/my_test_index?
Use Event Fetch API to request events from the iterator.
Get https://my_test_tenant/api/v2/dataexport/iterator/my_test_index/events?operation=next
Review the wait_time attribute in the response header and wait for enough time accordingly, like “wait_time”: 1
Use Iterator Events Request API to request events from the iterator.
Get https://my_test_tenant/api/v2/dataexport/iterator/my_test_index/events?operation=next
Repeat steps 4 and 5.
API Limits
We allow only one Client status iterator per tenant.
Concurrent Create Iterator or Delete Iterator requests are not supported and could result in a request failure.
The iterator service is designed to stream the recent event logs with high speed. You can only request for event logs that are not older than a certain time period; older events are dropped automatically if not requested in time. The supported retention for Client status iterators is 7 days.
Concurrent event fetch requests on the same iterator are not supported and will result in request failure.
Multiple consumers request event logs from the same iterator concurrently is not supported and could result in the appearance of missing data on the consumer.
In this Topic
Using the REST API v2 dataexport  Iterator Endpoints

---
## Advanced Log Upload Commands
**URL:** https://docs.netskope.com/en/advanced-log-upload-commands-144862/
**Last Modified:** 2025-08-31T01:42:51+00:00
**Scraped:** 2026-08-10T07:47:51.002280+00:00

Advanced Log Upload Commands - Netskope Technical Documentation
Advanced Log Upload Commands
Here are some additional log upload commands:
To set the number of bits for the network location IP address:
set log-upload network-bits
<networkbits>
To change the number of days (15 days is the default) the data should be retained for AD connector:
set log-upload adconnector-rentention-days
<days>
To set custom header for parsing received logs:
set log-upload header
<parser:header1,header2..>
To set custom pattern for parsing received logs:
set log-upload pattern
<parser:pattern.>
To set whether the user field in the event should be the AD user setting, email address from AD, or user from the log file:
set log-upload eventuser-source
<value>
Supported values are:
ad
,
email
, and
log
(default).
To disable or enable block events from being uploaded:
set log-upload block-events
<value>
Supported values are:
enable
, and
disable
.
To disable or enable threat detection:
set log-upload threat-detection
<value>
Supported values are:
enable
, and
disable
.
To prevent events that are older than a specified number of days from being reported in the UI:
set log-upload event-filter <days>
The maximum number of days you can specify is 90.
In this Topic
Advanced Log Upload Commands

---
## Advanced Log Upload Commands
**URL:** https://docs.netskope.com/en/advanced-log-upload-commands/
**Last Modified:** 2025-09-01T12:48:56+00:00
**Scraped:** 2026-08-10T07:47:53.549685+00:00

Advanced Log Upload Commands - Netskope Technical Documentation
Advanced Log Upload Commands
Here are some additional log upload commands:
To set the number of bits for the network location IP address:
set log-upload network-bits
<networkbits>
To change the number of days (15 days is the default) the data should be retained for AD connector:
set log-upload adconnector-rentention-days
<days>
To set custom header for parsing received logs:
set log-upload header
<parser:header1,header2..>
To set custom pattern for parsing received logs:
set log-upload pattern
<parser:pattern.>
To set whether the user field in the event should be the AD user setting, email address from AD, or user from the log file:
set log-upload eventuser-source
<value>
Supported values are:
ad
,
email
, and
log
(default).
To disable or enable block events from being uploaded:
set log-upload block-events
<value>
Supported values are:
enable
, and
disable
.
To disable or enable threat detection:
set log-upload threat-detection
<value>
Supported values are:
enable
, and
disable
.
To prevent events that are older than a specified number of days from being reported in the UI:
set log-upload event-filter <days>
The maximum number of days you can specify is 90.
In this Topic
Advanced Log Upload Commands

---
## Configure a Login Banner
**URL:** https://docs.netskope.com/en/configure-a-login-banner/
**Last Modified:** 2025-08-31T01:43:24+00:00
**Scraped:** 2026-08-10T07:48:04.254690+00:00

Configure a Login Banner - Netskope Technical Documentation
Configure a Login Banner
When you log into your virtual appliance, the default login banner for the Netskope Appliance is displayed in the console. You can secure the appliance by customizing the login banner to display custom instructions and warning messages for the user.
To configure a login banner, enter the following command at the configuration prompt:
set system login-banner
Copy and paste the login banner at the prompt.
Press
ctrl+D
to set the new login banner.
To save the login banner configuration, enter
save
at the configuration prompt.
In this Topic
Configure a Login Banner

---
## Configure a Login Banner
**URL:** https://docs.netskope.com/en/configure-a-login-banner-144852/
**Last Modified:** 2025-09-01T12:48:27+00:00
**Scraped:** 2026-08-10T07:48:06.700306+00:00

Configure a Login Banner - Netskope Technical Documentation
Configure a Login Banner
When you log into your virtual appliance, the default login banner for the Netskope Appliance is displayed in the console. You can secure the appliance by customizing the login banner to display custom instructions and warning messages for the user.
To configure a login banner, enter the following command at the configuration prompt:
set system login-banner
Copy and paste the login banner at the prompt.
Press
ctrl+D
to set the new login banner.
To save the login banner configuration, enter
save
at the configuration prompt.
In this Topic
Configure a Login Banner

---
## Configure Log Uploads
**URL:** https://docs.netskope.com/en/configure-log-uploads-355003/
**Last Modified:** 2025-08-31T01:42:48+00:00
**Scraped:** 2026-08-10T07:48:14.129325+00:00

Configure Log Uploads - Netskope Technical Documentation
Configure Log Uploads
The management plane appliance can upload logs directly through the UI, and both the management plane appliance and log parser appliances can also receive them via SFTP, SCP, and FTPS.
Log uploads are disabled by default on new appliances. To process logs, run the command
set log-upload enable true
. If log uploads are already running on an existing appliance, you can disable log processing by running the command
set log-upload enable false
. If an appliance is not being used for log parsing, run the command
set log-upload enable false
.
Configure Syslog on the OPLP
Upload Logs to the Netskope Tenant using HTTPS
Configure SSH Keys for Log Uploads
Upload Logs using SFTP
Upload Logs using SCP
Upload Logs using FTPS
Upload Logs from an Amazon S3 Bucket
Verify the Log Parser Connection
Advanced Log Upload Commands
In this Topic
Configure Log Uploads

---
## Configure Log Uploads
**URL:** https://docs.netskope.com/en/configure-log-uploads/
**Last Modified:** 2025-09-01T12:49:27+00:00
**Scraped:** 2026-08-10T07:48:17.659592+00:00

Configure Log Uploads - Netskope Technical Documentation
Configure Log Uploads
The management plane appliance can upload logs directly through the UI, and both the management plane appliance and log parser appliances can also receive them via SFTP, SCP, and FTPS.
Log uploads are disabled by default on new appliances. To process logs, run the command
set log-upload enable true
. If log uploads are already running on an existing appliance, you can disable log processing by running the command
set log-upload enable false
. If an appliance is not being used for log parsing, run the command
set log-upload enable false
.
Configure Syslog on the Appliance
Upload Logs to the Netskope Tenant using HTTPS
Configure SSH Keys for Log Uploads
In this Topic
Configure Log Uploads

---
## Configure NFS on the Log Parser Appliance
**URL:** https://docs.netskope.com/en/configure-nfs-on-the-log-parser-appliance/
**Last Modified:** 2025-08-31T01:43:27+00:00
**Scraped:** 2026-08-10T07:48:18.935213+00:00

Configure NFS on the Log Parser Appliance - Netskope Technical Documentation
Configure NFS on the Log Parser Appliance
A log parsing appliance can be configured to read logs from an NFS share. NFS configuration on the log parsing appliance must be performed using the CLI. You need to make sure NFS server is up, or otherwise the CLI configuration will not be activated. After you have an NFS node up and running, you can specify its IP address and the absolute path to the NFS share.
The NFS share should allow write access, as the log parsing appliance will need to create directories for specific log types. Logs need to be placed in the directory appropriate for that log type. After a log file has been queued for parsing, the original log file is deleted. Please ensure that you retain backups of the original log files, in case they are needed.
Note the IP address of the interface you configured. In this example the Inbound interface of the log appliance has the IP address of
1.1.1.2
.
Go to your NFS server and use the chmod command to set the permissions on the NFS server.
chmod 777
<nfs-share path>
Add the following entry in
/etc/exports
#format 
#
<nfs-share path>
<inbound interface IP configured on the log appliance>
/home/nsadmin/nfs-share/logs 1.1.1.2(rw,sync,no_root_squash,no_subtree_check)
Activate your new settings by entering this command:
%> sudo exportfs -a
Go back to log appliance CLI and enter these commands to configure NFS:
set log-upload nfs-server enable true
set log-upload nfs-server host
<IP address or name of your NFS server>
set log-upload nfs-server mount-options
<Comma separated list of NFS mount options>
set log-upload nfs-server remote-mountpoint
<Absolute path of the NFS shared directory>
set log-upload nfs-server subdirectory
<Absolute path of the subdirectory within the NFS shared directory>
save
The configuration was successful if you see:
NFS setup complete
Restarting all services
Restarting networking services
Restarting resolvconf
Restarting DNS proxy
Restarting log
Configuration saved
You can always look at the configuration by entering the show command:
show nfs-server
.
Enter the
exit
command to leave the nsshell configure mode.
If more than one log parsing appliance will be used, steps 1-7 need to be repeated on each one. It’s critical that each appliance be assigned its own NFS share because they were not designed to operate on the same NFS directory.
Troubleshooting your NFS CLI Configuration
If the configuration was unsuccessful for any reason, the following message might be displayed on the CLI prompt:
log01(config)# set nfs-server ip-address 1.1.1.1
log01(config)# set nfs-server remote-dir /home/nfs-share/logs
log01(config)# set nfs-server enable true
log01(config)# save
Restarting resolvconf
Restarting lclw
Configuration saved
NFS Server/Mount is not available...Please check NFS server configuration...
If NFS server config looks ok then try saving the config again...
If you see this:
Make sure your NFS server is up and running with correct access permission set for the log box you are using. Here is the sample from /etc/exports on an NFS server that was used for testing. You may choose to use different settings based on your network requirements, as long as the share is writeable (‘rw’). etc/exports from NFS server being used for testing:
#format
#
<nfs-share path><inbound interface IP configured on the log box>
/home/nsadmin/nfs-share/logs 1.1.1.2 (rw,sync,no_root_squash,no_subtree_check)
Make sure you have configured the inbound interface on the log parsing appliance and you have specified the correct IP address for the NFS server, along with the absolute path of NFS share directory as specified in
/etc/exports
on your NFS server.
On the NFS server’s command prompt, run the following command after editing
/etc/exports
:
> sudo exportfs -a
Save the configuration in the nsshell for the log parsing appliance again. If everything is setup correctly, it should be working properly.
In this Topic
Configure NFS on the Log Parser Appliance

---
## Configure SSH Keys for Log Uploads
**URL:** https://docs.netskope.com/en/configure-ssh-keys-for-log-uploads-144858/
**Last Modified:** 2025-08-31T01:42:49+00:00
**Scraped:** 2026-08-10T07:48:25.973638+00:00

Configure SSH Keys for Log Uploads - Netskope Technical Documentation
Configure SSH Keys for Log Uploads
You can configure your SSH key pairs to automatically upload logs to the appliance.
To use your own SSH key pairs:
Access the appliance console using ssh.
Log in using the
nsadmin/nsappliance
credentials. An nsshell opens.
Enter
configure
to enter the nsshell configure mode.
Add an entry to the ssh-public-keys list in the CLI configuration:
add log-upload ssh-public-keys
added index 0
Set the value of the ssh public key at the index returned from the last command. This requires you to paste the SSH public key:
set log-upload ssh-public-keys 0 key
Copy and paste the ssh public key
Enter one or more lines of input. When done, press Ctrl-D
ssh-rsa ABAQCYr/tT64RNidYhuGisLLQLdd2e1jDtxYepCcE0Z98iyzX57985Xi
eVWDn8PJbniexq4PRvMy8RRYZ2ktu7aqacCjIpqlgbG0Xxgk5mXApXCpglqIE/A/
lRtZqfp6+/mbn7RuBbUXFkEbYz3uPwUFgZOUEI2KUx9za8SYnUc64kCujmYZ7UF5
JXmvZg4AhIPVHzvT+XbLDHOsC8mNrgEQeslpB9jGbCYZSLQKHwx3Pknv+rQaJ04G
+WRM/NmokhZXhM7GKXrufQjKRbZeXcHBGksNMSzTL+YihAQDqq4qC0drnGdu3Ezz
SEfwuz+PJ+ugh test@ubuntu-docker==
^D
To see the configuration, enter the following command:
show log-upload ssh-public-keys
[
  {
    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYr/tT64RNidYh
sLLQLdd2e1jDtxYepCcE0Z98iyzX57985XineoeVWDn8PJbniexq4PRvMy8RRYZ2
7aqacCjIpqlgbG0Xxgk5mXApXCpglqIE/A/ZD1lRtZqfp6+/mbn7RuBbUXFkEbYz
wUFgZOUEI2KUx9za8SYnUc64kCujmYZ7UF55a8JXmvZg4AhIPVHzvT+XbLDHOsC8
gEQeslpB9jGbCYZSLQKHwx3Pknv+rQaJ04GqiL+WRM/NmokhZXhM7GKXrufQjKRb
cHBGksNMSzTL+YihAQDqq4qC0drnGdu3EzzVRrSEfw test@ubuntu-docker==
"
  }
]
Enter
save
to activate your changes.
Enter
exit
to leave the configure mode.
Enter
exit
to leave the nsshell and exit the appliance console.
In this Topic
Configure SSH Keys for Log Uploads

---
## Configure Syslog on the Appliance
**URL:** https://docs.netskope.com/en/configure-syslog-on-the-appliance/
**Last Modified:** 2025-08-31T01:43:37+00:00
**Scraped:** 2026-08-10T07:48:27.158952+00:00

Configure Syslog on the Appliance - Netskope Technical Documentation
Configure Syslog on the Appliance
You can configure syslog on the appliance to stream syslog messages directly from the enterprise firewall or proxy servers.
After the logs are streamed via syslog to the appliance, the syslog messages are written to a file in the
/nslogs/user/upload/
<parser-name>
folder. The file is captured at the beginning of every hour with the file name format:
parser name_month_day_hour_host.log
. Due to processing time, the latest completed file is for the previous hour.
After the logs are processed, the extracted cloud app events will get uploaded to your tenant instance in the Netskope cloud. To check the status of the logs in the Netskope tenant UI, go to
Settings > Risk Insights > Log > Upload
. You can also check the status of the logs on the appliance using command line interface (CLI) commands.
Basic Setup
protocol
specifies to use TCP or UDP. The default protocol is UDP and the default syslog port is 514.
Before setting the protocol, you must stop all processes that are running or in-flight.
Run the following command in operation mode.
log-upload stop
Run the following commands in configuration mode to enable syslog on the OPLP.
set log-upload syslogng protocol
<TCP|UDP>
set log-upload syslogng noparse enable true
noparse enable true
ensures the syslog message received from the firewall and/or proxy is written as-is and not truncated by the syslogng. If you are enabling syslog, we recommend that you enable this configuration.
Enable TLS for Log Upload via Syslog
You can configure syslog to upload logs to the OPLP using a TLS connection. TLS can only be enabled if the
protocol
is set to TCP. To enable TLS on syslogng you will require a server certificate and key.
Note
The appliance does not generate the server certificate and key.
Run the following commands in configuration mode to enable TLS for syslog.
set log-upload syslogng tls enable true
set log-upload syslogng tls server-cert
set log-upload syslogng tls server-key
Define the Log Source
Specifies what parser type to use for processing logs. For example, if you are uploading bluecoat proxy logs, choose
logsource proxysg-http-main
. Here are the valid options:
Note
These parser type names are case-sensitive must be entered exactly as they appear in this table.
asa
fortigate
proxysg
squid
asa-syslog
greenplum-bluecoat
proxysg-http-main
symantec-web-security
bro-ids
isa-splunk
proxysg-websense
trustwave
chkp
juniper-srx-structured-syslog
scansafe
websense
cisco-fwsm-syslog
mcafee
sensage
zscaler
cisco-wsa
netscreen-traffic
sfwder
cisco-wsa-syslog
panw
sonicwall-syslog
custom-csv
panw-syslog
sophos
add log-upload syslogng parserconfig
{server response should be} added index 0
set log-upload syslogng parserconfig 0 logsource
<log-source>
Define Filters
Separate logs into different directories based on the data in the logs.
set log-upload syslogng parserconfig 0 filter message
<message>
set log-upload syslogng parserconfig 0 filter name
<filter name>
Define Macros
Defines which macro templates to use.
set log-upload syslogng parserconfig 0 macros
<macros>
Define Parsers
Defines which parsers to use.
set log-upload syslogng parserconfig 0 parser
<parser name>
csv-parser columns (
<comma separated column name>
) delimiters (
<delimiter characters>
)
For example,
set log-upload syslogng parserconfig 0 parser panparser csv-parser columns (rserver, rtime, SNO) delimiters (chars(","))
Define Substitutions
Defines how to reformat the log files retrieved.
add log-upload syslogng parserconfig 0 rewrite substitute
set log-upload syslogng parserconfig 0 rewrite name
<any substition name>
set log-upload syslogng parserconfig 0 rewrite substitute 0 flags
<flag>
Note
This last command is optional. An example of a flag is
global
,
ignore-case
, etc.
set log-upload syslogng parserconfig 0 rewrite substitute 0 fromstring
<fromstring>
set log-upload syslogng parserconfig 0 rewrite substitute 0 tostring
<tostring>
set log-upload syslogng parserconfig 0 rewrite substitute 0 value message
In this Topic
Configure Syslog on the Appliance

---
## Configure SSH Keys for Log Uploads
**URL:** https://docs.netskope.com/en/configure-ssh-keys-for-log-uploads/
**Last Modified:** 2025-09-01T12:49:01+00:00
**Scraped:** 2026-08-10T07:48:28.335684+00:00

Configure SSH Keys for Log Uploads - Netskope Technical Documentation
Configure SSH Keys for Log Uploads
You can configure your SSH key pairs to automatically upload logs to the appliance.
To use your own SSH key pairs:
Access the appliance console using ssh.
Log in using the
nsadmin/nsappliance
credentials. An nsshell opens.
Enter
configure
to enter the nsshell configure mode.
Add an entry to the ssh-public-keys list in the CLI configuration:
add log-upload ssh-public-keys
added index 0
Set the value of the ssh public key at the index returned from the last command. This requires you to paste the SSH public key:
set log-upload ssh-public-keys 0 key
Copy and paste the ssh public key
Enter one or more lines of input. When done, press Ctrl-D
ssh-rsa ABAQCYr/tT64RNidYhuGisLLQLdd2e1jDtxYepCcE0Z98iyzX57985Xi
eVWDn8PJbniexq4PRvMy8RRYZ2ktu7aqacCjIpqlgbG0Xxgk5mXApXCpglqIE/A/
lRtZqfp6+/mbn7RuBbUXFkEbYz3uPwUFgZOUEI2KUx9za8SYnUc64kCujmYZ7UF5
JXmvZg4AhIPVHzvT+XbLDHOsC8mNrgEQeslpB9jGbCYZSLQKHwx3Pknv+rQaJ04G
+WRM/NmokhZXhM7GKXrufQjKRbZeXcHBGksNMSzTL+YihAQDqq4qC0drnGdu3Ezz
SEfwuz+PJ+ugh test@ubuntu-docker==
^D
To see the configuration, enter the following command:
show log-upload ssh-public-keys
[
  {
    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYr/tT64RNidYh
sLLQLdd2e1jDtxYepCcE0Z98iyzX57985XineoeVWDn8PJbniexq4PRvMy8RRYZ2
7aqacCjIpqlgbG0Xxgk5mXApXCpglqIE/A/ZD1lRtZqfp6+/mbn7RuBbUXFkEbYz
wUFgZOUEI2KUx9za8SYnUc64kCujmYZ7UF55a8JXmvZg4AhIPVHzvT+XbLDHOsC8
gEQeslpB9jGbCYZSLQKHwx3Pknv+rQaJ04GqiL+WRM/NmokhZXhM7GKXrufQjKRb
cHBGksNMSzTL+YihAQDqq4qC0drnGdu3EzzVRrSEfw test@ubuntu-docker==
"
  }
]
Enter
save
to activate your changes.
Enter
exit
to leave the configure mode.
Enter
exit
to leave the nsshell and exit the appliance console.
In this Topic
Configure SSH Keys for Log Uploads

---
## Configure Syslog on the OPLP
**URL:** https://docs.netskope.com/en/configure-syslog-on-the-oplp/
**Last Modified:** 2026-06-01T21:55:52+00:00
**Scraped:** 2026-08-10T07:48:30.700496+00:00

Configure Syslog on the OPLP - Netskope Technical Documentation
Configure Syslog on the OPLP
You can configure syslog on the OPLP to stream syslog messages directly from the enterprise firewall or proxy servers.
After the logs are streamed via syslog to the OPLP, the syslog messages are written to a file in the
/nslogs/user/upload/
<parser-name>
folder. The file is captured at the beginning of every hour with the file name format:
parser-name_month_day_hour_host.log
. Due to processing time, the latest completed file is for the previous hour.
After the logs are processed, the extracted cloud app events will get uploaded to your tenant instance in the Netskope cloud. To check the status of the logs in the Netskope tenant UI, go to
Settings > Risk Insights > Log > Upload
page. You can also check the status of the logs on the OPLP using the command line interface (CLI).
Basic Setup
protocol
specifies to use TCP or UDP. The default protocol is UDP and the default syslog port is 514.
Before setting the protocol, you must stop all processes that are running or in-flight.
Run the following command in operation mode.
log-upload stop
Run the following commands in configuration mode to enable syslog on the OPLP.
set log-upload syslogng protocol
<TCP|UDP>
set log-upload syslogng noparse enable true
noparse enable true
ensures the syslog message received from the firewall and/or proxy is written as-is and not truncated by the syslogng. If you are enabling syslog, we recommend that you enable this configuration.
Enable TLS for Log Upload via Syslog
You can configure syslog to upload logs to the OPLP using a TLS connection. TLS can only be enabled if the
protocol
is set to TCP. To enable TLS on syslogng you will require a server certificate and key.
Note
The appliance does not generate the server certificate and key.
Run the following commands in configuration mode to enable TLS for syslog.
set log-upload syslogng tls enable true
set log-upload syslogng tls server-cert
set log-upload syslogng tls server-key
Define the Log Source
Specifies what parser type to use for processing logs. For example, if you are uploading bluecoat proxy logs, choose
logsource proxysg-http-main
. Here are the valid options:
Note
These parser type names are case-sensitive must be entered exactly as they appear in this table.
Parsers
Adlogs
Asa
Asa-Fmt2
Asa-Fmt3
Asa-Fmt4
Asa-Fmt5
Asa-Fmt6
Asa-Syslog
Asa-Unified
Bro-Ids
Chkp
Cisco-Fwsm-Syslog
Cisco-Wsa
Cisco-Wsa-Syslog
Custom-Csv
Fortigate
Greenplum-Bluecoat
Isa-Splunk
Juniper-Srx-Structured-Syslog
Juniper-Srx-Unstructured-Syslog
Mcafee
Netscreen-Traffic
Panw
Panw-Syslog
Proxysg
Proxysg-Http-Main
Proxysg-Websense
Scansafe
Sensage
Sfwder
Sonicwall-Syslog
Sophos
Squid
Symantec-Web-Security
Trustwave
Utils
Websense
Zscaler
add log-upload syslogng parserconfig
{server response should be} added index 0
set log-upload syslogng parserconfig 0 logsource
<log-source>
Define Filters
Separate logs into different directories based on the data in the logs.
set log-upload syslogng parserconfig 0 filter message
<message>
set log-upload syslogng parserconfig 0 filter name
<filter name>
For the
<message>
option, you can enter an arbitrary string or a PCRE-compliant regular expression. The OPLP will filter and put matching messages into the configured log file.
Define Macros
Defines which macro templates to use.
set log-upload syslogng parserconfig 0 macros
<macros>
Define Parsers
Defines which parsers to use.
set log-upload syslogng parserconfig 0 parser
<parser name>
csv-parser columns (
<comma separated column name>
) delimiters (
<delimiter characters>
)
For example,
set log-upload syslogng parserconfig 0 parser panparser csv-parser columns (rserver, rtime, SNO) delimiters (chars(","))
Define Substitutions
Defines how to reformat the log files retrieved.
add log-upload syslogng parserconfig 0 rewrite substitute
set log-upload syslogng parserconfig 0 rewrite name
<any substition name>
set log-upload syslogng parserconfig 0 rewrite substitute 0 flags
<flag>
Note
This last command is optional. An example of a flag is
global
,
ignore-case
, etc.
set log-upload syslogng parserconfig 0 rewrite substitute 0 fromstring
<fromstring>
set log-upload syslogng parserconfig 0 rewrite substitute 0 tostring
<tostring>
set log-upload syslogng parserconfig 0 rewrite substitute 0 value message
In this Topic
Configure Syslog on the OPLP

---
## Configure the Log Parser Appliance on the Management Plane
**URL:** https://docs.netskope.com/en/configure-the-log-parser-appliance-on-the-management-plane/
**Last Modified:** 2025-08-31T01:43:25+00:00
**Scraped:** 2026-08-10T07:48:36.618093+00:00

Configure the Log Parser Appliance on the Management Plane - Netskope Technical Documentation
Configure the Log Parser Appliance on the Management Plane
You can use dedicated log parsing appliances to scale performance.
To configure an appliance for log parsing:
Log in to the log parser appliance using the credentials
nsadmin/nsappliance
. You should see the
nsappliance
prompt.
Your appliance has the factory default settings, so initialize it by issuing the following command:
nsappliance> initialize initializing the box... enter admin email: enter admin password:  password: setting up user... done. setting admin password... done. initialization successful.
You will be prompted for an admin email address and password, just like when a management appliance was being initialized, but this time the credentials are not relevant. They will only be used if this device is ever repurposed as a management appliance.
After initialization completes, enter
configure
to start configuration mode to set the hostname. When finished, enter
save
to activate the configuration:
nsappliance> nsappliance> configure Entering configuration mode nsappliance# set system hostname log01 nsappliance# save Restarting config agent Restarting messenger Restarting ssh tunnel service Configuration saved lp01(config)#
Set the required inbound interface on the appliance by entering these commands:
lp01(config)# set interface inbound ip
<IP address>
lp01(config)# set interface inbound gw
<gateway address>
lp01(config)# set interface inbound netmask
<subnet mask>
Tip
To review your entries, enter
show interface
.
Set the DNS server IP address by entering this command:
lp01(config)# set dns primary
<dns server IP address>
Enter
save
and wait for the prompt to return. This may take as long as 4 or 5 minutes while the appliance fully configures itself for the first time.
lp01(config)# save Restarting all services Restarting networking services Restarting resolvconf Restarting DNS proxy Restarting log Configuration saved lp01(config)#
Now that you have configured the inbound interface’s IP address for the log appliance, try to connect to it using your preferred ssh client. Here is an example using PuTTY running on Windows:
In this example, you logged in using
192.168.64.92
for the IP address specified for the inbound interface. When the connection is open, you can log in using the credentials
nsadmin/nsappliance
.
If the connection is successful, all further configuration changes should be done over ssh. If the connection is not successful, you can adjust the network settings over IPMI as described in step 5 above.
Enter
exit
to leave the config mode.
Enter
exit
to leave the nsshell and exit the log appliance console.
Note
All further configuration changes should be made using this SSH access method.
Access SSH and enter the
configure
command to start configuration mode.
Point this appliance to the local (on-premises) management appliance inbound IP address:
lp01(config)# set management-plane location local
If you’re configuring a combined, all-in-one appliance, enter this command instead:
set management-plane location on-box
Enter the management appliance local inbound IP address by entering this command:
lp01(config)# set management-plane local inbound-ip
<IP address>
Get your license key from your Netskope tenant UI (
Settings > Security Cloud Platform > On-Premises Infrastructure
), and then enter the license key entering this command.
lp01(config)# set system licensekey
<licensekey>
Note
A license key is only required if you will be downloading upgrade packages from the Netskope cloud.
Enter
save
.
In this Topic
Configure the Log Parser Appliance on the Management Plane

---
## Enable Hashing and Redaction of Log Fields
**URL:** https://docs.netskope.com/en/enable-hashing-and-redaction-of-log-fields/
**Last Modified:** 2025-08-31T01:42:58+00:00
**Scraped:** 2026-08-10T07:48:49.609000+00:00

Enable Hashing and Redaction of Log Fields - Netskope Technical Documentation
Enable Hashing and Redaction of Log Fields
The OPLP supports hashing or redaction of certain sensitive fields from the log file to give you enhanced privacy and control over your log data. The parser computes a hash for specified values and inserts that into the JSON object sent to the Netskope cloud.
The hash function is irreversible and the original key value cannot be recovered by anyone with access to the Netskope cloud. However, the hash function is repeatable on the OPLP to match certain key values to the hash, for forensics purposes.
Configure hashing or redaction  with these commands:
set log-upload perfieldaction fields
<field-name>
set log-upload perfieldaction action [remove|hash]
remove: empties the specified fields from extracted events
hash: replaces the field values with SHA256 hash.
To hash the username field, set the following commands:
set log-upload perfieldaction fields user 
set log-upload perfieldaction action hash
To hash both source-ip and user field, you can specify it as comma separated field values:
set log-upload perfieldaction fields user,srcip
set log-upload perfieldaction action hash
Note
We recommended to only hash the user field. Hashing the
srcip
field is supported but causes the source location to not be identified, and the user analytics map will not show the accurate location of the users.
To verify the hash value, enter this command from the Netskope shell:
log-upload gethash key
<value>
This runs the hash function on the key value to obtain the hash value and helps correlate specific key values against the entries in the Netskope cloud.
In this Topic
Enable Hashing and Redaction of Log Fields

---
## Export or Import Configurations
**URL:** https://docs.netskope.com/en/export-or-import-configurations/
**Last Modified:** 2025-08-31T01:43:12+00:00
**Scraped:** 2026-08-10T07:49:00.416026+00:00

Export or Import Configurations - Netskope Technical Documentation
Export or Import Configurations
Exporting or importing configurations enables you to deploy existing configurations to other appliances. Using this feature, you can save configurations outside the appliance for use at a later time, or use the configuration settings from one appliance to quickly setup multiple appliances.
Exporting Configurations
Importing Configurations
In this Topic
Export or Import Configurations

---
## Exporting Configurations
**URL:** https://docs.netskope.com/en/exporting-configurations/
**Last Modified:** 2025-09-01T12:48:34+00:00
**Scraped:** 2026-08-10T07:49:02.772338+00:00

Exporting Configurations - Netskope Technical Documentation
Exporting Configurations
Netskope recommends that you export configurations to an external storage device for use at a later time.
There are two ways to export configurations.
Using config-transporter script: Use this method to export configurations from appliance versions older than 46.
Using CLI: Use this method to export configurations from appliance version 46.
Exporting Configurations using config-transporter Script
Install the config-transporter script and export configurations from appliance versions older than 46.
Run the following command to install the config-transporter script.
sudo dpkg -i config-transporter-
<version>
.deb
The config-transporter package is installed in the /opt/ns/bin directory.
Go to the /opt/ns/bin/config-transporter directory and run the following command.
sudo python config_transporter.py --physical-appliance export --file /tmp/export_configurations.tar
Note
Ensure that you use the correct version of the config-transporter script to export configurations. For example, if you are exporting configurations from version 44.0 to 46.24, then install the config-transporter script from version 46.24. Contact Netskope support to get the correct version of the config-transporter script .
Exporting Configurations using a CLI
Starting from version 46, you can export configurations using the following CLI command.
scp export config to host <host-IP-address> path
<location-to-copy-to>
user
<user-name-on-the-remote-host>
In this Topic
Exporting Configurations

---
## Log in to the Appliance
**URL:** https://docs.netskope.com/en/log-in-to-the-appliance/
**Last Modified:** 2025-08-31T01:42:52+00:00
**Scraped:** 2026-08-10T07:49:20.743327+00:00

Log in to the Appliance - Netskope Technical Documentation
Log in to the Appliance
The appliance has two different command prompts:
<hostname>
: This is the nsshell prompt.
<hostname>
(config)
: This is the configuration prompt (nsshell prompt in configuration mode).
You can login to the appliance using one of the two admin user accounts,
nsadmin
or
nstransfer
. The
nsadmin
user account has the privilege to operate and configure the appliance. Whereas the
nstransfer
user account can be used to upload logs from the appliance using protocols like SFTP, SCP, or FTP.
Note
Netskope recommends that you set a new password for
nsadmin
and
nstransfer
user accounts to secure your appliance. To learn more:
Change the Appliance Password
.
You can also configure SSH keys on the appliance to log in without a password. To learn more:
Configure SSH Keys
.
Change the Appliance Password
Important
It is mandatory to update your password every 90 days (starting from the day of the appliance installation or upgrade).
Passwords must have a minimum length of 14 characters and include at least:
1 number
1 uppercase letter
1 lowercase letter
1 special character or symbol
To change your appliance password:
Connect to the virtual appliance console.
Log into the virtual appliance using the credentials:
nsadmin/nsappliance
.
Change your password by using the following command.
nsappliance> auth change-password nsadmin
New password:
<newpassword>
Retype new password:
<newpassword>
passwd: password updated successfully
nsappliance> auth change-password nstransfer
New password:
<newpassword>
Retype new password:
<newpassword>
passwd: password updated successfully
At the nsshell prompt, enter
configure
to go into configuration mode. The command prompt changes to the nsshell configuration prompt (
<hostname>
(config)
).
Configure SSH Keys
Note
The following steps illustrate how to add an SSH key for
nsadmin
and other user accounts except
nstransfer
. For instructions on adding an SSH key for the
nstransfer
user account, see
Configure SSH Keys for Log Uploads
.
To configure the SSH key on the appliance:
Connect to the virtual appliance console.
Create the SSH key by using the following command:
nsappliance(config)# add system ssh-public-keys
added index 0
nsappliance(config)# set system ssh-public-keys 0 user nsadmin
nsappliance(config)# set system ssh-public-keys 0 key
Enter one or more lines of input. When done, press Ctrl-D
ssh-ed25519 {SSH key content}
nsappliance(config)# save
You can now login to the appliance with the SSH key.
To create a user that uses the SSH key on the appliance:
Connect to the virtual appliance console.
Create the new user by using the following command:
nsshell> auth nsshell-user add username newuser
nsappliance(config)# add system ssh-public-keys
added index 2
nsappliance(config)# set system ssh-public-keys 2 user newuser
nsappliance(config)# set system ssh-public-keys 2 key
Enter one or more lines of input. When done, press Ctrl-D
ssh-ed25519 {SSH key content}
nsappliance(config)# save
You can now log in to the appliance as this user with the SSH key.
In this Topic
Log in to the Appliance

---
## Monitor Log Processing Status using a Command Line Interface
**URL:** https://docs.netskope.com/en/monitor-log-processing-status-using-a-command-line-interface/
**Last Modified:** 2025-08-31T01:43:02+00:00
**Scraped:** 2026-08-10T07:49:30.179726+00:00

Monitor Log Processing Status using a Command Line Interface - Netskope Technical Documentation
Monitor Log Processing Status using a Command Line Interface
Monitor the status of a single log file by using the following commands:
status log-file-history
: Provides details about when the log file was queued for processing, when the log completed processing, how many cloud events are extracted from the log, when the log was uploaded to the cloud, and how long processing took. It also shows any exceptions thrown during processing.
"support_tenant_sshkey.key": [
    "queued at 2016-09-28 07:00:47.197000", 
    "moved for processing at 2016-09-28 07:00:47.724000", 
    "splitting started at 2016-09-28 07:00:49.062000", 
    "splitting finished at 2016-09-28 07:00:49.303000", 
    "completed parsing at 2016-09-28 07:00:59.622000", 
    "completed uploading to cloud at 2016-09-28 07:01:06.831000", 
    "extracted 0 events from 27 lines", 
    "no of sessions is 0", 
    "time taken = 0:00:19.634000"
  ],
status log-file-history summary
<no of days>
: Provides a one-line summary of all the log files processed on the OPLP. You can specify the number of days as an input. For example, if you want to see the status of logs processed in the last 3 days, use the command:
status log-file-history summary 3
which returns the log file name, when it was found, and its status:
status log-file-history summary 1 
{
"ip2user_mapping.csv found at 2015­03­30 22:06:12.415000 and its moved for processing",
"user2canonical_mapping.csv found at 2015­03­30 22:06:12.457000 and its moved for processing",
"asa_Mon_14.log found at 2015­03­30 21:40:18.976000 and and its parsing is complete",
"asa_Mon_15.log found at 2015­03­24 23:00:25.628000 and and its parsing is complete",
}
status log-file-history filename
<name of the log file>
: Provides details about when the log file was queued for processing, when the log completed processing, how many cloud events are extracted from the log, when the log was uploaded to the cloud, and how long processing took. It also shows any exceptions thrown during processing.
status log-file-history filename asa_Tue_14.log
{
"asa_Tue_14.log": 
"queued at 2015­03­24 21:40:18.977000",
"moved for processing at 2015­03­24 21:40:19.032000",
"completed parsing at 2015­03­24 21:40:58.683000",
"extracted 1 events from 1 lines", "time taken = 0:00:39.706000",
}
To clear specific alerts, use the following command:
troubleshooting monitoring clear-unfinished-files
This command removes the following alerts:
Log_Process-5a
Log_Process-5b
Log_Process-5c
Files_not_picked_up_24_hrs
Files_not_picked_up_48_hrs
Files_not_uploaded_24_hrs
Files_not_uploaded_48_hrs.
The appliance and the Netskope tenant UI generate metrics alerts with the various system metrics. If you do not want to view metrics alerts, you can disable them. Use the following command in configuration mode:
appliance> configure
Entering configuration mode
appliance(config)# set metrics enable false
In this Topic
Monitor Log Processing Status using a Command Line Interface

---
## Upload Logs from an Amazon S3 Bucket
**URL:** https://docs.netskope.com/en/upload-logs-from-an-amazon-s3-bucket/
**Last Modified:** 2025-08-31T01:42:51+00:00
**Scraped:** 2026-08-10T07:49:56.681948+00:00

Upload Logs from an Amazon S3 Bucket - Netskope Technical Documentation
Upload Logs from an Amazon S3 Bucket
This section explains how to get unprocessed log files stored in Amazon S3 buckets into the parser directories for log processing. For example, you can retrieve Scansafe logs, but any S3 protocol compatible store, including native AWS S3, can be processed.
In order to configure log uploads from an S3 bucket, first get these values from your AWS account:
access key
secret access key
hostname
host-bucket
To upload log files from an Amazon S3 Bucket repository to the OPLP, enter these commands at the configuration prompt:
set log-upload aws-s3 access-key
<access-key>
set log-upload aws-s3 secret-key
<secret-key>
set log-upload aws-s3 hostname
<hostname>
set log-upload aws-s3 host-bucket
<host-bucket>
set log-upload aws-s3 use-https true
set log-upload aws-s3 enable true
set log-upload aws-s3 log-source
<log-source>
To set the start time, enter
log-upload aws-s3 start date-time
using the date-time format
date[-time] <MM-DD-YYYY> [HH:MM:SS]
with time in UTC/GMT. This is an operational command and should be entered in the nsshell.
Note
Ensure that the appliance and the Amazon S3 Bucket are both set to the same time zone in UTC/GMT.
In this Topic
Upload Logs from an Amazon S3 Bucket

---
## Upload Logs using FTPS
**URL:** https://docs.netskope.com/en/upload-logs-using-ftps/
**Last Modified:** 2025-08-31T01:43:26+00:00
**Scraped:** 2026-08-10T07:49:57.859099+00:00

Upload Logs using FTPS - Netskope Technical Documentation
Upload Logs using FTPS
If your network allows file transfers using FTPS instead of SFTP or SCP, you can upload log files by enabling FTPS on the appliance.  To do this, you must first generate and install an SSL certificate. Server side certificates are required to enable SSL inspection. You can use either a self-signed certificate or a CA certificate preferably signed by the enterprise’s Root or intermediate CA.
Make sure that the server certificate of the appliance uses a fully-qualified domain name as the common name.
Enter the command:
set log-upload ftps server-cert
Copy and paste your CA certificate into the buffer, press
Enter
, then type
Ctrl-D
to exit.
Enter the command:
set log-upload ftps server-key
Copy and paste your private key into the buffer, press the
Enter
key, and then enter
Ctrl-D
to exit.
If you are not using a CA and want the appliance to generate a self-signed certificate, use the following command:
run request certificate generate ftps self-signed city
<city>
common-name
<common-name>
country
<country>
days
<days>
email-address
<email-address>
organization
<organization>
organization-unit
<organization-unit>
state
<state>
Here’s an example command to generate self-signed certificate:
run request certificate generate ftps self-signed city "Los Altos" common-name "sforwarder.netskope.com"
organization "netskope" organization-unit "netskope cert authority"
state "CA" country "US" email-address "admin@netskope.com"
Enable log upload for FTPS:
set log-upload ftps enable true
Enter
save
and press
Enter
to save the configuration.
In this Topic
Upload Logs using FTPS

---
## Upload Logs using FTPS
**URL:** https://docs.netskope.com/en/upload-logs-using-ftps-158321/
**Last Modified:** 2025-09-01T12:49:00+00:00
**Scraped:** 2026-08-10T07:50:00.228532+00:00

Upload Logs using FTPS - Netskope Technical Documentation
Upload Logs using FTPS
If your network allows file transfers using FTPS instead of SFTP or SCP, you can upload log files by enabling FTPS on the appliance.  To do this, you must first generate and install an SSL certificate. Server side certificates are required to enable SSL inspection. You can use either a self-signed certificate or a CA certificate preferably signed by the enterprise’s Root or intermediate CA.
Make sure that the server certificate uses a fully-qualified domain name as the common name.
Enter the command:
set log-upload ftps server-cert
Copy and paste your CA certificate into the buffer, press
Enter
, then type
Ctrl-D
to exit.
Enter the command:
set log-upload ftps server-key
Copy and paste your private key into the buffer, press the
Enter
key, and then enter
Ctrl-D
to exit.
If you are not using a CA and want  to generate a self-signed certificate, use the following command:
run request certificate generate ftps self-signed city
<city>
common-name
<common-name>
country
<country>
days
<days>
email-address
<email-address>
organization
<organization>
organization-unit
<organization-unit>
state
<state>
Here’s an example command to generate self-signed certificate:
run request certificate generate ftps self-signed city "Los Altos" common-name "sforwarder.netskope.com"
organization "netskope" organization-unit "netskope cert authority"
state "CA" country "US" email-address "admin@netskope.com"
Enable log upload for FTPS:
set log-upload ftps enable true
Enter
save
and press
Enter
to save the configuration.
In this Topic
Upload Logs using FTPS

---
## Upload Logs using SCP
**URL:** https://docs.netskope.com/en/upload-logs-using-scp-158320/
**Last Modified:** 2025-08-31T01:42:50+00:00
**Scraped:** 2026-08-10T07:50:01.407663+00:00

Upload Logs using SCP - Netskope Technical Documentation
Upload Logs using SCP
Setting up non-interactive file transfers using SCP instead of SFTP is very useful for continuous log uploads.
Use Password-based Authentication
In order to use password-based authentication for SCP, set the password with the following nsshell command:
#nsshell> auth change-password nstransfer
This configures the password for the
nstransfer
admin used for uploading log files. Now you can SCP the logs by entering this command:
#scp
<filename>
nstransfer@
<system_IP>
:upload/
<parser-name>
Use Public Key Authentication
If desired, the private key used for SFTP access described in the previous section can be used instead of a password by entering this command:
#scp -i
<key_file>
<filename>
nstransfer@
<system_IP>
:upload/
<parser-name>
In this Topic
Upload Logs using SCP

---
## Upload Logs using SCP
**URL:** https://docs.netskope.com/en/upload-logs-using-scp/
**Last Modified:** 2025-09-01T12:48:55+00:00
**Scraped:** 2026-08-10T07:50:02.597698+00:00

Upload Logs using SCP - Netskope Technical Documentation
Upload Logs using SCP
Setting up non-interactive file transfers using SCP instead of SFTP is very useful for continuous log uploads.
Use Password-based Authentication
In order to use password-based authentication for SCP, set the password with the following nsshell command:
#nsshell> auth change-password nstransfer
This configures the password for the
nstransfer
admin used for uploading log files. Now you can SCP the logs by entering this command:
#scp
<filename>
nstransfer@
<system_IP>
:upload/
<parser-name>
Use Public Key Authentication
If desired, the private key used for SFTP access described in the previous section can be used instead of a password by entering this command:
#scp -i
<key_file>
<filename>
nstransfer@
<system_IP>
:upload/
<parser-name>
In this Topic
Upload Logs using SCP

---
## Upload Logs using SFTP
**URL:** https://docs.netskope.com/en/upload-logs-using-sftp-144860/
**Last Modified:** 2025-08-31T01:42:49+00:00
**Scraped:** 2026-08-10T07:50:03.878195+00:00

Upload Logs using SFTP - Netskope Technical Documentation
Upload Logs using SFTP
SFTP is an interactive way to upload log files, which helps you get familiarized with the overall process before automating it using SCP.
Upload Logs with Windows using SFTP
Make sure your log files have the
.log
extension. If using an archive (zip), you can only have one log file per archive.
You will need an SFTP client. If you are familiar with using private key files and/or have another PSFTP client, you can skip to step 5 below. To download a SFTP client, go to
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
and download the following files:
PSFTP: PuTTY SFTP client
PuTTY gen: PuTTY key generator
Download the private key from the Netskope tenant UI under
Settings > Risk Insights > Log > Upload
.
After you have the private key, you need to convert it to a format that PuTTy understands. To do this, launch the file
puttygen.exe
and click the Load button to select the private key file downloaded from the Netskope Administrator UI in step 3 above. Next click the Save Private Key button to convert the key file to a
.ppk
file that can be used for the PuTTY SFTP client. Remember the location for this key since we will need it in the next step.
From a command prompt, change to the directory where the converted
.ppk
key file resides, and then enter this command using the username provided in the Admin UI on the
Log > Upload
page:
psftp -i customerprivatekey.ppk nstransfer@
<appliance IP address>
When connected, go to the
upload
directory (
cd upload
). Next, go to the directory for the device used for generating the log file in the first step.
For example, if using Cisco IronPort, you would need to use the
cisco-wsa
directory (
cd cisco-wsa
).
If using Blue Coat logs, you would need to use the
proxysg-http-main
directory (
cd proxysg-http-main
).
If using a custom parser, use the directory named
custom-
<custom parser name>
, where
<custom parser name>
is the name on the Custom Tab in the Upload Log File dialog box in the Netskope UI (
Settings > Risk Insights > Log > Upload > Upload Logs
). In this case, the directory name would be
custom-test_1_parser
.
Upload the log file(s) using the
mput
command (
mput /logs/cisco-ironport.log
)
After the logs are uploaded, it will take some time for the system to parse the logs and show events in Skope IT. The larger the log files, the more time it will take.
Upload Logs with Mac or Linux using SFTP
Make sure your log files have the
.log
extension. If using an archive (zip), you can only have one log file per archive.
Download the private key from the Netskope Administrator interface.
You may need to change permissions of the private key file to restrict access. Enter this command to change permissions of the downloaded private key file:
chmod 600 customer_sshkey.key
Launch a terminal window and establish an SFTP connection to the Appliance IP
cd upload
Address, specifying the directory where the downloaded private key resides. Next enter this command using the username provided in the Admin UI on the
Log > Upload
page:
sftp -i /privatekey/customer_sshkey.key nstransfer@
<appliance IP address>
When connected, go to the
upload
directory (). Next, go to the directory for the device used for generating the log file in the first step. For example, if using Cisco IronPort, you would need to use the
cisco-wsa
directory (
cd cisco-wsa
). If using Blue Coat logs, go to ‘
proxysg-http-main
‘ (
cd proxysg-http-main
).
Upload the log file(s) using the
mput
command (
mput /logs/cisco-ironport.log
)
After the logs are uploaded, it will take some time for the system to parse the logs and show events in Skope IT. The larger the log files, the more time it will take.
In this Topic
Upload Logs using SFTP

---
## Upload Logs using SFTP
**URL:** https://docs.netskope.com/en/upload-logs-using-sftp/
**Last Modified:** 2025-09-01T12:48:55+00:00
**Scraped:** 2026-08-10T07:50:06.235332+00:00

Upload Logs using SFTP - Netskope Technical Documentation
Upload Logs using SFTP
SFTP is an interactive way to upload log files, which helps you get familiarized with the overall process before automating it using SCP.
Upload Logs with Windows using SFTP
Make sure your log files have the
.log
extension. If using an archive (zip), you can only have one log file per archive.
You will need an SFTP client. If you are familiar with using private key files and/or have another PSFTP client, you can skip to step 5 below. To download a SFTP client, go to
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
and download the following files:
PSFTP: PuTTY SFTP client
PuTTY gen: PuTTY key generator
Download the private key from the Netskope tenant UI under
Settings > Risk Insights > Log > Upload
.
After you have the private key, you need to convert it to a format that PuTTy understands. To do this, launch the file
puttygen.exe
and click the Load button to select the private key file downloaded from the Netskope Administrator UI in step 3 above. Next click the Save Private Key button to convert the key file to a
.ppk
file that can be used for the PuTTY SFTP client. Remember the location for this key since we will need it in the next step.
From a command prompt, change to the directory where the converted
.ppk
key file resides, and then enter this command using the username provided in the Admin UI on the
Log > Upload
page:
psftp -i customerprivatekey.ppk nstransfer@
<appliance IP address>
When connected, go to the
upload
directory (
cd upload
). Next, go to the directory for the device used for generating the log file in the first step.
For example, if using Cisco IronPort, you would need to use the
cisco-wsa
directory (
cd cisco-wsa
).
If using Blue Coat logs, you would need to use the
proxysg-http-main
directory (
cd proxysg-http-main
).
If using a custom parser, use the directory named
custom-
<custom parser name>
, where
<custom parser name>
is the name on the Custom Tab in the Upload Log File dialog box in the Netskope UI (
Settings > Risk Insights > Log > Upload > Upload Logs
). In this case, the directory name would be
custom-test_1_parser
.
Upload the log file(s) using the
mput
command (
mput /logs/cisco-ironport.log
)
After the logs are uploaded, it will take some time for the system to parse the logs and show events in Skope IT. The larger the log files, the more time it will take.
Upload Logs with Mac or Linux using SFTP
Make sure your log files have the
.log
extension. If using an archive (zip), you can only have one log file per archive.
Download the private key from the Netskope Administrator interface.
You may need to change permissions of the private key file to restrict access. Enter this command to change permissions of the downloaded private key file:
chmod 600 customer_sshkey.key
Launch a terminal window and establish an SFTP connection to the Appliance IP
cd upload
Address, specifying the directory where the downloaded private key resides. Next enter this command using the username provided in the Admin UI on the
Log > Upload
page:
sftp -i /privatekey/customer_sshkey.key nstransfer@
<appliance IP address>
When connected, go to the
upload
directory (). Next, go to the directory for the device used for generating the log file in the first step. For example, if using Cisco IronPort, you would need to use the
cisco-wsa
directory (
cd cisco-wsa
). If using Blue Coat logs, go to ‘
proxysg-http-main
‘ (
cd proxysg-http-main
).
Upload the log file(s) using the
mput
command (
mput /logs/cisco-ironport.log
)
After the logs are uploaded, it will take some time for the system to parse the logs and show events in Skope IT. The larger the log files, the more time it will take.
In this Topic
Upload Logs using SFTP

---
## Verify the Log Parser Connection
**URL:** https://docs.netskope.com/en/verify-the-log-parser-connection/
**Last Modified:** 2025-08-31T01:42:51+00:00
**Scraped:** 2026-08-10T07:50:08.596026+00:00

Verify the Log Parser Connection - Netskope Technical Documentation
Verify the Log Parser Connection
To verify the OPLP successfully connected to the Netskope cloud, go to
Settings > Security Cloud Platform > On-Premises Infrastructure
. Scroll down the page until you see your OPLP host name and Log Parser displayed beside your Serial Number. Last Seen shows the last time your OPLP connected to the Netskope cloud.
Note
It takes few minutes to refresh the status in the UI.
In this Topic
Verify the Log Parser Connection

---
## AWS Security Lake Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/amazon-security-lake-plugin-for-log-shipper/
**Last Modified:** 2026-06-23T14:27:22+00:00
**Scraped:** 2026-08-10T07:50:22.200457+00:00

AWS Security Lake Plugin for Log Shipper - Netskope Technical Documentation
AWS Security Lake Plugin for Log Shipper
This document explains how to configure the Amazon Security Lake v2.0.0 plugin in the Cloud Exchange platform. This plugin fetches Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status) and WebTx [via Netskope LogStreaming] logs. The data will be ingested in the Amazon Security Lake Custom Source bucket. This plugin does not support ingestion of data in raw JSON format.
Note
For IAM Roles Anywhere Authentication, we have validated this plugin with a single AWS Account.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope LogStreaming
or
Azure Netskope LogStreaming
plugin already configured.
An Amazon Security Lake enabled AWS account.
Auto generated S3 bucket for Amazon Security Lake
References:
https://docs.aws.amazon.com/security-lake/latest/userguide/
https://aws.amazon.com/security-lake
Access for AWS Athena, AWS Glue, AWS Lake formation, Creating Policy and Role on AWS.
Amazon Security Lake Plugin Support
This plugin supports ingestion of Alerts, Events and WebTx logs. The data will be ingested in the Amazon Security Lake Custom Source bucket. This plugin does not support ingestion of data in raw JSON format.
Data Type
Support
Events
Yes (Page, Application, Audit, Infrastructure, Network, Endpoint, Incident and Client Status)
Alerts
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content)
WebTx
Yes (via Netskope LogStreaming)
Note:
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope LogStreaming
or
Azure Netskope LogStreaming
plugin.
Performance Matrix
This performance reading is for a Large Cloud Exchange Stack with these VM specifications.
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Alerts/Events
~ 50k EPM
Note:
Each raw data has an average size of 2 KB.
Mappings
OCSF Class Mappings for Default Mapping file
The following table describes the OCSF class mappings for Default Mapping file applied to Netskope Alert, Event, and WebTx types when data is ingested from a Netskope tenant.
Note:
Default Mapping file will be using OCSF v1.3.0
Type
Netskope Alert/Event/Webtx Name
OCSF Class
Alert
Compromised Credential
Data Security Finding [2006]
Content
Data Security Finding [2006]
CTEP
Detection Finding [2004]
Device
Detection Finding [2004]
DLP
Data Security Finding [2006]
Malsite
Detection Finding [2004]
Malware
Detection Finding [2004]
Policy
Detection Finding [2004]
Quarantine
Detection Finding [2004]
Remediation
Detection Finding [2004]
Security Assessment
Data Security Finding [2006]
UBA
Detection Finding [2004]
Watchlist
Detection Finding [2004]
Event
Application
Application Lifecycle [6002]
Audit
Event Log Activity [1008]
Client Status
Detection Finding [2004]
with host profile
Endpoint
Detection Finding [2004]
Incident
Detection Finding [2004]
Infrastructure
Application Lifecycle [6002]
Network
Network Activity [4001]
Page
Detection Finding [2004]
Webtx
Transaction
Network Activity [4001]
with Network Proxy profile
Note
In the default mapping file, raw_data is not mapped for all alerts, events and webtx. If a user wants to send raw alert/event/webtx then they need to create a custom mapping with raw_data field mapped to default value as ‘raw_data’ for each alert/event/webtx type. 
Below is the example where Compromised Credential has raw_data field mapped with ‘raw_data’ default value:
Data Type Mappings
Here is the methodology followed for mapping Netskope fields to OCSF fields, and the corresponding transformations used. If new fields need to be added, the same can be used for consistency.
Example Netskope Fields
Transformation
Expected OCSF Field Type
Example Values
Values with Strings, For e.g. file paths, domain names, UUIDs,descriptions, comments and complex nested Objects
String
string_t
“\\printserver\\printer”,5182808a2a99fc688d4a8057,”{\”access_method\”: \”API Connector\”, \”AccountType\”: \”SAML\”}”
Values with Datetime, For e.g. src_time, last_event_timestamp, last_update_timestamp
Time Stamp
timestamp_t (Integer)
1768804071000
Values with Integers. For e.g. port, threshold, event counts or transaction ids
Integer
integer_t
404, 27017
Values requiring precision, For e.g. src_latitude, src_longitude
Floating Point
float_t
-3.6029212e+24,2.77645e+23
Configuration on AWS while using Custom Mappings
Security Lake expects a consistent parquet schema for all the files uploaded to S3. This ensures that the Glue Crawlers are able to infer the table schemas from the parquet files without errors.
If using a custom mapping or updating the provided mapping schema while parquets have already been uploaded, there are chances that the schema of the files no longer stays consistent. Meaning, columns existing in some files do not exist in others, or some files contain extra columns. When querying such partitions in Athena there are chances of running into the HIVE_PARTITION_SCHEMA_MISMATCH errors. Please make sure to edit the Glue Crawlers before moving to a custom mapping so that these errors can be avoided. This update needs to be done for Crawlers of every event/alert/webtx type that has different schemas between parquet files:
To edit the Crawler, go to
Set Output and Scheduling > Advanced Options
.
For
When the crawler detects schema changes in the data store, how should AWS Glue handle table updates in the data catalog?
, select
Add new columns only
.
Enable the toggle for
Update all new and existing partitions with metadata from the table
.
Click
Next > Update
.
API Details
Library
: The AWS SDK for Python (Boto3)
Usage: The AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Security Lake, Amazon Simple Storage Service (Amazon S3) and Amazon Amazon Security Token Service (STS). The SDK provides an object-oriented API as well as low-level access to AWS services.
The plugin uses the SDK to perform actions such as Listing Custom Log Sources, Creating Custom Log Sources in Security Lake, Assuming Provider Role which enables uploading to S3, and then uploading parquet files to S3.
Creating a Security Lake Client
securitylake_client = boto3.client(
         "securitylake",
         aws_access_key_id=self.aws_public_key,
         aws_secret_access_key=self.aws_private_key,
         aws_session_token=self.aws_session_token,
         region_name=self.configuration.get("region_name").strip(),
         config=Config(
             proxies=self.proxy,
             user_agent=USER_AGENT,
             read_timeout=READ_TIMEOUT,
             retries={"max_attempts": MAX_RETRIES, "mode": "standard"},
         ),
    )
Using the Security Lake Client to list/create Custom Log Sources
securitylake_client.list_log_sources()
securitylake_client.create_custom_log_source(**request_params)
Creating an STS Client
sts_client = boto3.client(
         "sts",
         aws_access_key_id=self.aws_public_key,
         aws_secret_access_key=self.aws_private_key,
         aws_session_token=self.aws_session_token,
         region_name=self.configuration.get("region_name").strip(),
         config=Config(
             proxies=self.proxy,
             user_agent=USER_AGENT,
             read_timeout=READ_TIMEOUT,
             retries={"max_attempts": MAX_RETRIES, "mode": "standard"},
         ),
    )
Using the STS Client to Assume a Provider Role
response = sts_client.assume_role(
         RoleArn=role_arn,
         RoleSessionName=role_session_name,
         ExternalId=external_id,
         DurationSeconds=ASSUMED_ROLE_DURATION_SECONDS,
)
Creating an S3 Client
s3_client = boto3.client(
         "s3",
         aws_access_key_id=self.aws_public_key,
         aws_secret_access_key=self.aws_private_key,
         aws_session_token=self.aws_session_token,
         region_name=self.configuration.get("region_name").strip(),
         config=Config(
             proxies=self.proxy,
             user_agent=USER_AGENT,
             read_timeout=READ_TIMEOUT,
             retries={"max_attempts": MAX_RETRIES, "mode": "standard"},
         ),
    )
Using an S3 Client to Upload Files
s3_client.upload_file(file_path, bucket_name, s3_key)
Applicable only for IAM Roles Anywhere
Creating IAM Client
iam_client = boto3.client(
         "iam",
         aws_access_key_id=self.aws_public_key,
         aws_secret_access_key=self.aws_private_key,
         aws_session_token=self.aws_session_token,
         region_name=self.configuration.get("region_name").strip(),
         config=Config(
             proxies=self.proxy,
             user_agent=USER_AGENT,
             read_timeout=READ_TIMEOUT,
             retries={"max_attempts": MAX_RETRIES, "mode": "standard"},
         ),
    )
Updating the Provider Role’s trust policy
role = iam_client.get_role(RoleName=role_name)
iam_client.update_assume_role_policy(RoleName=role_name, PolicyDocument=json.dumps(trust_policy))
User Agent
APN/1.1 (ahq9d89xj9gspapczzdb59goq)
Workflow
Configuration on AWS.
Configure the CLS Amazon Security Lake Plugin.
Configure a Business Rule for AWS Security Lake.
Add a Log Delivery configuration for AWS Security Lake.
Validate the AWS Security Lake plugin.
Watch a Video
Click play to watch a video.
Configure AWS
Using the AWS Plugin Authentication Method
Create a Policy
Go to
IAM > Policies
and click
Create policy
.
Add these permissions as JSON.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SecurityLakePerms",
            "Effect": "Allow",
            "Action": [
                "securitylake:CreateCustomLogSource",
                "securitylake:ListLogSources",
                "securitylake:GetDataLakeSources",
                "securitylake:ListDataLakes"
            ],
            "Resource": "*"
        },
        {
            "Sid": "LakeFormationPerms",
            "Effect": "Allow",
            "Action": [
                "lakeformation:RegisterResource",
                "lakeformation:GrantPermissions",
                "lakeformation:GetDataLakeSettings"
            ],
            "Resource": "*"
        },
        {
            "Sid": "GluePerms",
            "Effect": "Allow",
            "Action": [
                "glue:CreateTable",
                "glue:CreateDatabase",
                "glue:CreateCrawler",
                "glue:UpdateCrawler",
                "glue:UpdateDatabase",
                "glue:UpdateTable",
                "glue:StartCrawlerSchedule",
                "glue:GetDatabase",
                "glue:GetDatabases",
                "glue:GetTable",
                "glue:GetTables",
                "glue:GetTableVersion",
                "glue:GetTableVersions",
                "glue:GetPartition",
                "glue:GetPartitions"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowAssumeSecurityLakeProviderRole",
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole",
                "sts:SetSourceIdentity",
                "sts:TagSession"
            ],
            "Resource": [
                "arn:aws:iam::[aws-account-id]:role/AmazonSecurityLake-Provider-*"
            ]
        },
        {
            "Sid": "AllowPassAndReadRoleForCrawler",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole",
                "iam:GetRole",
                "iam:CreateRole",
                "iam:PutRolePolicy",
                "iam:ListRolePolicies",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3Perms",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:PutObject",
                "s3:CreateBucket",
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy"
            ],
            "Resource": "*"
        }
    ]
}
Note
Make sure you replace the AWS Account Id in the above policy before using it.
Enter a policy name.
Click
Create Policy
.
Create a Role
Go to
IAM > Roles
and click
Create role
.
Select the
AWS Service
.
Under Use Case, select
EC2
.
Click
Next
.
Select the permission policy created in
Create Policy
.
Click
Next
.
Enter a Role Name and Description, like
netskope-ce-instance-role
.
Click
Create Role
.
Assign a Role to the EC2 Instance
Open your EC2 instance console.
Click on
Instances
under
Instances
.
For your EC2 instance (where Cloud Exchange is Deployed), Go to
Action > Security > Modify IAM Role
.
Select the Role that you created above in
Create a role
(netskope-ce-instance-role).
Click
Add IAM role > Modify IAM Role
and click
Update IAM Role
.
Create Crawler Role ARN
Go to
IAM > Policies
and create a policy using these permissions:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueCrawlerListBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::aws-security-data-lake-us-east-1-*"
        },
        {
            "Sid": "GlueCrawlerReadObjects",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetObjectTagging",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "arn:aws:s3:::aws-security-data-lake-us-east-1-*/*"
        }
    ]
}
Enter a policy name and click
Create
.
Go to
Role
and click
Create a Role
. Go to
Trusted Entity Type > Select AWS Service
Service > Select Glue
.
Attach
AWSGlueServiceRole
and create the policy for this role.
Enter a Role Name and click
Create role
.
Copy the Role ARN; it will be used as the Crawler Role ARN.
Provide Permissions in Lake Formation
Go to
AWS Lake formation> Administration > Administrative roles and tasks
.
Set the
Access type
as
Data lake administrator
, select the created roles, and click
Confirm
. Make sure it includes the Crawler role as well as the instance role.
Go to the
Permissions > Data permissions
and click
Grant
.
Set the
Principle
type as
Principals
, and then select the roles. Make sure they include the Crawler role as well as the Instance role.
Note
If you want to query data on Athena then also add the user’s role under IAM users and roles along with the Crawler Role and Instance role.
Select the Named Data Catalog resources and enter the Catalogs and Databases where the data will be stored.
Provide all the database permissions and click
Grant
.
Using the AWS IAM Roles Anywhere Authentication Method
Prerequisites
The AWS Certificate Manager service is required to be enabled to authenticate the plugin using the AWS IAM Roles Anywhere Authentication Method.
Note: Make sure you create the Private Certificate Authority, Trust Anchor and Profile in the same region in which your AWS S3 Source Bucket resides.
Create a Policy for a Private Certificate
This Policy contains the required permissions for creating Private CA Certificate (including Permissions for creating Trust Anchor and Profile) and using the IAM Roles Anywhere.
Go to
Policy Generator
and Select IAM Policy as policy type and generate policy.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Private Certificate Authority
Actions:
CreateCertificateAuthority
DescribeCertificateAuthority
GetCertificate
GetCertificateAuthorityCertificate
GetCertificateAuthorityCsr
ImportCertificateAuthorityCertificate
IssueCertificate
ListCertificateAuthorities
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management (IAM)
Actions:
AttachRolePolicy
CreateAccessKey
CreateRole
DeleteRole
PassRole
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Certificate Manager
Actions:
DescribeCertificate
ExportCertificate
GetCertificate
ListCertificates
ListTagsForCertificate
RequestCertificate
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management Roles Anywhere
Actions:
CreateProfile
CreateTrustAnchor
GetProfile
GetTrustAnchor
ListProfiles
ListTrustAnchors
ARN: *
Click
Add Statement
.
Click
Generate Policy
.
Copy the Policy as it will be used in the next step for creating the policy required for creating the Private CA certificates.
Go to AWS Console and select
IAM
from
All Services
. Click
Policies
in the left panel and then click
Create Policy
.
Copy the policy to the JSON tab. and Click on
Next:Tags
, Click on
Next:Review.
.
Enter Name and Click on
Save Changes
, like
netskope-ce-rolesAnywhere-policy
.
Create Private Certificate Authority
Log in to the AWS Console
Search for
Certificate Manager
.
Click
AWS Private CA
.
Click
Create a private CA
.
Select
General-purpose
for
Mode options
.
Select
Root
for
CA type options
.
Enter an Organization (O).
Select
RSA 2048
for
Key algorithm options
.
Add tags
if any (optional).
Click the checkbox in the
CA permissions options
section.
Click the checkbox in the
Pricing
section
Click
Create
to create the CA certificate.
From
Actions
select
Install CA Certificate
.
Click
Confirm and Install
.
Create Trust Anchor for Private Certificate
Search for the IAM service and go to
Roles
under
Access management
. Scroll down to
Roles Anywhere
and select
Manage
.
Click
Create a Trust anchor
.
Enter a Trust anchor name, like
netskope-ce-trust-anchor
.
Select your
AWS Certificate Manager Private CA
(created in the previous steps) as the
Certificate authority (CA)
source.
Add tags if required.
Click
Create a trust anchor
.
Click the created Trust Anchor and copy the Trust Anchor ARN.
Create a Policy for Plugin Configuration
Go to
IAM > Policies
and click
Create Policy
.
Select
Json
, paste this policy, and then scroll down and click
Next
.
Policy:
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "SecurityLakePerms",
			"Effect": "Allow",
			"Action": [
				"securitylake:CreateCustomLogSource",
				"securitylake:ListLogSources",
				"securitylake:GetDataLakeSources",
				"securitylake:ListDataLakes"
			],
			"Resource": "*"
		},
		{
			"Sid": "LakeFormationPerms",
			"Effect": "Allow",
			"Action": [
				"lakeformation:RegisterResource",
				"lakeformation:GrantPermissions",
				"lakeformation:GetDataLakeSettings"
			],
			"Resource": "*"
		},
		{
			"Sid": "GluePerms",
			"Effect": "Allow",
			"Action": [
				"glue:CreateTable",
				"glue:CreateDatabase",
				"glue:CreateCrawler",
				"glue:UpdateCrawler",
				"glue:UpdateDatabase",
				"glue:UpdateTable",
				"glue:StartCrawlerSchedule",
				"glue:GetDatabase",
				"glue:GetDatabases",
				"glue:GetTable",
				"glue:GetTables",
				"glue:GetTableVersion",
				"glue:GetTableVersions",
				"glue:GetPartition",
				"glue:GetPartitions"
			],
			"Resource": "*"
		},
		{
			"Sid": "AllowAssumeSecurityLakeProviderRole",
			"Effect": "Allow",
			"Action": [
				"sts:AssumeRole",
				"sts:SetSourceIdentity",
				"sts:TagSession"
			],
			"Resource": [
				"arn:aws:iam::[aws-account-id]:role/AmazonSecurityLake-Provider-*"
			]
		},
		{
			"Sid": "AllowPassAndReadRoleForCrawler",
			"Effect": "Allow",
			"Action": [
				"iam:PassRole",
				"iam:GetRole",
				"iam:CreateRole",
				"iam:PutRolePolicy",
				"iam:ListRolePolicies",
				"iam:DeleteRole",
				"iam:DeleteRolePolicy"
			],
			"Resource": "*"
		},
		{
			"Sid": "AllowUpdateProviderRoleTrustPolicy",
			"Effect": "Allow",
			"Action": [
				"iam:UpdateAssumeRolePolicy",
				"iam:GetRole"
			],
			"Resource": "arn:aws:iam::
:role/AmazonSecurityLake-Provider-*"
		},
		{
			"Sid": "S3Perms",
			"Effect": "Allow",
			"Action": [
				"s3:ListBucket",
				"s3:PutObject",
				"s3:CreateBucket",
				"s3:ListAllMyBuckets",
				"s3:GetBucketLocation",
				"s3:GetBucketPolicy"
			],
			"Resource": "*"
		}
	]
}
Note
Make sure to replace AWS Account ID in the policy.
Enter a Policy Name and Description, like
IAM-policy-security-lake
.
Click
Create Policy
.
Create Role for Plugin Configuration
Go to
IAM > Roles
and click
Create Role
.
Select
Custom trust policy
as
Trusted entity
type, paste the Custom Trust policy shown below, and then click
Next
.
Custom Trust Policy:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "rolesanywhere.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetSourceIdentity"
            ]
        }
    ]
}
Attach the policy previously created to this role and click
Next
.
Enter a Role Name, scroll down, and click
Create role
.
After the role is created, open that role and copy its ARN, as it will be used as the Role ARN while configuring the Amazon Security Lake plugin.
Create a Profile
Go to
Roles Anywhere > Create a Profile
.
Enter a profile name and add the role that you just created in the
Create Role
section.
Scroll Down, click the check box in the
Custom role session name
section, and then click
Create a Profile
.
Open the created profile and copy the Profile ARN. This will be used while configuring the Amazon Security Lake plugin.
Request a Private Certificate
Go to
AWS Certificate Manager > Request certificate
.
Select
Request a private certificate
.
Click
Next
.
Select the Certificate authority created in the previous steps.
Provide a domain name in the
Fully qualified domain name
field (like
netskope-ce.com
).
Select
RSA 2048
as the
Key algorithm
.
Add tags if required.
Acknowledge the Certificate renewal permissions.
Click
Request
.
Go to
List certificates
on the navigation panel of AWS Certificate Manager.
Select the certificate created previously.
Click
Export
.
Enter the passphrase. Make a note of the passphrase as it will be required to configure the AWS Security Lake plugin using the
AWS IAM Roles Anywhere
Authentication method.
Click
Generate PEM Encoding
.
Download all the
Certificates
because they won’t be visible again. For new certificates, you will need to Export it again.
For More Info visit
AWS IAM Role Anywhere
Create a Crawler Role ARN
Create policy at
IAM > Policies
using the below permissions.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueCrawlerListBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::aws-security-data-lake-us-east-1-*"
        },
        {
            "Sid": "GlueCrawlerReadObjects",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetObjectTagging",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "arn:aws:s3:::aws-security-data-lake-us-east-1-*/*"
        }
    ]
}
Enter a policy name and click
Create
.
Go to
Roles
and click
Create a Role
. Click
Trusted Entity Type > Select AWS Service
Service > Select Glue
.
Attach
AWSGlueServiceRole
to the policy created previously for this role.
Enter a Role Name and click
Create role
.
Copy the Role ARN; it will be used as the Crawler Role ARN.
Provide Permissions in Lake Formation
Set
Access type
as
Data lake administrator
, select the created roles, and click
Confirm
. Make sure it includes the Crawler role as well as the Instance role.
Go to the
Permissions > Data permissions
and click
Grant
.
Select
Principals
as the
Principle type
,and select the roles. Make sure to include the Crawler role as well as the Instance role.
Note
If you want to query data on Athena, then also add the user’s role under IAM users and roles along with the Crawler Role and Instance role.
Select the
Named Data Catalog
resources and enter the Catalogs and Databases where the data will be stored.
Provide all the database permissions required and click
Grant
.
Steps after the plugin is configured with Auto-update Provider Role Trust Policy as
No
Manually create the Custom Data Source for each type of alerts, events, and WebTx on your AWS instance. Use the
OCSF Class Mappings for Default Mapping file
to map the alerts/events with the OCSF Class.
After custom data sources are created, you’ll need to manually update the Trust Policy for each provider role. Here is the example for the
clientstatus
event type.
Trust Policy:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::[aws-account-id]:root"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:SetSourceIdentity",
                "sts:TagSession"
            ]
        }
    ]
}
Configure the plugin using the manually created data sources.
Configure the Amazon Security Lake Plugin
1. In Cloud Exchange, go to
Settings > Plugin Store
.
2. Search for and select the
Amazon Security Lake v2.0.0 (CLS)
plugin.
3. Enter the Configuration Name (like
Amazon Security Lake
), select the mapping file per your requirements.
Note
With the default mappings, raw_data field will be reflected as null on AWS (Athena). To send raw_data users need to update the mapping and set the default value of raw_data field as raw_data for each alert/event/webtx. For example:
This plugin only supports OCSF format.
4. Click
Next
and enter the Configuration Parameters accordingly:
Authentication Method
Deploy with AWS
Enter these parameters:
AWS S3 Bucket Region Name:
AWS S3 Bucket Region Name from where to get the AWS S3 Bucket. Make sure that the region name matches the region in the Profile ARN and Trust Anchor ARN.
AWS Account ID:
AWS Account ID in which the AWS Security Lake Custom Source Bucket is created.
Parquet File Name Prefix:
Parquet File Name Prefix for the AWS Security Lake Custom Source Bucket. This is an optional field.
AWS Crawler Role ARN:
The Amazon Resource Name (ARN) of the IAM role that the AWS Glue crawler will use to access your data. This role must have permissions for accessing Security Lake, S3 buckets, Glue Data Catalog and Lake Formation. Please refer to the guide for detailed steps on configuring the Glue Crawler role.
Provider External ID:
An external ID used to establish a trust relationship with the log provider (for security best practices against ‘confused deputy’ attacks).
Provider Principal:
The AWS principal (usually an IAM Role ARN or Account ID) of the entity that will be writing logs to the S3 bucket.
Name of Custom Data Source for alert/event/webtx:
Custom Source Bucket of this name will be created in AWS Security Lake for the particular Alert/Event type or Webtx. Also, the folder name in the S3 bucket will be based on these values.
Deploy with AWS IAM Roles Anywhere
Scroll up and click
Save
.
Configure a Log Shipper Business Rule for Amazon Security Lake
In
Log Shipper
, click
Business Rules
.
Click
Create New Rule
.
Enter a Rule Name and configure the Filter per your requirements. Enter a Folder Name, if any.
Click
Save
.
Configure Log Shipper Log Delivery for Amazon Security Lake
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
Select a Source Configuration, Destination Configuration, and Business Rule.
Click
Save
.
Note/p>
For Amazon Security Lake, the total Logs/Webtx Sent to External Receiver count will not represent the count of ingested data. This count represents the number of Logs/Alerts/Events/Webtx pulled and stored in the file on Cloud Exchange and later on it will be uploaded to the Security Lake S3 bucket on AWS. Data will not be ingested to the destination if the pulled alert/event/webtx is less than 265 MB size, and then no same type of alert/event is pulled again after 5 minutes.
Validate the Amazon Security Lake Plugin
In order to validate the plugin workflow, you can check from Netskope Cloud Exchange and from AWS.
Validate the Pull
Go to
Settings > Logging
. Apply the filter as per your requirement. Here are some samples of pulling logs for events, alerts and Webtx log.
To Validate the ingestion from Cloud Exchange
Go to
Settings > Logging
. Apply the filter per your requirements. Example: message
Like “[CLS Amazon Security Lake]”
to check the logs related to the plugin.
You can search the logs for verifying the successful ingestion:
CLS Amazon Security Lake [CLS Amazon Security Lake]: [<alert/event name>] Successfully uploaded to S3
. Note that for WebTx use
<alert/event name>
as v2.
Note
Data will not be ingested to the destination if the pulled alert/event/webtx is less than 265 MB size and then no same type of alert/event is pulled again after 5 minutes.
Logs similar to below examples does not mean that the data is ingested to Security Lake S3 bucket:
CLS Amazon Security Lake [CLS ASL] [alerts] [ctep]: Successfully added 1 log(s) to the AWS Security Lake upload file. The file will be uploaded to the AWS Security Lake bucket once either 256 MB file size or 5 minutes upload condition is met.
Ingested 1 [alerts][ctep] log(s) into configuration CLS ASL successfully. Time taken: 2 seconds.
To Validate in AWS
Go to
S3 Bucket
➔
<
security lake bucket name
>
➔ ext ➔ Custom Data Source for alert/event/webtx.
This is example destination location for ‘ns_incident’ custom data source:
Note
It will have different folders according to dates(i.e. eventDay) under each alert/event/webtx type folder.
If you have configured the plugin with “Parquet File Name Prefix” then each file will have that prefix added to it.
Data will not be ingested to the destination if the pulled alert/event/webtx is less than 265 MB size and then no same type of alert/event is pulled again after 5 minutes.
To Validate Data on Athena
Note
Make sure the user has required permissions to query the data on Athena. Permissions can be provided to the user’s role from AWS Lake Formation > Data Permissions > Grant. For more information related to the permissions for querying data on Athena, you can contact the AWS Support team.
Before searching the data on Athena, make sure all the crawlers are executed successfully. Users can execute any crawler from the
AWS Glue > Crawlers
page on AWS. Select the needed crawlers and click on Run button to execute. Once it is executed properly then the user can search the ingested data on Athena. Users can also set an automatic schedule to execute these Crawlers by manually editing Crawler for each alert/event/webtx.
To search the ingested data, go to the
Amazon Athena > Query editor
.
Click on 3 dots > Preview Table for the table specific to the alert, event, or webtx. Here you can set the query as per your requirements.
This is sample ingest application event:
Scroll to view all the supported fields.
Here are some samples of ingested data:
For Events
For Alerts
Note
The table of CTEP alerts will store CTEP, C2, and IPS alerts.
For WebTx
Troubleshooting the AWS Security Lake Plugin
If you see any error while configuring the Plugin. It may be because of following reasons:
Invalid credentials
Security Lake is not enabled on the provided AWS account.
What to do:
Verify if the provided credentials are valid or not. Refer the steps mentioned in
Configuration on AWS
section.
Make sure Security Lake is enabled on the provided AWS account.
If you don’t see any Parquet files in the destination bucket in 10-15 mins after configuring. It may be due to following reasons:
Data is not getting pulled from the source plugin.
Data pulled is less than 256 MB and no new same type of data is pulled again.
What to do:
Verify if the logs are pulled or not, check logs from the Logging page for the Source Plugin.
Note that data will not be ingested to the destination if the pulled alert/event/webtx is less than 265 MB size and then no same type of alert/event is pulled again after 5 minutes.
Unable to ingest data on AWS (Security Lake S3 bucket). It may be due to one of the below mentioned reasons:
Insufficient permissions
For AWS IAM Roles Anywhere authentication, Auto-update Provider Role Trust Policy is set to No and the user has not updated the Trust Policies of the Provider role.
What to do:
Make sure you have followed the appropriate steps mentioned under
Configuration on AWS section
.
Use ‘
Steps after the plugin is configured with Auto-update Provider Role Trust Policy as No
’ section to update the required roles.
Unable to validated ingested files in S3 bucket for given bucket name
This problem may occur because older versions of the plugin used to have S3 bucket name as the plugin configuration name and all types of data was ingested in a single location.
What to do:
Configure a fresh CLS Amazon Security Lake v2.0.0 instead of upgrading the plugin from older plugin. version
Unable to query data on Athena, it may be due to following reasons:
No data is ingested on Security Lake S3 bucket.
User does not have permission to query data on Security Lake Database.
What to do:
Make sure data is ingested on the Security Lake S3 bucket. Refer to the
Validate from the AWS
section.
Make sure the user has the necessary permissions to access the Security Lake Database. Permissions can be provided to the user’s role from
AWS Lake Formation > Data Permissions
page. For more information related to the permissions for querying data on Athena, you can connect to the AWS Support team.
Parquet file is uploaded in the S3 bucket but Data is not visible on Athena or only some of the columns are visible. It can be because of the following reasons:
Crawler for that particular alert/event/webtx is not executed.
Insufficient permissions
What to do:
Either user needs to manually run the Crawler from AWS Glue > Crawlers page or user needs to Set output and scheduling for the Crawler as per their need.
Note
Each alert/event type and Webtx will have a separate Crawler.
Check the CloudTrail logs for particular crawler execution and verify if there are any errors in it similar to below image.Verify the permissions for the generated credentials for configuring the plugin or contact AWS support team.
Known Behaviors
Data will not be ingested to the destination if the pulled alert/event/webtx is less than 265 MB size and then no same type of alert/event is pulled again after 5 minutes.
Files for the pulled data will not be deleted if it is not ingested to the destination. Example: If user configured a the CLS Amazon Security Lake v2.0.0 plugin and pulled 1 mb of each type of alerts/events and Webtx during the initial pull and then either no new data is pulled or the plugin configuration is deleted then the files created during the initial pull will never get deleted.
Folders for any alert/event/webtx type will be created while uploading the first file of that type of alert/event/webtx on the Security Lake S3 bucket.
All the resources created by the plugin (i.e. Custom Data Sources, Crawlers, Tables under Data Lake formation) on AWS will not be deleted by deleting the plugin configuration.
Even if the Custom Data source for particular alert/event/webtx is deleted still the plugin will keep uploading the data to the destination folder until the folder is present under the Security Lake S3 bucket and if the destination folder is also deleted then the user will encounter an error. Example error log:
CLS Amazon Security Lake [CLS ASL19thJana] [Malware]: S3 upload failed with unexpected error: Failed to upload /opt/netskope/plugins/security_lake_staging/temp_15497_1768910939013.parquet to aws-security-data-lake-us-east-1-drr9keiinq7es73ywbjszqfsmbchwc/ext/a_delete/region=us-east-1/accountId=472514710809/eventDay=20260120/cd51579e-f5f8-11f0-ad9f-de8f29b50429--20260120120859.parquet: An error occurred (InvalidAccessKeyId) when calling the PutObject operation: The AWS Access Key Id you provided does not exist in our records.. Not retrying.
In the Default Mappings, there will be some fields that are mapped to some default values.
The total Logs/Webtx Sent to External Receiver count on the Log Delivery page will not represent the count of ingested data. This count represents the number of Logs/Alerts/Events/Webtx pulled and stored in the file on Cloud Exchange and later on it will be uploaded to the Security Lake S3 bucket on AWS.
Skipped count for pulled alerts/events/webtx can be verified from the logs. Example log:
CLS Amazon Security Lake [CLS ASL]: [alerts][Compromised Credential] Processed 2 records: 1 succeeded, 0 failed, 1 empty records skipped.
OCSF schema defines some fields in sibling pairs, for example activity_name (String) and activity_id (Integer from a predefined enum), status and status_id etc. In the Default Mappings, for all such fields the Integer enum values is mapped to 99 . This allows the String half of the pair to contain any field received from Netskope.
For example: In Compromised Credential Alert, severity_id is mapped to default value 99. It is recommended to refer to its String sibling severity and not severity_id to get the actual value received from Netskope.
Logs similar to below examples does not mean that the data is ingested to Security Lake S3 bucket:
CLS Amazon Security Lake [CLS ASL] [alerts] [ctep]: Successfully added 1 log(s) to the AWS Security Lake upload file. The file will be uploaded to the AWS Security Lake bucket once either 256 MB file size or 5 minutes upload condition is met.
Ingested 1 [alerts][ctep] log(s) into configuration CLS ASL successfully. Time taken: 2 seconds.
To verify the ingestion of data to the Security Lake S3 bucket, refer to the ‘
To validate the ingestion from Netskope Cloud Exchange
’ and ‘
To validate from the AWS
’ sections.
Users might observe some errors or warnings while validating the uploaded parquet files using the official OCSF
validator endpoint
, but they should not affect querying data on Athena. Below are some examples:
{
  "error": "attribute_enum_value_unknown",
  "message": "Unknown enum value at \"proxy_http_request.http_method\"; value \"\" is not defined for enum \"http_method\".",
  "value": "",
  "attribute": "http_method",
  "attribute_path": "proxy_http_request.http_method"
}
{
    "message": "Attribute \"evidences[0].device.os_machine_uuid\" value does not match regex of type \"uuid_t\".",
    "type": "uuid_t",
    "value": "f5d060933f64c16cc6661ad5",
    "warning": "attribute_value_regex_not_matched",
    "attribute": "os_machine_uuid",
    "regex": "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    "attribute_path": "evidences[0].device.os_machine_uuid"
},
{
    "message": "Attribute \"device.mac\" value does not match regex of type \"mac_t\".",
    "type": "mac_t",
    "value": "",
    "warning": "attribute_value_regex_not_matched",
    "attribute": "mac",
    "regex": "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$",
    "attribute_path": "device.mac"
}
{
    "message": "Attribute \"evidences[2].email.to[0]\" value does not match regex of type \"email_t\".",
    "type": "email_t",
    "value": "[\"amark@default.com\", \"johnak@default.com\", \"test_user@netstate.com\"]",
    "warning": "attribute_value_regex_not_matched",
    "attribute": "to",
    "regex": "^[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    "attribute_path": "evidences[2].email.to[0]"
}
Alerts of types C2 and IPS will be ingested under the table of CTEP alerts on AWS platform.
Only some of the columns will be visible in the Athena table if the crawler for a particular table is not executed. Either manually run the crawler for a particular table or set a schedule for particular crawler to execute automatically at a specific time.
In this Topic
AWS Security Lake Plugin for Log Shipper

---
## App Catalog
**URL:** https://docs.netskope.com/en/app-catalog/
**Last Modified:** 2026-06-19T16:08:28+00:00
**Scraped:** 2026-08-10T07:50:23.360434+00:00

App Catalog - Netskope Technical Documentation
App Catalog
After you click Search the results display in the App Catalog page. This lists all the apps that meet your search criteria. You can change your search criteria from this page to further refine your search or click Clear to start over.
Click any application to view
app specific details
. Optionally, click the ellipses at the end of the app on the main page and click
Edit Tags
to view app specific details.
Risk Weight Settings
Tip
This feature requires additional licensing. Contact Netskope Support to enable this feature in your account.
Admins can bulk customize CCI attribute weights across all categories. Click the ellipses at the end of the app on the main page and click
Edit Risk Weight.
The Risk Weight Settings page displays for the selected application. Click
Expand All
to see all the sub categories for the following:
Certifications and Standards
Data Protection
Access Control
Auditability
Disaster Recovery and Business Continuity
Legal and Privacy
Attack Surface Management
Sub categories are specific to the app so you may not see the same sub categories for all apps.
Click and drag the sliders to adjust the weight setting for the applicable categories and click
Save
.
In this Topic
App Catalog

---
## 3rd Party App Risk Assessment Catalog
**URL:** https://docs.netskope.com/en/3rd-party-app-risk-assessment-catalog/
**Last Modified:** 2026-06-19T16:10:45+00:00
**Scraped:** 2026-08-10T07:50:43.891278+00:00

3rd Party App Risk Assessment Catalog - Netskope Technical Documentation
3rd Party App Risk Assessment Catalog
Click
CCI
>
3rd Party Apps
to view the Marketplace App Catalog. This page provides filters for:
Marketplace: Google or Microsoft
Category: connected app category
Permission Level: Permission level is calculated as an aggregate max of the individual OAuth scopes/permissions required by the app. The higher permission level leads to more exposure and higher risk.
Vendor Confidence Level: Vendor confidence is derived from the CCL of the SaaS app from the same vendor. A higher vendor confidence level indicates a lesser risk with usage of the connected app.
Click a specific app name to view the details page.
In this Topic
3rd Party App Risk Assessment Catalog

---
## Kafka Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/kafka-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:35:22+00:00
**Scraped:** 2026-08-10T07:50:57.338130+00:00

Kafka Plugin for Log Shipper - Netskope Technical Documentation
Kafka Plugin for Log Shipper
This document explains how to configure the Kafka v1.0.1 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin ingests Netskope Alerts, Events, and WebTX[via Netskope LogStreaming] logs in CEF and JSON format from the Netskope Tenant into the Kafka topic on the Kafka server/cluster. The plugin will act as a producer to publish the message to the Kafka topic.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
Your Kafka server configuration parameters.
Connectivity to the Kafka server.
Kafka Plugin Support
This plugin is used to transform and ingest the alerts, events, and WebTX (via Netskope LogStreaming) logs to the Kafka topic on the Kafka server/cluster. The plugin will act as a producer to publish the message to the Kafka topic.
Data Type
Support
Alerts
Yes (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Watchlist, Quarantine, Remediation, UBA, CTEP)
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident)
WebTx Logs
Yes (via Netskope LogStreaming)
Syslog CE Logs
Not Supported
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
API Details
List of APIs Used
This plugin uses kafka-python libraries to create kafka producer and consumer.
The kafka-python library is a pure Python client for Apache Kafka that enables developers to interact with Kafka clusters directly from Python applications. It supports essential Kafka operations such as producing messages to topics, consuming messages from topics, and performing administrative tasks like creating or deleting topics. The library is easy to use and integrates well with Python-based systems, making it ideal for building real-time data pipelines or event-driven applications. With kafka-python, you can customize consumer group settings, manage offset commits, and configure producers with delivery guarantees, all using familiar Python code.
Creating the Consumer
KafkaProducer(
     bootstrap_servers=kafka_broker_address,
     value_serializer=lambda x: x.encode("utf-8"),
     acks=ACKS,
     partitioner=DefaultPartitioner(),
     retries=RETRIES,
     linger_ms=LINGER_MS,
     client_id=self._get_user_agent(),
     batch_size=BATCH_SIZE,
     compression_type=COMPRESSION_TYPE,
     request_timeout_ms=TIMEOUT_MS,
)
Creating the Producer
consumer = KafkaConsumer(
    bootstrap_servers=kafka_broker_address,
    security_protocol=kafka_security_protocol,
    ssl_cafile=tmp_ca_file,
    ssl_certfile=tmp_cert_file,
    ssl_keyfile=tmp_private_key_file,
    ssl_password=kafka_ssl_password,
    request_timeout_ms=TIMEOUT_MS,
)
To List the Topics Present on the Kafka cluster
consumer.topics()
To Send Data
producer.send(
    topic=kafka_topic_name,
    value=data
    if not isinstance(data, dict)
    else json.dumps(data),
)
Performance Matrix
This performance reading is conducted on a Large Stack CE with the below-mentioned VM specifications. The below readings are added with the consideration that it will pull around 10K alerts/events in ~8 seconds in CE.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to SIEM
~200K EPM
User Agent
netskope-ce-5.1.1-cls-kafka-v1.0.1
Workflow
Get your Kafka configuration parameters.
Configure the Kafka plugin.
Configure Log Shipper Business Rules for Kafka.
Configure Log Shipper Log Delivery for Kafka.
Validate the Kafka plugin.
Click play to watch a video.
Get your Kafka Configuration Parameters
The following configuration parameters are needed to configure the Kafka plugin for Log Shipper. Reach out to the Kafka server configuration team in order to get all the configuration parameters.
The ingestion of all the Events/Alerts and WebTx is done on the Offset Explorer (v3.0.2); here are the steps to configure the Kafka cluster on Offset Explorer.
Add a new Connection on Offset Explorer, and provide all the information for the cluster.
After a successful connection, go to the
Topics
folder under the connected cluster.
Click the
+
icon to add a new Topic in your cluster, and provide the Name of the Topic, Partition Count, and Replica Count. When finished, click
Add
.
After successful ingestion from Cloud Exchange, you can find the ingested data at
Clusters > {cluster_name} > Topics > {topic_name} > Data
.
Configure the Kafka Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Kafka v1.0.1 (CLS)
plugin.
Enter a plugin configuration name and select a Mapping. Disable the
Transform the raw logs
toggle if you want to ingest your alerts and events in raw JSON format.
Click
Next
and enter the configuration parameters:
Kafka Broker Address
: DNS/IP Address/FQDN of Kafka broker to which data will be sent. Note that the plugin just needs one broker that will respond to Metadata API requests.
Kafka Port
: Kafka Port address to which broker is configured.
Kafka Security Protocol
: Select the security protocol using which authentication will be performed and data will be sent to the Kafka cluster.
Kafka CA Certificate
: Kafka CA Certificate in PEM format. This configuration parameter is only applicable when SSL is selected as Kafka Security Protocol.
Kafka Client Certificate
: Kafka Client Certificate in PEM format. Note: This configuration parameter is only applicable when SSL is selected as Kafka Security Protocol.
Kafka Client Private Key
: Kafka Client Private Key in PEM format. This configuration parameter is only applicable when SSL is selected as Kafka Security Protocol.
Kafka SSL Private Key Password
: The password that is used while loading the certificate. This configuration parameter only applies when SSL is selected as Kafka Security Protocol. It is only needed when the PEM file is generated without a passphrase.
Kafka Topic Name
: Kafka Topic Name to which the logs should be sent. The Kafka Topic Name should not have any spaces in it.
Log Source Identifier
: This will be added as prefix to all the logs. (The log source identifier should not contain the whitespace).
All above mentioned parameters are needed when Security Protocol is SSL. If the security Protocol is Plaintext, add
Kafka Broker Address, Kafka Port
and
Topic Name.
Click
Save
. The plugin configuration will be available on the
Cloud Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for Kafka
Go to
Business Rules
. By default, there is a business rule that filters all alerts and events. If you need to filter out any specific type of alert or event, click
Create New Rule
to configure a new business rule by adding the rule name and filter.
Click
Save
.
Configure Log Shipper Log Delivery for Kafka
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (Netskope CLS plugin), the Destination plugin (Kafka plugin), and a business rule, and then click
Save
.
For ingestion of WebTx, select the Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming plugin), the Destination plugin (Kafka plugin), and then click
Save
.
Validate the Kafka Plugin
Validate in Cloud Exchange
In order to validate the plugin workflow:
Click
Logging
.
Search for ingested alerts with the filter
message contains ingested
.
The ingested logs will be filtered.
Validate in Kafka
The Kafka plugin was designed to send the CEF formatted data by encoding it to UTF-8, and JSON events by performing JSON serialization using json.dumps(), and then encoding it to UTF-8.
There are many ways to validate that the data is sent to the Kafka server, but here the Offset Explorer is used to validate it.
Troubleshooting the Kafka Plugin
Topic is created automatically in Kafka while ingesting data, even when it was deleted
What to do:
Add a new topic in Kafka.
Update the Kafka plugin with a new topic name and save it.
Delete the old topic on Kafka.
Following these steps will not create the deleted topic again on Kafka, and data will be ingested to the newly added topic.
Receiving “Kafka Broker is unreachable or Kafka cluster might be down
Verify Kafka Broker Address and Kafka Port provided in configuration parameters.
This issue might be due to one of these reasons:
The Kafka server is actually down.
The disk space for the server is full.
What to do:
Reach out to your IT and confirm which of the above reasons causes the error.
If Kafka is down, restarting it will work.
If disk space is full, either clear the unwanted files and empty the space, or get more disk space and restart the server.
In this Topic
Kafka Plugin for Log Shipper

---
## CrowdStrike LogScale Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/crowdstrike-logscale-plugin-for-log-shipper/
**Last Modified:** 2026-05-28T03:46:17+00:00
**Scraped:** 2026-08-10T07:50:59.731311+00:00

CrowdStrike LogScale Plugin for Log Shipper - Netskope Technical Documentation
CrowdStrike LogScale Plugin for Log Shipper
This document explains how to ingest Netskope Alerts, Events, and Web transaction logs in JSON format from your Netskope tenant to the CrowdStrike LogScale  using Cloud Exchange with the CLS CrowdStrike LogScale plugin. The plugin transforms and ingests the alerts, events, and WebTX logs into the CrowdStrike LogScale HTTP Event Collector.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured.
Your LogScale configuration parameters.
Connectivity to the CrowdStrike LogScale Platform. Example:
https://cloud.community.humio.com
.
LogScale Plugin Support
The Crowdstrike LogScale plugin is used to ingest Netskope Events, Netskope Alerts data and Web Transaction data in JSON format to the LogScale platform.
Data Type
Support
Event Support
Yes
Alert Support
Yes
WebTx Support
Yes (via Netskope LogStreaming)
All Netskope events, alert logs, and web transaction logs will be shared.
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope LogStreaming
or
Azure Netskope LogStreaming
plugin.
Permissions
For generating the Ingest Token, make sure your user account has the
Change ingest tokens
option. If not, contact your Organization Owner to generate and provide the Change ingest tokens access for your user.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/api/v1/ingest/hec
POST
Ingest data to Crowdstrike LogScale
Ingest Data
API Endpoint:
https://cloud.community.humio.com/api/v1/ingest/hec
Method:
POST
Parameters:
N/A
Headers:
Authorization: Bearer
<API Token>
Content-Type: application/json
Data:
{"event": {"_id": "224663acb2caf3ed8f833dd2", "justification_type": 23, "_insertion_epoch_timestamp": 1659017873, "access_method": "Client", "severity": "medium", "activity": "Upload", "activity_status": "Access Denied", "alert": "no", "app": "Alfresco", "app_session_id": 3606717343140728736, "appcategory": "Business Process Management", "browser": "Chrome", "browser_session_id": 2888757212810986401, "browser_version": "54.0.2840.90", "category": "Business Process Management", "cci": 56, "ccl": "low", "policy": "abc_ga_ti", "alert_name": "Malware found", "connection_id": 465830538214629538, "count": 1, "device": "Windows Device", "device_classification": "unmanaged", "dst_country": "US", "dst_geoip_src": 1, "dst_latitude": 47.682899, "dst_location": "Redmond", "dst_longitude": -122.120903, "dst_region": "Washington", "dst_timezone": "America/Los_Angeles", "dst_zipcode": "98052", "dstip": "13.107.6.151", "file_size": 105224532, "instance_id": "autoskope", "managed_app": "yes", "md5": "018c06f8ebef9e4c2ee6075db5825e24", "object": "TestResult_20170904-002256_demo.jpg", "object_type": "File", "organization_unit": "", "os": "Windows Server 2012", "os_version": "Windows Server 2012", "other_categories": ["Cloud Storage"], "page": " ", "page_site": "alfresco.com", "parent_id": "/personal/autotest3_autoskope_com/Documents", "referer": "https:// ", "site": "Alfresco.com", "slc_latitude": 13.0878400803, "slc_longitude": 80.2784729004, "src_country": "IN", "src_geoip_src": 2, "src_latitude": 12.8996, "src_location": "Chennai", "src_longitude": 80.2209, "src_region": "Tamil Nadu", "src_timezone": "N/A", "src_zipcode": "600001", "srcip": "52.172.6.204", "telemetry_app": "", "traffic_type": "CloudApp", "transaction_id": 1131464417688413744, "type": "nspolicy", "ur_normalized": "valeri.bradshaw@kkrlogistics.com", "url": "autoskope-my.sharepoint.com/personal/autotest3_autoskope_com/_api/web/GetFolderByServerRelativeUrl(@a1)/Files/Add(url=@a2,overwrite=@a3)", "user": "Valeri.Bradshaw@kkrlogistics.com", "userip": "10.0.0.5", "userkey": "v@kkrlogistics.com", "@timestamp": "2022-07-28T14:17:49Z"}}
Sample API Response:
{
    "text": "Success",
    "code": 0,
    "eventCount": 2
}
Performance Matrix
This performance reading is for a Large Stack CE tested with these VM specifications. These readings are added considering that it will ingest 10K alerts and events in 15 seconds.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Events, Alerts ingested to third-party SIEM
200K EPM
User Agent
netskope-ce-5.0.0-cls-crowdstrike-logscale/1.1.0
Workflow
Get your LogScale configuration parameters.
Configure the LogScale plugin.
Configure Log Shipper Business Rules for LogScale.
Configure Log Shipper Log Delivery for LogScale.
Validate the LogScale plugin.
Click play to watch a video.
Get your LogScale Configuration Parameters
Following configuration parameters are needed to configure the CrowdStrike LogScale plugin for Netskope Log Shipper.
CrowdStrike LogScale Host
: URL of your CrowdStrike LogScale Platform.
Ingest Token
: An Ingest Token is a unique string that identifies a repository and allows you to send data to that repository.
Generate an Ingest Token
Log in to your CrowdStrike LogScale instance.
Select your repository from the repositories and views page and click
Settings
.
Go to
Ingest tokens
and click
Add token
.
Add a Token name and select a JSON parser by selecting a JSON parser from the Assigned parser list.
Click
Save
.
Click on the eye icon on the Ingest Token page for the token you have created, you will see your Ingest token value. Copy it to use while configuring the plugin.
Configure the CrowdStrike LogScale Plugin
Go to
Settings > Plugin Store
. Search for and select the
CrowdStrike LogScale v1.1.0 (CLS)
plugin.
Add a Configuration Name and make sure the CrowdStrike LogScale Default Mapping is selected.
Disable the toggle button that is used to transform the raw logs, as the plugin only supports sharing of JSON formatted data.
Click
Next
and enter these parameters:
CrowdStrike LogScale Host
Ingest Token
Click
Save
. Your new plugin configuration can be seen at
Log Shipper > Plugin
.
Configure a Log Shipper Business Rule for LogScale
Go to
Log Shipper > Business Rules
, and by default, there’s a business rule that filters all alerts and events.
If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter. When finished, click
Save
.
Configure Log Shipper Log Delivery for LogScale
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (Netskope CLS), and Destination plugin (CrowdStrike LogScale), select a business rule, and click
Save
.
For WebTx, select the Source plugin (AWS Netskope LogStreaming or Azure Netskope LogStreaming), Destination plugin (
CrowdStrike LogScale
), and click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant and ingested into the Crowdstrike LogScale platform.
Validate the LogScale Plugin
Validate the Pull
In Cloud Exchange, go to
Logging
search for the pulled logs with the filter
message contains pulled
.
Validate the Push
Validate in Cloud Exchange
Go to
Logging
.
Search for ingested alerts with the filter
message contains ingested
.
The ingested logs will be filtered.
Validate in CrowdStrike LogScale
Go to the Search tab.
Apply filters to see specific data.
Troubleshooting
Ingested data is not visible on the LogScale Platform.
The LogScale cloud community has a data retention of 7 days. Any data older than the data retention period will not be available on the CrowdStrike LogScale platform.
What to do:
Check the data retention time on your platform from
Settings > Data retention
.
Update the data retention time. If you do not have access to update the data retention time, contact your CrowdStrike LogScale administration team.
In this Topic
CrowdStrike LogScale Plugin for Log Shipper

---
## Bitsight ThirdPartyTrust Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/bitsight-thirdpartytrust-plugin-for-log-shipper/
**Last Modified:** 2026-05-28T22:51:59+00:00
**Scraped:** 2026-08-10T07:51:13.169387+00:00

Bitsight ThirdPartyTrust Plugin for Log Shipper - Netskope Technical Documentation
Bitsight ThirdPartyTrust Plugin for Log Shipper
This document explains how to configure the ThirdPartyTrust plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This integration allows pushing alerts and events from Netskope to the ThirdPartyTrust platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
An account on the ThirdPartyTrust platform with Admin privileges.
Workflow
Get your ThirdPartyTrust API key.
Configure a New Plugin Repository.
Configure the ThirdPartyTrust plugin.
Configure Log Shipper Business Rules for ThirdPartyTrust.
Configure Log Shipper SIEM Mappings for ThirdPartyTrust.
Get your API Key from the ThirdPartyTrust Platform
Log in to your ThirdPartyTrust account that has Admin privileges.
Go to
Settings > Integrations
and copy an existing API Key for later. You can also generate a new API key by clicking
Generate Key
.
Configure a New Plugin Repository
To add the ThirdPartyTrust plugin to your Netskope Cloud Exchange instance, you need to configure a new plugin repository.
Go to
Settings > Plugin Repository
and click
Configure New Repository
.
Enter these following parameters:
Repository Name:
thirdpartytrust_repo
(can be any name).
Repository URL:
https://bitbucket.org/thirdpartytrust/netskope-plugin-install.git
Username and Password for your ThirdPartyTrust account.
Click
Save
.
Configure the BitSight Plugin
Go to
Settings > Plugins
, search for and select the BitSight plugin box to open the plugin creation pages.
Enter a Name and select the BitSight Default Mapping, and then click
Next
.
Enter your ThirdPartyTrust API key, and then click
Save
.
Configure a Log Shipper Business Rules for Bitsight
Go to
Log Shipper > Business Rules
.
Add only the
page and application event_type
filter values, or use the default
All
rule. The Bitsight plugin will only send
page
and
application
event types, discarding any other type of information.
Click
Save
.
Configure Log Shipper SIEM Mappings for Bitsight
Go to
Log Shipper > SIEM Mappings
and click
Add SIEM Mapping
.
For the Source Configuration, select the Netskope CLS plugin, and for Destination Configuration, select
the BitSight plugin. Select a Business Rule (or the default “All”) for this mapping.
Click
Save
.
The information will be processed by ThirdPartyTrust daily, at night.
The Discovered Vendors tab will appear in the ThirdPartyTrust application after the first set of data is processed, so you should be able to see it the day after you configured the plugin.
In this Topic
Bitsight ThirdPartyTrust Plugin for Log Shipper

---
## Datadog Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/datadog-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:19:30+00:00
**Scraped:** 2026-08-10T07:53:13.373218+00:00

Datadog Plugin for Log Shipper - Netskope Technical Documentation
Datadog Plugin for Log Shipper
This document explains how to configure the Datadog v1.1.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports the ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, and CTEP), Events (Page, Application, Audit, Infrastructure, Network, Incident, and Endpoint),
WebTx(via Netskope LogStreaming
), and Logs (Debug, Information, Error, and Warning) into the Datadog platform. It supports the ingestion of logs in both JSON and CEF formats.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming plugin
already configured (for pulling WebTx from the Netskope Log Streaming plugins).
A Netskope Cloud Exchange tenant with the
Syslog for CE
plugin already configured (for pulling CE Logs).
Datadog Platform access with the Datadog Agent installed.
Connectivity to the following hosts (any of these)
https://app.datadoghq.com
https://us3.datadoghq.com
https://us5.datadoghq.com
https://app.datadoghq.eu
https://app.ddog-gov.com
https://ap1.datadoghq.com
Datadog Plugin Support
Datadog plugin is used to ingest all the Alert, Events, CE Logs and WebTx[via Netskope LogStreaming] logs in CEF and JSON format.
Data Type
Support
Alerts
Yes. DLP, Malware, Policy, Compromised Credentials, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA
Event
Yes. Audit, Application, Infrastructure, Network, Incident, Page, Endpoint
WebTx
Yes (Compressed) (via Netskope LogStreaming)
Syslog CE Logs
Yes. Info, Error, Warning, Debug
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Permissions
Permission to generate an API Key in Datadog.
API Details
List of APIs used
API Endpoint
Method
Use Case
https://http-intake.logs.datadoghq.com/api/v2/logs
POST
Send Logs to the Datadog Platform
Send Logs
API Endpoint:
https://http-intake.logs.datadoghq.
<Datadog site>
/api/v2/logs
Method:
POST
Headers:
Key
Value
Content-Type
application/json
Accept
application/json
Content-Encoding
gzip(Only for WebTX[via Netskope LogStreaming] logs)
DD-API-KEY
<API Key>
User-Agent
netskope-ce-5.1.0-cls-datadog-v1.1.0
Parameters:
Key
Value
ddsource
netskope-ce
ddtags
netskopelogs,alerts
Request Body:
[{'message': '{"cci": 43, "timestamp": 1708515322000, "ccl": "poor", “ce_tenant_name”: “Plugins”}'}]
Sample API Response:
202 Accepted
Performance Matrix
This performance reading is conducted on a Large Stack CE with these VM specifications. These readings are noted with the consideration that it will ingest around 10K events in 10 seconds to the Datadog platform.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to SIEM
~200k EPM
User Agent
The user-agent added in this plugin is in the following format
netskope-ce-
<ce_version>
-
<module>
-
<plugin_name>
-v
<plugin_version>
For example:
netskope-ce-5.1.0-cls-datadog-v1.1.0
Workflow
Get your Datadog API Key.
Configure the Datadog Plugin.
Configure a Business Rule for the Datadog Plugin.
Configure Log Delivery for the Datadog plugin.
Validate the Datadog plugin.
Click play to watch a video.
Get your Datadog API Key
Log in to your machine where the Datadog Agent is installed.
Go to your Datadog agent directory as per your OS (
https://docs.datadoghq.com/agent/?tab=Linux
)
Open datadog.yaml file.
Change to
logs_enabled: true
.
Based on your OS flavor, you need to restart your Datadog Agent.(
https://docs.datadoghq.com/agent/?tab=Linux
)
Log in to Datadog Platform.
Hover on your username from the bottom Left corner.
Click
Organization Settings
.
Under
Access
click
API Keys
.
Click on the API Key, and then click
Copy
to copy the key.
Configure the Datadog Plugin
Go to
Settings > Plugin Store
. Search for and select the
CLS Datadog v1.1.0 (CLS)
plugin.
Add a plugin configuration name and make sure the
Datadog Default Mapping
file is selected for
Mapping
.
Disable the toggle button to transform the logs if you want to ingest the data in JSON format; keep it enabled if you want to ingest the data in CEF format.
Click
Next
and enter these parameters:
Datadog Site: The site associated with your Datadog account. For example: datadoghq.com.
API Key: An API Key is required by the Datadog Agent to submit metrics and events to Datadog. Provide the Datadog API Key obtained previously (from
Organization Settings > Access > API Keys
on the Datadog platform.
Datadog Tags: Tags associated with your logs. To add multiple tags, provide them as comma-separated values. For example:
env:prod,region:us-east-1
.
Click
Save
. The new plugin will be seen on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for Datadog
Go to
Log Shipper > Business Rules
.
By default, there is a business rule that filters all alerts and events.
If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Click
Save
.
Configure Log Shipper Log Delivery for Datadog
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (Netskope CLS), Destination plugin (Datadog), a business rule, and then click
Save
.
For WebTX select Source plugin (AWS Netskope Logstreaming or Azure Netskope Logstreaming), Destination plugin (CLS Datadog)
, a business rule, and then click
Save
.
For log sharing, select Source plugin (Syslog for CE) and Destination plugin (Datadog), a business rule, and then click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Datadog platform.
Validate the Datadog Plugin
Validate the Pull
To validate the pulling of Events, Alerts, logs, and Webtx (via Netskope LogStreaming) from the Netskope tenant:
Go to
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow:
Go to
Logging
and Search for ingested Events, Alerts & WebTx (via Netskope LogStreaming) with the filter
message contains ingested
. The ingested logs will be filtered.
To validate the push on Datadog, follow these steps:
Log in to the Datadog Platform.
Click
Logs
. You have the ability to apply filters based on your host by utilizing your Tenant name.
Troubleshooting the Datadog Plugin
Not able to see JSON Data on Datadog in historical cycle
Note
: Data in JSON format sent to Datadog will not appear on the platform if it is more than 18 hours old.
The logs in Cloud Exchange for the historical data in JSON format will show Ingested without any Error.
What to do
: Edit the Plugin and change the JSON to CEF format by enabling the transform logs option, so it will share the Historical Data.
In this Topic
Datadog Plugin for Log Shipper

---
## Local Export Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/local-export-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:22:44+00:00
**Scraped:** 2026-08-10T07:53:14.563161+00:00

Local Export Plugin for Log Shipper - Netskope Technical Documentation
Local Export Plugin for Log Shipper
This document explains how to configure the Local Export with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to deliver web transactions data to a designated location in your local storage.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured
.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
Plugin Scope
This plugin is used to deliver web transactions data to the Local Storage where your Netskope Cloud Exchange is installed.
Local Export Plugin Support
Data Type
Support
Events
No
Alerts
No
WebTx Logs
Yes (via Netskope Log Streaming)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Permissions
Permission to create a folder in a container with Read, Write, and Execute rights.
Permission to mount the folder in Docker File (required only if you want the data outside of the containers).
Performance Matrix
Note
As this plugin deals with ingestion of WebTx data, we recommended that you use a
Large Cloud Exchange Stack
with a mass storage capacity.
Workflow
Mount a directory outside of the core container.
Configure the Local Export plugin.
Configure Log Delivery for the Local Export plugin.
Validate the plugin.
Click play to watch a video.
Mount a Directory Outside of the Core Container
Utilizing mounting allows data retrieval from the Core Container without the need to access the container itself. Moreover, in the event of the container shutting down, all data within the container is deleted.
Follow these steps to mount the container with folder:
Log in to the machine where CE is installed.
Create the folder where you want to store data outside the container.
Go to the folder you created, and run
pwd
command for the path of that folder, and copy that path because it will be required for mounting.
Go to the folder where Netskope CE is installed.
Run this command to edit the
docker-compose.yml
file:
vi docker-compose.yml
.
Inside
docker-compose.yml
, go to
core:
, and below
volumes:
, add the new line with the path of the folder on the left separated with
:
, and then enter the path inside of the container in which you going to collect the WebTx data.
Path would be like
/home/devuser/WebTx_Data:/opt/Local_Export
.
Now go inside your docker container to create a empty folder that will collect data inside it.
To go inside the docker container, run
docker-compose exec -u 0 core sh
.
Inside the container, create a folder with the name you used in the
docker-compose.yml
file (like Local_Export as the folder name).
Give permission for Write and Executable using:
chmod 777 -R Local_Export(Folder Name)
.
Exit the container using
exit
.
Restart the Core container using
docker-compose restart core
.
Configure the Plugin using the same directory created inside the container.
Configure the Local Export Plugin
In Cloud Exchange, go to
Settings
>
Plugin Store.
Search for and select the
Local Export v1.0.0 (CLS)
plugin.
Enter a Configuration Name.
Click
Next
.
Enter these parameters:
Storage Path
: Storage path where data objects will be stored.
Object Prefix
: Object prefix for the data object name while pushing to the storage path. ‘/’ is not allowed in the object prefix.
Maximum File Size (in MBs)
: Maximum size of data object to be stored in the storage path. Value should be between 1 to 100.
Maximum Duration (in Seconds)
: Maximum duration after which the data object should be stored in the storage path.
Click
Save
. Your new plugin is be available on the
Cloud Log Shipper > Plugins
page.
Configure Log Delivery for the Local Export Plugin
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (AWS LogStreaming or Azure LogStreaming), the Destination plugin (Local Export) and click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested inside the container folder.
Validate the Local Export Plugin
Validate the Push
To validate the plugin workflow in Cloud Exchange.
Go to
Logging
and search for ingested events with the filter
CLS Local Export [plugin name]Successfully
.
The ingested logs will be filtered.
To validate the push from the docker container, follow these steps:
Log in to the machine where Cloud Exchange is installed.
Move to the folder where Cloud Exchange is installed.
Run
docker-compose exec -u 0 core sh
.
Go to the Storage Path you entered while configuring the plugin.
Run
ls
.
If you are using the Mounted Directory, then you can also check in that directory.
Troubleshooting the Local Export Plugin
Check folder has enough permissions to ingest data.
If not, then you need to give permission to that folder inside the container.
Log in to the machine where Cloud Exchange is installed.
Move to the folder where Cloud Exchange is installed.
Run
docker-compose exec -u 0 core sh
.
To check permissions, run
ls -l
.
To give permission to the folder, use
chmod 777 -R Local_export
(The folder where you want to ingest the data)
Limitations
This plugin’s functionality is limited to container-based deployments and it will not work with OVA deployments, as it does not allow editing the
docker-compose.yml
file. The changes required in the
docker-compose.yml
file will differ for each deployment. Refer to the respective deployment guides for the required changes.
As this plugin stores the WebTx data locally, it would consume an outrageous amount of storage space and can cause storage issues.
In this Topic
Local Export Plugin for Log Shipper

---
## AWS SQS Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/aws-sqs-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:45:18+00:00
**Scraped:** 2026-08-10T07:53:44.814790+00:00

AWS SQS Plugin for Log Shipper - Netskope Technical Documentation
AWS SQS Plugin for Log Shipper
This document explains how to configure the AWS SQS plugin for the Log Shipper module of the Netskope Cloud Exchange platform.This plugin supports ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA) data to the AWS SQS platform. To access the plugin, you would need the credentials of AWS. Note: This plugin supports ingestion in JSON format on the AWS SQS Queue.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
Connectivity to AWS SQS.
Connectivity to the following host: https://
<aws_region>
.console.aws.amazon.com/. For example: https://us-east-1.console.aws.amazon.com/
AWS SQS service access.
AWS SQS Plugin Support
AWS SQS plugin is used to ingest Netskope Alerts data to AWS SQS Queue. This plugin supports sending data in the JSON format to the SQS Queue.
Event Types
Not Supported
Alert Types
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA)
Log Types
Not Supported
WebTx Support
Not Supported
Mappings
Netskope Field
AWS SQS Field
alert_name
Name
alert_type
Type
Permissions
Amazon SQS Queue permissions to the IAM user to send Alerts data to Queue. Follow the steps mentioned in
Create a SQS Queue Policy
.
API Details
List of APIs Used
This plugin uses Python libraries to create and ingest data in AWS SQS.
Library: The AWS SDK for Python (Boto3).
Usage: The AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Simple Queue. Service (Amazon SQS), Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
Creating the SQS Client
:
sqs_client= boto3.client(
                "sqs",
                aws_access_key_id=self.aws_public_key,
                aws_secret_access_key=self.aws_private_key,
                aws_session_token=self.aws_session_token,
                region_name=self.region_name,
                config=Config(proxies=self.proxy, user_agent=self.useragent),
            )
Creating a Queue
:
queue= sqs_client.create_queue(
                        QueueName=queue_name
                    )
Getting a Queue URL
:
queue_url = sqs_client.get_queue_url(
                        QueueName=queue_name
                    )
Sending Messages in a Batch
:
response = sqs_client.send_message_batch(
                         QueueUrl=queue_url, Entries=batches
                      )
Performance Matrix
This performance reading is for a Large Stack CE tested on the below-mentioned VM specifications. The below readings are added with the consideration that it will ingest around 10K file size in 21 seconds.
Stack details
Size: LargeRAM: 32 GB
CPU: 16 Cores
Events, Alerts ingested to third-party SIEM
200K EPM
User Agent
netskope-ce-5.0.1-cls-aws_sqs-v1.0.0
Workflow
Create an AWS SQS Queue and Queue Policy.
Generate a Private Key, Certificate Body, Password Phrase, Profile ARN, Role ARN, Trust Anchor ARN, if using AWS IAM Role Anywhere for authentication. Or use another AWS authentication configuration.
Create a Queue.
Configure the AWS SQS Alerts plugin.
Configure a Business Rule.
Configure a SIEM Mapping.
Validate the plugin.
Click play to watch a video:
Create AWS SQS Queue
The queue name created here will be used in the Queue Name parameter while configuring the plugin.
To create a queue and set the required policies, log in to the AWS console.
From All Services, search for and select
Simple Queue Service
.
Click
Create queue
.
For Type, select
Standard
. Enter a name for the queue.
Provide the Configuration info according to your needs.
Enable Server-side encryption, and select
Amazon SQS Key
for the Encryption key type.
Select the Access policy, Redrive allow policy, Dead-letter queue, and Tags per your requirements. Click on Create.
The Queue is created successfully.
Create a SQS Queue Policy
Search for IAM, and on the left panel, click on
Policies
.
Click
Create policy
.
Click on the JSON tab, and enter the below-mentioned policy. Click
Next: Tags
and then
Next: Review
.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "sqs:GetQueueUrl",
                "sqs:SendMessage",
                "sqs:CreateQueue"
            ],
            "Resource": "arn:aws:sqs:*:XXXXXXXXXXX:*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "sqs:ListQueues",
            "Resource": "*"
        }
    ]
}
Enter a Name and click
Create Policy
.
Attach this policy to the user. Go to
IAM > Users
. Select the user that you want to attach a policy to, click
Add permissions
, and then click on Add permissions options.
Select
Attach policies directly
under Permissions, and search and select the policy created in the previous step for the source queue.
Click
Next
, and then click
Add permissions
. The policy will be attached to the user.
Plugin Authentication Methods
IAM Role Anywhere Authentication
Prerequisites
The
AWS Certificate Manager
service is required to be enabled to authenticate the plugin using the
AWS IAM Roles Anywhere
Authentication Method.
Make sure you create the Private Certificate Authority, Trust Anchor and Profile in the same region in which your AWS S3 Source Bucket resides.
Create a Policy
This Policy contains the required permissions for creating Private CA Certificate (including Permissions for creating Trust Anchor and Profile) and using the IAM Roles Anywhere.
Go to Policy Generator and select IAM Policy as policy type, enter Add Statement details, and generate a policy.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Private Certificate Authority
Actions:
CreateCertificateAuthority
DescribeCertificateAuthority
GetCertificate
GetCertificateAuthorityCertificate
GetCertificateAuthorityCsr
ImportCertificateAuthorityCertificate
IssueCertificate
ListCertificateAuthorities
ARN: *
Click
Add Statement
.
Scroll back up to add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management (IAM)
Actions:
AttachRolePolicy
CreateAccessKey
CreateRole
DeleteRole
PassRole
ARN: *
Click
Add Statement
.
Scroll back up to add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Certificate Manager
Actions:
DescribeCertificate
ExportCertificate
GetCertificate
ListCertificates
ListTagsForCertificate
RequestCertificate
ARN: *
Click
Add Statement
.
Scroll back up to add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management Roles Anywhere
Actions:
CreateProfile
CreateTrustAnchor
GetProfile
GetTrustAnchor
ListProfiles
ListTrustAnchors
ARN: *
Click
Add Statement
.
Click
Generate Policy
.
Copy the Policy as it will be used in the next step for creating the policy required for creating the Private CA certificates.
Go to AWS Console and select
IAM
from
All Services
. Click
Policies
in the left panel, and then click
Create Policy
.
Copy the policy to the JSON tab, click
Next:Tags
, and then click
Next:Review
.
Enter a name (like
netskope-ce-rolesAnywhere-policy
) and click
Save Changes
.
Create a Private Certificate Authority
Log in to AWS Console.
Search for
Certificate Manager
.
Click
AWS Private CA
.
Click
Create a private CA
.
For
Mode Options
, select
General-purpose
.
For
CA type options
, select
Root
.
Enter
Organization (O)
.
For
Key algorithm options
, select
RSA 2048
.
Add tags
if any (optional).
Check the checkbox in the
CA permissions options
section.
Check the checkbox in the
Pricing
section.
Click
Create
to create the CA certificate.
From
Actions
, select
Install
.
Click
Confirm and Install
.
Create a Trust Anchor
Search for the
IAM
service, go to Roles under Access management scroll down to Roles Anywhere and select
Manage
.
Click
Create a Trust anchor
Enter a
Trust anchor name
, like
netskope-ce-trust-anchor
.
Select
AWS Certificate Manager Private CA
(created in the previous steps) as a
Certificate authority (CA) source
Add tags if required.
Click
Create a trust anchor
.
Click on created
Trust Anchor
and copy the
Trust Anchor ARN
.
Create an IAM Role
Go to IAM services in the AWS Console.
Click
Role
in the Access Management submenu.
Click
Create Role
.
In the Trusted entity type, select
Custom Trust Policy
.
Go to
Policy Generator
.
Replace the Custom trust Policy with the below Trust Policy. This policy contains the permissions for using the roles anywhere service:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "rolesanywhere.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetSourceIdentity"
            ]
        }
    ]
}
Click
Next
.
In the Permissions policies, select the policy created in Create a SQS Queue Policy.
Click
Next
.
Provide a Role name (like
AWS-SQS-Role
) and Description for the role.
Click
Create role
.
Make a note of the Role ARN
as this will be required in the Plugin configuration parameter
Role ARN
for the authentication method
AWS IAM Roles Anywhere
.
Create a Profile
Select
Roles
under
Access management
.
Scroll down to
Roles Anywhere
and click
Manage
.
Expand the Setup steps.
Click
Step 2: Configure roles
.
Click
Configure a profile
.
Enter a Profile name, like
netskope-ce-profile
.
Select the role created in
Create IAM Role
netskope-ce-roleAnywhere
.
Remove the
Inline Policy
.
Click
Create profile
.
Select the created
Profile
and copy the
Profile ARN
.
Request a Private Certificate
Go to
AWS Certificate Manager > Request certificate
.
Select
Request a private certificate
.
Click
Next
.
Select the Certificate authority created in the previous step.
Provide a domain name in the Fully qualified domain name field, like
netskope-ce.com
.
Select
RSA 2048
as the Key algorithm.
Add tags if required.
Acknowledge the Certificate renewal permissions.
Click
Request
.
Go to
List certificates
from the navigation pane of AWS Certificate Manager.
Select the certificate created previously.
Click
Export
.
Enter the
passphrase.
Make a note of the passphrase as it will be required for the Configuration of the AWS Security Lake Plugin using the
AWS IAM Roles Anywhere
Authentication method.
Click
Generate PEM Encoding
.
Download all the
Certificates
as it won’t be visible again. For new certificates you will need to Export them again.
For More Info go to AWS IAM Role Anywhere
AWS Authentication
Create a Role
Go to
IAM
services in the AWS Console.
Click
Create role
.
Select the
AWS Service
.
Under Use case, select
EC2
.
Click
Next
.
Select the permission policy created in Create an AWS SQS Policy.
Click
Next
.
Enter a Role Name (like
AWS-SQS-Role
) and add a Description.
Click
Create Role
.
Assign a Role to an EC2 Instance
Log in to your EC2 instance console.
Click
Instances
under
Instances
.
Go to
Action > Security > Modify IAM Role
.
Select the Role that you created above in Create a Role. (
netskope-ce-instance-role
).
Click
Add IAM Role
or
Modify IAM Role
.
Assign a Role to a K8s Instance
Open your Role created for ServiceAccount while creating K8s instance.
Attach the policy created in Create a AWS SQS Policy.
Configure the AWS SQS Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the AWS SQS Plugin to open the plugin creation dialog.
Enter a Configuration Name. Disable the transformation toggle button, as only sending JSON data is supported.
Click
Next
.
Enter values for these parameters:
Authentication Method: Select the method to be used for authentication (Deployed on AWS/AWS IAM Roles Anywhere)
Private Key: Private Key for decrypting the AWS Private CA Certificate. Required for AWS IAM Roles Anywhere authentication type.
Certificate Body: Certificate Body for AWS Public/Private CA Certificate. Required for AWS IAM Roles Anywhere authentication type.
Password Phrase: Password Phrase for decrypting the CA Certificate. Required for AWS IAM Roles Anywhere authentication type.
Profile ARN: AWS Profile ARN for AWS client authentication. Required for AWS IAM Roles Anywhere authentication type.
Role ARN: AWS Role ARN for AWS client authentication. Required for AWS IAM Roles Anywhere authentication type.
Trust Anchor ARN: AWS Trust Anchor ARN for AWS client authentication. Required for AWS IAM Roles Anywhere authentication type.
AWS SQS Region Name: AWS SQS Region Name from where to get the AWS queue. Make sure that the region name matches the region in the Profile ARN and Trust Anchor ARN.
AWS SQS Queue Name: AWS SQS Queue Name in which the data object will be stored.
Click
Save
. The new plugin will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for AWS SQS
Go to the Business Rule page.
By default, we have a business rule that filters all alerts and events. If you want to filter out any specific type of alert, click on ‘Create New Rule’ and configure a new business rule by adding the rule name and filter.
Configure a Log Shipper SIEM Mapping for AWS SQS
Go to
Log Shipper > SIEM Mappings
and click
Add SIEM Mapping
.
Select the Source plugin (CLS Netskope), the Destination plugin (CLS AWS SQS), the business rule, and then click
Save
.
After the SIEM mapping is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the AWS SQS Queue.
Validate the AWS SQS Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant, go to Logging in Netskope CE. Search for the pulled logs..
Validate the Push
To validate the plugin workflow in Netskope Cloud Exchange:
Go to Logging and search for ingested events with the filter
message contains ingested
.
The ingested logs will be filtered.
To validate the push on the AWS SQS Queue:
Go to AWS Console. On the Search bar, search for
Queue
and click
Simple Queue Service
.
Search the Queue you used while creating the plugin.
Click on the queue name, and then click
Send and receive messages
.
Scroll down and click
Poll for messages
.
All the shared data will be visible as shown below.
Specific alerts can be filtered out using the
Search messages
text box. Click on the ID to view the Alert details. Click on the Attributes tab to see the Name and Type Mapping of the alert.
Troubleshooting
Unable to configure the CLS AWS SQS plugin.
If you are unable to configure the CLS AWS SQS plugin, then, it could be due to one of these reasons:
If the authentication method IAM Role Anywhere, the certificate and other configuration parameters may not be present in the same region.
If the Netskope CE is deployed on AWS, using the Deployed on AWS authentication method, the proper role is not attached to the EC2 instance.
Invalid values provided to the configuration parameters.
IAM permissions not provided to the user on the AWS platform.
To solve these issues, follow the below-mentioned steps.
Make sure that the certificate and other configuration parameters are created in the same region.
Make sure to follow the Role Assign section to assign a proper role to the EC2 instance.
Make sure valid values are provided in the configuration parameters. Navigate to the logging page and verify the log message.
Provide the IAM permissions to the user using which configuration parameters are created.
Unable to push alerts on the AWS SQS Queue.
If you are unable to push alerts on the AWS SQS Queue, then it could be due to the
Queue being deleted from the AWS SQS platform after configuring the CLS AWS SQS plugin.
To solve this issue, update the plugin configuration with the new queue name.
Unable to find alerts on the AWS SQS Queue.
If you are unable to find alerts on the AWS SQS Queue, then it could be due to the Default message retention period being 4 days for the AWS SQS Queue. If alerts are older than the message retention period, alerts are automatically deleted.
To solve this issue, follow these steps:
Go to the AWS console and enter credentials to log in.
From All Services, Select Simple Queue Service or search for Simple Queue Service in the search bar.
Select your queue from the list and click on the Edit button.
In Configuration, update Message retention period as per your requirement.
In this Topic
AWS SQS Plugin for Log Shipper

---
## Topologies
**URL:** https://docs.netskope.com/en/topologies-sites/
**Last Modified:** 2026-07-28T18:24:08+00:00
**Scraped:** 2026-08-10T07:54:51.226632+00:00

Topologies - Netskope Technical Documentation
Topologies
The topologies section of the “Settings” page provides data on Sites and Gateways.
Sites
The data displayed in the “Sites” section will help you assess network and application performances on a per-site basis of your corporate sites. It will help you compare how multiple sites perform in order to quickly identify any degradation and find its root cause from a contextualized view.
Creating a site is mandatory for deploying Enterprise Stations.
It includes the IPSec/GRE tunnels (if any) and also defines the Network Probe tests to be performed by the attached Enterprise Station(s).
View a List of Existing Sites
You can view a list of sites that have been created by doing the following:
Go to
Digital Experience Management
>
Settings
>
Sites
(under the “Topologies” section).
A list of existing sites will be displayed on the “Sites” page.
Components of a Site
The following section provides information about the primary components of a site:
Site Identification
Site Location
Secured Tunnels and Associated POP Tests
Site identification
A site can be identified through two attributes:
Its name you can freely choose to align with your organization’s requirements.
Its subnet(s): this(ese) subnet(s) correspond(s) to the IP address range(s) used by the end users when connecting from the site. This is generally one or multiple private IP address range(s)/subnet(s).
Multiple IP addresses, IP address ranges and/or IP address subnets can be added by separating them by commas.
Site Location
A site is geographically localized through the configuration of the country and city in which it is deployed.
For example, this setting will allow you to see your corporate sites on a map. You’ll also be able to group and filter collected data by site locations.
Secured Tunnels and Associated POP Tests
The “POP Testing” section enables you to link the IPSEc and/or GRE tunnels that you have configured in your Netskope environment to the corresponding site.
This is done by selecting tunnels from the dropdown lists.
Only tunnels that are not yet assigned to any Enterprise Station are shown in the dropdown list.
Associating tunnels to the site will automatically trigger corresponding Network Probe tests from the Enterprise Station that is deployed on the site. No need to manually create Network Probes (please refer to the “Network Probes” section for more information).
In addition to automatically testing the Netskope POP through the associated IPSec/GRE tunnels, you can also request the Enterprise Station to mimic the behavior of NSClients that actively steer the traffic to Netskope cloud while working from the site.
For this, simply select the “Monitor NSClient connectivity” checkbox.
Finally, you can specify how the Network Probes tests will be performed:
The method can be freely chosen between ICMP and UDP.
The interval between consecutive Network Probe tests can be set between 5 and 60 minutes by 5 minutes increments. The default value is 5 minutes.
Please refer to the “Network Probes” section for more details.
When you are done with the configuration, click the
Save
button to apply the configuration.
Configure a New Site
Go to
Digital Experience Management
>
Settings
>
Sites
(under the “Topologies” section).
Click the
Create
button to start the site creation process.
The New Site configuration page will open.
Complete the following fields on the “New Site” configuration page:
Name
: Create a name for the site for site identification..
Subnets
: Create subnet(s) for site identification.
Location
Country:
Select a country.
City
: Choose the city where the site is located.
POP Testing
Monitor NSClient connectivity
: Check the associated box to monitor NSClient connectivity.
IPsec Tunnels
: Choose IPsec Tunnels.
GRE Tunnels
: Choose GRE tunnels.
Testing Method
: Select a testing method.
Test Interval
: Select a test interval period for the POP connectivity tests.
Click the
Create
button to create your new site.
The newly created site is now visible in the list of sites.
Gateways
The concept of “gateway” is required to identify the location of the users who are steering their traffic through the NSClient. Since these users may move frequently, working from corporate sites and from home, it is important to be able to identify their location at any given time without requiring them to indicate their work location. The following list provides additional information about gateways:
A Gateway is defined by the corporate site’s local Internet breakout’s public IP address. This corresponds to the local Internet Service Provider (ISP) connection IP address.
A gateway must be associated with at least one site.
Multiple gateways can be associated with a single site.
Multiple sites can be associated with a single gateway.
Bulk Import/Export
Simplify the process of creating or updating site and gateway objects within your Netskope tenant using the bulk import/export tool. This tool allows for the upload of bulk site and gateway definitions via predefined CSV, JSON, and YAML templates. The templates are available for download via the Netskope tenant UI within the Import/Export section of the DEM settings UI.
Once an import file is uploaded to the tenant UI, the tool will run a comparison process and generate an output of all the changes that will be applied. Please ensure these changes are reviewed before the file is imported. As a best practice recommendation, we recommend you export the existing sites and/or gateways in the format of your choice as a backup, make a copy where you will make your changes or additions and import the copy. You can simply re-import the backup copy if you need to rollback your changes
To Export Sites and Gateways
Browse to
Digital Experience Management
>
Settings
>
Topologies
>
Import/Export
.
Select either Gateways or Sites, under the Export section, click on the Export button based on the format of your choice. Exports in CSV, JSON, and YAML formats are supported.
In this Topic
Topologies

---
## Export 3rd Party App Data
**URL:** https://docs.netskope.com/en/export-3rd-party-app-data/
**Last Modified:** 2025-08-31T01:47:01+00:00
**Scraped:** 2026-08-10T07:55:44.109093+00:00

Export 3rd Party App Data - Netskope Technical Documentation
Export 3rd Party App Data
To export 3rd Party Apps page data into a CSV file, follow the procedure:
Log in to your Netskope tenant and navigate to
API-Enabled Protection
>
Security Posture SaaS
>
3rd Party Apps
.
Click on the
Export
button.
In the
Export CSV
window, fill in the required fields.
Choose Columns to Export: Choose the specific columns you want to include in the export.
Number of Rows: Decide on the number of rows to export. You can either:
Export all rows up to 500,000, or
Specify a custom number of rows.
Define Export Filename: Enter a name for the exported file.
Click
Export
. A CSV file will be downloaded on your system with the export name.
In this Topic
Export 3rd Party App Data

---
## Log Shipper Plugin
**URL:** https://docs.netskope.com/en/log-shipper-plugin/
**Last Modified:** 2026-07-17T00:52:06+00:00
**Scraped:** 2026-08-10T07:56:07.098992+00:00

Log Shipper Plugin - Netskope Technical Documentation
Log Shipper Plugin
Release Notes
2.3.1 (Requires minimum Cloud Exchange version 6.1.0 and minimum Netskope Provider version 1.6.1)
Added
Added coordinated cleanup of the shared client status iterator so it is removed only when no Netskope plugin (Risk Exchange or Log Shipper) is using it. This feature requires Netskope Provider plugin v1.6.1 and Cloud Exchange version v6.0.0 or above.
2.3.0
Added
Added support for pulling forensics fields for DLP Incidents, To pull and ingest these fields update your Netskope Tenant version to 1.5.0 and CE version to 5.1.2.
Added fields to download originalfile and subfile in Incident events.
2.2.1
Added
Fixed compatibility issue when using a newer Log Shipper plugin with older provider versions.
2.2.0
Added
Added support for Client status events, To pull and ingest this event type update your Netskope Tenant version to 1.4.0.
2.1.0
Added
Added support for device and content alerts.
2.0.0
Changed
The Log Shipper plugin has been restructured and is now available in the Default repository.
1.0.0
Added
Initial release.
This document explains how to configure the Log Shipper v2.3.1 plugin in the Cloud Exchange platform. This plugin is used to fetch Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content) and Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status) from your Netskope Tenant.
Prerequisites
To complete this configuration, you need:
A Netskope Tenant (or multiple, for example, production and development/test instances).
The
Netskope tenant plugin
already configured and the Log Shipper module enabled.
Connectivity to a Netskope tenant with permission to generate v2/RBACv3 tokens.
Have a 3rd-party plugin like
Syslog
already configured in Cloud Exchange.
Log Shipper Plugin Support
This plugin is used to fetch Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content) and Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status) from Netskope Tenant.
Data Type
Description
Event Types
Yes (Audit, Application, Infrastructure, Network, Incident, Page, Endpoint, Client Status)
Alert Types
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA, Device, Content)
WebTx
No
Note
Device and Content alerts are supported starting from Cloud Exchange CE v5.1.0 and Tenant Plugin v1.2.0
Client status event is supported starting from Cloud Exchange v5.1.1 and Tenant Plugin v1.4.0
Forensics Data for Incident events is supported starting from Cloud Exchange v5.1.2 and Tenant Plugin v1.5.0
Coordinated cleanup of the shared client status iterator is supported from Cloud Exchange v6.1.0 and Tenant (Provider) v1.6.1
Mappings
Mapping File for Forensics Data
For ingesting forensics fields in CEF format you replace the mapping for incident event with the below snippet. This is just the suggested snippet, you can edit/update this as per your need. Make sure to only replace the incident event snippet in your mapping and not the entire mapping.
"incident": {
"header": {
"Device Vendor": {
"default_value": "Netskope",
"transformation": "String"
},
"Device Product": {
"default_value": "$tenant_name",
"transformation": "String"
},
"Device Version": {
"default_value": "NULL",
"transformation": "String"
},
"Device Event Class ID": {
"mapping_field": "type",
"default_value": "incident",
"transformation": "String"
},
"Name": {
"default_value": "NULL",
"transformation": "String"
},
"Severity": {
"default_value": "Unknown",
"transformation": "String"
}
},
"extension": {
"NetskopeJustificationType": {
"mapping_field": "justification_type",
"transformation": "String",
"default_value": "test"
},
"NetskopeJustificationReason": {
"mapping_field": "justification_reason",
"transformation": "String"
},
"fileId": {
"mapping_field": "object",
"transformation": "String"
},
"sourceServiceName": {
"mapping_field": "site",
"transformation": "String"
},
"outcome": {
"mapping_field": "status",
"transformation": "String"
},
"duser": {
"mapping_field": "assignee",
"transformation": "String"
},
"cfp3Label": {
"mapping_field": "severity",
"transformation": "String"
},
"deviceExternalId": {
"mapping_field": "instance_id",
"transformation": "String"
},
"cfp4Label": {
"mapping_field": "exposure",
"transformation": "String"
},
"c6a4Label": {
"mapping_field": "acting_user",
"transformation": "String"
},
"suser": {
"mapping_field": "user",
"transformation": "String"
},
"filePath": {
"mapping_field": "file_path",
"transformation": "String"
},
"fsize": {
"mapping_field": "file_size",
"transformation": "Integer"
},
"fileType": {
"mapping_field": "file_type",
"transformation": "String"
},
"msg": {
"mapping_field": "dlp_match_info",
"transformation": "String"
},
"inlineMsg": {
"mapping_field": "inline_dlp_match_info",
"transformation": "String"
},
"requestMethod": {
"mapping_field": "access_method",
"transformation": "String"
},
"act": {
"mapping_field": "activity",
"transformation": "String"
},
"reportedResourceID": {
"mapping_field": "instance",
"transformation": "String"
},
"request": {
"mapping_field": "url",
"transformation": "String"
},
"reason": {
"mapping_field": "object_type",
"transformation": "String"
},
"c6a3Label": {
"mapping_field": "owner",
"transformation": "String"
},
"sourceZoneURI": {
"mapping_field": "owner_pdl",
"transformation": "String"
},
"c6a1Label": {
"mapping_field": "file_lang",
"transformation": "String"
},
"reportedResourceName": {
"mapping_field": "true_obj_category",
"transformation": "String"
},
"reportedResourceType": {
"mapping_field": "true_obj_type",
"transformation": "String"
},
"customerKey": {
"mapping_field": "dlp_incident_id",
"transformation": "Integer"
},
"dvcpid": {
"mapping_field": "latest_incident_id",
"transformation": "Integer"
},
"rawEvent": {
"mapping_field": "dlp_parent_id",
"transformation": "Integer"
},
"suid": {
"mapping_field": "from_user",
"transformation": "String"
},
"fileHash": {
"mapping_field": "md5",
"transformation": "String"
},
"spid": {
"mapping_field": "connection_id",
"transformation": "Integer"
},
"dpid": {
"mapping_field": "app_session_id",
"transformation": "Integer"
},
"sourceDnsDomain": {
"mapping_field": "referer",
"transformation": "String"
},
"destinationZoneExternalID": {
"mapping_field": "dst_location",
"transformation": "String"
},
"sourceTranslatedZoneExternalID": {
"mapping_field": "src_location",
"transformation": "String"
},
"requestCookies": {
"mapping_field": "channel",
"transformation": "String"
},
"duid": {
"mapping_field": "to_user",
"transformation": "String"
},
"cfp1Label": {
"mapping_field": "cc",
"transformation": "String"
},
"cfp2Label": {
"mapping_field": "bcc",
"transformation": "String"
},
"cat": {
"mapping_field": "classification",
"transformation": "String"
},
"IncidentID": {
"mapping_field": "transaction_id",
"transformation": "String"
},
"requestClientApplication": {
"mapping_field": "app",
"transformation": "String"
},
"dlpFile": {
"mapping_field": "dlp_file",
"transformation": "String"
},
"timestamp": {
"mapping_field": "timestamp",
"transformation": "Integer"
},
"eventId": {
"mapping_field": "_id",
"transformation": "String"
},
"forensics_originalfile_url": {
"mapping_field": "forensics_originalfile_url",
"transformation": "String8000"
},
"forensics_subfile_url": {
"mapping_field": "forensics_subfile_url",
"transformation": "String8000"
},
"forensics_content": {
"mapping_field": "forensics_content",
"transformation": "String8000"
},
"forensics_metadata_content": {
"mapping_field": "forensics_metadata_content",
"transformation": "String8000"
},
"forensics_dlp_match_info": {
"mapping_field": "forensics_dlp_match_info",
"transformation": "String8000"
}
}
}
Permissions
Access to the required permissions is available in the link provided in the
v2 REST API scopes
.
For Device and Content alerts and Client Status events, you will require the following permissions:
/api/v2/events/dataexport/alerts/device (Read)
/api/v2/events/dataexport/alerts/content (Read)
/api/v2/events/dataexport/iterator (Read+Write)
For pulling forensics data for incident events, you will require the below permission:
/api/v2/incidents/dlpincidents (Read)
API Details
List of APIs Used
Validation
API Endpoint
Method
Use Case
/api/v1/app_instances
GET
To validate v1 token.
/api/v2/events/dataexport/events/alert
GET
To validate v2 token while configuring tenant.
Alerts
API Endpoint
Method
Use Case
/api/v2/events/dataexport/alerts/dlp
GET
Pull DLP Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/malware
GET
Pull Malware Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/remediation
GET
Pull Remediation Alerts from Netskope tenant
/api/v2/events/dataexport/alerts/securityassessment
GET
Pull Security Assessment Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/ctep
GET
Pull CTEP Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/malsite
GET
Pull Malsite Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/policy
GET
Pull Policy Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/quarantine
GET
Pull Quarantine Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/uba
GET
Pull UBA Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/watchlist
GET
Pull Watchlist Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/device
GET
Pull Device Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/content
GET
Pull Content Alerts from the Netskope tenant.
Events
API Endpoint
Method
Use Case
/api/v2/events/dataexport/events/page
GET
Pull Page Events from the Netskope tenant.
/api/v2/events/dataexport/events/application
GET
Pull Application Events from the Netskope tenant.
/api/v2/events/dataexport/events/audit
GET
Pull Audit Events from the Netskope tenant.
/api/v2/events/dataexport/events/infrastructure
GET
Pull Infrastructure Events from the Netskope tenant.
/api/v2/events/dataexport/events/network
GET
Pull Network Events from the Netskope tenant.
/api/v2/events/dataexport/events/incident
GET
Pull Incident Events from the Netskope tenant.
/api/v2/incidents/dlpincidents/{id}/forensics
GET
Pull Incident Forensics per dlp_incident_id.
/api/v2/events/dataexport/events/endpoint
GET
Pull Endpoint Events from the Netskope tenant.
api/v2/events/dataexport/iterator/netskope_ce_cs_iterator?eventtype=clientstatus
POST
Create a Client Status Iterator.
/api/v2/events/dataexport/iterator/
<iterator_name>
GET
Check the Status of a Client Status Iterator.
/api/v2/events/dataexport/iterator/
<iterator_name>
/events?operation=next
GET
Fetch data from a Client Status Iterator.
api/v2/events/dataexport/iterator/
<iterator_name>
DELETE
Delete a Client Status Iterator.
Validate a v1 token
API Endpoint:
https://
<tenant-url>
/api/v1/app_instances
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Request Parameters
Key
Value
op
list
limit
1
Payload
{"token":
<netskope_api_v1_token>
}
Sample API Response
{
    "status": "success",
    "data": [
        {
            "app": "Oracle Aconex",
            "instance_name": "46",
            "instance_id": "46",
            "type": "Custom",
            "tags": [
                "Unsanctioned"
            ],
            "last_modified": "2025-02-24 09:59:54",
            "custom": "0",
            "app_id": "46"
        }
    ]
}
Validate a v2 Token
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/alert
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "abc350cdb1e1958a03ccd13c",
    "access_method": "Endpoint",
    "acked": "false",
    "action": "block",
    "activity": "Insert",
    "alert": "yes",
    "alert_name": "TestBlock",
    "alert_type": "Device",
    "app": "",
    "category": "",
    "cci": 0,
    "ccl": "unknown",
    "count": 1,
    "device_classification": "not configured",
    "organization_unit": "",
    "os": "macOS",
    "other_categories": [],
    "policy": "TestBlock",
    "timestamp": 1719994603,
    "traffic_type": "",
    "type": "endpoint",
    "ur_normalized": "kmaheshwari@netskope.com",
    "user": "kmaheshwari@netskope.com",
    "userkey": "kmaheshwari@netskope.com",
    "record_type": "alert",
    "to_object": "",
    "account_id": "",
    "CononicalName": "",
    "malsite_country": "",
    "src_geoip_src": 0,
    "object": "",
    "fromlogs": "",
    "ext_labels": [],
    "last_timestamp": 0,
    "justification_type": "",
    "tss_mode": "",
    "user_id": "",
    "password_type": "",
    "suppression_key": "",
    "connection_id": 0,
    "sha256": "",
    "site": "",
    "src_longitude": 0.0,
    "os_version": "",
    "resp_cnt": 0,
    "src_timezone": "",
    "user_confidence_index": 0,
    "browser_version": "",
    "dst_region": "",
    "last_app": "",
    "dlp_rule_count": 0,
    "sessionid": "",
    "profile_id": "",
    "threshold": 0,
    "org": "",
    "suppression_end_time": 0,
    "nsdeviceuid": "",
    "parent_id": "",
    "compliance_standards": [],
    "true_obj_category": "",
    "severity": "",
    "sa_profile_id": 0,
    "malsite_longitude": 0.0,
    "sa_rule_id": "",
    "region_name": "",
    "device": "",
    "dlp_mail_parent_id": "",
    "evt_src_chnl": "",
    "malsite_latitude": 0.0,
    "request_id": 0,
    "sa_rule_severity": "",
    "dst_latitude": 0.0,
    "universal_connector": "",
    "malsite_ip_host": "",
    "referer": "",
    "dst_geoip_src": 0,
    "severity_level": "",
    "conn_starttime": 0,
    "dsthost": "",
    "last_location": "",
    "useragent": "",
    "breach_description": "",
    "shared_domains": "",
    "asset_object_id": "",
    "malicious": "",
    "sa_rule_name": "",
    "breach_target_references": "",
    "justification_reason": "",
    "conn_duration": 0,
    "object_id": "",
    "userPrincipalName": "",
    "alert_id": "",
    "exposure": "",
    "mime_type": "",
    "true_obj_type": "",
    "user_generated": "",
    "total_collaborator_count": 0,
    "browser_session_id": 0,
    "dst_timezone": "",
    "appsuite": "",
    "retro_scan_name": "",
    "page_site": "",
    "last_device": "",
    "dlp_unique_count": 0,
    "sAMAccountName": "",
    "src_zipcode": "",
    "file_size": 0,
    "domain": "",
    "title": "",
    "conn_endtime": 0,
    "dst_location": "",
    "telemetry_app": "",
    "netskope_pop": "",
    "malsite_region": "",
    "serial": "",
    "web_universal_connector": "",
    "modified": 0,
    "iaas_remediated": "",
    "internal_collaborator_count": 0,
    "object_type": "",
    "domain_ip": "",
    "orig_ty": "",
    "threshold_time": 0,
    "src_location": "",
    "dlp_profile": "",
    "data_type": "",
    "web_url": "",
    "src_time": "",
    "severity_level_id": 0,
    "resource_category": "",
    "browser": "",
    "region_id": "",
    "dlp_incident_id": 0,
    "last_country": "",
    "threat_match_value": "",
    "netskope_activity": "",
    "server_bytes": 0,
    "dlp_file": "",
    "two_factor_auth": "",
    "breach_date": 0,
    "url": "",
    "policy_actions": [],
    "req_cnt": 0,
    "external_collaborator_count": 0,
    "dst_country": "",
    "log_file_name": "",
    "scan_type": "",
    "src_region": "",
    "threat_source_id": 0,
    "notify_template": "",
    "malsite_category": [],
    "numbytes": 0,
    "dlp_is_unique_count": "",
    "account_name": "",
    "file_path": "",
    "file_lang": "",
    "suppression_start_time": 0,
    "custom_attr": {},
    "email_source": "",
    "sanctioned_instance": "",
    "owner": "",
    "bypass_traffic": "",
    "src_latitude": 0.0,
    "page": "",
    "dstip": "",
    "hostname": "",
    "dstport": 0,
    "matched_username": "",
    "src_country": "",
    "file_cls_encrypted": false,
    "md5": "",
    "iaas_asset_tags": [],
    "file_type": "",
    "malsite_id": "",
    "app_session_id": 0,
    "protocol": "",
    "userip": "",
    "breach_media_references": "",
    "instance": "",
    "app_activity": "",
    "client_bytes": 0,
    "sa_profile_name": "",
    "instance_id": "",
    "http_transaction_count": 0,
    "breach_id": "",
    "transaction_id": 0,
    "from_user": "",
    "last_region": "",
    "managementID": "",
    "shared_with": "",
    "resource_group": "",
    "appcategory": "",
    "event_type": "",
    "asset_id": "",
    "srcip": "",
    "managed_app": "",
    "dlp_parent_id": 0,
    "breach_score": "",
    "dst_zipcode": "",
    "dlp_rule_severity": "",
    "orignal_file_path": "",
    "threat_match_field": "",
    "dst_longitude": 0.0,
    "external_email": 0,
    "policy_id": "",
    "dlp_rule": ""
}
Get Compromised Credential Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/compromisedcredential
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "20575270a59c8ef1d85d535c",
    "acked": "false",
    "alert": "yes",
    "alert_name": "Secret share",
    "alert_type": "Compromised Credential",
    "app": "Friend2Friend",
    "category": "Cloud Storage",
    "cci": 29,
    "ccl": "poor",
    "count": 1,
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "timestamp": 1727659690,
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0495t@test.netskope.com",
    "user": "dte1953ce410-0495t@test.netskope.com",
    "userkey": "dte1953ce410-0495t@test.netskope.com",
    "division": "",
    "external_email": 0,
    "mail": "",
    "sAMAccountName": "",
    "password_type": "",
    "userPrincipalName": "",
    "breach_date": 0,
    "sAMAccountType": "",
    "breach_id": "",
    "breach_score": "",
    "department": "",
    "employeeType": "",
    "matched_username": "",
    "breach_media_references": "",
    "email_source": "",
    "breach_description": "",
    "breach_target_references": "",
    "distinguishedName": ""
}
Get DLP Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/dlp
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "31365da11ecc94a0d7edfb6f",
    "access_method": "API Connector",
    "acked": "false",
    "action": "alert",
    "alert": "yes",
    "alert_name": "GDrive Customer metadata shared externally",
    "alert_type": "DLP",
    "app": "Google Drive",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "ccl": "high",
    "device": "Other",
    "dst_country": "US",
    "dst_geoip_src": 1,
    "dst_latitude": 37.40599060058594,
    "dst_location": "Mountain View",
    "dst_longitude": -122.0785140991211,
    "dst_region": "California",
    "dstip": "172.217.14.78",
    "exposure": "organisation_wide_link",
    "ext_labels": [
        {
            "data_classification_label": "pym/uducbb2126/encryption_level_11",
            "id": "6e05576c-782b-42b4-b8f7-71dfb9ffb5a0",
            "instance": "uducbb2126",
            "name": "encryption_level_11",
            "vendor": "pym"
        },
        {
            "data_classification_label": "ydu/ldmwyo2852/encryption_level_11",
            "id": "20c2b17d-7612-4349-b1e1-62d0d6b48ccb",
            "instance": "ldmwyo2852",
            "name": "encryption_level_11",
            "vendor": "ydu"
        },
        {
            "data_classification_label": "uwa/eqpoco8593/encryption_level_9",
            "id": "6f77b892-3888-4148-8168-d954856d2fea",
            "instance": "eqpoco8593",
            "name": "encryption_level_9",
            "vendor": "uwa"
        }
    ],
    "file_lang": "ENGLISH",
    "file_path": "/My Drive/Clickhouse/Tenant Migration across MPs",
    "file_size": 196869,
    "file_type": "application/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "local_sha256": "edd7df8bb5a774a7531a389287a3bd71cf8e62197d93a205860003ed8339a4de",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "Tenant Migration across MPs",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "unknown",
    "owner": "foobar",
    "policy": "GDrive Customer metadata shared externally",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "site": "Google Drive",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1716551379,
    "title": "Tenant Migration across MPs",
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "rowkuxqaxdxnlnlw",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "RoWkuxQAxDxNlNLw",
    "userkey": "RoWkuxQAxDxNlNLw",
    "record_type": "alert",
    "page_site": "",
    "act_user": "",
    "src_longitude": 0.0,
    "dst_timezone": "",
    "device_classification": "",
    "to_user": "",
    "dlp_file": "",
    "connection_id": 0,
    "external_collaborator_count": 0,
    "incident_id": 0,
    "dlp_fingerprint_classification": "",
    "activity": "",
    "from_storage": "",
    "user_confidence_index": 0,
    "browser_version": "",
    "dynamic_classification": "",
    "smtp_to": [],
    "dlp_rule_severity": "",
    "shared_with": "",
    "outer_doc_type": 0,
    "orignal_file_path": "",
    "channel": "",
    "data_type": "",
    "userip": "",
    "sanctioned_instance": "",
    "src_region": "",
    "true_filetype": "",
    "dlp_rule_count": 0,
    "shared_domains": "",
    "owner_pdl": "",
    "dlp_unique_count": 0,
    "transaction_id": 0,
    "browser_session_id": 0,
    "userCountry": "",
    "bcc": "",
    "displayName": "",
    "srcip": "",
    "dlp_mail_parent_id": "",
    "hostname": "",
    "classification_name": "",
    "protocol": "",
    "sAMAccountName": "",
    "violating_user": "",
    "manager": "",
    "src_time": "",
    "src_country": "",
    "true_obj_category": "",
    "message_size": 0,
    "dlp_fingerprint_score": 0,
    "src_geoip_src": 0,
    "os_version": "",
    "true_type_id": 0,
    "to_storage": "",
    "tss_mode": "",
    "managed_app": "",
    "file_password_protected": "",
    "dlp_incident_id": 0,
    "managementID": "",
    "dlp_fingerprint_match": "",
    "src_timezone": "",
    "mail": "",
    "total_collaborator_count": 0,
    "from_user": "",
    "app_activity": "",
    "user_id": "",
    "custom_attr": {},
    "group": "",
    "file_cls_encrypted": false,
    "universal_connector": "",
    "message_id": "",
    "file_category": "",
    "dlp_parent_id": 0,
    "sub_type": "",
    "src_latitude": 0.0,
    "userPrincipalName": "",
    "dlp_is_unique_count": "",
    "dlp_rule_score": 0,
    "src_zipcode": "",
    "dlp_rule": "",
    "referer": "",
    "app_session_id": 0,
    "parent_id": "",
    "retro_scan_name": "",
    "src_location": "",
    "dst_zipcode": "",
    "dlp_profile": "",
    "true_obj_type": "",
    "violating_user_type": "",
    "policy_id": "",
    "web_universal_connector": "",
    "appsuite": "",
    "severity": "",
    "sha256": "",
    "collaborated": "",
    "page": ""
}
Get Malware Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/malware
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "TSS-scan": "TSS-Scan-V3",
    "_id": "389551cd1bdaa1ae4947c334",
    "access_method": "Client",
    "acked": "false",
    "action": "Detection",
    "activity": "Browse",
    "alert": "yes",
    "alert_name": "GT:JS.Adware.Popunder.4.34B7F109",
    "alert_type": "Malware",
    "app": "hitomi",
    "app_name": "hitomi",
    "app_session_id": 4113602168491103340,
    "appcategory": "Adult Content - Pornography",
    "browser_session_id": 2610528494199657827,
    "category": "Adult Content - Pornography",
    "cci": "",
    "ccl": "",
    "connection_id": 5767115909713174088,
    "count": 1,
    "detection_engine": "Netskope AV",
    "device": "Linux Device",
    "device_classification": "not configured",
    "dst_country": "UA",
    "dst_latitude": 50.45465850830078,
    "dst_location": "Kyiv",
    "dst_longitude": 30.523799896240234,
    "dst_region": "Kyiv",
    "dst_timezone": "Europe/Kyiv",
    "dst_zipcode": "N/A",
    "dstip": "185.255.122.62",
    "file_category": "Text",
    "file_id": "1dda26cbf77944ccb931f3444b554c74",
    "file_size": 2277,
    "file_type": "text/html",
    "hostname": "ub20-50-5-28",
    "incident_id": 7718454634228557343,
    "instance": "",
    "local_md5": "cda70ab0130f915723a53a5d9270e7a5",
    "malware_id": "3d81bec28fff68180bf8baa5727924ba",
    "malware_name": "GT:JS.Adware.Popunder.4.34B7F109",
    "malware_profile": "1",
    "malware_severity": "high",
    "malware_type": "Virus",
    "managed_app": "no",
    "md5": "cda70ab0130f915723a53a5d9270e7a5",
    "ml_detection": "None",
    "object_type": "File",
    "organization_unit": "",
    "os": "Linux",
    "os_version": "Linux 20.04",
    "page": "hitomi.la/",
    "page_site": "Web Background",
    "policy": "Threat-Malware-Policy-Crest-SRE-Test",
    "policy_id": "342F7551F4D4469E47D7736209486319 2024-07-01 16:28:12.174470",
    "protocol": "HTTPS/1.1",
    "request_id": 2907585389470724608,
    "scanner_result": "malicious",
    "severity": "High",
    "severity_id": 3,
    "sha256": "d330ea88b7a0c2f9190717d8f39a2e3942474c3fefe8b68112e7b93fde0fa9d4",
    "site": "hitomi",
    "src_country": "IN",
    "src_latitude": 23.0276,
    "src_location": "Ahmedabad",
    "src_longitude": 72.5871,
    "src_region": "Gujarat",
    "src_time": "Wed Aug 14 13:48:00 2024",
    "src_timezone": "Asia/Kolkata",
    "src_zipcode": "382350",
    "srcip": "110.226.17.67",
    "timestamp": 1723623535,
    "traffic_type": "Web",
    "transaction_id": 7718454634228557343,
    "true_filetype": "HTML",
    "tss_mode": "inline",
    "type": "nspolicy",
    "ur_normalized": "nipun.brahmbhatt@crestdata.ai",
    "url": "hitomi.la/",
    "user": "nipun.brahmbhatt@crestdata.ai",
    "user_id": "nipun.brahmbhatt@crestdata.ai",
    "userip": "10.50.5.28",
    "record_type": "alert",
    "department": "",
    "scan_time": 0,
    "tss_scan_failed": "",
    "usr_udf_supervisorname": "",
    "instance_id": "",
    "nsdeviceuid": "",
    "modified_date": 0,
    "dst_geoip_src": 0,
    "local_sha256": "",
    "sha1": "",
    "usr_udf_primarydomain": "",
    "fastscan_results": "",
    "sanctioned_instance": "",
    "company": "",
    "user_confidence_index": 0,
    "src_geoip_src": 0,
    "usr_udf_businesssegmentlevel1": "",
    "referer": "",
    "parent_id": "",
    "created_date": 0,
    "usr_udf_businesssegmentlevel2": "",
    "filename": "",
    "from_user": "",
    "file_path": "",
    "manager": "",
    "browser": "",
    "detection_type": "",
    "title": "",
    "object_id": "",
    "mime_type": "",
    "usr_display_name": "",
    "usr_udf_businesssegmentlevel4": "",
    "userPrincipalName": "",
    "appsuite": "",
    "scan_type": "",
    "tss_license": "",
    "managementID": "",
    "usr_status": "",
    "object": "",
    "custom_attr": {},
    "userCountry": "",
    "usr_title": "",
    "usr_udf_businesssegmentlevel3": "",
    "file_name": "",
    "shared_type": "",
    "usr_udf_companyname": "",
    "shared_with": "",
    "tss_fail_reason": "",
    "usr_udf_supervisorid": "",
    "browser_version": "",
    "usr_udf_employeeid": ""
}
Get Remediation Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/remediation
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "448ca50ee6142a954d64c577",
    "access_method": "API Connector",
    "acked": "true",
    "action": "alert",
    "activity": "Download",
    "alert": "yes",
    "alert_name": "Remediation alert",
    "alert_type": "Remediation",
    "app": "Clanwilliam Health",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 9,
    "ccl": "poor",
    "count": 1,
    "device": "Other",
    "dst_country": "NL",
    "dst_geoip_src": 2,
    "dst_latitude": 52.3759,
    "dst_location": "Amsterdam",
    "dst_longitude": 4.8975,
    "dst_region": "North Holland",
    "dst_zipcode": "1012",
    "dstip": "31.186.239.8",
    "file_size": 118585,
    "file_type": "application/vnd.google-apps.document",
    "instance_id": "netskope.com",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "object": "VTRapjqhGbaDXqHR",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "Windows 7.0",
    "policy": "policy_ga34",
    "request_id": "2459149802892628500",
    "site": "Clanwilliam Health",
    "src_country": "NL",
    "src_geoip_src": 2,
    "src_latitude": 52.3759,
    "src_location": "Amsterdam",
    "src_longitude": 4.8975,
    "src_region": "North Holland",
    "src_zipcode": "1012",
    "srcip": "31.186.239.8",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0268t@test.netskope.com",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "dte1953ce410-0268t@test.netskope.com",
    "managementID": "",
    "from_user": "",
    "os_version": "",
    "app_session_id": 0,
    "malware_severity": "",
    "actions_taken": "",
    "transaction_id": 0,
    "notify_template": "",
    "page": "",
    "browser_session_id": 0,
    "src_time": "",
    "tss_mode": "",
    "managed_app": "",
    "severity": "",
    "nsdeviceuid": "",
    "remediation_profile": "",
    "dlp_profile": "",
    "malware_name": "",
    "endpoints": "",
    "connection_id": 0,
    "policy_id": "",
    "endpoint_count": 0,
    "dst_timezone": "",
    "profile_hits": [],
    "malware_id": "",
    "hostname": "",
    "edr_app": "",
    "device_classification": "",
    "userip": "",
    "appsuite": "",
    "protocol": "",
    "incident_id": 0,
    "src_timezone": "",
    "sanctioned_instance": "",
    "page_site": "",
    "malware_type": "",
    "all_policy_matches": []
}
Get Security Assessment Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/securityassessment
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "15bbca35f014e9618efdc629",
    "_insertion_epoch_timestamp": 1727659690,
    "access_method": "API Connector",
    "acked": "false",
    "action": "alert",
    "activity": "Introspection Scan",
    "alert": "yes",
    "alert_name": "security-accessment-alert",
    "alert_type": "Security Assessment",
    "app": "LinkedIn",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "ccl": "medium",
    "count": 1,
    "device": "Other",
    "dst_country": "FR",
    "dst_geoip_src": 1,
    "dst_latitude": 48.883411,
    "dst_location": "Puteaux",
    "dst_longitude": 2.23894,
    "dst_region": "Ile-de-France",
    "dstip": "193.248.155.211",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "\\/My Drive\\/Clickhouse\\/Tenant Migration across MPs",
    "file_size": 196869,
    "file_type": "application\\/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application\\/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "OlWmGNTVpEVLCgWo",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local\\/Netskope\\/Active Users\\/US & International\\/Full Time",
    "os": "unknown",
    "other_categories": [],
    "owner": "foobar",
    "policy": "GDrive Customer metadata shared externally",
    "request_id": "2459149802892628500",
    "sa_profile_id": 1,
    "sa_profile_name": "CRzpqYgDBoKRThmb",
    "sa_rule_id": "icveiWoIMGqmEfUy",
    "sa_rule_name": "RLYnpTzcFeiRcQYr",
    "sa_rule_severity": "High",
    "scan_type": "Ongoing",
    "shared_with": "none",
    "site": "LinkedIn",
    "src_country": "FR",
    "src_geoip_src": 1,
    "src_latitude": 48.883411,
    "src_location": "Puteaux",
    "src_longitude": 2.23894,
    "src_region": "Ile-de-France",
    "srcip": "193.248.155.211",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "crest_sup_de_202112031049-0@crest.netskope.com",
    "url": "https:\\/\\/drive.google.com\\/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "crest_sup_de_202112031049-0@crest.netskope.com",
    "usergroup": [],
    "userkey": "crest_sup_de_202112031049-0@crest.netskope.com"
}
Get CTEP Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/ctep
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_correlation_id": "d54406dc-5457-4699-8754-c8eece88a804",
    "_event_id": "8de38a44-4ae5-44ac-a097-f9e3ce2aac2a",
    "_forwarded_by": "na",
    "_generator_id": "ad4c77a8-ac83-4493-936c-8d6394038556",
    "_id": "d62273697847e13a884e7562",
    "_insertion_epoch_timestamp": 1727659690,
    "_raw_event_inserted_at": 1676185709059,
    "_seq_id": 117219,
    "_service_identifier": "na",
    "_skip_geoip_lookup": "yes",
    "access_method": "API Connector",
    "acked": "false",
    "action": "block",
    "activity": "Login Successful",
    "alert": "yes",
    "alert_name": "c2",
    "alert_type": "c2",
    "app": "X3host",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 16,
    "ccl": "poor",
    "count": 1,
    "device": "11-inch iPad Pro",
    "dst_country": "US",
    "dst_geoip_src": 2,
    "dst_latitude": 45.8234,
    "dst_location": "Boardman",
    "dst_longitude": -119.7257,
    "dst_region": "Oregon",
    "dst_zipcode": "97818",
    "dstip": "52.218.153.131",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "/My Drive/Clickhouse/Tenant Migration across MPs",
    "file_size": 118783,
    "file_type": "application/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "legal_hold_profile_name": "oejTJocnOabNirPx",
    "lh_custodian_email": "ELGkdoczLAkrQMuq",
    "lh_custodian_name": "iRwQlRYvjwsFlVpg",
    "lh_dest_app": "dOkImPvoHqwfXFaU",
    "lh_dest_instance": "LKMHXgSCmGTmVbZL",
    "lh_fileid": "taAjyAQRSWraghfP",
    "lh_filename": "rsjjtAjqpCcYjaOU",
    "lh_filepath": "IhYDbjTXhzqtUZeD",
    "lh_original_filename": "vWijvCFegHYDULbn",
    "lh_shared": "WCLXYCUEBjqOlWHt",
    "lh_shared_with": "SwUYQdzFHslSQoxr",
    "lh_version": 1,
    "local_sha256": "fd856057ed7703e9b53458c7dbb6a3dc4ce9b957f3b307d81f06bf09c9bd8de3",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "OLizsiNCpTCziLEC",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "iOS  9.6",
    "other_categories": [],
    "owner": "dte1953ce410-0778t@test.netskope.com",
    "policy": "policy_ga13",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "site": "X3host technologies",
    "src_country": "NL",
    "src_geoip_src": 2,
    "src_latitude": 52.3759,
    "src_location": "Amsterdam",
    "src_longitude": 4.8975,
    "src_region": "North Holland",
    "src_zipcode": "1012",
    "srcip": "31.186.239.204",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0494t@test.netskope.com",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "dte1953ce410-0494t@test.netskope.com",
    "userkey": "dte1953ce410-0494t@test.netskope.com"
}
Get Malsite Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/malsite
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "01f6ca78bec577883076a738",
    "access_method": "Client",
    "acked": "false",
    "action": "block",
    "alert": "yes",
    "alert_name": "bget.ru",
    "alert_type": "malsite",
    "app": "",
    "app_session_id": 4910069257574835437,
    "appcategory": "Security Risk - Compromised/malicious sites",
    "browser_session_id": 1141245448937753175,
    "category": "Security Risk - Compromised/malicious sites",
    "cci": 0,
    "ccl": "unknown",
    "connection_id": 0,
    "count": 1,
    "device": "Linux Device",
    "device_classification": "not configured",
    "dst_country": "RU",
    "dst_latitude": 59.9417,
    "dst_location": "St Petersburg",
    "dst_longitude": 30.3096,
    "dst_region": "St.-Petersburg",
    "dst_timezone": "Europe/Moscow",
    "dst_zipcode": "195213",
    "dstip": "5.101.158.143",
    "dstport": 443,
    "hostname": "ip-172-31-37-148",
    "incident_id": 7989528656047608655,
    "ja3": "07ff1e545ef8ab3fcf8a4dc9272221c2",
    "ja3s": "NotAvailable",
    "malicious": "yes",
    "malsite_category": [
        "Malicious Site"
    ],
    "malsite_country": "RU",
    "malsite_id": "ae7c3ade12353ae7165e9b2f",
    "malsite_ip_host": "5.101.158.143",
    "malsite_latitude": 59.9417,
    "malsite_longitude": 30.3096,
    "malsite_region": "St.-Petersburg",
    "managed_app": "no",
    "notify_template": "block_page.html",
    "organization_unit": "",
    "os": "Linux",
    "os_version": "Linux 22.04",
    "other_categories": [
        "Security Risk",
        "Security Risk - Compromised/malicious sites"
    ],
    "page": "bget.ru/",
    "page_site": "bget",
    "policy": "TestMalsite2",
    "policy_id": "F1AE7109B6FC54098C582D3B0F149521 2024-05-28 13:48:56.784091",
    "protocol": "HTTPS/1.1",
    "request_id": 2851228580036571136,
    "severity_level": "med",
    "severity_level_id": 1,
    "site": "bget",
    "src_country": "US",
    "src_latitude": 39.0469,
    "src_location": "Ashburn",
    "src_longitude": -77.4903,
    "src_region": "Virginia",
    "src_time": "Tue May 28 10:07:00 2024",
    "src_timezone": "America/New_York",
    "src_zipcode": "20149",
    "srcip": "18.209.94.135",
    "telemetry_app": "",
    "threat_match_field": "domain",
    "threat_match_value": "bget.ru",
    "threat_source_id": 1,
    "timestamp": 1716905279,
    "traffic_type": "Web",
    "transaction_id": 7989528656047608655,
    "type": "malsite",
    "ur_normalized": "keshavhazard@gmail.com",
    "url": "bget.ru/",
    "user": "keshavhazard@gmail.com",
    "useragent": "python-requests/2.25.1",
    "userip": "172.31.37.148",
    "record_type": "alert",
    "malsite_reputation": "",
    "object": "",
    "org": "",
    "fromlogs": "",
    "log_file_name": "",
    "req_cnt": 0,
    "browser_version": "",
    "numbytes": 0,
    "department": "",
    "division": "",
    "retro_scan_name": "",
    "sfwder": "",
    "browser": "",
    "custom_attr": {},
    "malsite_confidence": 0,
    "server_bytes": 0,
    "client_bytes": 0,
    "malsite_first_seen": 0,
    "co": "",
    "sAMAccountName": "",
    "src_geoip_src": 0,
    "gateway": "",
    "referer": "",
    "suppression_start_time": 0,
    "resp_cnt": 0,
    "conn_duration": 0,
    "serial": "",
    "malsite_hostility": "",
    "dsthost": "",
    "dst_geoip_src": 0,
    "universal_connector": "",
    "malsite_active": "",
    "from_user": "",
    "object_type": "",
    "suppression_end_time": 0,
    "malsite_last_seen": 0,
    "severity": "",
    "aggregated_user": "",
    "malsite_consecutive": "",
    "appsuite": ""
}
Get Policy Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/policy
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "3ceffe626afca6f5d46befb6",
    "access_method": "Client",
    "acked": "false",
    "action": "block",
    "alert": "yes",
    "alert_name": "testprivateapp with2nd opt",
    "alert_type": "policy",
    "app": "[ExtraHop-Demo]",
    "appcategory": "n/a",
    "category": "n/a",
    "cci": 0,
    "ccl": "unknown",
    "client_bytes": 0,
    "client_packets": 0,
    "count": 1,
    "device": "Windows",
    "dsthost": "netskope.atlassian.net",
    "dstip": "",
    "dstport": 443,
    "end_time": "2025-02-28T08:22:47+00:00",
    "hostname": "WIN11-50-12-151",
    "ip_protocol": "TCP",
    "network_session_id": "9452921695540616650",
    "num_sessions": 1,
    "numbytes": 0,
    "organization_unit": "",
    "os": "Windows",
    "os_version": "11.0.22621",
    "other_categories": [],
    "policy": "testprivateapp with2nd opt",
    "protocol": "Http",
    "protocol_port": "TCP:443",
    "publisher_cn": "",
    "publisher_name": "",
    "server_bytes": 0,
    "server_packets": 0,
    "session_duration": 0,
    "site": "netskope.atlassian.net",
    "srcip": "",
    "srcport": 30700,
    "start_time": "2025-02-28T08:22:32+00:00",
    "timestamp": 1740731072,
    "total_packets": 0,
    "traffic_type": "PrivateApp",
    "tunnel_id": "53125",
    "tunnel_type": "NPA",
    "tunnel_up_time": 0,
    "type": "network",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "user": "tanushree.kurup@crestdata.ai",
    "userip": "",
    "record_type": "alert",
    "suppression_key": "",
    "app_activity": "",
    "file_type": "",
    "url": "",
    "policy_id": "",
    "custom_connector": "",
    "quarantine_profile": "",
    "q_original_shared": "",
    "file_path": "",
    "profile_emails": [],
    "referer": "",
    "md5": "",
    "redirect_url": "",
    "page_site": "",
    "malware_name": "",
    "suppression_end_time": 0,
    "user_id": "",
    "distinguishedName": "",
    "severity": "",
    "src_timezone": "",
    "tss_mode": "",
    "managed_app": "",
    "tss_fail_reason": "",
    "src_geoip_src": 0,
    "owner": "",
    "aggregated_user": "",
    "group": "",
    "total_collaborator_count": 0,
    "userCountry": "",
    "browser": "",
    "to_user": "",
    "from_object": "",
    "ext_labels": [],
    "shared_with": "",
    "useragent": "",
    "sessionid": "",
    "network": "",
    "malicious": "",
    "quarantine_file_id": "",
    "appsuite": "",
    "remediation_profile": "",
    "universal_connector": "",
    "mime_type": "",
    "browser_version": "",
    "src_zipcode": "",
    "access_key_id": "",
    "src_latitude": 0.0,
    "malware_type": "",
    "dynamic_classification": "",
    "src_region": "",
    "q_original_version": "",
    "instance_id": "",
    "message_id": "",
    "sfwder": "",
    "q_admin": "",
    "q_app": "",
    "object_type": "",
    "log_file_name": "",
    "malware_severity": "",
    "retro_scan_name": "",
    "displayName": "",
    "justification_reason": "",
    "q_instance": "",
    "src_location": "",
    "gateway": "",
    "forward_to_proxy_xau": "",
    "justification_type": "",
    "smtp_to": [],
    "app_session_id": 0,
    "request_id": 0,
    "app_scopes": "",
    "parent_id": "",
    "file_category": "",
    "file_id": "",
    "dlp_profile": "",
    "nsdeviceuid": "",
    "risk_level": "",
    "encrypt_failure": "",
    "quarantine_file_name": "",
    "src_longitude": 0.0,
    "file_size": 0,
    "org": "",
    "user_tmp": "",
    "activity_status": "",
    "threat_match_value": "",
    "malsite_category": [],
    "dst_timezone": "",
    "all_policy_matches": [],
    "incident_id": 0,
    "orignal_file_path": "",
    "object_id": "",
    "act_user": "",
    "http_status": "",
    "dst_country": "",
    "from_user": "",
    "req_cnt": 0,
    "transaction_id": 0,
    "browser_session_id": 0,
    "sanctioned_instance": "",
    "from_storage": "",
    "tss-mode": "",
    "cc": "",
    "activity": "",
    "sAMAccountName": "",
    "scan_type": "",
    "serial": "",
    "src_time": "",
    "managementID": "",
    "object": "",
    "q_original_filepath": "",
    "custom_attr": {},
    "shared_domains": "",
    "q_original_filename": "",
    "notify_template": "",
    "connection_id": 0,
    "telemetry_app": "",
    "threat_source_id": 0,
    "user_confidence_index": 0,
    "TSS-scan": "",
    "internal_collaborator_count": 0,
    "last_name": "",
    "mail": "",
    "sAMAccountType": "",
    "memberOf": "",
    "smtp_status": "",
    "Title": "",
    "dst_location": "",
    "bcc": "",
    "dst_geoip_src": 0,
    "exposure": "",
    "activity_type": "",
    "dlp_fail_reason": "",
    "dst_zipcode": "",
    "message_size": 0,
    "suppression_start_time": 0,
    "trust_computer_checked": "",
    "device_classification": "",
    "instance": "",
    "to_storage": "",
    "dst_latitude": 0.0,
    "division": "",
    "object_count": 0,
    "to_object": "",
    "modified": 0,
    "sender": "",
    "dst_region": "",
    "page": "",
    "conn_duration": 0,
    "two_factor_auth": "",
    "dst_longitude": 0.0,
    "data_type": "",
    "quarantine_profile_id": "",
    "malware_id": "",
    "manager": "",
    "src_country": "",
    "event_type": "",
    "external_collaborator_count": 0,
    "resp_cnt": 0,
    "threat_match_field": "",
    "tss_scan_failed": "",
    "dlp_scan_failed": "",
    "sha256": ""
}
Get Quarantine Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/quarantine
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "63d6a681f0d64a6f41cc084c",
    "_insertion_epoch_timestamp": 1727659690,
    "access_method": "API Connector",
    "acked": "false",
    "action": "quarantine-sahil",
    "activity": "Login Successful",
    "alert": "yes",
    "alert_name": "quarantine-alert",
    "alert_type": "quarantine",
    "app": "Dropbox",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 81,
    "ccl": "high",
    "count": 1,
    "device": "Other",
    "dst_country": "US",
    "dst_geoip_src": 2,
    "dst_latitude": 33.1432,
    "dst_location": "San Marcos",
    "dst_longitude": -117.1666,
    "dst_region": "California",
    "dst_zipcode": "92069",
    "dstip": "98.176.143.16",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "\\/My Drive\\/Clickhouse\\/Tenant Migration across MPs",
    "file_size": 196869,
    "file_type": "application\\/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application\\/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "weclTNVzKoULFCYX",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local\\/Netskope\\/Active Users\\/US & International\\/Full Time",
    "os": "unknown",
    "other_categories": [],
    "owner": "foobar",
    "policy": "GDrive Customer metadata shared externally",
    "q_admin": "KgBNclCNvMfSfwAe",
    "q_app": "Box",
    "q_instance": "IXlwfxAfRQMyUbso",
    "q_original_filename": "huSgEkeGhFjPDLhS",
    "q_original_filepath": "oJmMLhuvhIyXlarC",
    "q_original_shared": "private",
    "q_original_version": "1",
    "q_shared_with": "PqtCjqtPLVOOFkWk",
    "quarantine_action_reason": "TuJbfomareEgmNNT",
    "quarantine_app": "Amazon S3",
    "quarantine_failure": "mDsCCrKldEQdhrEF",
    "quarantine_file_id": "jeCCFYBKuaBggvol",
    "quarantine_file_name": "GEXNzZEGpZFQAuUv",
    "quarantine_profile": "fQECcfyXhgGUOJSO",
    "quarantine_profile_id": "xfFlQTBQWxjnIsXZ",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "shared_with": "none",
    "site": "Dropbox",
    "src_country": "DE",
    "src_geoip_src": 2,
    "src_latitude": 50.1188,
    "src_location": "Frankfurt am Main",
    "src_longitude": 8.6843,
    "src_region": "Hesse",
    "src_zipcode": "60313",
    "srcip": "8.39.144.84",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "crest_sup_de_202112031049-0@crest.netskope.com",
    "url": "https:\\/\\/drive.google.com\\/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "crest_sup_de_202112031049-0@crest.netskope.com",
    "usergroup": [],
    "userkey": "crest_sup_de_202112031049-0@crest.netskope.com"
}
Get UBA Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/uba
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "b7dce8f570123bdd868a8315",
    "access_method": "UCI Impact API",
    "acked": "false",
    "action": "anomaly_detection",
    "activity": "ActivityForUciImpactAPI",
    "alert": "yes",
    "alert_id": "505464b05529c82e34d31970",
    "alert_name": "External alert from Netskope due to Risky User",
    "alert_type": "uba",
    "anomaly_type": "Fact",
    "app": "",
    "appcategory": "n/a",
    "category": "n/a",
    "cci": 0,
    "ccl": "unknown",
    "count": 1,
    "createdTime": "2025-02-24 08:15:55.461000",
    "device": "Other",
    "event_type": "uba_analytics",
    "instance_id": "",
    "organization_unit": "",
    "policy": "External alert received via REST API",
    "score": 1,
    "severity": "informational",
    "src_country": "IN",
    "src_geoip_src": 2,
    "src_latitude": 23.0276,
    "src_location": "Ahmedabad",
    "src_longitude": 72.5871,
    "src_region": "Gujarat",
    "src_zipcode": "380009",
    "srcip": "122.170.162.148",
    "timestamp": 1740384954,
    "type": "nspolicy",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "user": "tanushree.kurup@crestdata.ai",
    "userkey": "tanushree.kurup@crestdata.ai",
    "windowId": 1740355200000,
    "record_type": "alert",
    "last_device": "",
    "surhn": "",
    "policy_id": "",
    "uba_ap1": "",
    "evt_src_chnl": "",
    "all_policy_matches": [],
    "threshold": 0,
    "web_universal_connector": "",
    "user_category": "",
    "managementID": "",
    "division": "",
    "download_app": "",
    "user_id": "",
    "dst_longitude": 0.0,
    "audit_type": "",
    "object_count": 0,
    "policy_name": "",
    "activity_status": "",
    "group": "",
    "act_user": "",
    "referer": "",
    "connection_id": 0,
    "app_category": "",
    "bin_timestamp": 0,
    "hostname": "",
    "app_activity": "",
    "md5": "",
    "risk_level_id": 0,
    "suppression_end_time": 0,
    "protocol": "",
    "request_type": "",
    "request_id": 0,
    "app_session_id": 0,
    "User_SPACE_Id": "",
    "user_name": "",
    "last_timestamp": 0,
    "netskope_activity": "",
    "dst_geoip_src": 0,
    "tss_scan_failed": "",
    "loginurl": "",
    "threshold_time": 0,
    "risk_level": "",
    "managed_app": "",
    "browser_version": "",
    "file_category": "",
    "from_user_category": "",
    "page": "",
    "last_location": "",
    "url": "",
    "uba_ap2": "",
    "sanctioned_instance": "",
    "object_id": "",
    "dst_timezone": "",
    "custom_attr": {},
    "to_object": "",
    "dst_country": "",
    "traffic_type": "",
    "telemetry_app": "",
    "page_site": "",
    "file_size": 0,
    "scopes": [],
    "anomalyData": {},
    "os": "",
    "audit_category": "",
    "tss_fail_reason": "",
    "userip": "",
    "last_app": "",
    "incident_id": 0,
    "suppression_start_time": 0,
    "dst_zipcode": "",
    "dstip": "",
    "policy_actions": [],
    "browser": "",
    "src_time": "",
    "sAMAccountName": "",
    "two_factor_auth": "",
    "uba_inst2": "",
    "site": "",
    "displayName": "",
    "sha256": "",
    "object": "",
    "last_country": "",
    "to_user": "",
    "object_type": "",
    "manager": "",
    "last_region": "",
    "dst_region": "",
    "dst_latitude": 0.0,
    "shared_credential_user": "",
    "file_type": "",
    "tss_mode": "",
    "appsuite": "",
    "device_classification": "",
    "logintype": "",
    "AccountType": "",
    "os_version": "",
    "parent_id": "",
    "TSS-scan": "",
    "user_role": "",
    "dst_location": "",
    "to_user_category": "",
    "user_confidence_index": 0,
    "mail": "",
    "browser_session_id": 0,
    "src_timezone": "",
    "useragent": "",
    "employeeType": "",
    "from_user": "",
    "uba_inst1": "",
    "User_SPACE_Name": "",
    "userPrincipalName": "",
    "transaction_id": 0,
    "distinguishedName": "",
    "profile_id": ""
}
Get Watchlist Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/watchlist
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "ad921f96aaf7dc5b6fe5d628",
    "access_method": "API Connector",
    "acked": "true",
    "activity": "Upload",
    "alert": "yes",
    "alert_name": "watchlist fired",
    "alert_type": "watchlist",
    "app": "Amazon App Suite",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 89,
    "ccl": "high",
    "count": 1,
    "device": "Other",
    "dst_country": "IN",
    "dst_geoip_src": 2,
    "dst_latitude": 19.0748,
    "dst_location": "Mumbai",
    "dst_longitude": 72.8856,
    "dst_region": "Maharashtra",
    "dst_zipcode": "400072",
    "dstip": "182.75.130.70",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "/My Drive/Clickhouse/Tenant Migration across MPs",
    "file_size": 119268,
    "file_type": "application/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "local_sha256": "aa477dd147d603cd0bd65b6dfb09021654e212aa3200ceb03e3a1e1d0fb37fdb",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "uVwtiXcnOjCdpJHt",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "Windows 8.0",
    "owner": "dte1953ce410-0545t@test.netskope.com",
    "policy": "policy_ga26",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "site": "Amazon App Suite",
    "src_country": "DE",
    "src_geoip_src": 2,
    "src_latitude": 50.1188,
    "src_location": "Frankfurt am Main",
    "src_longitude": 8.6843,
    "src_region": "Hesse",
    "src_zipcode": "60313",
    "srcip": "8.39.144.84",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0191t@test.netskope.com",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "dte1953ce410-0191t@test.netskope.com",
    "userkey": "dte1953ce410-0191t@test.netskope.com",
    "dst_timezone": "",
    "two_factor_auth": "",
    "dlp_fail_reason": "",
    "title": "",
    "conn_duration": 0,
    "shared_domains": "",
    "user_id": "",
    "notify_template": "",
    "severity_id": 0,
    "TSS-scan": "",
    "universal_connector": "",
    "to_user_category": "",
    "web_url": "",
    "severity": "",
    "netskope_activity": "",
    "malware_severity": "",
    "dlp_is_unique_count": "",
    "sAMAccountName": "",
    "hostname": "",
    "sanctioned_instance": "",
    "object_count": 0,
    "dlp_rule": "",
    "protocol": "",
    "file_id": "",
    "audit_type": "",
    "internal_collaborator_count": 0,
    "dlp_scan_failed": "",
    "appsuite": "",
    "dlp_rule_severity": "",
    "telemetry_app": "",
    "to_user": "",
    "true_obj_category": "",
    "useragent": "",
    "shared_with": "",
    "justification_reason": "",
    "dlp_parent_id": 0,
    "referer": "",
    "src_timezone": "",
    "connection_id": 0,
    "app_session_id": 0,
    "from_user_category": "",
    "client_bytes": 0,
    "malware_name": "",
    "total_collaborator_count": 0,
    "policy_id": "",
    "workspace": "",
    "data_type": "",
    "dlp_profile": "",
    "act_user": "",
    "malware_profile": "",
    "file_name": "",
    "fromlogs": "",
    "ml_detection": "",
    "app_activity": "",
    "malware_id": "",
    "dstport": 0,
    "transaction_id": 0,
    "detection_engine": "",
    "to_storage": "",
    "parent_id": "",
    "managed_app": "",
    "external_collaborator_count": 0,
    "nsdeviceuid": "",
    "tss_fail_reason": "",
    "managementID": "",
    "workspace_id": "",
    "true_obj_type": "",
    "justification_type": "",
    "aggregated_user": "",
    "network": "",
    "org": "",
    "page_site": "",
    "userPrincipalName": "",
    "tss_mode": "",
    "suppression_end_time": 0,
    "true_type_id": 0,
    "server_bytes": 0,
    "manager": "",
    "suppression_start_time": 0,
    "file_category": "",
    "app_name": "",
    "audit_category": "",
    "incident_id": 0,
    "serial": "",
    "resp_cnt": 0,
    "browser_version": "",
    "all_policy_matches": [],
    "enterprise": "",
    "numbytes": 0,
    "device_classification": "",
    "from_object": "",
    "dlp_rule_count": 0,
    "dsthost": "",
    "src_time": "",
    "user_category": "",
    "browser_session_id": 0,
    "sfwder": "",
    "scanner_result": "",
    "dlp_file": "",
    "os_version": "",
    "to_object": "",
    "malware_type": "",
    "log_file_name": "",
    "web_universal_connector": "",
    "enterprise_id": "",
    "dlp_incident_id": 0,
    "from_user": "",
    "userip": "",
    "page": "",
    "req_cnt": 0,
    "from_storage": "",
    "tss_scan_failed": "",
    "local_md5": ""
}
Get Device Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/device
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "983681ec8804b23e77c2c292",
    "access_method": "Endpoint",
    "action": "block",
    "activity": "Insert",
    "alert": "yes",
    "alert_name": "TestBlock",
    "alert_type": "Device",
    "computer_name": "N49J4M9T3C",
    "count": 1,
    "device_classification": "not configured",
    "organization_unit": "",
    "os": "macOS",
    "os_details": "Mac OS X Sonoma 14.3.1 arm64",
    "policy": "TestBlock",
    "policy_action": "block",
    "policy_name_enforced": "TestBlock",
    "timestamp": 1720005433,
    "traffic_type": "",
    "type": "endpoint",
    "ur_normalized": "kmaheshwari@netskope.com",
    "usb_device_id": "USB\\VID_03f0&PID_1985&REV_0110",
    "usb_device_name": "USB Flash Drive",
    "usb_device_sn": "070D2C206FCFA597",
    "usb_device_type": "usb mass storage",
    "usb_product_id": "6533",
    "usb_vendor_id": "HP",
    "user": "kmaheshwari@netskope.com",
    "userkey": "kmaheshwari@netskope.com",
    "record_type": "alert",
    "connection_type": "",
    "driver": "",
    "os_user_name": "",
    "usb_is_encrypted": false,
    "location": "",
    "custom_attr": {}
}
Get Content Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/content
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "3f14cdb17c8385f9a6acfab4",
    "access_method": "Endpoint",
    "action": "block",
    "activity": "Create",
    "alert": "yes",
    "alert_name": "mmm1",
    "alert_type": "Content",
    "app": "DesktopServicesHelper",
    "computer_name": "N49J4M9T3C",
    "count": 1,
    "destination_file_directory": "/Volumes/KALI LINUX",
    "destination_file_name": "urls.txt",
    "destination_file_path": "/Volumes/KALI LINUX/urls.txt",
    "device_classification": "not configured",
    "dlp_incident_id": 8329186087212438192,
    "dlp_profile": "DLPTest",
    "file_size": 52483,
    "file_type": "Plain Text file",
    "incident_id": 8329186087212438192,
    "md5": "da3faaff0b406f6aa4685aee47ece41c",
    "organization_unit": "",
    "os": "macOS",
    "os_details": "Mac OS X Sonoma 14.3.1 arm64",
    "os_user_name": "kmaheshwari",
    "pid": "0",
    "policy": "mmm1",
    "policy_action": "block",
    "policy_name_enforced": "mmm1",
    "process_name": "DesktopServicesHelper",
    "process_path": "/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/Resources",
    "sha256": "23a129d56da1579a68862808a22b7b3e1d64682cc7d4c725fdc8a8c7980310b6",
    "site": "DesktopServicesHelper",
    "timestamp": 1719993896,
    "traffic_type": "",
    "type": "endpoint",
    "ur_normalized": "kmaheshwari@netskope.com",
    "usb_device_type": "usb mass storage",
    "user": "kmaheshwari@netskope.com",
    "userkey": "kmaheshwari@netskope.com",
    "record_type": "alert",
    "custom_attr": {},
    "process_cert_subject": "",
    "device": ""
}
Get Page Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/page
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "56758f371f4e65c4049d423e",
    "access_method": "Client",
    "app": "Microsoft Accounts",
    "appcategory": "Application Suite",
    "bypass_reason": "SSL Do Not Decrypt Bypass Policy Matched",
    "bypass_traffic": "yes",
    "category": "Application Suite",
    "cci": 84,
    "ccl": "high",
    "connection_id": 0,
    "count": 1,
    "domain": "ecs.office.com",
    "dst_country": "US",
    "dst_latitude": 47.6722,
    "dst_location": "Redmond",
    "dst_longitude": -122.1257,
    "dst_region": "Washington",
    "dst_timezone": "America/Los_Angeles",
    "dst_zipcode": "98073",
    "dstip": "52.123.128.14",
    "dstport": 443,
    "netskope_pop": "IN-BOM2",
    "organization_unit": "",
    "os_version": "Windows NT 11.0",
    "other_categories": [
        "Technology",
        "Application Suite"
    ],
    "page": "ecs.office.com",
    "policy": "Default Microsoft appsuite SSL do not decrypt rule",
    "request_id": 3051109095898995457,
    "site": "Microsoft Office 365 Suite",
    "src_country": "IN",
    "src_latitude": 21.7003,
    "src_location": "Bharūch",
    "src_longitude": 72.9782,
    "src_region": "Gujarat",
    "src_time": "Fri Feb 28 14:26:08 2025",
    "src_timezone": "Asia/Kolkata",
    "src_zipcode": "392012",
    "srcip": "103.108.207.58",
    "ssl_decrypt_policy": "yes",
    "timestamp": 1740732961,
    "traffic_type": "CloudApp",
    "transaction_id": 0,
    "type": "connection",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "url": "ecs.office.com",
    "user": "tanushree.kurup@crestdata.ai",
    "user_generated": "yes",
    "userip": "10.50.12.151",
    "userkey": "tanushree.kurup@crestdata.ai",
    "record_type": "page",
    "useragent": "",
    "CononicalName": "",
    "forward_to_proxy_profile": "",
    "http_transaction_count": 0,
    "resp_content_type": "",
    "org": "",
    "browser_version": "",
    "conn_starttime": 0,
    "os": "",
    "network": "",
    "device": "",
    "req_cnt": 0,
    "src_geoip_src": 0,
    "conn_endtime": 0,
    "dst_geoip_src": 0,
    "hostname": "",
    "client_bytes": 0,
    "dsthost": "",
    "userPrincipalName": "",
    "numbytes": 0,
    "fromlogs": "",
    "rbi_template_name": "",
    "resp_cnt": 0,
    "browser_session_id": 0,
    "resp_content_len": 0,
    "server_bytes": 0,
    "forward_to_proxy_xau": "",
    "conn_duration": 0,
    "serial": "",
    "sAMAccountName": "",
    "log_file_name": "",
    "rbi_template_id": "",
    "dynamic_classification": "",
    "browser": "",
    "severity": "",
    "suppression_end_time": 0,
    "custom_attr": {},
    "action": "",
    "suppression_start_time": 0,
    "sessionid": "",
    "protocol": "",
    "app_session_id": 0
}
Get Application Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/application
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "5af424a2871523b6e13f853f",
    "access_method": "Client",
    "activity": "Download",
    "alert": "no",
    "app": "ContentSquare",
    "app_session_id": 8320876311700568950,
    "appcategory": "Web Analytics",
    "browser": "Edge",
    "browser_session_id": 5471226135867547944,
    "browser_version": "133.0.0.0",
    "category": "Web Analytics",
    "cci": 60,
    "ccl": "medium",
    "connection_id": 0,
    "count": 1,
    "device": "Windows Device",
    "device_classification": "not configured",
    "dst_country": "IE",
    "dst_latitude": 53.3382,
    "dst_location": "Dublin",
    "dst_longitude": -6.2591,
    "dst_region": "Leinster",
    "dst_timezone": "Europe/Dublin",
    "dst_zipcode": "D02",
    "dstip": "52.48.68.180",
    "dstport": 443,
    "hostname": "WIN11-50-12-151",
    "ja3": "261219d3f4c7b45e9e6014a0084dc181",
    "ja3s": "f4febc55ea12b31ae17cfb7e614afda8",
    "managed_app": "no",
    "netskope_pop": "IN-BOM2",
    "object": "pageview",
    "object_type": "File",
    "organization_unit": "",
    "os": "Windows 11",
    "os_version": "Windows NT 11.0",
    "other_categories": [
        "Content Server",
        "Web Analytics"
    ],
    "page": "c.contentsquare.net/pageview",
    "page_site": "contentsquare",
    "policy_id": "8467252215149297331 2025-02-19 10:04:24.766887",
    "protocol": "HTTPS/1.1",
    "request_id": 3045298505167235584,
    "severity": "unknown",
    "site": "ContentSquare",
    "src_country": "IN",
    "src_latitude": 23.0276,
    "src_location": "Ahmedabad",
    "src_longitude": 72.5871,
    "src_region": "Gujarat",
    "src_time": "Thu Feb 20 14:00:08 2025",
    "src_timezone": "Asia/Kolkata",
    "src_zipcode": "380006",
    "srcip": "182.69.215.65",
    "telemetry_app": "",
    "timestamp": 1740040217,
    "traffic_type": "CloudApp",
    "transaction_id": 1737423402988911503,
    "type": "nspolicy",
    "universal_connector": "yes",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "url": "c.contentsquare.net/pageview",
    "user": "tanushree.kurup@crestdata.ai",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "userip": "10.50.12.151",
    "userkey": "tanushree.kurup@crestdata.ai",
    "record_type": "application",
    "suppression_key": "",
    "app_activity": "",
    "file_type": "",
    "dlp_incident_id": 0,
    "custom_connector": "",
    "file_path": "",
    "referer": "",
    "md5": "",
    "suppression_end_time": 0,
    "user_id": "",
    "tss_mode": "",
    "channel_id": "",
    "dlp_rule_count": 0,
    "web_universal_connector": "",
    "tss_fail_reason": "",
    "src_geoip_src": 0,
    "owner": "",
    "alert_type": "",
    "total_collaborator_count": 0,
    "to_user": "",
    "ext_labels": [],
    "shared_with": "",
    "sessionid": "",
    "client_bytes": 0,
    "appsuite": "",
    "mime_type": "",
    "dlp_rule_severity": "",
    "workspace_id": "",
    "instance_id": "",
    "logintype": "",
    "policy": "",
    "log_file_name": "",
    "retro_scan_name": "",
    "justification_reason": "",
    "user_category": "",
    "netskope_activity": "",
    "justification_type": "",
    "smtp_to": [],
    "parent_id": "",
    "nsdeviceuid": "",
    "dlp_profile": "",
    "file_lang": "",
    "file_size": 0,
    "userPrincipalName": "",
    "org": "",
    "audit_type": "",
    "title": "",
    "orignal_file_path": "",
    "object_id": "",
    "dsthost": "",
    "from_user": "",
    "req_cnt": 0,
    "sanctioned_instance": "",
    "dlp_rule": "",
    "loginurl": "",
    "scan_type": "",
    "sAMAccountName": "",
    "serial": "",
    "managementID": "",
    "custom_attr": {},
    "from_user_category": "",
    "notify_template": "",
    "dlp_parent_id": 0,
    "user_confidence_index": 0,
    "internal_collaborator_count": 0,
    "dlp_unique_count": 0,
    "dlp_mail_parent_id": "",
    "true_obj_category": "",
    "dst_geoip_src": 0,
    "exposure": "",
    "dlp_is_unique_count": "",
    "numbytes": 0,
    "dlp_fail_reason": "",
    "suppression_start_time": 0,
    "audit_category": "",
    "true_obj_type": "",
    "data_center": "",
    "instance": "",
    "server_bytes": 0,
    "modified": 0,
    "action": "",
    "conn_duration": 0,
    "data_type": "",
    "fromlogs": "",
    "resp_cnt": 0,
    "workspace": "",
    "dlp_file": "",
    "CononicalName": "",
    "tss_scan_failed": "",
    "dlp_scan_failed": "",
    "sha256": ""
}
Get Audit Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/audit
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "audit_log_event": "Rest API V2 Call",
    "severity_level": 2,
    "supporting_data": {
        "data_type": "policy",
        "data_values": [
            "200",
            "POST",
            "/api/v2/policy/urllist/deploy",
            "trid=22f0b0dfb2b8d75d27aa528ff6040e5d.1740723551"
        ]
    },
    "timestamp": 1740723551,
    "type": "admin_audit_logs",
    "user": "DO-NOT-DELETE",
    "organization_unit": "",
    "ur_normalized": "do-not-delete",
    "count": 1,
    "_id": "074fdfdb6974f8960bfaede9",
    "record_type": "audit",
    "sAMAccountName": "",
    "details": [],
    "ccl": "",
    "userPrincipalName": ""
}
Get Infrastructure Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/infrastructure
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "timestamp": 1727659690,
    "severity": "high",
    "alarm_name": "No_events_from_device",
    "device_name": "panw-dpop-1",
    "metric_value": 43831789,
    "alarm_description": "Events from 仕事 device not received in the last 24 hours",
    "serial": "FF00A7BFFA4E6165E",
    "_insertion_epoch_timestamp": 1727659690,
    "supporting_data": "",
    "_id": "613ee55ec9d868fc47654a73"
}
Get Network Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/network
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "f67629951b42c8e556062456",
    "access_method": "Client",
    "action": "block",
    "app": "Domain Name Service (DNS)",
    "appcategory": "Shopping",
    "category": "Shopping",
    "cci": 0,
    "ccl": "unknown",
    "client_bytes": 0,
    "client_packets": 0,
    "count": 1,
    "device": "Other",
    "domain": "",
    "dst_geoip_src": 2,
    "dsthost": "",
    "dstip": "10.50.1.16",
    "dstport": 5353,
    "end_time": "2025-02-28T09:34:08+00:00",
    "flow_status": "close",
    "ip_protocol": "UDP",
    "numbytes": 0,
    "organization_unit": "",
    "os": "Windows NT 11.0",
    "policy": "default",
    "publisher_name": "",
    "server_bytes": 0,
    "server_packets": 0,
    "session_duration": 0,
    "site": "dns",
    "src_country": "IN",
    "src_geoip_src": 2,
    "src_latitude": 21.7003,
    "src_location": "Bharūch",
    "src_longitude": 72.9782,
    "src_region": "Gujarat",
    "src_zipcode": "392011",
    "srcip": "103.108.207.58",
    "srcport": 5353,
    "start_time": "2025-02-28T09:34:08+00:00",
    "timestamp": 1740735248,
    "total_packets": 0,
    "traffic_type": "non-web",
    "tunnel_id": "1138033360427841",
    "type": "network",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "user": "tanushree.kurup@crestdata.ai",
    "userip": "10.50.12.151",
    "userkey": "tanushree.kurup@crestdata.ai",
    "record_type": "network",
    "qdomain": "",
    "dst_region": "",
    "userPrincipalName": "",
    "dst_country": "",
    "tunnel_type": "",
    "dst_zipcode": "",
    "num_sessions": 0,
    "domain_ip": "",
    "dst_longitude": 0.0,
    "protocol": "",
    "tunnel_up_time": 0,
    "protocol_port": "",
    "network_session_id": "",
    "os_version": "",
    "dst_latitude": 0.0,
    "sAMAccountName": "",
    "hostname": "",
    "custom_attr": {},
    "publisher_cn": "",
    "dst_location": ""
}
Get Incident Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/incident
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
"_id": "6d462e0db470c7247e75322fd380031271d1be18db9d707ef6f3affc792f11b1",
"access_method": "Endpoint Protection",
"acting_user": "kmaheshwari@netskope.com",
"activity": "Create",
"app": "DesktopServicesHelper",
"assignee": "None",
"dlp_incident_id": 7268524954762607217,
"dlp_match_info": [
{
"dlp_action": "block",
"dlp_forensic_id": 1711868037568704387,
"dlp_policy": "mmm1",
"dlp_profile_name": "DLPTest",
"dlp_rules": []
}
],
"file_path": "/Volumes/KALI LINUX/urls.txt",
"file_size": 52483,
"file_type": "Plain Text file",
"md5": "da3faaff0b406f6aa4685aee47ece41c",
"object": "urls.txt",
"object_id": "hash_kmaheshwari@netskope.com_da3faaff0b406f6aa4685aee47ece41c_7b4a2e1f194ccb4e8eca958a472bfe3c3741d7a6",
"severity": "Low",
"status": "new",
"timestamp": 1719993903,
"title": "urls.txt",
"user": "kmaheshwari@netskope.com",
"record_type": "incident",
"instance": "",
"src_location": "",
"app_session_id": 0,
"zip_file_id": "",
"connection_id": 0,
"destination_site": "",
"to_user": "",
"latest_incident_id": 0,
"from_user": "",
"site": "",
"dst_location": "",
"inline_dlp_match_info": [],
"destination_instance_id": "",
"instance_id": "",
"channel": "",
"original_file_snapshot_id": "",
"bcc": "",
"referer": "",
"dlp_file": "",
"destination_app": "",
"true_obj_type": "",
"file_lang": "",
"url": "",
"true_obj_category": "",
"cc": "",
"owner_pdl": "",
"classification": "",
"object_type": "",
"ext_labels": [],
"exposure": "",
"dlp_parent_id": 0,
"owner": "",
"user_id": ""
}
Get Incident Forensics
API Endpoint:
https://
<tenant-url>
/api/v2/incidents/dlpincidents/{id}/forensics
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Request Parameters
Key
Value
dlp_incident_id in path param
dlp_incident_id
{
"status": "success",
"data": {
"meta": "{\"metadata_content\":\"filename: sensitive_data_onedrive_share.txt file_md5: 0bcafac7ce40ad3ebad1664307a046f1 file_type: text/plain file_lang: ENGLISH object_id: {\\\"drive_id\\\": \\\"b!PM0toX-2uEqSwuqUx0SzyDAe0n7GMw1Eok5wsoIE5ALI55tDhn-rSJB-vB4UWs5e\\\", \\\"driveitem_id\\\": \\\"014GLSS7Z2KV57XD3LXNFLWFO3HXHVREJB\\\", \\\"site_collection_id\\\": \\\"a12dcd3c-b67f-4ab8-92c2-ea94c744b3c8\\\"} ns_text_classifier: others \",\"dlp_match_info\":[{\"dlp_profile_name\":\"DLP-PCI\",\"dlp_rules\":[{\"dlp_rule_name\":\"Bank-CC\",\"dlp_rule_severity\":\"Low\",\"dlp_incident_rule_count\":3,\"dlp_data_identifiers\":[[{\"start_offset\":41,\"score\":1,\"end_offset\":56,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"Number\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\"\\n\\n\"},{\"start_offset\":59,\"score\":1,\"end_offset\":73,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"match\":\"378282XXXXX0005\",\"suffix\":\"\\n\\n\\n\\nAmerican\"}],[{\"start_offset\":78,\"score\":1,\"end_offset\":93,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"378282XXXXX0005\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\"\\n\\n\"},{\"start_offset\":96,\"score\":1,\"end_offset\":110,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"match\":\"371449XXXXX8431\",\"suffix\":\"\\n\\n\\n\\nAmerican\"}],[{\"start_offset\":115,\"score\":1,\"end_offset\":130,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"371449XXXXX8431\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\" Corporate\"},{\"start_offset\":143,\"score\":1,\"end_offset\":157,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"prefix\":\"\\n\\n\",\"match\":\"378734XXXXX1000\",\"suffix\":\"\\n\\n\\n\\nAustralian\"}]]}],\"dlp_action\":\"quarantine\",\"action_threshold_met\":true,\"dlp_policy\":\"CDS Data Protection Policy\",\"dlp_scan_type\":\"Ongoing\",\"dlp_policy_hash\":\"policy hash\"},{\"dlp_profile_name\":\"US Financial Data\",\"dlp_rules\":[{\"dlp_rule_name\":\"US-Bank-CC\",\"dlp_rule_severity\":\"Low\",\"dlp_incident_rule_count\":2,\"dlp_data_identifiers\":[[{\"start_offset\":19,\"score\":1,\"end_offset\":29,\"entity_name\":\"numbers/payment_card_number_terms/eng\",\"type\":\"content\",\"prefix\":\"Type\\n\\n\",\"match\":\"Credit Card\",\"suffix\":\" Number\"},{\"start_offset\":41,\"score\":1,\"end_offset\":56,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\"\\n\\n\"},{\"start_offset\":59,\"score\":1,\"end_offset\":73,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"match\":\"378282XXXXX0005\",\"suffix\":\"\\n\\n\\n\\nAmerican\"}],[{\"start_offset\":115,\"score\":1,\"end_offset\":130,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"3714XXXXXXXX31\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\" Corporate\"},{\"start_offset\":143,\"score\":1,\"end_offset\":157,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"prefix\":\"\\n\\n\",\"match\":\"378734XXXXX1000\",\"suffix\":\"\\n\\n\\n\\nAustralian\"},{\"start_offset\":203,\"score\":1,\"end_offset\":213,\"entity_name\":\"numbers/payment_card_number_terms/eng\",\"type\":\"content\",\"prefix\":\"...5610591081018250\\n\\n\\n\\n\",\"match\":\"Diners Club\",\"suffix\":\"\\n\\n30569309025904\"}]]}],\"dlp_action\":\"quarantine\",\"action_threshold_met\":true,\"dlp_policy\":\"CDS Data Protection Policy\",\"dlp_scan_type\":\"Ongoing\",\"dlp_policy_hash\":\"policy hash\"}]}",
"content": " Credit Card Type\n\nCredit Card Number\n\n\n\nAmerican Express\n\n37XXXXXXXXX0005\n\n\n\nAmerican Express\n\n37XXXXXXXXX8431\n\n\n\nAmerican Express Corporate\n\n37XXXXXXXXX1000\n\n\n\nAustralian BankCard\n\n5610XXXXXXXX50\n\n\n\nDiners Club\n\n30569XXXXXXXX5904\n\n\n\nDiners Club\n\n3852XXXXXXXX37\n\n\n\nDiscover\n\n60111XXXXXXXX117\n\n\n\nDiscover\n\n6011XXXXXXXX424\n\n\n\nJCB\n\n35301XXXXXXXX00\n\n\n\nJCB\n\n356XXXXXXXX05\n\n\n\nMasterCard\n\n555XXXXXXXX444\n\n\n\nMasterCard\n\n5105XXXXXXXX00\n\n\n\nVisa\n\n41XXXXXXXX111\n\n\n\nVisa\n\n401XXXXXXXX1881\n\n\n\nVisa\n\n422XXXXXXXX222"
}
}
Get Endpoint Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/endpoint
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "dffd23ac520f696e1c4bd020",
    "access_method": "Endpoint",
    "activity_type": "Process Start",
    "alert": "no",
    "alert_generated": false,
    "computer_name": "win11-50-1-92",
    "device_type": "Bluetooth File Transfer",
    "os": "Windows",
    "os_details": "Microsoft Windows 11 Pro 10.0.22621 64-bit",
    "policy_action": "allow",
    "process_name": "python.exe",
    "process_path": "\\??\\C:\\Program Files\\Python312\\python.exe",
    "sub_type": "SUBTYPE_DEVICE_CONTROL",
    "timestamp": 1725847324,
    "type": "endpoint",
    "user": "shubham.singhal@crestdata.ai",
    "record_type": "epdlp",
    "executable_hash": "",
    "location": "",
    "device_sn": "",
    "app": "",
    "destination_file_name": "",
    "printer_identifier": "",
    "file_type": "",
    "dlp_profile_name": "",
    "dlp_profile": "",
    "event_recovered": false,
    "destination_file_path": "",
    "dlp_incident_id": 0,
    "device_name": "",
    "source_file_directory": "",
    "alert_type": "",
    "process_cert_subject": "",
    "policy_name": "",
    "source_file_name": "",
    "incident_id": 0,
    "action": "",
    "policy_name_enforced": "",
    "policy_version": "",
    "executable_signed": false,
    "file_size": 0,
    "justification": "",
    "product_id": "",
    "vendor_id": "",
    "device_id": "",
    "destination_file_directory": "",
    "dlp_rule": "",
    "device": "",
    "alert_name": "",
    "pid": "",
    "port": "",
    "connection_type": "",
    "sha256": "",
    "policy_action_enforced": "",
    "activity": "",
    "driver": "",
    "unc_path": "",
    "file_origin": "",
    "os_user_name": "",
    "md5": ""
}
Create a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/netskope_ce_cs_iterator?
Method:
POST
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Request Parameters
Key
Value
eventtype
clientstatus
Sample API Response – if created successfully [202]
{"message":"Creation of the iterator, netskope_ce_cs_<unique_id_added> is in progress. Please use the iterator status API to check the status of the iterator. Please note that the iterator name has changed by appending an identifier to ensure uniqueness."
}
Sample API Response – if iterator cannot be created as already exists [400]
{"message":"Only one iterator is allowed per event type. Please use the existing iterator,<iterator_name>, or delete the existing iterator."
}
Check the Status of a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/
<iterator_name>
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Sample API Response
{
"status": "Ready"
}
Fetch Data from a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/
<iterator_name>
/events
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Request Parameters
Key
Value
operation
next
Sample API Response
_id,as,asn,city,client_install_time,client_version,count,continent,country,device_hash,device_id,enriched,guid,heart_beat,host_info.client_version,host_info.device_make,host_info.device_model,host_info.hostname,host_info.last_update_timestamp,host_info.mac_addresses,host_info.managementID,host_info.nsdeviceuid,host_info.old_nsdeviceuid,host_info.os,host_info.os_version,host_info.serial_number,host_info.steering_config,isp,last_connected_from_private_ip,last_connected_from_public_ip,last_event_timestamp,last_seen_device_event.actor,last_seen_device_event.event,last_seen_device_event.event_details,last_seen_device_event.npa_status,last_seen_device_event.service_name,last_seen_device_event.status,last_seen_device_event.status_v2,last_seen_device_event.timestamp,latitude,longitude,organization,postal_code,region,timestamp,user_info.device_classification_status,user_info.orgkey,user_info.userkey,user_info.username,zipcode,record_type
a7b8a3dd4aa3bebfac869f21,,,,0,123.0.0.2272,1,,,84a3c71061af4152f4e961f9,0AGE55ntv6Lg06dd2F30_092BDAE2-138E-38A4-1BC3-6BC72C4663E8,false,a9981877-c2be-4d8f-bf31-27410d8269d8,false,,"VMware, Inc.","VMware7,1",Win11-50-1-105,1740377213,00:50:56:81:A7:00,,092BDAE2-138E-38A4-1BC3-6BC72C4663E8,AFADEEE3-C9F6-3C54-E215-46EE64F4358C,0,11.0.22621,VMware-42 01 fa 68 fb 6b 7c 57-20 3c 42 df d2 c7 02 32,Default tenant config,,0.0.0.0,,1741034210,0,17,,8,Internet Security,0,0,1741034210,0,0,,,,0,0,lDFAMb4aR2ohwCHthoV,0AGE55ntv6Lg06dd2F30,nilay.modi@crestdata.ai,"396321",clientstatus
1c07aa9d8ad899d02b7c083b,,,,0,123.0.0.2272,1,,,84a3c71061af4152f4e961f9,0AGE55ntv6Lg06dd2F30_092BDAE2-138E-38A4-1BC3-6BC72C4663E8,false,a9981877-c2be-4d8f-bf31-27410d8269d8,false,,"VMware, Inc.","VMware7,1",Win11-50-1-105,1740377213,00:50:56:81:A7:00,,092BDAE2-138E-38A4-1BC3-6BC72C4663E8,AFADEEE3-C9F6-3C54-E215-46EE64F4358C,0,11.0.22621,VMware-42 01 fa 68 fb 6b 7c 57-20 3c 42 df d2 c7 02 32,Default tenant config,,0.0.0.0,,1741034205,0,7,Tunnel Down Due to SSL Error,8,Internet Security,1,0,1741034205,0,0,,,,0,0,lDFAMb4aR2ohwCHthoV,0AGE55ntv6Lg06dd2F30,nilay.modi@crestdata.ai,"396321",clientstatus
Sample API Response Headers
Delete a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/netskope_ce_cs_iterator_28b7611b-da34-4836-8bdb-89caa3320b6e
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Sample API Response
{
  "message": "Successfully deleted the iterator, netskope_ce_cs_iterator_28b7611b-da34-4836-8bdb-89caa3320b6e."
}
Performance Matrix
This performance reading is conducted on a Large Stack CE with these VM specifications.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to SIEM
~200k EPM
This figure represents the average performance across all alert and event types; however, the retrieval rate for incidents may fall below the average, with an estimated rate of approximately 1,500 incident events per minute.
User Agent
netskope-ce-
6.1.0
Workflow
Generate a v2 token for your Netskope tenant.
Configure the Log Shipper Plugin.
Configure a Business Rule.
Configure Log Delivery.
Validate the plugin.
Watch a Video
Click play to watch a video.
Generate a v2 token for your Netskope Tenant
In your Netskope tenant, go to
Settings > Tools > REST API v2
.
Click
New Token
.
Enter a Tenant Name.
Enter an Expire time. Select from Day(s), Hour(s), Week(s), Year(s).
Click
Add Endpoint
, and select the desired endpoints listed above in API Details, and enable the Read privilege. For more details, refer to the
Permissions
section and
REST API Scopes
.
Click
Save
.
Copy the token. It will be required when configuring the Netskope Tenant plugin in Cloud Exchange. Go here to configure the Netskope Tenant plugin.
Configure the Log Shipper Plugin
In Cloud Exchange, go to
Settings > General
and make sure the Log Shipper module is enabled. To enable this module.
Netskope tenant plugin
must be already configured.
Go to
Settings
>
Plugin Store
.
Search for and select the
Netskope Log Shipper
plugin.
Enter a configuration name and select a configured Netskope tenant from the dropdown.
Click
Next
and enter the Configuration Parameters:
Alert Types:
Types of alerts to fetch
Initial Range for Alerts (in days):
Number of days to pull the data for the initial run.
Event Types:
Types of events to fetch.
Pull DLP Incident Forensics:
Forensics fields for DLP Incidents will be fetched.
Note
By default
Forensics Originalfile Url (forensics_originalfile_url)
and
Forensics Subfile Url (forensics_subfile_url)
fields will be included irrespective of whether
Pull DLP Incident Forensics
is YES or NO.
If either the Netskope Ticket Orchestrator plugin or the Netskope Log Shipper plugin has the “Pull DLP Incident Forensics” field set to Yes, both plugins will automatically retrieve forensic fields for incident events.
Keeping the
Pull DLP Incident Forensics
field as
Yes
might impact the performance of the Netskope log shipper plugin as it will make additional API calls which will impact the performance of the plugin.
Any change in the value of the “Pull DLP Incident Forensics” field will not be respected once the plugin is configured, unless you restart the core or delete the Tenant plugin and CLS Netskope Log Shipper plugin and re-configure both the plugins.
Initial Range for Events (in hours):
Number of hours to pull the events data for the initial run.
If the plugin is directly upgraded to the latest version from the older version, you will have to edit the plugin and select the Client Status event type to pull it.
Click
Save
.
Configure a Business Rule for Log Shipper
Go to
Log Shipper > Business Rule
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, then click
Create New Rule
and configure a new business rule by adding the rule name and selecting filters, like those shown here.
Click
Save
.
Configure
Log Delivery
In order to add Log Delivery, a third-party Log Shipper plugin, like
Syslog
, has to be configured before proceeding. You need both a source and destination plugin (configurations) to create the Log Delivery.
Go to
Log Shipper > Log Delivery
.
Select the Source plugin (Netskope Log Shipper), Destination plugin (Syslog), and select a business rule.
Click
Save
.
After the Log Delivery is added, the data will start getting pulled from the Netskope tenant, transformed, and ingested into the Syslog plugin.
Validate the Log Shipper Plugin
Validating Events and Alerts are present in Tenant
To validate Events/Alerts in the Netskope tenant.
In your Netskope tenant, go to
Skope IT
.
For Alerts, go to
Alerts > Filters
and select an option from the
Last x Days
dropdown in the top-right corner.
For Events, go to
Skope IT
and select
Application Events
,
Page Event
, or
Network Events
.
For Audit Events, go to
Settings > Administrator > Audit Log
.
Note
For Client Status events validation on Netskope Tenant currently, there is no way to check the events in any of the pages, but you can refer to the API Details to verify the events.
Validate the Pull
To validate the pulling of Events/Alerts from the Netskope tenant, in Cloud Exchange, go to
Logging
and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events, Alerts with the filter
“message contains ingested”
. The ingested logs will be filtered.
Troubleshooting the Log Shipper Plugin
Receiving Error while Configuring the Log Shipper Plugin
Getting the error:
The Netskope tenant API V2 token does not have necessary permissions configured. Refer to the list of endpoints for which the token is missing permission. **
Cause:
The provided V2 token does not have the minimum required permissions to configure the tenant plugin in Cloud Exchange.
What to do:
Go to
Logging
and look for warning log similar to the following pattern:
TENANT Netskope Tenant (Required) [Netskope Tenant]: For Netskope Tenant, received 403 error for following endpoint(s)
Expand the log and get the list of endpoints for which permissions are missing.
Now update the v2 token permissions and add the permission for the above endpoint list from Netskope Dashboard.
Receiving an Error while Configuring Multiple Plugins
Getting the error:
Error: Value error, Error while creating iterator with name netskope_ce_cs_iterator_**. Cannot create Client Status Iterator. One iterator already exists for the Client Status event for your tenant. Delete the existing iterator to continue.
Cause:
Due to API Limitations of Client Status iterator, creation of more than one iterator is not possible.
What to do:
You can delete the already existing iterator using API, and create a new one from the plugin.
If a user removes the Client Status event type from one plugin or deletes the Tenant plugin with an iterator, it will automatically delete the iterator from Netskope Tenant. And by configuring a new plugin, users can create an iterator.
For more details on iterator deletion, refer to the
documentation
and reach out to your Netskope tenant support to delete an iterator.
Receiving cleanup() error while editing/enabling/disabling the plugin
You may encounter an error as shown below, this is due to incompatible cloud exchange version or incompatible tenant plugin version.
What to do:
Upgrade your Netskope Log Shipper to the latest version and your issue will be resolved.
Note
Device and Content alerts are supported starting from Cloud Exchange CE v5.1.0 and Tenant (Provider) v1.2.0
Client status event is supported starting from Cloud Exchange  v5.1.1, Tenant (Provider) v1.4.0
Unable to configure the plugin with Client status event
You may encounter below error because Client status event is supported starting from Cloud Exchange  v5.1.1 and Tenant Plugin v1.4.0.
What to do:
If you want to use this plugin on CE version below 5.1.1 and with Tenant version below v1.4.0, then remove the Client status event from Event Types field under Configuration Parameters, and then save the plugin.
If you want to pull Client status event then upgrade your  Cloud Exchange to v5.1.1, and Tenant Plugin to v1.4.0
Logs are not being ingested to the SIEM platform from the Netskope Log Shipper plugin
This could be due to this reason: when both Netskope Risk Exchange and Netskope Log Shipper are configured, and the Device entity is selected in CRE, a
client_status
iterator gets created for the tenant. If
Client Status
is not selected in the Event Types of the Netskope Log Shipper plugin, the existing iterator gets deleted during the CLS cleanup task (on plugin save). Since
Client Status
is not selected in the Event Types, the required iterator is not maintained. As a result, the task fails.
Steps to check the error:
Download the diagnostic file.
Unzip the diagnostic file and check for the below error message in the
core.log
file.
INFO/ForkPoolWorker-76194] Task common.pull[3c539ed9-0aa3-4ea9-b7f8-4d28c4e6b412] succeeded in 0.6612727344036102s: {'success': False, 'message': 'AttributeError("\\'NetskopePluginHelper\\' object has no attribute \\'tenant_name\\'")', 'trace': 'Traceback (most recent call last):
cloudexchange_core_1  |   File "/opt/netskope/common/utils/task_decorator.py", line 160, in wrapper
cloudexchange_core_1  |     ret = func(*args, **kwargs)
cloudexchange_core_1  |           ^^^^^^^^^^^^^^^^^^^^^
cloudexchange_core_1  |   File "/opt/netskope/common/celery/pull.py", line 132, in pull
cloudexchange_core_1  |     for data, data_sub_type, sub_type_config_mapping, is_expo_backoff in pulled_data:
cloudexchange_core_1  |   File "/opt/netskope/plugins/Default/netskope_provider/main.py", line 580, in pull
cloudexchange_core_1  |     client.sub_types = sub_type_config_mapping.keys()
cloudexchange_core_1  |     ^^^^^^^^^^^^^^^^
cloudexchange_core_1  |   File "/opt/netskope/plugins/Default/netskope_provider/utils/iterator_helper.py", line 523, in sub_types
cloudexchange_core_1  |     is_iterator_ready = self.netskope_api_plugin_helper.check_iterator_status(
cloudexchange_core_1  |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
cloudexchange_core_1  |   File "/opt/netskope/plugins/Default/netskope_provider/utils/iterator_api_helper.py", line 728, in check_iterator_status
cloudexchange_core_1  |    ...'}
What to do:
Go to the Log Shipper plugin configuration.
Select
Client Status
in the Event Types.
Save the plugin configuration.
This updates the iterator and allows event ingestion to the SIEM platform to resume successfully.
Known Behaviors
Fetching 0 Client Status Events in Historical Pulling
Even after providing sufficient permissions to the token used in the Tenant, the Client Status events are not pulled from historical pull tasks.
Getting the logs:
TENANT Netskope Tenant (Required) [tenant_name]: Skipping clientstatus subtype for historical pull as the Client Status does not support historical
.
Cause:
Due to API Limitations of Client Status iterator, historical pulling is not supported for Client Status events.
Fetching Device/Content alerts on Cloud Exchange v5.1.0 with Tenant v1.0.0
We have observed that in Netskope Log Shipper v2.2.1 there will be logs for pulling Device/Content alerts with Tenant(Provider) v1.0.0 but there will be no filter available in the business rule to filter Device/Content alerts until you upgrade your Tenant to v1.2.0 or above. Also, note that even after upgrading your Tenant to v1.2.0 or above you need to manually create a new business rule to include Device/Content alerts in the filter.
Netskope Log Shipper plugin pulls forensics fields even if “Pull DLP Incident Forensics” field is set to No
It may be due to reasons listed below:
If either the Netskope Ticket Orchestrator plugin or the Netskope Log Shipper plugin has the “Pull DLP Incident Forensics” field set to Yes, both plugins will automatically retrieve forensic fields for incident events.
Any change in the value of the
Pull DLP Incident Forensics
field will not be respected once the plugin is configured, unless you restart the core or delete the Netskope log shipper plugin as well as tenant plugin and reconfigure both the plugins.
Ingested content may have missing fields/data if you set “Pull DLP Incident Forensics” field as “Yes” or the content of any of the fields is very large
We have observed that some of the fields are very large and they have length beyond the maximum length supported by the Netskope Cloud Exchange. Due to this, you may encounter the below warning and you may observe that the ingested event is incomplete as rest of the values will be skipped.
Only 1 Netskope Tenant Plugin per Netskope Tenant
It is not recommended to use multiple Netskope Tenant plugins with the same Netskope Tenant. If you have configured Netskope Log Shipper or Netskope Risk Exchange plugin with the Netskope Tenant and you delete the client status iterator, then both the plugins will throw an error (example shown below) for deleting the Client Status Iterator, and you will not be able to use the Netskope Log Shipper or Netskope Risk Exchange plugin.
TENANT Netskope Tenant (Required) [crest-plugin-support]: Error occurred while Deleting Client Status Iterator netskope_ce_cs_iterator_1aef2620-80bc-43b2-ac1d-31d652ee0xxx for tenant https://crest-plugin-support.de.goskope.com.
In this Topic
Log Shipper Plugin

---
## Cloud Exchange Logs Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/cloud-exchange-logs-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:46:33+00:00
**Scraped:** 2026-08-10T07:56:13.616935+00:00

Cloud Exchange Logs Plugin for Log Shipper - Netskope Technical Documentation
Cloud Exchange Logs Plugin for Log Shipper
This document explains how to configure the Cloud Exchange Logs v2.1.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to pull logs of type Debug, Information, Warning and Error from Cloud Exchange Logs. This plugin can be used as a source plugin that can be used to ingest data to the 3rd-party platforms.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances) with the AWS Netskope Log Streaming service enabled.
A Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Cloud Exchange tenant with a 3rd-party plugin (like
Syslog
) already configured.
Cloud Exchange Logs Plugin Support
This plugin is used to pull Cloud Exchange Logs and share it with 3rd party plugins.
Data Type
Support
CE Logs
Yes (Error, Warning, Info, Debug)
Workflow
Configure the Cloud Exchange Logs plugin.
Configure a Business Rule.
Configure
Log Delivery (SIEM Mapping)
with the Cloud Exchange Logs plugin as the Source and a 3rd-Party plugin as the Destination.
Validation the plugin.
Click play to watch a video.
Configure the Cloud Exchange Logs Plugin
In Cloud Exchange, go to
Settings > General
and enable the Log Shipper module.
In
Settings
, go to
Plugin Store
. Search for and select the
Cloud Exchange Logs
plugin box.
Enter a configuration name.
Click
Next
and enter the Configuration Parameters:
Log Types:
Types of logs to fetch.
Initial Range (in days):
Number of days to pull the log data for the initial run.
Click
Save
.
Configure a Log Shipper Business Rule for the Cloud Exchange Logs Plugin
In Log Shipper, go to
Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Click
Save
.
Configure a Log Delivery (
SIEM Mapping) for Cloud Exchange Logs Plugin
In order to
Configure Log Delivery
(SIEM Mappings), a third-party Log Shipper destination plugin, like
Syslog
, has to be configured before proceeding. You need both a source and destination plugin (configurations) to create the SIEM mappings.
Go to the
Log Delivery
(SIEM Mapping) and click
Add Log Delivery Configuration
.
Select the Source plugin (CLS Cloud Exchange Logs), Destination plugin (CLS Syslog), and business rule, and then click
Save
.
Note
After the Log Delivery (SIEM mapping) is configured, the data will start getting pulled from the Netskope CE Logs, transformed, and ingested into the destination platform.
Validate the Cloud Exchange Logs Plugin
Validate the Pull
You must be able to fetch the logs from the Cloud Exchange platform. You can verify this the
Logging
page. Go to
Settings > Logging
. Apply a filter with the plugin configuration name.
Validate the Push
To validate the plugin workflow in Netskope Cloud Exchange:
Similarly, you can verify the logs for ingestion of data to the third-party platforms using the destination plugin configuration name.
Note
We have configured the Syslog plugin with the Splunk TCP Data input for illustration.
To validate the plugin workflow on Splunk:
You can search the ingested data with the log source identifier used while configuring the Syslog plugin. For more details related to the Syslog plugin, refer to the
plugin guide
.
Note
Resolution is supported in Cloud Exchange v6.0.0 and above.
In this Topic
Cloud Exchange Logs Plugin for Log Shipper

---
## Export DSPM Logs to Amazon S3
**URL:** https://docs.netskope.com/en/publishing-dspm-activity-logs-to-s3/
**Last Modified:** 2026-06-20T01:07:48+00:00
**Scraped:** 2026-08-10T07:57:08.297946+00:00

Export DSPM Logs to Amazon S3 - Netskope Technical Documentation
Export DSPM Logs to Amazon S3
Overview
Netskope Data Security Posture Management (DSPM), also known as Netskope One DSPM, generates activity logs that capture events such as scan executions, findings, configuration changes, and sidecar activity. You can export these logs to an Amazon Simple Storage Service (Amazon S3) bucket for long-term retention, analytics, or integration with downstream systems.
You can see downloadable logs of all activity within Netskope DSPM by navigating to
Administration > Activity Logs
. These are divided between
User Activity
and
System Activity
tabs, and can be sorted and filtered by activity type.
This guide explains how to configure your Netskope DSPM tenant to automatically publish these Activity Logs to Amazon S3 as
.json
objects, and how to validate that log delivery is working as expected.
To enable this feature in your tenant, please contact your Account Team or Netskope DSPM Support.
Prerequisites:
Before you start, ensure you have the following.
Netskope DSPM tenant:
Administrator access to your Netskope DSPM tenant.
AWS account:
An AWS account with permissions to create and manage:
Amazon S3 buckets.
IAM roles and policies.
(Optional)
KMS keys, if you use server-side encryption with AWS KMS.
Target S3 bucket:
An S3 bucket that will receive the DSPM logs. You can use an existing bucket or create a dedicated one for this purpose.
Plan Your S3 Log Export
Before configuring the export in Netskope DSPM, determine the following settings:
Bucket name and region:
The exact S3 bucket name and AWS Region where you will store DSPM logs.
Folder/prefix structure:
An optional prefix to organize logs, for example:
s3://<bucket-name>/dspm/logs/
Encryption requirements:
Decide if logs must be encrypted with S3-managed encryption keys (SSE-S3) or customer-managed keys using AWS KMS (SSE-KMS).
IAM trust and permissions model:
Netskope DSPM will write logs to S3 using an IAM role. This role requires a trust policy (allowing Netskope’s logging service to assume it) and an IAM policy granting write access (
s3:PutObject
,
s3:ListBucket
) to your target bucket.
Create or Select an S3 Bucket
If you do not already have a bucket for DSPM logs:
Sign in to the AWS Management Console and open the
Amazon S3
console.
Click
Create bucket
.
Specify the
Bucket name
(a globally unique name, such as
mycompany-dspm-logs
) and the
AWS Region
.
Configure options such as
Bucket versioning
(recommended for audit use cases) and
Default encryption
(SSE-S3 or SSE-KMS).
Adjust the
Block Public Access
settings to ensure the bucket remains private.
Click
Create bucket
.
If you are using an existing bucket, review its configuration to ensure it complies with your organization’s security and retention requirements.
Configure IAM Role and Policy for DSPM Logs
Create an IAM role that Netskope DSPM can use to write logs to your S3 bucket.
In the AWS Management Console, open the
IAM
service.
Click
Roles
and then
Create role
.
For
Trusted entity type
, configure the trust policy according to the guidance provided in the DSPM UI (typically, allowing a Netskope-managed principal to assume the role).
Attach an IAM policy that grants the role permission to write logs to the appropriate bucket and prefix. For example:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::<bucket-name>/<optional-prefix>/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::<bucket-name>"
    }
  ]
}
Complete the role creation and copy the
Role ARN
, which you will need to enter in the Netskope DSPM UI.
(Replace
<bucket-name>
and
<optional-prefix>
with values for your environment).
Configure DSPM to Export Logs to Amazon S3
After the S3 bucket and IAM role are ready, configure DSPM to publish logs.
Log in to your Netskope DSPM tenant.
Navigate to
Administration > Activity Logs
.
Follow the UI prompts to configure Amazon S3 as the log destination. Provide the following required fields:
Field
Required?
Value
cloud_account_id
Yes
Internal ID corresponding to your AWS Infrastructure Connection.
bucket_name
Yes
Name of the target bucket (assumption = this must already exist)
bucket_region
Yes
Region where bucket resides
file_prefix
No
Optional sub-folder to store destination files (only necessary if the S3 bucket is being shared with other business processes & you want to keep Netskope DSPM data segregated)
If the configuration screen supports it, run a
Test connection
to verify that DSPM can successfully write to the specified bucket.
Click
Save
.
Once enabled, Activity Logs will appear in S3 moving forward. Activity is not exported retroactively.
Validate Log Delivery to S3
After the configuration is saved, confirm that DSPM logs are being published to S3 correctly:
In the AWS console, go to
Amazon S3
.
Open the bucket configured as the DSPM log destination.
Navigate to the configured prefix or folder.
Confirm that new
.json
objects are being created. Depending on your settings, logs may appear organized by time, region, or log type.
(Optional)
Download a log file and verify that it contains the expected events (resource, action type, timestamp, user ID, description).
Troubleshooting:
If logs do not appear after a reasonable period:
Recheck the IAM role’s trust policy and permissions.
Confirm that the bucket name, region, and prefix in DSPM exactly match the S3 bucket.
Review any error messages in the DSPM UI related to log export.
Secure and Manage DSPM Logs in S3
To ensure ongoing security and compliance for your exported logs:
Encryption:
Ensure logs are encrypted at rest using SSE-S3 or SSE-KMS, based on your security policy.
Access Control:
Use strict S3 bucket policies and IAM to limit access to only the roles and users who require it.
Lifecycle Policies:
Configure S3 Lifecycle rules to transition older logs to lower-cost storage classes (such as S3 Glacier) or to expire them after a defined retention period.
Monitoring and Auditing:
Use AWS CloudTrail and AWS CloudWatch to monitor access to the bucket and detect anomalies.
Log Examples
All system and user activities are stored as separate
.json
objects with standard formatting. The timestamp on each record matches the time the activity was recorded in Netskope DSPM.
System Activity
{
   "timestamp": "02-15-2023 04:33:13",
   "type": "scan",
   "description": "Netskope One DSPM completed a scan of data store: 'fp-redshift'\n\nStart time: 2023-02-15 18:48:02.0\nEnd time: 2023-02-15 18:48:45.309\n\nNew queries scanned: 0\nExfiltration alerts generated: 0\nPrivacy alerts generated: 0\nData modification alerts generated: 0\nColumn classification alerts generated: 0\n\n# of new fields detected: 0\n# of new fields classified as sensitive: 0\n# of new fields classified as not sensitive: 0\n"
}
User Activity
{
   "timestamp": "02-15-2023 04:33:13",
   "type": "create",
   "username": "demo@netskope.com",
   "resource": "User Identity",
   "description": "User configured a new employee directory service with name Netskope One DSPM Directory"
}
In this Topic
Export DSPM Logs to Amazon S3

---
## FortiSIEM Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/fortisiem-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:34:15+00:00
**Scraped:** 2026-08-10T07:57:15.617373+00:00

FortiSIEM Plugin for Log Shipper - Netskope Technical Documentation
FortiSIEM Plugin for Log Shipper
This document explains how to configure the FortiSIEM v1.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Quarantine, Remediation, UBA, Watchlist, CTEP), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint), Web Transaction data, and CE logs (Debug, Information, Error, Warning) to FortiSIEM in JSON format.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for pulling WebTx from the Netskope Log Streaming plugins).
A Netskope Cloud Exchange tenant with the
Syslog for CE
plugin already configured (for pulling CE Logs).
Connectivity to the following host: FortiSIEM Server.
Parser will be required for parsing the collected logs while ingesting in CEF format and it has to be created and managed by the user.
FortiSIEM Plugin Support
The FortiSIEM plugin is used to ingest all the Alert, Events, WebTx [via Netskope LogStreaming] and CE Logs in JSON format to the specified FortiSIEM server. Ingestion in CEF format is not supported.
Data Type
Support
Events
Yes (Audit, Application, Infrastructure, Network, Incident, Page, Endpoint)
Alerts
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA)
WebTx
Yes (via Netskope LogStreaming)
Syslog CE Log
Yes (Info, Debug, Warning, Error)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
API Details
The plugin uses a
logging
third-party library to push the data to the FortiSIEM collector.
Library: logging
This module defines functions and classes which implement a flexible event-logging system for applications and libraries.
The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.
Refer to the official documentation for more information on the logging library.
https://docs.python.org/3/library/logging.html
List of Methods Used
Method: logging.getLogger(name=None)
Return a logger with the specified name or, if the name is None, return a logger which is the root logger of the hierarchy
All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
Method: setLevel(level)
Sets the threshold for this logger to level. Logging messages that are less severe than the level will be ignored; logging messages that have a severity level or higher will be emitted by whichever handler or handlers service this logger, unless a handler’s level has been set to a higher severity level than the level.
Method: handlers
The list of handlers is directly attached to this logger instance.
Note that this attribute should be treated as read-only; it is normally changed via the addHandler() and removeHandler() methods, which use locks to ensure thread-safe operation.
Method: addHandler(hdlr)
Adds the specified handler hdlr to this logger.
Method: removeHandler(hdlr)
Removes the specified handler hdlr from this logger.
Performance Matrix
This performance reading is conducted on a Large Cloud Exchange Stack with these VM specifications. These readings are added with the consideration that it will ingest around 10K events in 2 seconds to the FortiSIEM platform.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts/Events ingested to SIEM
~200K EPM
Workflow
Configure the FortiSIEM plugin.
Configure a Log Shipper Business Rule for FortiSIEM.
Configure Log Shipper Log Delivery for FortiSIEM.
Validate the FortiSIEM plugin.
Watch a Video
Click play to watch a video.
Configure the FortiSIEM Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
FortiSIEM v1.0.0 (CLS)
plugin.
Add a configuration name, and make sure you have the FortiSIEM Default Mapping file selected.
Note
Disable the toggle button to transform the logs in JSON, as the plugin only supports ingestion in JSON format. The ingestion of Endpoint event type is supported from CE version 5.1.0.
Click
Next
and enter values for these parameters:
FortiSIEM server: IP address/FQDN of FortiSIEM server in which data will be ingested.
FortiSIEM Protocol: Protocol to be used while ingesting data.
FortiSIEM Port: The port used while creating the Data input configuration.
Click
Save
. Your new plugin will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for FortiSIEM
In Log Shipper, go to
Business Rules
.
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Click
Save
.
Configure Log Shipper Log Delivery for FortiSIEM
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (CLS Netskope), Destination plugin (CLS FortiSIEM), and a business rule. Click
Save
.
For WebTx, select AWS Netskope LogStreaming or Azure Netskope LogStreaming and Destination plugin (CLS FortiSIEM), and click
Save
.
For Logs sharing,  select the Source plugin (CLS Syslog for CE), Destination plugin (CLS FortiSIEM), and a business rule, and click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the FortiSIEM platform.
Validate the FortiSIEM Plugin
Validate the Pull
To validate the pulling of Events, Alerts, logs, and Webtx from the Netskope tenant.
Go to the Logging in Netskope Cloud Exchange. Search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and search for ingested Events, Alerts, WebTx, and Logs with the filter
message contains ingested
. The ingested logs will be filtered.
Troubleshooting the FortiSIEM Plugin
Error occurred while ingesting data from CE to FortiSIEM
If you are unable to push alerts/events/logs/webtx[via Netskope LogStreaming] data on the FortiSIEM platform, then it could be due to the Port being deleted/disabled on the FortiSIEM platform.
What to do
:
Make sure the port is present and enabled, and if not, create a new port.
If ingested data is not reflected on the FortiSIEM Platform
If you are unable to view alerts/events/logs/webtx data on the FortiSIEM platform, it could be due to one of these reasons:
The filter is not correct on the SIEM platform.
There might be an error, but UDP was selected for the Port while configuring the FortiSIEM plugin. Hence, logs ingested are visible.
What to do
:
Make sure Data is searched using the correct filter.
Make sure to select the TCP port to check if there is any issue.
In this Topic
FortiSIEM Plugin for Log Shipper

---
## Scality Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/scality-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T03:47:07+00:00
**Scraped:** 2026-08-10T07:57:53.283158+00:00

Scality Plugin for Log Shipper - Netskope Technical Documentation
Scality Plugin for Log Shipper
This document explains how to configure the Scality plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to send Alerts (Anomaly, DLP, Malware, Policy, Compromised Credential, Legal Hold, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA and CTEP), Events (Page, Application, Audit, Infrastructure, Network, Incident and Endpoint) and WebTx[via Netskope LogStreaming] logs to the Scality platform. To access the plugin, you would need the credentials of Scality. Note that this plugin is designed to send raw (JSON) logs to Scality.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming plugin
already configured (for pulling WebTx from the Netskope Log Streaming plugins).
Your Scality instance URL, Access Key, Secret Access Key, and Scality Bucket Name.
A Scality instance and Bucket access.
Scality bucket permissions for the user.
ListBucket
CreateBucket
ListAllMyBuckets
GetBucketPolicy
GetBucketPublicAccessBlock
PutEncryptionConfiguration
PutBucketPublicAccessBlock
PutBucketPolicy
Scality Plugin Support
Scality plugin is used to ingest Netskope Events, Netskope Alerts, Web transaction data (via Netskope LogStreaming) to a Scality Bucket.
Data Type
Support
Events
Yes
Alerts
Yes
WebTx
Yes (via Netskope Log Streaming)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
The ingestion of Endpoint event type is supported from Cloud Exchange version 5.1.0.
Permissions
Scality bucket permissions to the user to send Events, Alerts, and Web transaction logs to buckets.
API Details
List of APIs Used
This plugin uses Python libraries to create file objects in Scality
Library: The AWS SDK for Python (Boto3)
Usage: The AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
Create the Client
s3_client = boto3.client(
                "s3",
                aws_access_key_id=self.scality_public_key,
                aws_secret_access_key=self.scality_private_key,
                aws_session_token=self.scality_session_token,
                endpoint_url=endpoint_url
                config=Config(proxies=self.proxy, user_agent=self.useragent),
            )
Create a Bucket
bucket = s3_client.create_bucket(
                        Bucket=bucket_name,
                        CreateBucketConfiguration=location,
                    )
Upload a File into the Bucket
s3_client.upload_file(
                file_name,
                bucket_name,
                object_name,
            )
Get an AWS Resource
s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=self.scality_public_key,
                aws_secret_access_key=self.scality_private_key,
                endpoint_url=endpoint_url
                config=Config(proxies=self.proxy, user_agent=self. user-agent),
            )
Workflow
Create a Scality Bucket.
Configure the Scality Plugin.
Configure a Log Shipper Business Rule for Scality.
Configure Log Delivery for Scality.
Validate the plugin.
Click play to watch a video.
Create a Bucket
Log to your Scality instance.
Enter your credentials and login.
Click
Create Bucket
and enter a bucket name in which you want to ingest your data.
Configure the Scality Plugin
In Cloud Exchange, go to
Settings
>
Plugin Store
. Search for and select the
Scality v1.0.0 (CLS)
plugin.
Enter a Configuration Name, and make sure you have the Scality Default Mappings (recommended) file selected.
Click
Next
and enter the Configuration Parameters:
Scality Endpoint URL
: Endpoint URL of your Scality instance (like
https://s3-your.domain.com/
)
Access Key
: Access Key for your Scality instance.
Secret Access Key
: Secret Access Key for your Scality instance.
Scality Bucket Name
: Scality Bucket Name in which the logs object will be stored. (Bucket will not be created if the bucket with the specified name does not exist on Scality.)
Maximum File Size (in MBs)
: Maximum size of WebTx[via Netskope LogStreaming] data object to be stored in the bucket. (Value should be between 1 to 100.)
Maximum Duration (in Seconds)
: Maximum duration after which the WebTx[via Netskope LogStreaming]
data object should be stored in the bucket.
Click
Save
. The new plugin will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for Scality
In Log Shipper, go to
Business Rules
.
By default, we have a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding a rule name and desired filters.  When finished, click
Save
.
Configure  Log Shipper Log Delivery for Scality
Go to
Log Shipper > Log Delivery
and click
Add Log Delivery Configuration
.
For alerts and events, select the Source plugin (Netskope CLS), Destination plugin (CLS Scality), your business rule, and then click
Save
.
For WebTx, select the Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming), and Destination plugin (CLS Scality), your business rule, and then click
Save
.
After the Log Delivery configuation is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into Scality.
Validate the Scality Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant, go to
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and search for ingested Events, Alerts, and WebTx with the filter
message contains ingested
.
The ingested logs will be filtered.
To validate the push on the Scality:
Log in to Scality.
Click on your bucket.
Click the
Alerts
folder.
Click on the
Events
folder.
Click on the
WebTx
folder.
Note that:
For alerts and events, the folder structure will be like
Alerts/feedname/year/month/day/hour/filename.txt
For WebTx, the folder structure will be like
Alerts/feedname/year/month/day/hour/filename.gz
Example:
demobucket/alerts/feedname=Malware/year=2023/month=11/day=30/hour=9/1701336881_139977276685128.txt
Troubleshooting the Scality Plugin
Facing issues while configuring the plugin
This error can occur during configuration if the Scality credentials or the bucket name is invalid.
What to do
:
Make sure your Scality Endpoint URL, Access Key, and Secret Access Key are valid.
Make sure that the bucket entered in the plugin exists on the Scality platform.
In this Topic
Scality Plugin for Log Shipper

---
## Microsoft Azure Event Hubs Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/microsoft-azure-event-hubs-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T10:37:08+00:00
**Scraped:** 2026-08-10T07:58:10.250260+00:00

Microsoft Azure Event Hubs Plugin for Log Shipper - Netskope Technical Documentation
Microsoft Azure Event Hubs Plugin for Log Shipper
This document explains how to configure the Microsoft Azure Event Hubs v2.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status) and WebTx [via Netskope LogStreaming] data. The data will be sent to the Microsoft Azure Event Hubs. This plugin supports ingestion in both CEF and JSON format.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured.
Standard tier subscription which have Event Hubs service.
For more information about Event Hubs service, go
here
.
For information about Azure Event Hubs for apache kafka, go
here
.
Connectivity to the following host:
https://portal.azure.com/
.
Microsoft Azure Event Hubs Plugin Support
This plugin supports ingestion of Alerts (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Watchlist, Quarantine, Remediation, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status) and WebTx (via Netskope Log Streaming
)
data. The data will be sent to the Microsoft Azure Event Hubs. This plugin supports ingestion in both CEF and JSON format.
Data Type
Support
Alerts
Yes (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Watchlist, Quarantine, Remediation, UBA, CTEP, Device, Content)
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status)
WebTx
Yes (via Netskope Log Streaming)
CE Logs
Not Supported
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope LogStreaming
or
Azure Netskope LogStreaming
plugin.
Permissions
While adding SAS Policy, make sure below mentioned permissions are checked:
Send
Listen
API Details
List of APIs Used
This plugin uses
kafka-python-ng
libraries to create kafka producer and consumer to ingest data to azure event hubs.
Library
: kafka-python-ng
Usage
: kafka-python-ng client for the Apache Kafka distributed stream processing system. kafka-python-ng is designed to function much like the official java client, with a sprinkling of pythonic interfaces (e.g., consumer iterators). kafka-python-ng is best used with newer brokers (0.9+), but is backwards-compatible with older versions (to 0.8.0). Some features will only be enabled on newer brokers.
bootstrap.servers=NAMESPACENAME.servicebus.windows.net:9093
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{YOUR.EVENTHUBS.CONNECTION.STRING}";
Create the Consumer
consumer = KafkaConsumer(
event_hub_name,
bootstrap_servers=bootstrap_server,
security_protocol=”SASL_SSL,
sasl_mechanism="PLAIN",
sasl_plain_username="$ConnectionString",
sasl_plain_password=connection_string,
request_timeout_ms=TIMEOUT_MS,
reconnect_backoff_ms=TIMEOUT_MS,
client_id=self._add_user_agent(),
)
List the Event Hubs present in the configured Event Hub Namespace
available_event_hubs = consumer.topics()
Create the Producer
producer = KafkaProducer(
bootstrap_servers=bootstrap_server,
security_protocol=”SASL_SSL”,
sasl_mechanism="PLAIN",
sasl_plain_username="$ConnectionString",
sasl_plain_password=connection_string,
batch_size=BATCH_SIZE,
acks=ACKS,
retries=retries,
linger_ms=LINGER_MS,
request_timeout_ms=TIMEOUT_MS,
reconnect_backoff_ms=TIMEOUT_MS,
value_serializer=lambda x: x.encode("utf-8"),
client_id=self._add_user_agent(),
)
Send Data to an Azure Event Hub
producer.send(
topic=event_hub_name,
value=(
data
if not isinstance(data, dict)
else json.dumps(data)
),
)
Performance Matrix
This performance reading was conducted on a Large Cloud Exchange Stack with these VM specifications. These readings are from ingesting around 2000k (2 Million) logs to Azure Event Hub in a batch of 10k.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Time taken to ingest a batch of Alerts/Events
~55 seconds
Note
The Microsoft Azure Event Hub configuration used for the above readings had 5 partitions and 5 throughput units.
User Agent
netskope-ce-6.0.0-cls-microsoft-azure-event-hubs-v2.0.0
Workflow
Configure Microsoft Azure Event Hubs.
Configure the Microsoft Azure Event Hubs Plugin.
Configure a Log Shipper Business Rule for Microsoft Azure Event.
Configure Log Shipper Log Delivery for Microsoft Azure Event.
Validate the plugin.
Watch a Video
Click play to watch a video:
Create a Namespace for Event Hub
Log in to the Microsoft Azure Platform.
Search for
Event Hubs
.
Click
Create
to create a Namespace.
Provide all the details and click
Review + create
. (For a Pricing tier, you can refer to the
Prerequisites
)
Create an Event Hub in Namespace
Go to the recently created Namespace, and click
+ Event Hub
to create a new Event Hub in the Namespace.
Enter all the required information and click
Review + create
.
Generate a Connection String for the Event Hub
For the Event Hubs Namespace Connection String, go to
Namespace > Settings > Shared access policies
.
Click
Add
to create a new Connection String. Enter a Policy Name and check these permissions:
Send
Listen
After the policy is created, click on the policy and copy the primary connection string.
Configure the Microsoft Azure Event Hubs Plugin
Go to
Settings > Plugin Store
. Search for and select the
Microsoft Azure Event Hubs v2.0.0 (CLS)
plugin.
Enter a plugin configuration name, and make sure you have the Microsoft Azure Event Hubs Default Mapping file is selected. If you want to share the data in JSON format, change the Format setting to JSON.
Click
Next
, and enter the Configuration Parameters:
Namesspace Name:
Your Microsoft Azure Event Hubs Namespace Name.
Port:
Your Microsoft Azure Event Hubs Port. The default port is 9093 for Event hubs TLS handshake, or provide the custom port based on your configuration.
Event Hubs Namespace Connection String:
Your Microsoft Azure Event Hubs Namespace Connection String. Like:
Endpoint=sb://<namespace_name>.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<shared_access_key>
. To get the connection string, go to
Microsoft Azure Event Hubs Namespace > Shared Access Policies > Primary connection string
.
Event Hub Name:
Your Microsoft Azure Event Hub Name.
Log Source Identifier:
This will be added as a prefix to all the logs. (The log source identifier should not contain whitespaces).
Exclude Timestamp Field:
Select
Yes
to ingest the data without the timestamp field. This option is only applicable to JSON-formatted data.
Exclude Log Source Identifier Field:
Select ‘Yes’ to ingest the data without the Log Source Identifier field. This option is only applicable to JSON-formatted data.
Producer Batch Size (in KB):
Maximum size (in KB) of a batch of messages that the producer will attempt to send to Event Hubs in a single request. Larger batch sizes can improve throughput but may increase memory usage. Allowed range: 16–1024 KB.
Buffer Memory (in MB):
Total memory (in MB) allocated for buffering unsent messages. If the buffer fills up, further send requests may be blocked or fail until space becomes available. Increasing this value can help handle bursts of log data. Allowed range: 32–128 MB.
Max Block Time (in seconds):
Maximum time (in seconds) a send operation will block if the buffer is full before raising an exception. This prevents indefinite blocking and helps control application responsiveness under heavy load. Allowed range: 10–60 seconds.
Batch Linger Time (in milliseconds):
Time (in milliseconds) the producer will wait for additional messages before sending a batch if the batch size is not reached. Higher values can increase batching efficiency but may add latency. Allowed range: 50–1000 ms.
Data Chunk Size:
Number of logs to group together into a single data chunk before sending to Event Hubs. Adjust this to control the granularity of data transmission and optimize performance for your workload. Allowed range: 1000–10000.
Flush Timeout (in seconds):
Maximum time (in seconds) allowed for flushing all buffered records to Event Hubs before timing out. Ensures that data is not delayed indefinitely in the buffer during shutdown or manual flush operations. Allowed range: 10–300 seconds.
Note
Exclude Timestamp Field
and
Exclude Log Source Identifier Field
are mandatory fields for JSON formatted data.
If you encounter errors related to memory allocation then you can increase the buffer memory and decrease the chunk size according to your Event Hubs configuration.
If you encounter a timeout error then users can increase flush timeout and decrease the chunk size according to their Event Hubs configuration.
If ingestion is taking much time then users need to increase the Event Hubs Configuration.
For a large stack, it is suggested to have 10 or more partitions and 20 or more throughput units.
For a medium stack, it is suggested to have 7 or more partitions and 10 or more throughput units.
For a small stack, it is suggested to have 5 or more partitions and 5 or more throughput units.
Click
Save
. Your new plugin configuration will be available on the
Log Shipper > Plugins
page.
Configure a Business Rule for Microsoft Azure Event Hubs
In Log Shipper, go to
Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
Click
Save
.
Configure a Log Shipper Log Delivery for Microsoft Azure Event Hubs
In Log Shipper, go to the
Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (AWS Log Streaming or Azure Log Streaming), Destination plugin (Microsoft Azure Event Hubs), a business rule, and then click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Microsoft Azure Event Hubs platform.
Validate the Microsoft Azure Event Hubs Plugin
Validate the Pull
In Cloud Exchange, go to the
Logging
and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and search for ingested Events and  Alerts With the filter
message contains ingested
. The ingested logs will be filtered.
To validate the push on the Microsoft Azure Event Hubs:
Log in to Microsoft Azure Platform.
Go to
Event Hubs > {Namespace} > Data Explorer.
Select the Event Hub, Partition ID, and Event position, and then click
View Events
. By selecting the Newest Position, you can get the live events ingested by the plugin. By selecting the Oldest Position, you can get the oldest events ingested as per the message retention time. And by selecting Custom Position, you can find a set of events from a custom filter.
Here is how the data will look if ingested in JSON format:
Here is how the data will look if ingested in JSON format without Timestamp and Log source identifier fields:
Troubleshooting the Microsoft Azure Event Hubs Plugin
Difficulties in saving the Microsoft Azure Event Hubs plugin
Despite entering all parameters and clicking the Save button, an error may occur, possibly due to the configuration differs from the specified settings.
What to do:
It could be because of incorrect configuration parameters, just follow the steps in the
Configure the Microsoft Azure Event Hub section
.
Not able to see the events on the Microsoft Azure Event Hubs
Even after successful ingestion of the events, not able to see the events ingested from the plugin. This could be due to the following reasons:
Selected the wrong configuration to see the events on Event Hub.
No events are ingested in the time of view events wait time.
Or the data you are looking for is outside of the retention period.
What to do:
Check if you have selected the
Newest Position
to see the live ingested events.
Check for the logs on the Cloud Exchange for the ingested events.
For checking the retention period of the Event Hub, go to the Overview page of the Namespace, and under that you can find the Message retention. And by editing the Event Hub, you can change the retention time of the Event Hub. Refer to the Create an Event Hub in Namespace section.
Unable to enable the plugin after plugin upgrade
When plugin is added to ingest the JSON formatted data and upgraded, if you use the
Skip
button, then you will encounter an error for the
Exclude Timestamp Field
and
Exclude Log Source Identifier Field
while enabling the plugin configuration after the plugin upgrade:
What to do:
Since the
Exclude Timestamp Field
and
Exclude Log Source Identifier Field
are mandatory fields for JSON formatted data, you need to select yes/no in both the fields as per your requirement.
Note
If you have configured an older plugin version with CEF formatted data and then you upgrade the plugin and while upgrading if you use the Skip button then by default you will be able to use that plugin configuration with CEF format and the newly added 2 fields(i.e.
Exclude Timestamp Field
and
Exclude Log Source Identifier Field
) will be empty.
Unable to Configure Plugin/Queue/Disable Plugin
If you are not able to save the plugin/configure queue/disable the Microsoft Azure Event Hubs plugin, it might be due to an SSL certificate verification failure.
What to do:
If you are running Cloud Exchange on your on-premises device and receiving the
“[SSL: CERTIFICATE_VERIFY_FAILED] certificate verification failed: unable to get local issuer certificate”
error, contact your organization IT Team. This issue can be resolved by using cloud platforms such as EC2 or Azure.
Timeout error while ingesting data to Microsoft Azure Event Hubs
Users might encounter the below timeout error due to flush timeout  and the chunk size set in the plugin configuration.
What to do:
Increase flush timeout  and decrease the chunk size according to your Event Hubs configuration.
Note:
If you encounter errors related to memory allocation then you can increase the buffer memory and decrease the chunk size according to your Event Hubs configuration.
If you encounter a timeout error then users can increase flush timeout and decrease the chunk size according to their Event Hubs configuration.
If ingestion is taking much time then users need to increase the Event Hubs Configuration.
For a large stack, it is suggested to have 10 or more partitions and 20 or more throughput units.
For a medium stack, it is suggested to have 7 or more partitions and 10 or more throughput units.
For a small stack, it is suggested to have 5 or more partitions and 5 or more throughput units.
Known Behavior of the Microsoft Azure Event Hubs Plugin
Users might not be able to ingest BWAN events, Events of type Client Status, Alerts of types Device and Content as this plugin does not support ingestion of BWAN events, Events of type Client Status, Alerts of types Device and Content.
Users may encounter escape characters in the ingested data due to several factors, such as accented characters (in English), characters of languages other than English, non-breaking spaces, newline characters, and other special formatting symbols.
Example:
<14>Apr 07 09:32:56 alltypes CEF:0|Netskope|Mock Netskope Tenant|NULL|application|NULL|Unknown|act=Download appcategory=Cloud Storage applicationType=nspolicy browser=unknown
\\u4ed5\\u4e8b
cci=89 ccl=high device=Other dst=ef82::1a12:1234:1b12 os=unknown requestClientApplication=Box sourceServiceName=Box src=ef82::1a12:1234:1b12 suser=support@netskope.com timestamp=1743736484
Here two Japanese characters that were ingested, which looked like “
\\u4ed5\\u4e8b
” in the above log.
Users may observe empty configuration parameters after plugin upgrade.
In this Topic
Microsoft Azure Event Hubs Plugin for Log Shipper

---
## Stream Logs to Amazon S3
**URL:** https://docs.netskope.com/en/stream-logs-to-amazon-s3/
**Last Modified:** 2026-06-15T23:14:22+00:00
**Scraped:** 2026-08-10T07:58:33.080520+00:00

Stream Logs to Amazon S3 - Netskope Technical Documentation
Stream Logs to Amazon S3
Netskope Log Streaming supports sending log files to Amazon S3. Provide details for the selected destination type. Destinations supported might offer different features and capabilities. The fields to fill in differ depending on the destination type the user selects.
Select Amazon S3 with SQS for optimum performance.
Verify your S3 bucket has the necessary
write permissions
to receive log files.
For the Amazon S3 destination field, fill in the following fields:
Name of Destination:
A human-readable description for the destination.
Bucket
: The name of the user’s Amazon S3 bucket (e.g., netskopepartnerlogfilebucket).
Folder Path
(optional): The path to the folder within the bucket where the user wants to store and save their logs. If the folders don’t exist in the bucket, Amazon creates them—for example, logs or logs/diagnostics. Amazon treats objects that end with / as folders. For example, if you start your path with /, as in /logs, Amazon creates two folders in your bucket. The first one is named /, and it contains the logs folder. To learn more:
Using folders in AWS
and
Bucket naming rules in Amazon S3
. NOTE: Do not start your path with a / unless you intend to create a root-level folder named /.
Access
Select your preferred authentication method.
IAM Role
is recommended for enhanced security.
Option 1: IAM Role (Recommended)
This method uses a trust relationship between your AWS account and Netskope, eliminating the need for long-lived credentials.
IAM Role ARN:
Enter the Amazon Resource Name (ARN) of the IAM role you created in your AWS account for Netskope. To learn more:
AWS setup details
Netskope Account ID:
This is a read-only field (e.g., 448000000000). You must copy this ID and add it to the
Trust Policy
of your IAM Role in the AWS Console to allow Netskope to write to your bucket.
Option 2: Access Keys
Access Key ID:
The Access Key ID to the S3 bucket, provided by AWS.
Secret Access Key:
The Secret Access Key to the S3 bucket, provided by AWS.
Region & Delivery
Region:
The AWS services region where your S3 bucket is hosted (e.g., us-east-1).
Set up IAM on Your Account
Create an IAM role.
Update the Roles
Trust Relationship
with the policy below.
Update the Roles
Permission
to include the s3 bucket write permission.
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"AWS": [
					"arn:aws:iam::<netskopeaccount-id>:root"
				]
			},
			"Action": [
				"sts:AssumeRole"
			]
		}
	]
}
Set up IAM on Your Account with ExternalId
Create an IAM role.
Update the Roles T
rust Relationship
with the policy below and note the condition which passes the externalId value.
Update the Roles
Permission
to include the s3 bucket write permission.
Use the IAM Role ARN and the externalID value when configuring the stream.
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"AWS": [
					"arn:aws:iam::<netskopeaccount-id>:root"
				]
			},
			"Action": [
				"sts:AssumeRole"
			],
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "externalIdNetskopeLogStreaming"
                }
            }
		}
	]
In this Topic
Stream Logs to Amazon S3

---
## Stream Logs to Azure Blob
**URL:** https://docs.netskope.com/en/stream-logs-to-azure-blob/
**Last Modified:** 2026-06-15T23:15:33+00:00
**Scraped:** 2026-08-10T07:58:34.252841+00:00

Stream Logs to Azure Blob - Netskope Technical Documentation
Stream Logs to Azure Blob
Netskope Log Streaming supports sending log files to Azure Blob. Provide details for the selected destination type. Destinations supported might offer different features and capabilities. The fields to fill in differ depending on the destination type the user selects.
For the Azure Blob destination field, fill in the following fields:
Name of Destination:
A human-readable description for the destination.
Storage account name
: The name of the storage account where the user wants to store logs. To learn more:
Blob storage resources
in Azure.
Container Name:
The name of the container within a user’s account where the user wants to store logs. To learn more:
Naming resources
in Azure.
Path
: The path to the folder within the bucket where the user wants to store and save their logs. If the folders do not exist in the bucket, Azure creates them—for example, logs or logs/diagnostics.
Access Key
: Either of the access keys associated with user’s Azure account. To learn more:
Authorization
in Azure.
In this Topic
Stream Logs to Azure Blob

---
## Stream Logs to GCP Cloud Storage
**URL:** https://docs.netskope.com/en/stream-logs-to-gcp-cloud-storage/
**Last Modified:** 2026-06-15T23:24:32+00:00
**Scraped:** 2026-08-10T07:58:35.424001+00:00

Stream Logs to GCP Cloud Storage - Netskope Technical Documentation
Stream Logs to GCP Cloud Storage
Netskope Log Streaming supports sending log files to GCP Cloud Storage. Provide details for the selected destination type. Destinations supported might offer different features and capabilities. The fields to fill in differ depending on the destination type the user selects.
For the GCP Cloud Storage destination field, fill in the following fields:
Name of Destination:
A human-readable description for the destination.
Bucket
: The name of the storage bucket you created in your Google Cloud account. To learn more:
Bucket naming conventions
for Google Cloud Storage.
Path
: Optional. The path to the folder within your Google Cloud bucket where you want to store logs. In Google Cloud Storage, paths work as object names. When you enter a custom path, such as netskope/logs/{%Y}, Google Cloud Storage doesn’t create new Netskope, logs, and {%Y} folders in the bucket. Instead, the objects are stored in one bucket and named netskope/logs/{%Y}/filename. To learn more:
Object naming guidelines
for details.
Private Key
: The complete contents of the service account JSON key file generated and downloaded from your Google Cloud account. Paste the entire JSON object, including all fields such as
type
,
project_id
,
private_key_id
,
private_key
,
client_email
, and
client_id
. Do not paste only the
private_key
value — entering the standalone private key (PEM format) results in a credential validation error.
Example format:
{ “type”: “service_account”, “project_id”: “your-project-id”, “private_key_id”: “…”, “private_key”: “—–BEGIN PRIVATE KEY—–\n…\n—–END PRIVATE KEY—–\n”, “client_email”: “your-sa@your-project-id.iam.gserviceaccount.com”, “client_id”: “…”, … }
To create a service account key, see
Create and delete service account keys
in the Google Cloud documentation.
After you save the destination, Netskope validates the credentials by writing a test file (
netskope-test-file.txt
) to your bucket. The presence of this file confirms connectivity and permissions are working. Log stream initialization can take up to 1 hour before event files begin appearing in the bucket. Files are delivered with gzip compression (
.gz
extension) under the configured path prefix.
In this Topic
Stream Logs to GCP Cloud Storage

---
## Publisher Logs for Troubleshooting
**URL:** https://docs.netskope.com/en/publisher-logs-for-troubleshooting/
**Last Modified:** 2026-03-03T02:05:27+00:00
**Scraped:** 2026-08-10T07:59:34.217925+00:00

Publisher Logs for Troubleshooting - Netskope Technical Documentation
Publisher Logs for Troubleshooting
Connection Segment
Description
Example
Registration Logs – Publisher
Logs to verify successful registration, or failed registration.
Logs to check:
~/logs/publisher_wizard.log
Successful Registration:
2021/07/27 20:00:41 UTC Registering with your Netskope address: ns-6413.us-sv5.npa.
<tenant-domain>
2021/07/27 20:00:41 UTC Publisher certificate CN: 130dbd9d40e4ad35 2021/07/27 20:00:41 UTC Attempt 1 to register publisher. 2021/07/27 20:00:43 UTC Publisher registered successfully.
Failed Registration:
2021/08/19 13:21:06 UTC Attempt 1 to register publisher. 2021/08/19 13:21:08 UTC Get https://ns-6413.us-sv5.npa.
<tenant-domain>
/api/discovery: x509: certificate signed by unknown authority 2021/08/19 13:21:08 UTC Registration failed because a discovery call didn’t succeed. Please generate a new token and try again.
Publisher ⇔ Netskope connectivity logs
Logs to check: ~/logs/agent.txt
Succesful tunnel connection:
eventlog.cpp:115:logPublisherTunnelEvent():0x0 {“eventId”: “NPACONNECTED”, “publisherId”: “130dbd9d40e4ad35”, “stitcherIp”: “163.116.135.6”, “tenant”: “ns-6413.us-sv5.npa.
<tenant-domain>
“}
Successful connection and certificate verification:
sslhelper.cpp:80:verify_callback():0x0 Verified: /DC=io/DC=newedge/CN=New Edge Root CA Failed connection due to SSL error sslhelper.cpp:302:logSslError():0x0 SSL Error 5 error:00000005:lib(0):func(0):DH lib
Publisher⇔ Netskope HTTPS logs
Management Plane:
openssl s_client -connect ns-{TENANTID}.{POPNAME}.npa.
<tenant-domain>
:443 -servername ns-{TENANTID}.{POPNAME}.npa.
<tenant-domain>
Data Plane
: openssl s_client -connect stitcher.npa.
<tenant-domain>
:443 -servername ns-{TENANTID}.{POPNAME}.npa.
<tenant-domain>
Publisher⇔ Application Connection Logs
Logs to check: ~/logs/agent.txt
Application definition and reachability:
reachability.cpp:109:parse():0x2484790
Added protocols
login.microsoftonline.com:tcp:443-443; tcp:80-80; udp:443-443; udp:80-80;
Application connection:
tcpproxyhandler.cpp:35:TcpProxyHandler():0x2504cf0
Creating tcp connection to
login.microsoftonline.com:443
Client connects and disconnects
May follow Publisher disconnects and can be used to correlate issues:
neconfig.cpp:121:setClientId():0x0 Set clientId l0ThzLYeZnqA
Indicates a graceful shut down and will not always be present if there’s an issue:
L3ClientChannel.cpp:48:destroy():0x1292810 Cleaning up l3clientChannel
In this Topic
Publisher Logs for Troubleshooting

---
## Publisher Filtering and Exporting Options
**URL:** https://docs.netskope.com/en/publisher-filtering-and-exporting-options/
**Last Modified:** 2026-03-03T02:06:50+00:00
**Scraped:** 2026-08-10T07:59:39.029282+00:00

Publisher Filtering and Exporting Options - Netskope Technical Documentation
Publisher Filtering and Exporting Options
To use these features, go to
Settings > Security Cloud Platform > Publishers
.
Filters
These filtering options are available in the Netskope UI.
Status
Update Profile
Version Update Status
Version
Publisher CN
Note
When you select a filter with a search icon
, that value is added to the search field so you can add more specifics. When a filter has an adjacent toggle arrow
, there are expanded options to choose from.
You can also clear and remove filters.
Export
The results displayed can be exported by clicking
Export
.
Choose to export the displayed columns, or select the columns to export, and then click
Export
.
In this Topic
Publisher Filtering and Exporting Options

---
## Understanding Supported Audit Log Events
**URL:** https://docs.netskope.com/en/understanding-supported-audit-log-events/
**Last Modified:** 2026-01-16T07:49:39+00:00
**Scraped:** 2026-08-10T07:59:48.678893+00:00

Understanding Supported Audit Log Events - Netskope Technical Documentation
Understanding Supported Audit Log Events
Audit logs are a record of all events, actions, or changes made within an organization’s systems, applications, or networks. These logs provide a historical account of what has occurred, including user activities, system modifications, and security-related events.
Navigate to
Settings > Administration > Audit Log
from your tenant home page. Refer to the article
About Audit Log
for more details.
Benefits:
Improved Security:
Real-time monitoring and analysis enable swift detection of potential threats.
Compliance Management:
Detailed records facilitate compliance with regulatory requirements.
Troubleshooting Efficiency:
Logs simplify issue resolution by providing a clear picture of what happened before an incident occurred.
Netskope SSPM logs audit events for the following actions:
Changes to rules
Changes to policies
Data exports
Verification of 3rd Party Apps
Changes to the posture score
Customization of the posture score
Viewing SSPM Events in Audit Logs
Follow the procedure to look for a specific SSPM event in the audit logs:
Log in to the
Netskope tenant UI
.
Go to
Settings > Administration > Audit Log
.
Click
+ Add Filter
.
In the
Log Type
option, enter “sspm” to display all supported SSPM events.
Select any listed event to filter the table and view details specific to that SSPM event.
References
Audit Log filters
In this Topic
Understanding Supported Audit Log Events

---
## CrowdStrike Next-Gen SIEM Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/crowdstrike-next-gen-siem-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:47:08+00:00
**Scraped:** 2026-08-10T08:00:12.017108+00:00

CrowdStrike Next-Gen SIEM Plugin for Log Shipper
This document explains how to configure the CrowdStrike Next-Gen SIEM v1.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports the ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, and CTEP) and Events (Page, Application, Audit, Infrastructure, Network, Incident, and Endpoint) to HEC / HTTP Event Connector on CrowdStrike Next-Gen SIEM platform. This plugin only supports sharing raw JSON data to CrowdStrike Next-Gen SIEM.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured
.
Access to a CrowdStrike Next-Gen SIEM Server to get your API URL and API Token.
Subscription to CrowdStrike Next-Gen SIEM service with valid certificates.
Connectivity to the following host:
https://*.ingest.us-1.crowdstrike.com/services/collector
.
CrowdStrike Next-Gen SIEM Plugin Support
This plugin supports the ingestion of Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, and CTEP) and Events (Page, Application, Audit, Infrastructure, Network, Incident, and Endpoint) to HEC / HTTP Event Connector on CrowdStrike Next-Gen SIEM platform. This plugin only supports sharing raw JSON data to CrowdStrike Next-Gen SIEM.
Types of Data Supported
Data Type
Description
Alerts Support
Yes (Compromised Credential, Policy, Malsite, Malware, DLP, Security Assessment, Watchlist, Quarantine, Remediation, UBA, CTEP)
Event Support
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint)
WebTx Support
Not Supported
CE Logs
Not Supported
API Details
List of APIs Used
API Endpoint
Method
Use Case
/services/collector
POST
Ingest Alert and Events
Ingest Alert and Events
API endpoint:
/services/collector
Method:
POST
Headers
Key
Value
Authorization
Bearer
<API Token>
Content-Type
application/json
User-Agent
netskope-ce-5.1.0-cls-crowdstrike-next-gen-siem/1.0.0
API Payload
Key
Value
event
Alert/Event JSON payload
timestamp
Timestamp in epoch format. e.g.1739436774
fields
#ce_log_source
Unique identifier for cloud exchange logs. Value: netskope-ce
#ce_log_source_identifier
Log Identifier for searching on Next-Gen SIEM.
Default value: Netskope Cloud Exchange
#ce_tenant_name
Tenant configuration name on cloud exchange. Example: Plugins
Sample API Payload
{
  "event": "<JSONalert/event>",
  "timestamp": 1739436774,
  "fields": {
    "#ce_log_source": "netskope-ce",
    "#ce_log_source_identifier": "Netskope Cloud Exchange",
    "#ce_tenant_name": "Plugins"
  }
}
Sample API Response
{
 "text": "Success",
 "code": 0
}
Performance Matrix
This performance reading is conducted on a Large Stack CE with these VM specifications. These readings are added factoring that it will ingest around 10K alerts and events in ~8.65 seconds to the CrowdStrike Next-Gen SIEM platform.
Stack Details
Alerts/Events ingested to third-party SIEM
Size: Large
RAM: 32 GB
CPU: 16 Cores
~200K EPM
User Agent
netskope-ce-5.1.0-cls-crowdstrike-next-gen-siem/1.0.0
Workflow
Configure on HEC/HTTP Event Connector on CrowdStrike Next-Gen SIEM
Configure the Netskope Tenant and Netskope CLS Plugins
Configure the CLS CrowdStrike Next-Gen SIEM Plugin
Add Business Rules
Add SIEM Mapping
Validation
Click play to watch a video.
Configure a Connector on CrowdStrike Next-Gen SIEM
Log in to CrowdStrike Platform
Click on the menu from the upper left corner, and go to
Next-Gen SIEM > Data onboarding
.
Search for
HEC / HTTP Event Connector
.
Click on the connector card, add a Data source (Data type as JSON) and Connector name, and add the
netskope-sse
parser.
Click the
Terms and Conditions
affirmation, and then click
Save
; this will create a connector on the
My Connectors
page.
To create the API URL and API token, click
Generate API key
. This will display the API URL and API Token. Save these, because the API Token can not be seen after closing it.
Configure the CrowdStrike Next-Gen SIEM Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and select the
CrowdStrike Next-Gen SIEM v1.0.0 (CLS)
plugin box.
Enter a configuration name, and make sure you have the CrowdStrike Next-Gen SIEM Default Mapping file selected. Disable the toggle button to transform the logs to ingest the data in JSON.
Click Next, and enter the conifiguration parameters:
API URL: Enter your API URL obtained previously. Example:
https://<UniqueIdentifier>.ingest.<Region>.crowdstrike.com/services/collector
.
API Token: Enter your API Token obtained previously.
Log Source Identifier: This will be added as a tag to all the alerts and events. Default value is Netskope Cloud Exchange.
Click
Save
. This plugin configuration will be available on the
Log Shipper > Plugins
page.
Configure a Log Shipper Business Rule for the CrowdStrike Next-Gen SIEM Plugin
In Log Shipper, go to
Business Rules
.
By default, there a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
When finished, click
Save
.
Configure a Log Shipper SIEM Mapping for the CrowdStrike Next-Gen SIEM Plugin
In Log Shipper, go to
SIEM Mappings
and click
Add SIEM Mapping
.
Select the Source plugin (CLS Netskope), Destination plugin (CrowdStrike Next-Gen SIEM), and a business rule, and then click
Save
.
After the SIEM mapping is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the CrowdStrike Next-Gen SIEM platform.
Validate the CrowdStrike Next-Gen SIEM Plugin
Validate the Pull
Go to the
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and search for ingested Events and Alerts with the filter
message contains ingested
. The ingested logs will be filtered.
To validate the push on the CrowdStrike Next-Gen SIEM platform:
Log in to CrowdStrike.
Click on the menu from the upper left corner, and go to
Next-Gen SIEM > Advanced event search
.
Add query like
“(#type=”netskope-sse”) | (#ce_log_source_identifier=”Netskope Cloud Exchange”) | tail(1000)”
, and also, events and alerts can be distinguished by adding
(#event.kind=”alert”)
or
(#event.kind=”event”)
.
Troubleshooting
Difficulties with saving the CrowdStrike Next-Gen SIEM plugin
Despite entering all parameters and clicking
Save
, an error may occur, possibly due to the server/port configuration differing from the specified settings.
What to do:
It could be because of incorrect configuration parameters; review the steps in the Configure the CrowdStrike Plugin section.
Kept the
When enabled, logs will be transformed using selected a mapping file
toggle enabled.
What to do:
As the plugin only supports sharing Alerts and Events in Raw JSON format, you need to disable the toggle, and then click
Save
.
In this Topic
CrowdStrike Next-Gen SIEM Plugin for Log Shipper

---
## Stream Logs to Splunk
**URL:** https://docs.netskope.com/en/stream-logs-to-splunk/
**Last Modified:** 2026-05-28T02:28:42+00:00
**Scraped:** 2026-08-10T08:00:42.675328+00:00

Stream Logs to Splunk - Netskope Technical Documentation
Stream Logs to Splunk
Netskope provides support for the following Splunk integrations to stream NLS logs.
Stream Logs to Splunk with AWS
Netskope Log Streaming supports sending log files to Splunk Add-on for AWS. This document will help you get the data from the AWS bucket to Splunk. To get the data from AWS to Splunk, there is Splunk Add-on for Amazon Web Services (AWS).
Sizing, performance, and cost considerations for the Splunk Add-on for AWS:
https://splunk.github.io/splunk-add-on-for-amazon-web-services/SizingAndCost
At a high level, the steps required to maintain data continuity and dashboard functionality are:
Install the Netskope Add-on for Splunk (if not already present).
Update the Netskope Add-on to the latest version (minimum v4.4.0).
Configure the AWS Add-on Input using the relevant sourcetype as instructed below.
Consider updating the sourcetype stanza in case of any other custom sourcetype.
Getting Data in Splunk using Splunk Add-on for Amazon Web Services (AWS)
A direct approach to get data from AWS S3 buckets in Splunk with the help of Splunk Add-on for Amazon Web Services (AWS). In this approach, we can leverage Splunk’s AWS connector and pull the data from S3 buckets.
This approach contains two methods to get the data from S3:
Getting real-time data using SQS based input (Recommended)
Getting historical data using Generic S3 input
You must install the legacy
Netskope Add-on for Splunk
. This is essential to ensure that the sourcetypes and necessary Netskope mappings are present, allowing the logs extracted by the new AWS TA to be properly parsed by the Netskope TA for successful indexing and searches.
Getting Real-time Data using SQS based S3 input (Recommended)
Users must configure SQS-based S3 input from Splunk Add-on for AWS to collect real-time data. For more information on SQS-based S3 input, refer official documentation:
https://splunk.github.io/splunk-add-on-for-amazon-web-services/SQS-basedS3/
Prerequisites
AWS users will need the following permissions:
Permissions are required for SQS access:
GetQueueUrl
ReceiveMessage
SendMessage
DeleteMessage
ChangeMessageVisibility
GetQueueAttributes
ListQueues
Required permissions for S3 buckets and objects:
GetObject (if Bucket Versioning is disabled).
GetObjectVersion (if Bucket Versioning is enabled).
Required permissions for KMS:
Decrypt
For more information, please refer to the official documentation of Splunk Add-on for AWS –
Configure AWS permissions for the SQS-based S3 input
.
Create a SQS Queue in AWS
From the search panel, search for SQS (Simple Queue Service).
Create a standard SQS Queue in the same region as the S3 bucket, set the
Visibility Timeout
to 5 minutes or more, and enable the
Dead-letter queue
.
Dead Letter Queue is to be used for the input for storing invalid messages. For information about SQS Dead Letter Queues and how to configure them, see the
Amazon SQS dead-letter queues
topic in the AWS documentation.
Create a SNS Topic in AWS
From the search panel, search for SNS (Simple Notification Service).
Create a standard SNS Topic in the same region as the S3 bucket.
Once created, note the SNS Topic ARN.
Edit the Access Policy for the SNS topic and replace it with below sample policy and save:
Enter your AWS SNS an S3 bucket ARN in the placeholders below. { “Version”: “2008-10-17”, “Id”: “example-ID”, “Statement”: [ { “Sid”: “example-statement-ID”, “Effect”: “Allow”, “Principal”: { “AWS”: “*” }, “Action”: “SNS:Publish”, “Resource”: “”, “Condition”: { “ArnLike”: { “aws:SourceArn”: “” } } } ] }
Click on
Create subscription
in the SNS Topic and subscribe to the SQS Services, and specifically select the SQS Queue we created in above steps.
Create Event Notification from S3
From S3 go to your bucket >
Properties.
From the
Event notifications
section, select
“Create event notification”
.
In the
Event types
section, select
All object create events
from the
Object creation.
In the
Destination,
select the
SNS Topic.
Select the created SQS queue from the dropdown.
Splunk Add-on for AWS Setup
Install
Splunk Add-on for Amazon Web Services (AWS)
on the splunk instance from Splunkbase or Splunk Web. For more help follow the
Installation overview for the Splunk Add-on for AWS
.
After configuring the IAM user, configure the Account in the Splunk Add-on.
Go to the
Configuration
Page.
In the
Account
tab, click
Add
.
Add the required information like Name, Key ID, and Secret Key.
Click
Add
.
After configuring the account successfully, create a new input to collect the data from the S3 bucket.
Go to the
Inputs
page.
Click
Create New Input
>
Custom Data Type
> select
SQS-based S3.
Add the required information in all the required fields. For
SQS Queue Name
, select the SQS Queue that was created earlier.
Update relevant sourcetype for example: netskope:web_transaction:nls for Netskope Web Transaction data. Refer
Sourcetype Consideration Based on the Input Configuration (Parse all files as CSV)
Section
For ingesting web transaction data via NLS using the sourcetype netskope:web_transaction:nls, it is recommended to keep the
“Parse all files as CSV” option disabled (unchecked)
in the Advanced Settings during input configuration. Enabling this option for web transaction data is not recommended, as it may lead to
increased Splunk license consumption
as well as it may introduce
field parsing issues.
For log types other than web transaction data, the
“Parse all files as CSV”
option can be enabled to ingest logs in JSON format.
When this option is disabled, logs are ingested in CSV format. However, additional configuration for CSV field extraction will be required depending on the selected sourcetype. It is recommended to validate the configuration outlined in the section
“Updating Field Extraction Configuration for a Sourcetype Using Splunk Web”
to ensure proper log parsing.
“CSV field delimiter” is required when the
Parse all files as CSV
is enabled. Ensure that this field in the Advanced Settings section is configured according to the delimiter used in the source CSV file.
Keep every other fields as default.
Click
Add
.
Sourcetype Consideration Based on the Input Configuration (Parse all files as CSV):
When
“Parse all files as CSV” = True
, refer below table:
Data Type
Sourcetype
Alerts
netskope:alert
Application
netskope:application
Connection (Page data)
netskope:connection
Endpoint
netskope:endpoint
Incident
netskope:incident
Network
netskope:network
Here, data will be in JSON format and hence, auto field extractions will take place.
When
“Parse all files as CSV” = False
, refer below table:
Data Type
Sourcetype
Web Transaction
netskope:web_transaction:nls
Alerts
netskope:alerts:nls
Application
netskope:application:nls
Connection (Page data)
netskope:connection:nls
Endpoint
netskope:endpoint:nls
Incident
netskope:incident:nls
Network
netskope:network:nls
Dashboard & Search Updates Required
Existing queries for any splunk dashboards/reports must be updated to support both legacy and new sourcetypes. For example:
sourcetype IN (“netskope:web_transaction”, “netskope:web_transaction:nls”)
It is recommended to standardize queries using wildcards where applicable:
sourcetype=”netskope:web_transaction*”
Performance Reference
https://splunk.github.io/splunk-add-on-for-amazon-web-services/S3PerformanceReference/#measured-performance-data
Getting Historical Data using Generic S3 input
Prerequisites
A valid AWS account with permissions to configure AWS services and create IAM roles and users. For more help follow the
AWS account prerequisites
.
Users must have an IAM role with the
s3admin
policy. For detailed instructions, refer to the documentation:
Manage accounts for the Splunk Add-on for AWS
.
Known Issues
Note that the Generic S3 input lists all the objects in the bucket and examines each file’s modified date every time it runs to pull uncollected data from an S3 bucket. When the number of objects in a bucket is large, this can be a very time-consuming process with low throughput. Hence, Splunk recommends configuring an SQS-Based S3 input to achieve efficiency.
While using Generic S3 input, it has come to our notice that, for a few set of events the fields-value parsing gets mismatched. This has been identified as the issue with the parser for Generic S3 input (AWS TA – v8.1.0) and Splunk has been informed about this, meanwhile Splunk Add-on team is working to fix this, it is recommended to use SQS-Based S3 input method.
Splunk Add-on for AWS Setup
Install
Splunk Add-on for Amazon Web Services (AWS)
on the Splunk instance from Splunkbase or Splunk Web. For more help follow the
Installation overview for the Splunk Add-on for AWS
.
Before configuring an account in Splunk, users will need an AWS account and IAM role with the
s3admin role
. Follow the documentation for more details:
Manage accounts for the Splunk Add-on for AWS
.
After configuring the IAM role, configure the Account in the Splunk Add-on.
Go to the
Configuration
Page.
In the
Account
tab, click
Add
.
Add the required information like Name, Key ID and Secret Key.
Click
Add
.
After configuring the account successfully, create a new input to collect the data from S3 bucket.
Go to the
Inputs
page.
Click
Create New Input
and select
Custom Data Type > Generic S3.
Add required information in all the required fields. For the
‘S3 Bucket’
field select the bucket that will contain the files from Netskope. For the documentation for more details:
Configure Generic S3 inputs for the Splunk Add-on for AWS
.
Update relevant sourcetype for example: netskope:web_transaction:nls for Netskope Webtx data. Refer
Sourcetype Consideration Based on the Input Configuration (Parse all files as CSV)
Section below.
For ingesting web transaction data via NLS using the sourcetype netskope:web_transaction:nls, it is recommended to keep the
“Parse all files as CSV” option disabled (unchecked)
in the Advanced Settings during input configuration. Enabling this option for web transaction data is not recommended, as it may lead to
increased Splunk license consumption
as well as it may introduce
field parsing issues.
For log types other than web transaction data, the
“Parse all files as CSV”
option can be enabled to ingest logs in JSON format.
When this option is disabled, logs are ingested in CSV format. However, additional configuration for CSV field extraction will be required depending on the selected sourcetype. It is recommended to validate the configuration outlined in the section
“Updating Field Extraction Configuration for a Sourcetype Using Splunk Web”
to ensure proper log parsing.
Sourcetype Consideration Based on the Input Configuration (Parse all files as CSV):
When
“Parse all files as CSV” = True
, refer below table:
Data Type
Sourcetype
Alerts
netskope:alert
Application
netskope:application
Connection (Page data)
netskope:connection
Endpoint
netskope:endpoint
Incident
netskope:incident
Network
netskope:network
Here, data will be in JSON format and hence, auto field extractions will take place.
When
“Parse all files as CSV” = False
, refer below table:
Data Type
Sourcetype
Web Transaction
netskope:web_transaction:nls
Alerts
netskope:alerts:nls
Application
netskope:application:nls
Connection (Page data)
netskope:connection:nls
Endpoint
netskope:endpoint:nls
Incident
netskope:incident:nls
Network
netskope:network:nls
Dashboard & Search Updates Required
Existing queries for any splunk dashboards/reports must be updated to support both legacy and new sourcetypes. For example:
sourcetype IN (“netskope:web_transaction”, “netskope:web_transaction:nls”)
It is recommended to standardize queries using wildcards where applicable:
sourcetype=”netskope:web_transaction*”
Stream Logs to Splunk with MSCS
Netskope Log Streaming supports sending log files to Splunk Add-on for Microsoft Cloud Services (MSCS). This document will help you get the data from the Azure Storage Blob to Splunk. To get the data from Azure to Splunk, there is Splunk Add-on for Microsoft Cloud Services (MSCS).
At a high level, the steps required to maintain data continuity and dashboard functionality are:
Install the Netskope Add-on for Splunk (if not already present). Learn more
here
.
Update the Netskope Add-on to the latest version (minimum v4.4.0).
Configure the MSCS Add-on Input using the standard netskope:web_transaction:nls sourcetype.
Consider updating the sourcetype stanza in case of any other custom sourcetype.
Getting Data in Splunk using Splunk Add-on for Microsoft Cloud Services (MSCS)
This approach enables direct data ingestion from Azure Storage Blobs into Splunk using the Splunk Add-on for Microsoft Cloud Services (MSCS) by leveraging Splunk’s Azure connector, data can be securely retrieved from Azure Storage Blobs and made available for analysis in Splunk.
Mandatory Requirement
: You must update the legacy
Netskope Add-on for Splunk
to the latest version. This is essential to ensure that the sourcetypes and necessary Netskope mappings are present, allowing the logs extracted by the new MSCS TA to be properly parsed by the Netskope TA for successful indexing and searches.
Getting Data using Azure Storage Blob Input
Prerequisites
Azure Storage Account. Please follow
Configure a Storage Account in Microsoft Cloud Services
for more information.
Data can be collected from Storage Blob using the
Access Key
,
Account Token
or
without using the Access Key or Token
.
Splunk Add-on for MSCS Setup
Install
Splunk Add-on for Microsoft Cloud Services
on the splunk instance from Splunkbase or Splunk Web. For more help follow the
Install the Splunk Add-on for Microsoft Cloud Services
.
Create Storage Account
Go to the
Configuration
Page
> Azure Storage Account
tab.
In the
Azure Storage Account
tab, click on Add.
Add the required information like Name, Account Name, Account Secret, Account Secret Type and Account Class Type.
Click on Add.
For more information follow
Connect to your Azure Storage Account with the Splunk Add-on for Microsoft Cloud Services
.
After configuring the storage account successfully, create a new input to collect the data from the Storage Blob.
Go to the
Inputs
page.
Click on
Create New Input
> select
Azure Storage Blob.
Add required information in all the required fields.
In the
Container Name
field, enter the name of the container that stores the blobs containing Netskope files.
In the
Blob List
field, enter a comma-separated list of blob names that contain the Netskope files.
Update relevant sourcetype for example: netskope:web_transaction:nls for Netskope Webtx data. Refer
Sourcetype Consideration Based on the Input Configuration (Parse all files as CSV)
Section below.
For ingesting web transaction data via NLS using the sourcetype netskope:web_transaction:nls, it is recommended to keep the
“Parse all files as CSV” option disabled (unchecked)
in the Advanced Settings during input configuration. Enabling this option for web transaction data is not recommended, as it may lead to
increased Splunk license consumption
as well as it may introduce
field parsing issues.
For log types other than web transaction data, the
“Parse all files as CSV”
option can be enabled to ingest logs in JSON format.
When this option is disabled, logs are ingested in CSV format. However, additional configuration for CSV field extraction will be required depending on the selected sourcetype. It is recommended to validate the configuration outlined in the section
“
Updating Field Extraction Configuration for a Sourcetype Using Splunk Web
”
to ensure proper log parsing.
For the
CSV field delimiter
parameter, specify the delimiter used in the Netskope data files.
Refer the documentation for more details:
Configure Azure Storage Blob modular inputs for the Splunk Add-on for Microsoft Cloud Services
.
Click
Add
.
Sourcetype Consideration Based on the Input Configuration (Parse all files as CSV):
When
“Parse all files as CSV” = True
, refer below table:
Data Type
Sourcetype
Alerts
netskope:alert
Application
netskope:application
Connection (Page data)
netskope:connection
Endpoint
netskope:endpoint
Incident
netskope:incident
Network
netskope:network
Here, data will be in JSON format and hence, auto field extractions will take place.
When
“Parse all files as CSV” = False
, refer below table:
Data Type
Sourcetype
Web Transaction
netskope:web_transaction:nls
Alerts
netskope:alerts:nls
Application
netskope:application:nls
Connection (Page data)
netskope:connection:nls
Endpoint
netskope:endpoint:nls
Incident
netskope:incident:nls
Network
netskope:network:nls
Dashboard & Search Updates Required
Existing queries for any splunk dashboards/reports must be updated to support both legacy and new sourcetypes. For example:
sourcetype IN (“netskope:web_transaction”, “netskope:web_transaction:nls”)
It is recommended to standardize queries using wildcards where applicable:
sourcetype=”netskope:web_transaction*”
Updating Field Extraction Configuration for a Sourcetype Using Splunk Web
Optimizing Splunk Ingestion for Netskope Log Streaming Web Transaction Logs
In this Topic
Stream Logs to Splunk

---
## Log Streaming Integrations
**URL:** https://docs.netskope.com/en/log-streaming-integrations/
**Last Modified:** 2026-02-11T21:38:48+00:00
**Scraped:** 2026-08-10T08:00:43.847060+00:00

Log Streaming Integrations - Netskope Technical Documentation
Log Streaming Integrations
Stream Logs to Crowdstrike
Stream Logs to Splunk
Stream Logs to IBM QRadar
Stream Logs to Cribl
Stream Logs to Elastic
In this Topic
Log Streaming Integrations

---
## AWS LogStreaming Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/aws-logstreaming-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:44:12+00:00
**Scraped:** 2026-08-10T08:00:51.071771+00:00

AWS LogStreaming Plugin for Log Shipper
This document explains how to configure the AWS Log Streaming v1.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to fetch the Netskope Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status), and WebTx logs from an AWS SQS queue-enabled S3 Bucket.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances) with the AWS Netskope Log Streaming service enabled.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with a 3rd-party plugin (like
Syslog
) already configured.
Amazon SQS Queue should be enabled on S3 bucket with following permissions to the IAM user. Make sure your user has admin access for the AWS account.
GetObject (Read)
GetObjectAttributes (Read)
GetQueueAttributes (Read)
GetQueueUrl (Read)
ReceiveMessage (Read)
DeleteMessage (Write)
Connectivity to a host with AWS S3 Bucket access.
AWS LogStreaming Plugin Support
This plugin is used to fetch the Netskope Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status), and WebTx logs from an AWS SQS queue-enabled S3 Bucket.
Data Type
Support
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint and Client Status)
Alerts
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content)
WebTx
Yes
CE Logs
No
Permissions
Amazon S3 bucket permissions to the IAM user to send Events, Alerts, and WebTx data to buckets.
GetObject (Read)
GetObjectAttributes (Read)
Amazon SQS Queue permissions to the IAM user to send Alerts data to Queue.
GetQueueAttributes (Read)
GetQueueUrl (Read)
ReceiveMessage (Read)
DeleteMessage (Write)
API Details
List of APIs Used
This plugin uses Python libraries to read the AWS SQS messages and then download the AWS S3 bucket data from the file object received from the SQS messages.
Library: The AWS SDK for Python (Boto3)
Usage: The AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Queue Service and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
Creating S3 the Client
s3_client = boto3.client(
"s3",
aws_access_key_id=self.aws_public_key,
aws_secret_access_key=self.aws_private_key,
aws_session_token=self.aws_session_token,
region_name=self.region_name,
config=Config(proxies=self.proxy, user_agent=self.useragent),
)
Creating SQS the Client
s3_client = boto3.client(
"sqs",
aws_access_key_id=self.aws_public_key,
aws_secret_access_key=self.aws_private_key,
aws_session_token=self.aws_session_token,
region_name=self.region_name,
config=Config(proxies=self.proxy, user_agent=self.useragent),
)
To get the SQS Queue URL
response = sqs_client.get_queue_url(QueueName=str(queue_name))
To receive messages from the SQS Queue
response = sqs_client.receive_message(
     QueueUrl=queue_url,
     MaxNumberOfMessages=1,
     WaitTimeSeconds=2,
     MessageAttributeNames=["All"],
)
Performance Matrix
This performance reading is for a Large Stack CE tested with these VM specifications. These readings are added with the following data considerations:
50 MB compressed ~500MB uncompressed (~500k) Alerts/Events in ~3.3 minutes
50 MB compressed ~500MB uncompressed (~500k) WebTx logs in ~2.5 minutes
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts-Events pull and ingested to third-party SIEM
~150K EPM
WebTx pull and ingested to third-party SIEM
~200K EPM
User Agent
APN/1.1 (ahq9d89xj9gspapczzdb59goq)
Workflow
Generate credentials for AWS Netskope LogStreaming authentication methods
Configure CLS AWS Netskope LogStreaming Plugin
Add Business Rules
Add a SIEM Mapping
Validate the plugin
Watch a Video
Click play to watch a video:
Configure the Queue with Amazon S3 Buckets
To configure the plugin, you will need to configure one queue with an Amazon S3 bucket:
Log in to your AWS account and go to
Amazon S3 > Buckets
to find your configured buckets.
Click on any of the buckets and go to
Properties > Event Notifications
.
From here create event notifications to ingest the data from the specified folder in the S3 bucket to the configured SQS Queue.
And from
Amazon SQS > Queues
, you can find your configured queues.
Create a AWS Netskope LogStreaming Policy
Search for
IAM
in the search box and from the left panel and click
Policies
.
Click
Create policy
.
On the JSON tab, enter this policy. Click
Next:Tags
, and then click
Next:Review
.
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": [
"s3:GetObject",
"s3:GetObjectAttributes"
],
"Resource": [
"arn:aws:s3:::*/*",
"arn:aws:s3:*:932414340604:accesspoint/*"
]
},
{
"Sid": "VisualEditor1",
"Effect": "Allow",
"Action": [
"sqs:DeleteMessage",
"sqs:GetQueueUrl",
"sqs:ReceiveMessage",
"sqs:GetQueueAttributes"
],
"Resource": "*"
}
]
}
Note
Make sure to update your AWS account ID in the above policy template.
Enter a Name and click
Create Policy
.
Attach this policy to the user. Go to
IAM > Users
and select the user for which you want to attach a policy. Click
Add permissions
and click the
Add permissions
option:
Select
Attach policies directly
under Permissions options, and then search for and select the policy created in the previous step for the source queue.
Click
Next
, and then click
Add permissions
. The Policy will be attached to the user.
Plugin Authentication Methods
IAM Role Anywhere Configuration
Prerequisites
The AWS Certificate Manager service needs to be enabled to authenticate the plugin using the AWS IAM Roles Anywhere authentication method.
Make sure you create the Private Certificate Authority, Trust Anchor, and Profile in the same region in which your AWS SQS Queue resides.
Create a Policy
This Policy contains the required permissions for creating Private CA Certificate (including Permissions for creating Trust Anchor and Profile) and using the IAM Roles Anywhere.
Go to
Policy Generator
and select
IAM Policy
as the policy type. Enter Add Statement details, and then generate the policy.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Private Certificate Authority
Actions:
CreateCertificateAuthority
DescribeCertificateAuthority
GetCertificate
GetCertificateAuthorityCertificate
GetCertificateAuthorityCsr
ImportCertificateAuthorityCertificate
IssueCertificate
ListCertificateAuthorities
ARN: *
Click
Add Statement
.
Scroll back up to add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management (IAM)
Actions:
AttachRolePolicy
CreateAccessKey
CreateRole
DeleteRole
PassRole
ARN: *
Click
Add Statement
.
Scroll back up to add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Certificate Manager
Actions:
DescribeCertificate
ExportCertificate
GetCertificate
ListCertificates
ListTagsForCertificate
RequestCertificate
ARN: *
Click
Add Statement
.
Scroll back up to add another statement.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management Roles Anywhere
Actions:
CreateProfile
CreateTrustAnchor
GetProfile
GetTrustAnchor
ListProfiles
ListTrustAnchors
ARN: *
Click
Add Statement
.
Click
Generate Policy
.
Copy the Policy as it will be used in the next step for creating the policy required for creating the Private CA certificates.
Go to AWS Console and select
IAM
from
All Services
. Click
Policies
in the left panel, and then click
Create Policy
.
Copy the policy to the JSON tab, click
Next:Tags
, and then click
Next:Review
.
Enter a name (like
netskope-ce-rolesAnywhere-policy
) and click
Save Changes
.
Create a Private Certificate Authority
Log in to the AWS Console.
Search for
Certificate Manager
.
Click
AWS Private CA
.
Click
Create a private CA
.
For
Mode Options
, select
General-purpose
.
For
CA type options
, select
Root
.
Enter the
Organization (O)
.
For
Key algorithm options
, select
RSA 2048
.
Add tags if any (optional).
Check the checkbox in the
CA permissions options
section.
Check the checkbox in the
Pricing
section.
Click
Create
to create the CA certificate.
From
Actions
, select
Install CA Certificate
.
Click
Confirm and Install
.
Create a Trust Anchor
Search for the
IAM
service, go to
Roles
under Access Management and then scroll down to Roles Anywhere and select
Manage
.
Click
Create a Trust anchor
.
Enter a Trust anchor name, like
netskope-ce-aws-verified-trust-anchor
.
Select
AWS Certificate Manager Private CA
(created in the previous steps) as a Certificate authority (CA) source. Select the Certificate that was created in the previous step in AWS Private Certificate Authority.
Add tags if required.
Click
Create a trust anchor
.
Click on the created
Trust Anchor
and copy the Trust Anchor ARN.
Create an IAM Role
Go to
IAM services
in the AWS Console.
Click
Roles
under the Access Management
Click
Create Role
.
In the Trusted entity type, select
Custom Trust Policy
.
Replace the Custom trust Policy with this Trust Policy. This policy contains the permissions for using the roles anywhere service:
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": [
"rolesanywhere.amazonaws.com"
]
},
"Action": [
"sts:AssumeRole",
"sts:TagSession",
"sts:SetSourceIdentity"
]
}
]
}
Click
Next
.
In the Permissions policies, select the policy created previously in
Create a SQS Queue Policy
.
Click
Next
.
Provide a Role name (like
AWS-SQS-Role
) and a Description for the role.
Click
Create role
. Search for the created role and click on the Role Name.
Make a note of the Role ARN because this will be required in the Plugin configuration parameter
Role ARN
for the authentication method
AWS IAM Roles Anywhere
.
Create a Profile
Go to
IAM services
in the AWS Console.
Select
Roles
under Access management.
Scroll down to Roles Anywhere and click
Manage
.
Expand the Setup steps.
Click
Step 2: Configure roles
.
Click
Configure a profile
.
Enter a Profile name, like
AWS-SQS-Profile
.
Select the role created in
Create IAM Role
.
Remove the
Inline Policy
.
Click
Create a profile
.
Select the created
Profile
and copy the
Profile ARN
.
Go to
AWS Certificate Manager > Request certificate
.
Select
Request a private certificate
.
Click
Next
.
Select the Certificate authority created in the previous step.
Provide a domain name in the Fully qualified domain name field, like
netskope-ce-verified-access.com
.
Select
RSA 2048
as the Key algorithm.
Add tags if required.
Acknowledge the Certificate renewal permissions.
Click
Request
.
Go to
List certificates
from the navigation pane of AWS Certificate Manager.
Select the certificate created previously.
Click
Export
.
Enter a passphrase
.
Make a note of the passphrase as it will be required for the Configuration of the AWS S3 Plugin using the
AWS IAM Roles Anywhere
Authentication method.
Click
Generate PEM Encoding
.
Download all the Certificates because these won’t be visible again. For new certificates, you will need to Export them again.
The Certificate body, Certificate Private Key will be required for the Configuration of the AWS Verified Access Plugin using the
AWS IAM Roles Anywhere
authentication method. For more info, go to
AWS IAM Role Anywhere
.
Deployed on AWS Authentication
Create a Role
Go to
IAM
services in the AWS Console.
Click
Create role
.
Select the
AWS Service
.
Under Use case, select
EC2
.
Click
Next
.
Select the permission policy created in
Create a SQS Queue Policy
.
Click
Next
.
Enter a Role Name (like
netskope-ce-instance-role
) and Description.
Click
Create Role
.
Assign a Role to an EC2 Instance
Log in to your EC2 instance console.
Click
Instances
under
Instances
.
Go to
Action > Security > Modify IAM Role
.
Select the Role that you created above in
Create a Role
. (
netskope-ce-instance-role
).
Click
Add IAM Role
or
Modify IAM Role
. Note that both EC2 instance and Queue should be on the same region.
Assign a Role to a K8s Instance
Open your Role created for ServiceAccount while creating K8s instance.
Attach the policy created in
Create a SQS Queue Policy
.
Configure the AWS LogStreaming Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
AWS Netskope LogStreaming v1.0.0 (CLS)
plugin box.
Enter a Configuration Name and
set the pull interval per your requirements.
Click
Next
and enter the Configuration parameters:
Authentication Method:
Select the method to be used for AWS client authentication.
Private Key:
Private Key for decrypting the AWS Private CA Certificate. Required for the AWS IAM Roles Anywhere authentication type.
Certificate Body:
Certificate Body for AWS Public/Private CA Certificate. Required for the AWS IAM Roles Anywhere authentication type.
Password Phrase:
Password Phrase for decrypting the CA Certificate. Required for the AWS IAM Roles Anywhere authentication type.
Profile ARN:
AWS Profile ARN for AWS client authentication. Required for the AWS IAM Roles Anywhere authentication type.
Role ARN:
AWS Role ARN for AWS client authentication. Required for the AWS IAM Roles Anywhere authentication type.
Trust Anchor ARN:
AWS Trust Anchor ARN for AWS client authentication. Required for the AWS IAM Roles Anywhere authentication type.
AWS Region Name
: AWS Region Name in which the SQS queue enabled S3 bucket is set up. Make sure that the region name matches the region in the Profile ARN and Trust Anchor ARN if you have selected the authentication method as AWS IAM Roles Anywhere.
AWS SQS Queue Name:
AWS SQS Queue Name with which the S3 bucket is set up. To get more details, go to
AWS > SQS > QueueName
. Make sure that the provided queue is pre-configured on your AWS instance. A new queue will not be created if the provided queue does not exist.
Note
AWS Region Name
and
AWS SQS Queue Name
are the only required fields for the Deployed on AWS authentication method.
Click
Save
. Your Plugin configuration will be available at
Log Shipper > Plugins
.
Note
We have configured the SYSLOG with Splunk plugin to ingest the pulled data from the AWS Netskope LogStreaming plugin.
Configure a Log Shipper Business Rule for AWS LogStreaming
In Log Shipper, go to
Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Configure Log Shipper SIEM Mappings for AWS LogStreaming
Go to
SIEM Mappings
and click
Add SIEM Mapping
.
Select the Source plugin (CLS AWS Netskope LogStreaming), a Destination plugin, and a business rule, and then click
Save
.
After the SIEM mapping is added, data will start to be pulled from the AWS Netskope LogStreaming tenant, transformed, and ingested into the 3rd-party SIEM platform.
Validate the AWS LogStreaming Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant, go to
Logging
in Cloud Exchange and search for the pulled logs with the filter
message contains pulled
.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested events/alerts with the filter
message contains ingested
, or you can also use the destination plugin name as the filter.
Troubleshooting the AWS LogStreaming Plugin
Facing issues while fetching Alerts/Events or WebTx data from the configured Queue
If you have configured AWS Netskope LogStreaming plugin and 3rd-party SIEM platform successfully and still you are getting error after configuring SIEM Mapping for the plugin, it can be due to one of these reasons:
You do not have access to the configured Queue.
The permissions provided to IAM User are insufficient.
All alerts/events/webtx data are consumed and nothing is available to pull from the queue.
The provided queue in the plugin might not be enabled in the S3 bucket.
What to do:
Verify if the Queue is available on the AWS SQS service.
Verify that IAM User has provided sufficient permissions provided. For the minimum permissions, you can refer to
Permissions
.
Verify that you have data to consume from the queue, for that you have to go to
Amazon SQS > Queues.
To verify the enabled queue in the S3 bucket, follow the steps mentioned in
Configure the
Queue
with Amazon S3 Buckets
.
Facing issues while configuring the new plugin
If you’re creating a new plugin with AWS IAM Roles Anywhere and get an error like:
What to do
:
After expanding the logger, you will see
At least one of the Trust Anchor ARN, Role ARN, and Profile ARN has a different account ID
, so you need to check that the provided parameters are generated from the same account and have the same region.
Data getting skipped while pulling through AWS Netskope LogStreaming Plugin
You might be facing this issue due to one of the following reasons:
Invalid file or file having invalid data
For Alerts/Events, alert_type and record_type are required fields and for WebTx, x-cs-timestamp is the required field. If the data does not have following fields then it will be skipped.
What to do
: Validate your file is valid and has valid data. Also, validate that the data contains the required fields. For Alerts/Events,
alert_type
and
record_type
are required fields; for WebTx,
x-cs-timestamp
is the required field.
Known Behaviors
If you have RBACv3 enabled in your Netskope tenant, you will not be able to use the Netskope LogStreaming services.
If you restart Netskope Cloud Exchange, or due to some reason your Netskope Cloud Exchange restarts automatically, while the AWS NLS plugin is running, then the pull task may get stuck in progress. To fix this, you can reconfigure the SIEM mapping to start the pulling again.
In this Topic
AWS LogStreaming Plugin for Log Shipper

---
## Azure Netskope Log Streaming Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/azure-logstreaming-plugin-for-log-shipper/
**Last Modified:** 2026-07-06T19:52:46+00:00
**Scraped:** 2026-08-10T08:01:18.380552+00:00

Azure Netskope Log Streaming Plugin for Log Shipper
Release Notes
1.0.1 (Minimum required CE version 5.1.2)
Changed
Updated handling for field filtering.
1.0.0
Added
Initial release.
This document explains how to configure the Azure Netskope LogStreaming v1.0.1 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to pull the Netskope Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status) and WebTx data from the Azure Containers using Storage Queue of Microsoft Azure Storage Account.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange instance with the
Tenant plugin
and
Log Shipper plugin
already configured.
Azure Netskope LogStreaming service enabled in Netskope Tenant.
A 3rd-party plugin (like
Syslog
) already configured.
Standard tier subscription which has Storage accounts service.
Connectivity to the following hosts:
https://portal.azure.com/
For more information about Storage account refer to this
documentation
.
Azure LogStreaming Plugin Support
This plugin is used to pull the Netskope Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status) and WebTx data from the Azure Containers using Storage Queue of Microsoft Azure Storage Account.
Data Type
Support
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident and Client Status)
Alerts
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, and Content)
WebTx
Yes
CE Logs
No
Mappings
The current Syslog plugin does not have a mapping file for Azure Netskope LogStreaming alerts, events and WebTx, users need to add a custom mapping file to transform these alerts, events and WebTx data. Using this mapping file the one can ingest the data in JSON format.
Sample Mapping file:
{
  "delimiter": "|",
  "syslog_map_version": "3.2.0",
  "cef_version": "0",
  "validator": "valid_extensions.csv",
  "taxonomy": {
    "json": {
      "alerts": {
        "dlp": [],
        "malware": [],
        "policy": [],
        "Compromised Credential": [],
        "Malsite": [],
        "Quarantine": [],
        "Remediation": [],
        "Security Assessment": [],
        "Watchlist": [],
        "uba": [],
        "ctep": [],
        "content": [],
        "device": []
      },
      "events": {
        "application": [],
        "audit": [],
        "infrastructure": [],
        "page": [],
        "network": [],
        "incident": [],
        "clientstatus": []
      },
      "webtx": {
        "v2": []
      }
    }
  }
}
Permissions
Here are the permissions needed for your azure account, if you are creating your own azure blob storage, make sure you have permissions to create and manage storage accounts and resource groups.
Storage Account Contributor:
To create, delete, and manage the storage account itself, including networking and access keys.
Storage Blob Data Contributor:
To perform data operations on Blobs (upload, download, delete).
Storage Queue Data Contributor:
To manage the queue messages (add, read, delete).
EventGrid Contributor:
Necessary to create the System Topic (on the storage account) and the Event Subscription.
API Details
This plugin uses Python libraries for fetching Netskope Alerts, Events and Webtx logs from the containers configured in the Microsoft Azure Storage Account.
Usage: The azure-storage-queue and azure-storage-blob libraries are part of the Azure SDK for Python, enabling interaction with Azure Storage services. azure-storage-queue is used to send, receive, and manage messages in queues, supporting decoupled and event-driven architectures. azure-storage-blob allows uploading, downloading, and managing files in Azure Blob Storage. Together, they are commonly used in workflows where blob uploads trigger processing events via queue messages.
Initialize Blob Service Client
Creates a client to interact with the Azure Blob Storage account using the connection string.
blob_service_client = BlobServiceClient.from_connection_string(
       conn_str=connection_string, user_agent=self._get_user_agent()
)
Initialize Queue Client
Creates a client to connect to the specified Azure Storage Queue using the provided connection string.
queue_client = QueueClient.from_connection_string(
    conn_str=connection_string,
    queue_name=queue_name,
    user_agent=self._get_user_agent(),
)
Initialize Queue Service Client
Creates a client to interact with the Azure Storage Queue service, allowing operations like listing queues within the storage account.
queue_service = QueueServiceClient.from_connection_string(
    conn_str=connection_string, user_agent=self._get_user_agent()
)
Receive Messages from a Queue
Retrieves a batch of messages from the Azure Storage Queue that are currently visible and available for processing.
messages = queue_client.receive_messages(
    messages_per_page=20, visibility_timeout=3000
)
Delete Messages from a Queue
Permanently removes a specific message from the Azure Storage Queue using its message ID and pop receipt.
queue_client.delete_message(
    message=msg.id,
    pop_receipt=msg.pop_receipt,
)
Performance Matrix
This performance reading is for a Cloud Exchange Large Stack tested on these VM specifications. These readings are added with the following data considerations:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts-Events pull
~200 EPM
Alerts-Events pull and ingested to a Log Shipper 3rd-party plugin
~180K EPM
WebTx pull
~200K EPM
WebTx pull and ingested to a Log Shipper 3rd-party plugin
~165K EPM
User Agent
netskope-ce-6.1.0-cls-azure-netskope-logstreaming-v1.0.1
Workflow
Generate credentials for Azure Netskope Log Streaming plugin.
Configure the Azure Netskope Log Streaming Plugin.
Configure a Business Rule.
Configure Log Delivery.
Validate the plugin.
Watch a Video
Click play to watch a video:
Generate Azure Netskope Log Streaming Credentials
To configure the Azure Netskope LogStreaming Plugin, you need to configure a queue in a Storage Account.
To configure a Storage Account:
Log in to your Microsoft Azure instance, and search for the Storage Account service.
Click on it, and if you have already configured any storage account, it will list on that page.
To configure a new Storage Account, click
Create
.
Provide all the required information and click on
Review + create
.
After successfully creating the storage account, go to
{storage_account} > Security + networking > Access keys
, and copy the connection string and use it in the plugin.
Now create a container and a queue. Go to
Data storage > Containers
and click
Add container.
Provide a name for the container, and click
Create.
Your container will be listed on that page.
To configure the queue, go to
Data storage > Queues
, click
+Queue
, provide a name for the queue, and then click
OK.
After configuring these, you need to create an Event Subscription for the queue. Go to
{storage_account} > Events
.
Click
+Event subscription
, provide all the details, and click
Create
. Provide a Name and System topic Name, set Event Schema as
Event Grid Schema
, and Filter to Event Types as
Blob Created
.
Configure the Endpoint with the storage account and queue that you just created.
Click
Create
.
The configuration is completed. When you have some valid files available in the container, the plugin will fetch the data from that file and ingest it to a Log Shipper 3rd-party plugin platform.
Note
This will trigger an event anytime a blob is created in any directory. To trigger an event when a blob is created in a specific directory, you need to enable
Enable subject filtering
and add that specific directory path in the filter option. Example:
Configure Log Streaming on Netskope Tenant
Log in to Netskope Tenant, and click
Settings
.
In Settings, go to
Tools > Log Streaming
.
Click
Create Stream
.
Provide these parameters:
Name:
Enter the name for the stream.
Data Collections:
If you want to stream Transaction logs to your cloud bucket, select the Transaction events checkbox. Otherwise, It will only stream Alerts and Events to your cloud bucket.
Note
Make sure to select Parser order 2, if you will be using it with Syslog v4.1.2 plugin, because the default mapping for Syslog v4.1.2 is compatible with Parser order 2.
Make sure the x-cs-timestamp field is enabled as Cloud Exchange uses this field for identifying the WebTx data.
Destination:
Select the destination for streaming and provide the information about the destination. Enter the Storage Account Name, Container Name, Path, and Access Key for your Azure container.
Compression:
Select the compression type you want.
Click
Save.
Configure the Azure Netskope LogStreaming Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Azure Netskope LogStreaming v1.0.1 (CLS)
plugin.
Enter the
Configuration Name
and
Pull Interval
for the plugin.
Click
Next
and enter the Configuration Parameters:
Microsoft Azure Storage Account Connection String:
The Microsoft Azure Storage Account Access Key Connection String created previously.
Microsoft Azure Data Storage Queue Name:
The Microsoft Azure Data Storage Queue Name for the Event Subscription created previously. Make sure that the provided queue is preconfigured in your Microsoft Azure Storage Account. A new queue will not be created if the provided queue does not exist.
Click
Save
. Plugin configuration will be available on the
Log Shipper > Plugins
page.
You need to have 3rd-party Log Shipper plugin, like
Syslog with Splunk plugin
, already configured to ingest the pulled data from the Azure Netskope LogStreaming plugin.
Configure a Log Shipper Business Rule for Azure Log Streaming
In Log Shipper, go to
Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific types of alerts or events, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Click
Save
.
Configure Log Shipper Log Delivery for Azure LogStreaming
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (CLS Azure Netskope LogStreaming), Destination plugin (like Syslog), select and business rule, and then click
Save
.
After Log Delivery is configured, the data will start to be pulled from the Azure Netskope LogStreaming tenant, transformed, and ingested into the 3rd-party plugin platform.
Validate the Azure LogStreaming Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant:
In Cloud Exchange, go to
Logging
and search for the pulled logs with the filter
“message contains pulled”
.
Validate the Push
To validate the push in Cloud Exchange:
Go to
Logging
and Search for ingested events with the filter
“message contains ingested”
.
The ingested logs will be filtered.
To view ingested data on Splunk (for example), search for ingested data using the TCP port and Log source identifier used while configuring the Log Shipper Syslog plugin.
Troubleshooting the Azure Netskope LogStreaming Plugin
Facing issues while configuring the new plugin
If you’re creating a new plugin and get this error, it may indicate that the queue name specified in the configuration does not exist in the Microsoft Azure Storage Account associated with the provided connection string
What to do:
Provide a valid Queue name for Storage Account associated with the provided connection string.
Facing issues while fetching Alerts/Events or WebTx data from the configured Queue
If you have configured Azure Netskope LogStreaming plugin and a 3rd-party plugin platform successfully, and you still get no messages after configuring Log Delivery for the plugin, it may be due to all the alerts/events/webtx data is being consumed and there is nothing available to pull from the queue.
What to do:
Verify that you have data to consume from the queue. Go to
{Storage_account} > Data Storage > Queues >
{Queue}.
Facing issues while transforming pulled events
After successfully pulling events from Azure Netskope LogStreaming plugin, while transforming the events, you are not able to transform the events. The root cause for this could be that the event type for which the error is received is not added into the mapping file.
What to do:
Make sure you have use the mapping file provided above for ingesting events, alerts and WebTx data in JSON format.
Facing issues while using plugin with proxy
If you are using the proxy server, and configuring the plugin with proxy, you might face this error:
This may be due to the proxy server being deployed on the local instance, and you are using the plugin on a cloud instance.
What to do:
Deploy your proxy server on a cloud instance instead of using a local instance.
Known Behavior
If you have RBACv3 enabled in your Netskope tenant, you will not be able to use the Netskope LogStreaming services.
Limitation
This plugin is only supported on Cloud Exchange deployed on a Cloud instance.
In this Topic
Azure Netskope Log Streaming Plugin for Log Shipper

---
## Review Custom Query Logs in DSPM
**URL:** https://docs.netskope.com/en/review-custom-query-logs-in-dspm/
**Last Modified:** 2026-03-01T00:02:46+00:00
**Scraped:** 2026-08-10T08:01:30.768761+00:00

Review Custom Query Logs in DSPM - Netskope Technical Documentation
Review Custom Query Logs in DSPM
Overview
For Data Stores that don’t provide native query logs, you can supply the Netskope DSPM application with custom query logs to take advantage of our Data-in-Use Monitoring capability. By supplying Netskope DSPM with custom query logs saved in a S3 bucket, you now have the flexibility to:
Onboard and connect a new S3 Account
if your query logs do not reside in the same account as your Data Stores.
Configure the indices or keys
in any order and provide Netskope DSPM with the necessary CSV/JSON mapping.
Prerequisites:
Access to the S3 bucket(s) is required for Netskope DSPM to ingest the custom query logs.  You would need to create a custom IAM policy for the same and attach it to the IAM role that has been created and assigned to your Netskope DSPM instance.
Instructions
Create IAM Policy for S3 Buckets
Open
IAM Console
and navigate to
Policies
section under Access Management section on the left menu bar. Click on the
Create Policy
button and move to the
JSON
tab as shown below.
Replace the entire
Line 3
i.e. “Statement”: [] with the contents as below
"Statement": [
  {
   "Effect": "Allow",
   "Action": [
			"s3:GetBucketTagging",
			"s3:ListBucketVersions",
			"s3:GetBucketLogging",
			"s3:ListBucket",
			"s3:GetAccelerateConfiguration",
			"s3:GetBucketVersioning",
			"s3:GetBucketAcl",
			"s3:GetBucketNotification",
			"s3:GetObject",
			"s3:GetBucketCORS",
			"s3:GetObjectTagging",
			"s3:GetBucketLocation",
			"s3:GetObjectVersion"
			],
			"Resource": [
				"arn:aws:s3:::bucket_name/*",
				"arn:aws:s3:::bucket_name"
			]
		}
	]
Replace bucket_name in the JSON section with the actual name of the S3 bucket that would contain the custom query log files.
3. on
Next
twice and in the
Review Policy
page provide the inputs as below and then click
Create Policy
Attach Policy to the Netskope DSPM Role
Click to navigate
to the Role section in IAM Console and search for
Netskope One DSPMRole
in the search box on the right. Click the hyperlink to move to the Permissions tab of
Netskope One DSPMRole.
Click
Add Permissions
button and select
Attach policies
In the next page in the search box type
Netskope One DSPM_S3-QueryLogs ,
select the radio button and click
Attach Policies
.
Here are samples of how a custom query log file may appear:
CSV Format
JSON Format
"alice","dev","SELECT * FROM users","2021-05-20 00:00:15.67","public","200"
"bob","dev","SELECT * FROM users LIMIT 50","2021-05-20 00:01:20.05",,
"charlie","dev","SELECT * FROM users WHERE firstname = 'Robert'","2021-05-20 00:03:25.05",,
"daniel","dev","SELECT\n""firstname"",\n""lastname""\nFROM ""users""","2021-05-20 00:05:40.59",,
{"username":"alice","database":"dev","query":"SELECT * FROM users","timestamp":"2021-05-23 00:00:15.67","schema":"public","rows":305}
{"username":"bob","database":"dev","query":"SELECT * FROM USERS LIMIT 123","timestamp":"2021-05-23 00:01:20.53"}
{"username":"charlie","database":"dev","query":"SELECT *  FROM users","timestamp":"2021-05-23 00:05:15.67"}
Follow the instructions in the next section to map your requisite query log format in Netskope DSPM.
Mapping Custom Query Logs Within Netskope DSPM
While connecting to the Data Stores in the
Select Capabilities
tab you can specify the following inputs after selecting
Custom Query Log
option under the
Data-in-use monitoring
section. Based on the Netskope DSPM capability to support for the Data Store the option for Data-in use monitoring would be enabled/disabled.
Field
Value
Highlight Color
Illustration
Select the Log format
CSV
Black
S3 Bucket
Provide the S3 bucket name where your query logs resides or will reside. Make sure that you have provided the requite IAM permissions for Netskope DSPM to access
Blue
Select Account (Existing)
Select from the dropdown list the appropriate AWS account where the S3 bucket containing the query logs resides
Green
Select Account (New S3 Account)
Use this option to connect to a new AWS account if the query logs are not stored in the same project as the Data Store you are connecting to
Purple
Prefix
Optional
None
Refer to the following illustration to help mapping the custom query log index or key values to the correct Netskope DSPM fields.
Highlight Color
Log Format
Mapping By
Example Mapping Index
Blue
CSV
Index position
Red
JSON
Key position
Once the mapping is successful you will receive a message highlighted in green accordingly as shown below:
Highlight text color
Log Format
Example
Green
CSV
Index position
Green
JSON
Key position
Press the
Continue
button to onboard the Data Store. Once the onboarding is completed you can visit the
Privilege Analysis
menu section and start to analyze the queries fired by the DB users connecting to the Data Store.
In this Topic
Review Custom Query Logs in DSPM

---
## View DSPM Activity Logs
**URL:** https://docs.netskope.com/en/view-dspm-activity-logs/
**Last Modified:** 2026-02-05T19:41:07+00:00
**Scraped:** 2026-08-10T08:02:14.869943+00:00

View DSPM Activity Logs - Netskope Technical Documentation
View DSPM Activity Logs
Overview
Netskope One DSPM’s Activity Logs is a recorded history of all important user and system activities, including record changes (creation, edits, and deletion) and actions initiated. Platform users can review, filter, and export this history for use in their security & compliance-related duties.
Accessing Activity Logs
Platform users with the necessary permission can access Activity Logs via the following steps:
Log into the Netskope One DSPM platform.
Navigate to
Administration > Activity Logs
.
The
Activity Logs screen
is displayed.
The Activity Logs screen is divided into three tabs, each recording different types of information. See below for details on using each specific tab.
User Activity Tab
The
User Activity tab
is a record of user-initiated actions & record changes. Examples of user activity include:
Creation, updates, and deletion of all records
User activities, such as Data Store discovery, etc.
When you visit the tab, a table is displayed with the following information:
Column Name
Details
Date/Time (UTC)
Timestamp representing when the activity occurred
Type
Nature of the activity. Possible values include: Create, Read, Update, Delete
Username
Netskope Administrator name who performed the activity
Note:
For legacy Dasera customers, this field may also contain the Platform User Name as well.”
Resource
Area of the platform where the activity occurred. Possible values (and the areas they cover) include:
– Administration
– Authentication
– Alert
– Classification
– Data Store
– Data Tag
– Licensing
– Platform Settings
– Policy
– Task
– User Identity
Description
Details of the activity. Hover over truncated values to view the entire content.
When available, this will include a unique identifier for named records such as Classification Field, Policy Name, etc
Actions
Click the
View icon
to display the activity record in a dedicated modal to assist with readability and printing.
Netskope One DSPM offers the following methods for narrowing the on-screen display of records:
Enter a text string that matches against any field.
Click on the Filter dropdown to filter by one-or-more values of specific fields.
If you wish to review the displayed records offline, click the
CSV Export icon
to generate a comma-separated values (CSV) file, which you can then research within separate tools such as Microsoft Excel and Google Sheets.
System Activity Tab
The
System Activity tab
is a record of platform-initiated actions. Examples of system activity include:
Discovery of new assets, such as Infrastructure Accounts, Data Stores, etc.
Scan failures
When you visit the tab, a table is displayed with the following information:
Column Name
Details
Date/Time (UTC)
Timestamp representing when the activity occurred
Type
Nature of the activity. Possible values include: Error, Fatal, Info, Warning, Scan
Notification
Details of the activity. Hover over truncated values to view the entire content.
Actions
Bold rows represent unread system activity records. For unread records, click the
Notification Read
icon to acknowledge the record. The icon will be replaced by a
Notification Unread
icon; click this to reverse any acknowledgement.
Netskope One DSPM offers the following methods for narrowing the on-screen display of records:
Enter a text string that matches against any field.
Click on the Filter dropdown to filter by one-or-more values of specific fields.
If you wish to review the displayed records offline, click the CSV Export icon to generate a comma-separated values (CSV) file, which you can then analyze using tools such as Microsoft Excel and Google Sheets.
Scan Activity Tab
The
Scan Activity tab
is a record of all scheduled and manual data store scan activity. Examples of scan activity include:
Completed scans
Aborted scans
Failed scan
When you visit the tab, a table is displayed with the following information:
Column Name
Details
Date/Time (UTC)
Timestamp representing when the activity occurred.
Type
Scheduled:
resulting from a scan frequency
Manual:
user-initiated scan.
Data Store
Name of the affected data store. Hyperlink to the overview in Data Store Inventory.
Sidecar Pool Name
Sidecar pool associated with the data store. Hyperlink to the Sidecar Administration screen. Blank if none.
Sidecar Name
Sidecar that scanned this data store. Blank if none.
Description
Details of the scan. Hover over truncated values to view the entire content.
Scan Result
Fail, Complete, or Aborted.
Netskope One DSPM offers the following methods for narrowing the on-screen display of records:
Enter a text string that matches against any field
Click on the Filter dropdown to filter by one-or-more values of specific fields.
If you wish to review the displayed records offline, click the
CSV Export icon
to generate a comma-separated values (CSV) file, which you can then research within separate tools such as Microsoft Excel and Google Sheets.
In this Topic
View DSPM Activity Logs

---
## Audit Log
**URL:** https://docs.netskope.com/en/audit-log-1/
**Last Modified:** 2025-08-31T01:38:34+00:00
**Scraped:** 2026-08-10T08:02:57.766137+00:00

Audit Log - Netskope Technical Documentation
Audit Log
Home
>
Settings
>
Administration
>
Audit Log
The audit log is a log of the critical activities done by the admin through the Netskope UI. This log will help you track the activities done in the Netskope UI.
You need administrative privilege to view the Audit Log.
The audit log contains the following information:
The date and time that an activity happened.
The email address of the admin who performed the activity.
The severity level of the activity.
The additional activity details.
Filters
About Filters
The filters allow you to search the log for activities based on severity, log type, and whether or not the user is Netskope personnel.
The following is a comprehensive list of all the filter menu options for the Audit Log:
Severity
Severity Levels:
High
Medium
Low
Info
Log Type
Log Types:
Access Denied
Login Failed
SSO Login Failed
Logout Successful
Admin logged out because of successive login failures
Login Successful
SSO Login Successful
Password Change Failed Attempt
Password Change Successful
Created new admin
Added SSO Admin
Edited SSO Admin Record
Created new support admin
Edit admin record
Deleted admin
Enabled admin
Disabled admin
Unlocked admin
Updated admin settings
Enabled Netskope Support SSO
Disabled Netskope Support SSO
Deleted Netskope SSO admin
SSO Login Successful by Netskope Support
SSO Login Failed by Netskope Support
Resend Verification Email
Reset password
Request OTP for Account Verification
Account activation link validation failed
OTP validation failed
Account Verification Successful
Created new inline policy
Edited inline policy
Deleted inline policy
Pushed inline policy
Set dedicated egress ip policy
Created new rbi template
Edited rbi template
Deleted rbi template
Pushed rbi template
Update default actions for inline policies
Pushed tunnel groups
Created new tunnel group
Edited tunnel group
Deleted tunnel group
Applied Phoenix policy record(s)
Created new introspection policy
Edit introspection policy record
Deleted introspection policy
Pushed Introspection policies
Created retro scan
Next Gen CASB API quarantine profile created
Next Gen CASB API quarantine profile edited
Next Gen CASB API quarantine profile deleted
Next Gen CASB API LH profile created
Next Gen CASB API LH profile edited
Next Gen CASB API LH profile deleted
Next Gen CASB API instance created
Next Gen CASB API instance updated
Next Gen CASB API instance deleted
Created a new Next Gen CASB API policy
Edited Next Gen CASB API policy
Deleted Next Gen CASB API policy
Pushed Next Gen CASB API policies
Next Gen CASB API pdf report downloaded
Next Gen CASB API pdf report emailed
Next Gen CASB API pdf report scheduled
Next Gen CASB API inventory exported
Next Gen CASB API retroscan created
Next Gen CASB API retroscan edited
Next Gen CASB API retroscan deleted
Next Gen CASB API retroscan paused
Next Gen CASB API retroscan stopped
Netskope Personnel
Netskope Personnel:
Yes
No
Date Range Filter
You can also use the date range filter to view the activities that occurred within a specific date range.
To use the date range filter:
Click the date range filter button in the top-right corner of the
Audit Log
page to view the date range menu.
The default setting is
Last 7 Days
.
Select from the standard date range options, or click
Date Range
on the bottom of the menu to select a customized date range.
Your selection will be applied instantly if you select from the standard date range options. If you want to view your customized date range selections, you must click the
APPLY
button.
Save Filters
You can save your preferred filter selections. To save your filter selections:
Open the drop-down filter menu by clicking the
button.
Select your filters.
Click the
Save Filter
icon to open the Save Filters window.
Enter a name for your saved filters in the
Enter Filter Name
field.
Click the
SAVE
button to save your filter selections.
Manage and View Saved Filters
To view your saved filters:
Click the
FILTERS
button to open the saved filters menu.
Click a saved filter to view it.
To manage saved filters:
Click the
FILTERS
button to open the saved filters menu.
Click the
MANAGE SAVED FILTERS
button.
Manage your saved filters by:
Click the pencil icon to change the name of the saved filters.
Click the share icon to share the saved filters with others.
Click the trashcan icon to delete the saved filters.
Export
You can export data from the audit log. To export:
Click the
EXPORT
button to open the Export menu.
Choose the columns to export.
Choose the number of rows to export.
Select the export name.
Click the
EXPORT
button to export the data.
Customize Columns
You can customize the columns to enable or disable the following columns:
User
Severity
Activity
To customize columns:
Click the
gear icon to open the
Customize Columns
menu.
Disable or enable columns:
Disable
: Uncheck the box next to the associated column’s name. When a box is empty, without a checkmark, the column is disabled.
Enable
: Click the empty box to add a check-mark. A column is enabled when the box next to the column’s name is blue with a check-mark inside.
Your changes to disable or enable columns will be applied instantly.
Note: Click the
RESTORE DEFAULT
button to restore the columns to the default settings.
In this Topic
Audit Log

---
## Stream Logs to IBM QRadar
**URL:** https://docs.netskope.com/en/stream-logs-to-ibm-qradar/
**Last Modified:** 2025-08-31T01:49:51+00:00
**Scraped:** 2026-08-10T08:03:27.178462+00:00

Stream Logs to IBM QRadar - Netskope Technical Documentation
Stream Logs to IBM QRadar
This topic helps you configure AWS S3 protocol connector for IBM QRadar. You must create a Log Source using the Amazon AWS S3 REST API protocol to collect compressed CSV data from the S3 bucket.
To ingest data using the Amazon AWS S3 REST API protocol, you must have QRadar version 7.5.0 UP4 or later.
To create a log source in QRadar (through the Log Source Management app) for ingesting data with Amazon AWS S3 REST API protocol from Netskope, complete the following steps:
1. Open the QRadar Log Source Management app from the QRadar console.
2. A separate window will pop up. Click on
+ New Log Source
button as shown below:
3. Select Log Source type as “
Netskope
”.
4. Select Amazon AWS S3 REST API protocol and click Configure Log Source Parameters on the Select Protocol Type page.
Refer this IBM document for more information regarding
Amazon AWS S3 REST API Protocol
.
5. On the Configure the Log Source parameters page, enter the required log source parameters:
Name: Name of the Log Source to be created.
Extension: Select NetskopeCustom_ext
6. Uncheck
Coalescing Events
to avoid grouping the events on the basis of Source and Destination IP. Click
Configure Protocol Parameters
to proceed.
7. On the Configure protocol parameters page:
Specify the Log Source Identifier for the log source to be created.
Select the Authentication Method.
Enter the value of the Access Key ID and Secret Key if the selected authentication method is Access Key ID / Secret Key.
Select the S3 Collection Method and fill all the necessary fields.
8. Enable the
Use Proxy
option and enter the proxy details.
9. Click
Test Protocol Parameters
to test.
10. Click
Finish
and then close the Log Source Management App window.
11. After closing Log Source Management App window, deploy the changes.
Deploying QRadar
Navigate to the Admin panel.
Click
Deploy Changes
. Best practice is to deploy the full configuration by clicking the
Advanced
dropdown.
In this Topic
Stream Logs to IBM QRadar

---
## Stream Logs to Crowdstrike
**URL:** https://docs.netskope.com/en/stream-logs-to-crowdstrike/
**Last Modified:** 2026-06-02T17:58:08+00:00
**Scraped:** 2026-08-10T08:03:28.362786+00:00

Stream Logs to Crowdstrike - Netskope Technical Documentation
Stream Logs to Crowdstrike
This document explains how to configure the AWS S3 bucket with the CrowdStrike S3 Data connector. The main purpose of this configuration is to stream the Web Transactions logs from an S3 bucket to the CrowdStrike NG-SIEM via their S3 Data connector.
Prerequisites
To complete this configuration, you need:
A Netskope tenant with a Web Transaction events license.
An AWS account.
A CrowdStrike Falcon account.
Note
Any changes to the field configuration (like reducing fields in the Netskope Log streaming configuration) must also be reflected in the parser for Netskope Transaction Logs. Failure to update the parser will lead to a field mismatch.
Configuration
Amazon
SQS Configuration
Create two SQS queues for the event notification configuration with the S3 bucket. One queue will be used for the Events & Alerts and the second queue will be used for the Web transaction logs.
Create the queue with the type as standard and keep all other configurations as default for the queue.
Make sure to change the access policy for the queue.
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:<AWSRegion>:<AccountID>:<SQSQueueName>"
    }
  ]
}
S3 Bucket Configuration
1. Select the bucket where you’re receiving the logs from the Netskope Log Streaming service.
The following is an example of the log file object.
2. Move to the properties of the bucket. Go to the event notification and add the configuration as shown below. Add the prefix and add the path of your folder where you’re receiving the logs. Select the Event type as
All object create events.
3. Select the destination as the SQS queue and also specify the exact queue.
4. Create one more event notifications for the other type of logs. After queue configuration, your bucket event notification will look similar to the following example.
IAM Role Configuration
1. Add the Trust policy and add the external ID from the CrowdStrike S3 Data connector configuration.
ARN Value: Your IAM role name <ARNValue> depends on your CrowdStrike cloud:
For US-1, enter arn:aws:iam::292230061137:role/crowdstrike-3pi-us1-connectors
For US-2, enter arn:aws:iam::292230061137:role/crowdstrike-3pi-us2-connectors
For EU-1, enter arn:aws:iam::292230061137:role/crowdstrike-3pi-eu1-connectors
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "<ARNValue>” 
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "44515bd2c1e44e029bb7d3b50ae2d845"
                }
            }
        }
    ]
}
2. Add the following permissions to the role.
For the
Amazon SQS
:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "arn:aws:sqs:
<AWSRegion>
:
<AccountID>
:
<SQSQueueName>
",
            "Effect": "Allow"
        }
    ]
}
For the
AWS SQS bucket
:
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "s3:GetObject",
     "Resource": [
       "arn:aws:s3:::
<S3Bucket>
/
<ObjectPrefix>
/*"
     ],
     "Effect": "Allow"
   },
   {
     "Action": "s3:ListBucket",
     "Resource": [
       "arn:aws:s3:::
<S3Bucket>
"
     ],
     "Effect": "Allow"
   }
 ]
}
Your IAM role should look similar to the following example.
CrowdStrike Data Connector Configuration in Falcon NG-SIEM
S3 Data connector configuration
1. Navigate to
data connector
>
data connections
> click
Add connection
.
2. Select the AWS S3 Data connector from the list.
3. Provide the connection name, Vendor, Vendor Product, Data source configuration, Data Timezone, and Parser.
4. Click
Manage configurations
>
Add configuration
. Provide the details for the configuration:
Name
: Name of the configuration
AWS Account ID
: AWS Account ID of your account
S3 Bucket Name
: S3 Bucket where you receiving the logs
Authentication Method
: IAM Assume Role
S3 object Prefix
: Provide the folder name or the object prefix
AWS Region
: Region containing the S3 bucket and SQS Queue
SQS Queue Name
: Your SQS Queue Name
5. Click
Save configuration
.
Migration Steps to AWS S3 Data Connector for Transaction Logs
As you start to move away from the Netskope Transactions Logs Data connector to the AWS S3 connector, follow these instructions to migrate to Netskope Log Streaming for Web transaction logs to avoid having any data loss. Here is the migration guide to help you in that transition.
The old connector used the PubSub Lite model to fetch the Transaction Logs using the below connector.
To safely migrate from the Netskope Transaction Logs Data Connector to the AWS S3 connector for Transaction Logs, you need to make sure to configure the AWS S3 connector with the correct parser.
After you start receiving the logs from your AWS S3 connector configuration, make sure to disable the Netskope Transaction Logs Data connector.
In this Topic
Stream Logs to Crowdstrike

---
## Stream Logs to Cribl
**URL:** https://docs.netskope.com/en/stream-logs-to-cribl/
**Last Modified:** 2025-08-31T01:49:51+00:00
**Scraped:** 2026-08-10T08:03:33.136891+00:00

Stream Logs to Cribl - Netskope Technical Documentation
Stream Logs to Cribl
The Netskope pack for Cribl offers log parsing and normalization for Netskope’s WebTx logs that are generated and placed into cloud storage containers (Netskope Log Streaming) by Intelligent Security Services Edge (SSE) components. The Netskope events are usually captured using a Cribl Stream Rest Collector whose config is maintained in the Cribl REST Collector Repository.
Cribl’s pack retrieves web transaction data for the purpose of integrating this rich context into security analytics systems or for long-term compliance needs. Functionality within the packs dropping or reducing the data. Post setting up the stream to the cloud bucket, this pack can be used to ensure appropriate streaming to Cribl.
Streamtags: Netskope
Use Cases: Reduction, Routing, Filtering
Data Type: Events/Logs
Deployment
Post ensuring integration set up to the Cloud Storage bucket from Log Streaming, install this pack from the
Cribl Pack Dispensary
.
Configure a Cloud Storage Collector for your source. For example: S3 or Azure Blob source collectors.
Create a Route and filter based on your source. For example, my source is named Netskope-Log-Streaming-Events-Alerts. You will need to match the name of your source.
Select the cc-netskope-log-streaming-events-and-alerts pack as the pipeline.
In this Topic
Stream Logs to Cribl

---
## Stream Logs to Elastic
**URL:** https://docs.netskope.com/en/stream-logs-to-elastic/
**Last Modified:** 2025-10-14T23:25:04+00:00
**Scraped:** 2026-08-10T08:04:42.231151+00:00

Stream Logs to Elastic - Netskope Technical Documentation
Stream Logs to Elastic
Netskope Log Streaming supports sending log files to Elastic. The first step is to set up your log stream. refer to
Log Streaming Configuration
. Ensure that compression is set to GZIP when configuring the stream as other compression types are not supported.
Collect Data from AWS
Prerequisite is you already have an AWS S3 bucket set up. The next step is to configure your AWS S3 bucket with Netskope to enable log streaming. Refer to follow
Stream Logs to Amazon S3
Collect Data from Azure Blob Storage
If you already have an Azure storage container set up, configure it with Netskope via log streaming.
Enable Netskope log streaming, refer to
Stream Logs to Azure Blob
.
Configure the integration using either Service Account Credentials or Microsoft Entra ID RBAC with OAuth2 options. For OAuth2 (Entra ID RBAC), you will need the Client ID, Client Secret, and Tenant ID. For Service Account Credentials, you will need either the Service Account Key or the URI to access the data.
How to setup the
auth.oauth2
credentials can be found in the Azure documentation
here
.
For more details about the Azure Blob Storage input settings, refer to the
Filebeat documentation
.
The service principal must be granted the appropriate permissions to read blobs. Ensure that the necessary role assignments are in place for the service principal to access the storage resources. For more information, refer to the
Azure Role-Based Access Control (RBAC) documentation
.
We recommend assigning either the
Storage Blob Data Reader
or
Storage Blob Data Owner
role. The
Storage Blob Data Reader
role provides read-only access to blob data and is aligned with the principle of least privilege, making it suitable for most use cases. The
Storage Blob Data Owner
role grants full administrative access — including read, write, and delete permissions — and should be used only when such elevated access is explicitly required.
Collect Data from a GCS Bucket
If you already have a GCS bucket setup, configure it with Netskope via log streaming.
Enable the Netskope log streaming, refer to
Stream Logs to GCP Cloud Storage
.
Configure the integration with your GCS project ID, Bucket name, and Service Account Key/Service Account Credentials File.
For more details about the GCS input settings, refer to the
Filebeat documentation
.
GCS Credentials Key File
Once you have added a key to GCP service account, you will get a JSON key file that can only be downloaded once.
To create a GCS bucket:
Make sure you have a service account available, if not follow the steps below:
Navigate to APIs & Services > Credentials
Click Create credentials > Service account
Once the service account is created, navigate to the Keys section and attach/generate your service account key.
Make sure to download the JSON key file once prompted.
Use this JSON key file either inline (JSON string object), or by specifying the path to the file on the host machine, where the agent is running.
A sample JSON Credentials file looks as follows:
{
  "type": "dummy_service_account",
  "project_id": "dummy-project",
  "private_key_id": "dummy-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nDummyPrivateKey\n-----END PRIVATE KEY-----\n",
  "client_email": "dummy-service-account@example.com",
  "client_id": "12345678901234567890",
  "auth_uri": "https://example.com",
  "token_uri": "https://example.com",
  "auth_provider_x509_cert_url": "https://example.com",
  "client_x509_cert_url": "https://example.com",
  "universe_domain": "example.com"
}
In this Topic
Stream Logs to Elastic

---
## Action Logs
**URL:** https://docs.netskope.com/en/action-logs/
**Last Modified:** 2025-10-31T23:04:54+00:00
**Scraped:** 2026-08-10T08:05:08.857365+00:00

Action Logs - Netskope Technical Documentation
Action Logs
Action logs provide a detailed record of actions performed on users or hosts. On the Action Logs page, you can view, filter, and manage these logs to track system activities and ensure accountability.
View Action Logs
Go to
Risk Exchange > Action Logs
.
The page displays a list of all action logs, including details such as the Business Rule that triggered the action, the plugin Configuration used, the Action performed, the current Status, and when it was last Modified At.
Action Log Statuses
Each action log has a status that indicates its current state:
Pending Approval
: The action requires manual approval before it can be executed.
Scheduled
: The action has been approved and is scheduled to be performed, either within the next few minutes or during a configured maintenance window.
Success
: The action was performed successfully.
Failed
: The action failed to execute.
Declined
: The action was manually declined and will not be executed.
Approve or Decline Pending Actions
A write-access user can approve pending actions.
To decline the pending action, select the action and click
Decline
to decline the action.
Go to
Risk Exchange > Action Logs
.
Action logs with status
Pending Approval
indicate that the action is not executed and requires approval to be completed.
Action logs can be expanded to see the details of the record as they were at the time when the record matched the specified business rule.
To approve the pending action, select the action and click
Approve
to approve the action.
Click
Approve
.
The Action Log status should now change to
Scheduled
and it will be performed within the next few minutes or the configured maintenance window duration.
Revert Actions
A write-access user can revert successful actions.
Go to
Risk Exchange > Action Logs
.
Action logs with status
Success
indicate that the action has been completed successfully and can be reverted if needed.
Select one or more successful action logs that you want to revert.
A confirmation dialog will appear. Click
Revert
to confirm the reversion.
The selected actions will be queued for reversion. The system will attempt to undo the effects of the original actions.
Once the reversion is processed, the action logs will be updated with reversion status and timestamp information.
Not all actions can be reverted. The ability to revert depends on whether the plugin supports the revert functionality for that specific action type.
In this Topic
Action Logs

---
## Importing and Exporting Dashboards
**URL:** https://docs.netskope.com/en/importing-and-exporting-dashboards/
**Last Modified:** 2026-02-02T06:38:13+00:00
**Scraped:** 2026-08-10T08:06:25.218635+00:00

Importing and Exporting Dashboards - Netskope Technical Documentation
Importing and Exporting Dashboards
With Netskope Advanced Analytics, you can move dashboards between different tenants or back up custom configurations by using the
Import From File
and
Export to File
feature.
This is particularly useful for moving dashboards from a test environment to production or for sharing custom community templates.
How to Export a Dashboard
Exporting a dashboard creates a .json (or sometimes zipped) file containing the metadata, layout, and query logic of your dashboard.
Navigate to
Advanced Analytics
from the Netskope admin console.
Go to your
Personal
or
Group
folder.
Locate the dashboard you wish to export.
Click the
three-dot (ellipses) menu
at the far right of the dashboard row.
Select
Export to File
.
Ensure you are not trying to export a default “Netskope Library” dashboard directly; you must first
Clone
it to your Personal folder to enable export options
.
The file automatically downloads to your local machine.
How to Import a Dashboard
Navigate to
Advanced Analytics
.
Select either the
Personal
or
Group
folder (depending on where you want the dashboard to live).
Click the
Import From File
button located at the top right of the folder view.
Click
Select File
and choose the dashboard file from your computer.
Click
Upload
.
Once the upload is complete, the dashboard will appear in your list. Open it to verify that the widgets populate correctly with your account’s data.
Key Requirements & Considerations
Feature
Details
Permissions
You must have an
Advanced Analytics license
and appropriate RBAC permissions (typically Admin or specific Report permissions) to see these options.
Custom Fields
If your dashboard uses
Custom Attributes
, these may not export. It is best practice to remove custom attributes before exporting or ensure the destination tenant has identical custom fields defined.
Data Sources
Exporting a dashboard only exports the
structure
. When imported, the dashboard will query the data available in the
new
tenant.
Default Library
You cannot export dashboards directly from the
Netskope Library
folder. You must
Clone
them to your Personal folder first.
In this Topic
Importing and Exporting Dashboards

---
## Darktrace Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/darktrace-plugin-for-log-shipper/
**Last Modified:** 2026-03-18T01:41:50+00:00
**Scraped:** 2026-08-10T08:07:31.386728+00:00

Darktrace Plugin for Log Shipper
This document explains how to configure the Darktrace v1.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin supports ingestion of Alerts (Anomaly, DLP, Malware, Policy, Compromised Credential, Legal Hold, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status), BWAN Events (Authentication, Audit, Client, Gateway, System), WebTx [via Netskope LogStreaming] and Logs (Debug, Information, Error, Warning). The data will be ingested in the SIEM platform. This plugin supports ingestion in CEF and JSON format.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Netskope Cloud Exchange tenant with the
BWAN plugin
already configured.
A Netskope Cloud Exchange tenant with the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin already configured (for ingesting WebTx from the Netskope Log Streaming plugins).
A Darktrace Server.
Note
Endpoint event type requires minimum Cloud Exchange version to be 5.1.0. BWAN events, Events of type Client Status and Alerts of type Device and Content requires minimum Cloud Exchange version to be 5.1.1.
Darktrace Plugin Support
The Darktrace plugin is used to ingest all the Alert, Events, WebTx[via Netskope LogStreming], and CE Logs in CEF and JSON format to the specified Darktrace server.
Data Type
Support
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status)
Alerts
Yes ( DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content)
Syslog CE Logs
Yes (Info, Error, Warning, Debug)
BWAN Events
Yes (Authentication, Audit, Client, Gateway, System)
WebTx
Yes (via Netskope LogStreaming)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Please refer to
Netskope Product EOL/EOS Announcements – Netskope Knowledge Portal
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
API Details
The plugin uses a ‘logging’ third-party library to push the data to the Syslog collector.
Library:
logging
This module defines functions and classes which implement a flexible event-logging system for applications and libraries.
The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.
Refer to the official documentation for more information on the logging library.
https://docs.python.org/3/library/logging.html
List of Methods Used
Method: logging.getLogger(name=None)
Return a logger with the specified name or, if the name is None, return a logger which is the root logger of the hierarchy.
All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
Method: setLevel(level)
Sets the threshold for this logger to level. Logging messages that are less severe than the level will be ignored; logging messages that have a severity level or higher will be emitted by whichever handler or handlers service this logger, unless a handler’s level has been set to a higher severity level than the level.
Method: handlers
The list of handlers is directly attached to this logger instance.
Note:
This attribute should be treated as operation.
read-only; it is normally changed via the addHandler() and removeHandler() methods, which use locks to ensure thread-safe
Method: addHandler(hdlr):
Adds the specified handler hdlr to this logger.
Method: removeHandler(hdlr):
Removes the specified handler hdlr from this logger.
Workflow
Configure the Darktrace Plugin
Configure a Log Shipper Business Rule for the Darktrace Plugin.
Configure Log Shipper Log Delivery for the Darktrace Plugin.
Validate the Darktrace Plugin.
Configure the Darktrace Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Darktrace v1.0.0 (CLS)
plugin.
Add a plugin configuration name and make sure you have the Darktrace Default Mapping file selected (if you want to use the CEF mapping).
Note
Disable the toggle button to transform the logs if you want to ingest the data in JSON; keep it enabled if you want to ingest the data in CEF format.
Click
Next
and enter the Configuration Parameters:
Darktrace server:
IP address/FQDN of Darktrace server in which data will be ingested.
Darktrace Protocol
: Protocol to be used while ingesting data.
Darktrace Port:
Darktrace port.
Darktrace Certificate:
Certificate is required only for TLS protocol.
Log Source Identifier:
This will be added as a prefix to all the logs.
Click
Save
. Your plugin configuration will be available at
Log Shipper > Plugins
.
Configure a Log Shipper Business Rule for the Darktrace Plugin
Go to
Business Rules
.
By default, there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter.
Configure Log Shipper Log Delivery for the Darktrace Plugin
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select the Source plugin (CLS Netskope), Destination plugin (CLS Darktrace), and a business rule.
For WebTx, select Source plugin (AWS Netskope Log Streaming or Azure Netskope Log Streaming) and Destination plugin (CLS Darktrace).
For Logs sharing, select the Source plugin (CLS Cloud Exchange Logs), and Destination plugin (CLS Darktrace).
Click
Save
.
After the Log Delivery configuration is added, the data will start to be pulled from the Netskope tenant, transformed, and ingested into the Darktrace platform.
Validate the Darktrace Plugin
Validate the Pull
To validate the pulling of Events, Alerts, logs, and WebTx (via Netskope LogStreaming) from the Netskope tenant, go to the
Logging
in Cloud Exchange and search for the pulled logs.
Validate the Push
To validatethe plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events, Alerts, WebTx and CE Logs with the filter
message contains ingested
. The ingested logs will be filtered.
Troubleshooting the Darktrace Plugin
An error occurred while configuring the Darktrace Plugin
If despite entering all parameters and clicking
Save
an error occurs, it may be due to one of these reasons:
The server/port configuration may differ from the specified settings (Netskope CE/Darktrace).
The port is not exposed on the Darktrace server.
What to do:
Expose the Port on the Darktrace server.
Error occurred while ingesting data from CE to Darktrace
If you are unable to push alerts/events/logs/webtx data on the Darktrace platform, then it could be due to one of these reasons:
The port is deleted/disabled on the Darktrace platform.
Darktrace server storage is full.
What to do:
Make sure the port is present and enabled, if not then create a new port.
Make sure to clean the event data if not necessary, or increase the storage of the Darktrace server.
If ingested data is not reflected on the Darktrace Platform
If you are unable to view alerts/events/logs/webtx data on the Darktrace platform, then it could be due to one of these reasons:
The filter is not correct on the Darktrace platform.
There might be an error but UDP was selected in the Port while configuring the Darktrace plugin.
What to do:
Make sure Data is searched using the correct filter.
Make sure to select the TCP port to check if there is any issue.
Network Event skipped due to unexpected type for Network Session ID field
If you are not able to get value for the Network session ID field, then it could be due to using an old Darktrace plugin where the network session id field is of number type.
What to do:
Update network session id field to string type to handle non-numeric data.
To update mappings, go to
Settings > Log Shipper > Clone
Darktrace Default Mappings
and add name for cloned mapping. Click
Events > Network > Extension
and select the
String
Type for
networkSessionId
. Click
Save
.
Use the updated mapping file in plugin configuration.
In this Topic
Darktrace Plugin for Log Shipper

---
## App Catalog and Risk Assessment
**URL:** https://docs.netskope.com/en/app-catalog-and-risk-assessment/
**Last Modified:** 2026-06-11T19:07:18+00:00
**Scraped:** 2026-08-10T08:08:04.208000+00:00

App Catalog and Risk Assessment
Contact your Netskope account team to enable Agentic Broker in your account. Additional licensing is required for Agentic Broker and DLP. Note, to create a DLP policy, the DLP add-on license is required if you do not have DLP enabled in your account.
MCP Catalog: Visibility and Risk Assessment
The MCP Catalog serves as a central repository for viewing publicly available MCP servers and their associated risk profiles.
Accessing the Catalog:
Navigate to
App Catalog > Generative AI > MCP Servers
in the left navigation panel.
Expanded Inventory:
The catalog now includes 13 publicly available MCP servers (official and community-developed) that support popular data sources.
Granular Attributes:
For each server, you can view detailed informational attributes and risk-scoring metrics to make informed security decisions.
Policy Integration:
Data from the MCP Catalog, including risk scores, can be used directly to create real-time access control policies.
In the app catalog, you now have a new section, the generative AI section, which has a list of MCP servers.
Netskope Console Left Navigation Bar:
A new Generative AI section with a list of public MCP Servers
These are a list of publicly available MCP servers such as remote MCP servers or MCP server code that is hosted on code repositories in locations such as GitHub.
AppCatalog – MCP Servers:
List of public MCP servers
Risk Assessment Capabilities
Filtering:
Filter servers by confidence level, type, and classification (Official vs. Community Edition).
Capability Analysis:
Identify if a server includes “non-read-only” tools.
Note:
Tools capable of
Update
or
Delete
operations pose a higher risk than read-only tools.
Strategic Authorization:
Use this data to authorize only those MCP servers that meet specific enterprise risk criteria.
You can filter on this list based on the confidence level, the type, and its classification such as whether it’s an official MCP server or whether it’s a community edition.
AppCatalog – MCP Servers – Confidence Level Filter:
Filter for public MCP Servers using the MCP Confidence Level filter
AppCatalog – MCP Servers – Confidence Level Filter:
Filtered list for MCP Confidence Level  of High
Click CLEAR to create the filter criteria.
AppCatalog – MCP Servers – Clear Button:
Click to clear filters
AppCatalog – MCP Servers – Type Filter:
Filter for public MCP Servers using the MCP Type filter for the type of data source, e.g., Developer and Coding Tools.
AppCatalog – MCP Servers – Type Filter:
Filtered list of public MCP Servers using the MCP Type filter for the type of data source, e.g., Developer and Coding Tools.
AppCatalog – MCP Servers – Classification Filter:
Filter for public MCP Servers using the MCP Classification filter for whether the MCP server is an official remote server/code repository or a community managed code repository.
AppCatalog – MCP Servers – Classification Filter:
Filtered list of public MCP Servers using the MCP Classification filter for the official MCP Servers.
Clicking an MCP server, you can see information about it such as its capabilities. You can see  whether it has tools that are non-read only and properties such as the authentication types it supports, the deployment model, whether it supports encryption and what type.
AppCatalog – MCP Servers – MCP Server Detail Page:
Click on an MCP Server to see the details such as its URL, repo link, non-read only tools, number of tools, types of tools and risk attributes.
Non-read only tools are either tools that can do update operations or they can do delete operations and there may be situations where you might only want to authorize MCP servers that do read only operations. or you may want to specifically block tools that do delete operations. So knowing this information allows you to make decisions about the kind of access controls you want to put in place for the use of this MCP server within your enterprise. You can use this information to make a decision on whether the risk profile of an MCP server public MCP server meets your criteria for whether you want to approve its use uh for connection as a remote MCP server and in other cases whether you want to approve the download of the code of an MCP server from specific GitHub repositories.
AppCatalog – MCP Servers – MCP Server Detail Page: Attributes, supported values and associated confidence level. A weighted average is taken to generate the composite score.
Customizing MCP Server Attributes for an updated Risk Assessment
Navigation and Configuration:
Navigate to the
App catalog
and then select
MCP Servers
.
Choose a specific MCP Server from the list.
Click on the
Configure attributes
option.
AppCatalog – MCP Servers – MCP Server Detail Page:
Configure Attributes Button (bottom right) to recompute confidence level based on specific MCP Server attribute settings.
Customization and Recalculation:
When configuring attributes, look for the relevant field. The dropdown menu for customization will only become enabled if the current attribute value is set to
Yes
.
Once enabled, you will have the option to select
No
to modify the attribute.
AppCatalog – MCP Servers – MCP Server Detail Page:
Select from dropdown to change .
After making the necessary customized changes, click the
Calculate
button.
The system will then compute a new, updated score based on the applied customizations.
The recalculated score is a point-in-time computation based on the values chosen by the user to aid in decision making on whether to allow this remote MCP server or code repo to be used in the enterprise.
Score Management and Reset:
Users have the ability to
Reset
the customized values, reverting all attributes back to their original configuration.
Following a reset, the score can be recalculated again to reflect the original, default values.
Click play to watch a video.
In this Topic
App Catalog and Risk Assessment

---
## Manage Logs
**URL:** https://docs.netskope.com/en/manage-logs/
**Last Modified:** 2026-05-18T15:01:10+00:00
**Scraped:** 2026-08-10T08:08:51.882101+00:00

Manage Logs - Netskope Technical Documentation
Manage Logs
To provide with a comprehensive view of your environment, perform the follow the steps below to generate and retrieve a diagnostic bundle.
Access the
Netskope
AI Gateway Configuration Wizard
using the
CLI interface
. For information on login details, see
Signing in to the Appliance
.
Select
Log Management
menu.
Set the AIG services log level to
Debug
to collect more detailed logs.
Navigate to the
Debug Bundle
menu and enter the password to generate the
ns-debug.zip
debug bundle.
In the
Debug Bundle
window, enter the password and press Enter.
This generates the
ns-debug.zip
debug bundle.
After generating the debug bundle, log in to the AI Gateway appliance via SFTP using the
nsdebug
account. Run the command
sftp nsdebug@{Gateway-IP}
to download the
ns-debug.zip
file. To log in to the AI Gateway appliance via SFTP, you can use the following command.
For example:
sftp -i ~/.ssh/your-ssh-key.pem -o IdentitiesOnly=yes nsdebug@{GATEWAY_IP}
Access the ESXi-based AI Gateway via password-based SFTP using the
nsdebug
account and the default password
nsadmin
. For improved security, update this default password within the
AI Gateway Configuration Wizard
via the CLI interface.
To access the AWS EC2 appliance, use an SSH key pair for passwordless SFTP login to the
nsdebug
account. During provisioning, bind your selected SSH key to the EC2 instance to enable secure authentication.
Upload the
ns-debug.zip
bundle and its corresponding decryption password to the Netskope support portal to facilitate log analysis by the engineering team.
In this Topic
Manage Logs

---
## Optimizing Splunk Ingestion for Netskope Log Streaming Web Transaction Logs
**URL:** https://docs.netskope.com/en/optimizing-splunk-ingestion-for-netskope-log-streaming-web-transaction-logs/
**Last Modified:** 2026-04-02T21:46:19+00:00
**Scraped:** 2026-08-10T08:09:17.315520+00:00

Optimizing Splunk Ingestion for Netskope Log Streaming Web Transaction Logs - Netskope Technical Documentation
Optimizing Splunk Ingestion for Netskope Log Streaming Web Transaction Logs
Overview
With Netskope Log Streaming integrated via Splunk Cloud Add-ons (such as AWS TA, MSCS TA, etc.), web transaction logs are ingested in JSON format. This allows Splunk to automatically extract fields using key-value pairs, improving searchability and ease of use.
However, unlike the Netskope TA and the deprecated web event streaming pipeline, where only raw web transaction log data was ingested without CSV headers, the JSON format includes field names along with values. As a result, this increases the overall data volume ingested into Splunk, which can lead to higher licensing costs.
To address this, you have the option to optimize ingestion volume by modifying the input configuration to ingest logs in raw CSV format instead of JSON.
Reducing Ingestion Volume
To reduce the amount of data being ingested, disable the option:
Parse all files as CSV
in the input configurations.
This change stops the conversion of logs into JSON format and instead allows the logs to be ingested in their raw CSV format. As a result, this significantly reduces the overall ingestion volume and helps lower the associated cost.
Important Considerations
While this approach helps reduce ingestion costs, it also introduces certain tradeoffs. Automatic field extraction will no longer be available, and the logs will appear as raw, unparsed data in Splunk. As a result, you will need to manually configure field extractions based on your requirements.
Manual Field Extraction (Required After Change)
Since field extraction will no longer happen automatically, you must define parsing rules using Splunk configurations such as:
props.conf
transforms.conf
Note that the structure of Netskope logs is determined by the fields selected in the tenant’s Log Streaming configuration, as well as the order in which those fields are defined.
Because of this, there is no one-size-fits-all parsing configuration. You must create and customize your field extraction rules based on your specific configuration.
Working with Raw Logs: Field Extraction Guide
Here are some basic steps to help you get started.
Step 1: Generate Regex and Configuration Files
Use AI assistant tools like ChatGPT to automatically generate the required regex and Splunk configuration files.
Provide the CSV header and a sample log entry.
Ensure the field headers are listed in the
exact order
as configured in Netskope.
Use the following structured prompt.
Prompt:
I have CSV logs with the following header:
date,time,bytes,c-ip,cs-bytes,cs-uri,cs-username,s-ip,time-taken,x-c-browser,x-c-location,cs-content-type,cs-dns,cs-host,cs-method,cs-referer,cs-uri-port,cs-uri-query,cs-uri-scheme,cs-user-agent,sc-status,x-c-browser-version,x-c-country,x-c-device,x-c-region,x-cs-app-cci,x-cs-app-instance-id,x-cs-app-suite,x-cs-connect-port,x-cs-ip-connect-xff
Sample log:
2026-03-19,06:17:43,2600,172.31.30.26,2315,-,user@company.com,16.16.109.171,58,Native,Stockholm,application/json,example.com,example.com,POST,-,443,-,https,agent,200,-,SE,Windows,Stockholm,-,-,-,-,-
Requirements:
1. Generate a REGEX with named capture groups for all fields.
2. Output Splunk configuration: props.conf transforms.conf
3. Ensure regex is production-ready and efficient.
4. Do NOT assume dynamic column order (fixed order only).
5. Add a nullQueue filter in transforms.conf to drop header rows (where raw event contains the header line)
Output format: Regex props.conf transforms.conf
Expected Outcome
A production-ready regex with named capture groups.
Properly formatted
props.conf
and
transforms.conf
.
Step 2: Update the configuration in Netskope Add-on:
Go to the Netskope TA local directory:
$SPLUNK_HOME/etc/apps/TA-NetskopeAppForSplunk/local/
Create or update the following files:
props.conf
transforms.conf
Add a new stanza for the
sourcetype
:
[netskope:web_transaction:nls]
Insert the generated configurations under the respective files.
Under the input Configurations, add a new
sourcetype
as
netskope:web_transaction:nls
from the UI.
Expected Outcome
Splunk is configured to parse Netskope logs using the defined regex.
Header rows are filtered out using
nullQueue
.
Sample stanza for props.conf
Sample stanza for transforms.conf
Step 3: Restart and Validate Splunk
Restart Splunk Enterprise
.
Expected Outcome
Logs must successfully ingest as CSV without fields.
Fields are correctly extracted and searchable.
Header rows are excluded from indexing.
Here’s a video demonstrating this process:
For Splunk Cloud Platform customers, all props.conf and transforms.conf configurations must be packaged within a custom add-on. After creating the add-on, upload it to your Splunk Cloud instance. For assistance, please contact Splunk Support.
Validation and Best Practices
Validate field extraction using Splunk search:
index=
<your_index>
| table *
To reduce initial ingestion volume, eliminate the fields you do not need from within the Netskope UI.
Stream only
required fields
from Netskope. Keep track of the following which will mandate the creation of a new parser:
Field order.
Any future changes in Netskope Log Streaming configuration.
In this Topic
Optimizing Splunk Ingestion for Netskope Log Streaming Web Transaction Logs

---
## Log Shipper Syslog Mapping
**URL:** https://docs.netskope.com/en/log-shipper-syslog-mapping/
**Last Modified:** 2026-04-28T07:06:12+00:00
**Scraped:** 2026-08-10T08:09:57.276799+00:00

Log Shipper Syslog Mapping - Netskope Technical Documentation
Log Shipper Syslog Mapping
Cloud Exchange uses a mapping file to translate Netskope field names to third party field names. For example, Netskope has a label
Source IP
and our default mapping file translates it to
src
.
Click play to watch a video.
Select a Mapping
With our dropdown mapping files, you can pick which destination formation you would like to use. You can also edit or create a mapping file.
Create/Edit a Mapping File
Cloud Exchange doesn’t allow you to edit a default mapping file. If you would like to make a change to a mapping file, select
Create copy of this file
under Action.
Go to
Settings > Log Shipper > Mapping
.
Note: You must be logged in as write-access user.
After you give this new mapping file a name, edit the fields you would like to.
The Netskope Field selector lists all available fields coming from Netskope for Alerts, Events and WebTx logs. The Target Field is what it will be translated to.
In this Topic
Log Shipper Syslog Mapping

---
## Microsoft Azure Log Analytics Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/microsoft-azure-log-analytics-plugin-for-log-shipper/
**Last Modified:** 2026-06-08T23:31:22+00:00
**Scraped:** 2026-08-10T08:11:52.557101+00:00

Microsoft Azure Log Analytics Plugin for Log Shipper
Release Notes
1.0.0
Added
Initial release.
Log Types: Alerts, Events, WebTx
Transformation: CEF (only supported in
Single Table
mode) and JSON
This document explains how to configure the Microsoft Azure Log Analytics v1.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. The plugin pushes Netskope Alerts, Events, and WebTx records from Cloud Exchange (CE) into one or more Microsoft Azure Log Analytics Custom Log Tables via a Data Collection Rule (DCR).
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A Microsoft Azure subscription with a Log Analytics workspace.
A Microsoft Entra ID application (client) with a client secret.
A Data Collection Rule (DCR) and a Data Collection Endpoint (DCE) configured in Azure.
The
Monitoring Metrics Publisher
role assigned to the Entra ID application on the DCR.
Connectivity to the following host:
https://portal.azure.com/
.
Microsoft Azure Log Analytics Plugin Support
The plugin pushes Netskope Alerts, Events, and WebTx records from Cloud Exchange (CE) into one or more Microsoft Azure Log Analytics Custom Log Tables via a Data Collection Rule (DCR).
Data Type
Support
Events
Yes
Alerts
Yes
WebTx
Yes
Cloud Exchange Logs
No
Permissions
This permission is needed for the plugin configuration:
Monitoring Metrics Publisher role on the Data Collection Rule (DCR)
API Details
List of APIs Used
API Endpoint
Method
Use Case
login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token
POST
Obtain OAuth 2.0 access token from Microsoft Entra ID
{dce_uri}/dataCollectionRules/{dcr_immutable_id}/streams/Custom-{table}?api-version=2023-01-01
POST
Ingest log records into Azure Log Analytics Custom Log Table
Get OAuth 2.0 Access Token
Endpoint:
POST login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token
Request Headers:
Key
Value
Content-Type
application/x-www-form-urlencoded
Request Body:
{
  "grant_type": "client_credentials",
  "client_id": "{app_id}",
  "client_secret": "{app_secret}",
  "scope": "https://monitor.azure.com/.default"
}
Sample Response:
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "<token>"
}
Ingest Log Records
Endpoint:
POST {dce_uri}/dataCollectionRules/{dcr_immutable_id}/streams/Custom-{table}?api-version=2023-01-01
Request Header
:
Key
Value
Authorization
Bearer {access_token}
Content-Type
application/json
Request Body:
[
  {
    "TimeGenerated": "2024-01-01T00:00:00Z",
    "Application": "Netskope CE",
    "DataType": "alerts",
    "SubType": "policy",
    "RawData": "<record or CEF string>"
  }
]
Performance Matrix
These readings were collected on a Large CE Stack with these specifications by running the plugin for a few hours in order to push log records.
Description
Specification
Stack Details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Alerts+Events Pushed Per Minute
~119k EPM (for Single Table)
~128k EPM (Per Data Type Table)
WebTx Pushed Per Minute
~140k EPM (for Single Table)
~130k EPM (Per Data Type Table)
User Agent
netskope-ce-6.1.0-cls-microsoft-azure-log-analytics-v1.0.0
Workflow
Configure a Log Analytics Workspace.
Create a Data Collection Endpoint (DCE) in Azure.
Create a Data Collection Rule (DCR) and Custom Log Tables in Azure.
Assign the Monitoring Metrics Publisher role to the Entra ID application on the DCR.
Register a Microsoft Entra ID application and generate a client secret.
Configure the Microsoft Azure Log Analytics plugin.
Configure a Log Shipper Business Rule.
Configure Log Shipper Log Delivery.
Validate the Microsoft Azure Log Analytics plugin.
Watch a Video
Click play to watch a video.
Configure a Log Analytics Workspace
Log in to
Azure
and select Log Analytics Workspace.
Click
Create Tab
.
Click
Subscription
, and then select an existing Resource Group (or create a new one).
Enter a name for your Log Analytics Workspace, select a region, and then click
Next > Next > Create
.
Configure an Application and get your Tenant ID, Application ID, and Client Secret
Log in to Azure with an account that has a Global Administrator role.
Go to
Azure App Registration > New Registration
.
In the registration form, enter a name for your application, and then click
Register
.
Make a copy of the Tenant ID and Application (Client) ID on the application page.
Click
Add a Certificate or Secret
, and then click
New client secret
to generate a Client secret. Add a description and Expire time, and then click
Add
.
Copy the value of Secret ID, as it will only be displayed once.
Configure a Data Collection Endpoint and get your DCE URI
Go to Azure Home and select
Monitor
from the Azure services.
Select
Data Collection Endpoints
on the left panel, and then click
Create
.
Enter a name for the Data collection Endpoint, select a Subscription and Resource Group, select a region (make sure that this region is the region of your Log Analytics Workspace), and then click
Review + create
.
From the Overview tab, copy the Logs Ingestion that will be your Data Collection Endpoint DCE URI.
Configure a Basic Table in Log Analytics Workspace and get your Data Collection Rule Immutable ID
A Custom Log Analytics Table requires sample data to be uploaded in order to create a JSON file on your system with the following content:
For Single table:
[   
    {         
        "RawData": {},         
        "Application":  "",         
        "DataType": "", 
        "SubType": "", 
        "TimeGenerated": "2022-11-01 12:00:00.576165"     
    } 
]
For Per Data Type Tables:
Alerts:
{
  "Application": "",
  "DataType": "",
  "SubType": "",
  "TimeGenerated": "2022-11-01 12:00:00.576165",
  "id": "",
  "access_key_id": "",
  "access_method": "",
  "account_id": "",
  "account_name": "",
  "AccountType": "",
  "acked": "",
  "act_user": "",
  "action": "",
  "actions_taken": "",
  "activity": "",
  "activity_status": "",
  "activity_type": "",
  "aggregated_user": "",
  "alert": "",
  "alert_detection_stage": "",
  "alert_id": "",
  "alert_name": "",
  "alert_source": "",
  "alert_type": "",
  "all_policy_matches": "",
  "anomaly_type": "",
  "anomalyData": "",
  "app": "",
  "app_activity": "",
  "app_category": "",
  "app_cci_apphosting_provider": "",
  "app_gdpr_level": "",
  "app_name": "",
  "app_scopes": "",
  "app_session_id": "",
  "appact": "",
  "appcategory": "",
  "appsuite": "",
  "archive_subfiles": "",
  "asset_id": "",
  "asset_object_id": "",
  "audit_category": "",
  "audit_type": "",
  "bcc": "",
  "bin_timestamp": "",
  "block_reason": "",
  "breach_date": "",
  "breach_description": "",
  "breach_id": "",
  "breach_media_references": "",
  "breach_score": "",
  "breach_target_references": "",
  "browser": "",
  "browser_session_id": "",
  "browser_version": "",
  "bypass_traffic": "",
  "category": "",
  "cc": "",
  "cci": "",
  "ccl": "",
  "channel": "",
  "classification_name": "",
  "client_bytes": "",
  "client_packets": "",
  "cloud_provider": "",
  "co": "",
  "collaborated": "",
  "company": "",
  "compliance_standards": "",
  "computer_name": "",
  "conn_duration": "",
  "conn_endtime": "",
  "conn_starttime": "",
  "connection_id": "",
  "connection_type": "",
  "CononicalName": "",
  "count": "",
  "created_date": "",
  "createdTime": "",
  "custom_attr": "",
  "custom_connector": "",
  "data_type": "",
  "department": "",
  "departmentNumber": "",
  "destination_file_directory": "",
  "destination_file_name": "",
  "destination_file_path": "",
  "detection_engine": "",
  "detection_type": "",
  "device": "",
  "device_classification": "",
  "deviceClassification": "",
  "dinsid": "",
  "displayName": "",
  "distinguishedName": "",
  "division": "",
  "dlp_fail_reason": "",
  "dlp_file": "",
  "dlp_fingerprint_classification": "",
  "dlp_fingerprint_match": "",
  "dlp_fingerprint_score": "",
  "dlp_incident_id": "",
  "dlp_is_unique_count": "",
  "dlp_mail_parent_id": "",
  "dlp_parent_id": "",
  "dlp_profile": "",
  "dlp_rule": "",
  "dlp_rule_count": "",
  "dlp_rule_score": "",
  "dlp_rule_severity": "",
  "dlp_scan_failed": "",
  "dlp_unique_count": "",
  "dns_profile": "",
  "domain": "",
  "domain_ip": "",
  "download_app": "",
  "driver": "",
  "dst_country": "",
  "dst_geoip_src": "",
  "dst_latitude": "",
  "dst_location": "",
  "dst_longitude": "",
  "dst_region": "",
  "dst_timezone": "",
  "dst_zipcode": "",
  "dsthost": "",
  "dstip": "",
  "dstport": "",
  "dynamic_classification": "",
  "edr_app": "",
  "eeml": "",
  "email_from_user": "",
  "email_modified": "",
  "email_source": "",
  "email_title": "",
  "email_user": "",
  "employeeType": "",
  "encrypt_failure": "",
  "encryption_status": "",
  "end_time": "",
  "endpoint_count": "",
  "endpoints": "",
  "enterprise": "",
  "enterprise_id": "",
  "event_type": "",
  "event_uuid": "",
  "evt_src_chnl": "",
  "exposure": "",
  "ext_labels": "",
  "external_collaborator_count": "",
  "external_email": "",
  "fastscan_results": "",
  "file_category": "",
  "file_cls_encrypted": "",
  "file_exposure": "",
  "file_id": "",
  "file_lang": "",
  "file_md5": "",
  "file_name": "",
  "file_owner": "",
  "file_password_protected": "",
  "file_path": "",
  "file_size": "",
  "file_type": "",
  "filename": "",
  "filepath": "",
  "fllg": "",
  "flpp": "",
  "forward_to_proxy_xau": "",
  "from_object": "",
  "from_storage": "",
  "from_user": "",
  "from_user_category": "",
  "fromlogs": "",
  "gateway": "",
  "gid": "",
  "group": "",
  "home_pop": "",
  "hostname": "",
  "http_method": "",
  "http_port": "",
  "http_status": "",
  "http_transaction_count": "",
  "iaas_asset_tags": "",
  "iaas_remediated": "",
  "iaas_remediated_by": "",
  "iaas_remediated_on": "",
  "iaas_remediation_action": "",
  "incident_id": "",
  "instance": "",
  "instance_id": "",
  "instance_name": "",
  "internal_collaborator_count": "",
  "ip_protocol": "",
  "ja3": "",
  "ja3s": "",
  "justification_reason": "",
  "justification_type": "",
  "last_app": "",
  "last_country": "",
  "last_device": "",
  "last_location": "",
  "last_name": "",
  "last_region": "",
  "last_timestamp": "",
  "legal_hold_profile_name": "",
  "lh_custodian_email": "",
  "lh_custodian_name": "",
  "lh_dest_app": "",
  "lh_dest_instance": "",
  "lh_fileid": "",
  "lh_filename": "",
  "lh_filepath": "",
  "lh_original_filename": "",
  "lh_shared": "",
  "lh_shared_with": "",
  "lh_version": "",
  "loc": "",
  "local_md5": "",
  "local_sha1": "",
  "local_sha256": "",
  "local_source_time": "",
  "location": "",
  "log_file_name": "",
  "logintype": "",
  "loginurl": "",
  "mail": "",
  "mal_id": "",
  "mal_sev": "",
  "mal_type": "",
  "malicious": "",
  "malsite_active": "",
  "malsite_category": "",
  "malsite_confidence": "",
  "malsite_consecutive": "",
  "malsite_country": "",
  "malsite_first_seen": "",
  "malsite_hostility": "",
  "malsite_id": "",
  "malsite_ip_host": "",
  "malsite_last_seen": "",
  "malsite_latitude": "",
  "malsite_longitude": "",
  "malsite_region": "",
  "malsite_reputation": "",
  "malware_id": "",
  "malware_name": "",
  "malware_profile": "",
  "malware_severity": "",
  "malware_type": "",
  "managed_app": "",
  "managementID": "",
  "manager": "",
  "matched_username": "",
  "md5": "",
  "memberOf": "",
  "message_id": "",
  "message_size": "",
  "metadata": "",
  "mime_type": "",
  "ml_detection": "",
  "modified": "",
  "modified_date": "",
  "netskope_activity": "",
  "netskope_pop": "",
  "network": "",
  "network_session_id": "",
  "notify_template": "",
  "ns_activity": "",
  "nsdeviceuid": "",
  "num_sessions": "",
  "num_users": "",
  "numbytes": "",
  "object": "",
  "object_count": "",
  "object_id": "",
  "object_type": "",
  "org": "",
  "organization_unit": "",
  "orig_ty": "",
  "orignal_file_path": "",
  "os": "",
  "os_details": "",
  "os_family": "",
  "os_user_name": "",
  "os_version": "",
  "other_categories": "",
  "outer_doc_type": "",
  "owner": "",
  "owner_pdl": "",
  "page": "",
  "page_site": "",
  "parent_id": "",
  "password_type": "",
  "pid": "",
  "policy": "",
  "policy_action": "",
  "policy_actions": "",
  "policy_id": "",
  "policy_name": "",
  "policy_name_enforced": "",
  "pop_id": "",
  "process_cert_subject": "",
  "process_name": "",
  "process_path": "",
  "profile_emails": "",
  "profile_hits": "",
  "profile_id": "",
  "protocol": "",
  "protocol_port": "",
  "publisher_cn": "",
  "publisher_name": "",
  "q_admin": "",
  "q_app": "",
  "q_instance": "",
  "q_original_filename": "",
  "q_original_filepath": "",
  "q_original_shared": "",
  "q_original_version": "",
  "q_shared_with": "",
  "qdomain": "",
  "qtype": "",
  "quarantine_action_reason": "",
  "quarantine_file_id": "",
  "quarantine_file_name": "",
  "quarantine_profile": "",
  "quarantine_profile_id": "",
  "record_type": "",
  "redirect_url": "",
  "referer": "",
  "region_id": "",
  "region_name": "",
  "related_malware": "",
  "remediation_profile": "",
  "req": "",
  "req_cnt": "",
  "request_id": "",
  "request_type": "",
  "resource_category": "",
  "resource_group": "",
  "resp": "",
  "resp_cnt": "",
  "retro_scan_name": "",
  "risk_level": "",
  "risk_level_id": "",
  "risk_score": "",
  "sa_profile_id": "",
  "sa_profile_name": "",
  "sa_rule_compliance": "",
  "sa_rule_id": "",
  "sa_rule_name": "",
  "sa_rule_severity": "",
  "sAMAccountName": "",
  "sAMAccountType": "",
  "sanctioned_instance": "",
  "scan_time": "",
  "scan_type": "",
  "scanner_result": "",
  "scopes": "",
  "score": "",
  "sender": "",
  "serial": "",
  "server_bytes": "",
  "server_packets": "",
  "serverity": "",
  "session_duration": "",
  "session_number_unique": "",
  "sessionid": "",
  "severity": "",
  "severity_id": "",
  "severity_level": "",
  "severity_level_id": "",
  "sfwder": "",
  "sha1": "",
  "sha256": "",
  "shared_credential_user": "",
  "shared_domains": "",
  "shared_type": "",
  "shared_with": "",
  "sharedType": "",
  "signature": "",
  "signature_id": "",
  "site": "",
  "smtp_client_domain": "",
  "smtp_status": "",
  "smtp_to": "",
  "spet": "",
  "spst": "",
  "src_country": "",
  "src_geoip_src": "",
  "src_latitude": "",
  "src_location": "",
  "src_longitude": "",
  "src_network": "",
  "src_region": "",
  "src_time": "",
  "src_timezone": "",
  "src_zipcode": "",
  "srcip": "",
  "srcport": "",
  "start_time": "",
  "sub_type": "",
  "subject": "",
  "subtype_field": "",
  "suppression_count": "",
  "suppression_end_time": "",
  "suppression_key": "",
  "suppression_start_time": "",
  "surhn": "",
  "tags": "",
  "telemetry_app": "",
  "thr": "",
  "threat_match_field": "",
  "threat_match_value": "",
  "threat_source_id": "",
  "threat_type": "",
  "threshold": "",
  "threshold_time": "",
  "timestamp": "",
  "TitleField": "",
  "title_field": "",
  "to_object": "",
  "to_storage": "",
  "to_user": "",
  "to_user_category": "",
  "total_collaborator_count": "",
  "total_packets": "",
  "traffic_type": "",
  "transaction_id": "",
  "true_filetype": "",
  "true_obj_category": "",
  "true_obj_type": "",
  "true_type_id": "",
  "trust_computer_checked": "",
  "tss_fail_reason": "",
  "tss_license": "",
  "tss_mode": "",
  "TSS_scan": "",
  "tss_scan_failed": "",
  "tunnel_id": "",
  "tunnel_type": "",
  "tunnel_up_time": "",
  "tur": "",
  "two_factor_auth": "",
  "type_field": "",
  "uba_ap1": "",
  "uba_ap2": "",
  "uba_inst1": "",
  "uba_inst2": "",
  "universal_connector": "",
  "ur_normalized": "",
  "url": "",
  "usb_device_id": "",
  "usb_device_name": "",
  "usb_device_sn": "",
  "usb_device_type": "",
  "usb_is_encrypted": "",
  "usb_product_id": "",
  "usb_vendor_id": "",
  "user": "",
  "user_category": "",
  "user_confidence_index": "",
  "user_confidence_level": "",
  "user_generated": "",
  "user_id": "",
  "user_name": "",
  "user_role": "",
  "User_SPACE_Id": "",
  "User_SPACE_Name": "",
  "user_tmp": "",
  "useragent": "",
  "userCountry": "",
  "usergroup": "",
  "userip": "",
  "userkey": "",
  "userPrincipalName": "",
  "usr_display_name": "",
  "usr_status": "",
  "usr_title": "",
  "usr_udf_businesssegmentlevel1": "",
  "usr_udf_businesssegmentlevel2": "",
  "usr_udf_businesssegmentlevel3": "",
  "usr_udf_businesssegmentlevel4": "",
  "usr_udf_companyname": "",
  "usr_udf_employeeid": "",
  "usr_udf_primarydomain": "",
  "usr_udf_supervisorid": "",
  "usr_udf_supervisorname": "",
  "violating_user": "",
  "violating_user_type": "",
  "watchlist_name": "",
  "web_universal_connector": "",
  "web_url": "",
  "windowId": "",
  "workspace": "",
  "workspace_id": "",
  "zip_password": ""
}
Events:
{
  "Application": "",
  "DataType": "",
  "SubType": "",
  "TimeGenerated": "2022-11-01 12:00:00.576165",
  "id": "",
  "access_method": "",
  "acting_user": "",
  "action": "",
  "activity": "",
  "activity_type": "",
  "alert": "",
  "alert_detection_stage": "",
  "alert_generated": "",
  "alert_name": "",
  "alert_type": "",
  "app": "",
  "app_activity": "",
  "app_cci_apphosting_provider": "",
  "app_gdpr_level": "",
  "app_session_id": "",
  "appact": "",
  "appcategory": "",
  "appsuite": "",
  "event_as": "",
  "asn": "",
  "assignee": "",
  "audit_category": "",
  "audit_log_event": "",
  "audit_type": "",
  "bcc": "",
  "boolean_metric_value": "",
  "browser": "",
  "browser_session_id": "",
  "browser_version": "",
  "bypass_reason": "",
  "bypass_traffic": "",
  "category": "",
  "cc": "",
  "cci": "",
  "ccl": "",
  "channel": "",
  "channel_id": "",
  "city": "",
  "classification": "",
  "client_bytes": "",
  "client_install_time": "",
  "client_packets": "",
  "client_version": "",
  "cloud_provider": "",
  "computer_name": "",
  "conn_duration": "",
  "conn_endtime": "",
  "conn_starttime": "",
  "connection_id": "",
  "connection_type": "",
  "CononicalName": "",
  "continent": "",
  "count": "",
  "count_metric_value": "",
  "country": "",
  "custom_attr": "",
  "custom_connector": "",
  "data_center": "",
  "data_type": "",
  "destination_app": "",
  "destination_file_directory": "",
  "destination_file_name": "",
  "destination_file_path": "",
  "destination_instance_id": "",
  "destination_site": "",
  "details": "",
  "device": "",
  "device_classification": "",
  "device_hash": "",
  "device_id": "",
  "device_name": "",
  "device_sn": "",
  "device_type": "",
  "dinsid": "",
  "dlp_fail_reason": "",
  "dlp_file": "",
  "dlp_incident_id": "",
  "dlp_is_unique_count": "",
  "dlp_mail_parent_id": "",
  "dlp_match_info": "",
  "dlp_parent_id": "",
  "dlp_profile": "",
  "dlp_profile_name": "",
  "dlp_rule": "",
  "dlp_rule_count": "",
  "dlp_rule_severity": "",
  "dlp_scan_failed": "",
  "dlp_unique_count": "",
  "dns_profile": "",
  "dom": "",
  "domain": "",
  "domain_ip": "",
  "driver": "",
  "dst_country": "",
  "dst_geoip_src": "",
  "dst_latitude": "",
  "dst_location": "",
  "dst_longitude": "",
  "dst_region": "",
  "dst_timezone": "",
  "dst_zipcode": "",
  "dsthost": "",
  "dstip": "",
  "dstport": "",
  "dynamic_classification": "",
  "eeml": "",
  "email_from_user": "",
  "email_modified": "",
  "email_user": "",
  "encryption_status": "",
  "end_time": "",
  "endpoint_policy_match_desired_action": "",
  "enriched": "",
  "event_recovered": "",
  "executable_hash": "",
  "executable_signed": "",
  "exposure": "",
  "ext_labels": "",
  "file_lang": "",
  "file_md5": "",
  "file_origin": "",
  "file_owner": "",
  "file_path": "",
  "file_size": "",
  "file_type": "",
  "filepath": "",
  "fllg": "",
  "flow_status": "",
  "flpp": "",
  "forward_to_proxy_profile": "",
  "forward_to_proxy_xau": "",
  "from_user": "",
  "from_user_category": "",
  "fromlogs": "",
  "guid": "",
  "heart_beat": "",
  "host_info_client_version": "",
  "host_info_device_make": "",
  "host_info_device_model": "",
  "host_info_hostname": "",
  "host_info_last_update_timestamp": "",
  "host_info_mac_addresses": "",
  "host_info_managementID": "",
  "host_info_nsdeviceuid": "",
  "host_info_old_nsdeviceuid": "",
  "host_info_os": "",
  "host_info_os_version": "",
  "host_info_serial_number": "",
  "host_info_steering_config": "",
  "hostname": "",
  "http_transaction_count": "",
  "incident_id": "",
  "inline_dlp_match_info": "",
  "instance": "",
  "instance_id": "",
  "internal_collaborator_count": "",
  "ip_protocol": "",
  "isp": "",
  "ja3": "",
  "ja3s": "",
  "justification": "",
  "justification_reason": "",
  "justification_type": "",
  "last_connected_from_private_ip": "",
  "last_connected_from_public_ip": "",
  "last_event_timestamp": "",
  "last_seen_device_event_actor": "",
  "last_seen_device_event_event": "",
  "last_seen_device_event_event_details": "",
  "last_seen_device_event_npa_status": "",
  "last_seen_device_event_service_name": "",
  "last_seen_device_event_status": "",
  "last_seen_device_event_status_v2": "",
  "last_seen_device_event_timestamp": "",
  "latest_incident_id": "",
  "latitude": "",
  "legal_hold_profile_name": "",
  "lh_custodian_email": "",
  "lh_custodian_name": "",
  "lh_dest_app": "",
  "lh_dest_instance": "",
  "lh_fileid": "",
  "lh_filename": "",
  "lh_filepath": "",
  "lh_original_filename": "",
  "lh_shared": "",
  "lh_shared_with": "",
  "lh_version": "",
  "local_source_time": "",
  "location": "",
  "log_file_name": "",
  "logintype": "",
  "loginurl": "",
  "longitude": "",
  "mal_sev": "",
  "managed_app": "",
  "managementID": "",
  "md5": "",
  "metric_name": "",
  "metric_true_count": "",
  "metric_type": "",
  "metric_value": "",
  "mime_type": "",
  "modified": "",
  "netskope_activity": "",
  "netskope_pop": "",
  "network": "",
  "network_session_id": "",
  "notify_template": "",
  "ns_activity": "",
  "nsdeviceuid": "",
  "num_sessions": "",
  "num_users": "",
  "numbytes": "",
  "oauth": "",
  "object": "",
  "object_id": "",
  "object_type": "",
  "org": "",
  "organization": "",
  "organization_unit": "",
  "original_file_snapshot_id": "",
  "orignal_file_path": "",
  "os": "",
  "os_details": "",
  "os_family": "",
  "os_user_name": "",
  "os_version": "",
  "other_categories": "",
  "owner": "",
  "owner_pdl": "",
  "package_version": "",
  "page": "",
  "page_site": "",
  "parent_id": "",
  "pid": "",
  "policy": "",
  "policy_action": "",
  "policy_action_enforced": "",
  "policy_id": "",
  "policy_name": "",
  "policy_name_enforced": "",
  "policy_version": "",
  "pop_name": "",
  "pop_pinned": "",
  "port": "",
  "postal_code": "",
  "printer_identifier": "",
  "process_cert_subject": "",
  "process_name": "",
  "process_path": "",
  "product_id": "",
  "protocol": "",
  "protocol_port": "",
  "publisher_cn": "",
  "publisher_ip": "",
  "publisher_name": "",
  "publisher_pop": "",
  "publisher_port": "",
  "q_shared_with": "",
  "qdomain": "",
  "qtype": "",
  "rbi_template_id": "",
  "rbi_template_name": "",
  "record_type": "",
  "referer": "",
  "region": "",
  "req": "",
  "req_cnt": "",
  "request_id": "",
  "resp": "",
  "resp_cnt": "",
  "resp_content_len": "",
  "resp_content_type": "",
  "response_time": "",
  "retro_scan_name": "",
  "risk_score": "",
  "sa_rule_compliance": "",
  "sAMAccountName": "",
  "sampled_text_size": "",
  "sanctioned_instance": "",
  "scan_type": "",
  "serial": "",
  "server_bytes": "",
  "server_packets": "",
  "serverity": "",
  "session_duration": "",
  "session_number_unique": "",
  "sessionid": "",
  "severity": "",
  "severity_level": "",
  "sha256": "",
  "shared_with": "",
  "site": "",
  "smtp_block_reason": "",
  "smtp_client_domain": "",
  "smtp_to": "",
  "source_file_directory": "",
  "source_file_name": "",
  "source_file_path": "",
  "spet": "",
  "spst": "",
  "src_country": "",
  "src_geoip_src": "",
  "src_latitude": "",
  "src_location": "",
  "src_longitude": "",
  "src_network": "",
  "src_region": "",
  "src_time": "",
  "src_timezone": "",
  "src_zipcode": "",
  "srcip": "",
  "srcport": "",
  "ssl_decrypt_policy": "",
  "start_time": "",
  "status": "",
  "sub_type": "",
  "subtype_field": "",
  "supporting_data": "",
  "suppression_end_time": "",
  "suppression_key": "",
  "suppression_start_time": "",
  "tags": "",
  "telemetry_app": "",
  "thr": "",
  "threat_type": "",
  "timestamp": "",
  "title_field": "",
  "to_user": "",
  "total_collaborator_count": "",
  "total_packets": "",
  "traffic_type": "",
  "transaction_id": "",
  "true_obj_category": "",
  "true_obj_type": "",
  "tss_fail_reason": "",
  "tss_mode": "",
  "tss_scan_failed": "",
  "tunnel_id": "",
  "tunnel_type": "",
  "tunnel_up_time": "",
  "tur": "",
  "type_field": "",
  "unc_path": "",
  "universal_connector": "",
  "ur_normalized": "",
  "url": "",
  "usb_device": "",
  "user": "",
  "user_category": "",
  "user_confidence_index": "",
  "user_confidence_level": "",
  "user_generated": "",
  "user_id": "",
  "user_info_device_classification_status": "",
  "user_info_orgkey": "",
  "user_info_userkey": "",
  "user_info_username": "",
  "useragent": "",
  "userip": "",
  "userkey": "",
  "userPrincipalName": "",
  "vendor_id": "",
  "violation": "",
  "web_universal_connector": "",
  "workspace": "",
  "workspace_id": "",
  "zip_file_id": "",
  "zip_password": "",
  "zipcode": ""
}
WebTx:
{
  "Application": "",
  "DataType": "",
  "SubType": "",
  "TimeGenerated": "2022-11-01 12:00:00.576165",
  "bytes": "",
  "c_ip": "",
  "cs_bytes": "",
  "cs_content_type": "",
  "cs_dns": "",
  "cs_host": "",
  "cs_method": "",
  "cs_referer": "",
  "cs_uri": "",
  "cs_uri_port": "",
  "cs_uri_query": "",
  "cs_uri_scheme": "",
  "cs_user_agent": "",
  "cs_username": "",
  "date_field": "",
  "rs_bytes": "",
  "rs_status": "",
  "s_ip": "",
  "sc_bytes": "",
  "sc_content_type": "",
  "sc_status": "",
  "sr_bytes": "",
  "time_field": "",
  "time_taken": "",
  "x_action": "",
  "x_action_reason": "",
  "x_c_authn_source": "",
  "x_c_authn_surrogate": "",
  "x_c_authn_surrogate_status": "",
  "x_c_authn_user": "",
  "x_c_authz_groups": "",
  "x_c_authz_ou": "",
  "x_c_authz_source": "",
  "x_c_browser": "",
  "x_c_browser_version": "",
  "x_c_country": "",
  "x_c_device": "",
  "x_c_device_classification": "",
  "x_c_device_uid": "",
  "x_c_hostname": "",
  "x_c_latitude": "",
  "x_c_local_time": "",
  "x_c_local_timestamp": "",
  "x_c_location": "",
  "x_c_longitude": "",
  "x_c_nsclient_client_profile": "",
  "x_c_nsclient_steering_profile": "",
  "x_c_nsclient_version": "",
  "x_c_os": "",
  "x_c_os_family": "",
  "x_c_os_version": "",
  "x_c_region": "",
  "x_c_timezone": "",
  "x_c_user_confidence_index": "",
  "x_c_zipcode": "",
  "x_category": "",
  "x_category_id": "",
  "x_client_ssl_err": "",
  "x_cs_access_method": "",
  "x_cs_access_proxy": "",
  "x_cs_app": "",
  "x_cs_app_activity": "",
  "x_cs_app_category": "",
  "x_cs_app_cci": "",
  "x_cs_app_ccl": "",
  "x_cs_app_from_user": "",
  "x_cs_app_instance_id": "",
  "x_cs_app_instance_name": "",
  "x_cs_app_instance_tag": "",
  "x_cs_app_instance_tags": "",
  "x_cs_app_object_id": "",
  "x_cs_app_object_name": "",
  "x_cs_app_object_type": "",
  "x_cs_app_suite": "",
  "x_cs_app_tags": "",
  "x_cs_app_to_user": "",
  "x_cs_connect_host": "",
  "x_cs_connect_port": "",
  "x_cs_connect_user_agent": "",
  "x_cs_connect_xau": "",
  "x_cs_domain_fronted_sni": "",
  "x_cs_dst_ip": "",
  "x_cs_dst_port": "",
  "x_cs_http_version": "",
  "x_cs_ip_connect_xff": "",
  "x_cs_ip_xff": "",
  "x_cs_nsclient_tunnel_type": "",
  "x_cs_page_id": "",
  "x_cs_parent_process": "",
  "x_cs_pid": "",
  "x_cs_ppid": "",
  "x_cs_process": "",
  "x_cs_session_id": "",
  "x_cs_site": "",
  "x_cs_sni": "",
  "x_cs_src_ip": "",
  "x_cs_src_ip_egress": "",
  "x_cs_src_port": "",
  "x_cs_ssl_cipher": "",
  "x_cs_ssl_engine_action": "",
  "x_cs_ssl_engine_action_reason": "",
  "x_cs_ssl_fronting_error": "",
  "x_cs_ssl_handshake_error": "",
  "x_cs_ssl_ja3": "",
  "x_cs_ssl_malformed_ssl": "",
  "x_cs_ssl_version": "",
  "x_cs_timestamp": "",
  "x_cs_traffic_type": "",
  "x_cs_tunnel_id": "",
  "x_cs_uri_path": "",
  "x_cs_url": "",
  "x_cs_userip": "",
  "x_cs_xau": "",
  "x_eip_policy_footprint": "",
  "x_eip_policy_name": "",
  "x_error": "",
  "x_other_category": "",
  "x_other_category_id": "",
  "x_policy_action": "",
  "x_policy_categories": "",
  "x_policy_dst_host": "",
  "x_policy_dst_host_source": "",
  "x_policy_dst_ip": "",
  "x_policy_justification_reason": "",
  "x_policy_justification_type": "",
  "x_policy_name": "",
  "x_policy_src_ip": "",
  "x_r_cert_end": "",
  "x_r_cert_enddate": "",
  "x_r_cert_expired": "",
  "x_r_cert_incomplete_chain": "",
  "x_r_cert_issuer_cn": "",
  "x_r_cert_mismatch": "",
  "x_r_cert_revocation_check": "",
  "x_r_cert_revoked": "",
  "x_r_cert_self_signed": "",
  "x_r_cert_start": "",
  "x_r_cert_startdate": "",
  "x_r_cert_subject_cn": "",
  "x_r_cert_untrusted_root": "",
  "x_r_cert_valid": "",
  "x_r_country": "",
  "x_r_latitude": "",
  "x_r_location": "",
  "x_r_longitude": "",
  "x_r_region": "",
  "x_r_zipcode": "",
  "x_request_id": "",
  "x_rs_file_category": "",
  "x_rs_file_language": "",
  "x_rs_file_md5": "",
  "x_rs_file_sha256": "",
  "x_rs_file_size": "",
  "x_rs_file_type": "",
  "x_s_country": "",
  "x_s_custom_signing_ca_error": "",
  "x_s_dp_name": "",
  "x_s_latitude": "",
  "x_s_location": "",
  "x_s_longitude": "",
  "x_s_region": "",
  "x_s_zipcode": "",
  "x_sc_notification_name": "",
  "x_server_ssl_err": "",
  "x_sr_dst_ip": "",
  "x_sr_dst_port": "",
  "x_sr_forward_dest": "",
  "x_sr_headers_name": "",
  "x_sr_headers_value": "",
  "x_sr_src_ip": "",
  "x_sr_src_port": "",
  "x_sr_ssl_cipher": "",
  "x_sr_ssl_client_certificate_error": "",
  "x_sr_ssl_engine_action": "",
  "x_sr_ssl_engine_action_reason": "",
  "x_sr_ssl_handshake_error": "",
  "x_sr_ssl_ja3s": "",
  "x_sr_ssl_malformed_ssl": "",
  "x_sr_ssl_version": "",
  "x_ssl_bypass": "",
  "x_ssl_bypass_reason": "",
  "x_ssl_policy_action": "",
  "x_ssl_policy_categories": "",
  "x_ssl_policy_dst_host": "",
  "x_ssl_policy_dst_host_source": "",
  "x_ssl_policy_dst_ip": "",
  "x_ssl_policy_issuer": "",
  "x_ssl_policy_name": "",
  "x_ssl_policy_src_ip": "",
  "x_support": "",
  "x_tenant_id": "",
  "x_tp_engine": "",
  "x_tp_malware_name": "",
  "x_tp_result": "",
  "x_tp_severity": "",
  "x_transaction_id": "",
  "x_type": ""
}
On the Azure home tab, go to
Log Analytics Workspace
, select the workspace created previously, and select
Tables
. Click
Create
and select
New Custom log (DCR based)
.
Enter a name for the table.
For the Data Collection Rule, click
Create a new data collection rule
and select a Subscription and Resource Group from the dropdown lists. Enter the region for your Log Analytics Workspace, and then click
Done
. Make sure to keep Table plan as Basic.
The new Data Collection Rule will be selected in the Data collection rule field. Click
Next
.
On the Schema and Transformation tab, click
Browse for files
and select the sample data JSON file you created previously.
Click
Next
and then click
Create
.
A Custom Log Table will be created with the suffix _CL.
Here you are changing the Table Plan from Analytics to Basic because the Basic log data plan lets you save on the cost of ingesting, and storing high-volume verbose logs in your Log Analytics workspace for debugging, troubleshooting, and auditing. If the Table Plan is not changed and kept as Analytics, the Logs will still be ingested in the Table without any issue. The Analytics table has a configurable retention period from 30 days to 730 days. The Basic table has Retention fixed at eight days. Basic Logs tables retain data for eight days. When you change an existing table’s plan to Basic Logs, Azure archives data that’s more than eight days old, but still within the table’s original retention period.
To get the Data Collection Immutable ID, go to
Home
, select
Monitor
from the
Azure Services > Data Collection Rules
, and then select the DCR created by you while creating the Custom Table.
In the Overview tab, click
JSON View
from the top right corner, and copy the immutableId.
Assign a Permission to DCR and DCE
On the Azure Home page, go to
Monitor > Data Collection Endpoint
and select the Endpoint created previously.
Select
Access control (IAM)
and click
Add role assignment
.
From the list of roles, select
Monitoring Metrics Publisher
and click
Next
.
Select a user, group, or service principal for which to assign access.
Click
Select Members
and search for the Application you created in the search box, and then select it.
Click
Review + assign
.
Repeat these same steps to assign permissions to the DCR (Data Collection Rule).
Configure the Microsoft Azure Log Analytics Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Microsoft Azure Log Analytics v1.0.0 (CLS)
plugin.
Provide the Configuration Name and change the Sync Interval per your requirement.
Click Next and enter the Configuration Parameters:
Tenant ID
: Microsoft Entra ID Directory (tenant) ID.
Application ID
: Application (client) ID of the Entra ID app.
Application Secret
: Client secret ID of the Entra ID app.
Data Collection Endpoint URI
: Base URI of the Data Collection Endpoint.
DCR Immutable ID
: Immutable ID of the Data Collection Rule.
Log Source Identifier
: Value written into the Application column on every row. Default: Netskope CE.
Ingestion Mode
: Select Single Table to send all data to one table, or Per Data Type to route each data type to a separate table.
Custom Log Table Name (Single Table mode)
: Destination table name that receives all records.
Data Types to Ingest (Per Data Type mode)
: Select one or more of Alerts, Events, WebTx.
Alerts Custom Log Table Name (Per Data Type mode)
: Destination table for Alerts data.
Events Custom Log Table Name (Per Data Type mode)
: Destination table for Events data.
WebTx Custom Log Table Name (Per Data Type mode)
: Destination table for WebTx data.
The plugin will not be configured with ‘CEF’ and ‘Per Data Type’ Ingestion mode together.
Click
Save.
Configure a Log Shipper Business Rule for Microsoft Azure Log Analytics
In Log Shipper, go to
Business Rules
and click
Add Business Rule
.
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
Click
Save
.
Configure Log Shipper Log Delivery for the Microsoft Azure Log Analytics Plugin
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select a Source Configuration, Destination Configuration, and Business Rule.
Click
Save
.
After the Log Delivery is added, the data will start to be pulled from the Netskope tenant and ingested into the Azure Monitor platform.
Validate the Microsoft Azure Log Analytics Plugin
Validate the Pull
To validate the pulling of indicators from the Netskope tenant.
In Cloud Exchange, go to
Logging
and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events and Alerts with the filter:
message contains “ingested”
.
To validate the push on Microsoft Azure Log Analytics:
In Azure Portal, go to your
Log Analytics workspace
and open
Logs
.
Query the Custom Log table (like YourTableName_CL | take 10) to verify that records have been ingested.
For example, below are the alerts ingested in Alerts table.
Here are the events ingested in Events table.
Here are the WebTx ingested in WebTx table.
If you have selected Single Table mode, then the plugin will ingest all alerts, events, and WebTx in a single table in CEF or JSON format.
Here are the examples of alerts, events and WebTx ingested in CEF and JSON format:
Troubleshooting the Microsoft Azure Log Analytics Plugin
Receiving an error code 403 while configuring the plugin in toast and log message
Ensure that you have the correct permissions for your application to the DCR. Check if you have assigned permissions to the correct Data Collection endpoint as described above. It may take up to 30 minutes to reflect the assigned permissions.
Having difficulties in saving the Microsoft Azure Monitor plugin
Despite entering all parameters and clicking the Save button, an error may occur, possibly due to:
Configuration differs from the specified settings.
Getting the below error:
What to do:
It could be because of incorrect configuration parameters, just follow the steps in the
Configure a Log Analytics Workspace
.
It could be due to the table recently created and used in the plugin, it takes time to reflect the table on Azure.
Unable to see the events on the Microsoft Azure Monitor
Even after successful ingestion of the events, not able to see the events ingested from the plugin. This could be due to one these reasons:
Incorrect query provided in Log searching.
No events are ingested in the platform.
Or the data you are looking for is outside of the searching Time Range.
What to do:
Check if you have provided the correct query in Log searching.
Check for the logs on the Cloud Exchange for the ingested events.
Check events are ingested in a longer time range.
CEF Formatting Cannot Be Used with Per Data Type Ingestion Mode
If you see
CEF formatting cannot be used with ‘Per Data Type’ Ingestion Mode
during plugin configuration, it could be due to the plugin configuration being set to CEF while the Ingestion Mode is set to Per Data Type, which is an unsupported combination.
What to do
: In the plugin configuration, switch from CEF to JSON, or change the Ingestion Mode to Single Table in the plugin configuration.
Known Behavior
These fields from the above mapping will appear with the suffix ‘_field’ in the Log Analytics table. This behavior is due to the Azure Log Analytics platform, where certain field names are reserved keywords and cannot be used directly in mappings. To avoid conflicts, the ‘_field’ suffix has been added to these fields:
type
title
subtype
date
time
TimeGenerated
Application
DataType
SubType
Additionally, if you encounter any errors while uploading a custom mapping to the Azure Log Analytics workspace table, it may be because one or more fields in the mapping are reserved keywords.
In this Topic
Microsoft Azure Log Analytics Plugin for Log Shipper

---
## Databricks Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/databricks-plugin-for-log-shipper/
**Last Modified:** 2026-07-07T03:07:06+00:00
**Scraped:** 2026-08-10T08:12:20.460262+00:00

Databricks Plugin for Log Shipper - Netskope Technical Documentation
Databricks Plugin for Log Shipper
Release Notes
1.0.0 (Minimum required CE version 6.0.0)
Added
Initial release.
Log Types: Alerts, Events, Webtx.
Format Type: JSON.
This document explains how to configure the Databricks v1.0.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to send Netskope Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status) and WebTx data to an AWS S3 bucket. This plugin supports ingestion in JSON format only. To view the data on databricks, make sure the S3 bucket is linked with the Databricks External Location.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange instance with the
Tenant plugin
and
Log Shipper plugin
already configured.
Already configured
AWS Netskope LogStreaming Plugin
or
Azure Log Streaming Plugin
for pulling Webtx logs.
A Databricks Workspace instance linked with an AWS account and Unity Catalog enabled.
An AWS S3 bucket with the following IAM permissions granted to the authenticating role:
s3:ListBucket, s3:GetBucketLocation, s3:PutObject
.
An AWS S3 bucket linked with Databricks External Location.
Databricks Plugin Support
This plugin is used to send Netskope Alerts (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content), Events (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status) and WebTx data to an AWS S3 bucket. This plugin supports ingestion in JSON format only. To view the data on databricks, make sure the S3 bucket is linked with the Databricks External Location.
Data Type
Support
Events
Yes (Page, Application, Audit, Infrastructure, Network, Incident, Endpoint, Client Status)
Alerts
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, UBA, CTEP, Device, Content)
WebTx
Yes
Cloud Exchange Logs
No
To pull Webtx logs, you need to use the
AWS Netskope LogStreaming plugin
or
Azure Log Streaming Plugin
.
Permissions
These permissions are needed for the plugin configuration:
s3:ListBucket on the target S3 bucket
s3:GetBucketLocation on the target S3 bucket
s3:PutObject on the target S3 bucket
If the role does not have `s3:GetBucketLocation` permission, the bucket region check is silently skipped during validation. Grant this permission to ensure a misconfigured region is caught at save time.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/sessions
POST
Generate temporary AWS credentials (IAM Roles Anywhere only)
Generate Temporary Credentials
Endpoint:
POST https://rolesanywhere.{region}.amazonaws.com/sessions
Request Headers:
Key
Value
Content-Type
application/json
X-Amz-Date
{timestamp}
X-Amz-X509
Base64-encoded DER certificate
Authorization
AWS4-X509-RSA-SHA256 Credential=170190831808398918967185780480038694669/20260611/us-east-1/rolesanywhere/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-x509, Signature=………………..
User-Agent
APN/1.1 (ahq9d89xj9gspapczzdb59goq)
Request Body:
{
  "durationSeconds": 900,
  "profileArn": "{profile_arn}",
  "roleArn": "{role_arn}",
  "sessionName": "Session",
  "trustAnchorArn": "{trust_anchor_arn}"
}
Sample Response:
{
  "credentialSet": [
    {
      "credentials": {
        "accessKeyId": "ASIA...",
        "secretAccessKey": "...",
        "sessionToken": "...",
        "expiration": "2024-01-01T00:15:00Z"
      }
    }
  ]
}
Library: AWS SDK for Python (Boto3)
1.
Creating the S3 Client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=self.aws_public_key,
    aws_secret_access_key=self.aws_private_key,
    aws_session_token=self.aws_session_token,
    region_name=self.configuration.get("region_name", "").strip(),
    config=Config(
        proxies=self.proxy,
        user_agent=self.useragent,
    ),
)
2. Check Bucket Existence
s3_client.head_bucket(Bucket=bucket_name)
3. Get Bucket Region
location = s3_client.get_bucket_location(Bucket=bucket_name)
bucket_region = location.get("LocationConstraint") or "us-east-1"
4. Upload File to S3
s3_client.upload_file(
    file_name,      # local temp file path
    bucket_name,    # S3 bucket name
    object_name,    # S3 object key
)
Performance Matrix
This performance reading was conducted on a Large Stack in Cloud Exchange with these VM specifications. These readings are added with the consideration that it will ingest around 15k Netskope alerts/events in 5 seconds to the destination.
Description
Specification
Stack details
Size: Large,
RAM: 32 GB,
CPU: 16 Cores
Alerts/Events ingested to SIEM
~ 180K Alerts/Events per minute
Webtx ingested to SIEM
~ 150K Webtx logs per minute
User Agent
APN/1.1 (ahq9d89xj9gspapczzdb59goq)
Workflow
Get credentials for configuring the Databricks plugin
Configure the Databricks plugin.
Configure a Business Rule.
Configure Log Delivery.
Validate the plugin.
Watch a Video
Click play to watch a video.
Configuration on AWS
Create a Policy
Log in to your AWS account, go to
IAM > Policies
and then click
Create Policy
.
Select json and paste this policy in it.
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"s3:GetBucketLocation",
				"s3:PutObject",
				"s3:ListBucket"
			],
			"Resource": "*"
		}
	]
}
Enter a name and description.
Click
Create Policy
.
Deployed on AWS authentication
Create a Role
Go to
IAM Services
in the AWS Console.
Go to the
Roles
page under
Access management
and click
Create Role
.
Select the AWS Service.
Under
Use case
, select
EC2
.
Click
Next
.
Select the permission policy created in
Create a Policy
.
Click
Next
.
Enter a Role Name and Description
.
Click
Create Role
.
Assign a Role to EC2 Instance
Open your EC2 instance console.
Go to the
Instances
page and select the required instance where Cloud Exchange is deployed.
Go to
Action > Security > Modify IAM Role
.
Select the Role that you created above in
Create a Role
.
Click
Add IAM Role
/
Update IAM Role
. Note that both the EC2 instance and S3 bucket should be in the same region.
Restart your EC2 instance if you get permission related errors even after updating the IAM role for the EC2 instance.
IAM Role Anywhere authentication
Prerequisites
The AWS Certificate Manager service is required to be enabled to authenticate the plugin using the
AWS IAM Roles Anywhere
authentication method.
Make sure you create the Private Certificate Authority, Trust Anchor, and Profile in the same region that your AWS S3 bucket resides.
Create a Policy
This Policy contains the required permissions for creating a Private CA Certificate(including Permissions for creating Trust Anchor and Profile) and using the IAM Roles Anywhere.
Go to
Policy Generator
and select IAM Policy as the policy type and generate policy.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Private Certificate Authority
Actions:
CreateCertificateAuthority
DescribeCertificateAuthority
GetCertificate
GetCertificateAuthorityCertificate
GetCertificateAuthorityCsr
ImportCertificateAuthorityCertificate
IssueCertificate
ListCertificateAuthorities
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management (IAM)
Actions:
AttachRolePolicy
CreateAccessKey
CreateRole
DeleteRole
PassRole
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Certificate Manager
Actions:
DescribeCertificate
ExportCertificate
GetCertificate
ListCertificates
ListTagsForCertificate
RequestCertificate
ARN: *
Click
Add Statement
.
Select Type of Policy: IAM Policy
Effect: Allow
AWS Service: AWS Identity and Access Management Roles Anywhere
Actions:
CreateProfile
CreateTrustAnchor
GetProfile
GetTrustAnchor
ListProfiles
ListTrustAnchors
ARN: *
Click
Add Statement
.
Click
Generate Policy.
Copy the Policy as it will be used in the next step for creating the policy required for creating the Private CA certificates.
Go to the AWS Console and select
IAM
from
All Services
. Click
Policies
in the left panel, and then click
Create Policy
.
Paste the policy generated in the previous section to the JSON tab. Click
Next: Tags
and
Next: Review.
Enter a Name and click
Save Changes
.
Create a Private Certificate Authority
Log in to the AWS Console.
Search for
Certificate Manager
.
Click
AWS Private CA
.
Click
Create a private CA
.
For
Mode Options
, select
General-purpose
, and for
CA type options
, select
Root
.
Enter the Organization (O).
For
Key algorithm options
, select
RSA 2048
.
Add tags if any (optional).
Enable the checkbox in the
CA permissions options
section.
Enable the checkbox in the
Pricing
section.
Click
Create
to create the CA certificate.
For
Actions
, select
Install
.
Click
Confirm and Install
.
Create a Trust Anchor
Search for
IAM Service
and go to
Roles
under
Access management
. Scroll down to
Roles Anywhere
and select
Manage
.
Click
Create a trust anchor
.
Enter a Trust anchor name.
Select the AWS Certificate Manager Private CA(created in the previous steps) as a Certificate authority (CA) source.
Select  the certificate that you created under AWS Certificate Manager Private CA.
Add tags if required.
Click
Create a trust anchor
.
Click on the created Trust Anchor and copy the Trust Anchor ARN. This will be required in the plugin Trust Anchor ARN configuration parameter for the AWS IAM Roles Anywhere authentication method.
Create an IAM Role
Go to
IAM Services
in the AWS Console.
Click
Role
in the
Access management
submenu.
Click
Create Role
.
For the
Trusted entity type
, select
Custom Trust Policy
.
Replace the Custom Trust Policy with this Trust Policy. This policy contains the permissions for using the Roles Anywhere service:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "rolesanywhere.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetSourceIdentity"
            ]
        }
    ]
}
Click
Next
.
In the Permissions policies, select the created policy from the
Create a policy
section previously.
Click
Next
.
Enter a Role name and Description for the role.
Click
Create role
.
Search for the created role and click on the Role Name.
Make a note of the Role ARN because this will be required in the plugin Role ARN configuration parameter for the AWS IAM Roles Anywhere authentication method.
Create a Profile
Go to
IAM Services
in the AWS Console.
Select
Roles
present under
Access management
.
Scroll down to Roles Anywhere and click
Manage
.
Expand the Setup steps.
Click
Step 2: Configure roles
.
Click
Configure a profile
.
Enter a Profile name.
Select the role created in the
Create IAM Role
step.
Remove the Inline Policy.
Click
Create profile
.
Click on the reated Profile and copy the Profile ARN.
Request a Private Certificate
Go to
AWS Certificate Manager > Request certificate
.
Select
Request a private certificate
.
Click
Next
.
Select the Certificate authority created in the previous steps.
Provide a domain name in the Fully qualified domain name field. For example: netskope-ce.com.
For
Key algorithm
, select
RSA 2048
.
Add tags if required.
Acknowledge the Certificate renewal permissions.
Click
Request
.
Go to
List certificates
from the navigation pane of AWS Certificate Manager.
Select the certificate created previously.
Click
Export
.
Enter the passphrase
.
Make a note of the passphrase as it will be required for the configuration of the AWS S3 Plugin using the
AWS IAM Roles Anywhere
authentication method.
Click
Generate PEM Encoding
.
Download all the Certificates because they won’t be visible again. For new certificates, you will need to Export them again.
Copy the Certificate body and Certificate Private Key, because they will be required for the Configuration of the AWS S3 Plugin using the
AWS IAM Roles Anywhere
Authentication method. For More Info visit
AWS IAM Role Anywhere
Link an AWS S3 Bucket to a Databricks External Location
Your AWS account must be already linked with your Databricks account. Refer to this
documentation
for more information.
Log in to Databricks and go to
Workspace
.
In the top search bar, enter
External Locations
and select it from the results.
Click
Create external location
.
Select
AWS Quickstart
and click
Next
.
Provide the bucket name in this format
s3://<bucket-name>
, and click
Generate new token
.
Copy the generated token, and then click
Launch in Quickstart
.
This will redirect you to the AWS console. Enter the Personal Access Token in the
Databricks Personal Access Token
field.
Check the Acknowledgement, and then click
Create stack
.
After it is done, you will be able to see the external location on the Databricks after 10 minutes to 15 minutes.
Note
Refer this
Databricks documentation
for more information related to linking an S3 bucket with an External location.
If you do not want to use a different S3 bucket for the Databricks plugin, then you can directly link the S3 bucket used for Netskope Log Streaming to the Databricks External location.
Configure the Databricks Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Databricks v1.0.0 (CLS)
plugin.
Enter the Basic Information:
Configuration Name:
Provide a plugin configuration name.
Mapping:
Choose the mapping configuration to be used. You can add a new one from
Settings > Log Shipper
.
Format:
Choose the format of data you want to transform. When JSON is selected, raw JSON logs will be sent. The ingestion may be affected if the Log Delivery Configuration does not accept raw log format.
Click
Next
and enter the Configuration Parameters, depending on the authentication method:
Deployed on AWS authentication:
Authentication Method:
Select the method to be used for AWS client authentication. ‘Deployed on AWS’ uses the IAM instance profile or role attached to the AWS environment. ‘AWS IAM Roles Anywhere’ uses an X.509 certificate and private key to obtain temporary AWS credentials — use this when CE is running outside AWS.
AWS S3 Bucket Region Name:
AWS region where the target S3 bucket resides. Make sure the region matches the region in the Profile ARN and Trust Anchor ARN when using IAM Roles Anywhere.
AWS S3 Bucket Name:
Name of the target AWS S3 bucket where Netskope Alerts and Events will be stored. This bucket must be linked with the Databricks External Location.
Example: netskope-alerts-bucket.
IAM Roles Anywhere
authentication:
Authentication Method:
Select the method to be used for AWS client authentication. ‘Deployed on AWS’ uses the IAM instance profile or role attached to the AWS environment. ‘AWS IAM Roles Anywhere’ uses an X.509 certificate and private key to obtain temporary AWS credentials. Use this when CE is running outside AWS.
Private Key:
PEM-encoded private key used to decrypt the AWS Private CA Certificate. Required for AWS IAM Roles Anywhere authentication.
Certificate Body:
PEM-encoded X.509 certificate body issued by your AWS Private or Public CA. Required for AWS IAM Roles Anywhere authentication.
Password Phrase:
Passphrase used to decrypt the CA certificate if it is encrypted. Required for AWS IAM Roles Anywhere authentication.
Profile ARN:
ARN of the IAM Roles Anywhere profile. Format: arn:aws:rolesanywhere:{region}:{account-id}:profile/{profile-id}. Required for AWS IAM Roles Anywhere authentication.
Role ARN:
ARN of the IAM role to be assumed. Format:
arn:aws:iam::{account-id}:role/{role-name}
. Required for AWS IAM Roles Anywhere authentication.
Trust Anchor ARN:
ARN of the IAM Roles Anywhere trust anchor. Format:arn:aws:rolesanywhere:{region}:{account-id}:trust-anchor/{anchor-id}. Required for AWS IAM Roles Anywhere authentication.
AWS S3 Bucket Region Name:
AWS region where the target S3 bucket resides. Make sure the region matches the region in the Profile ARN and Trust Anchor ARN when using IAM Roles Anywhere.
AWS S3 Bucket Name:
Name of the target AWS S3 bucket where Netskope Alerts and Events will be stored. This bucket must be linked with the Databricks External Location. Example:
netskope-alerts-bucket
.
Click
Save
.
Configure a Log Shipper Business Rule for Databricks
In Log Shipper, go to
Business Rules
and click
Add Business Rule
.
By default, there’s a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
and configure a new business rule by adding the rule name and filter(s).
Click
Save
.
Configure Log Shipper Log Delivery for the Databricks Plugin
In Log Shipper, go to
Log Delivery
and click
Add Log Delivery Configuration
.
Select a Source Configuration, Destination Configuration, and Business Rule.
Click
Save
.
To pull Webtx logs, you need to use the
AWS Netskope LogStreaming Plugin
or
Azure Log Streaming Plugin
.
Validate the Databricks Plugin
Validate the Pull
In Cloud Exchange, go to
Logging
and search for the pulled logs.
Validate the Push
To validate the plugin workflow in Cloud Exchange, go to
Logging
and search for ingested Events and Alerts with the filter:
message contains “ingested”
or
message contains “<destination plugin configuration name>”
.
Validate the Push on Databricks
Log in to the Databricks instance and go to the
Data Ingestion
page.
Click
Amazon S3
under
Databricks connectors
. Select the External location used while configuring the plugin on Cloud Exchange.
Sample ingested alerts:
Sample ingested events:
Sample ingested Webtx logs:
Troubleshooting the Databricks Plugin
Unable to configure the plugin
It may be due to one of these reasons:
Role not assigned to the EC2 instance where Cloud Exchange is hosted in case of Deployed on AWS authentication.
Incorrect credentials in case of IAM roles anywhere authentication.
What to do
:
In case you are using Deployed on AWS authentication then refer to the
Deployed on AWS authentication
section
In case you are using IAM roles anywhere authentication then refer to the
IAM Role Anywhere authentication
section.
AWS S3 bucket region mismatch
If you see the error AWS S3 bucket exists but is in region
‘{actual}’,
not the configured region ‘{configured}’, it could be due to the
AWS S3 Bucket Region Name
in the plugin configuration does not match the bucket’s actual region.
What to do
:
In the AWS S3 Console, go to the target bucket and verify its region under the bucket properties.
Update the
AWS S3 Bucket Region Name
in the plugin configuration to match the actual bucket region and save the configuration.
Known Behavior
When using the
AWS IAM Roles Anywhere
authentication method, proxy settings configured in Cloud Exchange are not forwarded to the IAM Roles Anywhere credential requests. The plugin attempts a direct connection to
rolesanywhere.{region}.amazonaws.com
. Ensure direct connectivity to this endpoint is available when using IAM Roles Anywhere behind a proxy.
The Cloud Exchange SSL Validation setting is applied only to Databricks API calls. IAM Roles Anywhere credential requests and AWS S3 (boto3) calls always use the library default SSL verification and are not affected by the Cloud Exchange SSL validation setting.
In this Topic
Databricks Plugin for Log Shipper

---
## Configure Azure Log Analytics Workspace
**URL:** https://docs.netskope.com/en/configure-azure-log-analytics-workspace/
**Last Modified:** 2026-07-13T05:09:33+00:00
**Scraped:** 2026-08-10T08:12:38.633305+00:00

Configure Azure Log Analytics Workspace - Netskope Technical Documentation
Configure Azure Log Analytics Workspace
Integrating an Azure Log Analytics workspace with Netskope enables Microsoft Graph activity logs to flow from your SharePoint environment, including commercial, GCC, and GCC High tenants into Netskope for security monitoring and threat investigation. These logs expand the data available to
Netskope Behavior Analytics
, which analyzes user activity patterns to detect insider threats, compromised accounts, and data exfiltration. Configuring this integration now ensures your environment is ready as new behavior analytics detections for Microsoft Graph activity become available.
Netskope Behavior Analytics uses Microsoft Graph activity logs to power threat detection scenarios for SharePoint. This integration enables log ingestion — Behavior Analytics detections that consume these logs will be available in a future release.
For additional use cases enabled by Microsoft Graph activity logs, refer to
Common use cases for Microsoft Graph activity logs
in Microsoft documentation.
Prerequisites
Before you configure the Azure Log Analytics workspace integration, ensure the following:
You have configured the SharePoint instance in Netskope and granted Netskope access to your Azure AD tenant. Granting access creates a service principal for the Netskope application — this is the identity that requires the
Reader
RBAC role in Step 3. If you previously granted access for this instance or for other applications, the service principal may already exist. In that case, you can provide the Workspace ID during onboarding directly.
You have an Azure account with an active subscription.
The following resource providers are registered under your subscription (navigate to
Subscription >
Click an active subscription
> Settings > Resource Providers
in the Azure portal):
microsoft.aadiam
— Required for Entra ID (Azure AD) diagnostic logs.
microsoft.insights
— Required for any diagnostic setting (core monitoring infrastructure).
You have reviewed
Cost planning estimates
and
Cost reduction for Log Analytics
in Microsoft documentation to understand potential costs associated with log ingestion.
Configure the Integration
To configure the Azure Log Analytics workspace integration follow the steps below.
Step 1: Create a Log Analytics Workspace
To create a Log Analytics workspace in Azure:
Follow
Create a Log Analytics workspace
in Microsoft documentation to create a new workspace.
Verify the workspace
Access control mode
is set to
Use resource or workspace permissions
.
If the access control mode is not set correctly, follow
Configure access control mode for a workspace
in Microsoft documentation to update it.
Step 2: Configure Diagnostic Settings
To route Microsoft Graph activity logs to the workspace:
Follow
Send logs to Azure Monitor
in Microsoft documentation to configure diagnostic settings.
Configure the diagnostic setting under
Microsoft Entra ID
, not under the Log Analytics workspace itself.
Route
MicrosoftGraphActivityLogs
to the workspace you created in Step 1.
It may take several hours and in some cases, a few days before logs begin appearing in the workspace.
Step 3: Assign Azure RBAC to the Netskope Application
To assign the
reader
role to the Netskope application:
In the Azure portal, navigate to your Log Analytics workspace.
In the left panel, select
Access control (IAM)
.
Select the
Role assignments
tab, then click
Add role assignment
.
On the
Role
tab, search for and select
Reader
, then click
Next
.
On the
Members
tab, click
+ Select members
.
In the search bar, search for
Netskope CASB API for SharePoint
and select the application.
The
Netskope CASB API for SharePoint
application only appears after you have granted Netskope access to your Azure AD tenant. If you can’t find it, complete the instance setup and grant access first, then return to this step.
Click
Review + assign
to complete the role assignment.
Step 4: Provide the Workspace ID in Netskope
To complete the configuration in the Netskope tenant:
Navigate to
Settings > Configure App Access > Next Gen > CASB API
and edit the
Setup Instance
page for Microsoft 365 SharePoint.
Under
Azure Log Analytics Workspace ID
, enter the workspace ID of the Log Analytics workspace you created. You can find the workspace ID in the Azure portal under your Log Analytics workspace >
Overview
>
Workspace ID
.
Click
Save
.
Editing the
Workspace ID
triggers a regrant for re-authentication. Netskope validates the Workspace ID after the grant is completed. The regrant does not trigger a re-scan of your SharePoint account; your existing Inventory is preserved.
Once saved, Netskope begins ingesting Microsoft Graph activity logs from your Azure Log Analytics workspace. These logs are used by
Netskope Behavior Analytics
to power threat detection for your SharePoint environment. Detections that leverage these logs will be available in a future release.
In this Topic
Configure Azure Log Analytics Workspace

---
## New MCP Servers added to MCP Servers Catalog
**URL:** https://docs.netskope.com/en/non-cataloged-mcp-servers/
**Last Modified:** 2026-08-06T07:32:46+00:00
**Scraped:** 2026-08-10T08:13:05.262331+00:00

New MCP Servers added to MCP Servers Catalog - Netskope Technical Documentation
New MCP Servers added to MCP Servers Catalog
A set of  new MCP servers listed here have been added to the MCP Servers Catalog.
Limitations on the newly added MCP Servers
These MCP servers are not available as a part of the list of remote MCP servers for creating Real-Time Protection (RTP) policies. To create an RTP policy for any of these MCP servers, you must first create a
Destination Profile
for the specific server, and then add that profile to the RTP policy. These MCP servers are also excluded from category-based policies.
Non Catagloged MCP Servers
Adobe AEM MCP
Adobe Experience Manager MCP
Affinity MCP
AgentMail MCP
AgentNDX MCP
AIDesigner MCP
AirOps MCP
Airtable MCP
Akeneo MCP
Alkemi MCP
alphaXiv MCP
Amazon Web Services MCP
Apiiro Guardian Agent MCP
Apollo MCP
Appwrite Docs MCP
Arcadia Finance MCP
Atlan MCP
Atlassian Rovo MCP
Auth0 Docs MCP
Base44 MCP
Better Auth MCP
Bigdata.com MCP
Biorxiv MCP
Bitly MCP
Bitrefill MCP
Booking.com MCP
Braintrust MCP
Brevo MCP
Browser Use MCP
Bryntum MCP
Business Central MCP
Cala MCP
Calendly MCP
CData Connect AI MCP
Circleback MCP
Claap MCP
Clarity AI MCP
Clay MCP
ClickUp MCP
Cloudflare API MCP
Cloudflare Workers Builds MCP
Cloudinary MCP
CockroachDB Cloud MCP
CoinGecko MCP
Common Room MCP
Consensus MCP
Contentful Remote MCP
Context7 MCP
CopilotKit MCP
Cortex MCP
Coupler.io MCP
Craft MCP
Cube MCP
Customer.io MCP
Cypress Cloud MCP
Datadog MCP
DataHub MCP
DealCentre MCP
Demandbase MCP
DevCyle MCP
DevExpress MCP
Devolutions Documentation MCP
DigiCert MCP
DocBase MCP
Document360 MCP
Dovetail MCP
Drata MCP
Draup MCP
Draw.io MCP
Dropbox MCP
DX MCP
EDINET DB MCP
Egnyte MCP
Embrace MCP
Etherscan MCP
Excalidraw+ MCP
Exotel MCP
Expo MCP
Fal.ai MCP
Fast MCP
Fast.io MCP
Fathom MCP
Figma MCP
Finout MCP
Fluid Attacks MCP
freee MCP
Gamma MCP
GitLab MCP
GitMCP MCP
Glama MCP
Glean Docs MCP
Gmail MCP
GoDaddy Domains MCP
Google Calendar MCP
Google Drive MCP
Granola MCP
Greptile MCP
Guru MCP
Harness Developer Hub MCP
Hex MCP
Higgsfield AI MCP
IFTTT MCP
Incident.io MCP
Inkeep MCP
InsideOut MCP
Instacart MCP
InvertirOnline MCP
Jam MCP
Jamf Developer Portal MCP
Jina AI Remote MCP
Job Search MCP
Jotform MCP
Kaggle MCP
Kentico Content Modeling MCP
Kentico Documentation MCP
Kiwi.com MCP
Klaviyo MCP
Knock MCP
Krisp MCP
LangChain Docs MCP
LangSmith MCP
LeanIX MCP
Lenny Transcripts MCP
LiveKit Docs MCP
LogRocket MCP
Lucid Developer Documentation MCP
Magic Patterns MCP
MailerLite MCP
Marvin EU MCP
Marvin MCP
Medusa MCP
Mem MCP
Mem0 MCP
Mermaid Chart MCP
Microchip MCP
Microsoft 365 Enterprise MCP
Microsoft Fabric MCP
Microsoft Sentinel MCP
Mintlify MCP
Monte Carlo MCP
Morningstar MCP
MoSPI MCP
Mural Pay API MCP
Music Studio MCP
N8n MCP
Netskope MCP
New Relic MCP
Nimble MCP
OneTrust Developer Portal MCP
OpenAI Docs MCP
OpenFGA MCP
OpenZeppelin Cairo Contracts MCP
OpenZeppelin Solidity Contracts MCP
OpenZeppelin Stellar Contracts MCP
OpenZeppelin Stylus Contracts MCP
Otter MCP
PagerDuty MCP
PandaDoc MCP
Parallel Task MCP
Pganalyze MCP
Pipeworx MCP
PixelLab MCP
Plane MCP
Port MCP
PostHog MCP
Privy Docs MCP
prompts.chat MCP
PubMed MCP
Pylon MCP
Quartr MCP
Raygun MCP
Read AI MCP
ReadMe Documentation MCP
Readwise MCP
Redpanda Docs MCP
Render MCP
Sanity MCP
Scalar MCP
Scalr MCP
Scholar Gateway MCP
Scholar Sidekick MCP
Semrush MCP
SFR Analytics MCP
Sigma Computing MCP
SignNow MCP
SimilarWeb MCP
Sitecore Marketer MCP
Slack MCP
Slite MCP
Smartsheet MCP
Socket MCP
Solo.io Docs MCP
Sourcegraph MCP
Sportradar MCP
Stack Overflow MCP
Storyblok MCP
Subframe MCP
Supermetrics MCP
Svelte MCP
ThoughtSpot MCP
ThousandEyes MCP
Thumbtack MCP
TicketLens MCP
TickTick MCP
Tldraw MCP
Topsort Analytics MCP
Topsort Documentation MCP
Tredict MCP
Trivago MCP
Unblocked MCP
Vaadin MCP
Vantage MCP
VedAstro MCP
VidIQ MCP
Vuetify MCP
Windsor.ai MCP
Wiz MCP
WordPress.com MCP
Workable MCP
Wrike MCP
Wyndham Hotels & Resorts MCP
Yargı MCP
YokTez MCP
You.com MCP
Zoho MCP
ZoomInfo MCP
In this Topic
New MCP Servers added to MCP Servers Catalog

---
## Log Streaming
**URL:** https://docs.netskope.com/en/log-streaming/
**Last Modified:** 2026-04-27T21:31:56+00:00
**Scraped:** 2026-08-10T08:13:51.712556+00:00

Log Streaming - Netskope Technical Documentation
Log Streaming
Log Streaming requires additional licensing. Contact your Netskope account team to enable it in your account.
Log Streaming Overview
To guarantee reliable data delivery, the Log Streaming pipeline employs automatic retransmission when delivery acknowledgment from the target bucket is not received within the expected window. Customers should anticipate up to 0.1% duplicate events at the SIEM destination as a consequence of this reliability mechanism.
Netskope Log Streaming allows you to access all Netskope-generated logs directly within your preferred cloud storage and further SIEM tools without the need for additional infrastructure like VMs, improving scalability, cost efficiency, and real-time data availability.
This solution eliminates the need for customers to manage additional infrastructure like VMs for log ingestion, reducing complexity, cost, and operational overhead. It also addresses scalability challenges, enables real-time log ingestion, and allows logs to be delivered to preferred cloud destinations, ensuring easier access and analysis within existing security and compliance workflows.
The following is the general procedural flow to launch your stream:
Configuring Streams
: Name and properties you want to stream
Choosing Data Sets
: Data parameters you want to log to the destination
Configuring Destinations
: Configure the destination to stream log files
Activating Streams
: Enable the configured stream
Once a stream is enabled, it appears in the stream control panel.
In this Topic
Log Streaming
