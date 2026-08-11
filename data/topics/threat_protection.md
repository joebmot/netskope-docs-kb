# Netskope Docs — Threat Protection
_Generated: 2026-08-11 08:11 UTC_
_Pages: 83_

---
## Advanced Threat Protection
**URL:** https://docs.netskope.com/en/advanced-threat-protection/
**Last Modified:** 2025-08-31T01:51:23+00:00
**Scraped:** 2026-08-11T06:59:34.497991+00:00

Advanced Threat Protection
Protect against unknown malicious websites
Protect against unknown web threats
Protect against viruses and malicious files
Protect against network-based attacks
Protection against Insider threats
Protect against Unmanaged S3 access
Shadow IT – Identifying unsanctioned AWS accounts using Skope IT
Control AWS apps using Instance IDs
Shadow IT – Identifying unsanctioned AWS accounts using Advanced Analytics
In this Topic
Advanced Threat Protection

---
## Identify Malware in data repositories and action per defined policy
**URL:** https://docs.netskope.com/en/identify-malware-in-data-repositories-and-action-per-defined-policy/
**Last Modified:** 2025-09-01T12:59:19+00:00
**Scraped:** 2026-08-11T07:01:06.352307+00:00

Identify Malware in data repositories and action per defined policy - Netskope Technical Documentation
Identify Malware in data repositories and action per defined policy
Prerequisites for the API protection use cases
Roles/actors in the use cases
Tenant creation
User accounts created
CASB API Protection connected to CSP (Cloud Service Provider)
CSP (Cloud Service Provider) administrator
Cloud governance team
Security Analyst
To enable malware scan in data repositories which are API protected services, follow the steps shown below:
Navigate to Settings > Threat Protection > API enabled protection.
Under Settings, click ‘Edit’ and select the options for actions to be taken based on severity of the malware.
Enable the Malware scans for instances of the API protected services.
Edit Settings:
To learn more:
Understanding API Protection
In this Topic
Identify Malware in data repositories and action per defined policy

---
## Protect against unknown web threats
**URL:** https://docs.netskope.com/en/protect-against-unknown-web-threats/
**Last Modified:** 2025-08-31T01:51:24+00:00
**Scraped:** 2026-08-11T07:01:35.034627+00:00

Protect against unknown web threats - Netskope Technical Documentation
Protect against unknown web threats
Netskope Remote Browser Isolation (RBI) isolates uncategorized and risky websites as an option for Netskope Secure Web Gateway (SWG) solutions. Known safe sites are allowed, known bad sites are blocked, and
risky websites are isolated for safe viewing
all within one cloud platform, one console, and one policy engine.
Follow the steps shown below to configure RBI:
Enable the RBI feature in your tenant.
Configure an isolation policy to forward traffic from selected categories to RBI using the “Isolate” action.
Remote Browser Isolation shows in the tab title.
Netskope icon will flutter as the page renders.
Once rendered there will be a star (*) in the browser tab title.
RBI Page event view:
In this Topic
Protect against unknown web threats

---
## Protection against Insider threats
**URL:** https://docs.netskope.com/en/protection-against-insider-threats/
**Last Modified:** 2025-08-31T01:51:25+00:00
**Scraped:** 2026-08-11T07:01:38.672791+00:00

Protection against Insider threats - Netskope Technical Documentation
Protection against Insider threats
Insider threats refer to security risks caused by malicious users within a corporate network. In the case of a malicious insider, the user typically is acting with intent and likely knows that they are breaking policy and potentially the law.
User and Entity Behavior Analytics (UEBA) products focus on monitoring both suspicious user behavior as well as other entities such as device, cloud application, data activity, and malicious threats across time and peer group.
UEBA helps to:
Focus on a typical “blind spot” which is Insider Threats
Better Manage Risk: Allows focus on the riskiest users & their activities
Enable prioritization and effective response – Actionable Security
Understand User Intent, and/or find a Compromise quickly
Advanced UEBA which is now available with R90 has 9-rule based detections, ML-based detections, UCI (User Confidence Index) in addition to efficiencies, new performance benchmarks and ease of use features.
Rule based detections:
ML-Based detections:
User Confidence Index Time based view:
To learn more:
Behavior Analytics
,
Behavior Analytics Detection Scenarios
In this Topic
Protection against Insider threats

---
## Threat Protection – Protect state for Managed App Activities
**URL:** https://docs.netskope.com/en/threat-protection-protect-state-for-managed-app-activities/
**Last Modified:** 2025-09-01T13:11:31+00:00
**Scraped:** 2026-08-11T07:01:54.839908+00:00

Threat Protection – Protect state for Managed App Activities
Identify Malware in data repositories and action per defined policy
In this Topic
Threat Protection – Protect state for Managed App Activities

---
## Threat scan on IaaS Storage
**URL:** https://docs.netskope.com/en/threat-scan-on-iaas-storage/
**Last Modified:** 2025-08-31T01:51:11+00:00
**Scraped:** 2026-08-11T07:01:56.155900+00:00

Threat scan on IaaS Storage - Netskope Technical Documentation
Threat scan on IaaS Storage
To enable threat scan on IaaS storage, navigate to
Settings
>
Threat Protection > API-enabled Protection
. Turn on the malware scan for the specific instance of the IaaS Storage.
To view the results of the malware scan, navigate to
Skope IT
>
Alerts
and set the ‘Alert_type’ to Malware in the filter.
In this Topic
Threat scan on IaaS Storage

---
## Threat Protection Features
**URL:** https://docs.netskope.com/en/threat-protection-features/
**Last Modified:** 2025-08-31T01:51:01+00:00
**Scraped:** 2026-08-11T07:01:57.346092+00:00

Threat Protection Features - Netskope Technical Documentation
Threat Protection Features
Feature
Description
Threat intelligence for malicious sites
Use 40 threat intelligence feeds to identify malicious sites that your employees may be visiting and block them. Threat intelligence is updated dynamically using multiple sources. You can also create your own threat list (e.g., URLs, hashes, etc.) using
Threat Exchange
.
Anomaly detection
Identify and remediate anomalous user behavior such as compromised credentials, data exfiltration, insider threats, privileged account access abuse, and more.
Cloud malware protection and remediation
Detect and block or quarantine infected files and replace with tombstone files. Remediation options include blocking and quarantining as well as analysis and response workflows. Layered detection approach includes static and heuristic analysis, machine learning, and sandboxing.
In this Topic
Threat Protection Features

---
## Advanced Threat Protection
**URL:** https://docs.netskope.com/en/advanced-threat-protection-86194/
**Last Modified:** 2025-09-03T18:23:15+00:00
**Scraped:** 2026-08-11T07:02:57.382677+00:00

Advanced Threat Protection - Netskope Technical Documentation
Advanced Threat Protection
Netskope Advanced Threat Protection includes multiple detection engines that detect sophisticated zero day threats and targeted attacks. The comprehensive, multi-engine approach ensures higher efficacy and protection against evasive threats that may be optimized to bypass some detection engines.
Advanced Threat Protection is not offered for applications accessed through China PoPs.
The Netskope Advanced Threat Protection solution includes:
Deobfuscation and recursive file unpacking with support for 350+ families of installers, packers, and compressors.
Pre-execution analysis and heuristics for 3,500+ file format families, with 3,000+ static binary threat indicators for Windows, Mac OS, Linux, iOS, Android, firmware, Flash, PDF, and other document types.
Cloud Sandboxing for 30+ file types, including Portable Executables, Microsoft Office, PDF files, batch files, unicode text files, archive files, Microsoft Visio, RTF, Flash, HTML, Java Applets, and other file formats. For example:
Archives
7-Zip (.7z)
Lempel–Ziv Finite State Entropy (.lzfse)
Python Wheel (.whl)
Roshal Archive (.rar, .rev)
Tape Archive (.tar)
ZIP Archive (.zip)
Web Application Archive (.war)
Windows App Package Format (.msix)
Certificates (.pem, .crt, .cer, .key)
Executables
Microsoft Software Installer (.msi)
Windows Executable (.exe)
Microsoft Office
Microsoft Access (.accdb, .mdb)
Microsoft Compiled HTML Help (.chm)
Microsoft Excel (.xlsx, .xlsm)
Microsoft OneDrive (.one)
Microsoft Outlook (.msg, .mbx)
Microsoft PowerPoint (.pptx, .pptm)
Microsoft Silverlight (.xap)
Microsoft Word (.docx, .docm)
Mobile
Android Application Package (.apk)
Dalvik Executable Format (.dex)
Text-Based File Formats
Comma-Separated Values (.csv)
Email File (.eml)
Extensible Markup Language (.xml, .sgm)
Hypertext Markup Language (.html, .htm, .xhtml)
JavaScript Object Notation (.json)
Portable Document Format (.pdf)
Tab-Separated Values (.tsv)
Text File (.txt)
Web Content
Adobe Flash (.swf)
Java (.jar)
MHTML Web Archive File (.mht)
XPInstall (.xpi)
Windows Files
Windows Batch File (.bat)
Windows Command Prompt (.cmd)
Windows Shortcut File (.lnk)
Machine learning deep analysis to detect unknown threats, anomalies, and behaviors, with ML models for PEs, PDFs, malicious Office files, and malicious URLs in files.
Patient zero alerts, Sandbox API, RetroHunt API, and MITRE ATT&CK sandboxing analysis.
Patient zero protection by holding files until Netskope finishes sandboxing.
Malware Retention profile to retain files detected as malicious in your designated location for SOC analysis.
Third-party sandbox integration for secondary detonations and verdicts.
Advanced Threat Protection enables engines in deep scan that overcome the limitations of traditional signature-based detection techniques:
Detects unknown malware (dynamic vs signature based).
Performs dynamic analysis, which can determine indicators of compromise (IOCs) such as command and control (C2) domains, IPs, endpoint registry keys, created files, etc. IOCs can be used to detect the next occurrences of the same malware without re-analyzing the artifact.
Patient zero
alerts provide zero day detection alerts and
patient zero protection policy
releases unknown files to users only after the Netskope advanced threat scanning engines determine they’re benign. Netskope holds the unknown file and notifies the user that it’s analyzing the file until it determines a verdict. The Netskope advanced threat engines can take up to 10 minutes (~2 min typical) to analyze the file after which the file will be blocked or allowed for the user.
REST APIs for integrating into typical security operations center (SOC) workflows.
RetroHunt API provides an API that allows you to query detections by hash (e.g., MD5 and SHA-256) if the file is seen (whether malicious or benign) in traffic within the Netskope account. Additionally, you can obtain a report for the detections and verdicts by the different engines. To learn more, go to
Settings
>
Tools
>
REST API v2
in your Netskope tenant, and then click the
API Documentation
.
Sandbox file submission API. Allows submitting files and retrieving a detailed analysis report from the sandbox.
Malware Retention profile
enables
retention of a malware sample
detected as malicious in inline user traffic in a customer designated IaaS cloud location. The malware sample can be retrieved at a later time for additional analysis. The Retention location can be customized and file will be protected (zip/password)
ATP alerts appear on the
Malware
page.
Configuring Advanced Threat Protection Integrations
To enable this feature, contact
Netskope Support
.
The Netskope cloud platform has threat protection capabilities, including advanced threat detection engines, such as heuristic analysis, sandbox analysis, and ransomware detection and remediation.
You can also leverage some of your existing, trusted threat detection products like
Palo Alto Networks Wildfire
,
Juniper SkyATP
, and
Check Point SandBlast
to work with Netskope ATP. You must have the Advanced Threat Protection license.
After integration, verify the status is green. Go to
Settings > Threat Protection > Integration
. Under
Advanced Threat Protection
look for a green arrow besides
Status
. Verifying the status is green ensures that blocklisted and allowlisted files are included in your Ransomware detection scan.
The file types Palo Alto Networks Wildfire supports are:
Android application package (APK) files
Adobe Flash files Archive (RAR and 7-Zip) files
Java Archive (JAR) files
Microsoft Office files
Portable executable (PE) files
Portable document format (PDF) files
Mac OS X files
Linux (ELF) files
In this Topic
Advanced Threat Protection

---
## Creating a Malware Detection Profile
**URL:** https://docs.netskope.com/en/creating-a-malware-detection-profile/
**Last Modified:** 2025-09-03T18:23:18+00:00
**Scraped:** 2026-08-11T07:05:55.582242+00:00

Creating a Malware Detection Profile - Netskope Technical Documentation
Creating a Malware Detection Profile
You can extend the default Netskope malware scan by creating custom malware detection profiles. In the malware detection profile, you can select the
file profile
as an allowlist or a blocklist. For example, you can include known malicious hashes sourced from other intelligence sources in the blocklist. You also can add known good files (e.g., proprietary content specific to the organization) to the allowlist so Netskope does not flag them as suspicious.
To create a malware detection profile:
Go to
Policies
>
Threat Protection
.
In the
Malware Detection Profiles
tab, click
New Malware Detection Profile
.
Under
Threat Scan
, click
Next
. The Netskope malware scan is selected by default. You can’t modify this field.
Under
Allowlist
, select the
file profile
that’s associated with the files you want to allow in your organization. You also can search for a profile.
Click
Next
.
Under
Blocklist
, select the
file profile
that’s associated with the files you want to block in your organization. You also can search for a profile.
Click
Next
.
Under
Set Profile
, enter a name for the profile.
Click
Save Malware Detection Profile
.
Click
Apply Changes
.
You can select the custom malware detection profile when configuring the
Real-time Protection policy
.
In this Topic
Creating a Malware Detection Profile

---
## Creating a Threat Protection Policy for API Data Protection
**URL:** https://docs.netskope.com/en/creating-a-threat-protection-policy-for-api-data-protection/
**Last Modified:** 2025-09-03T18:23:17+00:00
**Scraped:** 2026-08-11T07:05:56.926344+00:00

Creating a Threat Protection Policy for API Data Protection - Netskope Technical Documentation
Creating a Threat Protection Policy for API Data Protection
Netskope can scan files stored in your cloud storage applications for malware. To do this, you must configure the API Data Protection settings and enable malware scanning for your application instances.
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
– With larger files, there may be an increased end to end latency for policy processing.
– Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
Prerequisites
Before configuring threat protection for API Data Protection, ensure you:
Enable malware scanning in an API Data Protection app instance. Go to
Settings > Configure App Access > Classic > SaaS
, and select an existing app instance. In the
Edit Setup
window, under Instance Type, select
Malware
. Repeat for all app instances you want to perform malware scanning.
Create a
quarantine profile
.
Configure Threat Protection for API Data Protection
To configure threat protection for API Data Protection:
In the Netskope tenant UI, go to
Settings
>
Threat Protection
>
API-enabled Protection
.
Under
Settings
, click
Edit
to configure your malware settings.
In the
Edit Settings
window:
Low Severity Action
: Choose the action you want to take for low severity malware. Netskope recommends choosing
Alert
.
Alert
: Select to generate a
Skope IT alert
.
Quarantine
: Select to quarantine the file. Netskope zips/compresses the password-protected file and notifies the specified users.
Medium Severity Action
: Choose the action you want to take for medium severity malware. Netskope recommends choosing
Alert
.
Alert
: Select to generate a
Skope IT alert
.
Quarantine
: Select to quarantine the file. Netskope zips/compresses the password-protected file and notifies the specified users.
High Severity Action
: Choose the action you want to take for high severity malware. Netskope recommends choosing
Quarantine
.
Alert
: Select to generate a
Skope IT alert
.
Quarantine
: Select to quarantine the file. Netskope zips/compresses the password-protected file and notifies the specified users.
Quarantine Profile
: If you chose the
Quarantine
action, choose the
quarantine profile
used to store the files infected with malware.
You can only use one quarantine profile for a specific app to store the malicious files. For example, if you create a quarantine profile on Box, Netskope will use it to quarantine malicious files for the rest of the app instances with
Enable Malware Scan
selected (see Step 5).
File ZIP Password
: Enter a password for the ZIP file. Netskope quarantines and protects infected files with this password to prevent users from accidentally downloading infected files to their device.
Notify
: Select who to send an email notification when Netskope quarantines malicious files.
The notification email cannot be customized.
A sample email notification is as follows:
Users in quarantine profile
: The users or admins specified in the associated
quarantine profile
.
Owner
: The owner of the file.
Admin
: All
tenant admins
configured for your organization.
Collaborators
: The collaborators of the file.
Screenshot of the
Edit Settings
page:
Click
Save
.
Under
Malware Instances
, select
Enable Malware Scan
for the app instances you want to perform malware scanning.
Netskope has removed the
Malware Instances
table under
Settings > Threat Protection > API-enabled Protection
. Users can avail the same functionality to enable malware from
Settings > Configure App Access > Classic > SaaS
, enable the malware checkbox under
Setup Instance
.
You can view scanned malware for your app instances on the malware and malicious sites pages.
In this Topic
Creating a Threat Protection Policy for API Data Protection

---
## Creating a Threat Protection Policy for Patient Zero
**URL:** https://docs.netskope.com/en/creating-a-threat-protection-policy-for-patient-zero/
**Last Modified:** 2026-01-14T18:59:52+00:00
**Scraped:** 2026-08-11T07:05:59.340851+00:00

Creating a Threat Protection Policy for Patient Zero
A patient zero event occurs when a user downloads a file that’s not detected by signature-based analysis (e.g., Netskope AV engine) in Standard Threat Protection. However, if you have Advanced Threat Protection, you can prevent patient zero events by creating a Threat Protection policy that only releases unknown files to users after the Netskope advanced threat engines determine they’re benign. Netskope holds the unknown file and notifies the user that it’s analyzing the file until it determines a verdict. The Netskope advanced threat engines can take up to 10 minutes to analyze the file.
Netskope recommends using patient zero policies for high risk use cases, such as the following:
Risky file types (file type constraint)
Risky users (low Behavior Analytics User Confidence Index)
Risky application (low Cloud Confidence Index)
Risky locations
Unknown websites
A combination of the above cases.
This policy complements the inline ML-based Portable Executable (PE) classifier in Standard Threat Protection that detects and prevents zero-day threats.
To create a Threat Protection policy that prevents patient zero events:
Go to
Policies
>
Real-time Protection
.
Click
New Policy
and then
Threat Protection
On the
Real-time Protection
Policy
page:
Source
: Select the users, user groups, or organizational units you want to apply the patient zero policy to. Click
Add Criteria
to add other sources.
Destination
: Select the traffic destination you want to apply the patient zero policy to. You can scan traffic for URL categories, cloud apps, app instances, or any web traffic with a specific Cloud Confidence Level (CCL), application tag, or country destination.
For
Category
, select risky categories that aren’t already blocked in security risk, such as Newly Released Domains, Newly Observed Domains, Uncategorized, Parked domains, Unreachable, Miscellaneous, and Web Hosting, ISP & Telco.
For
Activities
, select
Download
and
Upload
. Click
Add Criteria & Constraints
. Go to
Activity Constraints
>
File Type
. For
File Should
, ensure it’s
match
. For
File Type
, click
Select File Type
.
In the
Select File Type
window, select
Binary and Executable
,
Spreadsheet
, and
Word Processor
. Netskope recommends creating a patient zero policy for these high risk file types. You can select more file types if needed.
Profile & Action
: Configure the following.
Th
reat Protection Profile
: Ensure it’s
Default Malware Scan (predefined)
. You can’t edit the default malware scan profile or add more profiles with the default profile.
Severity-Based Actions
: Edit each severity level and select
Block
for the
Action
.
Block till benign verdict by dynamic threat analysis
: Select to block users from uploading or downloading a file until Netskope dynamic threat analysis provides a benign verdict. The analysis can take up to 10 minutes.
Set Policy
: Enter a policy name. You can only use alphanumeric characters and symbols such as underscore (_), dash (-), and square brackets ([ ]). You cannot use the greater-than (>) or less-than (<) symbols in policy names.
+ Policy Description
: Click to add notes or information.
+ Email Notification
: Netskope doesn’t send email-based notifications for patient zero events. To learn more:
Viewing Patient Zero Events
.
Click
Save
.
In the
Move Policy
window, move the policy
To the top
. Patient zero policies must be above all other threat protection policies.
Click
Save
.
Click
Apply Changes
.
After creating a patient zero policy, you can use the
Policy
alert type to view the matched patient zero policy alerts on the Skope IT Alerts page. To learn more:
Viewing Patient Zero Events
.
End User Notifications & Custom Languages
While Advanced Threat Protection scans the file for patient zero, Netskope displays a notification to the user that the file needs additional scanning. Netskope automatically customizes this based on the OS/browser language. The default language is English, and the other supported languages include:
German
Spanish
French
Italian
Japanese
Chinese
Korean
Portuguese
Brazilian
In this Topic
Creating a Threat Protection Policy for Patient Zero

---
## Improved Reporting on Malware Files in API Data Protection
**URL:** https://docs.netskope.com/en/improved-reporting-on-malware-files-in-api-data-protection/
**Last Modified:** 2025-09-04T01:12:02+00:00
**Scraped:** 2026-08-11T07:08:25.735481+00:00

Improved Reporting on Malware Files in API Data Protection - Netskope Technical Documentation
Improved Reporting on Malware Files in API Data Protection
API Data Protection dashboard page now includes additional information about the MD5 checksum on malware as well as details if the malware was detected by Netskope or the SaaS application. Filtering capabilities on the newly available data is also added.
The current malware section on the API dashboard is now enhanced to provide more information about how Netskope calculates the  malware count and provide more malware metadata such as
MD5
checksum and
Detection Type
for files listed as malware on the dashboards’ file listing page.
As part of this enhancement, following changes are introduced:
The following screenshots and enhancements are taken from a Google Drive app instance. However, these enhancements are applicable for all supported storage apps.
Log in to the Netskope UI tenant, click
API-enabled Protection > SAAS
on the left navigation pane. The panel displays a list of apps. Click the desired app to view the app-specific dashboard statistics.
Added a tool-tip to explain how the malware count is calculated on the API-enabled Protection dashboard page.
How does Netskope calculate the malware file count on the API-enabled Protection dashboard?
The malware files count here only denotes the count of malware identified via API integrations to this specific SaaS application instance. Malware detected using other access methods are not included in this count. For malware detected by Netskope, navigate to
Incidents > Malware
.
For customers with threat protection enabled, the malware files count on the API-enabled Protection dashboard shows the combined malware files count from threats detected by the native SaaS app + threats detected by the Netskope threat engine.
For customers with no threat protection enabled, the malware files count on the API-enabled Protection dashboard shows the malware files count from threats detected by the native SaaS app only.
Renamed
Malware File
filter to
Malicious
. Added
MD5
checksum and
Detection Engine
filters.
The
MD5
checksum and
Detection Engine
filters are available only when
Malicious
filter is set to
Yes
.
The detection engine filter has the following sub-filters:
Native App
Netskope AV
Netskope Advanced Heuristic Analysis
Netskope Cloud Sandbox
Netskope Threat Intelligence
Added
MD5
checksum of the identified malware file and
Detection Engine
fields on the
File Details
page
You can click the magnifying glass icon to lookup the incident. The page redirect to
Incidents > Malware
.
Added a tooltip to explain how the malware count is calculated on the
Incidents > Malware
page.
The total malware count below is a combined count of all malware detected by Netskope across all access methods. The total count does not include malware detected by native SaaS apps.
In this Topic
Improved Reporting on Malware Files in API Data Protection

---
## Malware and Malicious Sites Pages
**URL:** https://docs.netskope.com/en/malware-and-malicious-sites-pages/
**Last Modified:** 2025-09-03T18:23:21+00:00
**Scraped:** 2026-08-11T07:08:54.225035+00:00

Malware and Malicious Sites Pages - Netskope Technical Documentation
Malware and Malicious Sites Pages
The malware and malicious sites pages help you manage threats to your network.
Malware
Malicious Sites
Reporting False Positives
In this Topic
Malware and Malicious Sites Pages

---
## API Source Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/api-source-plugin-for-threat-exchange/
**Last Modified:** 2025-08-31T01:53:26+00:00
**Scraped:** 2026-08-11T07:15:25.005150+00:00

API Source Plugin for Threat Exchange - Netskope Technical Documentation
API Source Plugin for Threat Exchange
The following document explains how to configure the Threat Exchange API Source Plugin for Cloud Exchange. The API Source plugin allows you to integrate virtually any third-party technology invoking an API endpoint to share IoCs, such as hashes and URLs from the third-party to a specific technology, and allow the API Source to read the IoCs managed by Threat Exchange.
Configure the API Source Plugin
To enable the API Source plugin, in Cloud Exchange go to
Settings > Plugins
, and then search for and select the
API Source (CTE)
plugin box. Once configured this will enable the API interface to manage the Indicators of Compromise.
Enter these parameters:
Configuration Name: this parameter is used not only to provide a name for the configuration, but it is also a mandatory parameter that must be provided in the
source field
of the POST request to the API endpoint used to create an IoC entry (
/api/cte/indicators/
).
Aging Criteria: Set the expiration time (in days) for the indicator.
Override Reputation: Set whether to override the reputation of the indicators received from this configuration. Set 0 to keep the default.
Enable SSL Verification: Set whether to check the certificate of the SSL connection used to exchange the IoCs.
Use System Proxy: set this parameter if you have configured a proxy for the Cloud Exchange and you want this plugin to use the same proxy.
When finished, click
Save
. After saving the configuration, you will see this plugin under the
Threat Exchange > Plugin
section.
Create an API Token
After enabling the plugin, you need to configure an API token. Go to
Settings > Users > API Tokens
and click Create New Token’:
Enter a Token Description and an expiration time, and then click
Create
.
After the token is created, you will see it under
Settings > Users > API Tokens
. Please note that the token is composed of a Client ID (visible) and Client Secret (can be copied using the button). These parameters are needed to authenticate the API call to read or update the IoCs in Cloud Exchange.
Share the IoCs from an API Source to a Netskope Tenant
As an example, if your use case requires sharing of IoCs from the API Source to a Netskope tenant, you need to specify the Netskope tenant, a business rule, and a sharing configuration.
Configure the Netskope Tenant
To specify a Netskope tenant, go to
Settings > Netskope Tenant
and click
Add Tenant
.
Enter these parameters:
Name: Enter a name for this tenant configuration name.
Tenant Name: Enter the tenant name (do not include goskope.com).
V1 API Token: Enter the V1 API token, available from your Netskope tenant under
Settings > Tools > Rest API v1
.
V2 API Token (optional): Enter the V2 API token, available from your Netskope tenant under
Settings > Tools > Rest API v2
.  Be sure to provide the proper permission to the token.
Initial Range (in days): Enter the number of days for which data must be pulled during the initial run.
Use System Proxy: Set this parameter if you have configured a proxy for the Cloud Exchange and you want this plugin to use the same proxy.
Click
Save
.
Configure a Netskope Plugin for Threat Exchange
In Cloud Exchange go to
Settings > Plugins
and click
Netskope v1.0.0.0 (CTE)
.
Enter these Basic Information parameters :
Configuration Name: Enter a name for this plugin.
Tenant: insert the tenant configuration name that you have defined when you have created the Netskope tenant.
Aging Criteria: Set an expiration time (in days) for the indicator
Override Reputation: set this parameter to override the reputation of the indicators received from this configuration. Set 0 to keep the default.
Click
Next
and enter the Configuration Parameters:
Enable Polling: Enable or disable polling data from Netskope.
Type of Threat Data: Select the data you want to share with this plugin. Possible values are: Malware, URL, or Both.
Click
Save
.
After saving the plugin configuration, you will see the configured plugin under
Threat Exchange > Plugins
.
Create a Business Rule
Before configuring a sharing configuration, you need to define a Business Rule, which decides the criteria to share the IoCs between the two configurations. To do so, go to T
hreat Exchange > Business Rules
and click
Create New Rule
. For example, the business rule below, called Every Severity, selects the IoCs with all the possible severities.
Enter a Rule Name.
Select the rules to use.
Click
Save
.
Create a Sharing Configuration
To create a sharing configuration, go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
:
Enter these parameters:
Source Configuration: Enter a configuration name for the ‘API Source’ plugin you configured previously. Remember that the ‘API Source’ plugin can only push IoCs to a third-party. If you want to read the IoCs from the Threat Exchange, use the corresponding GET method for the
/api/cte/indicators/
endpoint below. This means that you cannot insert an API Source as a destination configuration.
Business Rule: Select the Business Rule that you have defined previously and that states which indicators must be shared.
Destination Configuration: insert the configuration of the Netskope tenant that you have defined previously.
Target: Define the list where you want to insert the indicators of compromise. It is possible to define a URL list or a hash list. Please do note that the lists must be defined in the Netskope tenant.
Custom URL lists can be defined from
Policies > Profiles > Web > URL Lists
. A URL list must be inserted into a custom category to be enforced in a policy.
Custom file profiles can be defined from
Policies > Profiles > File
. A file profile must be inserted into a custom malware profile to be inserted in a policy.
List Name: Enter the name of the list (URL or file) where you want the indicator to be inserted.
List Size: Enter a size for the list (default is 8Mb).
Default URL/File Hash: Enter the default list where the indicator must be inserted when the List Name field is empty.
Click
Save
.
API Documentation
If you want to test the API, the documentation is available inside the Cloud Exchange interface at (
Help > API Docs
):
https://
<Cloud Exchange IP>
/api/docs#/Indicators
. In particular,the following endpoints are relevant:
GET
/api/cte/indicators/
: List the Indicators.
POST
/api/cte/indicators/
: Insert/update multiple indicators.
PATCH
/api/cte/indicators/
: Update a single indicator.
GET
/api/cte/dashboards/
: Get aggregated results from indicators.
DELETE
/api/cte/indicators/bulk
: Bulk delete indicators.
PATCH
/api/cte/indicators/bulk
: Bulk update indicators.
GET
/api/cte/tags
: Get configured tags from tenant
POST
/api/cte/tags
: Create new tags (globally)
DELETE
/api/cte/tags:
Delete tags (globally)
Examples of using the API to POST and PATCH IoCs
In this example an IOC is being pushed using POST to add an URL indicator,
www.dubya.com
, to an API plugin created and named
DW
. It has 2 tags associated with it that were already in the tenant – “
test_tag
” and “
test_tag2
”. If adding multiple tags, they must each be in their own open and close quotation marks, separated by a comma.
If you wish to POST IoC with tags, you need to create the tags ahead of time, either via the GUI or API.
To update an IoC with new data, use PATCH. In the example below, the IoC has had its reputation increased from 5 to 7.
Note that there are no additional tags added in this example.
Tags can be removed in the GUI or via the API using the
remove
command issued with a PATCH to endpoint
api/cte/indicators/bulk
. In the example below, the tag “
abc
” is removed from indicator “
b53f3c0cd32d7f20849850768da6431e5f876b7bfa61db0aa0700b02873393fa
“.
In this Topic
API Source Plugin for Threat Exchange

---
## AWS GuardDuty Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/aws-guardduty-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:39:24+00:00
**Scraped:** 2026-08-11T07:15:26.264196+00:00

AWS GuardDuty Plugin for Threat Exchange - Netskope Technical Documentation
AWS GuardDuty Plugin for Threat Exchange
This document explains how to configure the AWS GuardDuty integration with the Cloud Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches URLs (IPv4 and Domain) and Hash (SHA256) from the AWS GuardDuty platform. This plugin does not support pushing indicators to AWS GuardDuty.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Netskope Threat prevention subscription for malicious file hash sharing.
Access to your AWS Access Key ID (Public Key), AWS Secret Access Key (Private Key), AWS Session Token (Optional, only for temporary user), Region Name, and Detector ID (Unique Detector ID).
AWS GuardDuty Plugin Support
Fetched indicator types
URLs (IPv4 and Domain), SHA256
Shared indicator types
None
Mappings
Severity Mapping
Netskope Severity
AWS GuardDuty Severity
<1
Unknown
1.0 – 3.9
Low
4.0 – 6.9
Medium
7.0 – 8.9
High
9.0 – 10.0
Critical
Mappings for Pull (Netskope field – AWS GuardDuty fields)
Netskope Cloud Exchange indicator Field
AWS GuardDuty Field
value
EbsVolumeScanDetails Mapping
Service.EbsVolumeScanDetails.ScanDetections.ThreatDetectedByName.ThreatNames.FilePaths.FileName.Hash
NetworkConnectionAction Mapping
Service.Action.NetworkConnectionAction.RemoteIpDetails.IpAddressV4
PortProbeAction Mapping
Service.Action.PortProbeAction.PortProbeDetails.RemoteIpDetails.IpAddressV4
DnsRequestAction Mapping
Service.Action.DnsRequestAction.Domain
type
EbsVolumeScanDetails Mapping
SHA256
NetworkConnectionAction Mapping
URL
PortProbeAction Mapping
URL
DnsRequestAction Mapping
URL
firstSeen
EbsVolumeScanDetails Mapping
Service.EventFirstSeen
NetworkConnectionAction Mapping
Service.Action.EventFirstSeen
PortProbeAction Mapping
Service.Action.EventFirstSeen
DnsRequestAction Mapping
Service.Action.EventFirstSeen
lastSeen
EbsVolumeScanDetails Mapping
Service.EventLastSeen
NetworkConnectionAction Mapping
Service.Action.EventLastSeen
PortProbeAction Mapping
Service.Action.EventLastSeen
DnsRequestAction Mapping
Service.Action.EventLastSeen
severity
EbsVolumeScanDetails Mapping
Service.EbsVolumeScanDetails.ScanDetections.HighestSeverityThreatDetails.Severity
NetworkConnectionAction Mapping
Severity
PortProbeAction Mapping
Severity
DnsRequestAction Mapping
Severity
tags
EbsVolumeScanDetails Mapping
Service.EbsVolumeScanDetails.Sources }}+ {{GuardDuty-public if PublicIp is present in NetworkInterfaces +
GuardDuty-private if PrivateIpAddress is present in NetworkInterfaces
NetworkConnectionAction Mapping
Resource.InstanceDetails.Tags +
NetworkConnectionAction.Blocked=<value>
+
GuardDuty-public if PublicIp is present in NetworkInterfaces +
GuardDuty-private if PrivateIpAddress is present in NetworkInterfaces
PortProbeAction Mapping
portProbeAction.Blocked= <value> + Resource.InstanceDetails.Tags + GuardDuty-public if PublicIp is present in NetworkInterfaces + GuardDuty-private if PrivateIpAddress is present in NetworkInterfaces
DnsRequestAction Mapping
DnsRequestAction:Blocked: <value> +Resource.InstanceDetails.Tags +GuardDuty-public if PublicIp is present in NetworkInterfaces +GuardDuty-private if PrivateIpAddress is present in NetworkInterfaces
comments
EbsVolumeScanDetails Mapping
Finding Arn: Arn,TriggerFindingId:Service.EbsVolumeScanDetails.TriggerFindingId,Name:Service.EbsVolumeScanDetails.ScanDetections.ThreatDetectedByName.ThreatNames.FilePaths.FileName.Hash.Filename
Filepath:Service.EbsVolumeScanDetails.ScanDetections.ThreatDetectedByName.ThreatNames.FilePaths.FilePath,Description:Description
NetworkConnectionAction Mapping
Finding ARN: Arn, Finding Type: Type, Description: Description
PortProbeAction Mapping
Finding ARN: Arn, Finding Type: Type, Description: Description
DnsRequestAction Mapping
Finding ARN: Arn, Finding Type: Type, Description: Description,
Permissions
Below are the permissions needed to be attached to the IAM user for the plugin workflow.
GetFindings
ListFindings
API Details
List of APIs Used
This plugin uses python (Boto3 v1.34.44) library to get findings from the AWS GuardDuty platform.
Library: The AWS SDK for python (Boto3 v1.34.44)
Usage: The AWS SDK for python (Boto3) to create, configure, and manage AWS services,
such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service
Creating a GuardDuty Client Object
guardduty_client = boto3.Session(
    aws_access_key_id=self.aws_public_key,
    aws_secret_access_key=self.aws_private_key,
    region_name=self.configuration["region_name"].strip()
    config=Config(proxies=self.proxy, user_agent=self.useragent),
).client("guardduty")
List Findings
findings = guardduty_client.list_findings(
     DetectorId=detection_id,
     MaxResults=1,
     SortCriteria={"AttributeName": "updatedAt", "OrderBy": "ASC"},
  )
List Findings with Pagination
paginator = guardduty_client.get_paginator("list_findings")
    page_iterator = paginator.paginate(
      DetectorId=self.configuration["aws_detector_id"].strip(),
      FindingCriteria={
        "Criterion": {
          "updatedAt": {
            "Gte": int(checkpoint.timestamp() * 1000),
          }
        }
      },
       SortCriteria={"AttributeName": "updatedAt", "OrderBy": "ASC"},
    )
Get Findings
guardduty_client.get_findings(
         DetectorId=detection_id,
         FindingIds=finding_ids,
)
Performance Matrix
This plugin has been tested by fetching 288 findings from AWS GuardDuty Platform it takes around 15 seconds to fetch and store indicators from these findings in Netskope CE
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from AWS GuardDuty
~ 1K per minute
Indicators shared to AWS GuardDuty
NA
User Agent
netskope-ce-5.0.0-cte-aws-guardduty-v1.1.0
Workflow
Get your AWS GuardDuty credentials.
Configure the AWS GuardDuty plugin.
Configure sharing between Netskope and AWS GuardDuty.
Validate the AWS GuardDuty Plugin.
Click play to watch a video.
Create a Policy for AWS GuardDuty
Go to
IAM Services
in the AWS Console.
Click
Create policies
.
Select GuardDuty in Services.
Select
GetFindings
and
ListFindings
.
Click
Next
.
Add a Policy Name.
Click
Create Policy
.
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
Configure the AWS GuardDuty Plugin
Log in to your CE instance and go to
Settings > Plugins
.
Search for and select the AWS GuardDuty plugin box to configure the plugin.
Enter these values:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave default.
Aging Criteria: Expiry time of the plugin in days. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter these values:
Authentication Method: Select the method to be used for authentication (Deployed on AWS/AWS IAM Roles Anywhere)
Private Key: Private Key for decrypting the AWS Private CA Certificate. Required for
AWS IAM Roles Anywhere
authentication type.
Certificate Body: Certificate Body for AWS Public/Private CA Certificate. Required for
AWS IAM Roles Anywhere
authentication type.
Password Phrase: Password Phrase for decrypting the CA Certificate. Required for
AWS IAM Roles Anywhere
authentication type.
Profile ARN: AWS Profile ARN for AWS client authentication. Required for
AWS IAM Roles Anywhere
authentication type
.
Role ARN: AWS Role ARN for AWS client authentication. Required for
AWS IAM Roles Anywhere
authentication type.
Trust Anchor ARN: AWS Trust Anchor ARN for AWS client authentication. Required for
AWS IAM Roles Anywhere
authentication type.
Region Name: Region in which GuardDuty service is running. Make sure that the region name matches the region in the Profile ARN and Trust Anchor ARN.
Detector ID: The Unique ID of the detector.
Initial Range (in days): Number of days to pull the data for the initial run.
Click
Save
.
Add a Business Rule for AWS GuardDuty
To share indicators fetched from the AWS GuardDuty to the Netskope CE you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule follow the below steps:
Go to
Threat Exchange > Business Rule
and click
Create New Rule
.
Add the filter according to your requirement in the rule.
Configure Sharing for Netskope and AWS GuardDuty
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
, and in the Source Configuration dropdown list, select
AWS GuardDuty
.
Select a Business Rule, and then select
Netskope
for the Destination Configuration. Sharing configurations are unidirectional. data obtained from one plugin is shared with another plugin.
Select a Target. Each plugin will have a different target or destination for the IoC.
For Add a File Hash List, enter a List Name, List Size, and Default File Hash. The List Name needs to exist in your Netskope UI at
Settings > Policies > Profiles
. For information about creating a File Profile for hashes, refer to
Adding a File Profile
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Note
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin
API Source
, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect.
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Modify, Test, or Delete a Sharing Configuration
Each configuration supports 3 actions:
Edit the rule by clicking on the pencil icon.
Test the rule by clicking on the synchronization icon. This tests how many IoC will actually be sent to the destination system based on the timeframe and the rule.
Delete the rule by clicking on the garbage can icon.
Validate the AWS Guardduty Plugin
Validate the Pull
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the Filter
:
sources.source Like “<plugin name>”. You can filter the logs from CE as well with the plugin name.
On the AWS GuardDuty platform the Indicators are pulled from GuardDuty > Findings.
Validate the Push
To validate the push in Cloud Exchange, go to
Threat Exchange > Logging
and filter shared logs for Netskope.
To verify from the Netskope Tenant:
Log in to your Netskope Tenant.
Click
Policies
.
Click
File
(for Sha256).
Enter the File name that you used while configuring Sharing.
For URLs: (IPv4 and Domain).
Click
Web > URL Lists
.
Click on the URL List which was used while configuring the sharing
Troubleshooting
If you face issue while configuring the plugin with Deployed on AWS
Check the IAM Role attached to your EC2 Machine.
In this Topic
AWS GuardDuty Plugin for Threat Exchange

---
## Carbon Black Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/carbon-black-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:39:33+00:00
**Scraped:** 2026-08-11T07:15:37.750366+00:00

Carbon Black Plugin for Threat Exchange - Netskope Technical Documentation
Carbon Black Plugin for Threat Exchange
This document explains how to configure the Carbon Black plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows users to pull indicators of type SHA256 from the Carbon Black’s Alerts page. Additionally, this plugin also supports sharing of the indicators (IPv4, IPv6, Domain, MD5, SHA256) to the Carbon Black’s Watchlist page.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Threat Prevention subscription for malicious file hash sharing.
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Carbon Black Cloud instance.
Connectivity to the following host:
https://defense.conferdeploy.net
.
Carbon Black Plugin Support
Fetched indicator types
SHA256
Shared indicator types
SHA256, MD5, Domain, IPv4, IPv6
Mappings
Severity Mapping for Pull
Netskope CE Severity
Carbon Black Severity
Unknown
0
Low
1,2,3
Medium
4,5,6
High
7,8,9
Critical
10
Pull Mapping
Netskope CE Fields
Carbon Black Fields
Value
process_sha256
First Seen
first_event_timestamp
Last Seen
last_event_timestamp
Severity
severity
Tags
process_reputation
comments
process_name
Push Mapping
Netskope CE Field
Carbon Black Field
Value
IOC Value
Permissions
API Scopes permissions.
Scope
Read
Write
Update
org.alerts
Yes
No
No
org.feeds
Yes
Yes
Yes
API Details
List of APIs Used
API Endpoint
Method
Use Case
{cbc-hostname}/api/alerts/v7/orgs/{org_key}/alerts/_search
POST
Pull indicators.
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/reports
POST
Push indicators.
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds
POST
Create a feed.
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/feedinfo
GET
Get feed details
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/feedinfo
PUT
Update feed details
Pull Indicators
API Endpoint:
{cbc-hostname}/api/alerts/v7/orgs/{org_key}/alerts/_search
Method:
POST
Request Body:
{
    "rows": 2000,
    "criteria": {
        "minimum_severity": 1
    },
    "time_range": {
        "start": "2024-04-12T07:06:06.572000Z",
        "end": "2024-04-12T08:46:23.848713Z"
    },
    "start": 1,
    "sort": [
        {
            "field": "backend_timestamp",
            "order": "ASC"
        }
    ]
}
}
Headers:
X-AUTH-TOKEN: “ABCDEFGHIJKLMNO123456789/ABCD123456”
Content-Type: “application/json”
API Request Endpoint:
{
    "results": [
        {
            "org_key": "ABCD1234",
            "alert_url": "https://defense.conferdeploy.net/alerts?s[query_string]=id:708d7dbf-2020-42d4-9cbc-0cddd0ffa31a&orgKey=ABCD1234",
            "id": "708d7dbf-2020-42d4-9cbc-0cddd0ffa31a",
            "type": "WATCHLIST",
            "backend_timestamp": "2023-04-03T08:48:47.211Z",
            "user_update_timestamp": "2023-04-13T11:55:20.860Z",
            "backend_update_timestamp": "2023-04-03T08:48:47.211Z",
            "detection_timestamp": "2023-04-03T08:46:52.302Z",
            "first_event_timestamp": "2023-04-03T08:44:43.552Z",
            "last_event_timestamp": "2023-04-03T08:44:43.552Z",
            "severity": 6,
            "reason": "Process taskhostw.exe was detected by the report \"Abnormally Large DNS Exchanges (exfil or zone transfer)\" in watchlist \"zzz_XDR Sample IOCs\"",
            "reason_code": "19261158-dbbf-3077-9959-f8aa7f7551a1:0cc402b0-ea96-35c6-8418-a2f07acf616d",
            "threat_id": "19261158DBBF00775959F8AA7F7551A1",
            "primary_event_id": "t6a_TNVuQb6seMjk_VyDsg-0",
            "policy_applied": "NOT_APPLIED",
            "run_state": "RAN",
            "sensor_action": "ALLOW",
            "workflow": {
                "change_timestamp": "2023-04-13T11:55:20.860Z",
                "changed_by_type": "USER",
                "changed_by": "demouser@demoorg.com",
                "closure_reason": "NO_REASON",
                "status": "IN_PROGRESS"
            },
            "determination": {
                "change_timestamp": "1970-01-01T00:00:00.000Z",
                "value": "ALERT_CLASSIFICATION_UNKNOWN",
                "changed_by_type": "OPERATOR_UNKNOWN",
                "changed_by": null
            },
            "tags": null,
            "alert_notes_present": false,
            "threat_notes_present": false,
            "is_updated": false,
            "device_id": 18078555,
            "device_name": "DEMO\\DEMOMACHINE",
            "device_uem_id": "",
            "device_target_value": "MEDIUM",
            "device_policy": "Demo-policy",
            "device_policy_id": 12345678,
            "device_os": "WINDOWS",
            "device_os_version": "Windows 10 x64",
            "device_username": "DEMOMACHINE\\Administrator",
            "device_location": "UNKNOWN",
            "device_external_ip": "1.2.3.4",
            "device_internal_ip": "1.2.3.4",
            "mdr_alert": false,
            "report_id": "Fm0YsPDyQ1Kp1Pdd6Lnd8w-abd-defg-123",
            "report_name": "Abnormally Large DNS Exchanges (exfil or zone transfer)",
            "report_description": "IOC leveraging XDR fields to identify abnormally large DNS exchanges. The typical client DNS query to your DNS server is between 50-550 bytes. Large exchanges could be indicative of attack exfiltration or zone transfer attempts.",
            "report_tags": [],
            "ioc_id": "abd-defg-123",
            "ioc_hit": "netconn_application_protocol:DNS AND netconn_bytes_sent:[551 TO *]",
            "watchlists": [
                {
                    "id": "lgaClyOmQ86ZwZttq3ZDxg",
                    "name": "Demo IOCs"
                }
            ],
            "process_guid": "ABCD1234-0113db5b-000011bc-00000000-1d966088928e609",
            "process_pid": 4540,
            "process_name": "c:\\windows\\system32\\taskhostw.exe",
            "process_sha256": "1234cd567ab3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad",
            "process_md5": "123a4566ab18f93b93d551cd10c1598e",
            "process_effective_reputation": "COMPANY_WHITE_LIST",
            "process_reputation": "TRUSTED_WHITE_LIST",
            "process_cmdline": "taskhostw.exe SYSTEM",
            "process_username": "DEMOSERVER\\DEMO",
            "process_issuer_": "Demo CA",
            "process_publisher": "Demo Publisher",
            "parent_guid": "ABCD1234-0113db5b-000006bc-00000000-1d94225f1bb0897",
            "parent_pid": 1724,
            "parent_name": "c:\\windows\\system32\\svchost.exe",
            "parent_sha256": "123ab451a82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7",
            "parent_md5": "a123456789f632dc8d9404d83bc16316",
            "parent_effective_reputation": "TRUSTED_WHITE_LIST",
            "parent_reputation": "TRUSTED_WHITE_LIST",
            "parent_cmdline": "C:\\Windows\\system32\\svchost.exe -k netsvcs -p -s Schedule",
            "parent_username": "NT AUTHORITY\\SYSTEM",
            "childproc_guid": "",
            "childproc_username": "",
            "childproc_cmdline": ""
        }
    ],
    "num_found": 147,
    "num_available": 147
}
Push Indicators
API Endpoint:
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/reports
Method:
POST
Request Body:
{
    "reports": [
        {
            "title": "Netskope CTE Threat Report",
            "description": "",
            "severity": 10,
            "timestamp": 1712302532,
            "iocs_v2": [
                {
                    "match_type": "equality",
                    "field": "process_md5",
                    "values": [
                        "dc3d905ed90bbc148bccd34fe0c94d2d"
                    ],
                    "id": "8400901781583914388"
                },
                {
                    "match_type": "equality",
                    "field": "process_sha256",
                    "values": [
                        "926a34fbae94ab7ed7fe9a596f0507031e19044c06cbbca245efb30d926ea1e5"
                    ],
                    "id": "8400901781583914388"
                },
                {
                    "match_type": "equality",
                    "field": "ipv4",
                    "values": [
                        "204.225.210.233"
                    ],
                    "id": "-8400901781583914388"
                },
                {
                    "match_type": "equality",
                    "field": "dns",
                    "values": [
                        "r3626a7uj.top"
                    ],
                    "id": "8400901781583914388"
                }
            ],
            "id": "8400901781583914388"
        }
    ]
}
Headers:
X-AUTH-TOKEN: “ABCDEFGHIJKLMNO123456789/ABCD123456”
Content-Type: “application/json”
API Request Endpoint
:
https://defense.conferdeploy.net/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/reports
Sample API Response
:
200 OK
{
    "success": true
}
Create a Feed
API Endpoint:
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds
Method:
POST
Request Body:
{
    "feedinfo": {
        "name": "tesmm123",
        "owner": "7DESJ9GN",
        "provider_url": "",
        "summary": "test",
        "category": "development"
    },
    "reports": []
}
Headers:
X-AUTH-TOKEN: “ABCDEFGHIJKLMNO123456789/ABCD123456”
Content-Type: “application/json”
API Endpoint:
https://defense.conferdeploy.net/threathunter/feedmgr/v2/orgs/{org_key}/feeds
Sample API Response:
200 OK
{
    "results": [
        {
            "name": "testcrest",
            "owner": "7DeeJ9GN",
            "provider_url": "https://riu.service-now.com/",
            "summary": "Action based IOCs from Carbon Black Cloud Service Now App",
            "category": "external_threat_intel",
            "alertable": true,
            "source_label": null,
            "access": "private",
            "id": "rbWqcLoGRjSSoZg0LaC9iQ",
            "reports_count": null
        }
 ]
}
Get Feed Details
API Endpoint:
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds
Method:
GET
Parameters:
include_public:true
Headers:
X-AUTH-TOKEN: “ABCDEFGHIJKLMNO123456789/ABCD123456”
Content-Type: “application/json”
API Endpoint:
https://defense.conferdeploy.net/threathunter/feedmgr/v2/orgs/{org_key}/feeds
Sample API Response:
200 OK
{
    "results": [
        {
            "name": "testcrest",
            "owner": "7DeeJ9GN",
            "provider_url": "https://riu.service-now.com/",
            "summary": "Action based IOCs from Carbon Black Cloud Service Now App",
            "category": "external_threat_intel",
            "alertable": true,
            "source_label": null,
            "access": "private",
            "id": "rbWqcLoGRjSSoZg0LaC9iQ",
            "reports_count": null
        }
 ]
}
Update Feed Details
API Endpoint:
{cbc-hostname}/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/feedinfo
Method:
PUT
Request Body:
{
    "name": "CTE Threat Feed new",
    "owner": "7D****GN",
    "provider_url": "",
    "summary": "val",
    "category": "development",
    "alertable": true,
    "source_label": null,
    "access": "private",
    "id": "TlXvOfFLS2WEdcvRBcYFTw",
    "reports_count": null
}
Headers:
X-AUTH-TOKEN: “ABCDEFGHIJKLMNO123456789/ABCD123456”
Content-Type: “application/json”
API Request Endpoint:
https://defense.conferdeploy.net/threathunter/feedmgr/v2/orgs/{org_key}/feeds/{feed_id}/feedinfo
Sample API Response:
200 OK
{
    "name": "CTE Threat Feed new",
    "owner": "IRRRR",
    "provider_url": "",
    "summary": "val",
    "category": "development",
    "alertable": true,
    "source_label": null,
    "access": "private",
    "id": "TlX*********BcYFTw",
    "reports_count": null
}
Performance Matrix
Here is the performance reading conducted by pulling and sharing 100K indicators from/to Carbon Black on a Large CE Stack with the below specifications:
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Carbon Black
~14K per minute
Indicators shared with Carbon Black
~100K per minute
User Agent
netskope-ce-5.0.1-cte-carbon-black-v1.1.0
Workflow
Create a custom File Profile.
Create a Malware Detection Profile.
Create a Real-time Protection Policy.
Get your Carbon Black API Credentials.
Configure the Carbon Black plugin.
Configure sharing between Netskope and Carbon Black.
Validate the Carbon Black plugin.
Click play to watch a video.
Create a Secure Web Gateway Custom File Profile
In the Netskope UI, go to
Policies
, select
File
, and click
New File Profile
.
Click
File Hash
in the left panel, select
SHA256
from the File Hash dropdown list.
Enter a temporary value in the text field. Netskope does not support progressing without having a value in this field, and recommends entering a string of 64 characters that consists of the character
f
. For example,
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
. This will have a very low possibility of matching a valid file format.
Click Next
.
Enter a Profile Name and a Description. We recommend not having blank spaces in your profile name; use underscores for spaces.
Click
Save
.
To publish this profile into the tenant, click
Apply Changes
in the top right.
Create a Malware Detection Profile for Carbon Black
In the Netskope UI, go to
Policies
, select
Threat Protection
, and click
New Malware Detection Profile
.
Click
Next
.
Note
For this configuration example, we will be using the intelligence for this list as a block list. Netskope does support inclusion of both allow and block lists in the threat profiles.
Click
Next
again.
Select the File Profile you created in the previous section and click
Next
.
Enter a Malware Detection Profile name and click
Save Malware Detection Profile
.
To publish this profile in the tenant, click
Apply Changes
in the top right.
Create a Real-time Threat Protection Policy for Carbon Black
In the Netskope UI, go to
Policies > Real-time Protection
.
Note
The policy configured here is just an example. Modify as appropriate for your organization.
Click
New Policy
and select
Threat Protection
.
For
Source
, leave the default (User = All Users)
For
Destination
: select
Category
The Category section expands and allows you to search and select categories. Click
Select All
.
When finished, click outside of the Category section.
When the Activities & Constraints section opens, click
Edit
.
Select
Upload
and
Download
, and then click
Save
.
For
Profile & Action
, click in the text field.
Select the Malware Detection profile you created in the previous section.
For the Severity Levels, change all of the Actions settings from
Action: Alert
to
Action: Block
.
Select a template to choose which block message is sent to the user.
For
Set Policy
, enter a descriptive Policy Name.
Click
Save
in the top right to save the policy.
Choose the
To the top
option when it appear. (Or appropriate location in your security policy)
To publish this policy into the tenant, select
Apply Changes
in the top right.
Get your Carbon Black API Credentials
Log in to your Carbon Black Console.
Copy the Carbon Black Console
URL
. You will need this when configuring the Carbon Black plugin for Cloud Threat Exchange.
Go to
Settings
>
API Access
>
Access Levels
and click
Add Access Level
.
Enter a Name and Description appropriate for your custom API roll.
Select these scopes for access:
Notation Name org alerts: Read
Alerts: Read
Custom Detections for Org.feeds: Create, Read, Update
Click
Save
. After a few seconds, Access Level will be visible.
With the proper Scopes defined, next generate an API key with this access. Select the
API Keys
tab on the top of the page, and then click
Add API Key
.
Enter a Name and Description that is appropriate for your environment.
For
Access Level type
, select
Custom
. Select the Access Level that was created in Access Level.
Click
Save
. Copy the API ID, API Secret Key, and Org Key. Save these values for when you configure the Carbon Black plugin.
Configure the Carbon Black Plugin
In Cloud Exchange, go to
Settings
>
Plugins
.
Search for and select the
Carbon Black
1.1.0
(CTE)
box to open the plugin creation pages.
Enter and select the Basic Information on the first page:
Configuration Name: Enter a name appropriate for your integration.
Sync Interval: Interval to fetch data from this plugin source. Adjust the Sync Interval to appropriate value. Recommended is 5+ minutes.
Aging Criteria: Expire indicators after a specific time. Leave default.
Override Reputation: Set value to override reputation of indicators received for this configuration. Leave empty to keep the default.
Enable SSL verification: Enable if SSL verification is required for communication.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter and select the Configuration Parameters on the second page:
Management URL: Enter your Management URL copied from the Carbon Black console when creating your API key.
API ID: Enter your API ID copied when creating your API key.
API Secret: Enter your API Secret copied when creating your API key.
Organization Key: Enter your Organization Key copied when creating your API key.
Minimum Severity: Leave default.
Reputation: Leave default.
Enable Tagging: Enable if tagging is required.
Enable Polling: Enable/Disable polling Threat IOCs from Carbon Black. Disable if you only need to push Threat IoCs to Carbon Black.
Initial Range (in days): Number of days to pull the data for the initial run. Leave default.
Click
Save
in the top right corner. Go to
Threat Exchange > Plugins
to see your new Carbon Black plugin.
Configure a Threat Exchange Business Rule for Carbon Black
Business Rule is used to filter out the indicators that are to be shared. In order to share IoCs with Carbon Black, create a business rule using the following steps:
In Threat Exchange go to
Business Rules
and click
Create New Rule
.
Add the Rule name and select the fields through which you want to filter the IoCs.
Click
Save
.
Configure Threat Exchange Sharing for Carbon Black
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
, and in the Source Configuration dropdown list, select
CTE Netskope
.
Select a Business Rule, and then select
CTE Carbon Black
for the Destination Configuration. Sharing configurations are unidirectional. Data obtained from one plugin is shared with another plugin. To achieve bi- or multi-directional sharing, configure each separately.
Select a Target. Each plugin will have a different target or destination for the IoC.
Click
Save
.
Repeat steps 2-5, but select
CTE Carbon Black
as the Source Configuration and
CTE Netskope
as the Destination Configuration.
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Note
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin
API Source
, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect.
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Modify, Test, or Delete a Sharing Configuration
Each configuration supports 3 actions:
Edit the rule by clicking on the pencil icon.
Test the rule by clicking on the synchronization icon. This tests how many IoC will actually be sent to the destination system based on the timeframe and the rule.
Delete the rule by clicking on the garbage can icon.
Validate the Carbon Black Plugin
Validate the Pull
Indicators from Carbon Black are pulled from the Alerts page.
Click on the icon shown below for a particular alert to view the details.
As shown, SHA-256 will be the value of Carbon Black IoC in CE.
Indicators stored in CE can be verified from the
Threat Exchange > Threat IoCs
page.
Search the Carbon Black IoCs by filtering indicators for Carbon Black.
Example: Add a query on the Threat IoCs page, like
sources.source Is equal <plugin configuration name>.
You can also verify the indicators pulled in CE from the logs available on the
Logging
page.
Validate the Push
Shared IoCs to Netskope/CrowdStrike can be verified from logs available on the
Logging
page of Netskope CE.
IoCs shared on Carbon Black can be verified from the
Enforce > Watchlist
page. Click
Add Watchlists
.
Now search for the Feed name. Click on the Feed name that was provided while configuring the sharing. Click
CTE Feed Carbon Black Demo
. Click
Subscribe
.
Now search for the Feed name that was subscribed. Click on the Feed. Go to the
Reports
Page and click
Netskope CTE Threat Report
.
All the shared URLs (IPv4, IPv6, and Domain), md5, and sha256 will be visible.
Troubleshooting
Unable to Configure the Plugin.
If you are unable to configure the Carbon Black plugin, it could be due to one of these reasons:
The API ID and/or API Secret is incorrect.
The API Access is incorrect.
To solve these issues:
Provide correct API ID, API Secret. To get the correct credentials, follow the
Get your Carbon Black API Credentials
steps.
Provide correct scopes to the API Key. To know how to provide correct scopes, follow the
Get your Carbon Black API Credentials
steps.
Unable to share the data on the Carbon Black
If you are unable to share the data on the Carbon Black platform, it could be due to
Access is not as needed.
To solve this issue:
Provide correct scopes to the API Key. To know how to provide correct scopes, follow the
Get your Carbon Black API Credentials
steps.
Unable to Validate the data on the Carbon Black
If you are unable to view the data on the Carbon Black platform, it could be due to the
Feed name that was provided while configuring sharing is not present in the watchlist.
To solve this issue, follow these steps:
Subscribe to the Feed.
To know how to subscribe to the Feed, follow the
Validate the Push
steps.
Known Behavior
If the limit, like 1K IOCs per report, or 10K reports per feed is exceeded, it will prevent the edit or searching of IoCs on the report. Refer to the linked documentation below to know the sharing limit on the Carbon Black platform.
https://developer.carbonblack.com/reference/carbon-black-cloud/cb-threathunter/latest/feed-api/
After a New batch of IoCs are shared to the Feed, the old IoC’s will be replaced by the newly shared IoC’s.
In this Topic
Carbon Black Plugin for Threat Exchange

---
## Configure 3rd-party Threat Exchange Plugins
**URL:** https://docs.netskope.com/en/configure-3rd-party-threat-exchange-plugins/
**Last Modified:** 2025-10-31T23:24:01+00:00
**Scraped:** 2026-08-11T07:15:52.646919+00:00

Configure 3rd-party Threat Exchange Plugins - Netskope Technical Documentation
Configure 3rd-party Threat Exchange Plugins
Only admins and write-access users can configure 3rd-party Threat Exchange plugins. Threat Exchange comes with a library of supported plugins. Plugins can be easily configured to collect and share indicators related to file hashes of malicious software (malware) used in a Netskope DLP policy by following the plugin guide. Refer to the
Threat Exchange Custom Plugin Developers Guide
to understand how to build and upload a custom plugin.
You can also disable, enable, or delete existing plugin configurations. Threat Exchange can be configured with multiple plugins to the same system for different workflows from either the same Netskope tenant or multiple Netskope tenants.
Threat Exchange ONLY pulls the following IoC’s when they are available:
Malicious file file hashes in MD5 or SHA256 format.
URL: Depending on the nature of the plugin, these could be malicious URL, restricted URL, or allowed URL. The latter two would be for firewall, SWG, or CASB policy synchronization. Fetching malicious Hostnames, Domains and FQDNs are also supported.
IP addresses (CIDR): Depending on the nature of the plugin, these could be malicious IP (IPv4/IPv6), restricted IP, or allowed IP. The latter two would be for firewall, SWG, or CASB policy synchronization.
Abnormal Security Plugin for Threat Exchange
Anomali ThreatStream XDR Plugin for Threat Exchange
API Source Plugin for Threat Exchange
AWS GuardDuty Plugin for Threat Exchange
Carbon Black Plugin for Threat Exchange
Commvault Plugin for Threat Exchange
CrowdStrike Plugin for Threat Exchange
Cybereason Plugin for Threat Exchange
Darktrace Plugin for Threat Exchange
Digital Shadow Plugin for Threat Exchange
ExtraHop Reveal(x) 360 Plugin for Threat Exchange
Feedly Plugin for Threat Exchange
GitHub Plugin for Threat Exchange
HarfangLab Plugin for Threat Exchange
Illumio Plugin for Threat Exchange
Imperva Plugin for Threat Exchange
Infoblox Plugin for Threat Exchange
Maltiverse Plugin for Threat Exchange
Mandiant Plugin for Threat Exchange
Microsoft Defender for Cloud Apps Plugin for Threat Exchange
Microsoft Defender for Endpoint Plugin for Threat Exchange
Microsoft Office 365 Endpoints Plugin for Threat Exchange
Mimecast Plugin for Threat Exchange
MISP Plugin for Threat Exchange
OpenCTI Plugin for Threat Exchange
Palo Alto Networks Cortex XDR Plugin for Threat Exchange
Palo Alto Networks Panorama Plugin for Threat Exchange
Proofpoint Plugin for Threat Exchange
Rubrik Plugin for Threat Exchange
SecLytics Plugin for Threat Exchange
Secureworks Taegis Plugin for Threat Exchange
SecurityScorecard Plugin for Threat Exchange
SentinelOne Plugin for Threat Exchange
ServiceNow Plugin for Threat Exchange
Skyhigh Plugin for Threat Exchange
STIX/TAXII Plugin for Threat Exchange
Sophos Plugin for Threat Exchange
Tanium Plugin for Threat Exchange
ThreatConnect Plugin for Threat Exchange
ThreatQ Plugin for Threat Exchange
Trellix Plugin for Threat Exchange
Trend Vision One Plugin for Threat Exchange
Vectra AI Plugin for Threat Exchange
VMRay Plugin for Threat Exchange
Web Page IoC Scraper Plugin for Threat Exchange
In this Topic
Configure 3rd-party Threat Exchange Plugins

---
## Configure Threat Exchange Business Rules
**URL:** https://docs.netskope.com/en/configure-threat-exchange-business-rules/
**Last Modified:** 2025-10-31T23:38:47+00:00
**Scraped:** 2026-08-11T07:16:24.388600+00:00

Configure Threat Exchange Business Rules - Netskope Technical Documentation
Configure Threat Exchange Business Rules
Go to
Threat Exchange > Business Rules
. A page appears showing previously configured business rules (if applicable).
Click
Create New Rule
button. This opens a window where the rule can be given a descriptive name and a set of matching conditions selected. The boolean logic allows for
not
,
and
, and
or
functions for more than one rule to match on metadata provided about the IoC, including source, reputation, tag, severity, extended information, and many more.
You can add more rules and create groups of rules that can be additive or alternative. Rules can also be deleted by clicking on the rule and selecting the red garbage can.
Finally, rules can also be copied from the IoC page for use in a business rule by clicking on the
Copy Filter
button, or created from the IoC page by clicking on the document icon.
Enter the folder name that you want to add the rule(s) to or select an existing folders. At max Cloud Exchange supports a business folder hierarchy three levels deep.
When finished, click
Save
. Whenever a rule is saved or deleted, a green pop-up box will appear in the upper right corner reporting successful completion of the command.
Perform Actions on Business Rules
You can manage all the business rules from the Business Rules page. Write-access users can mute one or multiple business rules, and also clone an entire business rule, edit the query for business rules, or delete the business rules from this page. These Actions are explained in more detail below.
The number of rules shown on the page can be modified if there are more than 10 to show.
Clone a Business Rule
To clone a business rule, click the document icon on the rule and confirm the action.
Mute a Business Rule
Muting can be used to temporarily ignore any new IoCs that would normally trigger sharing.
Edit a Business Rule
To edit a business rule, click the pencil icon on the rule and make your changes. When finished, click
Save
.
Test a Business Rule
To test a business rule to see its matching the number of IoCs from a given period of time, select the sync icon on the rule and confirm the action. This will display the total number of IoCs matching this Business Rule.
Enter the Time Period (in days). Only the IoCs fetched during this period will be considered while evaluating the business rule. Checking the All Time button will evaluate all active IoCs for the past 365 days.
Click
Fetch
. This will invoke the test; it will not result in the IoC being shared. Actually sharing IoC requires configuring a sharing rule.
This will show the qualified number of URL(s) with size and qualified number of Filehash(es) with size.
Delete a Business Rule
To delete a business rule, click the trash icon on the rule and confirm the action.
Add, Edit or Delete Exception Rules to a Business Rule
Exception rules are used to exclude specific indicators based on some criteria. For example, you can exclude indicators with low severity or specific value, as well as create exception rules with query or tags.
Exceptions work like the business rules, and can use query language, or particular tags, making it easier to remove certain kinds of data from the primary matching rule. For example, the IoCs that have been tagged as benign by the SecOps team.
To create an Exception Rule, expand the rule and click the Exception Rules
+
icon.
Enter an exception rule name and add queries or tags. When finished, click
Save
.
Other actions that can be taken on exception rules include:
Editing existing rules by clicking on the pencil icon.
Deleting rules by clicking on the garbage can icon.
In this Topic
Configure Threat Exchange Business Rules

---
## Configure Threat Exchange Sharing with your Netskope Tenant
**URL:** https://docs.netskope.com/en/configure-threat-exchange-sharing-with-your-netskope-tenant/
**Last Modified:** 2025-11-01T00:39:40+00:00
**Scraped:** 2026-08-11T07:16:25.596759+00:00

Configure Threat Exchange Sharing with your Netskope Tenant - Netskope Technical Documentation
Configure Threat Exchange Sharing with your Netskope Tenant
You need to get the sharing information from Threat Exchange to use later when setting up a profile in the Netskope tenant. This informationis in the Threat Exchange module when you created a file hash share with a Netskope tenant as the Destination Configuration. You must have a Threat Exchange plugin and a sharing rule in order to push file hash information (or URL/IP addresses) to your Netskope tenant.
If you haven’t already done so, create Threat Exchange sharing to use in your Netskope tenant. The Sharing configuration settings needed are:
Source configuration will be the plugin that provided the file hash.
Business rule will be the configured rule to be used to decide what data to share from the IoC database.
Destination configuration will be the plugin where the data is destined (different plugins have different abilities to ingest data from Threat Exchange).
Target dictates where the data will be stored in the destination system. In the Netskope tenant, the data is either pushed to a URL list or, in this workflow, a file hash list.
List Size specifies the maximum size of any file pushed by Threat Exchange. Netskope only supports a maximum file size of 8 MB to be sent via a single RESTful API (v1 only) or GUI upload workflows.
Default File Hash is no longer needed and can be ignored as of Cloud Exchange 3.1.
When finished, click
Save
.
In this Topic
Configure Threat Exchange Sharing with your Netskope Tenant

---
## Configure Threat Exchange IoC Sharing
**URL:** https://docs.netskope.com/en/configure-threat-exchange-ioc-sharing/
**Last Modified:** 2026-05-28T02:31:00+00:00
**Scraped:** 2026-08-11T07:16:26.828581+00:00

Configure Threat Exchange IoC Sharing - Netskope Technical Documentation
Configure Threat Exchange IoC Sharing
This page describes how to configure IoC sharing between the plugins (and therefore connected vendor systems). Make sure to identify the sharing requirements between systems in advance of configuration. The sharing relationships each require a business rule to control what data is shared with the destination plugin.
Note that each plugin for which a sharing rule is intended may have requirements that dictate the nature of the business rule. There is no point in creating a sharing rule to match IoC for sharing if that rule will be used to push information towards a system that can not use or can not receive those IoC types (STIX/TAXI for example is a push, never a pull, model).
Additionally, there is a section on
IoC Sharing Best Practices
that suggests mechanisms to insert manual overrides to dictate exactly when IoCs are shared, rather than allowing the system to automatically share all rules. Tags are a central part of this approach.
Threat Exchange URL Handling
Netskope Threat Exchange enables the sharing of IoC from 3rd-party platforms to and from Netskope (and each other). Though originally designed for managing attack indicators, it has evolved to support additional use cases including synchronizing and managing secure web gateway (SWG) to allow and block lists, populating SSL interception or bypass lists for CASB and SWG, and surfacing file hash information for Github repositories to prevent this data from being inappropriately shared using Netskope’s inline DLP functionality.
Netskope will accept URLs, MD5 hashes, SHA256 hashes, IPv4 addresses, IPv6 addresses, hostnames, domains, and fully qualified domain names (FQDNs) to be used in the custom URL file for invocation as a destination match in a Netskope Real-time policy. The custom URL file must be used in policy, but that policy can result in any of the supported inline outcomes, including, but not limited to: block, alert, coach, justify, etc.
To communicate with Netskope tenants, Threat Exchange uses the
REST API V2
if it is enabled in the Netskope tenant and configured in Cloud Exchange, or
REST API V1
if that is the only token either configured or available, as is the case for updating file hashes for use in threat prevention policies.
Threat Exchange pushes this IoC information to Netskope into one of two locations. URL and IP addresses are pushed to a custom category file that is used by the custom categories function of the Next Generation Secure Web Gateway (
https://<your-tenant>.goskope.com/ns#/web-profiles-page?subview=webList
) and file hashes (MD5 and/or SHA256) are pushed to a file profile file (
https://<your-tenant>.goskope.com/ns#/file-filter-profile
).
However, just because information can be pushed by Threat Exchange does not mean that the information is usable by the receiving system. File hash types, URL formatting, or the availability of data repositories all can reduce the potential functionality of the sharing function.
For instance, CrowdStrike ingests the URL from Threat Exchange, but removes everything after the domain.
URL Requirements/Functionality for Threat Exchange to Netskope
Netskope accepts some URL, depending on their formatting. To learn more, go to:
Create Custom Categories
As you can see URL in the custom URL list, the file must be formatted a particular way, specifically each must look like one of the following
http(s)://url.domain.com/fullURI
OR
http(s)://ipaddress
OR
http(s)://*.domain.com/fullURI
When Threat Exchange sends a Non-compliant URL to Netskope
When Threat Exchange sends a URL (alone or as part of a larger update) that is rejected by the Netskope client, Threat Exchange parses the Netskope response, identifies the invalid URL, and marks it as “invalid”. By default, Threat Exchange will not attempt to push it again to the Netskope tenant.
These invalid indicators can be found in the Threat Exchange tenant by using the filter and searching for any indicators tagged as “invalid_host” or “Unshared”. Invalid App tags can be found using the tag “Invalid app”.
https://<your Cloud Exchange host>/cte/threat_iocs?query=sources.tags+IN+%28"Invalid+host"%29
Threat Exchange Filehash Handling
Netskope provides, and will accept, SHA256 and MD5 filehashes for use in files for invocation by inline threat prevention policies (or DLP rules relying on a filehash match). The file must be added into a policy, but that policy can result in any of the supported inline outcomes, including, but not limited to: block, alert, coach, justify, etc.
Duplicate IoC Handling
Netskope Threat Exchange allows write-access users to choose how to reconcile and manage duplicate IoC provided by the same or different sources. If ‘never override’ is chosen, all subsequent matching IoC metadata will be shown under the master IoC. Master or child IoC metadata can be used for creating sharing rules to decide what and which IoC and IoC metadata to send.
Add a Sharing Configuration
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
and select a source plugin configuration.
Select a Business Rule and a Destination Configuration. Sharing configurations are unidirectional. Data obtained from one plugin is shared with another plugin. To achieve bi- or multi-directional sharing, configure each separately.
Select a Target. Each plugin will have a different target or destination for the IoC.
Select an Action. Some plugins support multiple actions that equate to where the IoC could go, and therefore, what the receiving system will do with a matching indicator.
Some systems will support the IoC only to be used to match for certain endpoint OS (Windows, Mac, Linux).
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin API Source, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Manage a Sharing Configuration
Each configuration supports three actions: edit, sync, and delete.
Write-access users can update sharing or its target of an existing sharing configuration.
Click the Edit icon.
Update the required fields which you want to change.
Click
Save
.
Write-access users can sync an already configured sharing. This will trigger a sharing mechanism to share the IoCs to a destination configuration.
Click on the Sync icon.
Enter the Time Period (in days). Only the IoCs fetched during this period will be considered while evaluating the business rule. Checking the All Time will evaluate the IoCs from last year.
Click
Fetch
. This will display the number of IoCs will be shared with destination configuration. this action will be performed on.
Click
Sync
.
Write-access users can delete any of the existing configured sharing.
Click on the Delete icon.
Click
Delete
.
List IoCs and Filtering Capability
Threat Exchange maintains a database of IoCs provided from all configured plugins. You can view all available IoCs, view the metadata for each, and filter IoCs.
Go to Threat Exchange and click
Threat IoCs
.
A list of all active IoCs appear. The first time you see this screen, the default view will present IoCs added or updated (via API) in the last 7 days.
More can be pulled from the database of active IoCs, depending on the filtered query. The IoCs list is paginated with a default page size of 10 records that can be increased to show up to 100 records. By default, records are sorted in descending order of Last Seen.
You have different filter options available based on the IoC metadata or IoC Sources that is or can be associated with each IoC. Each user can add one or more filters and can add a group of filters to dive into a subset of all the active IoC. The detailed list of filter options and field meanings is presented below. You can also select
Not
for a negative filter criterion.
Field
Filter String variable
Description
Filter operators
Value
value
IoC value – MD5 SHA256 for filehash or URL.
Is equal and contains (Regex also supported).
Comments
comments
Comments provided for that IoC.
Is equal and contains (Regex also supported).
Type
type
Type of the IoC. MD5, SHA256, URL
any in, not in operator (Multiselect)
Netskope Hits
netskopeHits
Number of times Netskope has seen this IoC.
!=, <, <=, >, >=
Other Hits
OtherHits
Number of times third parties have seen this IoC.
!=, <, <=, >, >=
Test
test
Boolean value whether IoC is marked as Test from Netskope (a metadata field value used for testing)
Is equal, !=
Active
active
Boolean value whether IoC is expired or not.
Is equal, !=
Safe
safe
Boolean value whether IoC is safe or not. (Metadata field value used to denote a non-malicious IoC for the Github DLP plug-in)
Is equal, !=
Shared With
sharedWith
List of plugin configurations where IoC was pushed.
any in, not in operator (Multiselect)
Expires At
expiresAt
Time at which the IoC becomes inactive
!=, <, >, >=
Field
Filter String Variable
Description
Filter Operators
Source
sources.source
IoC value – MD5 SHA256 for filehash or URL.
Is equal and contains (Regex also supported).
Severity
sources.severity
Severity of IoC.
Is equal and contains (Regex also supported).
Reputation
sources.reputation
Confidence of the information. Low 1 – High 10.
!=, <, <=, >, >=
Netskope Hits
sources.netskopeHits
Number of times Netskope has seen this IoC.
!=, <, <=, >, >=
All Other Hits
sources.externalHits
Number of times third parties have seen this IoC.
!=, <, <=, >, >=
First Seen
sources.firstSeen
Time when CTE first saw IoC from a plug-in
!=, <, >, >=
Last Seen
sources.lastSeen
Time when CTE last saw IoC from a plug-in
!=, <, >, >=
Tags
sources.tags
Tags associated with the IoC data
any in, not in operator (Multiselect)
Comments
sources.comments
Comments provided for that IoC.
Is equal and contains (Regex also supported).
For more than one filter criteria, move the mouse to the upper right of the filter box and click
Add rule
. Select the appropriate comparison operator
And
or
Or
by moving the mouse over the Not button in the upper left; options will then be shown.
For alternative multi-data criteria, click
Add group
. Rules will be processed from top to bottom. Move the mouse to the upper right of the filter box to see the
Add group
option.
After selecting the desired filter, click
Apply Filter
. IoCs matching the filtering criteria will be listed in the UI.
Click
Clear
to remove the applied filter; the UI will revert to the default filter, and IoCs matching the default filter will be listed when the screen refreshes.
Users can copy the filter string created in the rules engine after applying the filter. Click
Copy Filter
to copy the actual search string. The copied string can be used as a filter in any plugin configuration to limit the data Threat Exchange sends to a third-party plugin.
Also users can enter the filter query manually and can load the filters according to the query.
Select and Modify Tags
Write-access users can modify Tags. Tags are used to add metadata to IoCs so SecOps teams can create workflows for filtering, viewing, staging, or pushing particular IoCs to plugins. More information regarding managing the tags can be found on
Manage Tags
section.
In this Topic
Configure Threat Exchange IoC Sharing

---
## Configure your Netskope Tenant for Threat Exchange File Hash Sharing
**URL:** https://docs.netskope.com/en/configure-your-netskope-tenant-for-cloud-threat-exchange-file-hash-sharing/
**Last Modified:** 2025-11-01T00:37:21+00:00
**Scraped:** 2026-08-11T07:16:31.736556+00:00

Configure your Netskope Tenant for Threat Exchange File Hash Sharing - Netskope Technical Documentation
Configure your Netskope Tenant for Threat Exchange File Hash Sharing
To share file hashes between your Netskope tenant and Threat Exchange, you need to:
Create a File and Malware Detection profile in your Netskope tenant for Cloud Threat Exchange to send file hashes for use in Real-time policy.
While setting up Cloud Threat Exchange for file hash sharing, you will be asked for the
List Name
you previously configured in your Netskope tenant.
Once you have hashes going to your Netskope tenant, you will need to build a policy to leverage this new data source. In this workflow, the file hashes will be used to enhance Netskope threat protection. However, you can also configure the plugin to push URL and/or IP addresses (individual or CIDR ranges) from Threat Exchange to a custom URL list.
In this Topic
Configure your Netskope Tenant for Threat Exchange File Hash Sharing

---
## Create a Malware Detection Profile in Your Netskope Tenant to use Threat Exchange File Hashes
**URL:** https://docs.netskope.com/en/create-a-malware-detection-profile-in-your-netskope-tenant-to-use-threat-exchange-file-hash-es/
**Last Modified:** 2026-03-21T02:25:14+00:00
**Scraped:** 2026-08-11T07:16:35.357675+00:00

Create a Malware Detection Profile in Your Netskope Tenant to use Threat Exchange File Hashes - Netskope Technical Documentation
Create a Malware Detection Profile in Your Netskope Tenant to use Threat Exchange File Hashes
After you have hashes going to your Netskope tenant, you will need to build a policy to check this new data source.
Go to
Policies > Threat Protection > New Malware Detection Profile
.
Click
Next
a couple of times to get to the
Blocklist
section. Select the Threat Exchange sharing file you created and click
Next
.
Ensure that you have provided an APIv1 token to the Netskope tenant configuration as a file hash file management does not have a v2 equivalent.
Name the profile and
Save
In this Topic
Create a Malware Detection Profile in Your Netskope Tenant to use Threat Exchange File Hashes

---
## Digital Shadow Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/digital-shadow-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:40:58+00:00
**Scraped:** 2026-08-11T07:16:49.254676+00:00

Digital Shadow Plugin for Threat Exchange - Netskope Technical Documentation
Digital Shadow Plugin for Threat Exchange
This document explains how to configure Digital Shadow with the Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows for pulling URLs (phishing-site-alert, impersonating-subdomain-alert and impersonating-domain-alert) from Digital Shadow to Netskope.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured
A Digital Shadow instance with the Elevate or Extend packages. Reach out to their Digital Shadow representative and ask them for API credentials (all keys granted as part of Elevate/Extend will have the required permissions).
The API key will be a 6-character letter/number combination (ex:
ABCD1E
). The API secret will be a 32-character letter/number combination (ex:
ABCDEF12GHIJKL345MNO6PQRSTUVWXYZ
.
Connectivity to the following host:
https://api.searchlight.app/
.
Digital Shadow Plugin Support
Fetched Indicator Types
Shared Indicator Types
URL
Not supported
Workflow
Create a custom File Profile.
Create a Malware Detection Profile.
Create a Real-time Protection Policy.
Create Digital Shadow credentials.
Configure the Digital Shadow Plugin.
Configure sharing between Netskope and Digital Shadow.
Validate the Digital Shadow Plugin.
Click
here
to watch a video.
Create a Secure Web Gateway Custom File Profile for Digital Shadow
In the Netskope UI, go to
Policies
, select
File
, and click
New File Profile
.
Click
File Hash
in the left panel, select
SHA256
from the File Hash dropdown list.
Enter a temporary value in the text field. Netskope does not support progressing without having a value in this field, and recommends entering a string of 64 characters that consists of the character
f
. For example,
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
. This will have a very low possibility of matching a valid file format.
Click Next
.
Enter a Profile Name and a Description. We recommend not having blank spaces in your profile name; use underscores for spaces.
Click
Save
.
To publish this profile into the tenant, click
Apply Changes
in the top right.
Create a Malware Detection Profile for Digital Shadow
In the Netskope UI, go to
Policies
, select
Threat Protection
, and click
New Malware Detection Profile
.
Click
Next
.
Note
For this configuration example, we will be using the intelligence for this list as a block list. Netskope does support inclusion of both allow and block lists in the threat profiles.
Click
Next
again.
Select the File Profile you created in the previous section and click
Next
.
Enter a Malware Detection Profile name and click
Save Malware Detection Profile
.
To publish this profile in the tenant, click
Apply Changes
in the top right.
Create a Real-time Threat Protection Policy for Digital Shadow
In the Netskope UI, go to
Policies > Real-time Protection
.
Note
The policy configured here is just an example. Modify as appropriate for your organization.
Click
New Policy
and select
Threat Protection
.
For
Source
, leave the default (User = All Users)
For
Destination
: select
Category
The Category section expands and allows you to search and select categories. Click
Select All
.
When finished, click outside of the Category section.
When the Activities & Constraints section opens, click
Edit
.
Select
Upload
and
Download
, and then click
Save
.
For
Profile & Action
, click in the text field.
Select the Malware Detection profile you created in the previous section.
For the Severity Levels, change all of the Actions settings from
Action: Alert
to
Action: Block
.
Select a template to choose which block message is sent to the user.
For
Set Policy
, enter a descriptive Policy Name.
Click
Save
in the top right to save the policy.
Choose the
To the top
option when it appear. (Or appropriate location in your security policy)
To publish this policy into the tenant, select
Apply Changes
in the top right.
Get your Digital Shadow Credentials
To get your API Key, API Secret, and Searchlight Account ID from Digital Shadow platform, reach out to their Digital Shadow representative and ask them for API credentials (all keys granted as part of Elevate/Extend will have the required permissions).
The API key will be a 6-character letter/number combination (ex:
ABCD1E
). The API secret will be a 32-character letter/number combination (ex:
ABCDEF12GHIJKL345MNO6PQRSTUVWXYZ
.
Configure the Digital Shadow Plugin for Threat Exchange
In Cloud Exchange, go to
Settings
and click
Plugins
.
Search for and select the Digital Shadow box to open the plugin creation pages.
Enter and select the Basic Information on the first page:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave default
Aging Criteria: Expiry time of the plugin in days. Default is 90.
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter the Configuration Parameters on the second page:
API Key: DigitalShadow API Key.
API Secret: DigitalShadow API Secret.
Searchlight Account ID: DigitalShadow Searchlight Account ID.
Click
Save
.
Configure Sharing for Netskope and Digital Shadow
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
, and in the Source Configuration dropdown list, select
Digital Shadow
.
Select a Business Rule, and then select
Netskope
for the Destination Configuration. Sharing configurations are unidirectional. data obtained from one plugin is shared with another plugin. To achieve bi- or multi-directional sharing, configure each separately.
Select a Target. Each plugin will have a different target or destination for the IoC.
Click
Save
.
Repeat steps 2-5, but select
Netskope
as the Source Configuration and
Digital Shadow
as the Destination Configuration.
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Note
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin
API Source
, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect.
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Modify, Test, or Delete a Sharing Configuration
Each configuration supports 3 actions:
Edit the rule by clicking on the pencil icon.
Test the rule by clicking on the synchronization icon. This tests how many IoC will actually be sent to the destination system based on the timeframe and the rule.
Delete the rule by clicking on the garbage can icon.
Validate the Digital Shadow Plugin
Based on the Plugin configuration, Indicators will pull from Digital Shadow. Go to
Threat Exchange > Threat IoCs
to view the received IoCs.
In this Topic
Digital Shadow Plugin for Threat Exchange

---
## GitHub Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/github-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:41:57+00:00
**Scraped:** 2026-08-11T07:16:58.931503+00:00

GitHub Plugin for Threat Exchange - Netskope Technical Documentation
GitHub Plugin for Threat Exchange
This document explains how to configure the GitHub plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows for sharing of file hashes of GitHub repository files with Netskope.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Threat Prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured
A GitHub Account with access to repositories from which the file hashes are required to be fetched.
Workflow
Get the GitHub API token.
Configure the GitHub Plugin.
Configure sharing between Netskope and GitHub.
Validate the GitHub Plugin.
Click play to watch a video.
Get the GitHub API Token
Log in to GitHub.
In the  top right corner of any page, click your profile photo, and then click
Settings
.
In the left panel, click
Developer settings
.
In the left panel, click
Personal access tokens
.
Click
Generate new token
from top right corner.
In Note, give your token a descriptive name.
Select the following scopes for repo and user.
Click the
Generate token
icon.
Copy the newly generated token by pressing
and save it in a secure location. This token is used to configuring the GitHub plugin.
Configure the GitHub Plugin
In Cloud Exchange, go to
Settings
and click
Plugins
.
Search for and select the
GitHub
plugin box to open the plugin creation pages.
Enter the Basic Information on the first page:
Configuration Name: Enter a name appropriate for your integration.
Poll Interval: Adjust to environment needs. We recommend not to go below 5 minutes for production environments.
Aging Criteria: Leave the default.
Override Reputation:  Leave the default.
Enable SSL Verification: Leave the default.
Click
Next
.
Enter the Configuration Parameters on the second page:
Base URL: Enter the Base URL of your GitHub API (only if default needs to be changed).
API Token: Enter your GitHub API token.
Repository Name: Enter comma-separated names of the repositories for which the file hashes are to be fetched. Leave empty to include all accessible repositories.
Tag: Leave the default.
Quota Limit: Leave the default.
Click
Save
in the top right corner. Go to
Threat Exchange > Plugins
to see your new GitHub plugin.
Configure Sharing for Netskope and GitHub
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
, and in the Source Configuration dropdown list, select
Github
.
Select a Business Rule, and then select
Netskope
for the Destination Configuration. Sharing configurations are unidirectional. data obtained from one plugin is shared with another plugin. To achieve bi- or multi-directional sharing, configure each separately.
Select a Target. Each plugin will have a different target or destination for the IoC.
Depending on the Target selected, Add to URL List or Add to File Hash List, the remaining options change. If using a File Hash List, jump to the next step.
For a URL List, select a List Name, enter a New List Name. The List Name must exist in the Netskope UI. For information about creating a URL List, refer to
Add a URL List
. Now select a URL List Type, and then a List Size and Default URL.
For Add a File Hash List, enter a List Name, List Size, and Default File Hash. The List Name needs to exist in your Netskope UI at
Settings > Policies > Profiles
. For information about creating a File Profile for hashes, refer to
Adding a File Profile
Click
Save
.
Repeat steps 2-6, but select
Netskope
as the Source Configuration and
GitHub
as the Destination Configuration.
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Note
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin
API Source
, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect.
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Modify, Test, or Delete a Sharing Configuration
Each configuration supports 3 actions:
Edit the rule by clicking on the pencil icon.
Test the rule by clicking on the synchronization icon. This tests how many IoC will actually be sent to the destination system based on the timeframe and the rule.
Delete the rule by clicking on the garbage can icon.
Validate the GitHub Plugin
In order to validate the integration you must have at least one repository accessible to the configured user on GitHub.
Go to
Threat Exchange
, and click
Threat IoCs
. You should see records from your GitHub plugin. You can filter based on Source values to check both the Netskope and GitHub plugin.
In the Netskope UI, go to
Policies > File > Your Custom File Profile
and click
File Hash
.
If data is not being brokered between the platforms, you can look at the audit logs in Cloud Exchange. In Cloud Exchange go to
Logging
and look through the logs for errors.
In this Topic
GitHub Plugin for Threat Exchange

---
## Manage Threat Exchange Business Rules and IoC Sharing
**URL:** https://docs.netskope.com/en/manage-threat-exchange-business-rules-and-ioc-sharing/
**Last Modified:** 2026-03-21T02:21:37+00:00
**Scraped:** 2026-08-11T07:17:32.010451+00:00

Manage Threat Exchange Business Rules and IoC Sharing - Netskope Technical Documentation
Manage Threat Exchange Business Rules and IoC Sharing
Write-access users can configure Business Rules and IoC sharing. This section describes how to configure the initial business rules used to identify IoCs to be shared, and the IoC sharing configured between plugins (and therefore connected vendor systems) based on the invoked business rules. The result is system-detected IoC sharing between two plugged-in solutions of all IoCs matching the business rule.
Configure Threat Exchange Business Rules
Map a Threat Exchange Business Rule to a Target
View Threat Exchange Business Rules
Configure Threat Exchange IoC Sharing
IoC Sharing Best Practices
List IoCs and Use Filter Options
In this Topic
Manage Threat Exchange Business Rules and IoC Sharing

---
## Mandiant Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/mandiant-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:45:30+00:00
**Scraped:** 2026-08-11T07:17:34.446043+00:00

Mandiant Plugin for Threat Exchange - Netskope Technical Documentation
Mandiant Plugin for Threat Exchange
This document explains how to configure the Mandiant Plugin with Threat Exchange module of the Netskope Cloud Exchange platform. This integration fetches IoCs of the type of URL (URL, FQDN, IPv4, and IPv6), and MD5 from the Google Mandiant platform. This plugin does not support sharing of indicators. You need a Google Mandiant Key ID and Key secret to configure the plugin.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Threat Prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Mandiant instance with admin access, and a subscription to Mandiant Advantage Threat Intelligence feeds: Security Operations feed and/or Fusion feed.
Connectivity to the following host:
https://api.intelligence.mandiant.com/
.
Mandiant Plugin Support
Fetched Indicator Types
Shared Indicator Types
URL, MD5, FQDN, IPV4, IPV6
Not supported
Mappings
Severity Mapping (Netskope field – Mandiant fields)
Netskope CE Fields
Mandiant field
UNKNOWN
0 or not available
LOW
10 <= mscore <= 39
MEDIUM
40 <= mscore <= 69
HIGH
70 <= mscore <= 89
CRITICAL
90 <= mscore <= 100
Mappings for Pull (Netskope field – Mandiant fields)
Netskope CE Fields
Mandiant Field
value
value
type
type
firstSeen
first_seen
lastSeen
last_seen
severity
mscore
tags
Category, attributed_associations.name
Permissions
Any “Free Subscription” account.
API Details
List of APIs Used
API Endpoint
Method
Use case
https://api.intelligence.mandiant.com/token
POST
To generate API Token
https://api.intelligence.mandiant.com/v4/indicator
GET
To get an indicators list
Generate Token
Example:
API Endpoint:
https://api.intelligence.mandiant.com/token
Method:
POST
Parameters:
grant_type: client_credentials
Headers:
Content-Type: application/x-www-form-urlencoded
Authorization
:
Basis <base64 encoded client id and client secret separated by colon>
API Request Endpoint:
https://api.intelligence.mandiant.com/token?grant_type=client_credentials
Sample API Response:
{
“access_token”: “86347c299bd7885736652a2506d26cf65361f795b69d4583xxxxxxxxxxxxxxxx”,
“token_type”: “Bearer”,
“expires_in”: 43199
}
Pull Indicators
Example:
API Endpoint:
https://api.intelligence.mandiant.com/v4/indicator
Method:
GET
Parameters:
start_epoch:1698050685
limit:1000
sort_by:last_updated:asc
end_epoch:1698054285
gte_mscore:50
exclude_osint:False
API Request Endpoint:
https://api.intelligence.mandiant.com/v4/indicator
Sample API Response:
{
“indicators”: [
{
“id”: “md5–98bf8a96-3e53-55ba-8d73-ec5295035298”,
“mscore”: 50,
“type”: “md5”,
“value”: “7462407e3723d097835aaf4832813f39”,
“is_publishable”: true,
“sources”: [
{
“first_seen”: “2023-10-22T20:04:42.689+0000”,
“last_seen”: “2023-10-22T20:04:42.689+0000”,
“osint”: true,
“category”: [],
“source_name”: “dtm.blackbeard”
}
],
“misp”: {
“akamai”: false,
“alexa”: false,
“amazon-aws”: false,
“apple”: false,
“automated-malware-analysis”: false,
“bank-website”: false,
“captive-portals”: false,
“censys-scanning”: false,
“cisco_1M”: false,
“cisco_top1000”: false,
“cisco_top10k”: false,
“cisco_top20k”: false,
“cisco_top5k”: false,
“cloudflare”: false,
“common-contact-emails”: false,
“common-ioc-false-positive”: false,
“covid”: false,
“covid-19-cyber-threat-coalition-whitelist”: false,
“covid-19-krassi-whitelist”: false,
“crl-hostname”: false,
“crl-ip”: false,
“dax30”: false,
“digitalside”: false,
“disposable-email”: false,
“dynamic-dns”: false,
“eicar.com”: false,
“empty-hashes”: false,
“fastly”: false,
“findip-host”: false,
“google”: false,
“google-chrome-crux-1million”: false,
“google-gcp”: false,
“google-gmail-sending-ips”: false,
“googlebot”: false,
“ipv6-linklocal”: false,
“majestic_million”: false,
“majestic_million_1M”: false,
“microsoft”: false,
“microsoft-attack-simulator”: false,
“microsoft-azure”: false,
“microsoft-azure-appid”: false,
“microsoft-azure-china”: false,
“microsoft-azure-germany”: false,
“microsoft-azure-us-gov”: false,
“microsoft-office365”: false,
“microsoft-office365-cn”: false,
“microsoft-office365-ip”: false,
“microsoft-win10-connection-endpoints”: false,
“moz-top500”: false,
“mozilla-CA”: false,
“mozilla-IntermediateCA”: false,
“multicast”: false,
“nioc-filehash”: false,
“openai-gptbot”: false,
“ovh-cluster”: false,
“parking-domain”: false,
“parking-domain-ns”: false,
“phone_numbers”: false,
“public-dns-hostname”: false,
“public-dns-v4”: false,
“public-dns-v6”: false,
“public-ipfs-gateways”: false,
“rfc1918”: false,
“rfc3849”: false,
“rfc5735”: false,
“rfc6598”: false,
“rfc6761”: false,
“second-level-tlds”: false,
“security-provider-blogpost”: false,
“sinkholes”: false,
“smtp-receiving-ips”: false,
“smtp-sending-ips”: false,
“stackpath”: false,
“tenable-cloud-ipv4”: false,
“tenable-cloud-ipv6”: false,
“ti-falsepositives”: false,
“tlds”: false,
“tranco”: false,
“tranco10k”: false,
“umbrella-blockpage-hostname”: false,
“umbrella-blockpage-v4”: false,
“umbrella-blockpage-v6”: false,
“university_domains”: false,
“url-shortener”: false,
“vpn-ipv4”: false,
“vpn-ipv6”: false,
“whats-my-ip”: false,
“wikimedia”: false,
“zscaler”: false
},
“last_updated”: “2023-10-23T08:45:19.739Z”,
“first_seen”: “2023-10-22T20:04:42.000Z”,
“last_seen”: “2023-10-22T20:04:44.000Z”
},
],
“next”: “FGluY2x1ZGVfY29udGV4dF91dWlkDnF1ZXJ5VGhlbkZldGNoKhZSLVdHTlNkN1MyZTA0NTRWTTk5bkxRAAAAADMcHecWcnR4bm9DOUtUTk96SVQ4bHdkLXB3QRZfM3JkdWVZcVRodTRxc3F6WkhYSmxnAAAAADPp8u0WaVNUa2J0TmRRVnUtcXJuVEhqX0pBQRY4alo4RU1sMVNucUltWEdGM2NKcnF3AAAAAD0Hx2cWTDZHTzJBM2lTM09kcnd5U2cwR1Y1QRZKQWJ1NGc5UlRCV3hCSW0zTG82aDNBAAAAADKcN64WVFVzRHBNZl9TaEs5UDZyVXVZYnM2ZxZhTlNRMWswMFNkT0l5VXhDM18wVnBRAAAAAFKUD6AWTEdjMWlMTjZUV2E3aXh1Vll4MVB0dxZZX1plVFpwOFJPbXhJVW54SzVHRzBBAAAAADnHZbkWNzBzRXhnZXFTZi1qR2lGYUpnSGpEQRZlYXQxYXZZTVFGMnlISUVpRklWa29BAAAAAEW_LlMWT1NQR1NjcGtST1c5b05TRjlnWUtGQRZxMEtYNHNpTlNjR3FxRy1YX1dELUdnAAAAADCdndUWa19EQlNvNkVRZDZOeGlpc0JhX0hRdxZVRmdzeEtaUVRORzllMmV6UXRka2NRAAAAADC6SvEWTWFVRmJaaFJSOENaQUVMYjVzRGJsdxZVRmdzeEtaUVRORzllMmV6UXRka2NRAAAAADC6SvAWTWFVRmJaaFJSOENaQUVMYjVzRGJsdxZJNDNlSUg3OVR6U19iWWFRRTQtWE9nAAAAAEv49akWMGxpaG5wQXVUN20tQ1pPY0czOVRUdxZqSlhzQ0w4SlJjeVRrbWM5clNuZFZRAAAAADCiS7sWU29ZTTBRN3hUd2VRNkFfT09WeDk1dxZNeUR3M1F3SVE3R1VFNzFQdXA5b3VnAAAAADK8xRcWaWRiWC15V29SZENDS1FpUHVVMWM4dxY4RFN4T3p1OFIxLWdlc2VwaGdPR2ZBAAAAAEAyJV0WeHV0Z09DY0RSX0doWXZSek1ZQnJjdxZfdXdQYlJmZVNFbTRsanhITnFCMEtBAAAAADnayq8WT0lPU25zc3BSWm1BQlJtVTMxd1BSQRZUdS04b3NnZ1NNcUxSSTNiTHBhdVZ3AAAAAEMF6YcWZVcwMmliVWtSY09LYVp3VG96eHhkQRZNeUR3M1F3SVE3R1VFNzFQdXA5b3VnAAAAADK8xRYWaWAADMzb-===”
}
Performance Matrix
Below is the performance reading conducted for fetching 100K IOCs in each plugin lifecycle on a Large CE instance with the below specifications.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Google Mandiant
~10K per minute
Indicators shared to Google Mandiant
Not Supported
User Agent
The user-agent added in this plugin is in the following format netskope-ce-<ce_version>-<module>-<plugin_name>-v<plugin_version>
netskope-ce-4.2.0-cte-google-mandiant-v2.0.0
Workflow
Create a custom File Profile.
Create a Malware Detection Profile.
Create a Real-time Protection Policy.
Get Mandiant credentials.
Configure a Mandiant Plugin.
Configure sharing between Netskope and Mandiant.
Validate the Mandiant Plugin.
Click play to watch a video.
Create a Secure Web Gateway Custom File Profile for Mandiant
In the Netskope UI, go to
Policies
, select
File
, and click
New File Profile
.
Click
File Hash
in the left panel, select
SHA256
from the File Hash dropdown list.
Enter a temporary value in the text field. Netskope does not support progressing without having a value in this field, and recommends entering a string of 64 characters that consists of the character
f
. For example,
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
. This will have a very low possibility of matching a valid file format.
Click Next
.
Enter a Profile Name and a Description. We recommend not having blank spaces in your profile name; use underscores for spaces.
Click
Save
.
To publish this profile into the tenant, click
Apply Changes
in the top right.
Create a Malware Detection Profile for Mandiant
In the Netskope UI, go to
Policies
, select
Threat Protection
, and click
New Malware Detection Profile
.
Click
Next
.
Note
For this configuration example, we will be using the intelligence for this list as a block list. Netskope does support inclusion of both allow and block lists in the threat profiles.
Click
Next
again.
Select the File Profile you created in the previous section and click
Next
.
Enter a Malware Detection Profile name and click
Save Malware Detection Profile
.
To publish this profile in the tenant, click
Apply Changes
in the top right.
Create a Real-time Threat Protection Policy for Mandiant
In the Netskope UI, go to
Policies > Real-time Protection
.
Note
The policy configured here is just an example. Modify as appropriate for your organization.
Click
New Policy
and select
Threat Protection
.
For
Source
, leave the default (User = All Users)
For
Destination
: select
Category
The Category section expands and allows you to search and select categories. Click
Select All
.
When finished, click outside of the Category section.
When the Activities & Constraints section opens, click
Edit
.
Select
Upload
and
Download
, and then click
Save
.
For
Profile & Action
, click in the text field.
Select the Malware Detection profile you created in the previous section.
For the Severity Levels, change all of the Actions settings from
Action: Alert
to
Action: Block
.
Select a template to choose which block message is sent to the user.
For
Set Policy
, enter a descriptive Policy Name.
Click
Save
in the top right to save the policy.
Choose the
To the top
option when it appear. (Or appropriate location in your security policy)
To publish this policy into the tenant, select
Apply Changes
in the top right.
Get your Mandiant Key ID and Key Secret
Go to
https://login.mandiant.com/
and log in.
Click on the
Mandiant Advantage Threat Intelligence
option under
Applications.
Click on Settings.
Go to API Access and Keys Section.
Click on the “Get Key ID and Secret” Button to retrieve your key ID and Secret.
Copy the Access ID and Secret Key, as these will not be accessible after closing the window. These are required to configure the Mandiant plugin.
Configure the Mandiant Plugin
In Cloud Exchange, go to
Settings
and click
Plugins
.
Search for and select the Mandiant plugin box to open the plugin creation pages.
Enter and select the Basic Information on the first page:
Configuration Name: Unique name for the configuration.
Sync Interval: Adjust the Sync Interval to appropriate value : Suggested is 5+ minutes.
Aging Criteria: Leave Default.
Override Reputation: Leave Default.
Enable SSL verification: Enable if SSL verification is required for communication.
Use System Proxy: Enable if proxy is required for communication.
Click
Next
.
Enter the Configuration Parameters on the second page:
Key ID: Enter the APIv4 Key ID generated from the ‘Setting > API Access and Keys Section’ of your Mandiant platform.
Key Secret: Enter the APIv4 Key Secret generated from the ‘Setting > API Access and Keys Section’ of your Mandiant platform.
Minimum Indicator Confidential Score (IC-Score): Provide the IC-Score from 0 to 100. Only the indicators with IC-Score greater than or equal to the specified score will be fetched.
Exclude Open Source Indicators: Exclude open source indicators from Mandiant.
Enable Tagging: Enable/Disable tagging functionality.
Initial Range: Number of days to pull the data for the initial run.
Click
Save
.
Configure a Business Rule for Mandiant
To share indicators from Google Mandiant to Netskope you need to have a business rule that will filter out the indicators that you need to share. To configure a business rule, follow the below steps:
Go to
Threat Exchange > Business Rule > Create New Rule
.
Add your required filter for the IoCs you want to share and click Save.
Configure Sharing for Mandiant
To share IoCs from the Google Mandiant plugin to Netskope, follow the below steps:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Google Mandiant), Business Rule, Destination Configuration (Netskope), and Target, and select the existing IoC List Name, or create a new IoC list on the platform.
Click
Save
.
Validate the Mandiant Plugin
Validate the Pull
You can verify the pulling of IOCs from the plugin by going to Loggings and checking the pulled logs from the CTE Google Mandiant plugin.
You can check the pulled data stored in CE under Threat Exchange > Threat IOCs. Search the IOCs pulled from the plugin. You can also filter the IOCs based on the tags, as shown below.
Log in to Mandiant.
Click
Threat Intelligence > Threat Intelligence
. Check the Alerts are present while clicking on any Incident -> Alerts & Insights.
Validate the Push
The Google Mandiant plugin does not support the pushing of IoCs. You can push the IoCs pulled from the Google Mandiant to Netskope or any Third-party plugin supported in Threat Exchange.
Follow the below steps to verify the pushed IoCs to Netskope.
To validate the pushed indicator on Netskope CE, go to Threat IoCs and search for IoCs that are shared with Netskope.
You can also verify the pushed IoCs from Logging in Netskope CE.
Filter the logs available from the Netskope plugin.
To validate the IoCs shared on Netskope follow the below steps:
Log in to the Netskope tenant. Go to
Policies > Web > URL Lists
. Click on your URL List that you selected while configuring the sharing and check the shared IOCs.
Note that we have shared all types of URLs (URL, FQDN, IP Address) pulled from Google Mandiant to Netskope URL List.
Log in to Netskope tenant. Go to
Policies > File > File Profile
. Click on your File List which you selected while configuring the sharing and check the shared IoCs.
Note that we have shared both types of MD5 pulled from Google Mandiant to Netskope File List.
For more information, go to Logging in the left nav panel.
Troubleshooting
Receiving error for exit code 401, Unauthorization
While configuring the plugin if you receive any kind of error in Key ID and Key Secret please check Key ID and Key Secret from the Mandiant platform.
Go to
https://login.mandiant.com/
and log in.
Click on the
Mandiant Advantage Threat Intelligence
option under
Applications.
Click
Settings
.
Go to the API Access and Keys Section.
Click
Get Key ID and Secret
to retrieve your key ID and Secret.
Verify both are correct.
When not able to fetch IOCs from Google Mandiant
If you are not able to fetch IoCs from Mandiant to Netskope Cloud Threat Exchange
Log in to Mandiant.
Click on Threat Intelligence-> Threat Intelligence
Check the Alerts are present while clicking on any Incident -> Alerts & Insights
Make sure alerts are present and if present they should be in your initial range.
,/p>
In this Topic
Mandiant Plugin for Threat Exchange

---
## Map a Threat Exchange Business Rule to a Target
**URL:** https://docs.netskope.com/en/map-a-threat-exchange-business-rule-to-a-target/
**Last Modified:** 2025-10-31T23:46:43+00:00
**Scraped:** 2026-08-11T07:17:35.647494+00:00

Map a Threat Exchange Business Rule to a Target - Netskope Technical Documentation
Map a Threat Exchange Business Rule to a Target
Write-access users can map a Threat Exchange business rule to a target. This section explains how to configure IoC sharing between the plugins (and therefore connected vendor systems). Make sure to identify the sharing requirements between systems in advance of configuration. The sharing filters (requires a business rule) allow for greater control over what data is shared with the plugin.
Go to
Threat Exchange > Sharing
.
Click
Add Sharing Configuration
.
Select a Source Configuration, Destination Configuration, and Business Rule.
Based on the selected Source Configuration, Destination Configuration list will be populated.
Based on the selection of Destination Configuration, a list of Target will be populated. Select a Target that you want to map to the selected Business Rule.
If the Target has some required parameters, user will need to add those.
Click
Save
.
Adding a new sharing configuration will share the existing IoCs (matching business rule) of the Source Configuration to the Destination Configuration.
The sharing configuration is unidirectional by default: data obtained from one plug-in is shared with another plugged-in system. To achieve bi-directional sharing, configure both directions of sharing separately.
Note
Plugins that do not have API for ingesting data can not receive threat data. This is true of the installed plugin “API Source” which provides a bucket associated with an API endpoint for remote 3rd party systems to push data to.
In this Topic
Map a Threat Exchange Business Rule to a Target

---
## Microsoft Defender for Endpoint Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/microsoft-defender-for-endpoint-plugin-for-threat-exchange/
**Last Modified:** 2026-06-11T02:10:36+00:00
**Scraped:** 2026-08-11T07:17:43.331041+00:00

Microsoft Defender for Endpoint Plugin for Threat Exchange - Netskope Technical Documentation
Microsoft Defender for Endpoint Plugin for Threat Exchange
Release Notes
1.4.0
Added
Added support for indicator retraction.
Added ‘Type of Threat data to pull’ and ‘Enable Polling’ configuration parameters.
Added support to bifurcate the URL by types (Domain, IPv4, IPv6 & URL).
Added resolution for error logs starting from CE v6.0.0.
Added support for storing access token in the storage.
1.3.1
Added
Added ‘Indicators with Generated Alert’ field in Configuration parameters.
Added ‘Generate Alert’ field in the sharing configuration.
Removed
Removed actions ‘Alert’ and ‘Alert and Block’ from configuration and sharing configuration.
1.3.0
Added
Added support for different regions for Base URL.
Added support for fetching indicators on the basis of actions provided.
Added support for Tagging on the basis of indicator action.
1.2.0
Changed
Replaced beta API’s with stable API endpoints.
1.1.0
Added
Added push support.
Changed
Changed deprecated apis.
1.0.0
Added
Initial release.
This document explains how to configure the Microsoft Defender for Endpoint v1.4.0 plugin for the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to pull indicators of type URL, IPv4, IPv6, Domain, MD5 and SHA256 from the
System > Settings > Endpoints > Indicators
page of the Microsoft Defender for Endpoint platform. This plugin supports sharing indicators of type URL, IPv4, IPv6, Domain, MD5 and SHA256 to the
System > Settings > Endpoints > Indicators
page in the Microsoft Defender for Endpoint platform. This plugin also supports pull and push retraction of indicators from the Microsoft Defender for Endpoint platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope tenant.
A Secure Web Gateway subscription for URL sharing.
A Netskope Cloud Exchange tenant with the the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Microsoft Defender for Endpoint account.
Your Microsoft Azure Tenant ID, Client ID, and Client Secret.
A Microsoft Azure Application with the Ti.ReadWrite.All Permission. For more information, go to this
article
.
Connectivity to these hosts:
https://api.securitycenter.microsoft.com/api/indicators
https://securitycenter.windows.com
https://login.microsoftonline.com
https://portal.azure.com
We have not tested the plugin end-to-end with base URLs
api-gcc.securitycenter.microsoft.us
and
api-gov.securitycenter.microsoft.us
since we don’t have a GCC tenant with us.
Microsoft Defender for Endpoint Plugin Support
This plugin is used to pull indicators of type URL, IPv4, IPv6, Domain, MD5 and SHA256 from the
System > Settings > Endpoints > Indicators
page of the Microsoft Defender for Endpoint platform. This plugin supports sharing indicators of type URL, IPv4, IPv6, Domain, MD5 and SHA256 to the
System > Settings > Endpoints > Indicators
page in the Microsoft Defender for Endpoint platform. This plugin also supports pull and push retraction of indicators from the Microsoft Defender for Endpoint platform.
Fetched Indicator Types
Shared Indicator Types
URL, IPv4, IPv6, Domain, MD5 and SHA256
URL, IPv4, IPv6, Domain, MD5 and SHA256
Indicators of the type URL will be differentiated as IP, URL or Domain and then ingested to Microsoft Defender for Endpoint. In Cloud Exchange, some of the IPs or Domains will be stored as type URL. When sharing those IoCs, this plugin will differentiate IPs,Domains and URL and will share IPs as type IP and Domains or URLs or FQDNs as URL/Domains.
IoC Retraction
IoC Retraction (Pull)
: Indicators will be fetched from Microsoft Defender for Endpoint and in the subsequent pull cycles if some indicators are deleted on Microsoft Defender for Endpoint or not within the retraction interval range then they will be marked as Retraced in Cloud Exchange.
IoC Retraction (Push)
: Retracted indicators present on Cloud Exchange will be deleted from Microsoft Defender for Endpoint during sharing.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
Yes
Mappings
Pull Mappings
Here are the mappings for pulled IoCs.
Netskope CTE Field
Defender API Field
Description
Indicator.value
indicatorValue
Indicator.type
indicatorType
Url → URL; DomainName→ Domain; FileMd5 → MD5; FileSha256 → SHA256; IpAddress→IPv4/IPv6
Indicator.firstSeen
creationTimeDateTimeUtc
Indicator.lastSeen
lastUpdateTime
Indicator.comments
title + description
Concatenated as “
<title>
|
<description>
“
Indicator.severity
severity
Indicator.tags
action
creates Defender_
<action>
tag; one tag per indicator.
Severity Mappings for Pull
Netskope Severity
Defender Severity
LOW
Low
MEDIUM
Medium
HIGH
High
UNKNOWN
Anything else
Push Mappings
Here are the mappings for shared IoCs.
Netskope CTE Field
Defender API field
Description
Indicator.value
indicatorValue
Indicator.type
indicatorType
URL → Url
Domain → DomainName
FQDN → DomainNameIPv4/IPv6 → IpAddressMD5 → FileMd5SHA256 → FileSha256
Indicator.comments
description
Formatted as ” Netskope-CTE |
<source>
| <comments>”
Indicator.severity
severity
action_dict.action (configured)
action
Mapped via action_conversion: unknown/alert/Alert → Audit; allow → Allowed; block → Block; AlertAndBlock → Block (and forces generateAlert=True).
action_dict.generate_alert
generateAlert
If action is Audit: forced True; otherwise uses configured Yes/No (boolean).
Indicator.type/value
type
“Indicator
<value>
of type
<indicatorType>
” (uses resolved type).
Severity Mapping for push
Netskope Severity
Defender Severity
LOW
Low
MEDIUM
Medium
HIGH
High
CRITICAL
High
Permissions
Microsoft Azure Application with the
Ti.ReadWrite.All
Permission. For more information, go
here
.
API Details
List of APIs used
Netskope CTE Field
Proofpoint API field
Type
threatStatus
threatStatus
String
interval
interval
Datetime
sinceSeconds
sinceSeconds
Integer
eventTypes
eventTypes
String
Authentication
This plugin uses the Python library to generate authentication tokens for .
Library: Microsoft Authentication Library for Python (msal)
Usage: Microsoft Authentication Library for Python (msal) to get authentication token for Microsoft Defender APIs.
Create a new session with credentials
scope = ["https://api.securitycenter.microsoft.com/.default"]
authority = "https://login.microsoftonline.com/{tenantID}
app = msal.ConfidentialClientApplication(
           client_id={clientID}, authority=authority, client_credential={clientSecret}, proxies=proxy
)
auth_json = app.acquire_token_for_client(scopes=scope)
auth_token = auth_json.get("access_token", "")
Pull Indicators
API Endpoint:
<Base URL>
/api/indicators
Method:
GET
Headers
Key
Value
Authorization
Bearer
<auth_token>
Content-Type
application/json
Accept
application/json
User-Agent
netskope-ce-6.1.0-cte-microsoft-defender-for-endpoint-v1.4.0
Parameters
Key
Value
$filter
combining creationTimeDateTimeUtc+ge+<UTC timestamp> and optional actions: action+eq+'<Action>’ joined with or.
e.g., creationTimeDateTimeUtc+ge+2025-02-05T00:00:00Z and (action+eq+’Alert’ or action+eq+’Audit’)
Sample API Response
{
  "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Indicators",
  "value": [
    {
      "id": "66407",
      "indicatorValue": "a40da157d2e56d26c01d8d57947779e1b403999ed32a1ac3553b46f501542e0d",
      "indicatorType": "FileSha256",
      "action": "Audit",
      "createdBy": "d45ccecf-7406-47f6-90e5-05f0b3f76094",
      "severity": "Informational",
      "category": 1,
      "application": null,
      "educateUrl": null,
      "bypassDurationHours": null,
      "title": "Indicator a40da157d2e56d26c01d8d57947779e1b403497e999a1ac3553b46f501542e0d of type FileSha256",
      "description": "Pull Test",
      "recommendedActions": null,
      "creationTimeDateTimeUtc": "2026-01-21T09:08:36.9319034Z",
      "expirationTime": null,
      "lastUpdateTime": "2026-01-21T09:08:36.9319034Z",
      "lastUpdatedBy": null,
      "rbacGroupNames": [],
      "rbacGroupIds": [],
      "notificationId": null,
      "notificationBody": null,
      "version": null,
      "mitreTechniques": [],
      "historicalDetection": false,
      "lookBackPeriod": null,
      "generateAlert": true,
      "additionalInfo": null,
      "createdByDisplayName": "Demo app",
      "externalId": null,
      "createdBySource": "PublicApi",
      "certificateInfo": null
    },
    {
      "id": "66408",
      "indicatorValue": "521e25b2d1bb9f8059dc7b0e86d05454bd599941e2a59620521ba1510be110e6",
      "indicatorType": "FileSha256",
      "action": "Audit",
      "createdBy": "d45ccecf-7406-47f6-90e5-05f999f76094",
      "severity": "Informational",
      "category": 1,
      "application": null,
      "educateUrl": null,
      "bypassDurationHours": null,
      "title": "Indicator 521e25b2d1bb9f8059dc7b0e86d05454bd565441e9999620521ba1510be110e6 of type FileSha256",
      "description": "Pull Test",
      "recommendedActions": null,
      "creationTimeDateTimeUtc": "2026-01-21T09:08:37.7747306Z",
      "expirationTime": null,
      "lastUpdateTime": "2026-01-21T09:08:37.7747306Z",
      "lastUpdatedBy": null,
      "rbacGroupNames": [],
      "rbacGroupIds": [],
      "notificationId": null,
      "notificationBody": null,
      "version": null,
      "mitreTechniques": [],
      "historicalDetection": false,
      "lookBackPeriod": null,
      "generateAlert": true,
      "additionalInfo": null,
      "createdByDisplayName": "Demo app",
      "externalId": null,
      "createdBySource": "PublicApi",
      "certificateInfo": null
    }
]
}
Push Indicators
API endpoint:
<Base URL>
/api/indicators
Method:
POST
Headers
Key
Value
Authorization
Bearer
<auth_token>
Content-Type
application/json
Accept
application/json
User-Agent
netskope-ce-6.1.0-cte-microsoft-defender-for-endpoint-v1.4.0
Body
{
        "indicatorValue": "malicious.example.com",
        "indicatorType": "DomainName",
        "action": "Block",
        "title": "Indicator malicious.example.com of type DomainName",
        "description": " Netskope-CTE | demo | Example domain IOC",
        "severity": "High",
        "generateAlert": true,
}
Sample API Response (Status Code: 201)
{
  "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Indicators/$entity",
  "id": "67908",
  "indicatorValue": "malicious.example.com",
  "indicatorType": "DomainName",
  "action": "Block",
  "createdBy": "d45ccecf-7406-47f6-90e5-05f0b3f76094",
  "severity": "High",
  "category": null,
  "application": null,
  "educateUrl": null,
  "bypassDurationHours": null,
  "title": "Indicator malicious.example.com of type DomainName",
  "description": " Netskope-CTE | demo | Example domain IOC",
  "recommendedActions": null,
  "creationTimeDateTimeUtc": "2026-02-09T07:01:36.6399107Z",
  "expirationTime": null,
  "lastUpdateTime": "2026-02-09T07:01:36.6399107Z",
  "lastUpdatedBy": null,
  "rbacGroupNames": [],
  "rbacGroupIds": [],
  "notificationId": null,
  "notificationBody": null,
  "version": null,
  "mitreTechniques": [],
  "historicalDetection": false,
  "lookBackPeriod": null,
  "generateAlert": true,
  "additionalInfo": null,
  "createdByDisplayName": "Demo app",
  "externalId": null,
  "createdBySource": "PublicApi",
  "certificateInfo": null
}
Delete Indicators
API endpoint:
<Base URL>
/api/indicators/{id}
Method:
DELETE
Headers
Key
Value
Authorization
Bearer
<auth_token>
Content-Type
application/json
Accept
application/json
User-Agent
netskope-ce-6.1.0-cte-microsoft-defender-for-endpoint-v1.4.0
Parameters
Key
Value
id
ID of the Indicator to delete on Defender platform
Delete Indicators for retraction
API endpoint:
<Base URL>
/api/indicators/BatchDelete
Method:
POST
Headers
Key
Value
Authorization
Bearer
<auth_token>
Content-Type
application/json
Accept
application/json
User-Agent
netskope-ce-6.1.0-cte-microsoft-defender-for-endpoint-v1.4.0
Body
{
    "IndicatorIds": [
        "<Indicator ID>"
    ]
}
Sample API Response
Status Code: 204 No Content
Performance Matrix
Here is the performance reading conducted by pulling and sharing 15K indicators from/to Microsoft Defender for Endpoint on a Large CE Stack with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicator fetched from Microsoft Defender for Endpoint
~15K IOCs per minute
Indicators shared with CrowdStrike
~100 per minute
For sharing of IoCs, Microsoft Defender has a rate limit of 100 IoCs per minute. Refer this
documentation
.
User Agent
netskope-ce-6.1.0-cte-microsoft-defender-for-endpoint-v1.4.0
Workflow
Get your Tenant ID, Application (Client) ID, and Client Secret from Microsoft Defender.
Add API Permissions for Microsoft Defender.
Configure the Microsoft Defender for Endpoint plugin.
Configure a Business Rule for Microsoft Defender for Endpoint.
Configure Sharing for Netskope and Microsoft Defender for Endpoint.
Validate the Microsoft Defender for Endpoint Plugin.
Watch a Video
Click play to watch a video.
Get your Tenant ID, Application (Client) ID and Client Secret from Microsoft Defender
Go to https://entra.microsoft.com/ and log in with your credentials
Click
App registrations
.
Click
New Registration
.
Provide the name for the application and click
Register
.
Copy the Application (Client ID), which is the Client (Application) ID in Netskope. Also copy the Directory (tenant) ID, which is tenant ID in Netskope. Click
Certificates & Secrets.
Click
New client secret
. Add a description and click
Save
.
Copy the value; it is the Client Secret needed for the plugin configuration.
Add API Permissions
In the left panel, click
API permissions
.
Click
Add a permission
.
Click
APIs my organization uses
, and then click
WindowsDefenderATP
.
Click
Application permissions
.
Select the
Ti.ReadWrite.All
permissions and click
Add permission
.
Click
Grant admin consent for Contoso
.
Click
Yes
.
Configure the Microsoft Defender for Endpoint Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Microsoft Defender for Endpoint v1.4.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name:
Unique name for the configuration.
Sync Interval:
Leave the default.
Aging Criteria:
Expiry time of the plugin in days. (Default: 90)
Override Reputation:
Set a value to override the reputation of indicators received from this configuration.
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. These configuration parameters determine how tags are stored for indicators pulled for this configuration.
Enable SSL Validation:
Enable SSL Certificate validation.
Click
Next
and enter the Configuration Parameters:
Base URL:
Base URL of the Microsoft Defender for Endpoint platform.
Tenant ID:
Directory (Tenant) ID of the Microsoft Entra ID application.
Application ID:
Application (Client) ID of the Microsoft Entra ID application.
Application Secret:
Client Secret of the Microsoft Entra ID application.
IOC Source (Applicable only while sharing IoCs):
The source where this indicator originated. This can be used for tracking where this indicator was defined. Limit 200 characters.
Type of Threat data to pull:
Type of Threat data to pull. If no threat type is selected, all threat type indicators will be pulled.
Actions:
Select the action(s) to filter the pulled indicators. If no action is selected, all indicators will be pulled regardless of their action.
Indicators with Generated Alert:
Select whether to pull indicators based on their
Generate Alert
flag.
Both
pulls all indicators regardless of this flag.
Enable Polling:
Enable/Disable polling data from Microsoft Defender for Endpoint. Disable if you only need to push indicators to Microsoft Defender for Endpoint.
Retraction Interval (in days):
Specify the number of days for which IoC retraction should be run for Microsoft Defender for Endpoint indicators. This parameter is applicable only if
IoC(s) Retraction
is enabled in Threat Exchange Settings. Value must be between 1 and 365.
Initial Range (in days):
Number of days to pull the data for the initial run.
Click
Save
.
Configure a Threat Exchange Business Rule for Microsoft Defender for Endpoint
To share indicators fetched from the Microsoft Defender for Endpoint to Netskope, and vice-versa, you need to have a business rule that will filter out the indicators that you want to share. To configure a business rule:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirements in the rule, and then click
Save
.
FQDN present in Cloud Exchange will be shared as URL/Domain in Microsoft Defender.
Configure Sharing for Netskope and Microsoft Defender for Endpoint
To share IoCs from the Netskope Cloud Exchange to the Microsoft Defender for Endpoint platform, and vice versa, follow these steps:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select the Source Configuration (Netskope CTE), the Business Rule, the Destination Configuration (Microsoft Defender for Endpoint), and Target(s). Enter these values:
Action:
The action that is taken if the indicator is discovered in the organization.
Generate Alert:
Generate alerts for the indicators. Note that for the action type
Audit
, the Generate Alert will be
Yes
by default, so even if you keep it as
No
with the action type
Audit
you will see the shared IoCs on Defender will have Generate alert as
Yes
.
Allow Existing Indicators to be deleted?:
Whether or not to delete the existing indicator(s) from the Microsoft Defender for Endpoint platform to insert new indicator(s). If Yes is selected, the oldest indicator will be deleted when max capacity of 15000 active indicators per tenant is exceeded.
Click
Save
.
Follow these steps again, but vice-versa for sharing Microsoft Defender for Endpoint IoCs to Netskope. Select your Source Configuration as Microsoft Defender for Endpoint, a Business Rule, Destination Configuration (CTE Netskope Threat Exchange), and Target.
When finished, click
Save
.
Validate the Microsoft Defender for Endpoint Plugin
Validate the Pull
Pulled data will be listed in Threat Exchange at
Threat IoCs
. You can filter the IoCs pulled from the platform using the filter:
sources.source
,
contains <plugin name>
.
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs for the Microsoft Defender for Endpoint plugin.
To verify the data available for pulling on Microsoft Defender for Endpoint, log in to Microsoft Defender and go to
Settings > Endpoints > Indicators
. You can verify URL indicators from IP Addresses and
URLs/Domains
page, and MD5 and SHA256 from the
File Hashes
page.
Validate the Push
Shared IoCs to Microsoft Defender for Endpoint can be verified at
Logging
in Cloud Exchange.
Note
For sharing of IoCs, Microsoft Defender has a rate limit of 100 IoCs per minute. Refer to the
documentation
.
If the IoCs are not shared within expected time and you do not see any logs in CE related to sharing after the initial log for sharing start then it may be due to the rate limit of Microsoft Defender. You can manually check via the Microsoft Defender’s API, whether the rate limit is exhausted or not for sharing IOCs.
To verify shared indicators on Microsoft Defender. Log in to Microsoft Defender and go to
Settings > Endpoints > Indicators
.
You can filter shared indicators by applying filter like
“Created by: <app_name>”
FQDN present in Cloud Exchange will be shared as URL/Domain in Microsoft Defender.
Validate the Retraction
For verifying the Retracted IoCs from Microsoft Defender, check the logs for IoC Retraction example:
message Like “CTE Microsoft Defender for Endpoint” && message Like “retraction”
.
The IoCs that are deleted on the Microsoft Defender or fall outside the retraction Interval will be marked as Retracted in Cloud Exchange as per the plugin configuration parameters.
To check the retracted IoCs in Cloud Exchange, go to
Threat IoCs
and search for
“sources.source Like “CTE CrowdStrike” && sources.retracted Is equal true”
.
Here’s the Destination Profile on the Netskope tenant before push retraction for CTE Netskope Threat Exchange executes:
You can verify the deletion of IoC from Netskope tenant from the Retraction result filed under particular IoC. In the below image you can see the Retraction result is marked as CTE Netskope Threat Exchange: retracted that means it was deleted from the Netskope tenant.
The sharing result will only be marked if the IoCs are pulled from the source plugin after creating the sharing configuration.
Here’s the URL List on the Netskope tenant after push retraction for CTE Netskope Threat Exchange executes:
This plugin also supports push retraction, which means IoCs pulled from 3rd-party platforms that were shared to Microsoft Defender platforms, and were marked as retracted in Cloud Exchange, will also get deleted from the Microsoft Defender platform. You can verify the same through the Retraction result field.
This is an MD file present on Defender:
Here the retraction result is CTE Microsoft Defender for Endpoint: retracted this means that particular IoC was deleted from Microsoft Defender platform as it was marked as retracted yes in Cloud Exchange.
MD5 was deleted from the Defender platform:
Troubleshooting the Microsoft Defender for Endpoint Plugin
Unable to configure the plugin
This may be due to one of these reasons:
Invalid configuration parameters.
Insufficient permissions.
License Error: During configuration of plugin if you receive error message
“Plugin: Microsoft Defender for Endpoint, Validation error occurred. Received status code: 403, Unauthorized request – No active license found”,
it may indicate that you have selected an incorrect Base URL for the credentials used.
What to do:
Verify all Tenant ID, Application ID and  Application Secret are correct and have proper permissions. Follow the
Configuration on Microsoft Defender
section.
Verify proper
permissions
are provided.
Unable to share IOCs to Microsoft Defender for Endpoint.
This may be due to the max capacity of 15000 active indicators per tenant on Microsoft Defender for Endpoint.
What to do:
Check the total number of IoCs on your Microsoft Defender for Endpoint. If it is 15k then you can edit the sharing configuration with
Allow Existing Indicators to be deleted?
fieldas Yes
.
If Yes is selected, the oldest indicator will be deleted when max capacity of 15000 active indicators per tenant is exceeded.
Error while upgrading the plugin
While updating the plugin from version v1.3.0 to version v1.3.1 user will get an validation error while saving the plugin as follows:
What to do:
In this case the follow the steps to successfully enable the plugin:
Select the skip option.
Go to the configured Threat exchange plugin, click on the edit icon for the Microsoft Defender for Endpoint plugin, and remove the actions
Alert
and
Alert And Block
if selected previously.
Select the value for
Indicators with Generated Alert
field as per your requirement whether you want to pull all the indicators or the one with generated alerts
yes
or
no
.
Save the plugin.
Click on the enable icon and select
Enable
.
In this Topic
Microsoft Defender for Endpoint Plugin for Threat Exchange

---
## Microsoft Defender for Cloud Apps Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/microsoft-defender-for-cloud-apps-plugin-for-threat-exchange/
**Last Modified:** 2026-07-18T00:43:44+00:00
**Scraped:** 2026-08-11T07:17:44.557630+00:00

Microsoft Defender for Cloud Apps Plugin for Threat Exchange - Netskope Technical Documentation
Microsoft Defender for Cloud Apps Plugin for Threat Exchange
Release Notes
1.1.0
Added
Added support for IoC(s) retraction.
Added support for Sanctioned, Unsanctioned, Allow, and Protected status indicators.
Added wildcard character support to indicators.
Fixed
Enhanced error handling and logging with detailed resolutions.
Improved indicator type detection for Domain, Hostname and FQDN types.
Optimized API authentication and request handling.
1.0.1
Changed
Changed Plugin name MCAS to Microsoft Defender for Cloud Apps.
1.0.0
Added
Initial Release.
This document explains how to configure the Microsoft Defender for Cloud Apps v1.1.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to pull IoCs of type Domains (Domains, FQDNs and Hostnames) from
Show navigation > Cloud apps > Cloud app catalog
under Microsoft Defender platform. The plugin supports pull retraction of IoCs from Microsoft Defender. This plugin does not support sharing of IoCs to Microsoft Defender platform.
Prerequisites
To complete this configuration, you need:
Netskope Tenant (or multiple, for example, production and development/test instances)
A Netskope Cloud Exchange instance with the
Tenant plugin
and
Threat Exchange plugin
already configured with the Threat Exchange module enabled.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope Tenant
Microsoft Defender for Cloud Apps platform credentials
Connectivity to the following hosts:
Microsoft Defender Cloud Apps instance URL
Example: https://your-instance.portal.cloudappsecurity.com
Microsoft Defender for Cloud Apps Plugin Support
This plugin is used to pull IoCs of type Domains (Domains, FQDNs and Hostnames) from
Show navigation > Cloud apps > Cloud app catalog
under Microsoft Defender platform. The plugin supports pull retraction of IoCs from Microsoft Defender. This plugin does not support sharing of IoCs to Microsoft Defender platform.
Fetched Indicator Types
Shared Indicator Types
Domains (Domains, FQDNs and Hostnames)
Not Supported
IOC Retraction
IOC Retraction (Pull): IoCs that are deleted on the Microsoft Defender or that are not under the selected status in the plugin configuration will be marked as retraced in Cloud Exchange.
For retraction to work, IoC(s) Retraction toggle must be enabled under Settings > Threat Exchange.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
Mappings
Mappings for Pull(Netskope field – Microsoft Defender for Cloud Apps fields)
Netskope CTE Field
Microsoft Defender for Cloud Apps API Field
Type
status
type
String
page_size
limit
Integer
skip
skip
Integer
Permissions
Microsoft Defender Cloud Apps API token with Read-only access.
API Details
List of APIs Used
API Endpoint
Method
Use case
/api/discovery_block_scripts/
GET
Validate Credentials and Pull indicators
Query Parameters:
Parameter
Type
Description
type
string
banned, sanctioned, protected, allow
limit
integer
Page size (default: 1000)
skip
integer
Pagination offset (default: 0)
Request Headers
Key
Value
Authorization
Token <API Token>
Content-Type
application/json
User-Agent
netskope-ce-5.1.2-cte-microsoft-defender-for-cloud-apps-v1.1.0
Sample Response
{
    "data": [
        {
            "_id": "mock0000abc1",
            "appId": 10000,
            "name": "Microsoft Office 365",
            "domainList": [
                "office.com",
                "outlook.com",
                "teams.com"
            ]
        },
        {
            "_id": "mock0000def2",
            "appId": 10001,
            "name": "Salesforce",
            "domainList": [
                "salesforce.com",
                "app.salesforce.com"
            ]
        }
    ]
}
Performance Matrix
Here is the performance reading conducted for fetching 100K IoCs in each plugin lifecycle on a Large CE instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Microsoft Defender for Cloud Apps
~45k IOCs per minute
User Agent
netskope-ce-6.1.0-cte-microsoft-defender-for-cloud-apps-v1.1.0
Workflow
Get your API URL and API token.
Configure the Microsoft Defender for Cloud Apps plugin.
Configure a Business Rule.
Configure Sharing.
Validate the plugin.
Watch a Video
Click play to watch a video.
Get your API URL from Microsoft Defender
Log in to Microsoft Defender platform and go to
Show navigation > System > Settings > About
.
Copy the API URL as it will be used while configuring the plugin.
Get your API Token from Microsoft Defender
Log in to Microsoft Defender platform and go to
Show navigation > System > Settings > API tokens
.
Click
Add token
, enter a Token name, and click
Generate
.
Copy the generated API token as it will be used while configuring the plugin.
Configuring Microsoft Defender for Cloud Apps Plugin
In Cloud Exchange, and go to
Settings > Plugin Store
.
Search for and select the
Microsoft Defender for Cloud Apps v1.1.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Plugin configuration name.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources.
Indicator Aging Criteria:
Expire indicators after specific time.(. Default: 90)
Override Reputation
: Set a value to override the reputation of indicators received from this configuration. (Default: 5)
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation
: Enable or Disable SSL Certificate validation.
Click
Next
and enter the Configuration Parameters:
URL:
Microsoft Defender Cloud Apps instance URL obtained previously. Example:
https://your-instance.portal.cloudappsecurity.com
.
API Token:
Microsoft Defender Cloud Apps API token with Read-only permissions you generated previously.
Status:
Select the Cloud App status types to pull IoCs from. If no status is selected, IoCs from all Cloud Apps will be pulled.
Enable Tagging:
Enable/Disable tagging functionality. When Yes is selected, status-specific tags will be added to the pulled IoCs.
Add Wildcard Prefix to IoCs:
Add Wildcard Prefix functionality. When Yes is selected, a wildcard character will be prepended to each pulled IoC.
Wildcard:
Wildcard character to prepend to each IoC when Add Wildcard Prefix to IoC(s) is set to
Yes
. A dot (.) is automatically inserted between the wildcard character and the IoC. Note that if the wildcard is kept empty while configuring the plugin, then it will prepend ‘*’ by default to all pulled IoCs ,and while editing the plugin configuring, it will throw a validation error to set the wildcard.
Note
When the Allow status is selected, all indicators associated with apps, except Sanctioned, Unsanctioned, and Protected apps are pulled from the Cloud app catalog page into Cloud Exchange and are assigned with the allow tag.
IoC retraction will be based on Status field. Example: If the plugin was configured with Unsanctioned, Sanctioned, and Protected statuses, and then you edit the plugin and keep only Unsanctioned, Sanctioned statuses, then the IoCs that were pulled from apps with the Protected status will be marked as retracted
yes
in Cloud Exchange.
Click
Save
. Your plugin will be added on the
Threat Exchange > Plugins
page.
Configure a Threat Exchange Business Rule for Microsoft Defender for Cloud Apps
To share indicators fetched from the Microsoft Defender for Cloud Apps to the Netskope Tenant or any 3rd-party platform, you need to have a business rule that filters out the indicators that you want to share.
Go to
Threat Exchange > Business Rules
and
Create New Rule
.
Add the filter according to your requirements in the rule, and then click
Save
.
Configure Threat Exchange Sharing for Microsoft Defender for Cloud Apps
To share IOCs from the Microsoft Defender for Cloud Apps to the Netskope Tenant or any 3rd-party platform, you need to create a Sharing configuration.
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Microsoft Defender for Cloud Apps), Business Rule, Destination Configuration (CTE Netskope Threat Exchange), and Targets.
Click
Save
.
Note
Sharing of IoCs on Defender is not supported for Microsoft Defender for Cloud Apps. To push IoCs from Microsoft Defender for Cloud Apps to Netskope, or to see IoC retraction workflow, refer to the
Netskope plugin guide
. Here is a list of Netskope Threat Exchange actions supported for IoCs pulled from Microsoft Defender for Cloud Apps:
Add to a URL List
Add to Private App
Add to Destination Profile
Add to DNS Profile
We have observed that the IoCs with the ‘*’ Wildcard prepended cannot be shared to the Destination Profile.
Validation
Validate the Pull
To verify the data available for pulling on Microsoft Defender for Cloud Apps. Log in to Microsoft Defender platform and navigate to
Show navigation > Cloud apps > Cloud app catalog
.
Open any of the applications, and then you will be able to see the
Domain
field. Those are the IoCs that will be pulled in Cloud Exchange.
Pulled data will be listed on the Threat IoCs page in Cloud Exchange. You can filter the IOCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
Here are some sample IoCs pulled with the Add Wildcard Prefix to IoCs as
Yes
:
Here are some sample IoCs pulled with the Add Wildcard Prefix to IoCs as
No
:
To verify pulled logs on Cloud Exchange, go to
Logging
and search logs from the CTE Microsoft Defender for Cloud Apps plugin using the plugin configuration name.
Validate the Pull Retraction
You can filter the logs related to retraction by using the filter:
sources.source Like “[Retraction]”
You can validate the retracted IoCs on the
Threat IoCs
page:
When IoCs pulled from Microsoft Defender for Cloud Apps are marked as retracted
yes
, then it will be marked as
<plugin-config-name>: retracted
in the Retraction Result if that IoC was already shared to Netskope tenant, or third Party platform and that destination plugin supports push retraction.
Sharing result will be only populated when the IoCs are pulled after creating the Sharing Configuration, that means Sharing result will not be populated for the IoCs that were already pulled before creating the Sharing Configuration.
Validate the Push Retraction
Push Retraction is not supported for Microsoft Defender for Cloud Apps. To push IoCs from Microsoft Defender for Cloud Apps to Netskope, or to see IoC retraction workflow, refer to the
Netskope plugin guide
.
IoCs pulled from Microsoft Defender for Cloud Apps were shared to the Destination Profile
CTE Demo
on the Netskope Tenant.
If any of the shared IoCs are marked as retracted in Cloud Exchange, it would be deleted from the Netskope tenant as well, and then retraction result will be marked as
CTE Netskope Threat Exchange: retracted
.
Here you can see the IoCs that were marked Retracted
Yes
in the retraction screenshot, and were also deleted from the Destination Profile on the Netskope tenant.
Troubleshooting the Microsoft Defender for Cloud Apps plugin
Unable to configure the Microsoft Defender for Cloud Apps plugin
It might be due to invalid credentials for Microsoft Defender for Cloud Apps.
What to do:
Follow the steps in
Configuration on the Microsoft Defender Platform
.
Unable to pull IoCs from the Microsoft Defender for Cloud Apps platform
After the plugin configuration if the IoCs are not pulled from the platform, it might be due to there being no IoCs available on the platform to pull.
What to do:
Identity your root cause from above and check if the IoCs are
available on the platform
to pull.
Known Behaviors
We have observed that the IoCs with the ‘*’ Wildcard prepended cannot be shared to the Destination Profile.
If the same IoC is present under multiple applications having different status, then that IoC will not be marked as retracted in Cloud Exchange.
In this Topic
Microsoft Defender for Cloud Apps Plugin for Threat Exchange

---
## Microsoft Office 365 Endpoints Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/microsoft-office-365-endpoints-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:46:26+00:00
**Scraped:** 2026-08-11T07:17:46.997775+00:00

Microsoft Office 365 Endpoints Plugin for Threat Exchange - Netskope Technical Documentation
Microsoft Office 365 Endpoints Plugin for Threat Exchange
This document provides instructions to configure the Microsoft Office 365 Endpoints integration with the Threat Exchange module of the Netskope Cloud Exchange platform. Use this plugin to fetch URLs from Microsoft Office 365 Endpoints. This plugin does not support sharing of indicators to Microsoft Office 365 Endpoints.
Microsoft provides dynamic information regarding Office 365, specifically what URLs and IPs each O365 service is under.
This information is updated periodically.
Adding this information in Cloud Exchange and the Netskope tenant provides automatic synchronization of the information into web categories.
These categories can be used in SSL decryption policies, Real-time Protection policies, and SAML authentication bypass.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Microsoft Office 365 Endpoints Plugin Support
Fetched indicator types
URL
Workflow
Configure the Microsoft Office 365 Endpoints plugin.
Configure sharing for the Microsoft Office 365 Endpoints plugin.
Click play to watch a video.
Configure the Microsoft Office 365 Endpoints Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
Microsoft Office365 Endpoints
plugin box to open the plugin creation page.
Enter a Configuration Name
Adjust the Sync Interval to the appropriate value: Suggested is 5+ minutes.
Enter Aging Criteria.
Adjust the Override Reputation to the appropriate value.
Click
Next
.
Select an Instance. Supported values are, Worldwide, China, Germany, USGovDoD, and USGovGCCHigh.
Select the Service Area Display Name. Supported values are, Exchange Online, Microsoft 365 Common and Office Online, Skype for Business Online and Microsoft Teams, SharePoint Online and OneDrive for Business. Keep this field empty to fetch URLs from all the Service Areas.
Click
Save
.
Configure Sharing for Netskope and Microsoft Office 365 Endpoints
In Threat Exchange, go to
Sharing
.
Click “
Add Sharing Configuration
.
For Source Configuration, select Microsoft Office 365 Endpoints plugin name you created previously.
Select the appropriate Business Rule from the second dropdown.
For Destination Configuration, choose Netskope.
Select Add to URL List in the Target dropdown.
Select the List Name, or select
Create new list
from the dropdown, and then enter a new List Name.
Select
Add to URL List
.
Enter a List Size.
Enter the Default URL.
Click
Save
.
In this Topic
Microsoft Office 365 Endpoints Plugin for Threat Exchange

---
## Mimecast Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/mimecast-plugin-for-threat-exchange/
**Last Modified:** 2026-03-25T00:02:28+00:00
**Scraped:** 2026-08-11T07:17:49.602093+00:00

Mimecast Plugin for Threat Exchange - Netskope Technical Documentation
Mimecast Plugin for Threat Exchange
This document explains how to configure the Mimecast v2.0.1 plugin with the Threat Exchange module in the Netskope Cloud Exchange platform. This plugin is used to fetch the indicators of type URL from the
Email Security > URL Protection > Logs
page, SHA256 and MD5 from the Mimecast platform.
This plugin also supports sharing the URL indicators to the
Email Security > URL Protection > URL Tools > Managed URLS
page using the Create Managed URL action, and sharing of SHA256 and MD5 indicators using the Perform Operation action to the Mimecast.
To access the plugin, you would need an API application on Mimecast and user credentials. Refer these Mimecast guides
here
for detailed steps.
Prerequisites
To complete this configuration, you need:
Netskope Tenant (or multiple, for example, production and development/test instances)
A
URL List
on your Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Mimecast platform credentials.
Mimecast administrator console with URL Protection service.
Access to create a Custom Admin Role.
Access create Custom API 2.0 Integration.
Subscription to Bring Your Threat Intelligence (BYOTI) package for file hash.
Connectivity to the following hosts:
https://login.mimecast.com/u/login/?gta=administration#/login
Mimecast Plugin Support
This plugin is used to fetch the indicators of type URL from the
Email Security > URL Protection > Logs
page, SHA256 and MD5 from the Mimecast platform. This plugin also supports sharing the URL indicators to the
Email Security > URL Protection > URL Tools > Managed URLS
page using the Create Managed URL action, and sharing of SHA256 and MD5 indicators using the Perform Operation action. To access the plugin, you would need an API application on Mimecast and user credentials. Refer to these Mimecast
guides
for detailed steps.
Fetched Indicator Types
Shared Indicator Types
URL, MD5, SHA256
URL, MD5, SHA256
IoC Retraction
IoC Retraction (Pull): Indicators fetched from Mimecast and that are not within the retraction interval range will be marked as Retracted = Yes in Cloud Exchange.
IoC Retraction (Push): Indicators fetched from Source Plugin and that were already shared to Mimecast will be deleted from Mimecast once they are marked Retracted in Cloud Exchange.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes (URLs, SHA256 and MD5)
IoC Retraction (Push)
Yes (URLs)
Note
For retraction to work, it is mandatory to enable the
IoC(s) Retraction
toggle under
Settings > Threat Exchange
.
Mappings
Mappings for Pull (Netskope Fields – Mimecast Fields)
Cloud Exchange Fields
Mimecast Fields
value
value
type
type
Comment
Sent from
<SenderAddress>
Mappings for Push (Hashes)
Cloud Exchange Fields
Mimecast Fields
value
value
type
type
provider
NetskopeCE
description
comments (max length is 20 characters)
operation_type
BLOCK/ALLOW/DELETE
Mappings for Push (URLs)
Cloud Exchange Fields
Mimecast Fields
value
value
action
BLOCK/DELETE
Permissions
Administration Console access
Access to create a Custom Admin Role with following permissions:
Account | Dashboard | Read
Monitoring | URL Protection | Read
Services | URL Protection | Edit (Read and Write)
Gateway | Tracking | Read
BYO Threat Intelligence | Upload
Subscription to Bring Your Threat Intelligence (BYOTI) package for file hash sharing.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/oauth/token
POST
Validate Credentials
/api/account/get-account
POST
Fetch account details endpoint
/api/ttp/threat-intel/get-feed
POST
Fetch Hashes endpoint
/api/ttp/url/get-logs
POST
Fetch URLs endpoint
/api/byo-threat-intelligence/create-batch
POST
Push Hashes (MD5 and SHA256)
/api/ttp/url/decode-url
POST
Decode URLs
/api/ttp/url/create-managed-url
POST
Push URLs
/api/ttp/url/get-all-managed-urls
POST
Get all URLs
/api/ttp/url/delete-managed-url
POST
Delete URLs
Get Bearer Token
API Endpoint:
https://api.services.mimecast.com/oauth/token
Method:
POST
Request Headers
Key
Value
client_id
Mimecast Client ID
client_secret
Mimecast Client Secret
grant_type
client_credentials
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Sample API Response
{
    "access_token": "V9RteK0pwTxPscMCCd6xs20f05Ob",
    "token_type": "Bearer",
    "expires_in": 1799,
    "scope": ""
}
Validate Credentials
API Endpoint:
https://api.services.mimecast.com/api/account/get-account
Method:
POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Sample API Response
{
    "meta": {
        "status": 200
    },
    "data": [
        {
            "region": "us",
            "archive": false,
            "gateway": true,
            "passphrase": "",
            "supportCode": "5656",
            "maxRetention": 30,
            "maxRetentionConfirmed": true,
            "minRetentionEnabled": false,
            "automatedSegmentPurge": true,
            "type": "full",
            "policyInheritance": false,
            "databaseCode": "test",
            "searchReason": false,
            "contentAdministratorDefaultView": "",
            "adminSessionTimeout": 720,
            "exportApi": false,
            "exgestAllowQuery": false,
            "exgestAllowExtraction": true,
            "expressAccount": false,
            "cybergraphV2Enabled": true,
            "accountCode": "",
            "accountName": "",
            "adminEmail": "",
            "contactEmail": "testuser@gmail.com",
            "domain": "",
            "userCount": 10,
            "umbrellaAccounts": [
                "CU2A110,CUSA131A2,CUSA133A2,CUSA42A10,CUS"
            ],
            "mimecastId": "01-1234-123",
            "contactName": "test user",
            "telephone": "123-123-123",
            "packages": [
                "Auto Responders (Site) [1005]",
                "Impersonation Protection [1060]",
            ]
        }
    ],
    "fail": []
}
Fetch Hashes (Md5 and Sha256)
API Endpoint:
https://api.services.mimecast.com/api/ttp/threat-intel/get-feed
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "data": [
        {
            "fileType": "csv",
            "feedType": "malware_grid"
        }
    ]
}
Sample API Response:
key|FileMimeType|FileName|FileSize|MD5|Observations|RecipientAddress|Route|SHA1|SHA256|SenderAddress|SenderDomain|SendingIP|Timestamp
0|||||1||Out||d693862cb6d4d22647921963dfe4be863fc8568b2676c4353663455dd585c426|null|null|209.221.13.136|2025-02-09T17:30:00.342Z
1|||||1||Out||7236787ed35fd54966f7d345b0698bc7a52bdc165d79c58a54fe05ca5be28c94|null|null|209.221.13.136|2025-02-09T17:30:01.364Z
2|||||1||Out||42de9806857b28c1fc8ac95cb0f16a146f62645f2468eae82e0ea62f0af4a057|null|null|70.165.34.181|2025-02-09T17:30:13.946Z
3|||||1||Out||e8960a547ad4f7f14331468f126375e2f100c7bdeb27cedec4bb3b9175e1727d|null|null|205.144.127.200|2025-02-09T17:30:20.958Z
4|||||1||Out||5e5aa18e4182f8f5544a2e742209297b77e56b7fb2b262b1ce3cafe6ecc7acc7|null|null|209.221.13.136|2025-02-09T17:30:31.256Z
Fetch URLs
API Endpoint:
https://api.services.mimecast.com/api/ttp/url/get-logs
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "meta": {
        "pagination": {
            "pageSize": 1,
            "pageToken": ""
        }
    },
    "data": [
        {
            "from": "2024-02-03T10:16:31+00:00",
            "scanResult": "malicious",
            "oldestFirst": true
        }
    ]
}
Sample API Response
{
    "meta": {
        "pagination": {
            "pageSize": 1,
            "totalCount": 17,
            "next": "eNqNkk9vgkAQxb_Lnj2wUExj4sFQwTWAVSx_9ga7qIssEHYRoel379aemtSEwxzmZWZ-L5n3CZr0nAs25oyCBZyBps1vrO7Eu5LB4pSWIp8ByeXPmKyveQUWIB-2dWb42lHHnOihRgY0VxokxqEkXDPd46rfBSYkgynTCJaJbo_UMkUSvbBdsRaoWPfuo7zBLYiJirp3rb_7Hnu2vxKoCkfqhEN2vErvbQVd1bscNlkUFknsay6_XzKG5p7VM6p6HG_lLtB6783raOx1WVRKHPkXYuy7zLG7f_h3z5rM16fzz1P5vT-db0znr5_yT0HPiGNX-EN52Bxqpd2Vpz6JaHnkr79_q_wbqQ4jKppM_ZunUSiwheaI-yKN_DZ01N0ACcTtMdHDDjtlh1U26GYLcQzpab9cghm45a1gdfWIW5uTuqVCpq18BPDrG9034fE"
        },
        "status": 200
    },
    "data": [
        {
            "clickLogs": [
                {
                    "userEmailAddress": "benjamin.rogers@demo-int.netskope-1.mime-api.com",
                    "fromUserEmailAddress": "sheila.tweed@demo-int.netskope-1.mime-api.com",
                    "url": "http://www.mccutchen.com",
                    "ttpDefinition": "Default Internal URL Protect Definition",
                    "subject": "Final Oxy Certificate----For the \"Data Room\"",
                    "action": "warn",
                    "adminOverride": "N/A",
                    "userOverride": "None",
                    "scanResult": "malicious",
                    "category": "Phishing & Fraud",
                    "sendingIp": "Internal IP",
                    "userAwarenessAction": "N/A",
                    "date": "2025-01-20T16:29:55+0000",
                    "actions": "None",
                    "route": "internal",
                    "creationMethod": "Entry Scan",
                    "emailPartsDescription": [
                        "Body"
                    ],
                    "messageId": "<3b899e671d27739b-274723@hapi.b41.one>",
                    "tagMap": {
                        "UrlReputationScan": {
                            "Status": [
                                "CustomerAll",
                                "VerdictBlock"
                            ],
                            "Type": [
                                "Malware, Phishing & Fraud"
                            ],
                            "UrlBlock": [
                                "ORIGINAL:http://www.mccutchen.com -> META_REDIRECT:http://www70.mccutchen.com (Blocked as MALWARE,PHISHING)",
                                "ORIGINAL:http://www.mccutchen.com -> META_REDIRECT:http://www70.mccutchen.com -> EXTRACTED:http://www70.mccutchen.com (Blocked as MALWARE,PHISHING)"
                            ],
                            "Url": [
                                "http://www70.mccutchen.com"
                            ]
                        }
                    }
                }
            ]
        }
    ],
    "fail": []
}
Decode URLs
API Endpoint:
https://api.services.mimecast.com/api/ttp/url/decode-url
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "data": [
        {"url": "www.katzlaw.com"},
        {"url": "http://exlorer.msn.com/intl.asp"}
    ]
}
Sample API Response
{
    "meta": {
        "status": 200
    },
    "data": [
        {
            "url": "www.katzlaw.com",
            "success": true
        },
        {
            "url": "http://exlorer.msn.com/intl.asp",
            "success": true
        }
    ],
    "fail": []
}
Push Hashes
API Endpoint:
https://api.services.mimecast.com/api/byo-threat-intelligence/create-batch
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "data": [
        {
            "hashList": [
                {
                    "hash": "9e953050c61f6fedf4305f65a81224a1145ccf7dff2acf2963c40ee7468cd9d1",
                    "provider": "NetskopeCE",
                    "description": "Test API"
                }
            ],
            "operationType": "DELETE"
        }
    ]
}
Sample API Response
{
    "meta": {
        "status": 200
    },
    "data": [
        {
            "batchIdToken": "eNoNjkkOgjAAAP_SqyaCVEtNPDTEAC5ERAgQL9A2KZVFNhGMf5frzGHmC1pO-4ZnDOxAMcBxjDz5hDB0IEFCCbpLYIa4D-i6Ju3pU3AopfOaSoGPhnqLnQNjiWOGj1Xd-Tqxkhzp0q3DPFrA3L0PzRgTNZrSsxZJoRjZ1bU1mRHL9fdgCWjfdlXBG1oxPucN3yM6JhrazC5NOirs-UpVtwjDJXjzps2qcga_P2ieOls",
            "status": "NOT_STARTED",
            "operationType": "DELETE",
            "hashCount": 2,
            "createTime": "2025-02-17T06:56:23.211Z[UTC]"
        }
    ],
    "fail": []
}
Push URLs
API Endpoint:
https://api.services.mimecast.com/api/ttp/url/create-managed-url
Method:
POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "data": [
        {
            "url": "http://example3.com",
            "action": "permit",
            "comment": "Netskope CE",
            "matchType": "explicit"
        }
    ]
}
Sample API Response
{
{
    "meta": {
        "status": 200
    },
    "data": [
        {
            "id": "wOi3MCwjYFYhZfkYlp2RMKIAOwgBXweUUcu0eTwirzBO48Dj4FQ1bYgyujdIycvnuKUxo9kpfZR5qr5gR1Wv_KCXbJQmclXmiZ8N_Fx_3R1RaxOE0x9IT9PFiD1mEL4W",
            "scheme": "http",
            "domain": "example3.com",
            "port": -1,
            "path": "",
            "queryString": "",
            "matchType": "explicit",
            "action": "permit",
            "comment": "Netskope CE",
            "disableUserAwareness": false,
            "disableRewrite": false,
            "disableLogClick": false
        }
    ],
    "fail": []
}
Get Managed URLs
API Endpoint:
https://api.services.mimecast.com/api/ttp/url/get-all-managed-urls
Method:
POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "data": [
        {
            "domainOrUrl": "http://example3.com",
            "exactMatch": true
        }
    ]
}
Sample API Response
{
    "meta": {
        "pagination": {
            "pageSize": 1,
            "totalCount": 1
        },
        "status": 200
    },
    "data": [
        {
            "id": "wOi3MCwjYFYhZfkYlp2RMKIAOwgBXweUUcu0eTwirzBO48Dj4FQ1bYgyujdIycvnuKUxo9kpfZR5qr5gR1Wv_KCXbJQmclXmiZ8N_Fx_3R1RaxOE0x9IT9PFiD1mEL4W",
            "scheme": "http",
            "domain": "example3.com",
            "port": -1,
            "path": "",
            "queryString": "",
            "matchType": "explicit",
            "action": "permit",
            "comment": "Netskope CE",
            "disableUserAwareness": false,
            "disableRewrite": false,
            "disableLogClick": false
        }
    ],
    "fail": []
}
Delete Managed URLs
API Endpoint:
https://api.services.mimecast.com/api/ttp/url/delete-managed-url
Method:
POST
Request Headers
Key
Value
Authorization
Bearer
<Bearer Token>
User-Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Accept
application/json
Request Body
{
    "data": [
        {
            "id": "wOi3MCwjYFYhZfkYlp2RMKIAOwgBXweUUcu0eTwirzBO48Dj4FQ1bYgyujdIycvnonkzMQDptATGOwyPSUGB5daY0iCYXSXKVRGrZu_YX6VRaxOE0x9IT9PFiD1mEL4W"
        }
    ]
}
Sample API Response
{
"meta": {
"status": 200
},
"data": [],
"fail": []
}
Performance Matrix
Here is the performance reading conducted for fetching and pushing 100K IoCs in each plugin lifecycle on a Large Cloud Exchange instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Mimecast
~37K per minute
Indicators shared to Mimecast (SHA256 and MD5)
~1.6K per minute
Indicators shared to Mimecast (URLs)
~700 IOCs per minute
Note
For URL sharing, readings are taken after sharing 30k URLs to Mimecast.
User Agent
netskope-ce-6.0.1-cte-mimecast-v2.0.1
Workflow
Get your Mimecast credentials.
Configure the Mimecast Plugin.
Configure a business rule for Mimecast.
Configure sharing for Netskope and Mimecast.
Validate the Mimecast Plugin.
Watch a Video
Click play to watch a video.
Get your Mimecast Credentials
Log in to your Mimecast instance.
Make note of the region in Mimecast Instance Base URL, in the form of
https://login-
<region>
.mimecast.com/
. You will need this when configuring the Mimecast Plugin in Threat Exchange.
Create a Custom Admin Role
Go to
Account
>
Admin Roles
.
Click
New Role
.
In the
Properties
section, enter these parameters:
Role Name:
Enter a name.
Description:
Briefly describe the role’s purpose.
In the
Application Permissions
section, enable the following permissions:
Account | Dashboard | Read
Monitoring | URL Protection | Read
Services | URL Protection | Edit
Gateway | Tracking | Read
BYO Threat Intelligence | Upload
Click
Save and Exit
.
Generate API 2.0 Keys
Go to
Integrations > Integrations Hub
.
Find the
Mimecast API 2.0
tile and click
Configure New
.
Enter the Application Details:
Application Name:
Enter a unique name for this integration.
Products:
You have to select only five products.
Account Management
Email Security Cloud Gateway
Security Events
Threat Management
Policy Management
Application Role:
Select the same role which you have created in the above
steps
.
Enter a
Technical Point of Contact
and
email
.
Click
Save
and a popup will display your Client ID and Client Secret. Copy them; there are needed to configure the plugin.
Note
For further information, go to the official Mimecast site
https://developer.services.mimecast.com/apis
.
Configure the Mimecast Plugin in Cloud Exchange
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Mimecast v2.0.1 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Leave the default.
Aging Criteria
: Expiry time of the plugin in days. (Default: 90)
Override Reputation
: Set a value to override the reputation of indicators received from this configuration. (Default: 5)
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Use System Proxy
: Enable if the proxy is required for communication.
Click
Next
and enter the Configuration Parameters:
API Base URL:
Mimecast API Base URL including region.
Client ID:
Mimecast API Client ID.
Client Secret:
Mimecast API Client Secret.
Indicator Feed Type:
The scope of data to fetch. Use
Malware Customer
to pull data from the account. Use
Malware Grid
to pull the data form the region grid. Use
Malsite
to pull URLs from URL Protection.
Types of Malware to Pull
(applicable when
feed_type
is
Malware Customer
or
Malware Grid
):
The scope of data to fetch. Use
Malware Customer
to pull data from the account. Use
Malware Grid
to pull the data form the region grid. Use
Malsite
to pull URLs from URL Protection.
Retraction Interval (in days):
Specify the number of days for which IoC retraction should be run for Mimecast indicators. Note that this parameter is applicable only for Netskope CE version 5.1.0 or later, and if IoC(s) Retraction is enabled in your Threat Exchange Settings.
Initial Range (in days):
Number of days to pull the data for the initial run.
Click
Save
.
Create a Threat Exchange Business Rule for Mimecast
To share indicators fetched from the Mimecast to Cloud Exchange, and vice-versa, you will need to have a business rule that will filter out the indicators that you want to share.
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirement in the rule, and then click
Save
.
Configure Sharing for Netskope and Mimecast
To share IoCs from Cloud Exchange to the Mimecast platform, or vice-versa:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Netskope CTE), Business Rule, Destination Configuration (Mimecast), and Target.
Select the existing IoC List Name, or create a new IoC list on the platform. The Mimecast plugin supports 2 types of actions under Target.
Create Managed URL (applicable for sharing URLs to Mimecast)
Supported Action types:
BLOCK
PERMIT
Supported Match types:
Explicit
Domain
Perform Operation (applicable for sharing File hashes (SHA256, MD5) to Mimecast)
Supported Operations:
ALLOW
BLOCK
DELETE
Click
Save
.
Click
Add Sharing Configuration
, and follow the same steps, but vice-versa for sharing Mimecast IoCs to Netskope. Select your Source Configuration (Mimecast), Business Rule, Destination Configuration (Netskope CTE), and Target.
Click
Save
.
Validate the Mimecast Plugin
In order to validate the workflow, you must have Netskope Alerts and/or Mimecast attributes/indicators. Polling Intervals were defined during plugin configuration.
Validate the Pull
Pulled data will be listed on
Threat IoCs
. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin name>”
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE Mimecast plugin.
To verify the data available for pulling on Mimecast, l
og in to Mimecast Platform and go to
Email Security > URL Protection > Logs
.
Note that Mimecast plugin only pulls Malicious URLs.
Note that the location from where hashes are pulled and pushed is not certain. According to the doc (
here
) it must be in the Mimecast Threat Dashboard. If you can’t find this, contact your Mimecast admin.
Validate the Push
To validate the push in Cloud Exchange, go to
Logging
and filter shared logs for the Mimecast plugin.
Go to
Threat IoCs
and filter logs shared with the Mimecast plugin.
On the Mimecast platform, go to
Email Security > URL Protection > Managed URL
to check the shared IoCs
of type URL
on the platform.
To filter the IoCs shared from Cloud Exchange, you can use a Domain or comment filter with the string
Netskope CE
.
Validate the Retraction
You can filter the logs related to retraction by using the filter:
sources.source Like “<plugin configuration name> [Retraction]”
.
You can validate the same at
Threat IoCs
:
When the IoCs shared from a Netskope Threat Exchange plugin, or 3rd-party plugin, to Mimecast, it will be retracted in Cloud Exchange and marked as
“<plugin-config-name>: retracted”
in the Retraction Result after they are deleted from the Mimecast Platform. If they are not deleted from the destination platform, then the Retraction Result will be pending.
Here you can see an IoC that was pulled from Netskope Tenant and shared to the Mimecast platform, and it is marked as Retracted = Yes in Cloud Exchange. Initially, its retraction result will be pending, meaning it is not yet deleted from the Mimecast platform. After it is deleted from the Mimecast platform, then its retraction result will be marked as retracted in Cloud Exchange as you can see in the screenshot. This means it was deleted from the Mimecast platform.
The same can be verified in the logs at
Logging
in Cloud Exchange.
URL List on Netskope where three IoCs pulled from Mimecast where already shared:
When the IoCs shared from Mimecast to a 3rd-party will be retracted in Cloud Exchange, it will be marked as
“<plugin-config-name>: retracted”
in the Retraction Result, which means they are deleted from the destination platform. If they are not deleted from the destination platform, then the Retraction Result will be pending.
URL List on Netskope Tenant after one of the URL was deleted as it was marked as retracted on Cloud Exchange:
Troubleshooting the Mimecast Plugin
Unable to configure the Mimecast plugin
If the plugin configuration fails, it may be due to one of these reasons:
Invalid Client ID and Client Secret
Incorrect permissions
What to do
: Refer the
Get your Mimecast Credentials
and
Permissions
sections to generate valid Client ID and Client Secret.
Unable to pull IoCs from the Mimecast platform
After the plugin configuration if the IoCs are not pulled from the platform it might be due to one of the following.
No IoCs are available on the platform to pull
IoCs are not available for the given time range or does not match the configuration parameters.
What to do:
Identity your root cause from above and follow below steps to resolve the issue.
No IoCs are available on the platform to pull
Check if the IoCs are
available on the platform
to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Mimecast platform, check if you have data for the given time range.
If the data is still available for the given time range it might be possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter and filter the same on the Anomali platform.
Unable to push the IoCs to Mimecast
If you are not able to push the IoCs on the platform it may be due to the following reasons:
insufficient permissions
maximum limit of the Mimecast instance is reached
What to do:
Make sure your tenant have the subscription to Bring Your Threat Intelligence (BYOTI) package for file hash.
Make sure Client ID and Client Secrets have proper permissions. Refer
Get your Mimecast Credentials
.
Quota for sharing file hash can be found from this endpoint “
/api/byo-threat-intelligence/get-quota
”
Quota for sharing URLs is not known, contact your Mimecast support team for it. Refer
Limitations
section.
Known Behaviors
The location from where hashes are pulled and pushed is not certain. According to the doc (
here
), it must be in the Mimecast Threat Dashboard. If you don’t find this, contact your Mimecast admin.
While upgrading the plugin if you use the Skip button, then the API Base URL, Client ID and Client Secret will be kept empty. Also the plugin configuration will be disabled. To enable that plugin configuration you need to manually edit the plugin configuration, and add the values for API Base URL, Client ID, and Client Secret.
Rate Limit issue: ​​The Mimecast documentation does not specify rate limits, such as the number of requests allowed per second or minute. Despite retrying 60 seconds after receiving a 429 status code, the rate limit is exceeded again after just two to three API requests. Without clear information on API limits, not able to handle this. This could potentially lead to an infinite loop, causing the pulling task to fail after some time. It has been observed that the rate limit is only exceeded for the pull hash API frequently, and not for the pull URL API. This may affect pulling and retraction workflow for hashes
Limitations
The plugin pull and push for MD5 and SHA256 has been verified with the API responses only as we are not able to see the Hashes on the platform.(Although Threat Dashboard is enabled). The quota for pushing hashes was unavailable, so hash sharing could not be tested.
On our Mimecast instance, we have observed that Mimecast does not allow sharing URLs more than 30k. For sharing URLs beyond 30k, Mimecast APIs return 200 status code. Also, the Mimecast official documentation does not have any maximum limit for sharing URLs to the endpoint
/api/ttp/url/create-managed-url
.
{
"meta": {
"status": 200
},
"data": [],
"fail": [
{
"key": {
"url": "http://test.yahoo.com/",
"matchType": "explicit",
"action": "block",
"comment": "Netskope CE",
"overrideUrl": false,
"disableUserAwareness": false,
"disableRewrite": false,
"disableLogClick": false
},
"errors": [
{
"code": "err_managed_url_create_failure",
"message": "Managed URL create failure",
"retryable": false
}
]
}
]
}
Due to this CTE Mimecast plugin will keep sharing URLs if user tries to share beyond the maximum limit, and users might observe logs similar to below log.
CTE Mimecast [CTE Mimecast push hash perf]: Successfully shared 0 URLs for batch 5000. Total URLs shared: 16.
In this Topic
Mimecast Plugin for Threat Exchange

---
## MISP Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/misp-plugin-for-threat-exchange/
**Last Modified:** 2026-05-28T03:37:34+00:00
**Scraped:** 2026-08-11T07:17:52.107002+00:00

MISP Plugin for Threat Exchange - Netskope Technical Documentation
MISP Plugin for Threat Exchange
This document explains how to configure the MISP v1.5.1 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows for sharing of URLs and file hashes with Netskope that have been identified by MISP or Netskope.
MISP is a threat intelligence platform for sharing, storing and correlating Indicators of Compromise of targeted attacks, threat intelligence, financial fraud information, vulnerability information or even counter-terrorism information. (
Learn more
)
This plugin is used to fetch event attributes from MISP (Malware Information Sharing Platform) and extract indicators of type SHA256, MD5, URL, Domain, IP (IPv4 and IPv6) and Hostname from them. It can also share the indicators of type SHA256, MD5, URL, Domain (Domain, FQDN, and Hostname), and IP (IPv4 and IPv6) as attributes to MISP Custom Events. To get required details for creating a new configuration, go to
https://<misp-url>/events/automation
.
Factor that the Source IP (ip-src) and Destination IP (
ip-dst
) will be stored as either IPv4 or IPv6 in Cloud Exchange. Source IP|Port (
ip-src|port
), Destination IP|Port (
ip-dst|port
), and Hostname|Port (hostname|port) will be stored as URLs in Cloud Exchange. For Domain|IP, the domain and IP (either IPv4 or IPv6) will be split and stored as separate IoCs in Cloud Exchange.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing and a
URL List
.
A Netskope Threat Prevention subscription for malicious file hash sharing and a
File Profile
.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A MISP Instance.
Connectivity to the following host: the MISP platform (
https://<misp-URL>
).
MISP Plugin Support
This plugin is used to fetch event attributes from MISP and extract indicators from them. This plugin supports pulling and pushing of IoCs.
Fetched Indicator Types
Shared Indicator Types
MD5
SHA256
URL (Source IP|Port [ip-src|port], Destination IP|Port [ip-dst|port] and Hostname|Port [hostname|port])
Domain,
IPv4 and IPv6(Source IP [ip-src] and Destination IP [ip-dst])
Domain (Domain|IP)
Hostname
MD5
SHA256
URL
Domain (Domain, FQDN and Hostname)
IP (IPv4 and IPv6)
Mappings
Pull Mapping
Cloud Exchange Fields
MISP API Response Fields
value
value
type
type:
md5, sha256, url, domain, ip-src, ip-dst, ip-src|port, ip-dst|port, hostname|port, domain|ip
first_seen
first_seen
last_seen
last_seen
Comment
Comment | Decaying Score:
<DecayingModel.score>
, Decaying Model ID:
<DecayingModel.id>
, Decaying Model Name:
<DecayingModel.name>
tags
Tag + MISPCATEGORY-
<category>
extendedInformation
<Base URL>
//events/view/
<event_id>
Note
The Source IP (ip-src) and Destination IP (ip-dst) will be stored as either IPv4 or IPv6 in Cloud Exchange. Source IP|Port (ip-src|port), Destination IP|Port (ip-dst|port), and Hostname|Port (hostname|port) will be stored as URLs in Cloud Exchange. For Domain|IP, the domain and IP (either IPv4 or IPv6) will be split and stored as separate IoCs in Cloud Exchange.
Push Mapping
Cloud Exchange Fields
MISP API Response Fields
value
value
type
type: md5, sha256, ip-src, url, domain, hostname
Note that the Domain, FQDN, Hostname in CE will be shared as domain to MISP Platform.
comment
comment
first_seen
firstSeen
last_seen
lastSeen
Tag
netskope-ce
Netskope CE |
<Source Plugin Name>
Permissions
Admin permissions is required to generate an Authentication Key.
API Details
List of APIs used
API Endpoint
Method
Use Case
/events/restSearch
POST
Check event existence
/attributes/restSearch
POST
Pull attributes
/tags/search/
<Tag name>
POST
Check tag existence
/tags/add
POST
Create tag
/events/edit/
<Event ID>
POST
Share indicators to existing event
/events/add
POST
Share indicators to new event
Check Event Existence
API Endpoint:
/events/restSearch
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Authorization
API Key
Accept
application/json
Content-Type
application/json
Parameters
Key
Value
returnFormat
json
limit
1
page
1
eventinfo
<Event Name>
metadata
true
Sample API Response
{
"response": [
{
"Event": {
"id": "1517",
"orgc_id": "1",
"org_id": "1",
"date": "2024-06-25",
"threat_level_id": "4",
"info": "new",
"published": false,
"uuid": "09502561-a07f-41e9-8359-59394878e47d",
"attribute_count": "11",
"analysis": "0",
"timestamp": "1719493608",
"distribution": "1",
"proposal_email_lock": false,
"locked": false,
"publish_timestamp": "0",
"sharing_group_id": "0",
"disable_correlation": false,
"extends_uuid": "",
"protected": null,
"event_creator_email": "admin@admin.test",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18",
"local": true
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18",
"local": true
},
"RelatedEvent": [
{
"Event": {
"id": "1325",
"date": "2024-07-05",
"threat_level_id": "4",
"info": "new5",
"published": false,
"uuid": "3508388f-b6a6-4be2-9b99-de05825cc304",
"analysis": "0",
"timestamp": "1720177270",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1324",
"date": "2024-07-02",
"threat_level_id": "4",
"info": "new4",
"published": false,
"uuid": "e8d24ff9-2955-4eb6-80f1-5f276fae2e42",
"analysis": "0",
"timestamp": "1720424260",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1319",
"date": "2024-06-27",
"threat_level_id": "4",
"info": "420test",
"published": false,
"uuid": "1e1f4455-8d0e-43dd-95ba-0fd4f7eb6abf",
"analysis": "0",
"timestamp": "1720418522",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1315",
"date": "2024-03-12",
"threat_level_id": "4",
"info": "test",
"published": false,
"uuid": "dceaa84e-156f-4a31-b0b2-a3ae0778d72a",
"analysis": "0",
"timestamp": "1720175425",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1308",
"date": "2015-01-01",
"threat_level_id": "1",
"info": "testevent",
"published": false,
"uuid": "0c3d5017-8edf-483b-a829-426bb2c56c92",
"analysis": "0",
"timestamp": "1699523309",
"distribution": "0",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
}
],
"Galaxy": [],
"CryptographicKey": [],
"Tag": [
{
"id": "251",
"name": "workflow:todo=\"create-missing-misp-galaxy-cluster\"",
"colour": "#770040",
"exportable": true,
"user_id": "0",
"hide_tag": false,
"numerical_value": null,
"is_galaxy": false,
"is_custom_galaxy": false,
"local_only": false,
"local": 0,
"relationship_type": null
}
]
}
}
]
}
Pull Attributes
API Endpoint:
/attributes/restSearch
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Authorization
API Key
Accept
application/json
Content-Type
application/json
Parameters
Key
Value
Comment
returnFormat
json
The format to return data in. e.g. json, csv, etc.
limit
1
Maximum records to return
page
1
Page number
eventid
< Event ID>
Event ID
timestamp
[
<Start Time>
,
<End Time>
]
Restrict the results by the timestamp (last edit)
category
[
<Categories Name>
]
Categories of attributes to pull.
type
[“md5″,”sha256″,”ip-src”,”domain”,”ip-src|port”, “ip-dst”,”ip-dst|port”,”domain|ip”,”hostname”,”hostname|port”]
Type of indicators to pull
tags
[“!netskope-ce”]
Include or exclude attributes with certain tags.
includeDecayScore
1
If set to 1, decay score information will be included for attributes that are affected by decaying.
decayingModel
[1,2]
Allows you to set the decaying model(s) to use to calculate the decay score.
excludeDecayed
1
Filter out all expired IoCs.
modelOverrides.threshold
30
JSON that can be used to modify Model parameters on-the-fly.
published
1
Set whether published or unpublished events should be returned Accepted values 0 or 1.
to_ids
1
By default (0) all attributes are returned that match the other filter parameters, regardless of their to_ids setting.
enforceWarninglist
1
Remove any attributes from the result that would cause a hit on a warninglist entry.
Sample API Response
{
"response": {
"Attribute": [
{
"id": "347224",
"event_id": "1315",
"object_id": "0",
"object_relation": null,
"category": "Network activity",
"type": "ip-src",
"to_ids": true,
"uuid": "567ac850-6337-4266-a646-9317661f8974",
"timestamp": "1719987636",
"distribution": "5",
"sharing_group_id": "0",
"comment": "",
"deleted": false,
"disable_correlation": false,
"first_seen": null,
"last_seen": null,
"value": "efd:2dbe:3d3:b9ac:71e1:fd4f:5d2:2de7",
"decay_score": [
{
"score": 30.478404654276954,
"base_score": 90,
"decayed": false,
"DecayingModel": {
"id": "2",
"name": "NIDS Simple Decaying Model Updated"
}
}
],
"Event": {
"org_id": "1",
"distribution": "1",
"id": "1315",
"info": "test",
"orgc_id": "1",
"uuid": "dceaa84e-156f-4a31-b0b2-a3ae0778d72a"
}
}
]
}
}
Check a Tag’s Existence on MISP
API Endpoint:
/tags/search/
<Tag name>
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Authorization
API Key
Accept
application/json
Content-Type
application/json
Parameters
Key
Value
limit
5000
offset
“”
Sample API Response
{
"Tag": {
"id": "1399",
"name": "netskope-ce",
"colour": "#ff0000",
"exportable": true,
"org_id": "0",
"user_id": "0",
"hide_tag": false,
"numerical_value": null,
"is_galaxy": false,
"is_custom_galaxy": false,
"local_only": false
}
}
]
Create a Tag on MISP
API Endpoint:
/tags/add
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Authorization
API Key
Accept
application/json
Content-Type
application/json
Parameters
Key
Value
name
<Tag Name>
colour
#ff0000
Sample API Response
{
"Tag": {
"id": "1400",
"name": "netskooe-ce",
"colour": "#ff0000",
"exportable": true,
"org_id": "0",
"user_id": "0",
"hide_tag": false,
"numerical_value": null,
"is_galaxy": false,
"is_custom_galaxy": false,
"local_only": false
}
}
Share Indicators to an Existing Event (Update Event)
API Endpoint:
/events/edit/
<Event ID>
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Authorization
API Key
Accept
application/json
Content-Type
application/json
Parameters
Key
Value
Comment
type
sha256
Indicator Type
value
56af10adb647b1e675f3f486c7941fbf637ebd0c6632e86e6dc9879d2214441a
SHA256 value
comment
Test IoC
first_seen
2024-07-05T09:48:51.585000
First Seen of the IoC
last_seen
2024-07-05T09:48:51.585000
First Seen of the IoC
Tag.name
netskope-ce |
<Source Plugin name>
Sample Payload
{
"Attribute": [
{
"type": "sha256",
"value": "56af10adb647b1e675f3f486c7941fbf637ebd0c6632e86e6dc9879d2214441a",
"comment": "Test IoC.",
"first_seen": "2024-07-05T09:48:51.585000",
"last_seen": "2024-07-05T09:48:51.585000",
"Tag": [
{
"name": "netskope-ce"
}
]
}
]
}
Sample API Response
{
"Event": {
"id": "1317",
"orgc_id": "1",
"org_id": "1",
"date": "2024-06-25",
"threat_level_id": "4",
"info": "new",
"published": false,
"uuid": "09502561-a07f-41e9-8359-59394878e47d",
"attribute_count": "12",
"analysis": "0",
"timestamp": "1720443083",
"distribution": "1",
"proposal_email_lock": false,
"locked": false,
"publish_timestamp": "0",
"sharing_group_id": "0",
"disable_correlation": false,
"extends_uuid": "",
"protected": null,
"event_creator_email": "admin@admin.test",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18",
"local": true
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18",
"local": true
},
"Attribute": [
{
"id": "1488555",
"type": "sha256",
"category": "Payload delivery",
"to_ids": true,
"uuid": "343b7c36-beb7-4197-945e-4b35c8179426",
"event_id": "1317",
"distribution": "5",
"timestamp": "1720443083",
"comment": "Test IoC.",
"sharing_group_id": "0",
"deleted": false,
"disable_correlation": false,
"object_id": "0",
"object_relation": null,
"first_seen": "2024-07-05T09:48:51.585000+00:00",
"last_seen": "2024-07-05T09:48:51.585000+00:00",
"value": "56af10adb647b1e675f3f486c7941fbf637ebd0c6632e86e6dc9879d2214441a",
"Galaxy": [
],
"ShadowAttribute": [
],
"Tag": [
{
"id": "1399",
"name": "netskope-ce",
"colour": "#ff0000",
"exportable": true,
"user_id": "0",
"hide_tag": false,
"numerical_value": null,
"is_galaxy": false,
"is_custom_galaxy": false,
"local_only": false,
"local": 0,
"relationship_type": null
}
]
}
],
"ShadowAttribute": [
],
"RelatedEvent": [
{
"Event": {
"id": "1325",
"date": "2024-07-05",
"threat_level_id": "4",
"info": "new5",
"published": false,
"uuid": "3508388f-b6a6-4be2-9b99-de05825cc304",
"analysis": "0",
"timestamp": "1720177270",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1324",
"date": "2024-07-02",
"threat_level_id": "4",
"info": "new4",
"published": false,
"uuid": "e8d24ff9-2955-4eb6-80f1-5f276fae2e42",
"analysis": "0",
"timestamp": "1720424260",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1319",
"date": "2024-06-27",
"threat_level_id": "4",
"info": "420test",
"published": false,
"uuid": "1e1f4455-8d0e-43dd-95ba-0fd4f7eb6abf",
"analysis": "0",
"timestamp": "1720418522",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1315",
"date": "2024-03-12",
"threat_level_id": "4",
"info": "test",
"published": false,
"uuid": "dceaa84e-156f-4a31-b0b2-a3ae0778d72a",
"analysis": "0",
"timestamp": "1720175425",
"distribution": "1",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
},
{
"Event": {
"id": "1308",
"date": "2015-01-01",
"threat_level_id": "1",
"info": "testevent",
"published": false,
"uuid": "0c3d5017-8edf-483b-a829-426bb2c56c92",
"analysis": "0",
"timestamp": "1699523309",
"distribution": "0",
"org_id": "1",
"orgc_id": "1",
"Org": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
},
"Orgc": {
"id": "1",
"name": "ORGNAME",
"uuid": "45d545a3-859f-4645-9139-0d8fb8730f18"
}
}
}
],
"Galaxy": [
],
"Object": [
],
"EventReport": [
],
"CryptographicKey": [
],
"Tag": [
{
"id": "251",
"name": "workflow:todo=\"create-missing-misp-galaxy-cluster\"",
"colour": "#770040",
"exportable": true,
"user_id": "0",
"hide_tag": false,
"numerical_value": null,
"is_galaxy": false,
"is_custom_galaxy": false,
"local_only": false,
"local": 0,
"relationship_type": null
}
]
}
}
Share Indicators to a New Event (Create Event)
API Endpoint:
/events/add
Method: POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Authorization
API Key
Accept
application/json
Content-Type
application/json
Parameters
Key
Value
Comment
type
sha256
Indicator Type
value
56af10adb647b1e675f3f486c7941fbf637ebd0c6632e86e6dc9879d2214441a
SHA256 value
comment
Test IoC.
first_seen
2024-07-05T09:48:51.585000
First Seen of the IoC
last_seen
2024-07-05T09:48:51.585000
First Seen of the IoC
Tag.name
netskope-ce
Sample Payload
{
"info": "test"
"Attribute": [
{
"type": "sha256",
"value": "56af10adb647b1e675f3f486c7941fbf637ebd0c6632e86e6dc9879d2214441a",
"comment": "Test IoC.",
"first_seen": "2024-07-05T09:48:51.585000",
"last_seen": "2024-07-05T09:48:51.585000",
"Tag": [
{
"name": "netskope-ce"
}
]
}
]
}
Sample API Response
{
"Tag": {
"id": "1400",
"name": "netskope-ce",
"colour": "#ff0000",
"exportable": true,
"org_id": "0",
"user_id": "0",
"hide_tag": false,
"numerical_value": null,
"is_galaxy": false,
"is_custom_galaxy": false,
"local_only": false
}
}
Performance Matrix
Here is the performance reading conducted by pulling and sharing 100K indicators from/to MISP on a Large CE Stack with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from MISP Platform
~18K per minute
Indicators shared with MISP Platform
~8K per minute
User Agent
netskope-ce-6.0.0-cte-misp-v1.5.1
Workflow
Get your MISP URL and API key.
Configure the MISP Plugin.
Configure a Business Rule.
Configure Sharing between Netskope and MISP.
Validate the MISP Plugin.
Watch a Video
Click play to watch a video:
Get your Instance URL and Auth Key
Log in to your MISP Instance and go to
Administration > List Auth Keys
.
Click
Add authentication key
, enter the required parameters, and click
Submit
.
Your MISP API key will be generated. Make a copy of this value for when you configure the Plugin.
Configure the MISP Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
MISP v1.5.1 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name
: Plugin configuration name.
Sync Interval
: Interval to fetch data from this plugin source.
Aging Criteria:
Expire indicators after a specific time.
Override Reputation
: Set value to override reputation of indicators received from this configuration. Leave empty to keep the default.
Enable SSL Validation
: Enable/Disable SSL Certificate validation based on your platform requirement.
Use System Proxy
: Use system proxy configured in Settings.
Click
Next
and enter the Configuration Parameters:
MISP Base URL:
Base URL of MISP instance. (like https://
<misp-url>
)
Authentication Key:
API Key generated from the MISP platform. API Key can be generated on the
Administration > List Auth Keys
page.
MISP Attribute Type:
Select MISP attribute type(MD5, SHA256, URL (Source IP|Port (ip-src|port), Destination IP|Port (ip-dst|port), and Hostname|Port (hostname|port)), Domain, IPv4 and IPv6 Source IP (ip-src) and Destination IP (ip-dst)), Domain( Domain|IP), Hostname). Indicators from only specified attribute types will be fetched. Keep empty to fetch indicators of all types. Multiple Types are accepted.
MISP attribute Category:
Select MISP attribute Category, Indicators from only specified Attribute Categories will be fetched. Keep empty to fetch indicators of all Categories. Multiple Categories are accepted.
MISP Attribute Tags:
Enter MISP Attribute Tags, Indicators from only specified comma-separated Tags will be fetched. Keep empty to fetch indicators of all Tags. Dynamic values are accepted.
Event Names:
Leave Event Names blank to fetch indicators from all the events or enter them separately by comma to fetch only those indicators which belong to that event. For now, we leave it blank.
Exclude IoCs from Event:
In Exclude IoCs from Event , enter the name of the event whose IoCs you want to exclude from being fetched. Indicators attached to the provided comma-separated events will be ignored while pulling data from MISP. Expected value is comma-separated event names or event IDs.
Ioc Event Type:
Indicators will be pulled based on the selected event type. Published, Unpublished or both types of events can be selected. Keep empty to fetch all types.
Decaying Score Threshold:
Only indicators having Decaying Score greater than Provided value will be pulled. Value should be in the range of 0 to 100.
Decaying Model IDs:
Decaying score of only specified comma separated decaying models will be tracked. Keep blank to fetch scores for all enabled decaying models that apply to the attribute type. Decaying model IDs can be found from ‘Global Action > List Decaying Models’.
Filter on IDS Flag:
Pull IoCs based on the Selected option for IDS. Enabled IDS flag, Disabled IDS flag or both types of indicators can be selected. Keep empty to fetch all indicators.
Enforce Warning List IOCs:
Select
Yes
to remove any IoC from the events that would cause a hit on a warning list entry. Warning List can be found from
Input Filters > Warninglists
.
Pulling Mechanism:
Select a Pulling Mechanism.
Incremental (Default):
Plugin will fetch data using stored checkpoint i.e. last_run_at of the plugin.
Look Back:
Plugin will fetch data subtracting lookback value from the plugin run time on every sync. For example: If the provided value is 72 Hrs, then it will fetch 72 Hrs of IoCs from now on every sync.
Look Back (in hours):
Enter Look Back (in hours) to pull the indicators of historical time from now on every time the plugin syncs. Default value is set to empty and it will only be used when Look Back is selected in Pulling Mechanism.
Retraction Interval (in days):
Retraction Interval days to run IoC(s) retraction for MISP indicators. Note that this parameter will only be considered if
IoC(s) Retraction
is enabled in the Threat Exchange settings. The minimum value expected for the retraction will be 1. If the retraction value is not added and IoC(s) Retraction is enabled in the global setting, retraction will not take place in the plugin.
Enable Tagging:
Plugin will pull tags associated with the IoCs if Enable tagging is Yes. If you do not want to pull tags with the IoCs, keep Enable tagging as No.
Initial Range (in days):
Number of days to pull the data for the initial run. Note: This parameter will only be considered if Pulling Mechanism is set to
Incremental
.
Click
Save
.
Note
IoCs stored in Cloud Exchange will have the current date and time as
Last_Seen
rather than the MISP’s last seen.
Configure a Threat Exchange Business Rule for MISP
A Business Rule is used to filter out the indicators that are to be shared. In order to share IoCs with MISP, create a business rule using the following steps:
Go to
Threat Exchange > Business Rules
and click
Create New Rule
.
Add a Rule name and select the fields for which you want to filter the IoCs.
Add a Rule name and select the fields for which you want to filter the IoCs. For example,
IoCs by Sources is equal to CTE Netskope
. Click
Save
.
Click
Create New Rule
. Add a Rule name and select the fields for which you want to filter the IoCs. For example,
IoCs by Sources is equal to CTE MISP
.
Click
Save
.
Add Threat Exchange Sharing for MISP
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select the Source configuration (Source from which you want to share data to MISP), a Business Rule, and the Destination (MISP Plugin).
Select the Target value
Add to Event
.
Enter the Event Name that you want to use for pushing IoCs on the MISP Platform.
Select the type for sharing the IPv4 or IPv6 IoCs to MISP.
Click
Save
.
Validate the MISP Plugin
Validate the Pull
Indicators from MISP are pulled from:
Event Actions > List Attributes
.
Indicators stored in Cloud Exchange can be verified from the
Threat Exchange > Threat IoCs
page.
Search for the MISP IoCs by filtering indicators on the Threat IoCs page with source name as
Configured MISP Plugin
.
Example: Add a query on the Threat IoCs page like
“sources.source Is equal “CTE MISP” && type IN (“<IOC_TYPE>”)”
You can also verify the indicators pulled in Cloud Exchange from the logs available at
Logging
.
For verifying the Retracted IoCs from MISP, check the logs for IoC Retraction. For example:
message Like “CTE MISP [CTE MISP] [Retraction]:”
When the IoCs shared from MISP to 3rd-Party will be retracted, it will be marked as
“<plugin-config-name>: retracted”
in the Retraction Result. If they are not deleted from the 3rd-party, the Retraction Result will be pending.
Note
The IoCs that are deleted on the MISP and fall under the Retraction Interval will be marked as Retracted in Cloud Exchange.
To check the retracted IoCs in Cloud Exchange, go to
Threat IoCs
and search for
“sources.source Like “CTE MISP” && sources.retracted Is equal true”
Validate the Push
Shared IoCs to MISP can be verified from logs available at
Logging
in Cloud Exchange.
IoCs shared on MISP can be verified from
Event Actions > List Events
.
Click on the Event ID that you used while configuring the sharing to view all the shared IoCs.
The IoC Labeling is added to each of the IoCs that are shared/pushed to MISP from Cloud Exchange, the format for the same will be
“Netskope CE | <plugin-name>”
The IoC labeling for the Shared IoCs will be added as a part of tags on MISP; it can also be verified by the log available in Cloud Exchange Logging while IoCs are shared to MISP.
Troubleshooting the MISP Plugin
Error while upgrading the plugin repository
While trying to upgrade a plugin if the below error is received, follow the steps provided.
What to do:
Click
Skip
and go to
Home > Threat Exchange > Plugins
.
Edit the plugin as it will be disabled due to an error while upgrading the plugin.
Click
Next
.
Scroll down to newly added params (Pulling Mechanism and Look Back) and select the method of pulling and provide Look Back as per the Pulling Mechanism selected.
Click
Save
and then enable the plugin.
Unable to pull/push data to MISP Plugin
If you are not able to share IoCs from Netskope to MISP, that could be the Authentication Key of MISP could have either expired, or has been deleted from the MISP Platform.
What to do:
Make sure that all the Authentication Key of MISP is not expired. Also ensure that the Key is not deleted from the MISP. Authentication Key and its details can be found at
Administration > List Auth Keys
.
Pulled domains and IPs are stored as URL in Cloud Exchange
If you have data pulled from MISP and the IoCs of type domain, IPv4 and IPv6 are stored as URL in Cloud Exchange, it could be due to one of the following reasons:
Plugin is not updated to v1.4.0
Plugin version is v1.4.0 but core is not updated to v5.0.1
IoC type on MISP is URL
What to do:
The URL bifurcation for the MISP plugin is available from MISP plugin v1.4.0, if your plugin is any version below this the bifurcation update won’t be available.
The URL bifurcation is supported in Cloud Exchange from core (CE version) v5.0.1, if your Cloud Exchange is not updated to the supported version the bifurcation will not be available and all domains and IPs pulled from the platform will be stored as URL. If you want to pull data as per the URL bifurcation your plugin version must be v1.4.0 or above and core version as v5.0.1 or above.
If both your core and plugin are updated and still few of the IoCs of type domain, IPv4 and  IPv6 are stored as URLs in Cloud Exchange, it must be due to the IoC type of the indicator on MISP. If the IoC on MISP has type as URL for the domains/IPs, it will be pulled and stored as URL in Cloud Exchange. If MISP has domain as IOC type, it will be pulled and stored as domain in Cloud Exchange. The IoC type for IPs on MISP is
ip-src
.
Limitation
Decaying Score is not in sync with MISP for Incremental Pulling Mechanism
If the user is using the Incremental pulling mechanism, after an IoC is pulled from MISP along with its decaying score, the IOoC will only be pulled again into Cloud Exchange if the timestamp for that indicator gets updated on MISP. Otherwise, the decaying score will remain as it was when initially pulled.
This is a limitation of the MISP platform: when updating the decaying score, the timestamp associated with the attribute is not updated. In Cloud Exchange, we use the timestamp fields from MISP attributes to capture only the updated indicators. Therefore, if the timestamp value is not updated, the IoC will never be pulled again into Cloud Exchange.
To address this, the user can use the Look Back pulling mechanism to pull all the indicators based on the Look Back period specified in the configuration parameters for each pull.
Known Behavior
Difference in response displayed on the UI in case
Decaying Model IDs
field is left empty and when all Model IDs are added
If no Model IDs are provided in the Decaying Model IDs field, the decaying scores associated with the attribute will be fetched in Cloud Exchange. For example, if there are three models in the MISP instance and only one model is attached to the attribute, only the decaying score for that specific model will be fetched in Cloud Exchange.
However, if specific Model IDs are provided, whether they are associated with the attribute or not, the scores for all available models will be returned via the API. In the MISP UI, only the associated models will be shown.
In this Topic
MISP Plugin for Threat Exchange

---
## Palo Alto Networks Panorama Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/palo-alto-networks-panorama-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:47:42+00:00
**Scraped:** 2026-08-11T07:18:19.240040+00:00

Palo Alto Networks Panorama Plugin for Threat Exchange - Netskope Technical Documentation
Palo Alto Networks Panorama Plugin for Threat Exchange
This document explains how to configure the Palo Alto Networks Panorama v1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. The Palo Alto Networks Panorama plugin fetches information about domains, IP addresses, file hashes (SHA256) from Wildfire logs, and URLs from URL Filtering logs.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Palo Alto Networks Panorama platform credentials.
Connectivity to the following host: Palo Alto Networks Panorama instance. For example: https://
<your-panorama-domain>.
Panorama Plugin Support
The Palo Alto Networks Panorama plugin is used to fetch SHA256 file hashes from Wildfire logs, and URLs from URL Filtering logs. This plugin does not support sharing of IoCs to Palo Alto Networks Panorama.
Fetched indicator types
Shared indicator types
SHA256, URLs
Not Supported
Mappings
Pull Mappings
Netskope CE Fields
Palo Alto Networks Panorama Fields
value
file hashes from Wildfire logs (SHA256)
OR
URLs from URL Filtering logs(URLs)
type
type
firstSeen
first_timestamp
lastSeen
last_timestamp
Severity
severity
tags
tags
comments
Filename: misc data from response
Note:
The comments are present only for indicator of type filehases(SHA256)
Permissions
The API Key needs to have XML API permissions available to pull the indicators. Follow
this
official document of the panorama platform to give permission to your user.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/api
GET
Get job id to fetch the logs
Pull indicators from Wildfire and URLs
Get job id to fetch the logs
API Endpoint:
BASE_URL/api
Method:
GET
Request Params
Key
Value
key
Api-key
type
type
log_type
Wildfire (For Malware)
OR
Url (For URL)
query
(time_generated geq ‘<last_run_time>’)
nlogs
5000
dir
forward
Sample API Response
{
  "response": {
    "@status": "success",
    "@code": "19",
    "result": {
      "msg": {
        "line": "query job enqueued with jobid 160"
      },
      "job": "160"
    }
  }
}
Pull indicators from Wildfire and URLs
API Endpoint:
BASE_URL/api
Method:
GET
Request Params
Key
Value
key
Api-key
type
type
action
get
job-id
job-id
Sample API Response
{
  "response": {
    "@status": "success",
    "result": {
      "job": {
        "tenq": "23:56:16",
        "tdeq": "23:56:16",
        "tlast": "16:00:00",
        "status": "ACT",
        "id": "165",
        "cached-logs": "0"
      },
      "log": {
        "logs": {
          "@count": "0",
          "@progress": "0"
        }
      }
    }
  }
}
Workflow
Create an Admin Role with the Required Permissions.
Create an Admin User.
Get your API Key
Configure the Panorama plugin
Validate the Panorama plugin.
Click play to watch a video.
Get your Panorama Base URL and API Key
Create an Admin Role Profile with the Required Permissions
In the Web UI, enable the following options:
Monitor
Logs
URL Filtering
WildFire Submissions
In the XML API, enable the following options:
Log
Configuration
No other permissions are required, so you can disable all other options.
Refer to these screenshots for reference:
When finished, click
OK
.
Create an Admin User
After the profile is created, go to
Panorama > Administrators
and create a new admin user.
Select
Custom Panorama Admin
as the
Administrator Type
.
Under the
Profile
section, choose the
Admin Role
created in the previous step.
Click
OK
.
Here’s a screenshot for reference:
Get your API Key
To configure the plugin, you will need an
API Key
. You can retrieve it by following the steps outlined in the Panorama documentation:
Get Your API Key
.
Configure the Palo Alto Networks Panorama Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the Palo Alto Networks Panorama box.
Enter the basic information:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave Default.
Aging Criteria: Leave Default.
Override Reputation: Leave Default.
Tags Aggregate Strategy: Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL verification: Enable if SSL verification is required for communication.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter the configuration parameters:
Base URL: The Base URL is the Panorama device’s IP address or Domain name, like https://
<your-panorama-domain>
.
API Key: The API keys on the firewall and Panorama enable you to authenticate API calls to the XML API and REST API.
Type of Threat data: Select Type of Threat Data. Select Malware if you want to pull only file hashes, or URL if you want to pull only URLs, and select Both if you want to pull both.
Initial Range (in days): Number of days to pull the data for the initial run.
Click
Save
.
Now plugin is configured and you’ll see plugin configuration in
Threat Exchange > Plugins.
Configure a Threat Exchange Business Rule for Panorama
To share indicators fetched from the Palo Alto Networks Panorama to the Netskope CE, you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule follow the below steps:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filters according to your requirements in the rule, and then click
Save
.
Configure Sharing for Panorama
To share IoCs from the Palo Alto Networks Panorama to the Cloud Exchange:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Palo Alto Networks Panorama), a Business Rule, the Destination Configuration (CTE Netskope), and a Target.
Click
Save
.
Validate the Palo Alto Networks Panorama Plugin
Validate the Pull
To verify the data available for pulling on Palo Alto Networks Panorama:
Log in to your Panorama instance.
Go to
Monitor > Wildfire Submissions.
You are fetching file hashes from this page. So if these logs appear over here, then indicators will be pulled in Cloud Exchange.
Go to
Monitor > URL Filtering
.
You are fetching URLs from this page. So, if logs are available in this page, then it will be fetched as an indicator in Cloud Exchange.
Troubleshooting the Panorama Plugin
Unable to pull IoCs from the Palo Alto Networks Panorama platform
After the plugin configuration if the IoCs are not pulled from the platform it might be due to one of the following.
No IoCs are available on the platform to pull
IoCs are not available for the given time range or do not match the configuration parameters.
What to do:
Identity your root cause from above and follow below steps to resolve the issue.
No IoCs are available on the platform to pull
Check if the IoCs are available on the platform to pull. If available, check the resolution for the next point.
IOCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Palo Alto Networks Panorama platform, check if you have data for the given time range.
If the data is still available for the given time range it might be possible that the IoCs for the provided filter (Malware, URL) in the plugin configuration are not available, so check the values from the plugin configuration parameter, and filter the same on the Palo Alto Networks Panorama platform.
Unable to configure the Palo Alto Networks Panorama plugin
It might be due to one of the following:
Invalid Base URL
Inavalid API key
What to do:
Identify the root cause and follow the steps for the specified issue.
Invalid Base URL
Refer to the
Prerequisites
section and ensure your Palo Alto Networks Panorama instance is working properly.
Invalid API key
Refer to the
Get your API Key
section to get the valid API Key for your Palo Alto Networks Panorama instance.
Limitation
We only support pulling 100k indicators as of now, which takes around 2 and a half hours to pull, and then a few more hours to store in Cloud Exchange. If the data to be pulled is greater than 100k, you might start to see some performance issues in Cloud Exchange, like data taking too long to be fetched, Cloud Exchange taking time to respond, etc. This issue will be fixed in the next release of Cloud Exchange.
In this Topic
Palo Alto Networks Panorama Plugin for Threat Exchange

---
## Proofpoint Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/proofpoint-plugin-for-threat-exchange/
**Last Modified:** 2026-06-11T00:57:36+00:00
**Scraped:** 2026-08-11T07:18:25.548823+00:00

Proofpoint Plugin for Threat Exchange - Netskope Technical Documentation
Proofpoint Plugin for Threat Exchange
Release Notes
2.0.0
Added
Added support for IoC(s) Retraction.
Added resolution for error logs starting from CE v6.0.0.
Added support to bifurcate the URL by types (Domain, FQDN and URL).
Added handling of API rate limit.
Changed
Improved error handling.
1.0.0
Added
Initial Release
This document explains how to configure the Proofpoint v2.0.0 plugin in the Cloud Exchange platform. This plugin is used to pull IoCs of type URL, SHA256, Domain, and FQDN from the Proofpoint TAP (Targeted Attack Protection) Dashboard under Threats. The plugin supports pull retraction of indicators from Proofpoint. This plugin does not support sharing of indicators to Proofpoint platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
DNS Profile
on your Netskope Tenant
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the Proofpoint platform.
Connectivity to the following host:
https://tap-api-v2.proofpoint.com
.
Proofpoint Plugin Support
This plugin is used to pull IOCs of type URL, SHA256, Domain, and FQDN from the Proofpoint TAP (Targeted Attack Protection) Dashboard under Threats. The plugin supports pull retraction of indicators from Proofpoint. This plugin does not support sharing of indicators to Proofpoint platform.
Fetched Indicator Types
Shared Indicator Types
URL, SHA256, Domain, FQDN
Not Supported
IOC Retraction
IoC Retraction (Pull):
Indicators will be fetched from Proofpoint and in the subsequent pull cycles. If some indicators are deleted from Proofpoint, they will be marked as Retracted in Cloud Exchange.
IoC Retraction (Push):
Retracted indicators present on Cloud Exchange will be deleted from Proofpoint during sharing.
Type
Description
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
Mappings
Pull Mappings
Netskope CTE Field
Proofpoint API field
Type
threatStatus
threatStatus
String
interval
interval
Datetime
sinceSeconds
sinceSeconds
Integer
eventTypes
eventTypes
String
API Details
List of APIs used
API Endpoint
Method
Use case
/v2/siem/all
GET
Validate Credentials and Pull indicators
Validate Credentials or Pull Indicators
API Endpoint:
https://tap-api-v2.proofpoint.com/v2/siem/all
Method:
GET
Request Parameters:
Parameter
Value
format
“JSON” (default)
interval
“2024-01-01T00:00:00Z/2024-01-01T01:00:00Z”
sinceSeconds
3600
threatStatus
“active”
User-Agent
netskope-ce-5.1.2-cte-proofpoint-v2.0.0
Sample API Response:
{
  "clicksPermitted": [
    {
      "url": "https://example.com/malicious",
      "threatTime": "2024-01-01T12:00:00Z",
      "threatURL": "https://threatinfo.proofpoint.com/...",
      "classification": "malware"
    }
  ],
  "clicksBlocked": [
    {
      "url": "https://blocked-site.com",
      "threatTime": "2024-01-01T12:30:00Z",
      "threatURL": "https://threatinfo.proofpoint.com/...",
      "classification": "phish"
    }
  ],
  "messagesDelivered": [
    {
      "threatsInfoMap": [
        {
          "threat": "abc123def456...",
          "threatType": "attachment",
          "threatTime": "2024-01-01T13:00:00Z",
          "threatUrl": "https://threatinfo.proofpoint.com/...",
          "classification": "malware"
        },
        {
          "threat": "https://malicious-url.com",
          "threatType": "url",
          "threatTime": "2024-01-01T13:15:00Z",
          "threatUrl": "https://threatinfo.proofpoint.com/...",
          "classification": "phish"
        }
      ]
    }
  ],
  "messagesBlocked": [
    {
      "threatsInfoMap": [
        {
          "threat": "def789ghi012...",
          "threatType": "attachment",
          "threatTime": "2024-01-01T14:00:00Z",
          "threatUrl": "https://threatinfo.proofpoint.com/...",
          "classification": "spam"
        }
      ]
    }
  ]
}
Performance Matrix
This reading is conducted on a Large CE Stack with below-mentioned specs by pulling 100k IOCs from each page and pushing 100k IOCs to Proofpoint.
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Indicators fetched from Proofpoint
~34.5k per min
User Agent
netskope-ce-6.1.0-cte-proofpoint-v2.0.0
Workflow
Get your credentials from Proofpoint.
Configure the Proofpoint Plugin.
Configure a Business Rule for Proofpoint Plugin.
Configure Sharing for Proofpoint Plugin.
Validate the Proofpoint Plugin.
Watch a Video
Click play to watch a video.
Get your Credentials from Proofpoint
Log in to Proofpoint TAP Dashboard and go to
Settings
.
In Settings, go to
Connected Applications
.
Click
Create New Credential
.
Enter a Name and select an External Service for the credential.
Copy the generated Service Principal and Secret as they will be used to configure the plugin in Cloud Exchange. When finished, click
Done
.
Configure the Proofpoint Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Proofpoint v2.0.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources.
Note that it is better to have a larger value for Sync Interval if you want to pull IoCs in large numbers.
Aging Criteria:
Expiry time of the plugin in days (Default: 90)
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Click
Next
and enter the Configuration Parameters:
Base URL:
Proofpoint TAP API Base URL, like
https://tap-api-v2.proofpoint.com.
Username:
Proofpoint Service Principal.
Password:
Proofpoint Secret.
Event Types:
Select event types to pull threat indicators (URL, SHA256, Domain, and FQDN) from Proofpoint. If no event types are selected, all event types will be included by default.
Enable Tagging:
Enable/Disable tagging functionality.
Retraction Interval:
Number of hours to use as the retraction interval for Proofpoint IoC(s) retraction. Valid values are in range from 1 to 168 hours. This parameter will only be considered if
IoC(s) Retraction
is enabled in the Threat Exchange Settings.
Initial Range:
Number of hours Threat IoCs to pull in the initial run. Valid values are in range from 1 to 168 hours.
Click
Save
.
Configure a Threat Exchange Business Rule for Proofpoint
To share indicators fetched from the Proofpoint to the Cloud Exchange, you need to have a business rule that will filter out the indicators that you want to share.
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirement in the rule.
Click
Save
.
Configure Threat Exchange Sharing for Proofpoint Plugin
To share IoCs from Proofpoint to Netskope Cloud Exchange:
In
Threat Exchange
, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Proofpoint), Business Rule, Destination Configuration (CTE Netskope), and Target.
Click
Save
.
Note
The Proofpoint plugin does not support sharing of IoCs, but the IoCs pulled from this plugin can be shared to other 3rd-party platforms.
For more details related to the sharing configuration for Threat Exchange, refer to the
Netskope Threat Exchange plugin guide
.
Validate the Proofpoint Plugin
Validate the Pull
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE Proofpoint plugin. You can filter the logs using the filter:
message Like “[<plugin configuration name>]”
.
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
Validate the Pull Retraction
To verify the Retracted IoCs, check the logs for IoC Retraction example:
message Like CTE Proofpoint [CTE Proofpoint] [Retraction].
You can filter the retracted IoCs from the platform using the filter:
sources.source Is equal “<plugin configuration name>” && sources.retracted Is equal true.
Note
The IoCs that fall outside the Retraction Interval will be marked as Retracted: Yes in Cloud Exchange.
Also, the plugin only pulls
Active
indicators, so the indicators that were first pulled with
Active
status, and then updated to
False Positive
or
Cleared
will be marked as retracted.
The sharing result will only be marked if the IoCs are pulled from the source plugin after creating the sharing configuration.
Validate the Push
Here you can see IoCs were added to the Destination Profile on Netskope Tenant.
Then some of the shared IoCs got marked as retracted so it was deleted from the list.
Troubleshooting the Proofpoint Plugin
Unable to pull IoCs from the Proofpoint platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IoCs are available on the platform to pull
IoCs are not available for the given configuration parameters (like Initial Range).
What to do:
Identity your root cause from above and follow one of these steps to resolve the issue.
No IoCs are available on the platform to pull:
Check if the IoCs are available on the platform to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in CE, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Proofpoint platform, check if you have data for the given time range.
In this Topic
Proofpoint Plugin for Threat Exchange

---
## SentinelOne Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/sentinelone-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:49:26+00:00
**Scraped:** 2026-08-11T07:18:49.053367+00:00

SentinelOne Plugin for Threat Exchange - Netskope Technical Documentation
SentinelOne Plugin for Threat Exchange
This document explains how to configure the SentinelOne v1.4.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches IoCs of type SHA256 and MD5 file hash from the
Incidents
page in SentinelOne. This plugin supports sharing SHA256, MD5, URL, IPv4, IPv6 and DNS(Domain, Hostname, and FQDN) to Threat Intelligence.
Note that the indicators shared via Cloud Exchange won’t be shown on SentinelOne. One can verify the shared IoCs via endpoint:
<SentinelOne Base URL>/web/api/v2.1/threat-intelligence/iocs
.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
configured on your Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A SentinelOne API Account or Global account.
Connectivity to the following host: SentinelOne platform.
For example:
https://usea1-partners.sentinelone.net
.
SentinelOne Plugin Support
This plugin fetches IoCs of type SHA256 and MD5 file hash from the
Incidents
page in SentinelOne. This plugin supports sharing SHA256, MD5, URL, IPv4, IPv6 and DNS(Domain, Hostname, and FQDN) to Threat Intelligence.
Fetched Indicator Types
Shared Indicator Types
SHA256, MD5
SHA256, MD5, URL, IPv4, IPv6, DNS(Domain, Hostname, and FQDN)
Mappings
Pull Mappings
Cloud Exchange Fields
SentinelOne Fields
value
fileSha256
comments
classification, confidenceLevel, engines
firstSeen
createdAt
lastSeen
updatedAt
tags
analystVerdictDescription
extraInformation
{SentinelOne_URL}/analyze/threats/{id}/overview
Push Mappings
Cloud Exchange Fields
SentinelOne Fields
value
value
type
type
value
externalId
firstseen
creationTime
expireAt
validUntill
comments
description
Permissions
Here are the permissions needed for the successful execution of the plugin.
Accounts: view
Groups: view
Roles: view
Sites: view
Endpoint threats: view, Fetch Threat File
Threat Intelligence: view, Manage
API Details
List of APIs used
API Endpoint
Method
Use Case
/web/api/v2.1/sites
GET
Fetch Site IDs.
/web/api/v2.1/threats
GET
Fetch Indicators and check for modified Indictators.
/web/api/v2.1/threat-intelligence/iocs
POST
Push Indicators.
/web/api/v2.1/threat-intelligence/iocs
DELETE
Delete Indicators.
Fetch Site IDs
API Endpoint:
https://
<SENTINEL TENANT>
/web/api/v2.1/sites
Method:
GET
Headers
Key
Value
Authorization
ApiToken
<TOKEN>
User Agent
netskope-ce-6.0.1-cte-sentinelone-v1.4.0
Parameters
Key
Value
name
Site Name
Sample API Response
{
    "data": {
        "allSites": {
            "activeLicenses": 7,
            "totalLicenses": 25
        },
        "sites": [
            {
                "accountId": "1268419425097944269",
                "accountName": "Netskope",
                "activeLicenses": 7,
                "createdAt": "2021-10-17T02:02:58.519858Z",
                "creator": "Sandeep Minhas",
                "creatorId": "1170348439571106212",
                "description": null,
                "expiration": null,
                "externalId": "97e5ca8f-5ad4-cb4a-7ef8-9d27a2557175",
                "healthStatus": true,
                "id": "1268419425114721486",
                "isDefault": true,
                "licenses": {
                    "bundles": [
                        {
                            "displayName": "Core",
                            "majorVersion": 1,
                            "minorVersion": 6,
                            "name": "core",
                            "surfaces": [
                                {
                                    "count": 25,
                                    "name": "Total Agents"
                                }
                            ],
                            "totalSurfaces": 25
                        }
                    ],
                    "modules": [
                        {
                            "displayName": "Ranger",
                            "majorVersion": 1,
                            "name": "ranger"
                        }
                    ],
                    "settings": [
                        {
                            "displayName": "365 Days",
                            "groupName": "malicious_data_retention",
                            "setting": "365 Days",
                            "settingGroup": "malicious_data_retention",
                            "settingGroupDisplayName": "Malicious Data Retention"
                        },
                        {
                            "displayName": "Available",
                            "groupName": "marketplace_access_status",
                            "setting": "Available",
                            "settingGroup": "marketplace_access_status",
                            "settingGroupDisplayName": "Marketplace Access"
                        },
                        {
                            "displayName": "Account",
                            "groupName": "account_level_ranger",
                            "setting": "Account",
                            "settingGroup": "account_level_ranger",
                            "settingGroupDisplayName": "Ranger Consolidation Level"
                        }
                    ]
                },
                "name": "Default site",
                "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiYjVjYTA0ZDVlYjc0MjA0MyJ9",
                "siteType": "Paid",
                "sku": "Core",
                "state": "active",
                "suite": "Core",
                "totalLicenses": 25,
                "unlimitedExpiration": true,
                "unlimitedLicenses": false,
                "updatedAt": "2024-01-23T12:37:22.573745Z"
            }
        ]
    },
    "pagination": {
        "nextCursor": null,
        "totalItems": 1
    }
}
Fetch Indicators and check for Modified Indicators
API Endpoint:
https://
<SENTINEL TENANT>
/web/api/v2.1/sites
Method:
GET
Headers
Key
Value
Authorization
ApiToken
<TOKEN>
User Agent
netskope-ce-6.0.1-cte-sentinelone-v1.4.0
Parameters
updatedAt__gte
2023-02-02T08:30:37.680000Z
updatedAt__lte
2023-02-09T08:47:37.680000Z
analystVerdicts
true_positive,suspicious,false_positive,undefined
limit
100
siteIds
1268419425114721486
{
  "data": [
    {
      "agentDetectionInfo": {
        "accountId": "1268419425097944269",
        "accountName": "Netskope",
        "agentDetectionState": "full_mode",
        "agentDomain": "NETSKOPE",
        "agentIpV4": "10.0.2.82,198.19.83.174",
        "agentIpV6": "",
        "agentLastLoggedInUpn": null,
        "agentLastLoggedInUserMail": null,
        "agentLastLoggedInUserName": "",
        "agentMitigationMode": "detect",
        "agentOsName": "Windows Server 2016 Datacenter",
        "agentOsRevision": "14393",
        "agentRegisteredAt": "2024-01-11T09:37:33.558245Z",
        "agentUuid": "919bda8871934b289fcd3f0b1ee3b2b6",
        "agentVersion": "23.3.3.264",
        "assetVersion": "264",
        "cloudProviders": {
          "AWS": {
            "awsRole": null,
            "awsSecurityGroups": [
              "Workspace"
            ],
            "awsSubnetIds": [
              "subnet-0b0533f1bb462f7bf",
              "subnet-0216a3836557c718f"
            ],
            "cloudAccount": "517168379634",
            "cloudImage": "ami-0fbea36fd7bd4f5fe",
            "cloudInstanceId": "i-036e160c50b977ee7",
            "cloudInstanceSize": "t3.medium",
            "cloudLocation": "ap-southeast-1",
            "cloudNetwork": "vpc-0fc65d8a5f3774876",
            "cloudTags": [
              "Endpoint does not have sufficient permissions to fetch tags"
            ]
          }
        },
        "externalIp": "18.140.109.245",
        "groupId": "1268419425123110095",
        "groupName": "Default Group",
        "siteId": "1268419425114721486",
        "siteName": "Default site"
      },
      "agentRealtimeInfo": {
        "accountId": "1268419425097944269",
        "accountName": "Netskope",
        "activeThreats": 0,
        "agentComputerName": "WSAMZN-FE0FUJ90",
        "agentDecommissionedAt": true,
        "agentDomain": "NETSKOPE",
        "agentId": "1860065221432363061",
        "agentInfected": false,
        "agentIsActive": false,
        "agentIsDecommissioned": true,
        "agentMachineType": "server",
        "agentMitigationMode": "detect",
        "agentNetworkStatus": "connected",
        "agentOsName": "Windows Server 2016 Datacenter",
        "agentOsRevision": "14393",
        "agentOsType": "windows",
        "agentUuid": "919bda8871934b289fcd3f0b1ee3b2b6",
        "agentVersion": "23.3.3.264",
        "groupId": "1268419425123110095",
        "groupName": "Default Group",
        "networkInterfaces": [
          {
            "id": "1860065221499471932",
            "inet": [
              "198.19.83.174"
            ],
            "inet6": [
            ],
            "name": "Ethernet 3",
            "physical": "06:36:49:72:4c:84"
          },
          {
            "id": "1860065221482694715",
            "inet": [
              "10.0.2.82"
            ],
            "inet6": [
            ],
            "name": "Ethernet 4",
            "physical": "06:29:ab:f6:cd:3e"
          }
        ],
        "operationalState": "na",
        "rebootRequired": false,
        "scanAbortedAt": null,
        "scanFinishedAt": null,
        "scanStartedAt": "2024-01-11T09:39:41.493730Z",
        "scanStatus": "started",
        "siteId": "1268419425114721486",
        "siteName": "Default site",
        "storageName": null,
        "storageType": null,
        "userActionsNeeded": [
        ]
      },
      "containerInfo": {
        "id": null,
        "image": null,
        "isContainerQuarantine": null,
        "labels": null,
        "name": null
      },
      "ecsInfo": {
        "clusterName": null,
        "serviceArn": null,
        "serviceName": null,
        "taskArn": null,
        "taskAvailabilityZone": null,
        "taskDefinitionArn": null,
        "taskDefinitionFamily": null,
        "taskDefinitionRevision": null,
        "type": null,
        "version": null
      },
      "id": "1860067293510813906",
      "indicators": [
        {
          "category": "Abnormalities",
          "description": "The Entry point for this binary is an RWX section. It might contain self-modifying code",
          "ids": [
            32
          ],
          "tactics": [
          ]
        },
        {
          "category": "Abnormalities",
          "description": "This binary has an RWX section. It might contain self-modifying code",
          "ids": [
            33
          ],
          "tactics": [
          ]
        },
        {
          "category": "General",
          "description": "This binary imports debugger functions",
          "ids": [
            6
          ],
          "tactics": [
          ]
        }
      ],
      "kubernetesInfo": {
        "cluster": null,
        "controllerKind": null,
        "controllerLabels": null,
        "controllerName": null,
        "isContainerQuarantine": null,
        "namespace": null,
        "namespaceLabels": null,
        "node": null,
        "nodeLabels": null,
        "pod": null,
        "podLabels": null
      },
      "mitigationStatus": [
      ],
      "threatInfo": {
        "analystVerdict": "undefined",
        "analystVerdictDescription": "Undefined",
        "automaticallyResolved": true,
        "browserType": null,
        "certificateId": "",
        "classification": "Malware",
        "classificationSource": "Static",
        "cloudFilesHashVerdict": null,
        "collectionId": "1860067293544368339",
        "confidenceLevel": "suspicious",
        "createdAt": "2024-01-11T09:41:40.575731Z",
        "detectionEngines": [
          {
            "key": "pre_execution_suspicious",
            "title": "On-Write Static AI - Suspicious"
          }
        ],
        "detectionType": "static",
        "engines": [
          "On-Write DFI - Suspicious"
        ],
        "externalTicketExists": false,
        "externalTicketId": null,
        "failedActions": false,
        "fileExtension": "EXE",
        "fileExtensionType": "Executable",
        "filePath": "\\Device\\HarddiskVolume2\\Users\\mrai\\Downloads\\wildfire-test-pe-file (2).exe",
        "fileSize": 55296,
        "fileVerificationType": "NotSigned",
        "identifiedAt": "2024-01-11T09:41:39.995000Z",
        "incidentStatus": "resolved",
        "incidentStatusDescription": "Resolved",
        "initiatedBy": "agent_policy",
        "initiatedByDescription": "Agent Policy",
        "initiatingUserId": null,
        "initiatingUsername": null,
        "isFileless": false,
        "isValidCertificate": false,
        "macroModules": null,
        "maliciousProcessArguments": null,
        "md5": null,
        "mitigatedPreemptively": false,
        "mitigationStatus": "not_mitigated",
        "mitigationStatusDescription": "Not mitigated",
        "originatorProcess": "msedge.exe",
        "pendingActions": false,
        "processUser": "NETSKOPE\\mrai",
        "publisherName": "",
        "reachedEventsLimit": false,
        "rebootRequired": false,
        "rootProcessUpn": null,
        "sha1": "c216b4134e0bd47a048699c6d961be65ef5672b3",
        "sha256": null,
        "storyline": "4C7C7E773CBBC497",
        "threatId": "1860067293510813906",
        "threatName": "wildfire-test-pe-file (2).exe",
        "updatedAt": "2024-02-10T10:10:28.751389Z"
      },
      "whiteningOptions": [
        "hash",
        "path"
      ]
    }
  }
],
"pagination": {
  "nextCursor": "eyJpZF9jb2x1bW4iOiAiVGhyZWF0Vmlldy5pZCIsICJpZF92YWx1ZSI6IDE5MTk2MDc5NzI5NTA1NDcxNjMsICJpZF9zb3J0X29yZGVyIjogImFzYyIsICJzb3J0X2J5X2NvbHVtbiI6ICJUaHJlYXRWaWV3LnNpdGVfaWQiLCAic29ydF9ieV92YWx1ZSI6IDEyNjg0MTk0MjUxMTQ3MjE0ODYsICJzb3J0X29yZGVyIjogImFzYyJ9",
  "totalItems": 71
}
}
Push Indicators
API Endpoint:
https://
<SENTINEL TENANT>
/web/api/v2.1/sites
Method:
POST
Headers:
Key
Value
Authorization
ApiToken
<TOKEN>
User Agent
netskope-ce-6.0.1-cte-sentinelone-v1.4.0
Parameters
Key
Value
name
SITE NAME
Body
Key
Value
value
5cd04805f9753ca08b82e88c27bf5426d1d356bb26b281885573051048911367
type
sha256
source
Netskope CE |
<Source Plugin Name>
externalId
value
method
EQUALS
creationTime
2024-03-28T18:01:52.751130Z
validUntil
2025-03-28T18:01:52.751130Z
description
This is an test indicator.
{
    "data": [
        {
            "value": "27e13bc0fea2b1181b5fe763880262a65b9b9c4dd60533b933fe2e9d50fb84a5",
            "type": "SHA256",
            "source": "Netskope CE | MISP",
            "description": "This is a test indicator.",
            "method": "EQUALS",
            "externalId": "27e13bc0fea2b1181b5fe763880262a65b9b9c4dd60533b933fe2e9d50fb84a5",
            "creationTime": "2024-03-28T18:01:52.751130Z",
            "validUntil": "2025-03-28T18:01:52.751130Z"
        }
    ],
    "filter": {}
}
Sample API Response
{
    "data": [
        {
            "batchId": "atmtn00000001b533e1b531f362cc40dcb066",
            "category": [],
            "creationTime": "2024-03-28T18:01:52.751130Z",
            "creator": "tanushree.kurup@crestdatasys.com",
            "description": "This is a test indicator.",
            "externalId": "27e13bc0fea2b1181b5fe763880262a65b9b9c4dd60533b933fe2e9d50fb84a5",
            "intrusionSets": [],
            "metadata": "",
            "method": "EQUALS",
            "mitreTactic": [],
            "reference": [],
            "scope": "account",
            "scopeId": "1268419425097944269",
            "source": "Netskope CE | MISP",
            "threatActors": [],
            "type": "SHA256",
            "updatedAt": "2024-12-02T15:31:15.710467Z",
            "uploadTime": "2024-12-02T15:30:24.310837Z",
            "uuid": "07ca58e55bbc1e9505fdb03fdc8b463a",
            "validUntil": "2025-03-28T18:01:52.751130Z",
            "value": "27e13bc0fea2b1181b5fe763880262a65b9b9c4dd60533b933fe2e9d50fb84a5"
        }
    ]
}
Delete/Retract Indicators
API Endpoint:
/web/api/v2.1/threat-intelligence/iocs
Method:
DELETE
Headers
Key
Value
Authorization
ApiToken
<TOKEN>
Body
Key
Value
filter.value
164a6e6f39e8c707269c7e5d934d6a0d
Example
{
	"filter": {
        "value": "164a6e6f39e8c707269c7e5d934d6a0d"
    }
}
Sample API Response
{
"data": {
"affected": 1
}
}
Performance Matrix
Here is the performance reading conducted for fetching and pushing 100K IoCs on a Large Cloud Exchange instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from SentinelOne
~35k per minute
Indicators shared with SentinelOne
~50k per minute
User Agent
netskope-ce-6.0.1-cte-sentinelone-v1.4.0
Workflow
Add roles to a user.
Get your SentinelOne Management URL and API token.
Configure the SentinelOne Plugin.
Configure a Business Rule for SentinelOne.
Configure Sharing for SentinelOne.
Validate the SentinelOne Plugin.
Watch a Video
Click play to watch a video.
Add Roles to a User
To configure the SentinelOne plugin the user should have specific roles added. Follow these steps to add the necessary roles to your user.
Log in to your SentinelOne platform as an Admin user.
Go to
Settings > Users > Roles > Actions > New Role
.
Ent a Role Name and description, and add these Roles.
Accounts: view
Groups: view
Roles: view
Sites: view
Endpoint threats: view, Fetch Threat File
Threat Intelligence: view, Manage
Click
Save
. Your Role will be added, If the user already has some roles assigned make sure it has all these roles added to the existing roles.
If your user has no roles assigned to them, add the newly added roles to your user by following the next steps.
Go to
Console User
and click on your user Email. A popup box will open. Click
Actions > Change Scope of Access
.
Select the Role name created in the above steps and click
Save
.
Give the user permission to generate an API token.
Creating a new User in SentinelOne
First log in to an Admin account and go to
Settings
in the left panel.
Go to
Users > Actions > Add a new User
.
It will ask for Fullname and Email Address.
Note
Give a unique Email Address that does not exist in the instance.
Select the Scope of Access as Account, and select the role created in
Adding Roles to the User
.
Now it will send an Authentication email on the given Email Address.
Click on the link in the email to log in with that user.
Get your Management URL and API Token
Login to your SentinelOne platform.
Click on your username in the top right corner, and click My User.
Click
Actions > Api Token Operations > Regenerate API Token
(generate if not already generated). Save the token once generated since it will only be visible once.
As for the URL, use the SentinelOne platform URL as your Management URL for configuring the plugin.
Configure the SentinelOne Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
SentinelOne v1.4.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Interval to fetch data from this plugin source.
Aging Criteria:
Expiry time of the plugin in days. (Default: 90)
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation
: Enable/Disable SSL Certificate validation based on your platform requirement.
Use System Proxy
: Enable if the proxy is required for communication.
Click
Next
and enter the Configuration Parameters:
Management URL
: The SentinelOne Management URL.
Example:
https://user-partners.sentinelone.net
.
API Token
: API token to authenticate SentinelOne.
Site name
: Name of the site to fetch alerts from. Leave blank to fetch data from all sites.
User Type:
Select whether the API token provided is for a Global User or Account User.
Analyst Verdict:
Pull Indicators based on the Analyst Verdict field. The Indicators with the selected Analyst Verdicts will be fetched from the SentinelOne platform.
Retraction Interval (in days):
Retraction Interval days to run IoC(s) retraction for SentinelOne indicators. Note that this parameter will only be considered if
IoC(s) Retraction
is enabled in Threat Exchange Settings. Value must be from 1 to 2^62.
Enable Tagging:
Enable/Disable tagging functionality.
Initial Range (in days)
: Number of days to pull the data for the initial run. Value must be from 0 to 2^62.
Click
Save
.
Configure a Threat Exchange Business Rule for SentinelOne
To share indicators fetched from the SentinelOne to Cloud Exchange, you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule, follow these steps:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add a Rule name and your required filters for the IoCs you want to share, and then click
Save
.
Configure Sharing for Threat Exchange and SentinelOne
To share IoCs from the Cloud Exchange to the SentinelOne platform, or from SentinelOne to Netskope, follow these steps:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Netskope CTE), Business Rule, Destination Configuration (SentinelOne), and Target.
Click
Save
.
Follow the same steps but vice versa for sharing SentinelOne IoCs to Netskope, select your Source Configuration as SentinelOne, Business Rule, Destination Configuration (Netskope CTE), and Target, and select the existing IoC List Name or create a new IoC list on the platform.
Click
Save
.
Validate the SentinelOne Plugin
Validate the Pull
Based on the Plugin configuration Indicators will pull from the SentinelOne. Go
Threat Exchange > Threat IoCs
to view the received IoCs.
Example:
Add a query on the Threat IoCs page like
“sources.source Is equal “CTE SentinelOne” && type IN (“<IOC_TYPE>”)”
.
You can also verify the indicators pulled in Cloud Exchange from the logs available at
Logging
.
In SentinelOne, go to
Incidents
from the left panel. Here in the Threats section, you can verify the indicators that are available for pull.
For verifying the Retracted IoCs from SentinelOne, check the logs for IoC Retraction example:
message Like “CTE SentinelOne [CTE SentinelOne] [Retraction]:”
SentinelOne plugin also supports push retraction which means the IoCs from third party plugins that are shared to the SentinelOne plugin and later were marked as retracted in Cloud Exchange, then those IoCs will be automatically deleted from SentinelOne platform through push retraction. You can verify the same by observing the Retraction Result field, which says
“<plugin configuration name>: retracted”
.
When the IoCs shared from SentinelOne to Third Party are deleted from that platform, then it will be marked as
“<plugin-config-name>: retracted”
in the Retraction Result. If they are not deleted from the Third party then the Retraction Result will be pending.
Note
The plugin also supports retraction based on the Analyst Verdict field. If the Analyst Verdict of an indicator is updated and the new value is not included in the plugin configuration, that indicator will be marked as retracted.
IoCs pulled from SentinelOne were shared to a File Hash of a File named
Sentinelone-demo
on the Netskope Tenant.
If any of the shared IoCs are marked as retracted in Cloud Exchange, it would be deleted from the Netskope tenant as well. Here, you can see the IoCs which were marked Retracted =
Yes
in the retraction screenshot, were also deleted from the File Hash on the Netskope tenant.
Validate the Push
To verify sharing indicators, go to
Threat Exchange > Threat IoCs
. Expand one of the Source plugin IoCs and check the status of Shared with Parameter.
For more information go to
Logging
from the nav bar and check the plugins logs.
Note
The shared indicators to SentinelOne lack a UI dashboard for viewing. However, we can utilize the API to see the ingested indicators.
Sample CURL:
curl --location 'https://usea1-partners.sentinelone.net/web/api/v2.1/threat-intelligence/iocs?limit=1000' \--header 'Authorization: ApiToken TOKEN' \--header 'Content-Type: application/json'
Run the provided CURL command in the Postman or any other API platform to verify the shared indicators. Also, you can add a filter of value/type/source in the params.
Note
The IoCs of types domain, host name and FQDN in Cloud Exchange will be shared as DNS to the SentinelOne platform.
The source field will contain the source labeling of the source plugin.
Once the shared indicator is marked as retracted in the Cloud Exchange, it will also be retracted from the SentinelOne platform as this plugin also supports push retraction.
To verify the push retraction, go to
Logging
and apply filter as shown here:
You can also verify the retracted shared indicator at
Threat IoCs
.
After the retraction is completed, you can verify the retraction on SentinelOne by running the CURL command again with the indicator value.
Troubleshooting the SentinelOne Plugin
Unable to pull IoCs from the SentinelOne platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of the following.
No IoCs are available on the platform to pull.
IoCs are not available for the given time range or do not match the configuration parameters.
What to do:
Identity your root cause from above and follow these steps to resolve the issue.
No IOCs are available on the platform to pull
Check if the IoCs are available on the platform to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the SentinelOne platform, check if you have data for the given time range.
If the data is available for the given time range, it might be possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values in the plugin Configuration Parameters, and filter the same on the SentinelOne platform.
Unable to push IoCs to the SentinelOne platform
If you are not able to share IoCs from Cloud Exchange to SentinelOne, that could be due to the user may not have required permissions.
What to do:
Check if the permissions given to the user fulfills the
required permissions.
Unable to verify shared IoCs on SentinelOne using the API provided in the plugin
If you have shared IoCs on SentinelOne, and trying to verify it using the API provided in the plugin, and getting the below response:
{
"errors": [
{
"code": 4030010,
"detail": "This page doesn't support multi-scopes users yet",
"title": "Insufficient permissions"
}
]
}
This might be due to the user whose token is being used has access to multiple site scopes, rather than being limited to a single application scope.
What to do
: Update the user scope with the Application scope as given in
Adding Roles to the User
section.
False Positive IoCs fetched from the plugin
If False Positive indicators are being fetched by the plugin, it could be due to one of the following reasons:
The configured plugin version is v1.3.0 or earlier
If the plugin version is v1.4.0 or newer, the False Positive value may have been selected in the Analyst Verdict field.
What to do:
If you are using plugin version v1.3.0 or earlier, upgrade to the latest version and ensure that the False Positive value is not selected in the Analyst Verdict field. Globally enable the Retraction toggle in the Threat Exchange settings and provide the values in the Retraction interval of the plugin.
If the plugin is already upgraded, edit the plugin configuration and manually remove the False Positive value from the Analyst Verdict field.
In this Topic
SentinelOne Plugin for Threat Exchange

---
## ServiceNow Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/servicenow-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:49:34+00:00
**Scraped:** 2026-08-11T07:18:52.690267+00:00

ServiceNow Plugin for Threat Exchange - Netskope Technical Documentation
ServiceNow Plugin for Threat Exchange
This document explains how to configure the ServiceNow Threat Intelligence Plugin integration with the Cloud Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows for sharing of URLs and file hashes with Netskope that has been identified by ServiceNow.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Threat prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A ServiceNow instance with admin access.
Workflow
Create a custom File Profile.
Create a Malware Detection Profile.
Create a Real-time Protection Policy.
Create a Service Now user.
Configure a ServiceNow Plugin.
Configure sharing between Netskope and ServiceNow.
Validate the ServiceNow Plugin.
Click play to watch a video.
Create a Secure Web Gateway Custom File Profile
In the Netskope UI, go to
Policies
, select
File
, and click
New File Profile
.
Click
File Hash
in the left panel, select
SHA256
from the File Hash dropdown list.
Enter a temporary value in the text field. Netskope does not support progressing without having a value in this field, and recommends entering a string of 64 characters that consists of the character
f
. For example,
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
. This will have a very low possibility of matching a valid file format.
Click Next
.
Enter a Profile Name and a Description. We recommend not having blank spaces in your profile name; use underscores for spaces.
Click
Save
.
To publish this profile into the tenant, click
Apply Changes
in the top right.
Create a Malware Detection Profile for ServiceNow
In the Netskope UI, go to
Policies
, select
Threat Protection
, and click
New Malware Detection Profile
.
Click
Next
.
Note
For this configuration example, we will be using the intelligence for this list as a block list. Netskope does support inclusion of both allow and block lists in the threat profiles.
Click
Next
again.
Select the File Profile you created in the previous section and click
Next
.
Enter a Malware Detection Profile name and click
Save Malware Detection Profile
.
To publish this profile in the tenant, click
Apply Changes
in the top right.
Create a Real-time Threat Protection Policy for ServiceNow
In the Netskope UI, go to
Policies > Real-time Protection
.
Note
The policy configured here is just an example. Modify as appropriate for your organization.
Click
New Policy
and select
Threat Protection
.
For
Source
, leave the default (User = All Users)
For
Destination
: select
Category
The Category section expands and allows you to search and select categories. Click
Select All
.
When finished, click outside of the Category section.
When the Activities & Constraints section opens, click
Edit
.
Select
Upload
and
Download
, and then click
Save
.
For
Profile & Action
, click in the text field.
Select the Malware Detection profile you created in the previous section.
For the Severity Levels, change all of the Actions settings from
Action: Alert
to
Action: Block
.
Select a template to choose which block message is sent to the user.
For
Set Policy
, enter a descriptive Policy Name.
Click
Save
in the top right to save the policy.
Choose the
To the top
option when it appear. (Or appropriate location in your security policy)
To publish this policy into the tenant, select
Apply Changes
in the top right.
Get the ServiceNow User ID and Password
Log in to your ServiceNow Instance with admin access.
Go to
System Security > Users and Groups > Users.
Click
New.
Enter the required information and make note of the
User ID
and
Password.
Click
Submit
.
On the
Roles
tab, click
Edit…
.
Add the
sn_ti.observable.admin
role and click
Save
.
Configure the ServiceNow Plugin
In Cloud Exchange, go to
Settings
and click
Plugins
.
Search for and select the
ServiceNow
plugin box to open the plugin creation page.
Enter the Configuration Name. >
Adjust the Sync Interval to appropriate value: Suggested is 5+ minutes.
Click
Next
.
Enter your ServiceNow Instance URL.
Enter the Username and Password you obtained when creating a ServiceNow user.
Enter an Initial Range (in days) to fetch indicators.
Click
Save
.
Configure Sharing for Netskope and ServiceNow
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
, and in the Source Configuration dropdown list, select
ServiceNow
.
Select a Business Rule, and then select
Netskope
for the Destination Configuration. Sharing configurations are unidirectional. data obtained from one plugin is shared with another plugin. To achieve bi- or multi-directional sharing, configure each separately.
Select a Target. Each plugin will have a different target or destination for the IoC.
Click
Save
.
Repeat steps 2-5, but select
Netskope
as the Source Configuration and
ServiceNow
as the Destination Configuration.
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Note
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin
API Source
, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect.
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Modify, Test, or Delete a Sharing Configuration
Each configuration supports 3 actions:
Edit the rule by clicking on the pencil icon.
Test the rule by clicking on the synchronization icon. This tests how many IoC will actually be sent to the destination system based on the timeframe and the rule.
Delete the rule by clicking on the garbage can icon.
Validate the ServiceNow Plugin
In order to validate the integration you must have Netskope Alerts and/or MISP attributes/indicators. Polling Intervals are defined during plugin configuration
Go to
Threat Exchange > Threat IoCs
.
In your Netskope tenant, go to
Policies > File
, select your custom File Profile, and then click
File Hash
.
In your ServiceNow Console, click
Threat Intelligence > Observables
.
If data is not being brokered between the platforms, you can look at the audit logs in Cloud Exchange. In Cloud Exchange, click
Logging
and look through the logs for errors.
In this Topic
ServiceNow Plugin for Threat Exchange

---
## Skyhigh Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/skyhigh-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:49:58+00:00
**Scraped:** 2026-08-11T07:18:53.898558+00:00

Skyhigh Plugin for Threat Exchange - Netskope Technical Documentation
Skyhigh Plugin for Threat Exchange
This document explains how to configure the SkyHigh integration with the Cloud Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows for the pulling of URLs and sharing them with Netskope.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the following host: SkyHigh expects a publically available URL that holds a flat file in Blue Coat format. Example:
Define category Blacklist1
1800covidx.com
18713279151.com
End
Define category Blacklist2
18statement.coronaviruspreppers.buzz
19covid-gouv12.com
End
Your Configuration Parameter. Reach out to Skyhigh for your Skyhigh CASB Published URL. Make sure you have access to the URL. It is assumed that the URL is publically available, so you do not need any extra permissions to pull data.
Skyhigh Plugin Support
Fetched indicator types
URL(URLs, FQDN, IP Addresses)
Shared indicator types
Do not support sharing
Performance Matrix
Data Pulled
Time Taken
1326
4 seconds
11323
1 minute 39 seconds
Workflow
Configure the SkyHigh Plugin for Threat Exchange.
Validate the Skyhigh plugin.
Click play to watch a video.
Configure the Skyhigh Plugin for Threat Exchange
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the SkyHigh plugin box.
Enter these parameters:
Configuration Name: Unique name for the configuration.Sync Interval: Leave Default.Aging Criteria: Leave Default.Override Reputation: Leave Default.Enable SSL verification: Enable if SSL verification is required for communication.Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter these parameters:
SyHigh CASB Published URL: SkyHigh published URL endpoint from which you want to pull the data.Category: The type of comma-separated category from which you want to pull data. Keep it blank to pull all data from the file.
Click
Save
.
Validate the Skyhigh Plugin
In Threat Exchange, go to
Threat IoCs
.
If data is not being fetched from the platform, you can look at the logs in Cloud Exchange. In Cloud Exchange Select Logging. Look through the logs for errors.
In this Topic
Skyhigh Plugin for Threat Exchange

---
## Sophos Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/sophos-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:50:33+00:00
**Scraped:** 2026-08-11T07:18:59.007317+00:00

Sophos Plugin for Threat Exchange - Netskope Technical Documentation
Sophos Plugin for Threat Exchange
This document explains how to configure the Sophos integration with the Cloud Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches the SHA256 type of threat indicator from Threat Graphs under Threat Analysis Center in the Sophos platform. This plugin does not support sharing of indicators to the Sophos platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Threat Prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Sophos instance.
A Service Principal ReadOnly user that can fetch the events using SIEM API.
Sophos Plugin Support
Fetched indicator types
SHA256
Workflow
Get your Sophos Client ID and Client Secret.
Configure the Sophos plugin.
Configure Sharing for Netskope and Sophos.
Validate the Sophos Plugin.
Click play to watch a video.
Get your Sophos Client ID and Client Secret
Log in to your Sophos Account.
Go to Global Settings and click
API Credentials
.
Enter a name for your credential set and a description, and then click
Add
.
Click
Copy
to save the Client ID, and then click
Show the Client Secret
to unhide the value.
Click
Copy
to save the Client Secret. These two values are needed for the Sophos plugin configuration.
Configure the Sophos Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
Sophos
plugin box to open the plugin creation page.
Enter a Configuration Name.
Adjust the Sync Interval to the appropriate value: Suggested is 5+ minutes.
Enter an Aging Criteria.
Adjust the Override Reputation to the appropriate value.
Click
Next
.
Enter your Sophos Client ID and Client Secret.
Click
Save
.
Configure Sharing for Netskope and Sophos
In Threat Exchange, go to
Sharing
.
Click
Add Sharing Configuration
.
For Source Configuration, select the Sophos plugin you just created.
Select an appropriate Business Rule from the dropdown.
For Destination Configuration, select
Netskope
.
For Target, select
Add to File Hash List
from the dropdown and enter a name and size.
Click
Save
.
In this Topic
Sophos Plugin for Threat Exchange

---
## STIX/TAXII Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/stix-taxii-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:50:09+00:00
**Scraped:** 2026-08-11T07:19:00.244013+00:00

STIX/TAXII Plugin for Threat Exchange - Netskope Technical Documentation
STIX/TAXII Plugin for Threat Exchange
This document explains how to configure the STIX/TAXII v3.2.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches IoCs of type Domain, URL and Hash (MD5 and SHA256) for version 1.1 and IOCs of type Domain, URL, IPv4, IPv6, and Hash (MD5 and SHA256) for version 2.1/2.2 from the TAXII feeds and extracts observables from them. This plugin supports retraction of IoCs pulled from TAXII feeds. This plugin does not support sharing of indicators to TAXII feeds.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Secure Web Gateway subscription for URL sharing.
A STIX/TAXII server to pull indicators.
STIX/TAXII API credentials details. Contact STIX/TAXII support for an appropriate Discovery URL/API Root URL.
Connectivity to STIX/TAXII Partner login URL.
STIX/TAXII Plugin Support
This plugin is used to fetch IoCs of type Domain, URL, and Hash (MD5 and SHA256) for version 1.1 and IoCs of type Domain, URL, IPv4, IPv6, and Hash (MD5 and SHA256) for version 2.1/2.2 from the TAXII feeds and extracts observables from them. This plugin supports retraction of IoCs pulled from TAXII feeds. This plugin does not support sharing of indicators to TAXII feeds.
Fetched Indicator Types
Shared Indicator Types
URL, Domain, IPv4, IPv6, and Hash (MD5 and SHA256)
Not Supported
Mappings for Pulled IoCs
For version 1.1
Cloud Exchange Fields
STIX/TAXII Fields
value
ioc_value
type
ioc_type
comments
observable.description or indicator.description or “Valid From: 2025-12-16T07:04:38.935940Z, Valid Until: 2025-12-16T07:04:38.935940Z” or “”
firstSeen
firstseen
lastSeen
lastseen
reputation
Indicator.confidence.value (Default 5)
severity
Indicator.likely_impact.value (Default UNKNOWN)
For version 2.x
Cloud Exchange Fields
STIX/TAXII Fields
Value
ioc_value
Reputation
int(o.get(“confidence”, 50) / 10)
Comments
o.get(“description”) or o.get(“pattern”) “Valid From: 2025-12-16T07:04:38.935940Z, Valid Until: 2025-12-16T07:04:38.935940Z” or “”
Firstseen
created_time
Lastseen
modified_time
Permissions
Permissions may vary from platform to platform. For the XSOAR platform, you will need an Administrator role.
API Details
This plugin uses Python libraries to fetch objects from the STIX/TAXII version 1x and 2x.
STIX/TAXII version 1x: cabby (https://pypi.org/project/cabby/)
STIX/TAXII version 2x: taxii2client (https://pypi.org/project/taxii2-client/)
Usage of libraries:
Cabby:
1) Client creation:
from cabby import create_client
client = create_client(
base,
port=port,
use_https=True,
discovery_path=discovery_url,
)
2) Fetch collections:
client.get_collections(uri=collection_uri)
3) Poll objects:
content_blocks = client.poll(
collection_name=collection,
begin_date=start_time,
)
Taxii2client:
1) ApiRoot object creation:
apiroot = ApiRoot21(
configuration["discovery_url"].strip(),
user=username,
password=password,
verify=self.ssl_validation,
proxies=self.proxy,
)
2) Fetch collections:
collections = apiroot.collections
3) Fetch objects:
pages = as_pages21(
func,
per_request=batch_size,
added_after=start_time,
next=next,
with_header=True,
headers=headers
)
Performance Matrix
Here are the performance readings conducted for fetching 100K IoCs in each plugin lifecycle on a Large Cloud Exchange instance with the below specifications.
A XSOAR TAXII server was used to pull data.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched via STIX/TAXII plugin
~3k per minute
User Agent
netskope-ce-6.0.0-cte-stix/taxii-v3.2.0
Workflow
Get your Discovery URL/API Root URL, username, and password.
Configure the STIX/TAXII plugin.
Configure a Business Rule.
Configure Sharing.
Validate the plugin.
A XSOAR TAXII server was used to pull data in these instructions.
Watch a Video
Click play to watch a video:
Configure the TAXII2 Server
Log in to the XSOAR server.
Click
Settings > Integrations > Instances
.
Search for
Taxi
and click
Add Instance
.
Enter the following information:
Name
: Enter the STIX/TAXII name.
TAXII2 Server version:
2.1 or 2.0.
Listen Port:
The port on which you want to send feeds.
Username:
The user name for the STIX server(This will be required when configuring plugin).
Password:
The password for stix server(This will be required when configuring plugin).
Collection JSON:
Collection name for Stix.
Response Size:
The size of the response you want to receive from the server. Note that Netskope Cloud Exchange only supports pulling up to a size of 1000 ICs.
Note
Example for Collection JSON:
{
"url_collection": {
"query": "type: URL",
"description": "This is a test collection"
},
"hashes_collection": {
"query": "type: File",
"description": "This is a test collection"
},
"domain_collection": {
"query": "type: Domain",
"description": "This is a test collection"
},
"IPv4_collection": {
"query": "type:IP",
"description": "Collection of IPv4 indicators for internal network analysis"
},
"IPv6_collection": {
"query": "type:IPv6",
"description": "Collection of IPv6 indicators for external threat tracking"
}
}
Click
Save
. For more information, see:
https://xsoar.pan.dev/docs/reference/integrations/taxii2-server
.
Configure the STIX/TAXII Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
STIX/TAXII v3.2.0 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name
: Plugin configuration name.
Sync Interval
: Interval to fetch data from this plugin source.
Aging Criteria:
Expire indicators after a specific time.
Override Reputation
: Set value to override reputation of indicators received from this configuration. Leave empty to keep default(Default value will be 5).
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. These configuration parameters determine how tags are stored for indicators pulled for this configuration.
Enable SSL Validation
: Enable/Disable SSL Certificate validation.
Use System Proxy
: Use system proxy configured in Settings.
Click
Next
and enter the Configuration Parameters:
STIX/TAXII Version:
Select STIX/TAXII Version as per your instance.
Discovery URL/API Root URL
: Discovery/Feed URL of TAXII server for version 1.x and API Root URL for version 2.x. Contact your STIX/TAXII support for appropriate Discovery URL/API Root URL.
Username
: Username required for authentication, if any.
Password:
Password required for authentication, if any.
Collection Names:
Comma separated collection names from which data needs to be fetched. Leave empty to fetch data from all of the collections.
Format:
“<collection1>,<collection2>,<collection3>”
Initial Range
: Number of days to pull the data for the initial run.
Look Back (in minutes):
Number of minutes to backdate the start time for pulling the data. Valid value is anything between 0 to 1440.
Type of Threat data to pull
: Type of Threat data to pull. Note: IPv4/IPv6 is only supported for STIX/TAXII version 2.x.
Severity:
Only indicators with matching severity will be fetched. STIX/TAXII version 2.x only supports Unknown severity, thus to pull data using STIX/TAXII version 2.x it is mandatory to select ‘Unknown’ in the severity field. Refer to
Troubleshooting
if you face any issue while pulling IOCs.
Reputation:
Only indicators with reputation equal to or greater than this will be saved in Netskope Cloud Exchange.
Pagination Method:
Pagination Method to use while pulling the indicators. Contact your STIX/TAXII support to choose the appropriate option.
Batch Size:
Number of indicators to fetch per bundle. Must be an integer in range 1 to 1000.
Retraction Interval (in days):
Number of days to look back for retraction checks. Leave empty to disable retraction. Must be an integer in range 0 to 365.
Note
There will be only the
Unknown
severity available in the configuration parameters for 2.x version.
The range for Batch Size is 1 to 1000 for 2.1 version and 2 to 1000 for 2.0 version.
For 1.1 version, the Batch Size configuration parameter will not be there.
Click
Save
.
Add a Threat Exchange Business Rule for STIX/TAXII
The business rule is used to filter out the indicators that are to be shared. To share IOCs with any third-party plugin, you need to create a business rule:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the rule name and select the fields through which you want to filter the IoCs.
Click
Save
.
Add Threat Exchange Sharing for STIX/TAXII
To configure the sharing:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select a Source configuration (source from which you want to share data), a Business Rule, and a Destination configuration.
Select the target value and action type.
Click
Save
.
Note that the STIX/TAXII plugin does not support sharing of indicators to TAXII feeds.
Validate the STIX/TAXII Plugin
Validate the Pull
Indicators stored in Cloud Exchange can be verified in Threat Exchange at
Threat IoCs
. Search the STIX/TAXII IOCs by filtering indicators from STIX TAXII plugin.
Example: Add a query on the Threat IoCs page like
“sources.source Is equal “CTE STIX TAXII” && type IN (“<IOC_TYPE>”)”
You can also verify the indicators pulled in Cloud Exchange from the logs available at
Logging
.
To verify whether IoCs are present on XSOAR platform, log in to your instance and go to
Indicators
.
Troubleshooting the STIX/TAXII Plugin
Unable to configure the STIX/TAXII plugin
If you are unable to configure the plugin, it might be due to one of these reasons:
Invalid Discovery URL/API Root URL.
Invalid Username or password.
Getting the below error while configuring the plugin:
CTE STIX/TAXII [CTE STIX TAXII]: Could not fetch the collection list from the server. Error: ('Connection broken: IncompleteRead(586 bytes read)', IncompleteRead(586 bytes read))
Getting error while configuring the plugin with on-premise instance for STIX/TAXII version 1.1.
What to do:
Verify the Discovery URL/API Root URL that you are using is correct. If you are not sure about the Discovery URL/API Root URL, then contact your STIX/TAXII support team for respective platforms.
Verify the username and password. They must be the same as the one used while configuring the TAXII server.
Verify the collection JSON provided in the STIX server. It must be as provided in the
plugin configuration
.
Might be due to the host not added in the container. To add the host, follow the below steps:
SSH to the VM where your Cloud Exchange is installed and stop all the containers using “sudo ./stop” script.
Edit your docker-compose file using command “vi docker-compose.yml”.
Add extra hosts under the core section.
Format:
extra_hosts: "
<your domain>
:
<your ip>
"
Save the file.
Start the Netskope Cloud Exchange using command
sudo ./start
.
Configure the plugin with your valid credentials for an on-premises setup.
Note
Use domain and IP of the server where your STIX/TAXII instance is hosted.
Unable to pull data with the STIX/TAXII plugin
If you are facing an issue while pulling the data via the STIX/TAXII plugin, it might be due to one of these reasons:
No data present on the 3rd party platform.
It may be due to the filters selected while configuring the plugin.
What to do:
Verify whether the IoCs are present on your platform. In the case of the XSOAR platform, you can verify it on the
Indicators
page.
Data matching the filter provided in the configuration parameters will be stored. For example for the Severity filter, only indicators with matching severity will be fetched. STIX/TAXII version 2.x only supports the
Unknown
severity, so to pull data using STIX/TAXII version 2.x, it is mandatory to select
Unknown
in the severity field. If the severity filter is having all values except
Unknown
severity, then no indicators will be stored in Netskope Cloud Exchange, and you will be able to see the logs for pulling at
Logging
.
Getting an error while enabling the plugin after a plugin upgrade
When you upgrade the STIX/TAXII plugin to the latest version, and you use the skip button while upgrading, then by default the plugin will be in disabled state, and Type of Threat data to pull field will have an older value, so you will face this error while enabling that plugin.
07/29/2025 12:19:48 PM
–
error
CTE STIX/TAXII [CTE STIX]: Invalid value for Type of Threat data to pull provided in configuration parameters. Available values are ‘sha256’, ‘md5’, ‘url’, ‘ipv4’, ‘ipv6’, ‘domain’.
What to do:
If you are unable to enable the plugin after plugin upgrade, then edit the plugin and make sure that Type of Threat data to pull is has a valid value. After the plugin upgrade, you need to manually remove the old values for Type of Threat data to pull the field, and add new values from the available list.
Supported types are as below:
Known Behaviors
We have observed that if the user upgrades the freshly configured plugin from an older version to STIX/TAXII v3.1.0, and if the initial run is not executed, then the plugin will not pull any IoCs for the range provided in the initial run.
Only the data matching the filter provided in the configuration parameters will be stored. For example, if Severity filter is having all values except the Unknown severity, then no indicators will be stored in Cloud Exchange still you will be able to see the logs for pulling in the Logging page.
Limitation
The
Last Run At
plugin configuration parameter displayed while editing the plugin configuration will be not useful for STIX/TAXII v2.x (As we have implemented a circuit breaker).
In this Topic
STIX/TAXII Plugin for Threat Exchange

---
## Threat Exchange Module
**URL:** https://docs.netskope.com/en/threat-exchange-module/
**Last Modified:** 2026-06-02T18:38:13+00:00
**Scraped:** 2026-08-11T07:19:09.917492+00:00

Threat Exchange Module - Netskope Technical Documentation
Threat Exchange Module
Threat Exchange is a rules-based engine for collecting and sharing indicators related to file hashes of malicious software (malware), file hashes of files used in Netskope DLP policy for absolute matching, or URLs used by plugged in systems for policy enforcement of restricted or allowed access.
Click play to learn how to set up Threat Exchange.
Threat Exchange Global Settings
Only write-access users can change Threat Exchange Global Settings.
Go to Settings > Threat Exchange
. If the same IoC value is reported from different sources, then based on the reconciliation criteria, Threat Exchange will decide which IoC metadata should be kept and which will be ignored.
Reconciliation Criterias
Possible Reconciliation Criterias include:
Always Overrides: If this criteria is selected, the latest IoC metadata will be kept in case of IoC Duplication.
Never Overrides: If this criteria is selected, the oldest IoC metadata will be kept in case of IoC Duplication.
Highest Severity Source Override: If this criteria is selected, the highest severity source’s IoC metadata will be kept in case of IoC Duplication.
Click play to watch a video.
IoC(s) Retraction
To enable IoC retraction from Cloud Exchange:
Go to
Setting > Threat Exchange
.
Enable the IoC(s) Retraction toggle and enter the Retraction Interval.
Click
Save
.
Configure 3rd-party Threat Exchange Plugins
View Configured Threat Exchange Plugins
Update Configured Threat Exchange Plugins
Manage Threat Exchange Business Rules and IoC Sharing
Configure your Netskope Tenant for Threat Exchange File Hash Sharing
Manage Tags
Threat Exchange Custom Plugin Developers Guide
In this Topic
Threat Exchange Module

---
## ThreatConnect Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/threatconnect-plugin-for-threat-exchange/
**Last Modified:** 2026-05-28T00:23:08+00:00
**Scraped:** 2026-08-11T07:19:11.238644+00:00

ThreatConnect Plugin for Threat Exchange - Netskope Technical Documentation
ThreatConnect Plugin for Threat Exchange
This document explains how to configure the v1.2.1 ThreatConnect plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. The ThreatConnect plugin is used to pull IoCs of type File (MD5 and SHA256), URL, Host and Address (IPv4 and IPv6) from the Indicators under the Intelligence Requirements from ThreatConnect. This plugin also supports sharing File (MD5 and SHA256), URL, Host and Address (IPv4 and IPv6) to the ThreatConnect’s Group under the Intelligence Requirements using the Add to Group action.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Threat Prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A ThreatConnect instance.
Connectivity to the following host:
http://partnerstage.threatconnect.com/
.
ThreatConnect Plugin Support
This plugin is used to pull IoCs of types File (MD5 and SHA256), URL, Host and Address (IPv4 and IPv6) from the Intel Requirements from ThreatConnect. This plugin also supports pushing File (MD5 and SHA256), URL, Host and Address (IPv4 and IPv6) to ThreatConnect’s Intel Requirements. This plugin supports performing actions such as
Add to Group
.
Fetched indicator types
URL, Host, Address (IPv4, IPv6) SHA256, MD5
Shared indicator types
URL, Host, Address (IPv4, IPv6) SHA256, MD5
Permissions
To create an API user make sure you have the organization administrator role of the Organization Administrator for creating an API User for getting the Access ID and the Secret Key.
To pull and push data from/to ThreatConnect make sure your user has these rights
Functionality
API Endpoint
Request Type
Permissions
Pull Indicators
/api/v3/indicators?
GET
Select any one of the following:
– App Developer
– Organization Administrator
– Read Only Commenter
– Read Only User
– Sharing User
– Standard User
List Groups
/api/v3/groups/
GET
Select any one of the following:
– App Developer
– Organization Administrator
– Read Only Commenter
– Read Only User
– Sharing User
– Standard User
Create Group
/api/v3/groups/
POST
Select any one of the following:
– App Developer
– Organization Administrator
– Sharing User
– Standard User
Push Indicators
/api/v3/indicators
POST
Select any one of the following:
– App Developer
– Organization Administrator
– Sharing User
– Standard User
Get Owner
/api/v2/owners/mine
GET
Select any one of the following:
– App Developer
– Organization Administrator
– Read Only Commenter
– Read Only User
– Sharing User
– Standard User
API Details
List of APIs used
API Name
Method
API Endpoint
Pull Indicators
GET
/api/v3/indicators?
List Groups
GET
/api/v3/groups/
Create Group
POST
/api/v3/groups/
Push Indicators
POST
/api/v3/indicators
Get Owners Mine
GET
/api/v2/owners/mine
Get Owners
GET
/api/v3/security/owners
Update Indicators
PUT
/api/v3/indicators/{value}
Pull Indicators
API Endpoint:
/api/v3/indicators
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC
<Token>
Timestamp
Unix Epoch of current date and time.
Query Parameters:
Parameter
Value
typeName IN
(“File”, “URL”, “Host”, “Address”,)
lastModified
String representation of Datetime in %Y-%m-%dT%H:%M:%SZ Format.
sorting
lastModified asc
fields
tags, associatedGroups, associatedArtifacts, associatedCases, securityLabels
resultStart
0
resultLimit
1000
Sample API Response:
{
    "data": [
        {
            "id": 152710117,
            "dateAdded": "2024-08-08T06:27:09Z",
            "securityLabels": {
                "data": [
                    {
                        "id": 1,
                        "name": "TLP:WHITE",
                        "description": "This security label is used for information that carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release.",
                        "color": "FFFFFF",
                        "owner": "System",
                        "dateAdded": "2016-08-31T00:00:00Z"
                    }
                ]
            },
            "ownerId": 252,
            "ownerName": "Netskope",
            "webLink": "https://partnerstage.threatconnect.com/#/details/indicators/152710117/overview",
            "tags": {
                "data": [
                    {
                        "id": 847399,
                        "name": "ABC",
                        "lastUsed": "2024-09-02T06:55:38Z"
                    }
                ]
            },
            "type": "Address",
            "lastModified": "2024-08-08T07:18:07Z",
            "rating": 4.00,
            "confidence": 84,
            "summary": "199.236.195.220",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 21946425,
                        "dateAdded": "2023-11-07T13:21:08Z",
                        "ownerId": 252,
                        "ownerName": "Netskope",
                        "webLink": "https://partnerstage.threatconnect.com/#/details/groups/21946425/overview",
                        "type": "Incident",
                        "name": "Netskope07112023",
                        "createdBy": {
                            "id": 781,
                            "userName": "02719309203714980821",
                            "firstName": "tco110",
                            "lastName": "netskopce",
                            "pseudonym": "APIUser9zYN7",
                            "owner": "Netskope"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "status": "None",
                        "lastModified": "2024-08-08T07:18:07Z",
                        "legacyLink": "https://partnerstage.threatconnect.com/auth/incident/incident.xhtml?incident=21946425"
                    }
                ]
            },
            "associatedCases": {
                "data": [
                    {
                        "id": 55,
                        "xid": "9b7789f5-f028-4972-977d-67051f3795ac",
                        "name": "yASdg",
                        "description": "sdfsdfs",
                        "dateAdded": "2022-04-20T08:20:37Z",
                        "lastUpdated": "2024-09-02T06:53:30Z",
                        "caseOpenTime": "2022-04-20T08:20:37Z",
                        "caseOpenUser": {
                            "id": 484,
                            "userName": "milan.thummar@crestdatasys.com (deleted 2023-05-31)",
                            "firstName": "Milan",
                            "lastName": "Thummar (deleted 2023-05-31)",
                            "pseudonym": "Milan Thummar (deleted 2023-05-31)",
                            "owner": "Netskope"
                        },
                        "status": "Open",
                        "severity": "Critical",
                        "resolution": "Not Specified",
                        "assignee": {
                            "type": "User",
                            "data": {
                                "id": 484,
                                "userName": "milan.thummar@crestdatasys.com (deleted 2023-05-31)",
                                "firstName": "Milan",
                                "lastName": "Thummar (deleted 2023-05-31)",
                                "pseudonym": "Milan Thummar (deleted 2023-05-31)",
                                "owner": "Netskope"
                            }
                        },
                        "createdBy": {
                            "id": 484,
                            "userName": "milan.thummar@crestdatasys.com (deleted 2023-05-31)",
                            "firstName": "Milan",
                            "lastName": "Thummar (deleted 2023-05-31)",
                            "pseudonym": "Milan Thummar (deleted 2023-05-31)",
                            "owner": "Netskope"
                        },
                        "owner": "Netskope",
                        "ownerId": 252
                    }
                ]
            },
            "associatedArtifacts": {
                "data": [
                    {
                        "id": 321,
                        "summary": "B055B13ACDCBD47240B9AA69DA6EB084B773DBAC344116ED0D2207FF558027B6",
                        "type": "File Hash",
                        "intelType": "indicator-File",
                        "source": "netskope",
                        "dateAdded": "2024-08-08T09:34:48Z",
                        "derivedLink": true,
                        "hashCode": "cF1Sl9pTga5xf2DhpM3wln447ZolLJ0As5e2W6i5Wmc="
                    },
                    {
                        "id": 320,
                        "summary": "Test Artifact",
                        "type": "User Agent",
                        "intelType": "indicator-User Agent",
                        "source": "netskope",
                        "dateAdded": "2024-08-08T09:28:50Z",
                        "derivedLink": true,
                        "hashCode": "XwI5ZkkEBvqtP5mY8ZovSaQwamZsL8LGR4eiKc4cNsA="
                    }
                ]
            },
            "ip": "199.236.195.220",
            "legacyLink": "https://partnerstage.threatconnect.com/auth/indicators/details/address.xhtml?address=199.236.195.220&owner=Netskope"
        }
    ],
    "status": "Success"
}
List Groups
API Endpoint:
/api/v3/groups
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC <Token>
Timestamp
Unix Epoch of current date and time.
Query Parameters:
Parameter
Value
tql
ownerName == <ownerName>
resultLimit
1000
Sample API Response:
{
    "data": [
        {
            "id": 10,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-10-21T19:54:59Z",
            "webLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=10",
            "type": "Document",
            "name": "Bad Document",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithOTI",
                "owner": "Demo Organization"
            },
            "upVoteCount":"0",
            "downVoteCount":"0",
            "fileName": "indicators.txt",
            "fileSize": 36,
            "status": "Success",
            "documentType": "Text",
            "documentDateAdded": "2021-10-21T19:54:59Z",
            "lastModified": "2022-03-09T12:44:04Z",
            "legacyLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=10"
        },
	]
}
Create a Group
API Endpoint:
/api/v3/groups
Method:
POST
Headers:
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC <Token>
Timestamp
Unix Epoch of current date and time.
Payload:
{
    "type": "Incident",
    "name": "Bad Incident",
    "tags": {
        "data": [
            {
                "name": "Netskope CEa"
            }
        ]
    }
}
Sample API Response:
{
    "data": {
        "id": 3,
        "ownerId": 1,
        "ownerName": "Demo Organization",
        "dateAdded": "2021-11-03T14:57:45Z",
        "webLink": "https://app.threatconnect.com/#/details/groups/3/overview",
        "type": "Incident",
        "name": "Bad Incident",
        "createdBy": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "owner": "Demo Organization"
        },
        "upVoteCount":"0",
        "downVoteCount":"0",
        "status": "New",
        "eventDate": "2021-11-03T00:00:00Z",
        "lastModified": "2021-11-03T14:57:4511:04:12Z",
        "legacyLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=3"
    },
    "message": "Created",
    "status": "Success"
}
Push Indicators
API Endpoint:
/api/v3/indicators
Method:
POST
Headers:
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC <Token>
Timestamp
Unix Epoch of current date and time.
Payload:
{
    "type": "Host",
    "hostName": "ultrabadguy.com",
    "associatedGroups": {
        "data": [
            {
                "id": 12
            }
        ]
    },
    "confidence": 85,
    "rating": 5,
    "tags": {
        "data": [
            {
                "name": "Netskope CE"
            }
        ]
    }
}
Sample API Response:
{
    "data": {
        "id": 4,
        "ownerId": 1,
        "ownerName": "Demo Organization",
        "dateAdded": "2021-11-05T16:43:17Z",
        "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
        "type": "Host",
        "lastModified": "2021-11-05T16:43:17Z",
        "rating": 5.00,
        "confidence": 85,
        "description": "This host is very dangerous",
        "summary": "ultrabadguy.com",
        "privateFlag": false,
        "active": true,
        "activeLocked": false,
        "hostName": "ultrabadguy.com",
        "dnsActive": true,
        "whoisActive": true,
        "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
    },
    "message": "Created",
    "status": "Success"
}
Get Owners Mine
API Endpoint:
/api/v2/owners/mine
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC <Token>
Timestamp
Unix Epoch of current date and time.
Sample API Response
{
  "status": "Success",
  "data": {
    "resultCount": 1,
    "owner": {
      "id": 1,
      "name": "Demo Organization",
      "type": "Organization"
    }
  }
}
Get Owners
API Endpoint:
/api/v3/security/owners
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC <Token>
Timestamp
Unix Epoch of current date and time.
Sample API Response:
{
	"data": [
		{
            "id": 1,
            "name": "Demo Organization",
            "type": "Organization",
            "ownerRole": "Organization Administrator",
            "permIndicator": "FULL",
            "permGroup": "FULL",
            "permPost": "FULL",
            "permTrack": "FULL",
            "permVictim": "FULL",
            "permAttribute": "FULL",
            "permApps": "BUILD",
            "permUsers": "FULL",
            "permSecurityLabel": "FULL",
            "permTag": "FULL",
            "permAttributeType": "FULL",
            "permSettings": "FULL",
            "permMembers": "READ",
            "permCopyData": "FULL",
            "permInvite": "FULL",
            "permTask": "FULL",
            "permCaseTag": "FULL",
            "permArtifact": "FULL",
            "permComment": "FULL",
            "permTimeline": "FULL",
            "permWorkflowTemplate": "FULL",
            "permPublish": "FULL",
            "permPlaybooksExecute": "FULL",
            "permPlaybooks": "FULL"
        },
	]
}
Update Indicator
API Endpoint:
/api/v3/indicators/{value}
Method:
PUT
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
Authorization
TC <Token>
Timestamp
Unix Epoch of current date and time.
Payload:
{
	"associatedGroups": {
		"data": [
			{"id": group_id},
		],
		"mode": "append",
	},
}
Sample API Response:
{
    "data": {
        "id": 4,
        "ownerId": 1,
        "ownerName": "Demo Organization",
        "dateAdded": "2021-11-05T16:43:17Z",
        "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
        "type": "Host",
        "lastModified": "2021-11-05T17:21:06Z",
        "rating": 5.00,
        "confidence": 92,
        "description": "This host is very dangerous",
        "summary": "ultrabadguy.com",
        "privateFlag": false,
        "active": true,
        "activeLocked": false,
        "hostName": "ultrabadguy.com",
        "dnsActive": false,
        "whoisActive": true,
        "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
    },
    "message": "Updated",
    "status": "Success"
}
Performance Matrix
Here is the performance reading conducted for fetching and sharing 100K IoCs in each plugin lifecycle on a Large CE instance with these specifications. The readings for pull are taken with keeping Enable Tagging as No. The readings for push were taken when the indicators being pushed were already present in the ThreatConnect platform and were updated with the push. If new indicators are pushed, the performance might see a positive impact
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from ThreatConnect
~10K per minute
Indicators shared to ThreatConnect
~150 per minute
User Agent
The user agent added for this plugin is in the following format:
netskope-ce-
<CE VERSION>
-
<MODULE NAME>
-
<PLUGIN NAME>
-v
<PLUGIN VERSION>
.
For example:
netskope-ce-5.0.1-cte-threatconnect-v1.2.1
.
Mappings
Default tags mapping for the Indicators pulled from the ThreatConnect platform.
Tag Mapping in Cloud Exchange based on IoC Type
Type of Indicator pulled from ThreatConnect
Tag added in Netskope CE for each type of indicator
URL
ThreatConnect-URL
Address(IPV4)
ThreatConnect-Address-IPV4
Address(IPV6)
ThreatConnect-Address-IPV6
Host
ThreatConnect-Host
File(MD5)
ThreatConnect-File-MD5
File(SHA256)
ThreatConnect-File-SHA256
Note
These tags will be created irrespective of enable tagging selected.
Pull Mappings
Netskope CE Fields
ThreatConnect Fields
Value
md5, sha256, text(URL), ip(Address), hostName(host)
Active
active
Severity
rating
Reputation
confidence
Comments
description
Firstseen
dateAdded
Lastseen
lastModified
Tags
Security Label-
+
Associated Group-
+
associatedCases.data.name +
Associated Artifacts-
+
Owner-
+
Private if privateFlag is True else Public +
tags
Note
For each value inside, data list tags will be created.
Push Mappings
Netskope CE Fields
ThreatConnect Fields
value
md5, sha256, text (URL), ip (Address), hostName (host)
type
url, File, Host, Address
Fetched existing_group_id
associatedGroups
Netskope CE
tags
severity
rating
reputation
confidence
Severity Mappings
Netskope CE Severity
ThreatConnect Severity
Unknown
0
Low
1
Low
2
Medium
3
High
4
Critical
5
Workflow
Create a custom File Profile.
Create a Malware Detection Profile.
Create a Real-time Protection Policy.
Get ThreatConnect credentials.
Configure a ThreatConnect Plugin.
Configure sharing between Netskope and ThreatConnect.
Validate the ThreatConnect Plugin.
Click play to watch a video.
Create a Secure Web Gateway Custom File Profile for ThreatConnect
In the Netskope UI, go to
Policies
, select
File
, and click
New File Profile
.
Click
File Hash
in the left panel, select
SHA256
from the File Hash dropdown list.
Enter a temporary value in the text field. Netskope does not support progressing without having a value in this field, and recommends entering a string of 64 characters that consists of the character
f
. For example,
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
. This will have a very low possibility of matching a valid file format.
Click Next
.
Enter a Profile Name and a Description. We recommend not having blank spaces in your profile name; use underscores for spaces.
Click
Save
.
To publish this profile into the tenant, click
Apply Changes
in the top right.
Create a Malware Detection Profile for ThreatConnect
In the Netskope UI, go to
Policies
, select
Threat Protection
, and click
New Malware Detection Profile
.
Click
Next
.
Note
For this configuration example, we will be using the intelligence for this list as a block list. Netskope does support inclusion of both allow and block lists in the threat profiles.
Click
Next
again.
Select the File Profile you created in the previous section and click
Next
.
Enter a Malware Detection Profile name and click
Save Malware Detection Profile
.
To publish this profile in the tenant, click
Apply Changes
in the top right.
Create a Real-time Threat Protection Policy for ThreatConnect
In the Netskope UI, go to
Policies > Real-time Protection
.
Note
The policy configured here is just an example. Modify as appropriate for your organization.
Click
New Policy
and select
Threat Protection
.
For
Source
, leave the default (User = All Users)
For
Destination
: select
Category
The Category section expands and allows you to search and select categories. Click
Select All
.
When finished, click outside of the Category section.
When the Activities & Constraints section opens, click
Edit
.
Select
Upload
and
Download
, and then click
Save
.
For
Profile & Action
, click in the text field.
Select the Malware Detection profile you created in the previous section.
For the Severity Levels, change all of the Actions settings from
Action: Alert
to
Action: Block
.
Select a template to choose which block message is sent to the user.
For
Set Policy
, enter a descriptive Policy Name.
Click
Save
in the top right to save the policy.
Choose the
To the top
option when it appear. (Or appropriate location in your security policy)
To publish this policy into the tenant, select
Apply Changes
in the top right.
Get your ThreatConnect Access ID and Secret Key
Log in to your ThreatConnect instance with an administrator account.
On the top navigation bar, hover the cursor over
Settings
and select
Org Settings
.
Go to the Organization Settings screen and click
Create API User
on the Membership tab.
The API User Administration window will be displayed. Enter these parameters:
First Name: Enter your first name.
Last Name: Enter your last name.
Organization Role: Select an Organization role.
Any of the following roles can be assigned to pull and push indicators:
App Developer.
Organization Administrator
Sharing User
Standard User
Include in Observations and False Positives: Select the checkbox to allow data provided by the API user to be included in observation and false-positive counts.
Allow User to Exceed API Link Limit: Select the checkbox to override the system-level limit on the number of association levels that can be retrieved at one time for intelligence items using v3 of the ThreatConnect API.
Custom TQL Timeout: Select the checkbox to override the system-level ThreatConnect Query Language (TQL)query timeout for the user. In the field to the right of the checkbox, enter the maximum amount of time, in milliseconds, that TQL queries made by the user will be allowed to run before timing out.
Note
This checkbox will be available only when the user creating the account has a System role of Operations Administrator or Administrator.
Disabled: Select the checkbox to disable an API user’s account in the event that the Administrator wishes to retain log integrity when the API user no longer requires ThreatConnect access.
Copy the Access ID and Secret Key, as these will not be accessible after the window is closed. These are required to configure the ThreatConnect plugin.
Click
Save
.
Configure the ThreatConnect Plugin
In Cloud Exchange, go to
Settings
and click
Plugins
.
Search for and select the
ThreatConnect v1.2.1 (CTE)
plugin box.
Enter and select the Basic Information on the first page:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave default.
Aging Criteria: Expiry time of the plugin in days. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if proxy is required for communication.
Click
Next
.
Enter the Configuration Parameters on the second page:
Base URL: Base URL for ThreatConnect API Endpoints –
https://
<yourcompany>
.threatconnect.com
Access ID: Access ID of ThreatConnect API.
Secret Key: Secret Key of ThreatConnect API.
Type of Threat Indicator: Type of threat IoC you want to pull from ThreatConnect.
Enable Tagging: Enable/Disable tagging functionality.
Enable Polling: Enable/Disable polling data from ThreatConnect.
Initial Range: Number of days to pull the data for the initial run.
Click
Save
.
Create a Business Rule for Sharing of Indicators
To share indicators from Cloud Exchange to ThreatConnect, and ThreatConnect’s indicators to Netskope, or any ThirdParty plugin, you need to have a business rule that will filter out the indicators that you need to share. To configure a business rule, follow these steps:
In Threat Exchange, click
Business Rules
and then
Create New Rule
.
Add your required filters for the IoCs you want to share.
Click
Save
.
Configure Sharing for Netskope and ThreatConnect
The ThreatConnect plugin supports sharing of URLs, MD5, and SHA256 types of IoCs. The plugin has an
Add to Group
action that will add indicators on ThreatConnect’s Intelligence Requirements. It will list all the available groups to which you can add your IoCs. To share IOCs to ThreatConnect follow these steps:
Go to
Threat Exchange
and select
Sharing
. The Sharing page displays the existing relationships for each sharing configuration in grid view as shown below. The Sharing page also has inputs to configure new sharing from one plugin to another.
Click
Add Sharing Configuration
, and in the Source Configuration dropdown list, select
Netskope CTE
.
Select a Business Rule, and then select
ThreatConnect
for the Destination Configuration. Sharing configurations are unidirectional. data obtained from one plugin is shared with another plugin. To achieve bi- or multi-directional sharing, configure each separately.
Select a Target. Each plugin will have a different target or destination for the IoC.
For Action, select Add to Group. The Add to Group action will add indicators to available groups in the organization. It will list out all the available groups in which you can add your IoCs. It will also show one last option as “Create New Group” which will create a new group in ThreatConnect and add all the indicators to that group.
Click
Save
.
Repeat steps 2-6, but select
ThreatConnect
as the Source Configuration and
Netskope CTE
as the Destination Configuration.
Click
Save
.
Adding a new sharing configuration on the active source poll will share the existing IoCs of the source configuration to the destination configuration. Whenever a new sharing configuration is built, all the active IoCs will also be considered for sharing if they match the source/destination combination.
Note
Plugins that do not have API for ingesting data cannot receive threat data. This is true of the installed plugin
API Source
, which provides a bucket associated with an API endpoint for remote 3rd-party systems to push data to. Once a Sharing policy has been added, it takes effect.
After a sharing configuration has been created, the sharing table will show the rule being invoked, the source system providing the potential IoC matches, the destination system that will receive matching IoC, and the target applicable to that rule. Multiple Sharing configurations can be made to support mapping certain IoC to multiple targets even on the system destination system.
Modify, Test, or Delete a Sharing Configuration
Each configuration supports 3 actions:
Edit the rule by clicking on the pencil icon.
Test the rule by clicking on the synchronization icon. This tests how many IoC will actually be sent to the destination system based on the timeframe and the rule.
Delete the rule by clicking on the garbage can icon.
Validate the ThreatConnect Plugin
Validate the Pull
Threat Exchange pulls Address (IPv4, IPv6), Files (SHA256, MD5), URLs, and Hosts  from
Browse > Indicators
in the ThreatConnect plugin.
Go to
Threat Exchange > Threat IoCs
and search for IoCs pulled from the ThreatConnect plugin.
The Host or domain values will be considered as Host on ThreatConnect, and will be stored as hostname in Cloud Exchange.
Observe Tags created:
Go to
Logging
and search for IoCs pulled from the ThreatConnect plugin.
Validate the Push
To verify pushed IoCs in ThreatConnect, Go to
ThreatConnect Platform > Browse > Indicators
.
IoCs pushed from Netskope will be tagged with
Netskope
.
Go to
Browse > Groups
. Select the Group type under which you have your group added. Select your group name and check the shared data.
Data shared in the Group will be appended and not replaced.
To validate the pushed indicators on Threat Exchange, go to
Threat IoCs
and search for IoCs that are shared with ThreatConnect.
Troubleshooting the ThreatConnect Plugin
Unable to Pull data from the ThreatConnect platform
If you are not able to pull data from the ThreatConnect platform, it might be due to one of the following things.
Data is not available on the platform to pull.
Data is available on platform, but not in the given time range provided in the plugin configuration.
What to do:
If data is not pulled from the plugin, first check if you have any data available on the
ThreatConnect platform
. If you have data to pull, check the date for the available data and check if the data falls under the time interval mentioned in the plugin configuration.
Unable to push IoCs to ThreatConnect
When sharing IoCs to ThreatConnect if you are receiving any error messages, check the error logs.
CTE ThreatConnect [CTE ThreatConnect]: Received exit code 400, Bad Request while Pushing indicator on ThreatConnect platform having indicator value: 1bfbefa4ff4d0df3ee0090b5079cf84ed2e8d5377ba5b7a30afd88367d57b9ff.
What to do:
The IoCs that were not shared will be added in the error log as shown above. IoCs that are already present on the ThreatConnect platform will not be shared. To confirm if the IoC is not shared because it is already present, go to
ThreatConnect > Create
. Select the type of IoC that failed to be pushed and try adding it. If you see that a value already exists, then it will not be shared to ThreatConnect from push.
CTE ThreatConnect [CTE ThreatConnect]: Received exit code 403, Forbidden while Pushing indicator on ThreatConnect platform having indicator value: 10.50.5.63. {"errCode":"0x1003","message":"This Indicator is contained on a system-wide exclusion list.","status":"Error"}
What to do:
The IoCs that were not shared will be added in the error log as shown above. All IoCs that will be a part of the exclusion list on ThreatConnect will not be shared on the ThreatConnect platform. To confirm if the IoC is not shared because of the exclusion list, go to
ThreatConnect > Create
. Select the type of IoC that failed to be pushed and try adding it. If you see that a value is present in the system-wide exclusion list, then it will not be shared to ThreatConnect from push.
Receiving the 400 Client Error in logs while executing the plugin life cycle
If you are receiving the above-mentioned error in logs while pulling indicators from the ThreatConnect platform, try increasing the value of the Custom TQL Timeout.
You can increase the TQL Timeout value using the following steps:
Log in to your ThreatConnect account.
Go to
Settings > Org Settings
.
Edit the account that you use for generating the configuration parameters and increase the value for the Custom TQL Timeout.
Receiving an error while updating the plugin using the plugin repository
If you are facing an issue updating the configured ThreatConnect plugin, follow these steps:
Close the plugin repo page once pulling and downloading the plugin updates.
Go to
Threat Exchange > Plugins
.
Edit the plugin, on the Configuration Parameters page. Remove the selected value from the Type of Threat Indicator field, and reselect the IoC type that you want to pull.
Click
Save
.
Click on the enable plugin icon and enable the plugin. The plugin will be updated with the latest changes and should start working as expected.
In this Topic
ThreatConnect Plugin for Threat Exchange

---
## Threat Exchange Custom Plugin Developers Guide
**URL:** https://docs.netskope.com/en/threat-exchange-custom-plugin-developers-guide/
**Last Modified:** 2026-03-21T02:27:56+00:00
**Scraped:** 2026-08-11T07:19:12.501089+00:00

Threat Exchange Custom Plugin Developers Guide - Netskope Technical Documentation
Threat Exchange Custom Plugin Developers Guide
This document explains how to create a new Threat Exchange plugin and extract maximum value out of your threat ecosystem by leveraging the functionality provided within the Threat Exchange module. To create a new developers guide, use this
template
.
Prerequisites
To create a new plugin, you need:
Python 3.x programming experience (intermediate level).
Access to the Netskope Cloud Exchange platform.
API or Python SDK access to the product or solution for which you need to write the plugin.
An account with minimum permission for the product.
Threat Exchange Module
The Cloud Exchange (CE) platform, and its Threat Exchange module, come with a rich set of features and functionality that allow for a high degree of customization, so we recommend that you familiarize yourself with the different aspects of the platform as listed below.
Note
This module supports sharing of data from Netskope to third party and vice-versa.
Netskope Concepts and Terminology
Core: CE core engine manages the 3rd-party plugins and their life cycle methods, plus has API endpoints for interacting with the platform to perform various tasks.
Module: The functional code areas that invoke modular-specific plugins to accomplish different workflows. Threat Exchange is one of the modules in Cloud Exchange.
Plugin: Plugins are Python packages that have logic to pull and push Threat IoC information to/from 3rd-party Threat Intel systems, which will then be stored in the Threat Exchange.
Plugin Configurations: Plugin configurations are the plugin class objects configured with the required parameters and scheduled by the Cloud Exchange core engine for pulling and pushing Threat IoC information.
Indicators (Threat IoCs): Indicators are malware hashes and malsite URLs objects gathered from various Threat Intel Platforms and stored in the Cloud Exchange database.
Development Guidelines
Use the Package Directory Structure for all Python code.
Make sure all the 3rd-party libraries packaged with the plugin package are checked for known vulnerabilities.
Make sure to follow standard Python code conventions:
PEP 8 – Style Guide for Python Code
.
Run and verify that the
flake8
lint check passes with the docstring check enabled. Also, the maximum length of a line should be 80.
Convert the timestamp values to the human-readable format (from epoch to DateTime object). Make sure the time that is being displayed on the UI should be in the local timezone.
If possible, add a default value while adding a configuration parameter in the plugin.
For Scripts/Integrations written in Python, make sure to create unit tests. Go to
Unit Testing
for more information.
Plugin architecture allows storing states; however, avoid storing huge objects for state management.
Check your python code for any vulnerabilities.
The plugin icon has to be under 10KB. Make sure to use the company logo (and not the product’s) with a transparent background. The recommended size for the logo is 300 x 50 or similar aspect ratio.
Use the checkpoint provided by the Threat Exchange core rather than implementing one on your own.
Follow the
Plugin Directory Structure
.
If the Plugin description contains a link, it should be a hyperlink redirecting to the documentation page.
The logger messages and the Toast messages should not contain the API Token and the Password type field values.
Pagination should always be considered while developing any feature in a plugin.
Make sure to add a retry mechanism for the 429 status code.
Make sure to map the various fields received from API calls with the Indicator data model to leverage the full benefit of the system. Fields like reputation, first-seen, and comments so that the data in the indicator fields makes more sense to the SOC user when analyzing the data.
Make sure to map the comment field which gives more context to the SOC analyst. The comment field could include the file name(in the case of Hash).
Use the checkpoint provided by the Cloud Exchange core rather than implementing one on your own.
Always check if the plugin supports the push mechanism or not and set the push_supported variable accordingly in manifest.json.
Use proper validation for the parameters passed to the validate method and provide the proper help text for all the parameters.
Use notifier object to raise the notification for failures or critical situations (like rate-limiting, or exceeding payload size) to notify the status of the plugin to the user.
Make sure to implement a proper logging mechanism with the logger object passed by the Cloud Exchange platform. Make sure enough logging is done which helps the Ops team in troubleshooting. Make sure any sensitive data is not logged or leaked in the notification.
Provide the proper help text (tooltip) for all the parameters. If feasible, make sure to explain the significance of the parameter in the tooltip.
There should be a placeholder for text type of configuration parameters.
Make sure to provide a meaningful name and description to plugin configuration parameters.
Make sure to provide an appropriate configuration type (text, number, password, choice, multi-choice) to the configuration parameters.
Make sure to use the proxy configuration dict and the SSL certificate validation flag that is passed by the CE platform while making any outbound request (API/SDK).
Make sure to collect the value of a non-mandatory parameter using the .get() method and provide a default value while using .get() method.
Make sure the plugin directory name (e.g sample_plugin) matches with the manifest.json’s id field.
User Agent should be added to the headers while making any API call. Format for the User Agent:
netskope-ce-
<ce_version>
-
<module>
-
<plugin_name>
-
<plugin_version>
.
Note
The plugin version should be dynamically fetched and to fetch netskope-ce-<version> string use the method defined by core.
API Tokens and Password fields should not use strip().
The log messages should start with “<module> <app name>; Plugin [configuration_name]: “.
Example: “URE Crowdstrik Plugin [CrowdStrike Configuration Name]: <log_message>”. [This is a suggestion, you can avoid configuration name]. (logger.info(“<module> <plugin_name> Plugin: <message>”))
While logging an error log, if possible, you should add a traceback of the exception.
Use:
self.logger.error(error, details=traceback.format_exc())
.
The Toast message should not contain the “
<app_name>
<module>
Plugin:” in the message.
Make sure to catch proper exceptions and status codes while and after making the API calls.
The CHANGELOG.md file should be updated with proper tags such as Added, Changed, and Fixed along with a proper user-friendly message. Make sure the file name should exactly matches CHANGELOG.md.
Writing a Plugin
This section explains the process of writing a plugin from scratch
Download the sample plugin from the
NetskopeOSS public Github repository
.
Development Setup
Python
Threat Exchange utilizes Python3 (v3.7 and above). Make sure to set up python3 in your development environment. Pytest is used to run unit tests.
Included Python Libraries
Following Python libraries are included within the Netskope Threat Exchange platform.
Library Name
Version
aiofiles
22.1.0
amqp
5.1.1
anyio
3.6.2
asgiref
3.6.0
attrs
22.2.0
azure-core
1.26.2
azure-storage-blob
12.14.1
bcrypt
4.0.1
boto3
1.26.51
botocore
1.29.51
billiard
3.6.4.0
celery
5.2.7
cabby
0.1.23
cachetools
5.2.1
celerybeat-mongo
0.2.0
certifi
2022.12.7
cffi
1.13.2
chardet
5.1.0
charset-normalizer
3.0.1
click
8.1.3
click-didyoumean
0.3.0
click-plugins
1.1.1
click-repl
0.2.0
colorama
0.4.6
colorlog
6.7.0
cryptography
39.0.0
cybox
2.1.0.21
defusedxml
0.7.1
dnspython
2.3.0
docker
6.0.1
fastapi
0.89.1
furl
2.1.3
google-api-core
2.11.0
google-auth
2.16.0
google-cloud-core
2.3.2
google-cloud-pubsub
2.13.12
google-cloud-pubsublite
1.6.0
google-cloud-storage
2.7.0
google-crc32c
1.5.0
google-resumable-media
2.4.0
googleapis-common-protos
1.58.0
grpc-google-iam-v1
0.12.6
grpcio
1.51.1
grpcio-status
1.51.1
gunicorn
20.1.0
h11
0.14.0
idna
3.4
importlib-metadata
6.0.0
isodate
0.6.1
jmespath
1.0.1
jsonpath
0.8
jsonschema
4.17.3
kombu
5.2.4
libcst
0.3.21
libtaxii
1.1.119
lxml
4.9.2
mongoengine
0.25.0
mongoquery
1.4.2
more-itertools
9.0.0
MarkupSafe
2.1.2
memory-profiler
0.61.0
mixbox
1.0.5
msrest
0.7.1
multidict
6.0.4
mypy-extensions
0.4.3
netskopesdk
0.0.25
numpy
1.23.5
oauthlib
3.2.2
onelogin
3.1.0
ordered-set
4.1.0
orderedmultidict
1.0.1
overrides
6.5.0
pandas
1.5.0
packaging
23.0
passlib
1.7.4
pycparser
2.21
prompt-toolkit
3.0.36
proto-plus
1.22.2
protobuf
4.21.12
psutil
5.9.4
pydantic
1.10.4
pyasn1
0.4.8
pyasn1-modules
0.2.8
PyJWT
2.6.0
pymongo
4.3.4
pyparsing
3.0.9
python-dateutil
2.8.2
pyrsistent
0.15.6
python-multipart
0.0.5
python3-saml
1.15.0
pytz
2022.7.1
PyYAML
6.0
requests
2.28.2
requests-oauthlib
1.3.1 4.9
rsa
4.9
six
1.16.0
starlette
0.22.0
sniffio
1.3.0
s3transfer
0.6.0
stix
1.2.0.11
taxii2-client
2.3.0
typing-inspect
0.8.0
typing-utils
0.1.0
typing_extensions
4.4.0
urllib3
1.26.14
uvicorn
0.20.0
vine
5.0.0
wcwidth
0.2.6
weakrefmethod
1.0.3
websocket-client
1.4.2
Werkzeug
2.2.2
xmlsec
1.3.11
zipp
3.11.0
requests-mock
1.7.0
Including Custom Plugin Libraries
Netskope advises bundling any of the third party python libraries your plugin will need with the plugin package itself. To achieve this bundling use the pip installer; it provides a switch which takes a directory as an input. If it is provided, pip will install the packages into that directory.
For example, the command shown below will install the
cowsay
package into the directory
lib
.
> pip install cowsay --target ./lib
For the official documentation on this, refer
https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-t
.
While importing modules from above lib folder, we should be using relative import instead of absolute import, as shown below:
rom .lib import cowsay
IDE
Recommended IDEs are PyCharm or Visual Studio Code.
Plugin Directory Structure
This section describes the typical directory structure for the Threat Exchange plugin.
/sample_plugin/
  ├──__init__.py
  ├──CHANGELOG.md
  ├──icon.png
  ├──main.py
  ├──manifest.json
Sample Plugin Contents
README.md: README file contains the documentation for the Plugin integration use case.
__init__.py: Every plugin package is considered a python module by the Cloud Exchange code. Make sure every plugin package contains the empty “__init__.py” file.
CHANGELOG.md: This file contains the details about plugin update and should be updated with proper tags as Added, Changed, Fixed along with a proper user-friendly message
icon.png: Plugin icon logo, this will be visible in the plugin chiclet and configuration cards on the UI. The logo should have a transparent background with recommended size of 300*50 pixels or a similar aspect ratio.
main.py: This python file contains the Plugin class containing the concrete implementation for the pull, push and validate method.
manifest.json: Manifest file for the plugin package containing information about all the configurable parameters and their data types. This file has more information about the plugin integration as well.
The listed files here are mandatory for any plugin integration, but you can add other files based on specific integration requirements.
Note:
Make sure the plugin directory name (e.g sample_plugin) matches with the manifest.json’s id field.
CHANGELOG.md
This is a file that contains details about plugin update and should be updated with proper tagsas Added, Changed, Fixed along with a proper user-friendly message.
Added: Use it when new features are added.
Fixed: Use it when any bug/error fixed.
Changed: Use it when there is any change in existing implementation of plugin.
Sample Changelog.md
# 1.0.1
## Fixed
- Fixed pagination when there are more than 10k Logs
# 1.0.0
## Added
- Initial release.
Manifest.json
This is a JSON file that stores the meta-information related to the plugin, which is then read by the Threat Exchange module to render the plugin in the UI, as well as enabling the Threat Exchange module to know more about the plugin, including required configuration parameters, the plugin-id, the plugin-name, etc.
Every plugin must contain this file with the required information so that Threat Exchange can instantiate the Plugin object properly.
Common parameters for manifest.json include:
name: (string) Name of the plugin. (Required)
id: (string) Id of the plugin package. Make sure it is unique across all the plugin installed in the Cloud Exchange. The ID has to match the directory name of the plugin package. (Required)
version: (string) Version of the plugin. Usage of a MAJOR.MINOR.PATCH (ex. 1.0.1) versioning scheme is encouraged although there are no restrictions. (Required)
description: (string) Description of the plugin. Provide a detailed description which mentions the capabilities and instructions to use the plugin, (ex. This plugin works with product foo and extracts both md5 and sha256 hashes as well as malURL to Threat Exchange and pushes the same to product foo.) This description would appear on the Plugin Configuration card. (Required)
push_supported: (boolean) This flag indicates whether the plugin supports the push method or not. If it is set to false then sharing related fields will not be displayed in the UI. (optional, defaults to true)
patch_supported: (boolean) This flag indicates whether the integrated product supports incrementally reporting indicators. Certain products (e.g. Netskope features using RESTAPIv1) expect that all the indicators have to be reported each time. In such cases “patch_supported” is required to be set as ‘False’. Alternatively, ServiceNow allows sharing indicators one at a time and retains the previously shared indicators. In its a case, patch_supported was required to be set as ‘True’. (Required)
configuration: (array) Array of JSON objects that contains information about all the parameters required by the plugin – their name, type, id, etc. The common parameters for the nested JSON objects are explained below.
label: Name of the parameter. This will be displayed on the plugin configuration page. (Required)
key: Unique parameter key, which will be used as a key in the python dict object where the plugin configuration is used. (Required)
type: Value type of the parameter. Allowed values are ‘text’, ‘password’, ‘number’, ‘choice’, and ‘multichoice’. (Required) Refer to Plugin Configuration parameter types below for more details.
default: The default value for this parameter. This value will appear in the plugin configuration page on Threat Exchange UI. Supported data-types are “text”, “number”, and “list” (for multichoice type). (Required)
mandatory: Boolean which indicates whether this parameter is mandatory or not. If a parameter is mandatory Threat Exchange UI won’t let you pass an empty value for the parameter. Allowed values are “true” and “false”. (Required)
description: Help text level description for the parameter which can give more details about the parameter and expected value. This string will appear in the plugin configuration page as a help-text. (Required)
choices: A list of JSON objects containing key and value as JSON keys. This parameter is only supported by
‘type’: ‘choice and multichoice’
.
Plugin Configuration Parameter Types
Make sure all the required plugin configuration parameters are listed under the configuration section of manifest.json for the plugin.
Password Parameter
Use this parameter for storing any secrets/passwords for authentication with API endpoints. Parameters with type as the password will have a password text box in the Plugin configuration page and will be obfuscated and encrypted by the platform.
Sample JSON
"configuration": [
    {
        "label": "Api token",
        "key": "api_token",
        "type": "password"
    },
]
Plugin configuration view:
Text Parameter
Use this parameter for storing any string information such as base-url, username, etc. This parameter will have a normal text input on the plugin configuration page.
Sample JSON
"configuration": [
    {
        "label": "Tenant Name",
        "key": "tenant_name",
        "type": "text"
    },
]
Plugin configuration view:
Number Parameter
Use this parameter for storing number/float values. This parameter will have a number input field on the plugin configuration page.
Sample JSON
"configuration": [
    {
        "label": "Maximum File hash list size in MB.",
        "key": "max_size",
        "type": "number"
    },
]
Plugin configuration view:
Choice Parameter
Use this parameter for storing any enumeration parameter values. This parameter will have a dropdown on the plugin configuration page.
Sample JSON
"configuration": [
{
"label": "Type of Threat data to pull",
"key": "ioc_type",
"type": "choice",
"choices": [
    {
      "key": "Both",
      "value": ["malware", “malsite”]
    },
    {
      "key": "Malware",
      "value": "malware"
    },
    {
      "key": "Malsite",
      "value": "malsite"
    }
  ]
 },
]
Plugin configuration view:
After selecting the input.
Multichoice Parameter
Use this parameter for storing multiple choice values. This parameter will have a dropdown on the plugin configuration page with ability to select multiple values.
Sample JSON
"configuration": [
    {
        "label": "Severity",
        "key": "severity",
        "type": "multichoice",
        "choices": [
            {
                "key": "Unknown",
                "value": "unknown"
            },
            {
                "key": "Low",
                "value": "low"
            },
            {
                "key": "Medium",
                "value": "medium"
            },
            {
                "key": "High",
                "value": "high"
            },
            {
                "key": "Critical",
                "value": "critical"
            }
        ],
        "default": [
            "critical",
            "high",
            "medium",
            "low",
            "unknown"
        ],
        "mandatory": false,
        "description": "Only indicators with matching severity will be saved."
    }
]
Plugin Configuration View:
Toggle Parameter
This parameter stores a boolean value; toggle enabled is True and toggle disabled is False.
Enable SSL Verification: This variable should be used while making any API call in plugin.
Use System Proxy (‘proxy’): Use system proxy configured in Settings.(Default: False)
Plugin Configuration View:
Note
This parameter is provided by Core, and it is not allowed to add from plugins manifest.json file.
main.py
This python file contains the core implementation of the plugin.
Standard Imports
from netskope.integrations.cte.plugin_base import PluginBase, ValidationResult, PushResult
from netskope.integrations.cte.models import Indicator, IndicatorType
from netskope.integrations.cte.models.business_rule import Action, ActionWithoutParams
PluginBase Variables
PluginBase provides access to variables which can be used during the plugin lifecycle.
Methods. Here is the list of variables.
Variable Name
Usage
Description
self.logger
self.logger.error(“Message”)
self.logger.warn(“Message”)
self.logger.info(“Message”)
Logger handle provided by core. Use this object to log important events. The logs would be visible in the Cloud Exchange Audit logs. Refer the
Logging
documentation.
self.configuration
self.configuration.get(<attribute-key-name>)
JSON representation of the configuration object of Plugin instance. Use this to access the configuration attributes like authentication credentials, server details, etc. Use the key name of the attribute mentioned in manifest.json.
self.last_run_at
If self.last_run_at:
self.last_run_at.timestamp()
Use this format to convert the last run time in epoch format.
Provides the timestamp of last successful run time of the Plugin’s pull method. The Cloud Exchange core maintains the checkpoint time after each successful pull() execution. For the first execution, the value would be None. The datatype of the object is datetime.
self.storage
Cloud Exchange provides the plugin a mechanism to maintain state. Use this object to persist any state that would be required during subsequent calls. The datatype of this object is python dict.
self.notifier
self.notifier.info(“message”)
self.notifier.warn(“message”)
self.notifier.error(“message”)
This object provides handle of Cloud Exchange core’s notifier. Use this object to push any notification to the platform. The notifications would be visible on Threat Exchange UI. Make sure the message contains summarized information for user to read and take necessary actions.
For example, a used notifier in Netskope plugin if the push() method exceeds 8MB limit of the product.
self.proxy
requests.get(url=url, proxies=self.proxy)
Handle of system’s proxy settings if configured, else {}.
self.ssl_validation
requests.get(url=url, verify=self.ssl_validation)
Boolean value which mentions if ssl validation be enforced for REST API calls.
Plugin Class
Plugin class has to be inherited from the PluginBase class. PluginBase class is defined in
netskope.integrations.cte.plugin_base
.
Make sure Plugin class provides implementation for the pull, push and validate method.
Plugin class will contain all the necessary params to establish connection and authentication with the 3rd-party API.
Constants like PLUGIN_NAME, LIMIT, etc. should be declared.
"""Sample plugin implementation.
This is a sample implementation of base PluginBase class. Which explains the concrete implemetation
of the base class.
"""
from netskope.integrations.cte.plugin_base import PluginBase, ValidationResult, PushResult
from netskope.integrations.cte.models import Indicator, IndicatorType
from typing import List
from datetime import datetime
import requests
PLUGIN_NAME = "<module> <plugin_name> Plugin
class SamplePlugin(PluginBase):
   """SamplePlugin class having concrete implementation for pulling and pushing threat information.
   This class is responsible for implementing pull, push and validate methods with proper return types,
   so that it's lifecycle execution can be scheduled by the CTE core engine.
   """
Def Pull()
This is an abstract method of PluginBase Class.
This method implements the logic to pull the Threat IoCs (Malware & Malsites) from the API endpoints. This method is invoked periodically.
Make sure it’s unit-testable.
Use the checkpoint passed by the Cloud Exchange platform by invoking
self.last_run_at
It returns the datetime.datetime Python object containing timestamp when this method was last executed successfully.
Use the proxy configuration passed by the Cloud Exchange platform by invoking
self.proxy
. It returns the python dict object which can be used directly with requests module.
All the configuration parameters for API authentication are passed as python dict receives them by invoking
self.configuration.
All the logs be logged by the
self.logger
object with proper log level (info, warn, error). This object logs the logs to MongoDB and can be accessed via API calls.
Use
self.ssl_validation
bool to enable/disable validation of the SSL server certificate.
Return the list of Indicator objects (Refer to below) which contain the data received from the API endpoint.
In the case of failure raise an error or exception of appropriate type with proper message.
def pull(self):
"""Pull the Threat information from the 3rd part Threat Intel systems.
Implement the logic of pulling Threat data from 3rd party apis and return the list of objects netskope.integrations.cte.models.Indicators on successful pull otherwise raises an exception.
Returns:
    List[netskope.integrations.cte.models.Indicators]: List of indicator objects received from the 3rd-party Threat Intel Systems.
"""
# Load all the configured plugin parameters as python dict object.
# Use the key name provided in the manifest.json file for the configuration parameters to
# get the value of that particular parameter.
config = self.configuration
# get proxy settings dict, just the way requests module requires.
proxy_dict = self.proxy
# get the ssl_validation bool for enabling/disabling validation of SSL server certificates.
ssl_validation = self.ssl_validation
start_time = self.last_run_at  # datetime.datetime object.
# How to use proxy dict and ssl_validation flag.
resp = requests.get("www.example.com", proxies=proxy_dict, verify=ssl_validation)  # noqa: F841
# Get the logger object for logging purpose. This logger object logs all the logs to mongodb
# under the cte database logs collection. Log timestamp is automatically recorded by the logger library.
# Supported logging levels are info, warn and error.
logger = self.logger
logger.info(f"{PLUGIN_NAME}: Starting Pulling data for sample plugin.")
indicator_list = self.pull_data_from_3rd_party_api(config, logger)
logger.info(f"{PLUGIN_NAME}:logger.info("{PLUGIN_NAME}: Finished pulling data")
return indicator_list
Def Push()
This is an abstract method of PluginBase Class.
This method implements the logic to push the Threat IoC information shared by the Cloud Exchange platform to the product API endpoints.
It receives all the parameters that the Pull method receives in addition to that it receives the List of Indicator objects from the Cloud Exchange platform as method argument which are to be shared with the integrating product.
This method will be invoked when the Cloud Exchange platform receives a new indicator from a source and sharing of indicators is configured with the current plugin configuration.
If the API supports the PATCH method to share the indicators then this method will receive only one indicator object in the list otherwise it will receive all the indicator objects which are returned after applying the sharing filters on all the indicators in the Threat Exchange platform database.
Make sure to handle the case when the maximum payload size supported by API endpoint is exceeded. There can be multiple ways to handle this case:
If the API endpoint supports multiple requests with a fixed payload size, send the data in chunks.
If the API endpoint does not support multiple requests (i.e. we can push it in one API call only) either plugin can skip the remaining indicators and raise a notification to the user to adjust the sharing filters or it can fail with the error of exceeded payload size.
Return the PushResult object (Refer to
PushResult Class
with a success flag indicating whether the Push operation was successful or not.
Handle all the Exceptions with connection and HTTP response code.
def push(self, indicators: List[Indicator]):
    """Push the Indicator list to the 3rd party Threat Intel systems.
    Implement the logic of spliting the indicators list according to their type and push the data
    to the 3rd party APIs. This method will be invoked while sharing the Threat information with 3rd party.
    Args:
        indicators (List[netskope.integrations.cte.models.Indicators]): List of Indicator objects to be pushed.
    Returns:
        netskope.integrations.cte.plugin_base.PushResult: PushResult object with success flag and Push result message.
    """
    # Load all the configured plugin parameters as python dict object.
    # Use the key name provided in the manifest.json file for the configuration parameters to
    # get the value of that particular parameter.
    config = self.configuration
    # get proxy settings dict, just the way requests module requires.
    proxy_dict = self.proxy
    # get the ssl_validation bool for enabling/disabling validation of SSL server certificates.
    ssl_validation = self.ssl_validation
    # How to use proxy dict and ssl_validation flag.
    resp = requests.get("www.example.com", proxies=proxy_dict, verify=ssl_validation)   # noqa: F841
    # Get the logger object for logging purpose. This logger object logs all the logs to mongodb
    # under the cte database logs collection. Log timestamp is automatically recorded by the logger library.
    # Supported logging levels are info, warn and error.
    logger = self.logger
    logger.info(f"{PLUGIN_NAME}: Starting Pulling data for sample plugin.")
    push_result = self.push_data_to_3rd_party_api(config, logger, indicators)
    logger.info("f"{PLUGIN_NAME}: Finished Pushing data for sample plugin.")
    return push_result
Def Validate()
This is an abstract method of PluginBase Class.
This method validates the plugin configuration and authentication parameters passed while creating a plugin configuration.
This method will be called only when a new configuration is created or updated.
Validate against all the mandatory parameters are passed with the proper datatype.
<li”>Validate the authentication parameters and the API endpoint to ensure the smooth execution of the plugin lifecycle.
Return the object of ValidationResult (Refer to
ValidationResult Class
) with a success flag indicating validation success or failure and the validation message containing validation failure reason.
def validate(self, data):      
     """Validate the Plugin configuration parameters.
  Validation for all the parameters mentioned in the manifest.json for the existence and
  data type. Method returns the netskope.integrations.cte.plugin_base.ValidationResult object with success = True in the case
  of successful validation and success = False and a error message in the case of failure.
  Args:
      data (dict): Dict object having all the Plugin configuration parameters.
  Returns:
      netskope.integrations.cte.plugin_base.ValidateResult: ValidateResult object with success flag and message.
  """
  self.logger.info(f"{PLUGIN_NAME}: Executing validate method for Sample plugin")
  if (
      "secret_field_id1" not in data
      or not data["secret_field_id1"]
      or type(data["secret_field_id1"]) != str
  ):
      self.logger.error(
          f"{PLUGIN_NAME}: Validation error occurred Error: Secret Field1 is required with type string."
      )
      return ValidationResult(
          success=False, message="Invalid Secret Field 1 provided.",
      )
else:
return ValidationResult(
        success=True, message="Validation Successful for Sample plugin"
   )
Def get_actions()
This is an abstract method of PluginBase Class.
This method should return a list of all the supported actions (displayed as
Targets
in the UI) if the plugin supports sharing of indicators (i.e. manifest has push_supported=true) otherwise it should return an empty list.
Add all the supported actions in the ActionWithoutParams class and return a list of objects of ActionWithoutParams class.
If the plugin supports sharing of indicators then this method should return at least one action.
If manifest has push_supported=false:
def get_actions(self):
"""Get available actions.
Returns:
 List[ActionWithoutParams]: List of ActionWithoutParams objects that are supported by the plugin.
"""
 return []
If manifest has push_supported=true:
def get_actions(self): 
"""Get available actions.
Returns:
List[ActionWithoutParams]: List of ActionWithoutParams objects that are supported by the plugin.
"""
return [
ActionWithoutParams(label=”Share Indicators”, value=”share”)
ActionWithoutParams(label=”Add to Group”, value=”add”)
]
Def get_action_fields():
This is an abstract method of PluginBase Class.
This method should return the list of fields to be rendered in the UI when a target is selected from dropdown.
This method should be called after the user selects any of the actions.
If the selected action requires any parameters then return a list of dictionaries (where each dictionary is a configurable input) otherwise return an empty list.
Go to
Manifest.json
to see how fields are defined.
If manifest has push_supported=false:
def get_action_fields(self, action: Action):
"""Get fields required for an action.
Args: 
 action (Action): Action object which is selected as Target.
Return:
 List[Dict]: List of configurable fields based on selected action.
"""
 return []
If manifest has push_supported=true:
def get_action_fields(self, action: Action):
"""Get fields required for an action.
Args: 
 action (Action): Action object which is selected as Target.
Return:
 List[Dict]: List of configurable fields based on selected action.
"""
 if action.value == “add”:
         return [
     {
       “label”: “Group Name”,
       “key”: “group_name”,
       “type”: “text”,
       “default”: “”,
       “mandatory”: True,
       “description”: “Name of group.”
     }
 ]
else:
 return []
Def validate_action():
This is an abstract method of PluginBase Class.
This method validates the action and their parameters.
This method will be called only when the new sharing configuration is created or existing sharing configuration is updated.
Validate against all the mandatory parameters are passed with the proper datatype.
Return the object of ValidationResult (Refer to
ValidationResult Class
) with a success flag indicating validation success or failure and the validation message containing validation failure reason.
If the plugin is not push supported then return ValidationResult object with a success flag otherwise check for validations.
If manifest has push_supported=false:
def validate_action(self, action: Action):
"""Validate Action Parameters.
Args: 
action (Action): Action object having all the configurable parameters.
Return:
netskope.integrations.cte.plugin_base.ValidateResult: ValidateResult object with success flag and message.
"""
return ValidationResult(success=True, message=”Validation successful.”)
If manifest has push_supported=true:
def validate_action(self, action: Action):
"""Validate Action Parameters.
Args: 
action (Action): Action object having all the configurable parameters.
Return:
netskope.integrations.cte.plugin_base.ValidateResult: ValidateResult object with success flag and message.
"""
if action.value not in [“share”, “add”]:
return ValidationResult(
 success=False, message=”Unsupported action provided.”
       )
if action.value == “add”:
if action.parameters.get(“group_name”) is None:
return ValidationResult(
 success=False, message=”Group Name should not be empty.”
       )
return ValidationResult(
 success=True, message=”Validation successful.”
 )
Data Models
This section lists down the Data Models and their properties.
IndicatorType Model
This class provides the Python data model for an IndicatorType object.
This model has 3 fields: URL, SHA256, MD5 of type string.
You will interact with the model in the pushmethod as you sending a list of Indicators to thirdparty.
Data Model Properties
Name
Type
Description
URL
string
It can be used for URLs
SHA256
string
It can be used for sha256 typ of file hashes
MD5
string
It can be used for md5 type of file hashes
from netskope.integrations.cte.models import ( Indicator,
IndicatorType,
SeverityType,
)
Indicator(
value=behavior_info.get("ioc_value"),
type=IndicatorType.SHA256,
comments=behavior_info.get("ioc_description", ""),
firstSeen=datetime.datetime.strptime(
behavior_info.get("timestamp"),
"%Y-%m-%dT%H:%M:%SZ",
),
lastSeen=datetime.datetime.strptime(
behavior_info.get("timestamp"),
"%Y-%m-%dT%H:%M:%SZ",
),
severity=self.get_severity_from_int(behavior_info.get("severity", 0)),
)
SeverityType Model
This class provides the Python data model for an SeverityType object.
This model has 5 fields: UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL of type string.
You will interact with the model in the pull method as you return a list of Indicators.
Data Model Properties
Name
Type
Description
UNKNOWN
string
It can be used for unknown severity
LOW
string
It can be used for low severity
MEDIUM
string
It can be used for medium severity
HIGH
string
It can be used for high severity
CRITICAL
string
It can be used for critical severity
from netskope.integrations.cte.models import SeverityType
if type(severity) is not int or severity == 0:
return SeverityType.UNKNOWN
if 10 <= severity <= 39:
return SeverityType.LOW
if 40 <= severity <= 69:
return SeverityType.MEDIUM
if 70 <= severity <= 89:
return SeverityType.HIGH
if 90 <= severity <= 100:
return SeverityType.CRITICAL
return SeverityType.UNKNOWN
ActionWithoutParams Model
This class provides the Python data model for an ActionWithoutParams object.
This model has 2 fields: label and value of type string.
You will interact with the model in the get_actions method as you return a list of available actions.
Data Model Properties
Name
Type
Description
label
string
Label displayed on UI
value
string
Value of the field
from netskope.integrations.cte.models.business_rule import
ActionWithoutParams
ActionWithoutParams(
label="Add to Suspicious Object List",
value="suspicious_object",
)
This class provides the Python data model for an Indicator object.
Pull method returns the list of objects of Indicator class with the information receivedfrom API calls.
Supported values for type field is
IndicatorType.MD5
,
IndicatorType.SHA256
and
IndicatorType.URL
. MD5 and SHA256 types are used to represent malware indicators and URL type is used to represent malsite indicators.
The value of the reputation field has to be in the range of 1-10. The default value of thereputation fields is 5, if not supplied. If it is supplied (within that range) CTE will accept and display it.
Data Model Properties
Name
Type
Description
value
string
Indicator value. It can be MD5/SHA256 hash value in the case of Malware indicators, and domain-name/url in case of Malsite indicators.
type
Enum (IndicatorType)
It can be IndicatorType.MD5 or IndicatorType.SHA256 in the case of Malware indicators, IndicatorType.URL in case of Malsite indicators.
test
bool
Indicates whether it’s a test indicator or not.
Default – False
reputation
int
Reputation score of indicator.
Default – 5
expiresAt
datetime.datetime
Time after which Indicator will be marked as inactive by Cloud Exchange.
firstSeen
datetime.datetime
datetime.datetime object indicating when the indicator was discovered for the first time.
Default – Current System time when Indicator object was created.
lastSeen
datetime.datetime
datetime.datetime object indicating when the indicator was discovered for last time.
Default – Current System time when Indicator object was created.
comments
string
Comment string which gives more information about the indicator.
severity
Enum (SeverityType)
Severity of the indicator. Possible values are:
SeverityType.LOW
SeverityType.MEDIUM
SeverityType.HIGH
SeverityType.CRITICAL
SeverityType.UNKNOWN
extendedInformation
string
A link leading to an external source for extended information regarding the indicator. The value in this field will be rendered as a clickable URL in the UI. URL scheme must be either HTTP or HTTPS.
from netskope.integrations.cte.models import Indicator, IndicatorType  
Indicator(
      value="md5hash",         # md5 hash value of the indicator.
      type=IndicatorType.MD5,  # Type of indicator.
      test=True,               # Indicates whether it's test indicator or not. Defaults to False.
      reputation=7,            # Reputation score of Indicator. Defaults to 5.
      # Time after which Indicator will be marked as inactive.
      expiresAt=datetime.datetime(2022, 12, 23, 15, 22, 52, 667126),
      # Time when the Indicator was discovered first time. Defaults to current time.
      firstSeen=datetime.datetime(2017, 1, 11, 15, 22, 52, 667126),
      # Time when the Indicator was discovered last time. Defaults to current time.
      lastSeen=datetime.datetime(2019, 12, 23, 15, 22, 52, 667126),
      # Comment which gives more information about the indicator.
      comments="Indicator explanation",
  ),
PushResult Class
This class contains the result of Push operation of indicators to the product API endpoint.
The success flag indicates the push operation result and the message flag should have proper error message in the case of failure. (In a case of success a simple success message with success flag True should be returned)
Data Model Properties
Name
Type
Description
success
bool
success flag indicates the result of push operation, whether it succeeded or failed.
message
string
Message field denotes the error in case of failure. In case of success it can be a simple success message.
from netskope.integrations.cte.plugin_base import PushResult
PushResult(
    success=True, 
    message=" Successfully pushed data to 3rd party."
)
ValidationResult Class
This class contains the result of the validation process on the plugin configuration parameters passed to the Plugin object while creating a new configuration for the plugin.
Make sure that all the parameters passed to the validate method are validated against the data-type and value.
Validate method returns the object of this class with a success flag indicating the result of validation operation and message field contains the proper error message in the case of validation failure. (In a case of success a simple success message with success flag True has to be returned)
Data Model Properties
Name
Type
Description
success
bool
success flag indicates the result of validation operation, whether it succeeded or failed.
message
string
Message field denotes the error in case of failure. In case of success it can be a simple success message.
from netskope.integrations.cte.plugin_base import ValidationResult
ValidationResult(
           success=True,
           message="Validation Successfull for Sample plugin"
       )
Logging
Cloud Exchange provides a handle of logger object for logging.
Avoid print statements in the code.
This object logs to the central Cloud Exchange database with the timestamp field. Supported log levels are
info
,
warn
and
error
.
Make sure any API authentication secret or any sensitive information is not exposed in the log messages.
Make sure to implement a proper logging mechanism with the logger object passed by the CE platform.
Make sure enough logging is done, which helps the Ops team in troubleshooting.
Make sure any sensitive data is not logged or leaked in the notification or logs.
self.logger.error(
               f"{PLUGIN_NAME}: Error log-message goes here."
 )
 self.logger.warn(
               f"{PLUGIN_NAME}: Warning log-message goes here."
 )
 self.logger.info(
               f"{PLUGIN_NAME}: Info log-message goes here."
 )
Notifications
Cloud Exchange provides a handle of the notification object, which can be used to generate notifications on Cloud Exchange UI.
This object is passed from Cloud Exchange to the plugin object. Every plugin integration can use this object whenever there is a case of failure, which has to be notified to the user immediately. The notification timestamp is managed by Cloud Exchange.
This object will raise the notification in the UI with a color-coding for the severity of the failure. Supported notification severities are
info
,
warn
, and
error
.
Make sure any API authentication secret or any sensitive information is not exposed in the notification messages.
Use a notifier object to raise the notification for failures or critical situations (like rate-limiting, or exceeding payload size) to notify the status of the plugin to the user.
self.notifier.info(
              f"{PLUGIN_NAME}: Info notification-message goes here."
)
self.notifier.error(
              f"{PLUGIN_NAME}: Error notification-message goes here."
)
self.notifier.warn(
              f"{PLUGIN_NAME}: Warning notification-message goes here."
)
Tagging
Threat Exchange provides a utility class to handle tagging related functionalities from the plugin push/pull/validate methods. Below are some of the examples of what it can be used for.
Create a New Tag
from netskope.integrations.cte.models import TagIn
from netskope.integrations.cte.utils import TagUtils
utils = TagUtils()
utils.create_tag(Tag(name="Tag Name", color="#FF0000"))
Find if a Tag with a Given Name Already Exists
utils = TagUtils()
if utils.exists("Tag Name"):
    pass  # tag already exists
Remove a Tag from Some Indicators
utils = TagUtils()
utils.on_indicators({
    "source": "Test"
}).remove("Tag Name")
This removes the Tag Name tag from all the indicators with source=”Test”. The first and only argument to ‘on_indicators’ is a ‘dict’ object. This has to be a valid mongo query.
Add a Tag to Some Indicators
utils = TagUtils()
utils.on_indicators({
    "source": "Test"
}).add("Tag Name")
Testing
Linting
As part of the build process, we run a few linters to catch common programming errors, stylistic errors, and possible security issues.
Flake8
This is a basic linter. It can be run without having all the dependencies available and will catch common errors. We also use this linter to enforce the standard python pep8 formatting style. On rare occasions, you may encounter a need to disable an error/warning returned from this linter. Do this by adding an inline comment of the sort on the line you want to disable the error:
# # noqa: <error-id>
For example:
example = lambda: 'example' # example = lambda: 'example' # noqa: E731
When adding an inline comment always also include the error code you are disabling for. That way if there are other errors on the same line they will be reported.
Refer to:
https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors
PEP8 style docstring check is also enabled with the flake8 linter. So make sure every function/module has a proper docstring added.
Unit Testing
Ensure unit testing to test small units of code in an isolated and deterministic fashion. Make sure that unit tests avoid performing communication with external APIs and use mocking. Make sure unit tests ensure the code coverage is more than 70%.
Environment Setup
In order to work with unit testing, the integration or automation script needs to be developed following the
Plugin Directory Structure
. We use PIP to install all the required Python module dependencies required to run the setup. Before running the tests, make sure you install all the required dependencies mentioned in the
requirements.txt
of the Cloud Exchange core repository.
Write Your Unit Tests
Make sure unit tests are written in a separate Python file named:
<your_plugin_name>
_test.py. Within the unit test file, each unit test function should be named: test_
<your test case>
. More information on writing unit tests and their format is available at the
PyTest Docs
.
Mocking
Use
pytest-mock
for mocking. pytest-mock is enabled by default and installed in the base environment mentioned above. To use a mocker object simply pass it as a parameter to your test function. The mocker can then be used to mock both the plugin class object and also external APIs.
Example:
def test_netskope_pull_success(mocker):
   mocker.patch("cte.plugins.netskope.main.NetskopePlugin.pull")
   pull_return_result = [
       Indicator(value="ind1", type=IndicatorType.MD5),
       Indicator(value="ind2", type=IndicatorType.SHA256),
       Indicator(value="ind3", type=IndicatorType.URL),
   ]
   NetskopePlugin.pull.return_value = pull_return_result
   ns = NetskopePlugin(None, None, None, logger)
   actual_pull = ns.pull()
   assert pull_return_result == actual_pull
To mock request module response for API calls (requests_mock Pytest plugin is installed with all the dependencies):
def test_fetch_threat_data_malware(requests_mock):
   endpoint_url = "https://example-api.com"
   mock_response_json = {
       'status': 'success',
       'data': [
           {
               'local_md5': 'ind1',
           },
           {
               'local_md5': 'ind2',
           },
           {
               'local_md5': 'ind3',
           },
       ]
   }
   requests_mock.get(endpoint_url, json=mock_response_json)
   config_dict = {
       "api_token": "abc",
       "tenant_name": "partners",
       "file_list": "test",
       "url_list": "sample",
       "threat_data_type": "URL",
       "is_pull_required": "Yes",
       "max_file_hash_cap": 8,
       "max_url_list_cap": 8,
   }
   ns = NetskopePlugin(config_dict, None, None, logger)
   actual_ind_list = ns.fetch_threat_data(
       endpoint_url,
       config_dict['api_token'],
       datetime.datetime.now(),
       time.time(),
       "malware"
   )
   indicator_list = [
       Indicator(value="ind1", type=IndicatorType.MD5),
       Indicator(value="ind2", type=IndicatorType.MD5),
       Indicator(value="ind3", type=IndicatorType.MD5),
   ]
   assert len(actual_ind_list) == len(indicator_list)
   for i in range(len(actual_ind_list)):
       assert actual_ind_list[i].value == indicator_list[i].value
Run Your Unit Tests
$ PYTHONPATH=. pytest
Deploy the Plugin on Cloud Exchange
Package the Plugin
Cloud Exchange expects the developed plugin to be in zip or tar.gz format.
Execute this command to zip the package:
zip -r sample_plugin.zip sample_plugin
Execute this command to generate tar.gz package:
tar -zcvf sample_plugin.tar.gz sample_plugin
Upload the Plugin
Use the zip or tar.gz file to deploy the plugin.
In Cloud Exchange, go to
Setting > Plugins
.
Click
Add New Plugin
.
Click
Browse
.
Select the zip or tar.gz file.
Click
Upload
.
Note
This plugin is supported for the Threat Exchange module only.
Add a Repository
To deploy your plugin on the Cloud Exchange platform, you can add a repository to store your plugin.
In Cloud Exchange, go to
Setting > Plugin Repository
.
Click
Configure New Repository
.
Enter a Repository name, Repository URL, Username, and Personal Access Token.
Click
Save
.
Go to
Settings > Plugins
.
Select the Repository name from the Repository dropdown.
In this Topic
Threat Exchange Custom Plugin Developers Guide

---
## ThreatQ Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/threatq-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:54:47+00:00
**Scraped:** 2026-08-11T07:19:13.718882+00:00

ThreatQ Plugin for Threat Exchange - Netskope Technical Documentation
ThreatQ Plugin for Threat Exchange
This document explains how to configure the ThreatQ v1.1.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. The ThreatQ plugin is used to fetch the indicators of type URL, IP (IPv4, IPv6), FQDN, SHA256, and MD5 from the
ThreatQ Library > Indicators
page on the ThreatQ platform. This plugin does not support sharing of indicators to the ThreatQ platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Secure Web Gateway subscription for URL sharing.
A Threat prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A ThreatQ instance.
Connectivity to the following host: URL of the ThreatQ instance
Example: https://
<IP>
/ ; here the IP is the IP of the machine where your ThreatQ instance is hosted.
ThreatQ Plugin Support
The ThreatQ plugin fetches the indicators of type URL, IP (IPv4, IPv6), FQDN, SHA256, and MD5 from the ThreatQ platform. This plugin does support the sharing of indicators.
Fetched Indicator Types
Shared Indicator Types
URL, IP (IPv4, IPv6), FQDN, SHA256 and MD5
Not Supported
Mappings
Pull Mapping
Netskope CE Fields
ThreatQ Fields
value
value
type
type
reputation
score
active
status
extendedInformation
<THREATQ URL>
/indicators/
<IOC ID>
/details
tags
tags (Tags associated with the indicator)
Note that all the statues on ThreatQ except
Expired
will be considered as
Active
in Cloud Exchange.
Severity Mapping
Netskope CE Severity
ThreatQ Score
Critical
10
High
9
Medium
8
Medium
7
Low
6
Low
5
Low
4
Low
3
Low
2
Low
1
Low
0
API Details
This plugin uses Python libraries to authenticate with the ThreatQ API and fetch indicators from the ThreatQ platform.
Library
: threatqsdk (version = ‘1.8.0’)
Create a ThreatQ Object
tq = Threatq(
     host,
     (client_id, client_secret),
     private=True,
     verify=verify,
     proxy=proxy_info,
)
Fetch Indicators
FIELDS = [“id”, “value”, “type”, “score”, “status”, “tags”]
tlsearch = ThreatLibrary(tq, fields=FIELDS)
Give all the TL Search results using ThreatQ Search Names
tlsearch.get_saved_search(search_name).execute(
                "indicators"
)
Performance Matrix
Here is the performance reading conducted for fetching and pushing 100K IOCs in each plugin lifecycle on a Large CE instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from ThreatQ
~23k IOCs per minute
User Agent
netskope-ce-5.1.1-cte-threatq-v1.1.0
Workflow
Get your ThreatQ Client ID and Client Secret.
Create a Search name on ThreatQ.
Configure the ThreatQ Plugin.
Configure a Business Rule for ThreatQ.
Configure Sharing for ThreatQ.
Validate the ThreatQ Plugin.
Click play to watch a video.
Get your ThreatQ Client ID and Client Secret
Log in to your ThreatQ VM.
Run the following command to generate a Client ID and Client Secret.
sudo /var/www/api/artisan threatq:oauth2-client --name=Netskope
Copy the Client ID and Client Secret. These are needed to configure the ThreatQ plugin.
Create a Search Name on ThreatQ
In your ThreatQ instance, go to
Threat Library > Indicators
.
Apply the filters as per your requirements.
For example, filter indicators of type MD5.
Click
Save As
to create the search name.
Name your Data collection.
Click
Save Data Collection
.
Note that the name of your Data collection will be used as Search name while configuring the ThreatQ plugin.
Configure the ThreatQ Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
ThreatQ v1.1.0 (CTE)
plugin box.
For Basic Information, enter these parameters:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave the default.
Aging Criteria: Expiry time of the plugin in days. ( Default: 90 )
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enables SSL Certificate validation.
Use System Proxy: Enable if proxy is required for communication.
Click
Next
.
For Configuration Parameters, enter these values:
ThreatQ URL: This is the URL to the ThreatQ instance.
ThreatQ Client ID: This is the ThreatQ Oauth2 Client ID.
ThreatQ Client Secret: This is the ThreatQ Oauth2 Client Secret.
ThreatQ Search Names: These are the ThreatQ search names that contain the data to be imported. This should be a comma-separated list of search names, or a single search name.
Note that if one of the provided search names doesn’t exist on ThreatQ instance, or if it is invalid, then you won’t be able to save the configuration.
Click
Save
.
Configure a Threat Exchange Business Rule for ThreatQ
To share indicators fetched from the ThreatQ to the Cloud Exchange, you need to have a business rule that will filter out the indicators that you want to share. To configure a business rule:
Go to
Threat Exchange > Business Rule
and click
Create New Rule
.
Add filters according to your requirements in the rule, and then click
Save
.
Configure Threat Exchange Sharing for ThreatQ
To share IoCs from the Netskope CE to the Netskope tenant:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE ThreatQ), a Business Rule, a Destination Configuration (CTE Netskope), and a Target.
Click
Save
.
Validate the ThreatQ Plugin
Validate the Pull
To check the pulled IoCs, go to
Logging
and search for IoCs with plugin name.
Pulled data will be listed at
Threat IoCs
. You can filter the IoCs pulled from the platform using the filter
: sources.source Like “<plugin name>”
We can validate the pulled IoCs at
Threat IoCs
:
To check the available IoCs pulling on the ThreatQ platform, go to
ThreatQ Platform > ThreatLibrary > Indicators.
Note that if you need to filter the IoCs based on the search names used while configuring the plugin.
Validate the Retraction
You can filter the logs related to retraction by using the filter:
sources.source Like “<plugin configuration name> [Retraction]”
.
Note that for the ThreatQ plugin, the working of retraction is based on the ThreatQ Search names. This means only those indicators will be marked retracted, which were already pulled and later on they are not present in the provided search names ( For example: Either the indicators were deleted from the source platform, or the search name in the plugin configuration was updated).
You can validate the same at
Threat IoCs
:
Note that the retraction will only work for Active indicators. The Inactive indicators will not be marked as retracted in Cloud Exchange.
This plugin does not support sharing of IoCs to the ThreatQ platform, but the IoCs pulled from ThreatQ plugin can be shared to other third party platforms. When the IoCs shared from ThreatQ to a 3rd-party are deleted from that platform, then it will be marked as
“<plugin-config-name>: retracted”
in the Retraction Result. If they are not deleted from the 3rd-party platform, the Retraction Result will be pending or else be retracted.
IoCs pulled from ThreatQ were shared to a URL List
CTE Demo
on the Netskope tenant.
If any of the shared IoCs are marked as retracted in Cloud Exchange, it would be deleted from the Netskope tenant as well. Here, you can see the IoCs which were marked
Retracted “Yes”
in the retraction screenshot, and were also deleted from the URL List on the Netskope tenant.
Troubleshooting the ThreatQ Plugin
Unable to configure the ThreatQ plugin
It might be due to one of these reasons:
Invalid configuration parameters
SSL verification
What to do:
Identify the root cause and follow the steps for solution.
Invalid configuration parameters. Follow the steps in the
Configure the ThreatQ Plugin
section to verify the configuration parameters are valid.
SSL verification: You might encounter this error for SSL verification.
03/21/2025 5:25:51 PM
–
error
CTE ThreatQ [CTE ThreatQ]: Unexpected validation error occurred while authenticating. Error: HTTPSConnectionPool(host=’10.50.1.21′, port=443): Max retries exceeded with url: /api/token?grant_type=client_credentials (Caused by SSLError(SSLCertVerificationError(1, ‘[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1147)’)))
If your ThreatQ instance is hosted on a local machine, then you need to disable the SSL verification while configuring the plugin.
Unable to pull IOCs from the ThreatQ platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IoCs are available on the platform to pull
No IoCs are available related to the provided search name on the platform to pull
What to do:
Identify the root cause and apply the solution.
If no IoCs are available on the platform to pull, check if the IoCs are present on the platform to pull.
To verify IoCs, go to
ThreatQ Platform > ThreatLibrary > Indicators
.
If
no IOCs are available related to the provided search name on the platform to pull, filter the records on the ThreatQ based on the search name used while configuring the plugin.
To verify IoCs, go to
ThreatQ Platform > ThreatLibrary > Indicators
.
For example, you can see the IoCs for Search name
“All_indicators”
in the below screenshot:
Getting an error for Invalid ThreatQ Search Name(s)
ThreatQ Search Names field accepts comma separated values and if one of the provided values is invalid which means that search name does not exist on your ThreatQ instance then you will encounter the below error.
03/21/2025 6:05:19 PM
–
error
CTE ThreatQ [CTE ThreatQ]: Invalid ThreatQ Search Name(s) provided in configuration parameters. Error: No saved searches match the name provided
What to do:
Verify whether all the provided Search Names are present on your ThreatQ instance and if any of the Search Name is not present, then you can follow the steps in the
Configure the ThreatQ Plugin
section.
In this Topic
ThreatQ Plugin for Threat Exchange

---
## Trend Vision One Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/trend-micro-vision-one-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:55:39+00:00
**Scraped:** 2026-08-11T07:19:16.176563+00:00

Trend Vision One Plugin for Threat Exchange - Netskope Technical Documentation
Trend Vision One Plugin for Threat Exchange
This document explains how to configure the Trend Vision One plugin with the Cloud Threat Exchange module of the Netskope Cloud Exchange platform. This plugin supports pulling and sharing of URLs, domains, SHA256 file hashes, and IP addresses to Netskope that have been identified by Trend Micro Vision One.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Secure Web Gateway subscription for URL sharing.
A Threat Protection subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Trend Vision One Authentication token.
Access to a Trend Vision One portal:
Australia (
https://portal.au.xdr.trendmicro.com/
)
European Union (
https://portal.eu.xdr.trendmicro.com/
)
India (
https://portal.in.xdr.trendmicro.com/
)
Japan (
https://portal.xdr.trendmicro.co.jp/
)
Singapore (
https://portal.sg.xdr.trendmicro.com/
)
United States (
https://portal.xdr.trendmicro.com/
)
Connectivity to the following host:
https://api.xdr.trendmicro.com
.
Trend Micro Vision One Plugin Support
This plugin supports pulling data from the Suspicious Object List under Suspicious Object Management from the Trend Vision One platform. This plugin also supports sharing of IoCs to the Suspicious Object List and Exception List.
Fetched indicator types
URL, IPv4, IPv6, SHA256, Domain
Shared indicator types
URL, IPv4, IPv6, SHA256, Domain
Mappings
Type Mapping
CE IoC Types
Trend Vision One IoC Types
URL
Domain URLs IPv4 IPv6
SHA256
File SHA-256
Severity Mapping
CE Severity Fields
Trend Vision One Severity Fields
unknown
high
low
low
medium
medium
high
high
critical
high
Pull Mapping
Netskope CE Fields
Trend Vision One Fields
value
indicator_value
type
type
comments
description
LastSeen
lastModifiedDateTime
severity
risklevel
Push Mapping
Netskope CE Fields
Trend Vision One Fields
value
indicator_value
description
description
severity
risklevel
Permissions
Below are the permissions needed for the plugin.
Threat Intelligence > Suspicious Object Management.
View, filter, search
Yes
Manage lists and configure settings
Yes
API Details
List of APIs used
API Endpoint
Method
Use Case
/v3.0/threatintel/suspiciousObjects
GET
To pull indicators.
/v3.0/threatintel/suspiciousObjects
POST
To push indicators to Suspicious Object List
/v3.0/threatintel/suspiciousObjectExceptions
POST
To push indicators to Exception List
Pull Indicators
API Endpoint:
/v3.0/threatintel/suspiciousObjects
Method:
GET
Parameters:
Key
Value
orderBy
string
startDateTime
string <date-time>
endDateTime
string <date-time>
top
integer
Headers:
Key
Value
Authorization
Bearer <Authentication Token>
User-Agent:
<USER AGENT>
Content-Type
application/json
Accept
application/json
API Request Endpoint
:
https://api.in.xdr.trendmicro.com//v3.0/threatintel/suspiciousObjects
Sample Response
:
{
  "items": [
         {
              "url": "https://*.example.com/path1/*",
              "type": "url",
              "description": "object description",
              "lastModifiedDateTime": "2019-03-15T07:44:27Z"
         }
     ],
  "nextLink":    "https://api.xdr.trendmicro.com/v3.0/xdr/threatintel/suspiciousObjects?top=50&skipToken=eyJpZCI6IjI1MGQxMmE3ZDQyMmVhM"                  
}
Push Indicators
API Endpoints:
/v3.0/threatintel/suspiciousObjects
/v3.0/threatintel/suspiciousObjectExceptions
Method:
POST
Request Body
:
[
      {
"url": "https://*.example.com/path1/*",
"description": "object description"
       }
]
Headers
:
Key
Value
Authorization
Bearer <Authentication Token>
User-Agent:
<USER AGENT>
Content-Type
application/json
Accept
application/json
API Request Endpoints
:
https://api.in.xdr.trendmicro.com//v3.0/threatintel/suspiciousObjects https://api.in.xdr.trendmicro.com//v3.0/threatintel/suspiciousObjectExceptions
Sample Response
:
207 Multiple status code
[
  {
    "status": 201
  }
]
Performance Matrix
This reading is conducted on a Large CE Stack with these specs by pulling and pushing 100K IoCs.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Trend Vision One
~20K per minute
Indicators shared with Trend Vision One
~12K per minute
User Agent
netskope-ce-5.0.0-cte-trend-vision-one-v1.0.2
Workflow
Create User Roles.
Get your Authentication Token.
Configure the Trend Vision One plugin.
Configure a business rule for Trend Vision One.
Configure sharing for Netskope and Trend Vision One.
Validate the Trend Vision One plugin.
Click play to watch a video.
Get your Trend Vision One Authentication Token
Create User Roles
In order to generate the API Key, you need to create a user role. Follow these steps to configure the User Role on Trend Vision One.
Login to your Trend Vision One platform and go to
Administration > User Roles
.
Click
Add Role
and provide a Role name, and then go to the Permissions tab.
Scroll down to
Threat Intelligence > Suspicious Object Management
and select these permissions.
View, filter and search
Manage lists and configure settings
Click
Submit
and your Role will be saved and used for generating the API Key.
Generate an API Key
In to Trend Vision, go to
Administration > API Keys.
Click
Add API Keys
.
Add a Name, select the previously created role, and select an expiration time.
Click
Add
. Save the key to use it to configure the plugin, and it will only be visible once.
Configure the Trend Vision One Plugin
In Cloud Exchange, go to
Settings
and click
Plugins
.
Search for and select the
Trend Micro Plugin
box to open the plugin creation pages.
Enter and select the Basic Information on the first page:
Configuration Name: Enter a name appropriate for your integration.
Sync Interval: Adjust to environment needs. We recommend not to go below 5 minutes for production environments.
Aging Criteria: Expiration Date for indicators.
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL verification: Enable if SSL verification is required for communication.
Use System Proxy: Enable if proxy is required for communication
Click
Next
.
Enter and select these Configuration Parameters:
Data Region: Select a Region for your Trend Vision One account.Authentication Token: Enter your Trend Vision One Authentication Token obtained previously.Enable Polling: Enable to start pulling data.Initial Range (in days): Enter an Initial range to fetch indicators.
Click
Save
.
Configure a Threat Exchange Business Rule for Trend Vision One
To share indicators fetched from Trend Vision One to the Netskope and vice versa, you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule, follow these steps:
In Threat Exchange,  go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirement in the rule.
Configure Threat Exchange Sharing for Trend Vision One
To share IoCs from the Netskope CE to the Trend Vision One platform or vice versa, follow these steps:
In Threat Exchange, go to
Sharing
. Click
Add Sharing Configuration
.
Select your Source Configuration (Netskope CTE), the Business Rule, Destination Configuration (Trend Vision One), and Target (Suspicious Object List).
Click
Save
.
Add another Sharing configuration, but select Trend Vision One as the Source Configuration, and Netskope CTE as the Destination Configuration, plus the Business Rule and desired Target (like URL List or File Hash List). When finished, click
Save
.
Validate the Trend Vision One Plugin
Validate the Pull
To verify the data pulled from the Trend Vision One platform, follow these steps.
Go to
Logging
and filter the pull logs from the Trend Vision One plugin.
Data from Trend Vision One is pulled from the Threat Intelligence > Suspicious Object Management > Suspicious Object List.
Validate the Push
Indicators pushed from CE can be checked from Logging. Search filter to check the IoCs pushed to Trend Vision One platform.
Pushed data on Trend Vision One will be listed on either the Suspicious Object list or Exception list page from Suspicious Object Management under Threat Intelligence, depending on the target page selected while configuring the sharing.
The pushed IoCs on Trend Vision One can identified based on the default description added from CE, like Created from Netskope CTE.
Troubleshooting
Indicators are not pulled from the Trend Vision One platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of the following.
IoCs are not available on the platform to pull
IoCs are not available for the given time range
Available IoCs are pushed from CE
Unable to push IoCs to Trend Vision One
What to do:
Identity your root cause from the list above and follow these steps to resolve the issue.
No IoCs are available on the platform to pull
Check if the IoCs are available on the platform to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in CE, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Trend Vision One platform, check if you have data for the given time range.
Available IoCs are pushed from CE
If the IoCs are available on the platform and yet not pulled, check the description of the IoCs. IoCs that are shared from CE will have a default description, like Created from Netskope CTE.
And those IoCs will not be pulled back in CE.
Unable to push IoCs to Trend Vision One
If you are not able to push the IoCs on the platform and receiving error while pushing, it might be due to either:
Insufficient permission for the API Key (Authentication token)
Platform has reached it limit for IoCs
What to do:
Identify the reason for IoCs not being pushed. Check if the User has sufficient permissions. If sufficient permissions are added and the IoCs are still not pushed, check the count of each type of IoCs that you are trying to push on Trend Vision One to check if the limit exceeded for the IoCs.
If the domain that you are trying to share has multiple /, it won’t be shared to the Trend Vision One platform, as the platform itself does not consider a domain with multiple / as a valid domain.
Limitation
Observed that we are only able to push 10K IoCs of each type on the Trend Vision One’s Suspicious Object List page and around ~300 IoCs in total on the Exception List page.
In this Topic
Trend Vision One Plugin for Threat Exchange

---
## Update Configured Threat Exchange Plugins
**URL:** https://docs.netskope.com/en/update-configured-threat-exchange-plugins/
**Last Modified:** 2025-10-31T23:29:26+00:00
**Scraped:** 2026-08-11T07:19:21.025843+00:00

Update Configured Threat Exchange Plugins - Netskope Technical Documentation
Update Configured Threat Exchange Plugins
Write-access users can update already configured plugins.
On the Plugin page, you can edit, disable/enable, and delete the configuration using the icons on the top of each configuration tile.
When you delete a configuration, the UI prompts the admin with an option to keep the threat data in the Threat Exchange database if there are any IoC derived from the configured plug-in configuration. If the associated IoC are kept, they continue to be displayed in the Threat Exchange database with the previous configuration name in each of their metadata.
Note
If another configuration was rebuilt with the same name and using the same plugin, the legacy data will be bound to any new data gathered by the new configuration.
In this Topic
Update Configured Threat Exchange Plugins

---
## View Configured Threat Exchange Plugins
**URL:** https://docs.netskope.com/en/view-configured-threat-exchange-plugins/
**Last Modified:** 2025-10-31T23:25:57+00:00
**Scraped:** 2026-08-11T07:19:35.661357+00:00

View Configured Threat Exchange Plugins - Netskope Technical Documentation
View Configured Threat Exchange Plugins
Write-access users can view the list of configured plugins and the status.
Go to
Threat Exchange
and click
Plugins
.
A list of configured plugins is displayed in the Configured Plugins section. Each plugin configuration is displayed as a card. There can be multiple plugin configurations for each vendor, each performing a task (sharing IoC, filtering, pulling IoC from Threat Exchange) a different way to the same or different vendor systems.
The following details are displayed on each tile:
Logo of the plugin vendor.
Name: The configuration name provided while configuring that plugin.
Plugin Status: Enabled or Disabled. If it is actively polling, the word
running
will be shown next to the arrow.
Retrieved from: This timestamp indicates the most recent occasion when the Indicators were fetched from the plugin platform.
Pushed to: This timestamp denotes the last instance when the Indicators were sent to this plugin.
In this Topic
View Configured Threat Exchange Plugins

---
## View Threat Exchange Business Rules
**URL:** https://docs.netskope.com/en/view-threat-exchange-business-rules/
**Last Modified:** 2025-10-31T23:49:11+00:00
**Scraped:** 2026-08-11T07:19:38.095297+00:00

View Threat Exchange Business Rules - Netskope Technical Documentation
View Threat Exchange Business Rules
You can view business rules in list view or grid view, and toggle between Grid and List views using the button besides the Refresh button.
Click the list icon to see the List View.
Click the blocks icon to see Grid View.
You can expand each folder to see the business rules in that folder, and also delete a whole folder of business rules.
You can use the settings icon to choose which fields to be viewed in the column.
In this Topic
View Threat Exchange Business Rules

---
## Schedule Auto-Upgrade for the Content and Threat Feed Packages
**URL:** https://docs.netskope.com/en/schedule-auto-upgrade-for-the-content-and-threat-feed-packages/
**Last Modified:** 2025-08-31T01:43:04+00:00
**Scraped:** 2026-08-11T07:25:42.999012+00:00

Schedule Auto-Upgrade for the Content and Threat Feed Packages - Netskope Technical Documentation
Schedule Auto-Upgrade for the Content and Threat Feed Packages
Scheduling an auto-upgrade ensure you always have the latest Netskope products. The auto-upgrade procedure for both the content and threat feed packages are the same except for specific code strings for each within the commands.
To schedule an auto-upgrade for the content or threat-feed packages:
Go to the Netskope shell:
nsshell
Enter
configure
To schedule the auto-upgrade, enter one of these commands:
set auto-upgrade content period daily at
<specify hour in 24 hour format>
or
set auto-upgrade threat-feed period daily at
<specify hour in 24 hour format>
For example, to schedule an auto-upgrade at 1.00 am everyday, enter one of these commands:
set auto-upgrade content period daily at 01:00
or
set auto-upgrade threat-feed period daily at 01:00
In this Topic
Schedule Auto-Upgrade for the Content and Threat Feed Packages

---
## Threat Protection
**URL:** https://docs.netskope.com/en/threat-protection-115996/
**Last Modified:** 2025-09-01T12:49:04+00:00
**Scraped:** 2026-08-11T07:25:48.158839+00:00

Threat Protection - Netskope Technical Documentation
Threat Protection
The Dataplane On-Premises appliance uses threat protection to detect malware and malicious sites. To use threat protection, contact
support@netskope.com
and get the license to enable this feature in your tenant UI.
For information on configuring threat protection in your tenant UI, see
Configure Threat Protection for API Data Protection
.
You can disable threat protection by running the following command.
set dataplane tssfastscan enable false
In this Topic
Threat Protection

---
## Cybereason Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/cybereason-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:40:32+00:00
**Scraped:** 2026-08-11T07:26:20.906296+00:00

Cybereason Plugin for Threat Exchange - Netskope Technical Documentation
Cybereason Plugin for Threat Exchange
This document explains how to configure the v1.1.0 Cybereason plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. The Cybereason plugin is designed to fetch the IoCs (Domain, IPv4, IPv6, MD5, and SHA256) from the
Security Profile > Reputations
page, and store them in Cloud Exchange. Additionally, the plugin supports sharing of IoCs (Domain, IPv4, IPv6, MD5, and SHA256) to the Cybereason
Security Profile > Reputations
page.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Netskope Threat Prevention subscription for malicious file hash sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured
Your Cybereason account username and password.
Connectivity to the following host:
https://integration.cybereason.net:8443
.
Cybereason Plugin Support
Fetched indicator types
SHA256, MD5, Domain, IPv4, IPv6
Shared indicator types
SHA256, MD5, Domain, IPv4, IPv6
Permissions
To access this plugin you will need admin access to your Cybereason platform. Contact the Cybereason team for admin access.
Mappings
Pull Mapping
Netskope CE Fields
Cybereason Fields
Value
Value
Type
Type
First Seen
Added On
Last Seen
Last Modified
Push Mapping
Netskope CE Fields
Cybereason UI Fields
Comment
Description
Value
Value
Permissions
To access this plugin, you will need admin access to your Cybereason platform. Contact the Cybereason team for admin access.
API Details
List of APIs used
API Endpoint
Method
Use Case
/login.html
POST
To authenticate the plugin
/rest/classification/reputations/list
POST
To Pull Reputations (IoCs)
/rest/classification/upload
POST
To Push Reputations (IoCs)
To Authenticate
API Endpoint:
https://
<baseurl>
/login.html
Method:
POST
Headers
Key
Value
User-Agent
<User Agent>
Content-Type
application/x-www-form-urlencoded
Cookie
<Cookie>
Accept
application/json
Payload:
Key
Value
username
<username>
password
<password>
Sample API Response:
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Cybereason</title>
    <meta name="viewport" content="width=device-width">
    <link rel="shortcut icon" href="favicon.ico">
</head>
<body class="cbr-theme-light">
    <app></app>
    <script type="text/javascript">
        (function () {
        var loadScript = function({ uri, async, onLoad, onError, attrs }) {
        var isSync = async === undefined ? true : async;
        const script = document.createElement('script');
        script.setAttribute('type', 'text/javascript');
        script.setAttribute('src', uri);
        script.async = isSync;
        if (onLoad) script.onload = onLoad;
        if (onError) script.onerror = onError;
        if (attrs && attrs.length) attrs.forEach(function (attr) {script.setAttribute(attr.name,       attr.val)});
        document.body.appendChild(script);
    };
    var loadCSS = function(uri) {
        const head = document.getElementsByTagName('head')[0];
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = uri;
        link.media = 'all';
        head.appendChild(link);
    };
	var attrs = [{ name: 'data-shell-sdk-url', val: 'rest/uimodules/js/shell-sdk' }];
    function loadFallbackGlobalStyles() {
        loadScript({ uri: '/externals/cbr-global-styles-1.4.1.js' });
    }
    function requireGlobalStyles() {
        var initRuntimesPromise = window.CbrInfraShell &&       window.CbrInfraShell.initRuntimesPromise;
		if (initRuntimesPromise) {
    		initRuntimesPromise.then(() => {
       			require(['@cbr/global-styles']);
    		}).catch(() => {
                loadFallbackGlobalStyles();
            })
		} else {
            loadFallbackGlobalStyles();
        }
    }
    function loadFallback() {
        window.__isLoadShellFallback__ = true;
        var fallbSrc = '/rest/uimodules/js/shell-sdk/latest/shell.js';
        loadScript({ uri: fallbSrc, async: false, onLoad: requireGlobalStyles, onError: loadFallbackGlobalStyles, attrs });
    	// prevent chaching by adding query param
        loadCSS('/public/common.css?23.2.120');
        loadCSS('/public/vendors.css?23.2.120');
        loadCSS('/public/app.css?23.2.120');
        loadScript({ uri: '/public/common.js?23.2.120' });
        loadScript({ uri: '/public/vendors.js?23.2.120' });
        loadScript({ uri: '/app.js?23.2.120' });
        loadScript({ uri: '/externals/pendo.js' });
    }
    var tenant = window.location.hostname.split('.')[0];
    var _shellSdkUri = (window?.localStorage && window?.localStorage.getItem('shell.shellSdkUri')) || '';
    var shellSrc = (_shellSdkUri || '/rest/dynamic/v1/ui-infra-shell/public-api/js/shell.js') + '?pVersion=23.2.120&tenantId='+ tenant;
    loadScript({ uri: shellSrc, async: false, onLoad: requireGlobalStyles, onError: loadFallback, attrs });
})();
    </script>
</body>
</html>
Pull Reputations (IoCs)
API Endpoint:
https://
<baseurl>
/rest/classification/reputations/list
Method:
POST
Headers:
Key
Value
User-Agent
<User Agent>
Content-Type
application/json
Sample Payload:
{
  "filter": {
    		"includeExpired": true,
  	   },
  "page": 0,
  "size": 20
}
Sample API Response
{
    "outcome": "success",
    "data": {
        "reputations": [
            {
                "key": "2001:0db8:0:0:0:ff00:42:8888",
                "reputationType": "IP",
                "isBlocking": false,
                "maliciousType": "blacklist",
                "comment": "",
                "expiration": -1,
                "owningUser": "gjenkins@netskope.com",
                "firstSeen": 1713948991801,
                "lastUpdated": 1713948991801,
                "additionalKeys": [],
                "lookupKeyType": "IPV6"
            }
        ],
        "total": 1
    }
}
Push Reputations (IoCs)
API Endpoint:
https://
<baseurl>
/rest/classification/upload
Method:
POST
Headers:
Key
Value
User-Agent
<User Agent>
Cookie
<cookie>
Payload:
Key
Value
classification_file
CSV file [Upload the reputations csv file]
Performance Matrix
Below is the performance reading conducted by pulling and sharing 100K indicators from/to Cybereason on a Large CE Stack with the below specifications.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Cybereason
~15K per minute
Indicators shared with Cybereason
~1K per minute
User Agent
netskope-ce-5.0.1-cte-cybereason-v1.1.0
Workflow
Get your Cybereason instance information.
Configure the Cybereason Plugin.
Configure a business rule for Cybereason.
Configure sharing between Netskope and Cybereason.
Validate the Cybereason Plugin.
Click play to watch a video.
Get your Cybereason Information
For configuring the Cybereason plugin, you will need the Base URL, Username, and Password from your Cybereason instance.
Username:
Username of your Cybereason platform.
Password:
Password of your Cybereason platform.
Configure the Cybereason Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
Cybereason
plugin box.
For Basic Information, enter these values:
Configuration Name: Unique name for the configuration.
Sync Interval: Interval to fetch data from this plugin source.
Aging Criteria: Expire indicators after a specific time.
Override Reputation: Set value to override the reputation of indicators.
Enable SSL verification: Enable if SSL verification is required for communication.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
For Configuration Parameters, enter these values:
Base URL: URL of Cybereason console from which you want to fetch the data.
Username: API username/Username to access the Cybereason platform.
Password: API Password/Password of the Cybereason platform.
Enable Polling: Enable if you want to fetch data.
Click
Save
.
Add a Threat Exchange Business Rule for Cybereason
To share the indicators to Cybereason, add a business rule to filter out the data that you want to share. To do this, follow these steps.
Go to
Threat Exchange > Business rule
.
Click
Create New Rule
.
Add a Rule name and create filters per your requirements, like those shown below.
Click
Save
.
Configure Threat Exchange Sharing for Cybereason
Configure Sharing in order to share the IoCs with Cybereason.
In Threat Exchange, go to
Sharing
.
Click
Add Sharing Configuration
.
Click on the
Source Configuration
dropdown and choose Netskope (or any source plugin that you want to share IoCs from).
Click the
Business Rule
dropdown and select the Business Rule created earlier.
Click the
Destination Configuration
dropdown and select Cybereason.
For sharing IoCs, click on the
Target
dropdown and choose
Share Indicators
.
For sharing URLs, click on the
Target
dropdown and choose
Add to URL List
. Enter the URL List name from your Netskope tenant and create a new list. Select the URL List Type, then enter a List Size and the Default URL.
For sharing hashes, click on the
Target
dropdown and choose
Add to File Hash List
. Enter the List Name (File Profile) from your Netskope tenant, and then enter a List Size.
Click
Save
.
Validate the Cybereason Plugin
Validate the Pull
Indicators from Cybereason are pulled from this page:
Security Profile > Reputation
.
Note that indicators that have a “created from netskope” description will not be pulled.
Indicators stored in Cloud Exchange can be verified from the
Threat Exchange > Threat IoCs
page.
Search the Cybereason IoCs by filtering indicators from Cybereason.
Example: Add a query on the Threat IoCs page like “sources.source Is equal “<plugin configuration name>”.
You can also verify the indicators pulled in Cloud Exchange from the logs available on the
Logging
page.
Validate the Push
Shared IoCs to Netskope/Cybereason can be verified from logs available on the
Logging
page of Cloud Exchange.
Troubleshooting
Unable to Validate/Push the data on the Cybereason Platform
If you are unable to view the data on the Cybereason platform, it could be due to one of these reasons:
URLs with invalid format (format not supported by Cybereason platform), example: protocol.subdomain.domainname are being shared for which the API returns a success message, but the whole batch of IoCs will not be shared.
Invalid (MD5, SHA256) IoCs are shared.
While pushing the data in batches, there could be server error from the Cybereason platform, and hence the batch push has been skipped.
To solve these issues:
Remove the URLs with invalid format (format not supported by Cybereason platform) protocol.subdomain.domainname and try to again share the IoCs using manual sync.
Verify in Cloud Exchange, there will be a log present which IoC is invalid. Remove the particular IoC and try to share the IoCs using manual sync.
Try to again push the data using manual sync.
Unable to pull the data from the Cybereason Platform
If you are unable to pull the data on the Cybereason platform, it could be due to one of these reasons:
No IOCs are present on the platform to pull.
API returning read timeout while pulling the IoCs.
Polling is set to “No” in the Cybereason plugin configuration.
To solve these issues:
Make sure that valid IOCs are present in the Cybereason if pulling is needed. If IOCs are present on the platform, check the description of the IOCs if it is “created from netskope” the IOCs will not be pulled as those are shared from CE itself.
Wait for API to recover the timeout issue.
Set Polling as “Yes” in the Cybereason plugin.
Known Behaviors
All the indicators will be shared as blacklist on the Cybereason Platform. Hence, you will see action in the Cybereason platform as “Detect Only”.
If any of the invalid IOCs are present in a batch for sharing, the whole batch will be ignored.
Once the pulling for all the pages is done, the pulling will again start from page 1, because there is no field in the API to implement the checkpoint mechanism.
In this Topic
Cybereason Plugin for Threat Exchange

---
## Illumio Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/illumio-plugin-for-threat-exchange/
**Last Modified:** 2026-06-02T02:58:09+00:00
**Scraped:** 2026-08-11T07:26:52.919665+00:00

Illumio Plugin for Threat Exchange - Netskope Technical Documentation
Illumio Plugin for Threat Exchange
Important
The Illumio plugin for the Threat Exchange Module in Cloud Exchange has been deprecated. Go
here
for more information.
In this Topic
Illumio Plugin for Threat Exchange

---
## Feedly Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/feedly-v1-0-0-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:56:43+00:00
**Scraped:** 2026-08-11T07:26:59.161634+00:00

Feedly Plugin for Threat Exchange - Netskope Technical Documentation
Feedly Plugin for Threat Exchange
This document explains how to configure the CTE Feedly v1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches SHA256 hashes, MD5 hashes, URLs, domains, and IP addresses from Feedly Stream. This plugin also fetches IoCs in MISP format from Feedly Stream.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Feedly Instance and access to your credentials: Feedly Stream ID, Feedly Enterprise Access Token.
Connectivity to the following host: https://feedly.com/.
Feedly Plugin Support
Functionality
Is available
Pull Functionality
Yes
Push Functionality
No
Permissions
Feedly Enterprise Access Token which user can get from Customer Success Manager will be have already needed permission for plugin.
Performance
Instance details:
RAM: 4 GB
CPU: 4 Core
Data
Time taken to store
100K
~25 mins
API Details
The plugin uses a Feedly third-party library to pull the indicators from the Feedly platform.
Refer to the official documentation for more information on the Feedly SDK.
https://github.com/feedly/python-api-client
The Feedly Enterprise Access Token will be obtained from the Feedly administrator. Refer to
Feedly documentation
for more information.
Workflow
Get your Feedly credentials.
Configure the Feedly Plugin for Threat Exchange.
Validate the Feedly plugin.
Click play to watch a video.
Get your Feedly Configuration Parameters
Create a Feed
Log in to your Feedly account.
Click the
Power Search
icon (as shown).
Select the Topics that you would like to subscribe to.
Select from your feed or
Across the Web
from the top.
For example, if you just wanted to fetch subscribe
Indicators of Compromise
, select it.
Click
Follow AI Feed
and select the folder in which you want to add the feed. For example, add in a Test Feed.
Click
Add
.
Enter the Feed Name and click
FOLLOW AI Feed
.
In a few seconds, your feed should be successfully created.
Get your Feedly Stream ID
Log in to your Feedly account.
Go to the Feed that you wanted to fetch from the Feedly dashboard.
You should see “
Test IoC feed for CTE Plugin”
.
Click on “
…
” in the top right corner and go to the sharing option.
Scroll down to the bottom and you’ll see the
Feedly Stream ID
field. Copy the value; you will need this to configure the Feedly plugin.
Get your Feedly Enterprise Access Token
If you are a Feedly Enterprise customer, please contact your customer success manager at enterprise@feedly.com
Configure the Feedly Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the Feedly plugin box to open the configuration page.
Add a Configuration Name, a Sync Interval, and enable Use System Proxy if needed for connectivity.
Click
Next
and Add the Feedly Stream ID, Feedly Enterprise Access Token, Type of IoCs, Enable Tagging and Initial Range(In Days)
Feedly Stream ID:
Stream Id you got previously.
Feedly Enterprise Access Token:
Access token you got previously.
Type of IoCs
: IoC types you want plugin to pull from Feedly Stream.
Enable Tagging
: Select yes if you want tags to be attached with indicators and select no if you don’t want them. By default yes will be selected.
If Yes is selected, then the tags that have more than 50 characters length will be skipped. But they will be present in the IoC comment.
Initial Range:
No. of days from when data needs to be pull on initial run.
Click
Save
.
Your new plugin configuration can be seen at
Threat Exchange > Plugins
.
Validate the Feedly Plugin
Validate in Cloud Exchange
Go to
Threat Exchange > Threat IoCs
.
Add a filter for the source configuration of Feedly.
You will see all the indicators fetched from the Feedly Stream on this page.
Validate in Feedly
Users can see the feeds made by them in the Team Feeds section of the Feedly dashboard.
IoCs is the feed name, and there are many feeds, as shown in the above image.
Now to see the indicators of the first feed, click on the feed. You’ll see something similar to what’s shown below.
Per the above screenshot, you can see that two IoCs were found. Specifically, there are two domains.
Users can also see the actual IoCs in the highlighted section. Refer to the below screenshot.
In this Topic
Feedly Plugin for Threat Exchange

---
## Threat and Data Protection for RBI
**URL:** https://docs.netskope.com/en/threat-and-data-protection-for-rbi/
**Last Modified:** 2025-08-31T01:46:40+00:00
**Scraped:** 2026-08-11T07:27:07.734443+00:00

Threat and Data Protection for RBI - Netskope Technical Documentation
Threat and Data Protection for RBI
This feature provides support for DLP and Threat Protection policies for file upload and download traffic through RBI. Admins can safely enable uploads and downloads in isolated browsing sessions, creating additional real-time protection policies to scan files for Threat Protection and DLP.
The integration of RBI with Netskope Threat Protection and Data Protection Microservices allows NG-SWG to process all traffic generated in isolation and brings additional benefits such as:
Configurable File Uploads and Downloads settings in RBI templates
Full visibility of user activity in isolation, leveraging app inline connectors to detect user activities
Leverage Threat Protection and DLP profiles for isolated and not-isolated traffic
Increased visibility over potential threats stopped by RBI
Localized content in isolation
The workflow for this feature includes:
Review your isolate policies and RBI templates to
enable uploads and/or downloads
(prerequisite).
Set up security policies (
Threat Protection
or
DLP
) to control uploads and downloads.
Review Skope IT Events (
Page
,
Application
) and
Alerts
.
Review
Malware and Malicious Sites
Incidents.
Review
DLP Incidents
.
Review
Best Practices
.
Enable File Downloads / Uploads in RBI Templates
RBI template settings for FIle Upload and File Download control whether users can initiate an upload or download operation within an isolated browsing session.
“File Upload / File Download” settings in RBI templates must be enabled as a prerequisite prior to creating Real-time Protection policies for Isolation (Threat Protection and Data Protection policies). Admins have to create or edit existing RBI templates that are used in conjunction with the isolate policies.
Navigate to
Policies > Real Time Protection > Review Suggestions
. This displays only the existing policies that have the
Action = Isolate
applied.
You can identify the RBI templates attached to the existing Isolate policies.
Tip
By default, Filed Upload and File Download settings are disabled in all existing RBI templates: “Predefined” and “Customer defined” RBI templates. If File Upload / File Download is not enabled, users browsing in isolation will see a warning message if they initiate uploads or downloads. To learn more:
Isolation in an End User’s Browser
Navigate to
Policies
>
Templates
>
RBI
> click
New Template
or edit an existing template. The RBI Template window displays.
Click File Upload and/or File Download.
Click Save.
To learn more:
RBI Templates
Create a DLP Policy for RBI File Upload and File Download
You can create a new or edit an existing DLP policy to control uploads and downloads in isolated traffic. To detect and prevent data loss (DLP) in isolated traffic the RBI template associated with the isolate policy should have the
File Upload / File Download settings enabled
. Netskope DLP service scans uploads and downloads for any data protection violations while browsing in isolation and applies the appropriate action.
Admins must place the DLP / Threat policies
before
the isolate policy to apply controls on the activity or content of the upload / download.
Navigate to
Policies > Real-time Protection > New Policy > DLP
to create a new DLP policy.
To identify the scope (Destination “categories”, “cloud apps”) of existing isolation policies, navigate to
Policies > Review Suggestions
. This displays only the existing policies that have the
Action = Isolate
applied.
Optionally, click
+ADD FILTER
to search for a specific policy or filter by
Action > Isolate
or
RBI Template
.
To learn more:
Real-time Protection policies
DLP Profiles
In general, all source and destination criteria for DLP policies are supported. Find below the most relevant criteria and supported values for DLP policies processing isolated traffic:
Destination
: Category, Application NoteTo learn more about the list of supported categories and applications for Targeted RBI and Extended RBI see:
RBI categories definitions
,
Extended RBI – web categories
,
Extended RBI – cloud apps
Activities
: Download, Upload
Action
: Alert, Allow, Block, User Alert
Activity Constraints
: File Type, File Size
Create a Threat Protection Policy for RBI File Upload and File Download
You can create a new or edit an existing Threat Protection policy to control uploads and downloads in isolated traffic. To detect and prevent data loss (DLP) in isolated traffic the RBI template associated with the isolate policy should have the
File Upload / File Download settings enabled
. Netskope Threat Protection service scans uploads and downloads for any data protection violations while browsing in isolation and applies the appropriate action.
Navigate to
Policies > Real-time Protection > New Policy > Threat Protection
to create a new Threat Protection policy.
To identify the scope (Destination “categories”, “cloud apps”) of existing isolation policies, navigate to
Policies > Review Suggestions
. This displays only the existing policies that have the
Action = Isolate
applied.
Optionally, click
+ADD FILTER
to search for a specific policy or filter by
Action > Isolate
or
RBI Template
.
To learn more:
Real-time Protection policies
Threat Protection policies
In general, all source and destination criteria for DLP policies are supported. The following criteria are the most relevant supported values for Threat Protection policies processed in isolated traffic.
Destination
: Category, Application
Activities
: Download, Upload
Note
Only Download and Upload are supported for isolated traffic. Any other activity (e.g. Edit, Share, etc.) is not supported.
Action
: Alert, Allow, Block, User Alert
Activity Constraints
: File Type, File Size
Activity Constraints
Skope IT Events
Once a violation / match of a Threat Protection or DLP policy is detected for a file upload or download, Netskope policy, Data Protection, and Threat Protection engines generate Skope IT application events, page events, and alerts.
Skope IT Application Events
Application events related to RBI include the following RBI specific fields:
From Isolation: values include “yes”, “no”
RBI template ID
RBI template name
Application events that correspond to activities performed by the user while browsing an isolated webpage display “yes” in the From Isolation column.
Requests that match an isolate policy but were not isolated (not isolable content) generate an Application event “no” in the From Isolation column. To learn more about best practices for no isolated traffic, refer to:
Create Real-time Protection Policies fo
r content that you cannot isolate
.
For certain generated application events, you can also view a corresponding Skope IT alert. This is signified by the orange dot by the timestamp column.
Tip
The ‘From Isolation’ column is specific to application events related to RBI. For any application event not related to RBI, values in the ‘From Isolation’ column may remain blank.
Click the gear icon to customize columns, From Isolation. The From Isolation values include:
yes: The application event happens in an isolated browsing session.
no: The application event corresponds to a request processed by RBI, but not isolated (not a webpage).
empty: The application event is not related to RBI.
Click
+Add Filter
to filter From Isolation or Alert Type for a more granular view.
Click
Export
to export From Isolation activity.
View Application Event Details.
Skope IT Alerts
Alerts related to RBI include the following RBI specific fields:
From Isolation: values include “yes”, “no”
RBI template ID
RBI template Name
Alerts that correspond to activities performed by the user while browsing an isolated webpage display “yes” in the From Isolation column.
Alerts corresponding to requests that match an isolate policy but were not isolated (not isolable content) generate an Alert entry listed as “no” in the From Isolation column. To learn more about best practices for no isolated traffic, refer to:
Create Real-time Protection Policies for content that you cannot isolate
.
Tip
RBI related alerts share the same RBI specific fields with RBI related application events. The ‘From Isolation’ column is specific to application events related to RBI. For any application event not related to RBI values, the ‘From Isolation’ column may remain blank.
View Skope IT Alert Details
Skope IT Page Events
Navigate to
Skope IT
>
Page Events
to view related activity for isolated browsing sessions.
Isolated browsing sessions generate two page events.
The first page event with the Action column showing “isolate” shows that an isolated browsing session took place and summarizes the traffic corresponding to the RBI protocol that handles communication between the user and RBI.
The second page event with the Action column left blank (for the same website) summarizes the browsing activity of the RBI browsing session on behalf of the user.
Malware and Malicious Sites
If malware is detected in an isolated browsing session, Netskope RBI creates an alert for you to review and act on.
Navigate to
Incidents
>
Malware
to search for malware detected in isolation.
Navigate to
Incidents
>
Malicious Sites
to search for malsites detected in an isolated browsing session.
Click the Maliste name to view the alert information. Malsites visited in isolation are identified by the “isolate” action.
Malware infected files uploaded or downloaded in isolation are detected as malware by Netskope and generates a regular alert with “Detection” listed in the Action column.
You will see “yes” listed in the From Isolation column for Action Type “policy” alerts. And for Action Type “Malware” alerts, the From Isolation column is blank.
You will typically see two alerts, one for the policy (including the RBI specific field “From isolation”) and one for malware.
DLP Incidents
If a DLP violation is detected in an isolated browsing session, Netskope DLP detects it and creates an alert for you to review and act on. You will typically see two alerts, one for the policy and one for DLP.
1. Navigate to
Incidents
>
DLP
.
2. Click a DLP alert to view the incident details.
3. Click the Violations Alerts icon to view the alert details.
Alert details
Best Practices
This section contains best practices which will grow as input is gathered.
Policy Ordering
Policy ordering is important as outlined below:
Admins must place the DLP / Threat policies
before
the isolate policy to apply controls on the activity or content of the upload / download.
Refer to the following help topic to handle any content you cannot isolate that may reach the RBI platform:
Create Real-time Protection policies for content that you cannot isolate
Netskope Browser and Client User Notifications
Users can configure both browser and client user notifications to alert the user to a given action that is blocked or requires user justification. In conjunction with Threat and Data Protection for RBI, browser notifications are supported for web applications that support them.
Client notifications will not be presented to end users in certain situations upon a policy violation if the customer configures client based notifications or if the isolated web application does not support browser based notifications.
This limitation only affects the user notification, the action assigned to the policy violation (alert, block, etc.) is applied. For blocked uploads or downloads the browser will present a file upload / download failure.
The following is an example of a browser based user notification template your end users may see upon violation in isolation.
Browser based notification for a DLP alert:
File Size and Type Limitations
RBI sets a 400 MB file size limit for file uploads and file downloads. In addition, DLP and Threat Protection services have their own default file sizes. To learn more:
Advanced File Scanning
In this Topic
Threat and Data Protection for RBI

---
## SecurityScorecard Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/securityscorecard-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:48:51+00:00
**Scraped:** 2026-08-11T07:27:16.339498+00:00

SecurityScorecard Plugin for Threat Exchange - Netskope Technical Documentation
SecurityScorecard Plugin for Threat Exchange
This document explains how to configure the SecurityScorecard integration with the Threat Exchange module of the Netskope Cloud Exchange platform. This integration allows for the pulling of domains from SecurityScorecard as URLs into Netskope.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
Secure Web Gateway subscription for URL sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
SecurityScorecard License (Pro, Business, Enterprise).
Connectivity to the following host:
https://platform.securityscorecard.io/
SecurityScorecard Plugin Support
Fetched indicator types
URL
Companies having these Issues will be fetched from SecurityScorecard and stored in Netskope as URLs.
web_vuln_host_high
redirect_to_insecure_website
web_vuln_host_low
web_vuln_host_medium
local_file_path_exposed_via_url_scheme
communication_with_server_certificate_issued_by_blacklisted_country
communication_server_with_expired_cert
domain_missing_https_v2
links_to_insecure_website
uses_log4j
website_defacement
ransomware_association
alleged_breach_incident
ransomware_victim
adware_installation
adware_installation_trail
anonymous_proxy
attack_detected
malware_controller
malware_infection
malware_infection_trail
phishing
pva_installation
pva_installation_trail
exploited_product
ransomware_infection
ransomware_infection_trail
suspicious_traffic
threat_actor_hosting_infrastructure
tlscert_expired
tlscert_revoked
tlscert_self_signed
tlscert_excessive_expiration
tlscert_weak_signature
tlscert_no_revocation
product_uses_vulnerable_log4j
ssh_weak_protocol
ssh_weak_cipher
ssh_weak_mac
tls_weak_protocol
tls_weak_cipher
patching_cadence_high
service_vuln_host_high
patching_analysis_high
patching_cadence_low
service_vuln_host_low
patching_analysis_low
patching_cadence_medium
service_vuln_host_medium
patching_analysis_medium
patching_cadence_info
service_vuln_host_info
Workflow
Get your SecurityScorecard API token.
Configure the SecurityScorecard Plugin.
Validate the SecurityScorecard Plugin.
Click play to watch a video.
Get your SecurityScorecard API Token
To generate API Token using a Bot User, follow the steps provided in
this
document. Also store API Token in your secrets as it appears only once.
Log in into your SecurityScorecard platform.
Click
User Profile Menu
in the top right corner.
Click
My Settings
.
Click
API
in the left menu bar.
Click
Generate new API Token
, and then copy the token and store it in safe location. The API appears only once.
Configure the SecurityScorecard Plugin
Log in to Cloud Exchange.
Go to
Settings > Plugins
.
Click on the SecurityScorecard plugin tile.
Enter the Basic Information:
Configuration Name: Unique name for the plugin configuration.
Sync Interval: Interval to fetch data from the plugin source. Recommendation is 24 hours.
Aging Criteria: Expiry time of the indicators in days. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this plugin configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if proxy is required for communication.
Click
Next
.
Enter the Configuration Parameters:
API Token: The API Token you got earlier.
Portfolios: Comma-separated Portfolio names for which we need to pull the indicators.
Company Grade Threshold: Company grade threshold filter (Options: A, B, C, D, F). IoCs will be generated for URLs with the specified SecurityScorecard grade and lower.
Severity: Only the tags of issues for specified severity will be fetched (Options: Positive, Info, Low, Medium, High).
Click
Save
.
Configure Sharing for the SecurityScorecard Plugin
In Threat Exchange, click
Sharing
and enter the following field values:
Source: Source plugin of which  you want to share the data.
Business rule: Select a business rule that you want to apply to IoCs.
Destination: Destination plugin where you want to push the data.
Target: Possible destination or action that use IoCs while pushing the data.
After saving the configuration, click
Sync
.
Add Time period for that you want to share data, click
Fetch
, and then click
Sync
. Check
All time
to share all the data from source plugin.
Validate the SecurityScorecard Plugin
Pulling of Indicators
Based on the Plugin configuration Indicators will be pulled from the SecurityScorecard. Go to
Threat Exchange > Threat IoCs
to view the received IoCs.
Sharing of Indicators
Verify sharing indicators from
Threat Exchange > Threat IoCs
. Expand one of the Source plugin IoCs and check status of Shared with Parameter.
Log in to the Netskope UI. Go to
Policies > Web > URL Lists
and locate your URL list.
Click on the list and verify the URLs.
For more information, go to
Logging
in the left panel.
In this Topic
SecurityScorecard Plugin for Threat Exchange

---
## CrowdStrike Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/crowdstrike-plugin-for-threat-exchange-2/
**Last Modified:** 2026-05-27T23:40:14+00:00
**Scraped:** 2026-08-11T07:27:17.792018+00:00

CrowdStrike Plugin for Threat Exchange
This document explains how to configure the CrowdStrike v2.3.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches Threat IoCs of type Hash (MD5 and SHA256), Domains, IPv4, IPv6 from CrowdStrike’s Endpoint detections and the IoC management page.
This plugin supports sharing the Threat IoCs to CrowdStrike’s IoC management page and can perform Isolate/Remediate actions for hosts. Only file hash IoCs activate prevention; Domain, IPv4, IPv6 don’t trigger prevention in CrowdStrike. Sharing URL information from Netskope Cloud Exchange to CrowdStrike is not recommended, as CrowdStrike currently only supports ingesting SHA256, MD5, Domain, IPv4, and IPv6.
To access the plugin, you need the API credentials. This plugin supports the pull and push retraction of IoCs from Crowdstrike.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A CrowdStrike instance.
Connectivity to any one of the following hosts:
Commercial cloud (api.crowdstrike.com)
US 2 (api.us-2.crowdstrike.com)
Falcon on GovCloud (api.laggar.gcw.crowdstrike.com)
EU cloud (api.eu-1.crowdstrike.com)
If you have the IP allowlist configured on CrowdStrike, make sure to add the public IP of the machine where cloud exchange is running. For more information, refer to the
documentation
.
CrowdStrike Plugin Support
This plugin fetches Threat IoCs of type Hash (MD5 and SHA256), Domains, IPv4, IPv6 from CrowdStrike’s Endpoint detections and IoC management page. This plugin supports sharing the Threat IoCs to CrowdStrike’s IoC management page and can perform Isolate/Remediate actions for hosts. Only file hash IoCs activate prevention; Domain, IPv4, IPv6 don’t trigger prevention in CrowdStrike. Sharing URL information from Cloud Exchange to CrowdStrike is not recommended, as CrowdStrike currently only supports ingesting SHA256, MD5, Domain, IPv4, and IPv6. To access the plugin, you need the API credentials. This plugin supports pull and push retraction of IoCs from Crowdstrike.
Fetched indicator types
Shared indicator types
SHA256, MD5, Domain, IPv4, IPv6
SHA256, MD5, Domain, IPv4, IPv6
IoC Retraction
IoC Retraction (Pull): Indicators will be fetched from CrowdStrike, and in the subsequent pull cycles, if some indicators are deleted on CrowdStrike, then they will be marked as Retracted in Cloud Exchange.
IoC Retraction (Push): Retracted indicators present on Cloud Exchange will be deleted from CrowdStrike during sharing.
Retraction Type
Supported
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
Yes
Permissions
Scope
Read
Write
Alerts
Yes
No
IoC Management
Yes
Yes
Hosts
Yes
Yes
IoCs (Indicators of Compromise)
Yes
No
Mappings
Here are the fields that are pulled and pushed from CrowdStrike and mapped in Cloud Exchange.
Endpoint Detection Page Mappings
Cloud Exchange Fields
CrowdStrike API Response Fields
value
ioc_value
type
ioc_type
comments
IoC Description:
description
if
ioc_context.ioc_description
is empty, else
ioc_context.ioc_description
Pattern Disposition Description:
pattern_disposition_description
Pattern Disposition Value:
pattern_disposition
firstSeen
updated_timestamp
lastSeen
updated_timestamp
severity
severity
reputation
confidence/10
tags
[“CrowdStrike-Endpoint-Detections”]
Severity Mappings for Endpoint Detection
Netskope Severity
CrowdStrike Severity
Low
10-39
Medium
40-69
High
70-89
Critical
90-100
Unknown
0 or greater than 100
IoC Management Page Mappings
Cloud Exchange Fields
CrowdStrike API Response Fields
value
value
type
type
severity
severity
firstSeen
created_on
lastSeen
modified_on
comment
Format: Comment format: Source:
<Source Value>
,
action:
<Action Value>
, platforms:
<Platform Value>
, metadata fields:
<Metadata Value>
Combination of Source, action, platforms, and metadata fields.
tags
tags + [“non-CrowdStrike-discovered”]
Severity Mappings for IoC Management
Cloud Exchange Severity
CrowdStrike Severity
Unknown
Informational
Low
Low
Medium
Medium
High
High
Critical
Critical
Mappings for Pushed IoCs
CrowdStrike API Payload Fields
Cloud Exchange Fields/Default Values
value
value
type
type
description
comments
severity
severity
tags
tags
expiration
expiresAt
action
Action selected in action parameter
Possible values: [“no_action”, “allow”, “prevent_no_ui”, “prevent”, “detect”]
source
Netskope – Cloud Threat Exchange |
<Source Plugin Name>
Example: Netskope – Cloud Threat Exchange | MISP
platforms
Platforms selected in the action parameters.
Possible values are: [“windows”, “mac”,”linux”]
Note that Severity will only be mapped for CrowdStrike supported actions only. So, the severity will not be mapped for actions like Block, Hide Detection, and Allow.
API Details
List of APIs Used
Use Case
Method
Endpoint
API Scope
Get auth token
POST
/oauth2/token
None
Pull updated indicators from Endpoint Detections page
POST
/alerts/combined/alerts/v1
Alerts (Read)
Pull indicators from Custom IoC Management, check for modified IoCs, and check the existence of indicators on IoC Management
GET
/iocs/combined/indicator/v1
IoC Management (Read)
Push indicators to Custom IoC Management
POST
/iocs/entities/indicators/v1
IoC Management (Write)
Pull the host IDs from the indicator value for the Isolate/Remediate action
GET
indicators/queries/devices/v1
IoCs (Indicators of Compromise) (Read)
Perform Isolate/Remediate action
POST
/devices/entities/devices-actions/v2
Hosts (Write)
Get Auth Token
API Endpoint:
/oauth2/token
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Payload
Parameter
Value
grant_type
client_credentials
client_id
<Client ID>
client_secret
<Client Secret>
Sample API Response
{
    "access_token": "",
    "expires_in": 1799,
    "token_type": "bearer"
}
Pull Updated Indicators from Endpoint Detection Page
API Endpoint:
/alerts/combined/alerts/v1
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Payload
Key
Value
Description
filter
updated_timestamp:>=’2020-06-02T00:00:00.927384Z’+ioc_type:[‘hash_md5′,’hash_sha256′,’md5′,’sha256′,’domain’,’ipv4′,’ipv6′]
+ioc_source:!*’Netskope – Cloud Threat Exchange*’
+pattern_disposition:![1,2,3,4]
Filters from last timestamp+ioc_type filter
+excludes IoCs created by plugin
+excludes pattern disposition values
sort
updated_timestamp|asc
Sorts updated_timestamp by descending
limit
1000
Default batch size of 1000
after
<id>
ID of the next page to fetch if total is more than the given limit
Sample API Response
{
    "meta": {
        "query_time": 0.138995532,
        "pagination": {
            "total": 142,
            "limit": 100,
            "after": "eyJ2ZXJzaW9uIjoidjEiLCJ0b3RhbF9oaXRzIjoxNDIsInRvdGFsX3JlbGF0aW9uIjoiZXEiLCJjbHVzdGVyX2lkIjoiZjNjMiIsImFmdGVyIjpbMTc0ODUyNjI2NTk0MywxNzQ4NTI5ODY3NTc1LCJjMTdmM2E4MGRlZDA0MThlYjEwN2RiM2QyNmEyNzk4MzppbmQ6MDNkY2FjNGI4NzJmNGQyNjg0NjQzZDIyOTJjMzhiMDE6MjU4Mjk0MDkwODQzNC01NzM0LTEzOTI0MzY4Il0sInRvdGFsX2ZldGNoZWQiOjEwMH0="
        },
        "powered_by": "detectsapi",
        "trace_id": "1aa55d82-077e-4725-b390-25429b6a0f4c"
    },
    "errors": [],
    "resources": [
        {
            "agent_id": "7c566a5cc4ee4248a83d0405d7273a49",
            "aggregate_id": "aggind:7c566a5cc4ee4248a83d0405d7273a49:137439072286",
            "alleged_filetype": "exe",
            "associated_files": [],
            "child_process_ids": [
                "pid:7c566a5cc4ee4248a83d0405d7273a49:297786408684"
            ],
            "cid": "c17f3a80ded0418eb107db3d26a27983",
            "cloud_indicator": "true",
            "cmdline": "\"C:\\Program Files (x86)\\Microsoft\\EdgeUpdate\\Install\\{856B848F-38B5-4946-921B-FB2F7713213E}\\MicrosoftEdge_X64_137.0.3296.68.exe\" --msedge --verbose-logging --do-not-launch-msedge --system-level --channel=stable",
            "composite_id": "c17f3a80ded0418eb107db3d26a27983:ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143",
            "confidence": 100,
            "context_timestamp": "2025-06-18T04:57:29Z",
            "control_graph_id": "ctg:7c566a5cc4ee4248a83d0405d7273a49:137439072286",
            "crawled_timestamp": "2025-06-18T05:57:51.199159695Z",
            "created_timestamp": "2025-06-18T04:58:51.562849229Z",
            "data_domains": [
                "Endpoint"
            ],
            "description": "A SHA256 hash matched a Custom Intelligence Indicator (Custom IOC) with low severity.",
            "device": {
                "agent_load_flags": "0",
                "agent_local_time": "2025-06-17T22:47:44.249Z",
                "agent_version": "7.24.19607.0",
                "bios_manufacturer": "VMware, Inc.",
                "bios_version": "VMW201.00V.24006586.B64.2406042154",
                "cid": "c17f3a80ded0418eb107db3d26a27983",
                "config_id_base": "65994767",
                "config_id_build": "19607",
                "config_id_platform": "3",
                "device_id": "7c566a5cc4ee4248a83d0405d7273a49",
                "external_ip": "61.219.78.165",
                "first_seen": "2025-02-17T17:21:36Z",
                "groups": [
                    "1012add21d3e4e08b146dbfdb37c5ca0"
                ],
                "hostinfo": {
                    "domain": ""
                },
                "hostname": "DESKTOP-LQDIGUR",
                "last_seen": "2025-06-18T05:48:27Z",
                "local_ip": "10.66.2.89",
                "mac_address": "00-0c-29-ee-47-37",
                "machine_domain": "",
                "major_version": "10",
                "minor_version": "0",
                "modified_timestamp": "2025-06-18T05:52:52Z",
                "os_version": "Windows 10",
                "ou": null,
                "platform_id": "0",
                "platform_name": "Windows",
                "product_type": "1",
                "product_type_desc": "Workstation",
                "status": "contained",
                "system_manufacturer": "VMware, Inc.",
                "system_product_name": "VMware20,1"
            },
            "display_name": "CustomIOCHashLow",
            "email_sent": true,
            "external": true,
            "falcon_host_link": "https://falcon.crowdstrike.com/activity-v2/detections/c17f3a80ded0418eb107db3d26a27983:ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143?_cid=g03000nb3ghi5x4fappp2bjsndr5ej4q",
            "filename": "MicrosoftEdge_X64_137.0.3296.68.exe",
            "filepath": "\\Device\\HarddiskVolume3\\Program Files (x86)\\Microsoft\\EdgeUpdate\\Install\\{856B848F-38B5-4946-921B-FB2F7713213E}\\MicrosoftEdge_X64_137.0.3296.68.exe",
            "files_written": [
                {
                    "filename": "setup.exe",
                    "filepath": "\\Device\\HarddiskVolume3\\Program Files (x86)\\Microsoft\\EdgeUpdate\\Install\\{856B848F-38B5-4946-921B-FB2F7713213E}\\EDGEMITMP_60DE1.tmp",
                    "timestamp": "1749829318"
                }
            ],
            "global_prevalence": "common",
            "grandparent_details": {
                "cmdline": "C:\\Windows\\system32\\services.exe",
                "filename": "services.exe",
                "filepath": "\\Device\\HarddiskVolume3\\Windows\\System32\\services.exe",
                "local_process_id": "904",
                "process_graph_id": "pid:7c566a5cc4ee4248a83d0405d7273a49:296364257770",
                "process_id": "296364257770",
                "sha256": "4a912dc98c977788131aad0ae468d86792211ed225f80b2c344a3690b4437428",
                "timestamp": "2025-06-13T04:55:18.990Z",
                "user_graph_id": "uid:7c566a5cc4ee4248a83d0405d7273a49:S-1-5-18",
                "user_id": "S-1-5-18",
                "user_name": "DESKTOP-LQDIGUR$"
            },
            "id": "ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143",
            "indicator_id": "ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143",
            "ioc_context": [
                {
                    "ioc_source": "primary_module",
                    "ioc_type": "sha256",
                    "ioc_value": "5219f66e6cab3aa843f6e89ee3d47d32,d757eb8b567d76eb19f7009adbb9d013c7cf1861f45b18a023d6866e8baa2a2d",
                    "type": "ioc"
                }
            ],
            "ioc_source": "primary_module",
            "ioc_type": "sha256",
            "ioc_value": "5219f66e6cab3aa843f6e89ee3d47d32,d757eb8b567d76eb19f7009adbb9d013c7cf1861f45b18a023d6866e8baa2a2d",
            "local_prevalence": "unique",
            "local_process_id": "1868",
            "logon_domain": "WORKGROUP",
            "md5": "5219f66e6cab3aa843f6e89ee3d47d32",
            "name": "CloudDetect-CustomerIOC-SHA256-Low",
            "objective": "Falcon Detection Method",
            "parent_details": {
                "cmdline": "\"C:\\Program Files (x86)\\Microsoft\\EdgeUpdate\\MicrosoftEdgeUpdate.exe\" /svc",
                "filename": "MicrosoftEdgeUpdate.exe",
                "filepath": "\\Device\\HarddiskVolume3\\Program Files (x86)\\Microsoft\\EdgeUpdate\\MicrosoftEdgeUpdate.exe",
                "local_process_id": "4336",
                "md5": "c019e421d9f897108e51666cbae2c8b0",
                "process_graph_id": "pid:7c566a5cc4ee4248a83d0405d7273a49:297758877134",
                "process_id": "297758877134",
                "sha256": "3096d8e82917a9b73f322f4b1743e52e9b0c8b3c5933a957e73e29d6973cdd5b",
                "timestamp": "2025-06-16T10:26:29Z",
                "user_graph_id": "uid:7c566a5cc4ee4248a83d0405d7273a49:S-1-5-18",
                "user_id": "S-1-5-18",
                "user_name": "DESKTOP-LQDIGUR$"
            },
            "parent_process_id": "297758877134",
            "pattern_disposition": 0,
            "pattern_disposition_description": "Detection, standard detection.",
            "pattern_disposition_details": {
                "blocking_unsupported_or_disabled": false,
                "bootup_safeguard_enabled": false,
                "containment_file_system": false,
                "critical_process_disabled": false,
                "detect": false,
                "fs_operation_blocked": false,
                "handle_operation_downgraded": false,
                "inddet_mask": false,
                "indicator": false,
                "kill_action_failed": false,
                "kill_parent": false,
                "kill_process": false,
                "kill_subprocess": false,
                "mfa_required": false,
                "operation_blocked": false,
                "policy_disabled": false,
                "prevention_provisioning_enabled": false,
                "process_blocked": false,
                "quarantine_file": false,
                "quarantine_machine": false,
                "registry_operation_blocked": false,
                "response_action_already_applied": false,
                "response_action_failed": false,
                "response_action_triggered": false,
                "rooting": false,
                "sensor_only": false,
                "suspend_parent": false,
                "suspend_process": false
            },
            "pattern_id": 5311,
            "platform": "Windows",
            "poly_id": "AADBfzqA3tBBjrEH2z0monmDgEHElB4TLZI4zzCC9NmU_gAATiEItOfbNan5F65GbEhxGr5sIpuo7GVQmBmbrXDpFsSf8Q==",
            "priority_explanation": [
                "[MOD] The parent process was identified as: MicrosoftEdgeUpdate.exe"
            ],
            "priority_value": 87,
            "process_id": "297785683156",
            "process_start_time": "1749829315",
            "product": "epp",
            "scenario": "intel_detection",
            "seconds_to_resolved": 0,
            "seconds_to_triaged": 0,
            "severity": 30,
            "severity_name": "Low",
            "sha1": "0000000000000000000000000000000000000000",
            "sha256": "d757eb8b567d76eb19f7009adbb9d013c7cf1861f45b18a023d6866e8baa2a2d",
            "show_in_ui": true,
            "source_products": [
                "Falcon Insight"
            ],
            "source_vendors": [
                "CrowdStrike"
            ],
            "status": "new",
            "tactic": "Custom Intelligence",
            "tactic_id": "CSTA0005",
            "technique": "Indicator of Compromise",
            "technique_id": "CST0005",
            "timestamp": "2025-06-18T04:57:29.681Z",
            "tree_id": "137439072286",
            "tree_root": "297785683156",
            "triggering_process_graph_id": "pid:7c566a5cc4ee4248a83d0405d7273a49:297785683156",
            "type": "ldt",
            "updated_timestamp": "2025-06-18T05:57:51.199148989Z",
            "user_id": "S-1-5-18",
            "user_name": "DESKTOP-LQDIGUR$"
        }
    ]
}
Pull Indicators from IoC Management, Check for Modified IoCs, and Check the Existence of indicators on IoC Management
Endpoint:
/iocs/combined/indicator/v1
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Parameters
Key
Value
Description
limit
2000
Max limit for 1 page.
offset
Empty string for first API call and add limit to for next API calls, like offset+=limit.
The offset to start retrieving records from.
after
WzE2NjU1MTQ1MDQzODYsIjEzM2U2YzUwNjA5NzJjYmEyY2UwODg2ODQ3
MzRiMzc1ZTZkZGFlMzNjNTlmNzJhYjFkZmQ0NTlmNmVhY2QzMWYiXQ==
A pagination token used with the limit parameter to manage pagination of results. On your first request, don’t provide an ‘after’ token. On subsequent requests, provide the ‘after’ token from the previous response to continue from that place in the results.
To access more than 10k indicators, use the ‘after’ parameter instead of ‘offset’.
filtertype: [‘md5’,’sha256’, ’domain’,’ipv4’,ipv6’] + modified_on:> ‘2023-07-08T01:01:41Z’Perform filtering on the basis of indicator type and the modified time of indicator.sortmodified_onSort indicators on modified time.
Sample API Response
{
  "meta": {
    "query_time": 0.035081512,
    "pagination": {
      "limit": 1,
      "total": 640,
      "offset": 1,
      "after": "WzE2ODkyNjE2NjI2MjcsIjM4MDI2Yzk5MzQ1ZGI5NDE4NGMwYTY3MTIwOGUwZGQwNWY4NmNjNzlhMmI2NTRjNTVjNzg0NTQ5YzZiYmMxNzAiXQ=="
    },
    "powered_by": "ioc-manager",
    "trace_id": "0dddfbcf-e93f-4ae0-b143-6c79912224cb"
  },
  "errors": null,
  "resources": [
    {
      "id": "38026c99345db94184c0a671208e0dd05f86cc79a2b654c55c784549c6bbc170",
      "type": "md5",
      "value": "00000d9007e7a6b0842e802957137079",
      "source": "Netskope_CSPlugin_v3",
      "action": "detect",
      "severity": "high",
      "metadata": {
        "filename": "unused"
      },
      "platforms": [
        "windows"
      ],
      "expired": false,
      "deleted": false,
      "applied_globally": true,
      "from_parent": false,
      "created_on": "2023-07-13T15:21:02.627637187Z",
      "created_by": "cc5fc723039543d29a796a349d2f1525",
      "modified_on": "2023-07-13T15:21:02.627637187Z",
      "modified_by": "cc5fc723039543d29a796a349d2f1525"
    }
  ]
}
Match IoC Existence on IoC Management
API Endpoint:
/iocs/combined/indicator/v1
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Parameters
Key
Value
limit
2000
filter
Value: [
<IoC Values>
]
Sample API Response
{
    "meta": {
        "query_time": 0.022017219,
        "pagination": {
            "limit": 100,
            "total": 1,
            "offset": 1,
            "after": "WzE3MTI1NjE2NTU2MzIsImY4NjU1ZDM2OTJiNDllNjVhNWEzMmRmYTM4N2QzZTI3NTk3NTRhOGI0Y2ZjNDI0YzhmODBmZDY1NzZjMGJjOGEiXQ=="
        },
        "powered_by": "ioc-manager",
        "trace_id": "8ab48640-e2ef-4cf0-b631-d33f897defb1"
    },
    "errors": null,
    "resources": [
        {
            "id": "f8655d3692b49e65a5a32dfa387d3e2759754a8b4cfc424c8f80fd6576c0bc8a",
            "type": "md5",
            "value": "4309e189b0e68c2c0f554dd4202d00bd",
            "source": "Netskope_CSPlugin_v3",
            "action": "detect",
            "severity": "high",
            "metadata": {
                "filename": "testpdv_5e67ccdec797303d7973900c3c1ed399_4309e189b0e68c2c0f554dd4202d00bd_1712561301_sha256-blacklist-sample.txt"
            },
            "platforms": [
                "windows"
            ],
            "expired": false,
            "deleted": false,
            "applied_globally": true,
            "from_parent": false,
            "created_on": "2024-04-04T15:42:22.809754471Z",
            "created_by": "cc5fc723039543d29a796a349d2f1525",
            "modified_on": "2024-04-08T07:34:15.632004689Z",
            "modified_by": "cc5fc723039543d29a796a349d2f1525"
        }
    ]
}
Update an Indicator on IoC Management
API Endpoint:
iocs/entities/indicators/v1
Method:
PATCH
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Payload
Key
Value
Description
indicators
[{
“id”: “f8655d3692b49e65a5a32dfa387d3e2759754a8b4cfc424c8f80fd6576c0bc8a”,
“source”: “Netskope_CSPlugin_v3”,
“action”: “no_action”,
“platforms”: [“windows”],
“applied_globally”: true,
“severity”: “critical”,
“tags”: [“netskope-ce”],
“type”: “md5”,
“description”: “This is a test indicator.”,
“value”: “4309e189b0e68c2c0f554dd4202d00bd”
}]
List of dictionaries containing indicator payloads.
comment
Indicators updated from Netskope Cloud Exchange.
Sample API Response
{
    "meta": {
        "query_time": 0.253615007,
        "pagination": {
            "limit": 0,
            "total": 1
        },
        "powered_by": "ioc-manager",
        "trace_id": "8dd3a607-8bec-46f5-a79c-9692d6d92818"
    },
    "errors": null,
    "resources": [
        {
            "id": "f8655d3692b49e65a5a32dfa387d3e2759754a8b4cfc424c8f80fd6576c0bc8a",
            "type": "md5",
            "value": "4309e189b0e68c2c0f554dd4202d00bd",
            "source": "Netskope_CSPlugin_v3",
            "action": "no_action",
            "severity": "critical",
            "description": "This is a test indicator.",
            "metadata": {
                "filename": "testpdv_5e67ccdec797303d7973900c3c1ed399_4309e189b0e68c2c0f554dd4202d00bd_1712565995_sha256-blacklist-sample.txt"
            },
            "platforms": [
                "windows"
            ],
            "tags": [
                "netskope-ce"
            ],
            "expired": false,
            "deleted": false,
            "applied_globally": true,
            "from_parent": false,
            "created_on": "2024-04-04T15:42:22.809754471Z",
            "created_by": "cc5fc723039543d29a796a349d2f1525",
            "modified_on": "2024-04-08T08:52:28.142410877Z",
            "modified_by": "61794791c7554fecab6a975090f98f6d"
        }
    ]
}
Push an Indicator to IoC Management
API Endpoint:
iocs/entities/indicators/v1
Method:
PATCH
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Data
Key
Value
Description
indicators
[
{
“action”: “allow”,
“applied_globally”: true,
“description”: “This is a test indicator from netskope.”,
“platforms”: [
“linux”
],
“severity”: “High”,
“source”:
“Netskope – Cloud Threat Exchange | netskope”
,
“tags”: [
“netskope”
],
“type”: “md5”,
“value”: “d60fbc101972fe1ed086fdf05b520dfa”
}
]
List of dictionaries containing indicator payloads.
comment
Indicators shared from Netskope Cloud Exchange.
Get Host IDs from Indicator Value
API Endpoint:
/indicators/queries/devices/v1
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Parameters
Key
Value
Description
type
md5
Indicator types possible values are sha256, md5, domain, ipv4 and ipv6.
value
4309e189b0e68c2c0f554dd4202d00bd
Hash or Actual IoC Value.
limit
100
Max limit for hosts.
offset
“”
Empty string or offset got from previous API call.
Sample API Response
{
    "meta": {
        "query_time": 6.8e-8,
        "pagination": {
            "offset": "",
            "limit": 100
        },
        "trace_id": "2039578c-1e94-4e56-a2c7-58bea1c12857",
        "entity": "/devices/entities/devices/v1{?ids*}"
    },
    "resources": [
        "9d4f598cec024ac2bf3c5e2afdc69129",
        "331c40581b7a4d4a81863bf630edc868"
    ],
    "errors": []
}
Retract (Delete) IoCs from IoC Management
API Endpoint:
/iocs/entities/indicators/v1
Method:
DELETE
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Parameters
Key
Value
limit
2000
filter
Value:[“d60fbc101972fe1ed086fdf05b520dfa”] + modified_on:>=’2024-11-28T17:15:15Z’
Sample API Response
{
  "meta": {
    "query_time": 0.228808146,
    "pagination": {
      "limit": 0,
      "total": 1
    },
    "powered_by": "ioc-manager",
    "trace_id": "be320583-bf85-4edd-bace-f851b784dbe6"
  },
  "errors": null,
  "resources": null
}
Get Host IDs from an Indicator Value
API Endpoint:
/indicators/queries/devices/v1
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Parameters
Key
Value
Description
type
md5
Indicator types possible values are sha256, md5, domain, ipv4 and ipv6
value
4309e189b0e68c2c0f554dd4202d00bd
Hash or Actual IOC Value
limit
100
Max limit for hosts
offset
“”
Empty string or offset got from the previous API call.
Sample API Response
{
    "meta": {
        "query_time": 6.8e-8,
        "pagination": {
            "offset": "",
            "limit": 100
        },
        "trace_id": "2039578c-1e94-4e56-a2c7-58bea1c12857",
        "entity": "/devices/entities/devices/v1{?ids*}"
    },
    "resources": [
        "9d4f598cec024ac2bf3c5e2afdc69129",
        "331c40581b7a4d4a81863bf630edc868"
    ],
    "errors": []
}
Perform Isolate/Remediate Action
API Endpoint:
devices/entities/devices-actions/v2
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Authorization
Bearer
<Bearer Token>
Payload
Key
Value
action_parameters
[
{
“name”: “unhide_host”,
“value”: “unhide_host”
}
]
ids
[
<Host IDs>
]
Sample API Response
{
    "meta": {
        "query_time": 17.960566309,
        "powered_by": "device-api",
        "trace_id": "d7fa97da-83c3-4349-b870-e19d85983605"
    },
    "resources": [
        {
            "id": "331c40581b7a4d4a81863bf630edc868",
            "path": "/devices/entities/devices/v1"
        }
    ],
    "errors": []
}
Note
In the plugin, the Isolate/Remediate action is performed in batches, like for containment and lift containment, the batch size will be 5000, and for hide_host and unhide_host, the batch size will be 100.
Performance Matrix
Here is the performance reading conducted by pulling and sharing 100K indicators from/to CrowdStrike on a Large Cloud Exchange Stack with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from CrowdStrike’s IoC Management page
~20K per minute
Indicators fetched from CrowdStrike’s Endpoint Detection page
~27K per minute
Indicators shared with CrowdStrike
~1K per minute
User Agent
The user agent for this plugin is in the following format:
<vendor>
-
<integration name>
/
<version>
For example:
netskope-ce-5.1.2-cte-crowdstrike/2.3.0
Workflow
Create a custom File Profile.
Create a Malware Detection Profile.
Create a Real-time Protection Policy.
Get your CrowdStrike Client ID and Client Secret.
Configure the CrowdStrike Plugin.
Configure sharing between Netskope and CrowdStrike.
Validate the CrowdStrike Plugin.
Watch a Video
Click play to watch a video.
Get your CrowdStrike Client ID and Client Secret
Log in to your CrowdStrike platform and go to
Support and Resources > API Client and Keys
.
Click
Create API Client
. Add the Client name and provide the scopes listed in the
Permissions
section.
Copy the Client ID and Secret, and then click
Create
.
Get your Host ID for the Isolate/Remediate Hosts Action
To perform the Isolate/Remediate Hosts action it is mandatory to have the hosts for the IoCs on whom you want to perform the action for present on the CrowdStrike platform or the host on which you want to perform action on CrowdStrike should have some IoCs associated to that Hosts . To check the same follow these steps:
Copy the IoC that you want to use for performing the Isolate/Remediate action.
Go to the CrowdStrike platform and search the IoC on CrowdStrike’s Endpoint Detection page from the top left menu’s Endpoint Security.
You’ll see the detections listed as shown in above screenshot. Click on any one of the listed detections, and click
See full detection
on the bottom of the page.
Go to details, and scroll down to Hosts, you will find the host ID. Copy the Host ID.
Configure the CrowdStrike Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
CrowdStrike v2.3.0 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name: Plugin configuration name.
Sync Interval: Interval to fetch data from this plugin source.
Aging Criteria: Expire indicators after a specific time.
Override Reputation: Set value to override reputation of indicators received from this configuration. Leave empty to keep default.
Tags Aggregate Strategy: Select an option from the dropdown.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: If using a proxy, use system proxy configured in Settings.
Click
Next
.
Enter the Configuration Parameters:
Base URL: Base URL of CrowdStrike instance, like
https://api.crowdstrike.com
.
Client ID: Client ID generated from the CrowdStrike platform.
Client Secret: Client Secret generated from the CrowdStrike platform.
Enable Polling: Enable/Disable polling Threat IoCs from CrowdStrike. Disable if you only need to push Threat IoCs to CrowdStrike.
Indicator Source Page: The source page from which plugin should pull the indicators.
Type of Threat data to pull: Type of Threat data to pull. Allowed values are SHA256, MD5, Domain, IPv4 and IPv6.
Exclude Pattern Disposition values: Indicators with these pattern disposition values will not be pulled from the Endpoint Detections page. Add multiple values separated by comma(Example Format: 1,2,3). All indicators without a pattern_disposition field will be pulled. Refer the
CrowdStrike Documentation
to get the Pattern Disposition values.
Retraction Interval (in days): Retraction Interval days to run IoC(s) retraction for CrowdStrike indicators. Note that this parameter will only be considered if
IoC(s) Retraction
is enabled in Threat Exchange Settings.
Initial Range: Number of days Threat IoCs to pull in the initial run.
Indicator Batch Size: The origin of this Threat IoC. This field can be utilized to trace the origin of the IoC on the CrowdStrike Custom IOC. Limited to 200 characters.
Note that IoCs present on the IoC Management and Endpoint Detection pages in Crowdstrike UI won’t be pulled if the source is starting from
Netskope – Cloud Threat Exchange
.
Click
Save
.
Configure a Threat Exchange Business Rule for CrowdStrike
A Business Rule is used to filter out the indicators that are to be shared. In order to share IoCs with CrowdStrike, create a business rule using these steps:
Go to
Threat Exchange > Business Rules
and click
Create New Rule
.
Add the Rule name and select the fields through which you want to filter the IoCs.
Click
Save
.
Configure Threat Exchange Sharing for CrowdStrike
CrowdStrike v2.3.0 supports performing Remediate and Isolate actions on the Hosts. This plugin also updates the already shared Indicators on CrowdStrike when reshared.
CrowdStrike Actions
Perform Action
No Action
:
Save the indicator for future use, but take no action. No severity is required.
Allow
:
This applies to hashes only. Allow the indicator and do not detect it. Severity does not apply and should not be provided.
Block, Hide Detection
:
This applies to hashes only. Block and detect the indicator, but hide it from
Endpoint security > Monitor > Endpoint detections
. Has a default severity value.
Block: This applies to hashes only. Add the indicator to the Block list using which the prevention policy will block the processes on the host from which this indicator is generated.
Detect Only
:
Show it as detection and take no action on it.
Isolate/Remediate Hosts
Contain: Contains the host and stops any network communications to locations other than the CrowdStrike cloud and IPs specified in your containment policy.
Lift Containment: Lifts containment on the host and returns its network communications to normal.
Hide Host: Deletes a host. After the host is deleted, no new detections for the host will be reported via the UI or API. A maximum of 100 hosts can be hidden at a time.
Unhide Host: Restores a host if deleted. Detection reporting resumes after the host is restored.
To configure sharing:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select Source configuration (Source from which you want to share data to CrowdStrike), select a Business Rule, and Destination.
Select a Target value and Action type.
Click
Save
.
Validate the CrowdStrike Plugin
Validate the Pull
Indicators from CrowdStrike are pulled from these pages:
Endpoint security > Endpoint Detection
Endpoint security > IoC Management
Note that:
IoCs that have a Source other than
Netskope – Cloud Threat Exchange
will be pulled from CrowdStrike.
In the CrowdStrike UI,
Netskope – Cloud Threat Exchange
will be displayed as
Netskope Cloud Threat Exchange
.
Indicators stored in Cloud Exchange can be verified at
Threat Exchange > Threat IoCs
. Search the CrowdStrike IoCs by filtering indicators from CrowdStrike.
Example: Add a query on the Threat IoCs page like “
sources.source Is equal “CTE CrowdStrike” && type IN (“<IOC_TYPE>”)
“
You can also verify the indicators pulled in Cloud Exchange from the logs available at
Logging
in Cloud Exchange.
CTE CrowdStrike [CTE CrowdStrike]: Successfully fetched 141 indicator(s) for 141 alert(s) from CrowdStrike Endpoint Detections.
CTE CrowdStrike [CTE CrowdStrike]: Successfully fetched 6978 indicator(s) from CrowdStrike Custom IOC Management in total 4 pages.
Validate the Push
Shared IoCs to CrowdStrike can be verified from the logs available at
Logging
in Netskope Cloud Exchange.
Note that if the IoCs are already present on the CrowdStrike, it will be updated.
CTE CrowdStrike [CTE CrowdStrike]: Successfully shared 4 indicator(s) with CrowdStrike Custom IOC Management. 0 indicator(s) failed to be shared.
CTE CrowdStrike [CTE CrowdStrike]: Successfully filtered 4 indicators out of 4, received from the business rule.
IoCs shared on CrowdStrike can be verified from the
Endpoint security > IoC Management
page.
To verify the original source of indicator from which this was pulled in Cloud Exchange and shared to CrowdStrike. Check the Source Field for their particular IoC.
For example if indicator is shared from Netskope Threat Exchange plugin to CrowdStrike plugin then it will be shown as Netskope – Cloud Threat Exchange | Netskope Threat Exchange. Similarly if IOC is shared from MISP then it will be shown as Netskope – Cloud Threat Exchange | MISP. Check below screen-shot for reference.
When the IoCs shared from CrowdStrike to Third Party will be retracted it will be marked as “<plugin-config-name>: retracted” in the Retraction Result. If they are not deleted from the Third party the Retraction Result will be pending.
IoCs shared to perform isolate/remediate host action on the specific host on CrowdStrike can be verified from
Host setup and management >
Host Management
.
Search the host ID for associated with the particular hash for which the action has been performed and check the
Containment Status
.
Currently, the Status of the Host is
Normal
.
Add sharing to perform the
Contain
Operation on the host. After sharing has been initiated. Go to
Logging
and search for
Successfully executed
.
Go back to the CrowdStrike platform and check if the status has been changed or not. Follow the same steps for other Isolate/Remediate actions.
Validate the Retraction
For verifying the Retracted IoCs from CrowdStrike, check the logs for IoC Retraction example: ‘message Like
CTE CrowdStrike [configuration_name] [Retraction]
’
Note that the IoCs that are deleted on the CrowdStrike and fall outside the Retraction Interval will be marked as Retracted in Cloud Exchange.
To check the retracted IoCs in Cloud Exchange, go to
Threat IoCs
and search for
“sources.source Like “CTE CrowdStrike” && sources.retracted Is equal true”
.
This plugin also supports push retraction, which means IoCs pulled from 3rd-party platforms that were shared to CrowdStrike platforms, and were marked as retracted in Cloud Exchange, will also get deleted from the shared platform if that platform supports deletion of IoCs. You can verify the same through the Retraction result field.
Troubleshooting the CrowdStrike Plugin
Getting error while updating CrowdStrike from older version to v2.3.0
Due to change in the permissions for the new API endpoints, you will encounter an error while upgrading the plugin from the older version.
What to do:
Before upgrading the plugin in Cloud exchange, update the permissions for Client ID and Secret. It should have below mentioned permissions:
Scope
Read
Write
Detections
Yes
No
IOC Management
Yes
Yes
Hosts
Yes
Yes
IOCs (Indicators of Compromise)
Yes
No
Alerts
Yes
No
Once you upgrade your plugin then you can remove the permissions for ‘Detections’.
If you are receiving an error while updating the plugin using the plugin repository, follow the below steps:
Close the plugin repo page once you pull and download the plugin updates.
Go to the Threat Exchange > Plugins.
Edit the plugin, go to the Configuration parameter page > remove the selected value from the “Type of Threat Data to pull” field, and select the IOC type that you want to pull.
Select the source page from the “Indicator Source Page” dropdown.
Save the plugin.
Click on the enable plugin icon and enable the plugin. The plugin will be updated with the latest changes and start working as expected.
Receiving the same IoC from Crowdstrike Endpoint detection, that was shared to Crowdstrike’s Custom IoC Management page with action
Detect Only
(Loopback Issue)
If you are facing the loopback issue that is receiving the same IoC from Crowdstrike Endpoint detection, that was shared to Crowdstrike’s Custom IoC Management page with action
Detect Only
, follow the below steps
What to do:
Update the plugin to the latest version (2.3.0), as the issue is addressed in that.
The plugin keeps pulling IoCs in a loop
If your plugin keeps pulling same batch of IOCs in again and again then, follow the below steps
What to do:
Update the plugin to the latest version (2.3.0), as the issue is addressed in that. Thus, the plugin will not pull the same IOCs again and again.
Receiving an error while configuring the plugin
If you are facing an issue while configuring the CrowdStrike plugin, follow the below steps
What to do:
Make sure correct credentials are provided, and the generated credentials have the needed permissions.
Receiving 403 forbidden error while configuring the plugin
If you are receiving 403 error, verify the below scenarios:
Check if the provided Client ID and Client Secret values are correct.
The API client has proper permissions:
Check if you have proper
permissions
provided to the API Client.
If you are upgrading the plugin follow the steps mentioned in
Getting error while updating CrowdStrike from older version to v2.3.0
section.
You have IP groups added in the IP Allowlist Management page.
Follow the below steps to add your CE’s public IP to CrowdStrike’s IP allowlist:
On your CrowdStrike tenant, navigate to `Host setup and management > Falcon users > IP Allowlist Management` page and check if any IP groups are added. If added, it will be listed on the page. If not, your screen will look as below. Follow the below steps in case you have the IP groups added in the IP Allowlist Management page.
If you have some IP allowlist groups configured on your CrowdStrike tenant, make sure to add the `Public IP Address` of the virtual machine where cloud exchange is running into an existing group, or you can create a new IP allowlist Group. While adding that, make sure you have Access Type `API` selected as shown below.
Unable to pull data from the CrowdStrike Platform
If you are facing an issue while pulling the data from the CrowdStrike plugin, follow the below steps.
What to do:
Go to the Logging page, verify if any error has occurred and try to fix it.
Go to the CrowdStrike UI, and verify if Client ID/Secret are present, and not expired.
Note that some of the IoCs on CrowdStrike may not have the type or value field or those fields are empty. Such IoCs will not be pulled to Cloud Exchange.
Receiving a 500 Server error while updating/sharing the IoCs to CrowdStrike
If you are receiving the below error message in logs while sharing the IoCs to CrowdStrike, it might be because of the batch size provided in the plugin configuration for sharing being large.
What to do:
Change the batch size for the sharing from the plugin configuration:
Edit the CrowdStrike plugin in
Threat Exchange > Plugins
.
Reduce the
Indicator Batch Size
parameter and save the plugin.
Not able to share IoCs from Cloud Exchange to the CrowdStrike plugin
If you are not able to share IoCs from Netskope to CrowdStrike, that could be due to below-mentioned reason:
The IoCs present for Netskope plugin are of invalid type.
Proper Permissions are not set for the Client ID, Client Secret for CrowdStrike.
What to do:
Make sure that valid types of IoCs are present. CrowdStrike does not support URLs, if you are trying to share URL types of IoCs it will not be shared.
Make sure that all the needed permissions are set for Client ID, Client Secret for CrowdStrike.
Known Behaviors
Crowdstrike supports sharing of only 1M IoCs to the IoC Management Page so if the page already has exceeded the limit IoCs won’t be shared from Netskope Cloud Exchange and the user will first have to delete the existing IoCs.
We have observed that some of the IoCs on CrowdStrike may not have the type or value field or those fields are empty. Such IoCs will not be pulled to Netskope Cloud Exchange.
We have observed that the CrowdStrike platform does not support providing severity while performing some actions (‘Allow’, ‘Block, hide detection’), so while sharing IoCs from Netskope Cloud Exchange the severity will not be shared.
We have observed that the CrowdStrike APIs do not return data in sorted form sometimes, due to which the details pulled in Cloud Exchange might not be as per latest detection. So, it is possible that a particular IoCs might have multiple occurrences and the pull details of that IoC in Cloud Exchange might not be the latest one.
We have observed that CrowdStrike allows to store multiple IoCs in the value field for Endpoint Detection page where the type of that IoCs can be different to that of all the IoCs present in the value field. The plugin will store the IoC with respect to type field and the rest of the IoCs will be skipped and will not be stored. In the below example you can see that the type is
sha256
and the
ioc_value
field contains 2 values out of which one is of type
md5
. In this case,
sha256
will be stored in Cloud Exchange and other values will not be stored.
{ "agent_id": "7c566a5cc4ee4248a83d0405d7273a49", "aggregate_id": "aggind:7c566a5cc4ee4248a83d0405d7273a49:137439072286", "alleged_filetype": "exe", "associated_files": [], "child_process_ids": [ "pid:7c566a5cc4ee4248a83d0405d7273a49:297786408684" ], "cid": "c17f3a80ded0418eb107db3d26a27983", "cloud_indicator": "true", "cmdline": "\"C:
Program Files (x86)\\Microsoft\\EdgeUpdate\\Install\\\\
{856B848F-38B5-4946-921B-FB2F7713213E}
\\MicrosoftEdge_X64_137.0.3296.68.exe\" --msedge --verbose-logging --do-not-launch-msedge --system-level --channel=stable",
"composite_id": "c17f3a80ded0418eb107db3d26a27983:ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143",
"confidence": 100,
"context_timestamp": "2025-06-18T04:57:29Z",
"control_graph_id": "ctg:7c566a5cc4ee4248a83d0405d7273a49:137439072286",
"crawled_timestamp": "2025-06-18T05:57:51.199159695Z",
"created_timestamp": "2025-06-18T04:58:51.562849229Z",
"data_domains": [
"Endpoint"
],
"description": "A SHA256 hash matched a Custom Intelligence Indicator (Custom IOC) with low severity.",
"device": {
"agent_load_flags": "0",
"agent_local_time": "2025-06-17T22:47:44.249Z",
"agent_version": "7.24.19607.0",
"bios_manufacturer": "VMware, Inc.",
"bios_version": "VMW201.00V.24006586.B64.2406042154",
"cid": "c17f3a80ded0418eb107db3d26a27983",
"config_id_base": "65994767",
"config_id_build": "19607",
"config_id_platform": "3",
"device_id": "7c566a5cc4ee4248a83d0405d7273a49",
"external_ip": "61.219.78.165",
"first_seen": "2025-02-17T17:21:36Z",
"groups": [
"1012add21d3e4e08b146dbfdb37c5ca0"
],
"hostinfo":
{ "domain": "" }
,
"hostname": "DESKTOP-LQDIGUR",
"last_seen": "2025-06-18T05:48:27Z",
"local_ip": "10.66.2.89",
"mac_address": "00-0c-29-ee-47-37",
"machine_domain": "",
"major_version": "10",
"minor_version": "0",
"modified_timestamp": "2025-06-18T05:52:52Z",
"os_version": "Windows 10",
"ou": null,
"platform_id": "0",
"platform_name": "Windows",
"product_type": "1",
"product_type_desc": "Workstation",
"status": "contained",
"system_manufacturer": "VMware, Inc.",
"system_product_name": "VMware20,1"
},
"display_name": "CustomIOCHashLow",
"email_sent": true,
"external": true,
"falcon_host_link": "https://falcon.crowdstrike.com/activity-v2/detections/c17f3a80ded0418eb107db3d26a27983:ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143?_cid=g03000nb3ghi5x4fappp2bjsndr5ej4q",
"filename": "MicrosoftEdge_X64_137.0.3296.68.exe",
"filepath": "\\Device
HarddiskVolume3
Program Files (x86)\\Microsoft\\EdgeUpdate\\Install\\\\{856B848F-38B5-4946-921B-FB2F7713213E}
MicrosoftEdge_X64_137.0.3296.68.exe",
"files_written": [
{ "filename": "setup.exe", "filepath": "\\Device\\HarddiskVolume3
Program Files (x86)\\Microsoft\\EdgeUpdate\\Install\\\\
{856B848F-38B5-4946-921B-FB2F7713213E}
EDGEMITMP_60DE1.tmp",
"timestamp": "1749829318"
}
],
"global_prevalence": "common",
"grandparent_details":
{ "cmdline": "C:\\Windows\\system32\\services.exe", "filename": "services.exe", "filepath": "\\Device\\HarddiskVolume3\\Windows\\System32\\services.exe", "local_process_id": "904", "process_graph_id": "pid:7c566a5cc4ee4248a83d0405d7273a49:296364257770", "process_id": "296364257770", "sha256": "4a912dc98c977788131aad0ae468d86792211ed225f80b2c344a3690b4437428", "timestamp": "2025-06-13T04:55:18.990Z", "user_graph_id": "uid:7c566a5cc4ee4248a83d0405d7273a49:S-1-5-18", "user_id": "S-1-5-18", "user_name": "DESKTOP-LQDIGUR$" }
,
"id": "ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143",
"indicator_id": "ind:7c566a5cc4ee4248a83d0405d7273a49:297785683156-5311-1935186763644973143",
"ioc_context": [
{ "ioc_source": "primary_module", "ioc_type": "sha256", "ioc_value": "5219f66e6cab3aa843f6e89ee3d47d32,d757eb8b567d76eb19f7009adbb9d013c7cf1861f45b18a023d6866e8baa2a2d", "type": "ioc" }
],
"ioc_source": "primary_module",
"ioc_type": "sha256",
"ioc_value": "5219f66e6cab3aa843f6e89ee3d47d32,d757eb8b567d76eb19f7009adbb9d013c7cf1861f45b18a023d6866e8baa2a2d",
"local_prevalence": "unique",
"local_process_id": "1868",
"logon_domain": "WORKGROUP",
"md5": "5219f66e6cab3aa843f6e89ee3d47d32",
"name": "CloudDetect-CustomerIOC-SHA256-Low",
"objective": "Falcon Detection Method",
"parent_details":
{ "cmdline": "\"C:\\Program Files (x86)\\Microsoft\\EdgeUpdate\\MicrosoftEdgeUpdate.exe\" /svc", "filename": "MicrosoftEdgeUpdate.exe", "filepath": "\\Device\\HarddiskVolume3\\Program Files (x86)\\Microsoft\\EdgeUpdate\\MicrosoftEdgeUpdate.exe", "local_process_id": "4336", "md5": "c019e421d9f897108e51666cbae2c8b0", "process_graph_id": "pid:7c566a5cc4ee4248a83d0405d7273a49:297758877134", "process_id": "297758877134", "sha256": "3096d8e82917a9b73f322f4b1743e52e9b0c8b3c5933a957e73e29d6973cdd5b", "timestamp": "2025-06-16T10:26:29Z", "user_graph_id": "uid:7c566a5cc4ee4248a83d0405d7273a49:S-1-5-18", "user_id": "S-1-5-18", "user_name": "DESKTOP-LQDIGUR$" }
,
"parent_process_id": "297758877134",
"pattern_disposition": 0,
"pattern_disposition_description": "Detection, standard detection.",
"pattern_disposition_details":
{ "blocking_unsupported_or_disabled": false, "bootup_safeguard_enabled": false, "containment_file_system": false, "critical_process_disabled": false, "detect": false, "fs_operation_blocked": false, "handle_operation_downgraded": false, "inddet_mask": false, "indicator": false, "kill_action_failed": false, "kill_parent": false, "kill_process": false, "kill_subprocess": false, "mfa_required": false, "operation_blocked": false, "policy_disabled": false, "prevention_provisioning_enabled": false, "process_blocked": false, "quarantine_file": false, "quarantine_machine": false, "registry_operation_blocked": false, "response_action_already_applied": false, "response_action_failed": false, "response_action_triggered": false, "rooting": false, "sensor_only": false, "suspend_parent": false, "suspend_process": false }
,
"pattern_id": 5311,
"platform": "Windows",
"poly_id": "AADBfzqA3tBBjrEH2z0monmDgEHElB4TLZI4zzCC9NmU_gAATiEItOfbNan5F65GbEhxGr5sIpuo7GVQmBmbrXDpFsSf8Q==",
"priority_explanation": [
"[MOD] The parent process was identified as: MicrosoftEdgeUpdate.exe"
],
"priority_value": 87,
"process_id": "297785683156",
"process_start_time": "1749829315",
"product": "epp",
"scenario": "intel_detection",
"seconds_to_resolved": 0,
"seconds_to_triaged": 0,
"severity": 30,
"severity_name": "Low",
"sha1": "0000000000000000000000000000000000000000",
"sha256": "d757eb8b567d76eb19f7009adbb9d013c7cf1861f45b18a023d6866e8baa2a2d",
"show_in_ui": true,
"source_products": [
"Falcon Insight"
],
"source_vendors": [
"CrowdStrike"
],
"status": "new",
"tactic": "Custom Intelligence",
"tactic_id": "CSTA0005",
"technique": "Indicator of Compromise",
"technique_id": "CST0005",
"timestamp": "2025-06-18T04:57:29.681Z",
"tree_id": "137439072286",
"tree_root": "297785683156",
"triggering_process_graph_id": "pid:7c566a5cc4ee4248a83d0405d7273a49:297785683156",
"type": "ldt",
"updated_timestamp": "2025-06-18T05:57:51.199148989Z",
"user_id": "S-1-5-18",
"user_name": "DESKTOP-LQDIGUR$"
}
You might see logs like these in your Cloud Exchange:
CTE CrowdStrike [CTE CrowdStrike]: Successfully fetched 143 indicator(s) for 142 alert(s) from CrowdStrike Endpoint Detections.
Completed storing the batch of 142 indicator(s) for configuration 'CTE CrowdStrike'.
Here, the fetch count is greater than the store count because of the IoCs shown in the above example, which is having multiple values in the
ioc_value
field only the value which is a valid
sha265
will be stored in the Cloud Exchange
When sharing file hashes with CrowdStrike IoC Management, previously deleted file hashes may cause issues. If a user deletes file hashes for any reason and they are successfully removed from the UI and not returned via the
GET /iocs/combined/indicator/v1
endpoint, the plugin will treat them as new indicators. Consequently, it will attempt to share them using the
POST /iocs/entities/indicators/v1
endpoint. This results in a 409 Conflict error due to the hash pairs already existing in the system, as indicated by the following API response:
{
 "meta": {
  "query_time": 24.138019618,
  "powered_by": "ioc-manager",
  "trace_id": "bc6c0a83-b883-4289-8d1e-d9ad37aec273"
 },
 "errors": [
  {
   "code": 409,
   "message": "type sha256 and value 7440f5212e00eaa2b9425e0cb29f7e92c481e82a9cefc313177aa61fbb9e8a60 pair already exists."
  },
  {
   "code": 409,
   "message": "type md5 and value 328f95a67c92885fbaf9946c913149bd pair already exists."
  },
  {
   "code": 409,
   "message": "type sha256 and value e8ce6cee6554f2699605da7a59abe4ff81d96c5f2e4066e2314ddac92363fdd3 pair already exists."
  }
 ],
 "resources": []
}
In this Topic
CrowdStrike Plugin for Threat Exchange

---
## HarfangLab Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/harfanglab-plugin-for-threat-exchange/
**Last Modified:** 2026-07-18T00:49:34+00:00
**Scraped:** 2026-08-11T07:27:37.605333+00:00

HarfangLab Plugin for Threat Exchange - Netskope Technical Documentation
HarfangLab Plugin for Threat Exchange
Release Notes
2.0.0 (Required minimum CE version for this is 6.0.0)
Added
Added support to pull IoC(s).
Added support for pull and push retraction.
Added support to bifurcate the URL by types (Domain, FQDN, Hostname and URL) and hashes by types (SHA256, MD5).
Added handling of API rate limit.
Changed
Improved error handling.
Added resolution for error logs.
1.0.0
Added
Initial Release.
This document explains how to configure the HarfangLab v2.0.0 plugin in the Cloud Exchange platform. This plugin pulls IoCs of type Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5 from the
Threat intelligence > IoC Sources
page, and SHA256, MD5 from the
Threat intelligence > Driver Block List
page on the HarfangLab platform. This plugin also supports sharing IoCs of type Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5 back to the HarfangLab
Threat intelligence > IoC Sources
page. This plugin supports pull and push retraction of IoCs from the
Threat intelligence > IoC Sources
page from HarfangLab.
Prerequisites
To complete this configuration, you need:
Netskope Tenant (or multiple, for example, production and development/test instances)
A Netskope Cloud Exchange instance with the
Tenant plugin
and
Netskope Threat Exchange plugin
already configured and the Threat Exchange module enabled.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope tenant.
A
File Profile
on your Netskope tenant.
Connectivity to the following host: HarfangLab Partner login URL.
Example:
https://<id>.hurukai.io:8443/
HarfangLab Plugin Support
This plugin pulls IoCs of type Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5 from the
Threat intelligence > IoC Sources
page, and SHA256, MD5 from the
Threat intelligence > Driver Block List
page on the HarfangLab platform. This plugin also supports sharing IoCs of type Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5 back to the HarfangLab
Threat intelligence > IoC Sources
page. This plugin supports pull and push retraction of IoCs from the
Threat intelligence > IoC Sources
page from HarfangLab.
Fetched indicator types
Shared indicator types
Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5
Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5
Per HarfangLab’s IoC types, this plugin supports pulling of URL, Hash, Domain Name, Source IP, Destination IP and Dest. or Source IP. Also, this plugin supports sharing of URL, Domain Name, Hash and Dest. or Source IP.
IoC Retraction
For retraction to work, IoC(s) Retraction toggle must be enabled under
Settings > Threat Exchange
.
IoC Retraction (Pull)
: IoCs that are deleted on the HarfangLab, or that are not under the selected Source Type or Type of Threat data to pull, and not under the retraction interval (only for source type IoC sources) in the plugin configuration, will be marked as retracted in Cloud Exchange.
IoC Retraction (Push)
: IoCs that were already shared to HarfangLab, and are marked as retracted
Yes
in Cloud Exchange, will be deleted from HarfangLab platform.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes (IoC Sources, Driver block list)
IoC Retraction (Push)
Yes (IoC Sources)
Mapping
Since HarfangLab uses the URL IoC type to store all types of indicators, we are bifurcating them into IPv4, IPv6, FQDN, Domain, Hostname, and URL for accurate IoC type mapping.
Push Indicators Mappings
HarfangLab Field
Netskope Indicator Field
value
indicator.value
type
indicator.type → HarfangLab type
source_id
Resolved from action ioc_list_name
global_state
Action param Action (global_state)
hl_status
Action param Maturity (hl_status)
description
Force-stamped CE prefix (not a raw param)
comment
Action param comment
name
Action param name
references
Action param references
rule_level_override
Derived from indicator.severity (
not
a param)
rule_confidence_override
Action param Confidence Override (rule_confidence_override)
If Confidence Override is set to
No Override
, the HarfangLab platform sets the confidence level to
Moderate
.
Severity Mappings
Netskope Severity
HarfangLab Severity
unknown
informational
low
low
medium
medium
high
high
critical
critical
Push Reputation Mappings
CE Reputation
HarfangLab Confidence
1-3
weak
4-7
moderate
8-10
strong
Push IoC Types Mappings
Netskope CE Type
HarfangLab Type
Example Value
SHA256
Hash
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
MD5
Hash
d41d8cd98f00b204e9800998ecf8427e
URL
URL
https://malware.com/payload.exe
Hostname
URL
localhost, WIN-SERVER01
Domain
Domain Name
example.com
FQDN
Domain name
sub.example.com
IPv4
Dest. or Source IP
8.8.8.8
IPv6
Dest. or Source IP
2001:db8::1
IPv4 + tag Harfanglab-Type:Source IP
Source IP
8.8.8.8
IPv4 + tag Harfanglab-Type:Destination IP
Destination IP
8.8.8.8
IPv6 + tag Harfanglab-Type:Source IP
Source IP
2001:db8::1
IPv6 + tag Harfanglab-Type:Destination IP
Destination IP
2001:db8::1
Permissions
Here are the two permissions needed for the plugin to pull and share IoCs on the HarfangLab platform.
View & edit Yara,Sigma, IOC & Driver block list engines
View & manage rules at ‘Testing’ and ‘Experimental’ maturity level
API Details
List of APIs used
API Detail
Method
API Endpoint
Create IOC List
POST
/api/data/threat_intelligence/IOCSource/
Fetch Existing IOC List
GET
/api/data/threat_intelligence/IOCSource/?limit=500&offset=0
Fetch IOC Rules (Pull Indicators)
GET
/api/data/threat_intelligence/IOCRule/
Push Indicators
POST
/api/data/threat_intelligence/IOCRule/
Delete IOC Rule (Push Retraction)
DELETE
/api/data/threat_intelligence/IOCRule/{id}/
Fetch Driver Block List
GET
/api/data/threat_intelligence/DriverBlocklist/?limit=500&offset=0
Create IOC List
Parameters:
None
API Request with Curl
curl --location 'https://b517af1bf2225fc3.hurukai.io:8443/api/data/threat_intelligence/IOCSource/' \ --header 'Authorization: Token 66752e19a9872d67e348e0e192a9bexxxxxxxxxx' \ --header 'Content-Type: application/json' \ --data '{ "name": "Test IOC List", "description": "IOC List created from Netskope CE" }'
Sample API Response
{
  "id": "7f3ceca9-33d4-4db7-bdd6-3e1dc63a7aa0",
  "ioc_count": 0,
  "ioc_testing_in_progress_count": 0,
  "ioc_testing_count": 0,
  "ioc_experimental_count": 0,
  "last_update": "2023-10-03T12:59:16.381480Z",
  "creation_date": "2023-10-03T12:59:16.381564Z",
  "name": "Test IOC List",
  "description": "IOC List created from Netskope CE",
  "enabled": true,
  "block_on_agent": true,
  "endpoint_detection": true,
  "last_modifier": null
}
Fetch Existing IOC List
Parameters
Parameter
Value
Comments
limit
500
Limit for 1 page
offset
0, 500, 1000…
Incremented by limit for each page until next is null
API Request with Curl
curl --location 'https://b517af1bf2225fc3.hurukai.io:8443/api/data/threat_intelligence/IOCSource/?limit=500&offset=0' \
 --header 'Authorization: Token 66752e19a9872d67e348e0e192a9bexxxxxxxxxx'
Sample API Response
{
  "count": 8,
  "next": null,
  "previous": "/api/data/threat_intelligence/IOCSource/?limit=500",
  "results": [
    {
      "id": "f72c82c9-e136-43a5-8a37-4bd121af5464",
      "ioc_count": 370,
      "ioc_testing_in_progress_count": 0,
      "ioc_testing_count": 0,
      "ioc_experimental_count": 0,
      "last_update": "2023-09-29T06:02:41.011727Z",
      "creation_date": "2023-09-29T06:02:41.011770Z",
      "name": "test",
      "description": "IOC List created from Netskope CE",
      "enabled": false,
      "block_on_agent": false,
      "endpoint_detection": false,
      "last_modifier": null
    }
  ]
}
Push Indicators
Parameters:
None
API Request with Curl
curl --location 'https://b517af1bf2225fc3.hurukai.io:8443/api/data/threat_intelligence/IOCRule/' \
--header 'Authorization: Token 66752e19a9872d67e348e0e192a9bexxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
    "value": "61.134.36.102",
    "source_id": "6345304d-2592-4286-9682-06a900d6ca96",
    "type": "url",
    "global_state": "alert",
    "hl_status": "stable",
    "description": "Netskope CE | <plugin_name>",
    "rule_level_override": "high",
    "rule_confidence_override": null
}'
Sample API Response
{
  "id": "19a89c4e-b58a-446a-b27a-6b55d4fb891e",
  "source_id": "6345304d-2592-4286-9682-06a900d6ca96",
  "last_modifier": {
    "id": 7,
    "username": "NetskopeCE"
  },
  "last_update": "2023-10-03T12:54:24.608988Z",
  "creation_date": "2023-10-03T12:54:24.609060Z",
  "hl_status": "stable",
  "hl_local_testing_status": null,
  "enabled": true,
  "type": "url",
  "value": "61.134.36.102",
  "comment": null,
  "info": null,
  "category": null,
  "description": "Netskope CE | <plugin_name>",
  "references": [
  ],
  "source": "6345304d-2592-4286-9682-06a900d6ca96"
}
Fetch IoC Rules(Pull Indicators)
Parameters
Parameter
Value
Comments
source_id
Eg., 6345304d-2592-4286-9682-06a900d6ca96
IOC Source list ID to pull from
last_update__gte
2024-01-01 00:00:00
Window start — space-separated datetime (no T/Z)
last_update__lte
2024-01-02 00:00:00
Window end (now)
limit
500
Limit for 1 page
offset
0, 500, 1000…
Incremented by limit for each page until next is null
API Request with Curl
curl --location 'https://b517af1bf2225fc3.hurukai.io:8443/api/data/threat_intelligence/IOCRule/?source_id=6345304d-2592-4286-9682-06a900d6ca96&last_update__gte=2024-01-01%2000:00:00&last_update__lte=2024-01-02%2000:00:00&limit=500&offset=0' \
--header 'Authorization: Token 66752e19a9872d67e348e0e192a9bexxxxxxxxxx'
Sample API Response
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "19a89c4e-b58a-446a-b27a-6b55d4fb891e",
      "source_id": "6345304d-2592-4286-9682-06a900d6ca96",
      "last_modifier": {
        "id": 7,
        "username": "NetskopeCE"
      },
      "last_update": "2023-10-03T12:54:24.608988Z",
      "creation_date": "2023-10-03T12:54:24.609060Z",
      "hl_status": "stable",
      "hl_local_testing_status": null,
      "enabled": true,
      "type": "url",
      "value": "61.134.36.102",
      "comment": null,
      "info": null,
      "category": null,
      "description": null,
      "references": [
      ],
      "source": "6345304d-2592-4286-9682-06a900d6ca96"
    }
  ]
}
Fetch Driver Block List
Parameters
Parameter
Value
Comments
limit
500
Limit for 1 page
offset
0, 500, 1000…
Incremented by limit for each page until next is null
API Request with Curl
curl --location 'https://b517af1bf2225fc3.hurukai.io:8443/api/data/threat_intelligence/DriverBlocklist/?limit=500&offset=0' \--header 'Authorization: Token 66752e19a9872d67e348e0e192a9bexxxxxxxxxx'
Sample API Response
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "b2d4f8a1-1c3e-4f5a-9b7d-8e2c1a6f0d3b",
      "last_update": "2023-10-03T12:54:24.608988Z",
      "creation_date": "2023-10-03T12:54:24.609060Z",
      "enabled": true,
      "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "comment": null,
      "description": null
    }
  ]
}
Delete IOC Rule for Push
API Request with Curl
curl --location --request DELETE 'https://b517af1bf2225fc3.hurukai.io:8443/api/data/threat_intelligence/IOCRule/19a89c4e-b58a-446a-b27a-6b55d4fb891e/' \--header 'Authorization: Token 66752e19a9872d67e348e0e192a9bexxxxxxxxxx'
Sample API Response
HTTP/1.1 204 No Content
Performance Matrix
Here is the performance reading conducted after pulling 100K IoCs and sharing 1K IoCs on a Large CE instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators pulled from HarfangLab
~ 10K IoCs per minute
Indicators shared with HarfangLab
~ 45 IoCs per minute
User Agent
netskope-ce-6.1.0-cte-harfanglab-v2.0.0
Workflow
Get your HarfangLab API token.
Configure the HarfangLab plugin.
Configure business rules for the HarfangLab plugin.
Configure sharing for Netskope and HarfangLab.
Validate the HarfangLab plugin.
Watch a Video
Click play to watch a video.
Get your HarfangLab API Token
Create a Role on Harfanglab
Log in to your HarfangLab instance and go to
Administration > Roles
.
Click
Roles
and then click
Create role
.
Enter a name and description for the new role, and then click
Create
.
Click the
i
icon for that specific role name to edit it.
Only give permissions for
YARA, Sigma, IOC & Driver block list engines
to view and edit on the
Threat Intelligence
permission, and click the checkbox
View & manage rules at ‘Testing’ and ‘Experimental’ maturity level
.
Click
Save
.
Attach this role to a specific user.
Assign a Role to the User
In the left panel, go to
Administration > Users
.
Select the user and click on
i
icon to edit its role. If you want to create a new user, then click
Create new user
.
Update the role with the role that you created in the
Create role
section.
Get the API Token
On the left panel, go to
Administration > Users
.
Click on your username and scroll down to API Token. Click
Generate Token
if the token hasn’t already been generated, and copy the API Token to use it when configuring in the plugin.
Configure the HarfangLab Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
HarfangLab v2.0.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources.
Indicator Aging Criteria:
Define Expiry Time (In Days) for Threat Intel/Indicators. (Default: 90)
Override Reputation
: Set value to override the reputation of indicators received from this configuration. Use 0 to retain the default value, which will not override the indicator’s reputation.
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Click
Next
and enter the Configuration Parameters:
Tenant URL
: Base URL of HarfangLab instance. For example:
https://<instance_id>.hurukai.io:<port>
.
API Token
: API Token for authenticating to HarfangLab.
Source Type:
Select the source(s) to pull Threat IoCs from HarfangLab. At least one source must be selected.
Type of Threat data to pull:
Type of Threat IoCs to pull from HarfangLab. Allowed values are SHA256, MD5, Domain, FQDN, Hostname, IPv4, IPv6, URL. Driver Block List only supports SHA256 and MD5. Leave empty to pull all supported types.
IOC Sources Name:
Comma-separated names of IoC Sources to pull from HarfangLab. Leave this empty to pull from all available IoC Sources. Applicable only when
IoC Sources
is selected as the Source Type.
Initial Range (in days):
Number of days Threat IoCs to pull from IoC Sources in the initial run. Valid values are in range from 0 to 100000 days. Applicable only when
IoC Sources
is selected as the Source Type.
Enable Retraction:
Enable retraction for pulled indicators. When
Yes
, indicators no longer present on HarfangLab will be retracted in Cloud Exchange. For IoC Sources, a Retraction Interval must also be configured. This parameter is only considered if
IoC(s) Retraction
is enabled in the Threat Exchange settings.
Retraction Interval (in days):
Number of days to use as the retraction interval for IoC Sources retraction. Valid values are in the range from 1 to 100000 days. Required when Enable Retraction is
Yes
and
IoC Sources
is selected as the Source Type. This parameter will only be considered if
IoC(s) Retraction
is enabled in the Threat Exchange settings.
Enable Tagging:
Enable/Disable tagging of pulled indicators. When enabled, indicators pulled from IoC Sources are tagged with the IoC Source name, and indicators pulled from Driver Block List are tagged with
HarfangLab-Driver-Block-List
.
Enable Polling:
Enable/Disable polling Threat IoCs from HarfangLab. Disable if you only need to push Threat IoCs to HarfangLab.
Click
Save
.
Configure a Threat Exchange Business Rule for the HarfangLab Plugin
To share indicators from Netskope Cloud Exchange to HarfangLab, you need to have a business rule that will filter out the indicators that you want to share.
Go to
Threat Exchange > Business Rules
and click
Create New Rule
.
Enter a rule name and add a filter as per your requirement for the IoCs you want to share, and then click
Save
.
Configure Sharing for the HarfangLab Plugin
The HarfangLab plugin supports the sharing of URLs, MD5, and SHA256 types of IoCs.
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Netskope Threat Exchange), Business Rule, and Destination Configuration (CTE HarfangLab), and Target, and then select the following parameters:
IOC Source Name:
Select an existing IoC Source list dropdown or select
Create New IOC List
.
New IOC Sources Name:
Name of the new IoC Sources to create on HarfangLab. Required when
Create New IOC List
is selected.
Name:
Optional display name for the IoC.
Description:
Optional description for the IoC.
Comment:
Optional comment for the IoC.
References:
Optional comma-separated list of reference URLs or identifiers. Each entry will be sent as a separate item.
Confidence Override:
Override the confidence for all pushed IoC(s). Select
IoC Reputation
to derive confidence from the indicator’s reputation score (1-3: weak, 4-7: moderate, 8-10: strong). For No override, it’s been observed that even if you create an IoC with Confidence as
No override
, the HarfangLab UI will show it as
moderate
.
Action:
Select the action for all pushed IoC(s). The default value is
Alert
.
Maturity:
Select the maturity status for all pushed IoC(s). The default value is
Stable
.
Click
Save
.
Note
Refer to the
Netskope Threat Exchange plugin
guide for more information related to sharing on the Netskope Tenant. As the HarfangLab plugin supports pulling URL, IPv4, IPv6,Hostname, Domain, FQDN, SHA256, and MD5, you can perform these actions on Netskope using these indicators:
Add to a URL List
Add a File Profile
Add to Private App
Add to Destination Profile
Add to DNS Profile
Validate the HarfangLab Plugin
Validate the Pull
This plugin supports pulling IoCs of type Domain, FQDN, Hostname, IPv4, IPv6, URL, SHA256 and MD5 from the
IoC Sources
page, and SHA256, MD5 from the
Driver Block List
page.
To verify the available IoCs on HarfangLab, go to the
Threat Intelligence > IoC
page.
Go to the
Driver Block List
tab to see Hashes (SHA256 and MD5).
Go to the
IoC Sources
tab to see all the IoC sources.
Click on any of the source names to check the IoCs present under that IoC source.
To verify the pulling of IoCs on Cloud Exchange, go to
Settings > Logging
and apply the filter with the plugin configuration name. Example:
message Like “CTE HarfangLab”
.
Pulled IoCs will be visible on the Threat IoCs page in Cloud Exchange.
Validate the Push
To verify pushed IoCs on HarfangLab, go to
Threat Intelligence > IoC Sources
.
Click on the IoC List name that you used while configuring the plugin, and check the IoCs available in the list.
Click on the IoC to view its details. Note that IoCs having description like ‘
Netskope CE | <plugin name>’
will not be pulled again back to Cloud Exchange.
To validate the pushed indicator in Cloud Exchange, go to
Threat IoCs
and search for IoCs that are shared with HarfangLab.
You can also verify the pushed IoCs from
Logging
in Cloud Exchange. Filter the logs available from the Harfanglab platform.
Validate the Retraction
For Pull Retraction
To verify the retracted IoCs, go to
Threat IoCs
and apply the filter shown here.
To verify the logs related to retraction, you can apply the filter shown here.
This is the Destination profile where the IoCs pulled from Harfanglab were shared.
As the IoCs pulled from HarfangLab was marked as Retracted
yes
, and it was already shared to the destination profile on the Netskope tenant, it will get deleted from that destination profile, and the status for it can be verified from retraction result. In this case the retraction result is
CTE Netskope Threat Exchange: retracted
, which means it was deleted from the destination profile.
Here you can see the retracted IoCs were deleted from this destination profile.
For Push Retraction
As the HarfangLab plugin supports push retraction, so the IoCs that were shared to HarfangLab platform and are marked as Retracted
yes
, it will be deleted from the HarfangLab platform at the next sync interval, and its result can be verified from retraction result field. Here the retraction result is
CTE HarfangLab: retracted
, which means this IoC is deleted from the IoC Sources on HarfangLab that was used in the sharing configuration.
To verify the logs related to retraction, you can apply the filter as shown here.
Here you can see the same IoC is deleted on HarfangLab.
Troubleshooting the HarfangLab Plugin
Unable to use the plugin after upgrading from older plugin version
It may be due to a change in format for API token. You may encounter this error.
What to do:
Use the Skip button while upgrading the plugin, and then go to the plugins page and edit the HarfangLab plugin configuration. Update the API token with the format shown below, save the plugin, and then enable it.
Old API Token format: “Token 66752e19a9872d67e348e0e192a9besxxxxxxxxx”
New API Token format for HarfangLab v2.0.0: “66752e19a9872d67e348e0e192a9besxxxxxxxxx”
Unable to pull IoCs from HarfangLab
If you are not able to pull IoCs from HarfangLab, then this may be due to incorrect Source Name, or no IoCs present on the IoC Sources page or the Drivier block list page.
What to do:
Make sure the IoCs are present on the Harfang Lab platform, and the Source Name in the plugin configuration is correct. Refer to the
Validate the Pull
section.
Receiving an invalid URL or invalid Token error while creating the plugin configuration.
This error might occur if the provided URL in the plugin configuration is invalid.
What to do:
Make sure to give the correct URL that you use to access your HarfangLab platform. Make sure to only add the Tenant URL along with the port. Refer to the
Configuration on HarfangLab
section.
Receiving error for exit code 401, Unauthorization
If you are receiving the 401 error, it may be due to an incorrect API token.
What to do:
Make sure that the Token provided exists on the HarfangLab platform. Or generate a new API Token. Refer to the
Configuration on HarfangLab
section.
Receiving error for exit code 403, Forbidden error
If you are receiving the 403 error, it may be due to the token with insufficient permissions.
What to do:
If this error is received while configuring the plugin, or any time in the plugin lifecycle, check the API Tokens permission. Refer to the
Configuration on HarfangLab
section.
Known Behaviors
It has been observed that even if you create an IoC with confidence as
No override
, the HarfangLab UI will show it as
moderate
.
HarfangLab APIs do not support updating the IoCs, which means if you want to update any of the existing IoCs, then you need to either share that IoC to a New IoC Source, or delete that IoC from the current IoC Sources, and share it again.
In this Topic
HarfangLab Plugin for Threat Exchange

---
## ExtraHop Reveal(x) 360 Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/extrahop-revealx-360-plugin-for-threat-exchange/
**Last Modified:** 2026-01-30T01:06:15+00:00
**Scraped:** 2026-08-11T07:28:04.403441+00:00

ExtraHop Reveal(x) 360 Plugin for Threat Exchange - Netskope Technical Documentation
ExtraHop Reveal(x) 360 Plugin for Threat Exchange
This document explains how to configure the ExtraHop
Reveal(x) 360 v1.1.1
plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin
fetches offender’s IP Address (ipv4) and Hostname from the
Detections
page of the ExtraHop platform. The Plugin does not support sharing indicators to ExtraHop Reveal(x) 360 platform
.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances.
A
URL List
configured on the Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
ExtraHop Reveal(x) 360 account with API Access enabled.
Connectivity to the following host: ExtraHop Reveal(x) 360 login URL. Example:
https://extrahop-bd.cloud.extrahop.com/
.
ExtraHop Reveal(x) 360 Plugin Support
This plugin fetches offender’s IP Address (ipv4) and Hostname from the
Detections
page of the ExtraHop platform. The Plugin does not support sharing indicators to ExtraHop Reveal(x) 360 platform.
Fetched Indicator Types
Shared Indicator Types
IPv4, Hostname
Not supported
Mappings
Pull Mappings
Cloud Exchange Fields
ExtraHop Fields
Value
object_value, hostname
Type
IPv4, hostname
Severity
risk_score
Comments
Id: “id”,
Risk Score: “risk_score”,
Type: “type”,
Mattire Information: “mitre_tactics”,
Description: “description”
Firstseen
mod_time
Lastseen
mod_time
Severity Mapping
Cloud Exchange Severity
ExtraHop Severity
LOW
1 to 30
MEDIUM
31 to 79
HIGH
80 to 99
UNKNOWN
other
Permissions
The REST API Access and generate credentials access should be enabled for the system, For more details, refer to the ExtraHop Reveal(x) 360 documentation
here
.
API Access.
Functionality
Permissions
Pull Indicators
System Access > Full read-only.
NDR Module Access > Full access.
API Details
The ExtraHop Reveal(x) 360 REST APIs were used for authenticating the credentials and pulling the data from ExtraHop Reveal(x) 360.
List of APIs Used
API Detail
Method
API Endpoint
Generate Token
POST
/oauth2/token
Pull Indicators
POST
/api/v1/detections/search
Generate Token
API Endpoint:
https://extrahop-bd.api.cloud.extrahop.com/oauth2/token?grant_type=client_credentials
Method:
POST
Parameters:
grant_type: client_credentials
Headers:
Content-Type: application/x-www-form-urlencoded
Authorization
:
Basis
<base64 encoded client id and client secret separated by colon>
Sample API Response:
{
"access_token": "eyJraWQiOiJkbndoem42RUNpaW9mSDRSTWdVV0FlZ1lhRHMrVlRDeDhXN1dJZnpVYjZjPSIsImFsZyI6********mZGhkcXR0dWM5aXFwc2pndWxzaXEifQ.pw-cbQTSVC1HlRdl_v63si5Jvz6fILbT-wFWua-AEBvk-GXGMXBUKCYs4g-ZvnWnSpcfsMAJZTTOO-05qpbnYE-K3N7qOQ",
"expires_in": 600,
"token_type": "Bearer"
}
Pull Data
API Endpoint:
https://extrahop-bd.api.cloud.extrahop.com/api/v1/detections/search
Method:
POST
Parameters:
None
Body:
{
"offset": 0,
"limit": 1,
"mod_time": 1696524883357,
"filter": {
"risk_score_min": 0
},
"sort": [
{
"direction": "asc",
"field": "mod_time"
}
]
}
Sample API Response
[
{
“id”: 21474836485,
“start_time”: 1696521252445,
“update_time”: 1696521252445,
“end_time”: 1696521252445,
“mod_time”: 1696524883357,
“title”: “ET POLICY Ipconfig Command in SMB Traffic – Possible Lateral Movement”,
“description”: “The ExtraHop system observed activity that matched rule values in signature ID\n(SID) 2027185:\n\n * Flow: [tcp] any → internal 445\n * Payload: `/SMB.*(?i)ipconfig(?-i)/s`\n\n\nRule Created: 2019-04-11 \n\n\n”,
“risk_score”: 45,
“type”: “ids_bad_unknown”,
“recommended_factors”: [],
“recommended”: false,
“categories”: [
“sec”,
“sec.ids”
],
“properties”: {
“sid”: “2027185”
},
“participants”: [
{
“role”: “offender”,
“object_id”: 12884901896,
“object_type”: “device”,
“object_value”: “10.1.0.86”,
“hostname”: “pc2.i.rx.tours”,
“id”: 2171,
“external”: false,
“scanner_service”: null
},
{
“role”: “victim”,
“object_id”: 12884901899,
“object_type”: “device”,
“object_value”: “10.1.0.238”,
“hostname”: “pc3.i.rx.tours”,
“id”: 2174,
“external”: false,
“scanner_service”: null
}
],
“ticket_id”: null,
“assignee”: null,
“status”: null,
“resolution”: null,
“mitre_tactics”: [],
“mitre_techniques”: [],
“appliance_id”: 5,
“is_user_created”: false
}
]
Performance Matrix
Here is the performance reading conducted after pulling 100K IoCs on a Large CE instance with the below specifications.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators pulled from ExtraHop Reveal(x) 360
~14K per minute
User Agent
netskope-ce-6.0.0-cte-extrahop-reveal(x)-360-v1.1.1
Workflow
Get your ExtraHop Reveal(x) 360 Base URL, Client ID, and Client Secret.
Configure the ExtraHop Reveal(x) 360 plugin.
Configure a Business Rule for ExtraHop Reveal(x) 360.
Configure sharing between ExtraHop Reveal(x) 360 and Threat Exchange.
Validate the ExtraHop Reveal(x) 360 plugin.
Watch a Video
Click play to watch a video.
Get your ExtraHop Reveal(x) 360 Base URL, Client ID, and Client Secret
In ExtraHop Reveal(x) 360, go to
Settings > API Access
.
Scroll down and click
Create Credentials
.
Enter a name for your Rest API Credentials and provide this access.
System Access > Full read-only.
NDR Module Access > Full access.
Click
Save
.
Copy the API Endpoint and remove the oath2/token from it. This will be the Base URL for the plugin.
Copy the ID and Secret. This secret will not be visible later so make sure to make a note of it.
Configure the ExtraHop Reveal(x) 360 Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
CTE ExtraHop Reveal(x) 360 v1.1.1 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration
Sync Interval
: Leave the default.
Aging Criteria:
Expiry time of the plugin in days. (Default: 90)
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Click
Next
and enter the Configuration Parameters:
Base URL
: ExtraHop Reveal(x) 360 API Base URL. This Base URL is displayed in the Reveal(x) 360 API Access page under API Endpoint. The Base URL should not include /oauth/token.
Client ID
: ExtraHop Reveal(x) 360 API ID.
Client Secret
: ExtraHop Reveal(x) 360 API Secret.
Minimum Risk Score
: Only the indicators with severity greater than or equal to specified value will be fetched. Select a value between 0-99. If no value is provided all the indicators will be fetched.
Retraction Interval:
Retraction Interval days to run IoC(s) retraction for ExtraHop indicators. Note: This parameter will only be considered if
IoC(s) Retraction
is enabled in Threat Exchange Settings.
Initial Range
: Number of days to pull the data for the initial run.
Click
Save
.
Configure a Threat Exchange Business Rule for ExtraHop Reveal(x) 360
To share indicators fetched from the ExtraHop Reveal(x) 360 to Cloud Exchange, you need to have a business rule that will filter out the indicators that you want to share.
In Threat Exchange, go to
Business Rules
and
Create New Rule
.
Add the filter based on your requirements and click
Save
.
Configure Sharing for the ExtraHop Reveal(x) 360 Plugin
To share IoCs from the ExtraHop Reveal(x) 360 plugin to Netskope:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (ExtraHop Reveal(x) 360), a Business Rule, the Destination Configuration (Netskope), and Target. Select the existing IoC List Name, or create a new IoC list.
Click
Save
.
Validate the ExtraHop Reveal(x) 360 Plugin
Validate the Pull
You can verify the pulling of IoCs from the plugin by going to
Logging
and checking the pulled logs from the ExtraHop Reveal(x) 360 plugin.
You can check the pulled data stored in Cloud Exchange at
Threat Exchange > Threat IoCs
. Search the IoCs pulled from the plugin.
You can also filter the IoCs based on the tags.
To verify the pull from the ExtraHop Reveal(x) 360 platform, log in to the ExtraHop Reveal(x) 360 platform and go to the
Detections
tab. You will see the detections. The plugins pulls the offender’s hostname and IP address of the detections.
To check the retracted IoCs in Cloud Exchange, go to
Threat IoCs
and search for IoCs whose retraction value is
Yes: sources.retracted Is equal true
.
You can also verify IoC retraction via the Cloud Exchange Logs. Go to
Logging
and search for: message
Like “extrahop” && message Like “Rectracted”
.
Validate the Push
The ExtraHop Reveal(x) 360 plugin does not support the pushing of IoCs.
You can push the IoCs pulled from the ExtraHop Reveal(x) 360 to Netskope or any 3rd-party plugin supported in Threat Exchange. Refer to
IoC Retraction
.
Here are the IoCs shared to Netskope before they were retracted in Cloud Exchange.
IoCs marked as retracted in Cloud Exchange will be retracted from Netskope tenants as well if shared.
Troubleshooting the  ExtraHop Reveal(x) 360 Plugin
Unable to pull IoCs from the plugin
If you are not able to pull any IoCs from the plugin it might be due to one of the following reasons:
IoCs are not available at all for pulling.
The Detections present on ExtraHop Reveal(x) 360 does not contain the Offender’s information i.e., Object Value or Hostname.
There are no detections on ExtraHop Reveal(x) 360 matching the severity selected on the configuration page.
What to do:
In order to resolve this issue, follow these steps respectively:
IoCs are not available at all for pulling. Log in to the ExtraHop Reveal(x) 360 platform and go to the
Detection
tab. You will see the detections and under the offender section the hostname and IP address of the detections.
The Detections present on ExtraHop Reveal(x) 360 does not contain the Offender’s information like Object Value or Hostname. Check under
Detections
if the detections present on the platform have Offender information (Hostname or IP address). The detections will only be fetched if it has at least any one of these details.
There are no detections on ExtraHop Reveal(x) 360 matching the severity selected on the configuration page.
In this Topic
ExtraHop Reveal(x) 360 Plugin for Threat Exchange

---
## Commvault Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/commvault-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:39:58+00:00
**Scraped:** 2026-08-11T07:28:29.057091+00:00

Commvault Plugin for Threat Exchange - Netskope Technical Documentation
Commvault Plugin for Threat Exchange
This document explains how to configure the Commvault v1.0.0 integration with the Cloud Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches URL and pushes the same to the Commvault platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
URL list
on your Netskope Tenant.
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Commvault Instance.
The hostname used while sharing (reach out to Commvault for assistance, if needed).
Connectivity to the following host: Commvault platform URL.
Plugin Scope
The Commvault plugin fetches IoCs of the type of URL from the Commvault platform. This plugin shares the URL to Commvault. You need the Command Center API URL, Commvault Access Token to access the plugin. IoCs are pulled from
CommandCenter > Unusual File Activities
. The IoCs are pushed to the same page in the hostname under Threat Scan External Software detected tab.
Commvault Plugin Support
Fetched indicator types
URL
Shared indicator types
URL
Mappings
Severity
Commvault Severity
CE Severity
-1
Unknown
0-3
Low
4-7
High
8-10
Critical
Mappings for Pull (Netskope field – Commvault fields)
Netskope CE Fields
Commvault Field
value
client_hostname
severity
Refer to Severity Mapping
type
URL
firstSeen
timeSource
lastSeen
timeSource
Mappings for Push
Netskope CE Fields
Commvault Field
value
client.hostname
lastSeen
anomalyDetectedBy.anomalyDetails.anomalyEvents.detectionTime
lastSeen
anomalyDetectedBy.anomalyDetails.detectionTime
Comment
anomalyDetectedBy.anomalyDetails.anomalyReason
anomalyDetectedBy.vendorName (netskope-ce it will be an constant value)
anomalyDetectedBy.anomalyDetails.anomalyEvents.eventId(Random UUID eg:456fdd12trhth43)
extendedInformation
anomalyDetectedBy.anomalyDetails.anomalyEvents.eventUrl
anomalyDetectedBy.anomalyDetails.timesSeen(1 Always Constant)
anomalyDetectedBy.anomalyDetails.eventType (URL)
Permissions
Assign the following permissions to the user. For more information, refer to the
Commvault documentation
.
View permission on the CommCell.
Agent Management on All Servers.
View permission on All Servers.
API Details
Validate
API Endpoint:
<Command Center API URL>
/commandcenter/api/Events
Method:
GET
Headers:
Key
Value
Accept
application/json
authToken
<Commvault Access Token>
Sample API Response:
{
  "commservEvents": [
    {
      "severity": 9,
      "eventCode": "117440845",
      "acknowledge": 0,
      "eventCodeString": "7:333",
      "subsystem": "cvd",
"description": “
<event_description>
",
      "id": 115920200,
      "timeSource": 1702291179,
      "type": 0,
      "clientEntity": {
         "clientId": 57238,
         "clientName": "
<client_name>
",
         "displayName": "
<display_name>
"
      }
    }
  ]
}
Fetch Events
API Endpoint:
<Command Center API URL>
/commandcenter/api/Events
Method:
GET
Headers:
Key
Value
Accept
application/json
authToken
<Commvault Access Token>
paginginfo
0
Parameters:
Key
Value
level
10
showAnomalous
True
fromTime
Epoch timestamp
Sample API Response:
{
  "commservEvents": [
    {
      "severity": 9,
      "eventCode": "117440845",
      "acknowledge": 0,
      "eventCodeString": "7:333",
      "subsystem": "cvd",
"description": “
<event_description>
",
      "id": 115920200,
      "timeSource": 1702291179,
      "type": 0,
      "clientEntity": {
         "clientId": 57238,
         "clientName": "
<client_name>
",
         "displayName": "
<display_name>
"
      }
    }
  ]
}
Get Client Details
API Endpoint:
<Base URL>
/commandcenter/api/Client/
<Client ID>
Method:
GET
Headers:
Key
Value
Accept
application/json
authToken
<Commvault Access Token>
Sample API Response:
"clientProperties":{
            "client":{
                      "clientEntity": {
                                "hostName": "
<host_name>
"
                        }
            }
}
Push
API Endpoint:
<Command Center API URL>
/commandcenter/api/Client/Action/Report/Bulk/Anomaly
Method:
PUT
Headers:
Key
Value
Accept
application/json
authToken
<Commvault Access Token>
Body:
{
"anomalyDetections": [
  {
    "client": {
    "hostName": "<Host Name>"
    },
    "anomalyDetectedBy": {
      "vendorName": "NetSkope CTE",
      "anomalyDetails": [
        {
          "anomalyEvents": [
           {
             "detectionTime": 1698837719,
             "eventId": "456fdd12trhth43",
             "eventUrl": "url target"
           }
         ],
         "anomalyReason": "Testing",
         "detectionTime": 1699422560,
         "eventId": "12fdg-232333333",
         "timesSeen": 1,
         "eventType": "URL"
       }
      ]
     }
    }
   ]
 }
Sample API Response
:
"anomalyDetections": [
   {
     "client": {
        "clientName": "dm2perf8_2"
     },
      "errorResponse": {}
   }
 ]
}
Performance Matrix
Below is the performance reading conducted for fetching and pushing 100K IOCs in each plugin lifecycle on a Large CE instance with the below specifications.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Commvault
~ 10K per minute
Indicators shared to Commvault
~ 200 per minute
Note
The above performance for pull has been conducted using mock data since the Commvault platform does not have sufficient data to test the performance for pulling of IoCs. This might be the reason for the performance difference in the pull and push. Also it has been observed that the hits on the Commvault platform for shared IoCs is resetted to 0 after the hits surpasses to 5000.
User Agent
netskope-ce-5.0.0-cte-Commvault-v1.0.0
Workflow
Get your Commvault Access Token.
Configure the Commvault plugin.
Add a Business Rule.
Configure Sharing between Threat Exchange and Commvault.
Validate the plugin.
Watch a Video
Click play to watch a video.
Get your Commvault Access Token
Log in to your Commvault Instance.
Click
Profile
on the top right to expand it.
Click
Profile
.
Click
Access tokens
.
Click
Add token
.
Enter a Token Name, Expire Date, and Scope, and then click
Submit
.
Copy the token and save it in a safe place because it will only be visible once.
Configure the Commvault Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the Commvault plugin box to configure the plugin.
Enter these values:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave default.
Aging Criteria
:
Expiry time of the plugin in days. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter these values:
Command Center API URL
:
Command Center URL where alerts are pushed to/pulled from, like
https://commandcenter.nam.contoso.com/
.
Commvault Access Token
:
Enter the Access Token generated from the
Profile > Access tokens
section of your Commvault platform.
Enable Polling: Enable/Disable polling Threat IOCs from Commvault. Disable if you only need to push Threat IOCs to Commvault.
Initial Range (in days): Number of days to pull the data for the initial run.
Click
Save
.
Add a Threat Exchange Business Rule for Commvault
To share indicators fetched from the Commvault to the Cloud Exchange and vice versa, you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule follow the below steps:
Go to
Threat Exchange > Business Rule > Create New Rule
.
Add the filter according to your requirement in the rule.
Configure Sharing for Netskope and Commvault
To share IoCs from the Cloud Exchange to the Commvault platform and vice versa, follow these steps:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Cloud Exchange), the Business Rule, Destination Configuration (Commvault), and Target as
Report client as Anomalous
.
Repeat step 2 for sharing Commvault IoCs to Cloud Exchange. Select your Source Configuration as Commvault, the Business Rule, and the Destination Configuration (Cloud Exchange).
Add a Target and select the existing IoCs List Name, or create a new IoCs list on the platform.
Click
Save
.
Note
Only the existing Clients on the Commvault platform can be tagged/marked as anomalous in Commvault, hence we cannot create new Client on the platform while sharing.
Validate the Commvault Plugin
Validate the Pull
Pulled data will be listed on the Threat IOCs page. You can filter the IOCs pulled from the platform using the Filter
:
sources.source Like “<plugin name>”. You can filter the logs from CE as well with the plugin name.
On the Commvault platform the IoCs are pulled from
CommandCenter > Unusual File Activities
.
Note
The IoCs will be pulled from all the tabs under the Unusal File Activities, except the External Software detected, since we push IoCs to that page.
Validate the Push
To validate the push in CE, go to
Logging
and filter shared logs for the Commvault plugin.
To check the ingested data on the platform, log in to Commvault and go to
CommandCenter > Unusual File Activities
. Click on the hostname and check the shared data under External software detected.
Troubleshooting
Unable to pull IOCs from the Commvault platform
After the plugin configuration if the IoCs are not pulled from the platform it might be due to one of the following.
No IoCs are available on the platform to pull
IoCs are not available for the given time range or do not match the configuration parameters
The event code does not match.
What to do:
Identity your root cause from above and follow below steps to resolve the issue.
No IoCs are available on the platform to pull: Check if you have data to be pulled from the
platform
if so check the initial range provided in the plugin configuration. The data available on the Commvault platform should match the initial range added in the plugin.
Below are the possible event codes that are matched in the plugin while pulling the IOCs as these event codes are associated with malicious events, if this Event Codes does not match during the pull call data won’t be pulled, 14:337, 7:333, 14:337, 69:59, 69:60.
Unable to share IoCs on Commvault
If you are unable to share IoCs to Commvault and receive below error.
Unable to share 50 indicator(s) from 50 indicator(s) to Commvault. The indicators may have an invalid value, or the client’s hostname might not be available in Commvault.
What to do:
To share the IoCs on Commvault it is necessary that the IoCs that are to be shared have a Host detected or Configured on the Commvault platform.
In this Topic
Commvault Plugin for Threat Exchange

---
## Palo Alto Networks Cortex XDR Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/palo-alto-networks-cortex-xdr-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:47:30+00:00
**Scraped:** 2026-08-11T07:28:30.282781+00:00

Palo Alto Networks Cortex XDR Plugin for Threat Exchange - Netskope Technical Documentation
Palo Alto Networks Cortex XDR Plugin for Threat Exchange
This document will provide the technical documentation required to configure the Palo Alto Networks Cortex XDR integration with the Threat Exchange module of the Netskope Cloud Exchange platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
Palo Alto Cortex Platform access for pulling and sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Your Palo Alto Networks Cortex XDR API credentials (API ID, Base URL, and Authentication Method).
Connectivity to the following host: Palo Alto Networks Cortex XDR login URL.
For example: https://api-wwt3.xdr.us.paloaltonetworks.com/
Plugin Scope
This plugin supports the pulling and sharing of indicators from/to the Palo Alto Networks Cortex XDR platform. The Palo Alto Networks Cortex XDR plugin fetches indicators of types File (MD5 and SHA256) from Palo Alto Networks Cortex XDR and stores them into Netskope CE. The plugin also supports sharing the Netskope CE indicators SHA256, MD5, URL ( IPv4, Domain) with existing groups on the Palo Alto Networks Cortex XDR platform.
Palo Alto Networks Cortex XDR Support
Fetched indicator types
SHA256, MD5
Shared indicator types
SHA256, MD5, URL (IPv4, Domain)
Mappings
Mappings for Pull (Netskope field – Palo Alto Networks Cortex XDR fields)
Netskope CE Fields
Palo Alto Networks Cortex XDR Fields
Value
action_process_image_sha256, action_process_image_md5
Severity
severity (informational ⇒ Low) other levels are the same as it is)
Comments
Description:
<description>
, Host Name:
<host_name>
, Matching Status:
<matching_status>
, Source:
<source>
, Resolution Status: resolution_status
Firstseen
event_timestamp
Lastseen
event_timestamp
Tags
tags+original_tags
Mapping for Push (Netskope field – Third Party field)
Netskope CE Fields
Palo Alto Networks Cortex XDR Fields
value
md5, sha256, URL(IPv4, Domain)
type
URL (IPv4, Domain),SHA256, MD5
severity
unknown > Informational
low > LOW
Medium > MEDIUM
High > HIGH
Critical > CRITICAL
comments
comments
expiresAt
expiration_date
Permissions
To create an API user, ensure that you have the Organisation Administrator role to the Palo Alto Networks Cortex XDR platform for creating an API User for getting the API Key ID, API Key, and Authentication Method.
To pull and push data from/to Palo Alto Networks Cortex XDR make sure your user has the below rights.
Functionality
Permissions
Pull Indicators
Select the following:
Alerts & Incidents (
View
)
Push Indicators
Select the following:
Detections (
View/Edit
)
API Details
List of APIs used
API Detail
Method
API Endpoint
Pull Indicators
POST
/public_api/v1/alerts/get_alerts_multi_events/
Push Indicators
POST
/public_api/v1/indicators/insert_jsons
Pull Indicators
Example:
API Endpoint:
POST public_api/v1/alerts/get_alerts_multi_events/
Method
: Post
Parameter:
None
API Request Endpoint
:
{
    "request_data": {
        "filters": [
            {
                "field": "creation_time",
                "operator": "gte",
                "value": 1664794415000
            },
            {
                "field": "severity",
                "operator": "in",
                "value": [
                    "informational",
                    "low",
                    "medium",
                    "high",
                    "critical"
                ]
            }
        ],
        "search_from": 0,
        "search_to": 1,
        "sort": {
            "field": "creation_time",
            "keyword": "asc"
        }
    }
}
API Response:
{
    "reply": {
        "total_count": 887,
        "result_count": 1,
        "alerts": [
            {
                "external_id": "7904b8db15cc4658b1e617dbafef1cca",
                "severity": "medium",
                "matching_status": "UNMATCHABLE",
                "end_match_attempt_ts": null,
                "local_insert_ts": 1683342672687,
                "last_modified_ts": null,
                "bioc_indicator": null,
                "matching_service_rule_id": null,
                "attempt_counter": 0,
                "bioc_category_enum_key": null,
                "is_whitelisted": false,
                "starred": false,
                "deduplicate_tokens": null,
                "filter_rule_id": null,
                "mitre_technique_id_and_name": null,
                "mitre_tactic_id_and_name": null,
                "agent_version": "8.0.1.44",
                "agent_ip_addresses_v6": null,
                "agent_device_domain": null,
                "agent_fqdn": "Matthewharding's iPhone 14 Pro",
                "agent_os_type": "iOS",
                "agent_os_sub_type": "16.4.1",
                "agent_data_collection_status": null,
                "mac": null,
                "is_pcap": false,
                "alert_type": "Unclassified",
                "resolution_status": "STATUS_010_NEW",
                "resolution_comment": null,
                "dynamic_fields": null,
                "tags": [
                    "DS:PANW/XDR Agent"
                ],
                "malicious_urls": null,
                "events": [
                    {
                        "agent_install_type": "STANDARD",
                        "agent_host_boot_time": null,
                        "event_sub_type": null,
                        "module_id": "Incoming call or message reported as spam",
                        "association_strength": 50,
                        "dst_association_strength": null,
                        "story_id": null,
                        "event_id": null,
                        "event_type": null,
                        "event_timestamp": 1683342667518,
                        "actor_process_instance_id": null,
                        "actor_process_image_path": null,
                        "actor_process_image_name": null,
                        "actor_process_command_line": null,
                        "actor_process_signature_status": "N/A",
                        "actor_process_signature_vendor": null,
                        "actor_process_image_sha256": null,
                        "actor_process_image_md5": null,
                        "actor_process_causality_id": null,
                        "actor_causality_id": null,
                        "actor_process_os_pid": null,
                        "actor_thread_thread_id": null,
                        "causality_actor_process_image_name": null,
                        "causality_actor_process_command_line": null,
                        "causality_actor_process_image_path": null,
                        "causality_actor_process_signature_vendor": null,
                        "causality_actor_process_signature_status": "N/A",
                        "causality_actor_causality_id": null,
                        "causality_actor_process_execution_time": null,
                        "causality_actor_process_image_md5": null,
                        "causality_actor_process_image_sha256": null,
                        "action_file_path": null,
                        "action_file_name": null,
                        "action_file_md5": null,
                        "action_file_sha256": null,
                        "action_file_macro_sha256": null,
                        "action_registry_data": null,
                        "action_registry_key_name": null,
                        "action_registry_value_name": null,
                        "action_registry_full_key": null,
                        "action_local_ip": null,
                        "action_local_ip_v6": null,
                        "action_local_port": null,
                        "action_remote_ip": null,
                        "action_remote_ip_v6": null,
                        "action_remote_port": null,
                        "action_external_hostname": null,
                        "action_country": "UNKNOWN",
                        "action_process_instance_id": null,
                        "action_process_causality_id": null,
                        "action_process_image_name": null,
                        "action_process_image_sha256": null,
                        "action_process_image_command_line": null,
                        "action_process_signature_status": "N/A",
                        "action_process_signature_vendor": null,
                        "os_actor_effective_username": null,
                        "os_actor_process_instance_id": null,
                        "os_actor_process_image_path": null,
                        "os_actor_process_image_name": null,
                        "os_actor_process_command_line": null,
                        "os_actor_process_signature_status": "N/A",
                        "os_actor_process_signature_vendor": null,
                        "os_actor_process_image_sha256": null,
                        "os_actor_process_causality_id": null,
                        "os_actor_causality_id": null,
                        "os_actor_process_os_pid": null,
                        "os_actor_thread_thread_id": null,
                        "fw_app_id": null,
                        "fw_interface_from": null,
                        "fw_interface_to": null,
                        "fw_rule": null,
                        "fw_rule_id": null,
                        "fw_device_name": null,
                        "fw_serial_number": null,
                        "fw_url_domain": null,
                        "fw_email_subject": null,
                        "fw_email_sender": null,
                        "fw_email_recipient": null,
                        "fw_app_subcategory": null,
                        "fw_app_category": null,
                        "fw_app_technology": null,
                        "fw_vsys": null,
                        "fw_xff": null,
                        "fw_misc": null,
                        "fw_is_phishing": "N/A",
                        "dst_agent_id": null,
                        "dst_causality_actor_process_execution_time": null,
                        "dns_query_name": null,
                        "dst_action_external_hostname": null,
                        "dst_action_country": null,
                        "dst_action_external_port": null,
                        "contains_featured_host": "NO",
                        "contains_featured_user": "NO",
                        "contains_featured_ip": "NO",
                        "image_name": null,
                        "container_id": null,
                        "cluster_name": null,
                        "referenced_resource": null,
                        "operation_name": null,
                        "identity_sub_type": null,
                        "identity_type": null,
                        "project": null,
                        "cloud_provider": null,
                        "resource_type": null,
                        "resource_sub_type": null,
                        "user_agent": null,
                        "user_name": "matthewharding"
                    }
                ],
                "alert_id": "179151",
                "detection_timestamp": 1683342667518,
                "name": "Incoming call or message reported as spam",
                "category": "Spam",
                "endpoint_id": "36c16cd205934e2fbf1bc874a1479b03",
                "description": "A number was reported by the user as spam",
                "host_ip": null,
                "host_name": "Matthewharding's iPhone 14 Pro",
                "mac_addresses": null,
                "source": "XDR Agent",
                "action": "REPORTED",
                "action_pretty": "Detected (Reported)",
                "original_tags": [
                    "DS:PANW/XDR Agent"
                ]
            }
        ]
    }
}
Push Indicators
Example:
API Endpoint:
POST public_api/v1/indicators/insert_json
Method
: Post
Parameter:
None
API Request Endpoint
:
{
    "request_data": [
        {
            "severity": "MEDIUM",
            "comment": "\\Device\\HarddiskVolume2\\Windows\\System32\\mavinject.exe",
            "vendors": [
                {
                    "vendor_name": "Netskope Cloud Exchange"
                }
            ],
            "expiration_date": 1704215925000,
            "indicator": "7562cf3c1237df992a6b8885b5ad5eaf1b5c40840bbe0d1ce09c2d61b5a12c44",
            "type": "HASH"
        }
    ],
    "validate": true
}
Performance Matrix
Below is the performance reading conducted for fetching and sharing 100K IOCs in each plugin lifecycle on a Large CE instance with the below specifications.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Palo Alto Networks Cortex XDR
~10K per minute
Indicators shared to Palo Alto Networks Cortex XDR
~16K per minute
User Agent
The user agent added for this plugin is in the following format:
netskope-ce-<CE VERSION>-<MODULE NAME>-<PLUGIN NAME>-v<PLUGIN VERSION>
Example
netskope-ce-4.2.0-cte-palo-alto-networks-cortex-xdr-v1.0.0
Workflow
Get an API Key from the Palo Alto Networks Cortex XDR platform.
Configure the Palo Alto Networks Cortex XDR plugin.
Add a Business Rule.
Configure Sharing for Netskope and the Palo Alto Networks Cortex XDR.
Validate the Palo Alto Networks Cortex XDR plugin.
Click play to watch a video.
Get your Palo Alto Networks Cortex XDR API Key
Go to your Palo Alto Networks Cortex XDR platform and log in with your credentials.
On the Bottom left navigation bar, hover over
Settings
and select
Configurations Settings
.
Click
API Keys
, then click
New Key
.
Enter the following information:
Security Level: Select Security Level from Advanced/Standard.
Role: Create a Custom Role with (Detections (
View/Edit
)/Alerts & Incidents (
View
)).
Enable Expiration Date: Check the box with API Key to set the expire date.
Click
Save
.
Copy the API Key, as it will not be accessible after the window is closed.
Configure the Palo Alto Networks Cortex XDR Plugin
Go to
Settings > Plugins
, search for and select the CTE Palo Alto Networks Cortex XDR box to configure the plugin.
Enter these values:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave the default.
Aging Criteria: Expiry time of the plugin in days. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if a proxy is required for communication.
Click
Next
.
Enter these values:
Base URL: Base URL for Palo Alto Networks Cortex XDR API Endpoints.
API ID: API ID of Palo Alto Networks Cortex XDR API.
API Key: Secret Key of Palo Alto Networks Cortex XDR API.
Authentication Method: Type of Authentication you choose while creating the API Token from Palo Alto Networks Cortex XDR.
Enable Polling: If you want to pull indicator from Palo Alto Networks Cortex XDR.
Type of Threat data to Pull: SHA256/MD5.
Severity: If you want to pull any specific Severity data.
Enable Tagging: Enable/Disable tagging functionality.
Initial Range: Number of days to pull the data for the initial run.
Click
Save
.
Add a Business Rule for Palo Alto Networks Cortex XDR
To share indicators from Netskope CE to Palo Alto Networks Cortex XDR and Palo Alto Networks Cortex XDR’s indicators to Netskope or any Third-party plugin you need a have a business rule that will filter out the indicators that you need to share. To configure a business rule follow the below steps:
Go to
Threat Exchange > Business Rule
and click
Create New Rule
.
Add your required filter for the IoCs you want to share and click
Save
.
Configuring Sharing for Netskope and Palo Alto Networks Cortex XDR
Palo Alto Networks Cortex XDR plugin supports the sharing of URLs(IPv4, Domain), MD5, and SHA256 types of IOCs. The plugin has a
Create IOCs
action that will create indicators. To share IoCs with Palo Alto Networks Cortex XDR, follow these steps:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Netskope), the Business Rule, and Destination Configuration (Palo Alto Networks Cortex XDR), and for Target, enter
Create IOCs
.
Click
Save
.
Create another Sharing Configuration to share Palo Alto Networks Cortex XDR IoCs with Netskope. Select Palo Alto Networks Cortex XDR as the Source, and Netskope as the Destination.
Click
Save
.
Validate the Palo Alto Networks Cortex XDR Plugin
Validate the Pull
SHA256,MD5 are pulled from INCIDENT RESPONSE > Incidents, from the Palo Alto Networks Cortex XDR plugin.
Click
Alerts & Insights
, and then click any alert to expand it to find the SHA256 and MD5 values that will be pulled.
Based on your plugin configuration, Indicators will pull from the Palo Alto Networks Cortex XDR plugin to Netskope CE.
Go to
Threat Exchange > Threat IoCs
and search for IoCs pulled from the Palo Alto Networks Cortex XDR plugin.
Validate the Push
To verify pushed IoCs in Palo Alto Networks Cortex XDR, go to
Palo Alto Networks Cortex XDR Platform > DETECTION RULES > IOC
.
IoCs pushed from Netskope have been VENDORS as Netskope Cloud Exchange.
To validate the pushed indicator in Threat Exchange, go to
Threat IoCs
and search for IoCs that are shared with Palo Alto Networks Cortex XDR.
Note:
The Palo Alto Networks Cortex XDR platform can accommodate up to 4 million IOCs. Once this limit is reached, any newly ingested indicators will be discarded.
Reference Link
Troubleshooting
Receiving the 400 Client Error in logs while executing the plugin life cycle.
While saving the plugin if plugin is no able to save with valid creds 401.
If you are receiving the above-mentioned error in log while configuring the plugin check the authentication method in Palo Alto Networks Cortex XDR
Log in to Cortex XDR Platform.
Click
Setting > Configurations
.
Click
API Keys
.
Check the Security Level and Authentication Method in Plugin (both should be the same).
When Receiving 403 permission while pulling or pushing IoCs
If you receive 403 permission while pulling or pushing IoCs check the roles on Palo Alto Networks Cortex XDR.
Log in to Cortex XDR Platform.
Go to
Setting > Configurations > Roles
.
Check the roles.
Expand
INCIDENT RESPONSE
.
Alerts & Incidents should have View Permission.
Expand
DETECTION & Threat INTEL
.
Rules should have View/Edit Permission.
When not able to fetch IoCs from Palo Alto Networks Cortex XDR
If you are not able to fetch IoCs from Palo Alto Cortex to Netskope Threat Exchange.
Log in to Palo Alto Networks Cortex XDR.
Click
Incident Response > Incidents
.
Check the Alerts are present while clicking on any
Incident > Alerts & Insights
.
In this Topic
Palo Alto Networks Cortex XDR Plugin for Threat Exchange

---
## Anomali ThreatStream XDR Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/anomali-threatstream-xdr-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:38:52+00:00
**Scraped:** 2026-08-11T07:28:32.775803+00:00

Anomali ThreatStream XDR Plugin for Threat Exchange - Netskope Technical Documentation
Anomali ThreatStream XDR Plugin for Threat Exchange
This document explains how to configure the Anomali ThreatStream XDR v1.3.2 plugin for the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to fetch the indicators of type URL, IP (IPv4, IPv6), Domain, SHA256, and MD5 from the Observables on Anomali ThreatStream XDR. This plugin supports sharing MD5, SHA256, URL, Domain, IPv4 and IPv6 to Observables on the Anomali ThreatStream XDR platform using the Share Indicators action.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
An Anomali Threatstream Cloud Platform or On-Premises instance.
Connectivity to the following hosts:
For Cloud Platform : https://api.threatstream.com.
For On-Premises: https://
<ThreatStream_On-Premises_IP_or_FQDN
>.
Anomali Threatstream XDR Plugin Supports
The plugin is used to pull and push IoCs of type URL, IPv4, IPv6, Domains, MD5, and SHA256 from/to Anomali ThreatStream XDR’s Observables.
Fetched Indicator Types
Shared Indicator Types
URL, Domains, IP(IPv4), IPv6, SHA256, MD5
URL, Domains, IP(IPv4), IPv6, SHA256, MD5
IoC Retraction
Anomali Threatstream XDR plugin supports pull retraction. Pull retraction will be based on the Retraction Interval field under configuration parameters and configured plugin filters. This means the IoCs present under the Retraction Interval range will not be marked as retracted and rest of the IoCs will be marked as retracted in Cloud Exchange.
IoC Retraction (Pull): Indicators will be fetched from Anomali and in the subsequent pull cycles. If some indicators are deleted from Anomali, they will be marked as Retracted in Cloud Exchange.
Type
Description
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
IoC Source Labeling
Indicator shared to the third party will have a field describing the source plugin which actually fetched this IoC.
Type
Description
IoC Source Labelling
Supported (Netskope CE |
<Source Plugin>
)
Mappings
Severity Mappings
Netskope Severity
Anomali ThreatStream XDR Severity
low
low
medium
medium
high
high
critical
very-high
unknown
–
Indicator Mappings for Pull and Push
Netskope Fields
Anomali ThreatStream XDR Observable Fields
value
value
type
type
firstSeen
created_ts
lastSeen
modified_ts
reputation
confidence
severity
meta.severity
comments
description
tags
tags.name
Reputation-Confidence Mappings
Netskope Reputation
Anomali ThreatStream XDR Confidence
1
1-10
2
11-20
3
21-30
4
31-40
5
41-50
6
51-60
7
61-70
8
71-80
9
81-90
10
91-100
Push Indicators Mappings
Anomali ThreatStream XDR Observable Field
Netskope Indicator Field
url for URL IoC Type
domain for Domain IOC type
scrip for IPv4 IoC type
ipv6 for IPV6 IoC Type
md5 for MD5 and SHA256 IoC Types
value
subtype(For SHA256 and MD5 only)
SHA256 for SHA256
MD5 for MD5
itype
ITypes selected for their Respective IOC type below are the Action parameters used for each IOC Type:
URL iType for URLs
IP iType for IPv4
IPv6 iType for IPv6
Domain iType for domains
Hash [MD5, SHA256] iType for SHA256 and MD5
severity
Severity
very-high if Critical
high if high
medium -> medium
low -> low
unknown -> “”
confidence
reputation
description
comments
tags.name
Tags + “netskope-ce” + “Netskope CE |
<Source Plugin Name>
”
Performance Matrix
This reading is conducted on a Large Cloud Exchange Stack wit
h
these specifications by pulling and pushing 100K IoCs.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Anomali ThreatStream XDR
~33K per minute
Indicators shared with Anomali ThreatStream XDR
~180K per minute
Permissions
These permissions are needed for the plugin configuration.
Approval Intel
Show API for Users
API Details
List of APIs used
API Endpoint
Method
Use Case
/api/v2/intelligence
GET
To pull indicators and check for modified indicators
/api/v2/intelligence/
PATCH
To push indicators
Pull indicators and check for modified indicators
API Endpoint:
/api/v2/intelligence
Method:
GET
Parameters:
Key
Value
limit
1000
modified_ts__gt
2024-01-23T13:33:40.314Z
update_id__gt
0
order_by
update_id
remote_api
true
type
domain,ip,ipv6,hash,url
hash$subtype(For SHA256 and MD5)
MD5,SHA256
confidence__gte
1
status
active
meta.severity
low,medium,high,very-high
tags
tag1, tag2
feed_id
0,1
Headers:
Key
Value
Authorization
apikey
<username>
:
<password>
Content-Type
application/json
Accept
application/json
User-Agent
netskope-ce-6.0.1-cte-anomali-threatstream-xdr-v1.3.2
Sample API Response:
{
“objects”: [
{
“source”: “Botscout BOT IPs”,
“threatscore”: 17,
“threat_type”: “bot”,
“trusted_circle_ids”: [
146,
211,
388
],
“description”: null,
“workgroups”: [],
“sort”: [
17729579514
],
“resource_uri”: “/api/v2/intelligence/60654060239/”,
“modified_ts”: “2023-10-18T11:11:57.115Z”,
“update_id”: 17729579514,
“source_reported_confidence”: 65,
“type”: “ipv6”,
“uuid”: “39a5d9b0-c48e-4831-afdb-511f57c039ec”,
“feed_id”: 141,
“retina_confidence”: -1,
“created_ts”: “2023-10-18T10:52:26.484Z”,
“id”: 60654060239,
“value”: “2401:4900:171:609:11:98:550:76”,
“itype”: “bot_ipv6”,
“org”: “”,
“confidence”: 65,
“expiration_ts”: “2024-01-16T10:52:23.000Z”,
“owner_organization_id”: 2,
“meta”: {
“severity”: “medium”,
“detail2”: “imported by user 668”
},
“is_anonymous”: false,
“is_public”: false,
“asn”: “”,
“status”: “active”,
“tags”: [
{
“id”: “1yx”,
“name”: “childfirstbehaviortherapy.seo”
},
{
“id”: “3t7”,
“name”: “childfirstbehaviortherapy.seo@gmail.com”
}
],
“can_add_public_tags”: false,
“subtype”: null,
“tlp”: null,
“created_by”: null,
“rdns”: null,
“is_editable”: false
}
],
“meta”: {
“offset”: 0,
“limit”: 1,
“total_count”: 1499,
“next”: “/api/v2/intelligence/?limit=1&modified_ts__gt=2023-04-08T19%3A46%3A42.345Z&order_by=update_id&status=active&type=ipv6&update_id__gt=0&search_after=17729579514”,
“took”: 34
}
}
Push Indicators
API Endpoint:
/api/v2/intelligence/
Method:
PATCH
Request Body:
{
    "meta": {
        "classification": "private",
        "allow_unresolved": true,
        "allow_update": true,
        "enrich": false
    },
    "objects": [
        {
            "url": "https://185.67.81.10",
            "severity": "high",
            "itype": "compromised_url",
            "type": "url",
            "tags": [
                {
                    "name": "Netskope CE | MISp",
                    "tlp": "white"
                },
                {
                    "name": "netskope-test",
                    "tlp": "white"
                }
            ]
        }
    ]
}
Headers:
Key
Value
Authorization
apikey
<username>
:
<password>
Content-Type
application/json
Accept
application/json
User-Agent
netskope-ce-6.0.1-cte-anomali-threatstream-xdr-v1.3.2
Sample API Response:
202 Accepted
User Agent
netskope-ce-6.0.1-cte-anomali-threatstream-xdr-v1.3.2
Workflow
Get your Anomali ThreatStream XDR credentials.
Configure the Anomali ThreatStream XDR plugin.
Configure a Business Rule for Anomali ThreatStream XDR.
Configure Sharing between Netskope and Anomali ThreatStream XDR.
Validate the Anomali ThreatStream XDR plugin.
Watch a Video
Click play to watch a video.
Get your Anomali ThreatStream XDR Credentials
Contact your Anomali Support team to get your Base URL, Username, and API Key.
Configure the Anomali ThreatStream XDR Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Anomali ThreatStream XDR v1.3.2 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Leave default.
Aging Criteria:
Expiry time of the plugin in days (Default: 90).
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Click
Next
and enter the Configuration Parameters:
Base URL:
The ThreatStream API Base URL based on your Cloud or On-Premises instance.
Username:
ThreatStream platform username (used while logging to platform).
API Key:
API Key fetched from the ThreatStream Anomali XDR platform.
Remote Observables:
Select Yes or No to retrieve the Remote Observables.
Type of Threat Data to pull:
Select based on the data you want to pull. The plugin supports type and subtype filtering from Anomali for the IoC types supported in Cloud Exchange.
Minimum Confidence:
Provide value for confidence(in range of 1-100) IoCs whose confidence is greater than or equal to the provided value will be pulled.
Severity:
IoCs with provided severity will be pulled.
Status:
IoCs with matching Status will be fetched.
Tags:
Indicators matching the Tags will be pulled, enter single or multiple comma separated Tag names. Keep blank to pull IoCs with all Tags.
Feed ID:
Indicators matching the Feed ID will be pulled, enter single or multiple comma separated numeric values for Feed ID. Keep blank to pull IoCs from all feeds.
Note
When multiple Tags or Feed IDs are added, the plugin will pull data from each mentioned tag using the OR operation.
If you have added both Tags and Feed ID in the plugin for pulling the data, the IoCs will be pulled using AND operation between the tags and Feed ID, i.e. IoCs will only be pulled if the specified Feed ID has the mentioned tags.
Enable Polling:
Keep Yes to pull data, Keep No if plugin is used for pushing.
Enable Tagging:
Keep Yes to pull tags along with all IoCs from the platform.
Retraction Interval:
Specify the number of days for which IoC retraction should be run for Anomali ThreatStream XDR indicators. Note: This parameter is applicable only for Cloud Exchange version 5.1.0 or later, and if IoC(s) Retraction is enabled in Threat Exchange Settings.
Initial Range:
Number of days Threat IoCs to pull from initial range.
Click
Save
. Your plugin configuration is shown in
Plugins
.
Congfigure a Threat Exchange Business Rule for Anomali ThreatStream XDR
To share indicators fetched from the Anomali ThreatStream XDR to the Cloud Exchange and vice versa, you will need to have a business rule that will filter out the indicators that you want to share.
To configure a business rule:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirement in the rule, and click
Save
.
Configure Sharing for Netskope and Anomali ThreatStream XDR
To share IoCs from Cloud Exchangeto the Anomali ThreatStream XDR platform, or vice versa, follow these steps:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Netskope CTE), Business Rule, Destination Configuration (Anomali ThreatStream XDR), and Target.
Select these parameters:
URL iType:
Select the iType that you want to assign to your URL.
IP iType:
Select the iType that you want to assign to your IP.
IPv6 iType:
Select the iType that you want to assign to your IPv6.
Domain iType:
Select the iType that you want to assign to your Domain.
Hash[MD5, SHA256] iType:
Select the iType that you want to assign to your Hash [MD5, SHA256].
Follow the same steps but vice versa for sharing Anomali ThreatStream XDR IoCs to Netskope select your Source Configuration as Anomali ThreatStream XDR, Business Rule, Destination Configuration(Netskope CTE), and Target. Refer to the
Netskope plugin guide
for more details.
Click
Save
.
Validate the Anomali ThreatStream XDR Plugin
Validate the Pull
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE Anomali ThreatStream XDR plugin.
To verify the data available for pulling in Anomali ThreatStream XDR, go to
Analyze > Observables
.
To verify the Retracted IoCs, check the logs for IoC Retraction example:
message Like CTE Anomali ThreatStream XDR [CTE Anomali ThreatStream XDR] [Retraction]:
You can filter the retracted IoCs from the platform using the filter:
sources.source Is equal “<plugin configuration name>” && sources.retracted Is equal true
Note
The IoCs that fall under the Retraction Interval will be marked as Retracted: Yes in Cloud Exchange.
Here you can see IoCs were added to the URL list on Netskope Tenant.
Then some of the shared IoCs got marked as retracted so it was deleted from the URL list.
Note
Anomali does not support the deletion (retraction) of IoCs on their platform. As a result, any previously shared IoCs will not be deleted (retracted) on Anomali.
Validate the Push
Shared IoCs to Anomali can be verified from logs available at
Logging
in Cloud Exchange.
Note
The Anomali has a limit to ingest 10MB data in one push cycle, so if the data to be ingested is more than 10MB it will be divided in 10MB chunks to push.
On the Anomali platform, go to
Analyze > Observables, IOC
. Pushed IoCs from Cloud Exchange will have
netskope-ce
added as a tag.
Note
All IoCs pushed from Cloud Exchange will have the Visibility as private, like My Organization, and it will not be a part of the Anomali community.
Note
You can also use the IoC source labeling to filter the shared IOCs according to the source plugin. For example to filter shared IoCs which were pulled from Netskope tenant you can use this filter as a tag:
Tag format: “Netskope CE |<source plugin name>”
Troubleshooting the Anomali ThreatStream Plugin
Unable to pull IoCs from the Anomali ThreatStream platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IoCs are available on the platform to pull.
IoCs are not available for the given time range or does not match the configuration parameters.
What to do:
Identity your root cause noted above, and then follow one of the next two sections to resolve the issue.
No IoCs are
available
on the platform to pull
Check if the IoCs are
available on the platform
to pull. If available, check the resolution mentioned in the next section.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Anomali platform, check if you have data for the given time range.
If the data is still available for the given time range, it might be possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter and filter the same on the Anomali platform.
Also, make sure that you have
Yes
selected in the enable polling to pull the IoCs.
Unable to push the IoCs to Anomali
If you are not able to push the IoCs on the platform and receive an error while pushing, it might be due to insufficient
permissions
for the user.
IoCs are pushed from CE but not available on the Anomali platform
If IoCs are pushed and not reflected on the platform, it might be due to the IoCs count being too big. When data is shared to Anomali, it sometimes takes time to reflect on the platform. At the most 10MB data can be shared in a page at a time.
What to do:
The pushed data will be reflected, but it might take some time, sometimes minutes, sometimes hours, so we suggest waiting for the data to be reflected.
Known Behaviors
Following are the things that have been noticed while verifying the plugin workflow.
Sometimes multiple IoCs for a single record are created on the Anomali ThreatStream platform after the IoCs are shared.
Sometimes ingested IoCs take time to reflect on the Anomali platform after IoCs are pushed. This might take minutes or in some cases hours.
Unknown severity from Cloud Exchange is not mapped in Anomali, so when IoCs are shared with Unknown severity, the platform calculates its own severity and assigns it to the IoC.
The iType for the IoCs won’t be updated if the IoCs are reshared with updated iType.
Sometimes if an IoC with a matching value already exists on the Anomali ThreatStream platform as an expired indicator, the platform does not modify or update the existing IoC, even when a successful API call is made to push the same IoC.
Certain URLs shared via API calls may not be displayed in the Anomali ThreatStream UI, despite being accepted by the API. This could be due to additional filtering or validation applied on the platform’s end.
Anomali API provides multiple IoC objects in the API response, and in some cases, the IoC values are the same, but some other parameters like severity, reputation, etc. are different.
In this Topic
Anomali ThreatStream XDR Plugin for Threat Exchange

---
## Trellix Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/trellix-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:55:19+00:00
**Scraped:** 2026-08-11T07:29:20.435948+00:00

Trellix Plugin for Threat Exchange - Netskope Technical Documentation
Trellix Plugin for Threat Exchange
This document explains how to configure the Trellix plugin for the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches MD5, SHA256, URL (Domain, IP (IPv4, IPv6), URL) from Trellix EPO. This plugin does not support pushing data to the Trellix platform.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on the Netskope tenant.
A
URL List
on the Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Trellix platform access.
Trellix developer access with pre-approved client credentials.
Connectivity to the following host: Trellix Platform (Example:
https://api.manage.trellix.com
)
Trellix Plugin Support
Fetched indicator types
URL (Domains, URLs, IP(IPv4, IPv6)), SHA256, MD5
Shared indicator types
Not Supported
Mappings
Severity
Trellix Severity
CE Severity
Destruction (>70)
Critical
Malicious (51-70)
High
Malicious Enabler (31-50)
Medium
Probable Malicious (16-30)
Low
Dual Use (1-15)
Low
Unconfirmed (0/Null)
Unknown
Mappings for Pull (Netskope fields – Trellix fields)
Netskope CE Fields
Trellix Fields
type
attributes.type
value
attributes.value
firstSeen
attributes.created-on
comments
attributes.comments
severity
attributes.lethality
Permissions
Below are the permissions needed for the plugin workflow to pull data from Trellix using Get IoCs API.
Note: You need to generate a Client ID and Client Secret from Trellix Platform; for that contact Trellix support.
Ins.user
Ins.suser
ins.ms.
soc.act.tg
API Details
List of APIs used
API Endpoint
API Method
Use Case
https://iam.mcafee-cloud.com/iam/v1.4/token
POST
Used for authorization process & Generating access token.
https://api.manage.trellix.com/insights/v2/iocs
GET
Used for pulling indicators in pagination from Trellix Platform.
Authorization API
API Endpoint:
https://iam.mcafee-cloud.com/iam/v1.4/token
API Method:
POST
Headers:
Key
Value
Authorization
<Basic Token>
Content-Type
application/json
x-api-key
<Trellix API Key>
Accept
application/json
Body:
Key
Value
scope
[“ins.user | ins.suser | ins.ms.r | soc.act.tg”]
grant_type
client_credentials
audience
iam_client
Sample API Response:
{
    "tid": 1134613553,
    "token_type": "Bearer",
    "expires_in": 600,
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImI3SUFJeXpseDUyOG9sdjZWNEx6dFRRU0oxWSIsImtpZCI6ImI3SUFJeXpseDUyOG9sdjZWNEx6dFRRU0oxWSJ9.eyJpYXQiOjE3MTIwNjU1NjksImp0aSI6Ijg3OWRhMThlLWJlNjYtNDI5MS0wODhhLTE4NWVlMGI4MTY2MiIsIm5iZiI6MTcxMjA2NTU1OSwiZXhwIjoxNzEyMDY2MTY5LCJzdWIiOiJMRUkzU2pobHJKRzF2QVdZTGZSTk5xd3l4IiwiY2xpZW50X2lkIjoiTEVJM1NqaGxySkcxdkFXWUxmUk5OcXd5eCIsImlzcyI6Imh0dHBzOi8vaWFtLm1jYWZlZS1jbG91ZC5jb20vaWFtL3YxLjAiLCJzY29wZSI6Imlucy5tcy5yIGlucy5zdXNlciIsImNsaWVudF90eXBlIjoiTmV0c2tvcGVEZWxlZ2F0ZSIsInRlbmFudF9pZCI6IkQxOTU4NTcwLUY1NUEtNDRCOC04QjQ0LTE1M0ExRTQ5NUFBNyIsImF1ZCI6ImlhbV9jbGllbnQiLCJhcGkiOiJ2MS40IiwidG9rZW5faWQiOiJIdTRoZ2tGQWdWWG52SVc4aGRncmp3cnJyIn0.cdOP9qC49Szr55JHZNMVnsIPYEeKt99OO8Xi_SMr485P1f7SaSUL07nTSJZHIxVDs82C3pbW7RpA4TWLYmpnxbj8T8kUwsOlPFwz_13aQkN_RGDB3C4ahpG6KDTtsl6suqTCmwNQhABmMpIo0O75YmXZsrIcj_0pesXPgzXeDsICiUVTdwkheQETE6uX2MKHJpPak5sbCcyxIXyk5uRD9z2O9PqGr8M_D3QHV_PZgLYwuC0UlwKXXeSg6JrdM75UQowF1pRarDacv9EyYBfOc0eAKfTtQuOiLGBU4_xQbXDArm"
}
Get IoCs API
API Endpoint:
<Trellix Base URL>/insights/v2/iocs
API Method:
GET
Headers:
Key
Value
Authorization
<Bearer Token>
Content-Type
application/json
x-api-key
<Trellix API Key>
Accept
application/json
Query Parameters:
Key
Value
filter[created_on][gte]
String representation of date & time
page[limit]
1000 is max supported limit by Trellix
page[offset]
Starting from 0
Sample API Response:
{
    "links": {
        "self": "https://api.manage.trellix.com/insights/v2/iocs?filter[created_on][gte]=2024-03-19T06:55:42.989219Z&page[limit]=1000&page[offset]=0",
        "first": "https://api.manage.trellix.com/insights/v2/iocs?filter[created_on][gte]=2024-03-19T06:55:42.989219Z&page[limit]=1000&page[offset]=0",
        "last": "https://api.manage.trellix.com/insights/v2/iocs?filter[created_on][gte]=2024-03-19T06:55:42.989219Z&page[limit]=1000&page[offset]=23000",
        "prev": null,
        "next": "https://api.manage.trellix.com/insights/v2/iocs?filter[created_on][gte]=2024-03-19T06:55:42.989219Z&page[limit]=1000&page[offset]=1000"
    },
"data": [
        {
            "type": "iocs",
            "id": "0004f51a-e281-4764-9912-498d4aaf3c80",
            "links": {
                "self": "https://api.manage.trellix.com/insights/v2/iocs/0004f51a-e281-4764-9912-498d4aaf3c80"
            },
            "attributes": {
                "type": "sha1",
                "value": "9c45cd81c6d70dc584a58646aab8fdfc1102501b",
                "coverage": null,
                "uid": "e90bdf44-d93a-48df-a998-4271f5486922",
                "is-coat": 0,
                "is-sdb-dirty": 0,
                "category": "Payload delivery",
                "comment": "",
                "lethality": 70,
                "determinism": 30,
                "created-on": "2024-03-30T13:33:20.000Z"
            },
            "relationships": {
                "campaigns": {
                    "links": {
                        "self": "https://api.manage.trellix.com/insights/v2/iocs/0004f51a-e281-4764-9912-498d4aaf3c80/relationships/campaigns",
                        "related": "https://api.manage.trellix.com/insights/v2/iocs/0004f51a-e281-4764-9912-498d4aaf3c80/campaigns"
                    }
                }
            }
        },
    ]
}
Performance Matrix
This reading is conducted on a Large CE Stack with below mentioned specs by pulling and pushing 100K IOCs.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Trellix
~2.4k per minute
User Agent
netskope-ce-5.0.1-cte-trellix-v1.0.0
Workflow
Get the API Key, Client Secret and Client ID.
Configure the Trellix plugin.
Configure a Business Rule.
Configure Sharing.
Validate the plugin.
Click play to watch a video.
Get your Trellix API Token, Client ID, and Client Secret
Log in to your Trellix Developer Portal and click
Self Service
.
Under Self Service, click
API Access Management
.
Copy the API Key.
Scroll down and generate Client ID and Client Secret, and then copy them.
Configure the Trellix Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the Trellix plugin box to configure the plugin.
Enter and select these parameters:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave the default.
Aging Criteria: Expiry time of the plugin in days (Default: 90).
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter and select these parameters:
Base URL: Trellix Base URL. For example:
https://api.manage.trellix.com/
.
API Key: The Trellix API Key you obtained earlier.
Client ID: The Client ID you obtained earlier.
Client Secret: Client Secret you obtained earlier.
Type of Threat data to pull: Type of Threat data to pull. Allowed values are MD5, SHA256, Domain, URL, and IP.
Initial Range: Number of days Threat IOCs to pull from initial range.
Click
Save
.
Configure a Threat Exchange Business Rule for the Trellix Plugin
To share indicators fetched from the Trellix to the Netskope CE, you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule:
In Threat Exchange, go to
Business Rule
and click
Create New Rule
.
Add the filter according to your requirement in the rule, and then click
Save
.
Configure Threat Exchange Sharing for the Trellix Plugin
To share IoCs from Trellix to Netskope:
In Threat Exchange go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (Trellix), a Business Rule, Destination Configuration (Netskope CTE), and Target.
Click
Save
.
Validate the Trellix Plugin
Validate the Pull
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the filter:
IoC by Sources-Source-Contains
-<
plugin name>
.
To verify pulled logs on Cloud Exchange, go to
Logging
and search logs from the CTE Trellix plugin.
To verify the data available for pulling on Trellix:
Log in to Trellix.
On the left menu bar under MVISION, click
Trellix Insights
.
Under Campaigns, click on any one.
Validate the Push
To validate the push in Cloud Exchange, go to
Logging
and filter shared logs for CTE Netskope.
To verify on the Netskope Tenant.
Log in to your Tenant.
Click
Policies
.
Click
File
(for Sha256).
Locate the File Profile name that you entered while configuring sharing.
For URLs (IP and Domain)
Click
Web > URL Lists
.
Click on the URL List that was used while configuring sharing.
Troubleshooting
Indicators are not pulled from the Trellix platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of the following.
IoCs are not available on the platform to pull.
IoCs are not available for the given time range.
Go to the Trellix Platform and on the left menu bar, under MVISION, click
Trellix Insights
.
Check the campaigns are available.
IoCs are not available for the given time range
If the IOoCs are available on the platform to pull, but the plugin has not pulled the IoCs in CE, check the number of days mentioned in the initial range parameter of the plugin configuration. On Trellix, check if you have data for the given time range.
Known Behavior
We have received 429 errors while pulling the IoCs from the Trellix Platform, and the limit does not get reset until the next day. The process of pulling the IoCs from the Trellix Platform resulted in a series of 429 errors. Regrettably, the limit for these errors will not reset until the next day.
In this Topic
Trellix Plugin for Threat Exchange

---
## Malware
**URL:** https://docs.netskope.com/en/about-malware/
**Last Modified:** 2026-07-06T19:52:34+00:00
**Scraped:** 2026-08-11T07:30:41.433919+00:00

Malware - Netskope Technical Documentation
Malware
To view files affected by malware in your organization, go to
Incidents
>
Malware
.
At the top, you can see the following statistics from the last 90 days:
The total files analyzed by the Advanced Threat Protection engine.
The total unique detections matched from the Netskope Cloud Effect.
The total new files analyzed by the Multi-Stage Sandbox.
Viewing File Incidents
In the
Files
tab, you can:
Refresh the malware incident results.
Filter malware incidents by a specific time frame. You can use a predefined time frame or choose
Date Range
to use the calendar and time menus to customize your own.
Click
+ Add Filter
to filter the malware incidents and narrow your search results. You also can click
to search and filter the malware incidents by a query.
View the primary metrics of the malware incidents:
Users Affected
: The total number of users whose files were affected by malware.
Malware
: The total number of malware detected by the scan.
Incidents
: The total number of malware incidents detected with Real-Time Protection.
View a list of files affected by the malware. For each file, you can see the following information:
File Name
: The names of the files associated with the malware. Click to view the
file details
.
Application
: The application associated with the file and affected by the malware.
User
: The user affected by the malware.
Instance
: The instance of the accessed application.
Exposure
: The file sharing settings of the infected file, which are controlled in the application. The settings include:
Private
Internally Shared
Externally Shared
Public
MD5
: The MD5 hash calculated from the file during detection. You can use this hash value to confirm that the file you have downloaded is the same file that was scanned.
Mode
: The type of Netskope policies that detected the infected file.
Inline
: The real-time protection policies detected the file.
Introspection
: The API data protection policies detected the file.
Action
: The action taken on the infected file based on your policy.
#Incidents
: The number of incidents caused by the infected file for inline access mode. Click to see the following information:
Last Seen
: The time the incident occurred with the infected file. For each new incident, Netskope creates a new timestamp and incident ID.
Incident ID
: The unique ID for each time Netskope sees the infected file inline. Click to go to
Skope IT Alerts
and see all the transactions associated with the incident ID and MD5 of the infected file.
Policy Action
: The action taken on the infected file based on your policy.
Note
Incident information is only available for
Inline
mode. For
Introspection
mode, the column always displays zero incidents.
Malware Name
: The name of the detected malware.
Severity
: The severity level Netskope assigned to the malware. The severity categories are:
High
: Viruses
Medium
: Spyware
Low
: Other malware
To learn more:
Malware Severity Levels and Detection Types
.
Detection Engines
: The threat engines that detected the infected file.
Detection Time (GMT)
: The last time Netskope detected the file hash in GMT.
Detection Time
: The last time Netskope detected the file hash in your local time zone.
Sort the table by the above information.
Export all malware incidents (up to 500,000 rows) to a CSV file. All incidents display
Detection
for the
Last_action
column.
Click
to customize table columns or restore the default ones.
Click
to choose one of the following options:
Download
: Click to download the malicious file sample as a password-protected ZIP file. You can go to
Settings
>
Threat Protection
>
API-enabled Protection
to get the ZIP password. This option only applies to API Data Protection (Introspection).
Report False Positive
: Click to do the following.
Report false positive
: Click to report the file to Netskope as a false positive, which opens a Netskope Support case to track the resolution. To use this feature, you must be logged in to your tenant and have an active account on the
Netskope Support Portal
.
Add to file profile
: Click to add the file hash to a
file profile
, which you can use to allow or block the file. Allowlists and blocklists are supported for real-time protection only.
View Alerts
: Click to go to
Skope IT Alerts
and see all the transactions associated with the incident ID and MD5 of the infected file.
Download Retention File
:
Click to download the
retained malicious file sample
as a password-protected ZIP file.
The password is
infected
.
This option only applies to Real-Time Protection (Inline).
View up to 100 malware incidents per page.
View multiple pages of the table.
Viewing Detection Engine Details
In the
Detection Engine
tab, you can:
Refresh the malware incident results.
Filter malware incidents by a specific time frame. You can use a predefined time frame or choose
Date Range
to use the calendar and time menus to customize your own.
Click
+ Add Filter
to filter the malware incidents and narrow your search results. You also can click
to search and filter the malware incidents by a query.
View the primary metrics of the malware incidents:
Users Affected
: The total number of users whose files were affected by the malware.
Malware
: The total number of malware detected by the scan.
Incidents
: The total number of malware incidents detected with Real-Time Protection.
View a list of threat detection engines involved with the malware incidents. For each engine, you can see the following information:
Detection Engine
: The Netskope or integrated partner threat engines that detected the malicious files.
Malware
: The total number of unique malware names detected by the threat engine.
#Users
: The total number of users affected by the malware.
#Files
: The total number of unique file hashes affected by the malware. Click to view the
file details
.
Sort the table by the above information.
Export a list of the detection engine details (up to 500,000 rows) to a CSV file.
View up to 100 affected files per page.
View multiple pages of the table.
Viewing File Details
On the
Malware Details
page, you can click the file name to see an in depth analysis.
On the
File Details
page, you can:
View summarized information on the infected file:
MD5
: The MD5 hash value of the file. You can use it to validate data integrity. Click to copy it to your clipboard.
SHA256
: The SHA-256 hash value of the file. You can use it to find identical files. Click to copy it to your clipboard.
Users Affected
: The total number of users affected by the file.
Threats Detected
: The type of threat detected.
Go to
Skope IT Alerts
and see all the malware detection alerts associated with the MD5 of the infected file.
Look up more malware information on VirusTotal, a third-party aggregator of malware information. VirusTotal is a complementary source of information and might not have details on all malware especially in documents that are private to your organization.
Click to:
Report the file to Netskope as a false positive and open a Netskope Support case to track the resolution.
Add the file hash to a
file profile
that allows or blocks the infected file. You can use this option to add an infected file to an allowlist so it’s exempted from the analytics engine.
Export the infected file details as a STIX report (.json) or PCAP file (.pcap).
View Netskope AV signature matching for the infected file.
View detections from Netskope Threat Intelligence. Netskope’s curated threat intelligence includes indicators of compromise (IOCs) gleaned from detections discovered by advanced scanning engines in the Netskope cloud.
View
advanced heuristics analysis
for the infected file.
View
cloud sandbox analysis
for the infected file.
View file analysis from an integrated third-party threat detection engine, such as Palo Alto Networks Wildfire, Juniper SkyATP, and Check Point SandBlast. To learn more:
Advanced Threat Protection
. Click
Download Analysis Result
to download the results as a PDF file.
In this Topic
Malware

---
## Secureworks Taegis Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/secureworks-taegis-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T22:57:55+00:00
**Scraped:** 2026-08-11T07:30:47.797385+00:00

Secureworks Taegis Plugin for Threat Exchange - Netskope Technical Documentation
Secureworks Taegis Plugin for Threat Exchange
This document explains how to configure the v1.0.0 Secureworks Taegis plugin for the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches Domains and IP Addresses. This plugin does not support sharing of indicators to the Secureworks Taegis platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing. Refer to
URL Lists
for more information.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to Secureworks Taegis (https://
<secureworks taegis>
)
Secureworks Taegis Plugin Support
This plugin fetches Domains and IP Addresses. This plugin does not support sharing of indicators to the Secureworks Taegis platform.
Fetched indicator types
Domains, IP Address
Shared indicator types
Not Supported
Mappings
Pull Mapping
Netskope CE Fields
Secureworks Taegis Fields
Value
HostAddress
Type
IP or Domain
firstSeen
MemberSince
Tags
WatchList (IoC type in Secureworks)
Comments
ReasonAdded
Tags Mapping
Netskope CE Tags
Secureworks Taegis Tags
CTU Botnet Indicators IP
CTU Botnet Indicators IP List – MSS
CTU Threat Group Indicators IP
CTU Threat Group Indicators IP List – MSS
Third Party Threat Group Indicators IP
Third Party Threat Group Indicators IP List – MSS
CTU Botnet Indicators Domain
CTU Botnet Indicators Domain List – MSS
CTU Threat Group Indicators Domain
CTU Threat Group Indicators Domain List – MSS
Third Party Threat Group Indicators Domain
Third Party Threat Group Indicators Domain List – MSS
Permissions
You will need the admin account access in order to generate the required credentials for the plugin.
API Details
List of APIs used
API Endpoint
Method
Use Case
/auth/api/v2/auth/token
POST
Get OAuth2 token
/intel-requester/ti-list/latest
GET
Get threat indicator lists
Get OAuth2 token
API Endpoint:
<BASE_URL>
/auth/api/v2/auth/token
Method:
POST
Headers
Key
Value
Authorization
Basic {$CLIENT_ID:$CLIENT_SECRET}
Body:
{
     "grant_type": "client_credentials"
}
Sample API Response:
{
    "access_token": "eyJhbGcrruuzwo7-....",
    "expires_in": 36000,
    "expiry": "2024-07-19T19:09:43.000Z",
    "token_type": "Bearer"
}
Get Threat Indicator Lists
API Endpoint:
<BASE_URL>/intel-requester/ti-list/latest
Method:
GET
Headers
Key
Value
Authorization
Bearer ${ACCESS_TOKEN}
Sample API Response:
[
{"link": "https://s3.us-east-2.amazonaws.com/ctpx-prod-threat-intel/scwx-attackerdb/ip/40/attackerdb-ip-third-party-threat-group-indicators-ip-list---mss-rev4207.csv?REDACTED_AUTH",
  "name": "scwx-attackerdb/ip/40/attackerdb-ip-third-party-threat-group-indicators-ip-list---mss-rev4207.csv"},
 {"link": "https://ctpx-prod-threat-intel.s3.us-east-2.amazonaws.com/ctp-attackerdb/ip/38/attackerdb-ip-ctu-threat-group-indicators-ip-list---mss-rev4200.csv?REDACTED_AUTH",
  "name": "ctp-attackerdb/ip/38/attackerdb-ip-ctu-threat-group-indicators-ip-list---mss-rev4200.csv"},
 {"link": "https://s3.us-east-2.amazonaws.com/ctpx-prod-threat-intel/scwx-attackerdb/ip/42/attackerdb-ip-ctu-botnet-indicators-ip-list---mss-rev4207.csv?REDACTED_AUTH",
  "name": "scwx-attackerdb/ip/42/attackerdb-ip-ctu-botnet-indicators-ip-list---mss-rev4207.csv"},
 {"link": "https://s3.us-east-2.amazonaws.com/ctpx-prod-threat-intel/scwx-attackerdb/domainname/43/attackerdb-domainname-ctu-threat-group-indicators-domain-list---mss-rev4184.csv?REDACTED_AUTH",
  "name": "scwx-attackerdb/domainname/43/attackerdb-domainname-ctu-threat-group-indicators-domain-list---mss-rev4184.csv"},
 {"link": "https://s3.us-east-2.amazonaws.com/ctpx-prod-threat-intel/scwx-attackerdb/domainname/45/attackerdb-domainname-third-party-threat-group-indicators-domain-list---mss-rev4207.csv?REDACTED_AUTH",
  "name": "scwx-attackerdb/domainname/45/attackerdb-domainname-third-party-threat-group-indicators-domain-list---mss-rev4207.csv"},
 {"link": "https://s3.us-east-2.amazonaws.com/ctpx-prod-threat-intel/scwx-attackerdb/domainname/47/attackerdb-domainname-ctu-botnet-indicators-domain-list---mss-rev4207.csv?REDACTED_AUTH",
  "name": "scwx-attackerdb/domainname/47/attackerdb-domainname-ctu-botnet-indicators-domain-list---mss-rev4207.csv"}
 ]
Performance Matrix
This reading is conducted on a Large CE Stack with below mentioned specs by pulling and pushing 100K IoCs.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Secureworks Taegis
~25K per minute
Indicators shared with Secureworks Taegis
Not Supported
User Agent
netskope-ce-5.0.1-cte-secureworks-taegis-v1.0.0
Workflow
Get your Tenant ID.
Generate an Access Token.
Get your Client ID and Client Secret.
Configure the Secureworks Taegis plugin.
Validate the Secureworks Taegis plugin.
Click play to watch a video.
Get your Secureworks Taegis Credentials
Use the steps provided in the Secureworks Taegis documentation in order to generate the Client ID and Secret.
https://docs.ctpx.secureworks.com/apis/api_authenticate/#part-1-create-client-credentials
Or use the steps in the following sections.
Get your Tenant ID
To get your tenant ID, log in to Taegis XDR, go to
Tenant Settings
from the left-hand panel, and select
Subscriptions
.
Save the Tenant ID to use it to get your Client ID and Secret.
Generate the Access Token
Log in to XDR in Chrome.
Open the Chrome Developer Tools (Right click on your Secureworks Taegis Subscription page, and go to
Inspect > Console
).
Enter “
copy(localStorage.access_token)
” in your Console. The access token will be copied in your clipboard.
Note:
The access token token is not displayed in the Chrome Developer Tools Console, it is only copied to your clipboard. The command returns undefined.
Get your Client ID and Client Secret
In a command line terminal, run the following commands to create your client credentials. Paste the
access_token
from your clipboard into the commands in place of
your_access_token
. Also, substitute your
tenant ID
in place of
your_tenant_id
and enter a unique name to identify your application in place of
your_unique_application_name
.
Your new client credentials are returned in the response. Save the
client_id
and
client_secret
values from this response.
Credentials for Linux:
export ACCESS_TOKEN="your_access_token"
export TENANT_ID="your_tenant_id"
curl -g \
-H "Authorization: Bearer $ACCESS_TOKEN" \
-H "X-Tenant-Context: $TENANT_ID" \
-H "Content-type: application/json" \
-X POST \
-d '{"query": "mutation createClient($name: String!, $roles: [ID!]) { createClient(name: $name, roles: $roles) { client { id name client_id roles role_assignments { id tenant_id role_id role_name expires_at } tenant_id created_at updated_at created_by updated_by environment } client_secret } }", "variables": {"name": "your_awesome_app_name"}}' \
https://api.ctpx.secureworks.com/graphql
Credentials for Windows:
set ACCESS_TOKEN=your_access_token
set TENANT_ID=your_tenant_id
curl -H "Authorization: Bearer %ACCESS_TOKEN%" -H "X-Tenant-Context: %TENANT_ID%" -H "Content-type: application/json" https://api.ctpx.secureworks.com/graphql -d "{\"query\": \"mutation createClient($name: String!, $roles: [ID!]) { createClient(name: $name, roles: $roles) { client { id name client_id roles role_assignments { id tenant_id role_id role_name expires_at } tenant_id created_at updated_at created_by updated_by environment } client_secret } }\", \"variables\": {\"name\": \"your_awesome_app_name\"}}"
You should get something similar to the following:
{
  "data": {
    "createClient": {
      "client": {
        "client_id": "<YOUR_CLIENT_ID>",
        "created_at": "2023-03-03T20:58:40.24986Z",
        "created_by": "0000",
        "environment": "production",
        "id": "<UUID>",
        "name": "your_awesome_app_name",
        "role_assignments": [
          {
            "expires_at": null,
            "id": "<UUID>",
            "role_id": "a4903f9f-465b-478f-a24e-82fa2e129d2e",
            "role_name": "TenantAnalyst",
            "tenant_id": "50530"
          }
        ],
        "roles": "tenantAnalyst",
        "tenant_id": "<TENANT_ID>",
        "updated_at": "2023-03-03T20:58:40.24986Z",
        "updated_by": "0000"
      },
      "client_secret": "<YOUR_CLIENT_SECRET>"
    }
  }
}
Configure the Secureworks Taegis Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the
Secureworks Taegis
plugin box to configure the plugin.
Enter the Basic Information:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave the default.
Aging Criteria: Expiry time of the plugin in days (default: 90).
Override Reputation: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter the Configuration Parameters:
Base URL: The Base URL of your instance.
Client ID: The Client ID generated in Secureworks Taegis.
Client Secret: The Client Secret generated in Secureworks Taegis.
Type of Threat Data to pull: Select the type of Threat Data to pull from Domains and IP Address, based on your requirement.
Enable Tagging: Keep Yes if you want to pull tags along with the indicators. Otherwise, select No.
Click
Save
.
Add a Business Rule
Not Supported.
Add Sharing
Not Supported
Validate the Secureworks Taegis Plugin
Validate the Pull
To verify the pulling of IoCs from Secureworks platform, go to
Logging
and search for Logs pulled from the Secureworks plugin.
The pulled IoCs will be stored in Cloud Exchange on the Threat IoCs page. You can filter the IoCs based on its type or plugin name.
Example:
sources.source like
CTE Secureworks Taegis
&& type IN (
ipv4
,
domain
).
Validate the Push
Push is not supported for the Secureworks Taegis plugin. If you want to push IoCs pulled from Secureworks Taegis to Netskope, refer to the
Threat Exchange plugin guide
.
Troubleshooting
Receiving error while pulling IOCs or configuring the plugin
If you are receiving any of the below errors in logs while configuring the plugin, or when data is being pulled from the platform, it might be due to your plugin configuration parameter being expired.
CTE Secureworks Taegis: Validation error occurred. Error: Received exit code 401, Unauthorized, Verify Client ID and Client Secret provided in the configuration parameters.
CTE Secureworks Taegis [CTE Secureworks Taegis]: Received exit code 401, Unauthorized access while getting auth token.
What to do:
Follow the steps for generating the plugin credentials and use it for your plugin.
Known Behavior
We cannot see the IoCs that are pulled on the platform.
In this Topic
Secureworks Taegis Plugin for Threat Exchange

---
## Web Page IoC Scraper Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/web-page-ioc-scraper-plugin-for-threat-exchange/
**Last Modified:** 2026-07-20T19:16:10+00:00
**Scraped:** 2026-08-11T07:30:49.032144+00:00

Web Page IoC Scraper Plugin for Threat Exchange - Netskope Technical Documentation
Web Page IoC Scraper Plugin for Threat Exchange
Release Notes
2.0.0
Added
Added support for File Type (JSON, XML, HTML, Plain Text).
Added support for IoC Retraction.
1.2.0
Fixed
The pull functionality now includes an option to choose whether to extract only the domain name or use the full URL. For example, if the URL is
google.com/abc/xyz
, selecting
Yes
will extract only the domain google.com, while selecting
No
will retain the full URL
google.com/abc/xyz
. This setting is applicable only when the indicator type
URL
is selected in the Type of Threat Data to Pull configuration parameter.
1.1.1
Fixed
Fixed Bugs in Pull Functionality.
1.1.0
Changed
Renamed the plugin from
External Website
to
Web Page IOC Scraper.
Added
Added support to bifurcate the URL by types (Domain, IPv4, IPv6) starting from CE v5.0.1.
1.0.0
Added
Initial release.
This document explains how to configure the Web Page IoC Scraper v2.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin pulls IoCs of type URL, Domain, IPv4, IPv6, MD5 and SHA256 from any public website. This plugin does not support sharing of IoCs or performing any actions.
Note that this plugin was previously named
External Website
; it has been renamed to
Web Page IoC Scraper
.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope Tenant
A publicly accessible URL serving an IoC feed in plain text, JSON, XML, or HTML format.
Connectivity to your Web Page IoC Scraper
Web Page IoC Scraper Plugin Support
This plugin pulls IoCs of type URL, Domain, IPv4, IPv6, MD5 and SHA256 from any public website. This plugin does not support sharing of IoCs or performing any actions.
Fetched Indicator Types
Shared Indicator Types
URL, IPv4, IPv6, Domains, SHA256, MD5
Not Supported
IoC Retraction
The plugin supports IoC retraction by refetching the feed and identifying indicators no longer present, signalling CE to retract them from its threat intelligence store.
Type
Description
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
For retraction to work, IoC(s) Retraction toggle must be enabled under Settings > Threat Exchange.
API Details
List of APIs Used
API Endpoint
Method
Use Case
https://bitbucket.org/abcd/netskope_ce_abcd/raw/0ee77838f1e1b0491c13e*********/ios.txt
GET
Fetch the IoC feed payload
Fetch IoC Feed
Endpoint:
https://bitbucket.org/abcd/netskope_ce_abcd/raw/0ee77838f1e1b0491c13e*********/ios.txt
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0-cte-web-page-ioc-scraper-v2.0.0
Sample Response
HTTP/1.1 200 OK
Content-Type: text/plain
185.220.101.1
malware.example.com
44d88612fea8a8f36de82e1278abb02f
Performance Matrix
Here is the performance reading conducted after pulling 100K IoCs on a Large CE instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Web Page IoC Scraper
~55k per minute
User Agent
netskope-ce-6.1.0-cte-web-page-ioc-scraper-v2.0.0
Workflow
Configure the Web Page IoC Scraper Plugin.
Configure a Business Rule for Web Page IoC Scraper.
Configure Sharing for Web Page IoC Scraper.
Validate the Web Page IOC Scraper plugin.
Watch a Video
Click play to watch a video.
Configure the Web Page IoC Scraper Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Web Page IoC Scraper v2.0.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Plugin configuration name.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources.
Aging Criteria:
Expire indicators after specific time.
Override Reputation
: Set value to override reputation of indicators received from this configuration. Leave empty to keep default.
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameters determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation
: Enable SSL certificate verification.
Click
Next
and enter the Configuration Parameters:
Website URL:
Add URL of public website from where you want to pull data.
Type of Threat data to pull:
Type of Threat data to pull. Allowed values are SHA256, MD5, URL, Domain, IPv4, IPv6.
File Type:
Expected response format (Plain Text, JSON, XML, HTML).
Extract Domains from URL:
Choose whether to extract only the domain name or use the entire URL. For example, if the URL is
google.com/abc/xyz
, selecting
Yes
will extract google.com, while selecting
No
will use the full URL
google.com/abc/xyz
. Note that this setting is applicable only when the indicator type
URL
is selected in the Type of Threat Data to Pull configuration parameter.
Note
This setting is applicable only when the indicator type
URL
is selected in the Type of Threat Data to Pull configuration parameter.
The Extract Domains from URL parameter will work as follow in below scenarios: (Here the assumption is that only URL type of data is available to fetch)
Only URL Selected
.
Extract Domains from URL
Fetched IOC Type
Yes
extracted domain
No
URL (raw data)
Only Domain Selected
Extract Domains from URL
Fetched IOC Type
Yes
extracted domain
No
extracted domain
Both Selected
Extract Domains from URL
Fetched IOC Type
Yes
extracted domain
No
URL, extracted domain
Click
Save
.
Configure a Threat Exchange Business Rule for Web Page IoC Scraper
To share indicators fetched from the Web Page IoC Scraper to Cloud Exchange, you need a business rule that will filter out the indicators that you want to share.
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirements in the rule, and then click
Save
.
Configure Threat Exchange Sharing for Web Page IoC Scraper
To share IoCs from the Web Page IoC Scraper plugin to Cloud Exchange:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Web Page IoC Scraper), Business Rule, Destination Configuration (CTE Netskope), and a Target.
Click
Save
.
Note
Sharing of IoCs with the Web Page IoC Scraper plugin is not supported. To push IoCs from the Web Page IoC Scraper to Netskope, or to see IoC retraction workflow, refer to the
Threat Exchange plugin guide
.
Because the plugin can pull IoCs of type URL, Domain, IPv4, IPv6, MD5 and SHA256 from any public website, we can perform Add to URL list, Add to File Hash list, Add to Private App, Add to Destination Profile and Add to DNS Profile on the Netskope tenant.
Validate the Web Page IoC Scraper Plugin
Validate the Pull
You can verify the pulling of IoCs from the plugin by going to
Logging
and checking the pulled logs from the CTE Web Page IoC Scraper plugin.
You can add a filter like
message Like “CTE Web Page IOC Scraper”
You can check the pulled data stored in Cloud Exchange under
Threat Exchange > Threat IOCs
. Search the IoCs pulled from the plugin.
Note
Because the plugin is configured with keeping Extract Domains from the URL field as
Yes
, the URLs available on the website were converted into domains.
For example, if you have a URL (https://example.com/path) on your website, here are the possible scenarios:
If you keep
Yes
in the Extract Domains from the URL field, only one IoC will be stored in CE (example.com) and it will be stored as domain type.
If you keep
No
in the Extract Domains from the URL field, two IoCs will be stored in CE (https://example.com/path as URL and example.com as domain).
If you keep the Extract Domains from the URL field as
No
, then it will store the URL in raw format and in domain as well. (For example, 192.168.1.1 is an extracted domain from http://192.168.1.1/dashboard URL.)
Validate the Pull Retraction
The pull retraction for the plugin is done based on the indicators available on the website provided in the plugin configuration and filter provided in the business rule parameters. If any indicator is removed from the website, it will be marked as retracted in Cloud Exchange. Or if you have removed some value from Type of Threat data to pull, it will be marked as retracted.
You can filter the logs related to retraction by using the filter:
sources.source Like “[Retraction]”
You can validate the retracted IoCs on the
Threat IoCs
page:
Note
When IoCs pulled from Web Page IoC Scraper are marked as retracted
yes
, then it will be marked as
<plugin-config-name>: retracted
in the Retraction Result if that IoC was already shared to the Netskope tenant or a 3rd-party platform, and that destination plugin supports push retraction.
Validate the Push Retraction
Push Retraction is not supported for Web Page IoC Scraper. To push IoCs from Web Page IoC Scraper to Netskope, or to see IoC retraction workflow, refer to the
Threat Exchange plugin guide
.
IoCs pulled from Web Page IoC Scraper were shared to a Destination Profile
CTE Demo
on the Netskope tenant.
If any of the shared IoCs are marked as retracted in Cloud Exchange, it would be deleted from the Netskope tenant as well then retraction result will be marked as
“CTE Netskope Threat Exchange: retracted”
.
You can see the IoCs that were marked Retracted
Yes
in the retraction screenshot. These were also deleted from the Destination Profile on the Netskope tenant.
Troubleshooting the Web Page IOC Scraper Plugin
Unable to pull data from the plugin
If you are not able to pull IoCs from the platform, it might be due to one of these reasons:
The Website URL is not public.
Available IoCs to pull are invalid or not supported.
What to do:
Check the website URL. It should be publicly accessible in order to pull IoCs. If that is the case, check the data available to pull. The IoCs supported for pulling should be of type SHA256, MD5, URL, Domain, IPv4, IPv6, and valid.
Not able to pull IoCs of type IPv4, IPv6, and Domains after plugin update on Cloud Exchange versions below 5.0.1
If you are no longer able to pull the above mentioned IoC types, it can be due to the URL bifurcation added in the plugin from CE version 5.0.1.
What to do:
If you have updated your plugin on CE versions below 5.0.1, you might need to manually edit the plugin and select the IPv4, IPv6 and Domain, types of IoCs in the Type of Threat data to pull dropdown list. Previously, the plugin only supported the IoC types MD5, SHA256 and URL, where the URL itself included the subtypes. And new IoC type filters were added in the new plugin version, so they would not be selected in the existing configured plugin.
Note
The IoCs of types IPv4, IPv6, and Domains will still be listed as type
URL
if the CE version is below 5.0.1 even though the latest plugin is configured. Since the support for URL bifurcation is available only from CE version 5.0.1.
Not able to pull IoCs of type URLs
If you are not able to pull IoCs of type URL, it can be due to one of these reasons:
There are no available URLs on the website provided.
Extract Domains from URL is set to
Yes
and the URLs available on the website are extracted to domains.
What to do:
Verify you have available URLs to fetch from the website provided.
Verify that the configured plugin has Extract Domains from URL is set to
Yes
, and if you want to fetch URLs, you can set it to
No
. For more such scenarios, refer to
Web Page IoC Scraper plugin configuration
section.
In this Topic
Web Page IoC Scraper Plugin for Threat Exchange

---
## Rubrik Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/rubrik-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:48:06+00:00
**Scraped:** 2026-08-11T07:30:59.896502+00:00

Rubrik Plugin for Threat Exchange - Netskope Technical Documentation
Rubrik Plugin for Threat Exchange
This document explains how to configure the v1.0.0 Rubrik plugin with the Threat Exchange module of the Cloud Exchange platform. This plugin supports sharing the threat IoCs of type MD5 and SHA256 to the Rubrik’s Threat Hunt page, and can perform a
Start Threat Hunt
action.
Prerequisites
To complete the plugin configuration, you’ll need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to your Rubrik Security Cloud instance (for example:
<customername>.
my.rubrik.com).
Rubrik Plugin Support
The plugin supports pushing SHA256, and MD5 to Rubrik. The plugin also supports performing the
Start Threat Hunt
action on the Shared IoCs.
Fetched indicator types
Not Supported
Shared indicator types
SHA256, MD5
API Details
List of APIs used
Use Case
Method
Endpoint
API Scope
Get auth token
POST
/api/client_token
None
Get objectFids from Rubrik platform
POST
/api/graphql
Threat Hunt (Read)
Get the clusters present on Rubrik
POST
/api/graphql
Threat Hunt
(Read)
Start Threat Hunt on Rubrik
POST
/api/graphql
Threat Hunt (Read)
Get Auth Token
API Endpoint:
/api/client_token
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cte-rubrik-v1.0.0
Payload
Parameter
Value
client_id
<Client ID>
client_secret
<Client Secret>
Sample API Response
{
    "access_token": "",
    "expires_in": 43200,
    "Client_id" : “”
}
API for Start Threat Hunt Action
Get ObjectFids from Rubrik
API Endpoint:
/api/graphql
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cte-rubrik-v1.0.0
Authorization
Bearer <Bearer Token>
Content-Type
application/json
Payload
GraphQL Query
Variables
query SnappableQuery($first: Int, $after: String, $typeFilter: [HierarchyObjectTypeEnum!], $filter: [Filter!], $sortBy: HierarchySortByField, $sortOrder: SortOrder) {
  inventoryRoot {
    descendantConnection(first: $first, after: $after, typeFilter: $typeFilter, filter: $filter, sortBy: $sortBy, sortOrder: $sortOrder) {
      edges {
        cursor
        node {
          id
          ... on WindowsFileset {
            isPassThrough
            __typename
          }
          ... on ShareFileset {
            isPassThrough
            __typename
          }
          ... on LinuxFileset {
            isPassThrough
            __typename
          }
          ... on O365Onedrive {
            userPrincipalName
            __typename
          }
          ...EffectiveSlaColumnFragment
          ...HierarchyObjectClusterColumnFragment
          ...HierarchyObjectLocationColumnFragment
          ...HierarchyObjectNameColumnFragment
          ...HierarchyObjectTypeFragment
          ... on AzureNativeVirtualMachine {
            region
            isAdeEnabled
            resourceGroup {
              subscription {
                name
                __typename
              }
              __typename
            }
            effectiveSlaDomain {
              ...ArchivalSpecFragment
              __typename
            }
            __typename
          }
          ... on AzureNativeManagedDisk {
            region
            isAdeEnabled
            resourceGroup {
              subscription {
                name
                __typename
              }
              __typename
            }
            effectiveSlaDomain {
              ...ArchivalSpecFragment
              __typename
            }
            __typename
          }
          ... on CloudDirectNasExport {
            exportPath
            __typename
          }
          __typename
        }
        __typename
      }
      pageInfo {
        endCursor
        hasNextPage
        hasPreviousPage
        __typename
      }
      __typename
    }
    __typename
  }
}
fragment EffectiveSlaColumnFragment on HierarchyObject {
  id
  effectiveSlaDomain {
    ...EffectiveSlaDomainFragment
    ... on GlobalSlaReply {
      description
      __typename
    }
    __typename
  }
  ... on CdmHierarchyObject {
    pendingSla {
      ...SLADomainFragment
      __typename
    }
    __typename
  }
  __typename
}
fragment EffectiveSlaDomainFragment on SlaDomain {
  id
  name
  ... on GlobalSlaReply {
    isRetentionLockedSla
    retentionLockMode
    __typename
  }
  ... on ClusterSlaDomain {
    fid
    cluster {
      id
      name
      __typename
    }
    isRetentionLockedSla
    retentionLockMode
    __typename
  }
  __typename
}
fragment SLADomainFragment on SlaDomain {
  id
  name
  ... on ClusterSlaDomain {
    fid
    cluster {
      id
      name
      __typename
    }
    __typename
  }
  __typename
}
fragment HierarchyObjectClusterColumnFragment on HierarchyObject {
  ...CdmClusterLabelFragment
  ... on CloudDirectHierarchyObject {
    cluster {
      id
      name
      __typename
    }
    __typename
  }
  __typename
}
fragment CdmClusterLabelFragment on CdmHierarchyObject {
  cluster {
    id
    name
    version
    __typename
  }
  primaryClusterLocation {
    id
    __typename
  }
  __typename
}
fragment HierarchyObjectLocationColumnFragment on HierarchyObject {
  logicalPath {
    name
    objectType
    __typename
  }
  physicalPath {
    name
    objectType
    __typename
  }
  __typename
}
fragment HierarchyObjectNameColumnFragment on HierarchyObject {
  name
  __typename
}
fragment HierarchyObjectTypeFragment on HierarchyObject {
  objectType
  __typename
}
fragment ArchivalSpecFragment on GlobalSlaReply {
  archivalSpec {
    storageSetting {
      targetType
      __typename
    }
    __typename
  }
  archivalSpecs {
    storageSetting {
      targetType
      __typename
    }
    __typename
  }
  __typename
}
{
  "first": 1,
  "filter": [
    {
      "texts": [
        "false"
      ],
      "field": "IS_GHOST"
    },
    {
      "texts": [
        “”
      ],
      "field": "CLUSTER_ID"
    }
  ],
  "sortBy": "NAME",
  "sortOrder": "ASC",
  "typeFilter": [
    "LinuxFileset",
    "ShareFileset",
    "VmwareVirtualMachine",
    "WindowsFileset",
    "HypervVirtualMachine",
    "NutanixVirtualMachine",
    "NAS_FILESET"
  ],
  "after":"Y3Vyc29yOmludDow"
}
Sample API Response
{
    "data": {
        "inventoryRoot": {
            "descendantConnection": {
                "edges": [
                    {
                        "cursor": "Y3Vyc29yOmludDox",
                        "node": {
                            "id": "",
                            "effectiveSlaDomain": {
                                "id": "",
                                "name": "MGMT-12H-30D-1Y-AWS-USW1",
                                "isRetentionLockedSla": false,
                                "retentionLockMode": "NO_MODE",
                                "__typename": "GlobalSlaReply",
                                "description": "Upgraded from Cluster_A"
                            },
                            "pendingSla": null,
                            "__typename": "NasFileset",
                            "cluster": {
                                "id": "",
                                "name": "Cluster_A",
                                "version": "8.1.3-p11-25483",
                                "__typename": "Cluster"
                            },
                            "primaryClusterLocation": {
                                "id": "",
                                "__typename": "DataLocation"
                            },
                            "logicalPath": [
                                {
                                    "name": "/volume1/ISO: **",
                                    "objectType": "FilesetTemplate",
                                    "__typename": "PathNode"
                                },
                                {
                                    "name": "/volume1/ISO",
                                    "objectType": "NasShare",
                                    "__typename": "PathNode"
                                },
                                {
                                    "name": "domain.com",
                                    "objectType": "NasSystem",
                                    "__typename": "PathNode"
                                }
                            ],
                            "physicalPath": [
                                {
                                    "name": "/volume1/ISO: **",
                                    "objectType": "FilesetTemplate",
                                    "__typename": "PathNode"
                                },
                                {
                                    "name": "/volume1/ISO",
                                    "objectType": "NasShare",
                                    "__typename": "PathNode"
                                },
                                {
                                    "name": "domain.com",
                                    "objectType": "NasSystem",
                                    "__typename": "PathNode"
                                }
                            ],
                            "name": "/volume1/ISO: **",
                            "objectType": "NAS_FILESET"
                        },
                        "__typename": "HierarchyObjectEdge"
                    }
                ],
                "pageInfo": {
                    "endCursor": "Y3Vyc29yOmludDox",
                    "hasNextPage": true,
                    "hasPreviousPage": true,
                    "__typename": "PageInfo"
                },
                "__typename": "HierarchyObjectConnection"
            },
            "__typename": "InventoryRoot"
        }
    }
}
Get Clusters Present on Rubrik
API Endpoint:
/api/graphql
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cte-rubrik-v1.0.0
Authorization
Bearer <Bearer Token>
Content-Type
application/json
Payload
GraphQL Query
Variables
query ClusterPickerQuery($first: Int, $after: String, $filter: ClusterFilterInput, $sortBy: ClusterSortByEnum, $sortOrder: SortOrder) {
  clusterConnection(filter: $filter, sortBy: $sortBy, sortOrder: $sortOrder, first: $first, after: $after) {
    edges {
      cursor
      node {
        id
        status
        ...ClusterIconNameFragment
        ...ClusterVersionColumnFragment
        ...ClusterTypeColumnFragment
        ...ClusterCapacityColumnFragment
        ...ClusterProtectedCountColumnFragment
        ...ClusterGeoLocationColumnFragment
        ...ClusterNameColumnFragment
        __typename
      }
      __typename
    }
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
      __typename
    }
    __typename
  }
}
fragment ClusterIconNameFragment on Cluster {
  id
  name
  status
  pauseStatus
  state {
    clusterRemovalState
    __typename
  }
  defaultAddress
  passesConnectivityCheck
  connectivityLastUpdated
  ...ClusterNodeConnectionFragment
  globalManagerConnectivityStatus {
    urls {
      url
      isReachable
      __typename
    }
    __typename
  }
  systemStatus
  ccprovisionInfo {
    jobStatus
    jobType
    progress
    vendor
    __typename
  }
  __typename
}
fragment ClusterNodeConnectionFragment on Cluster {
  clusterNodeConnection {
    nodes {
      id
      status
      ipAddress
      __typename
    }
    __typename
  }
  __typename
}
fragment ClusterVersionColumnFragment on Cluster {
  version
  eosDate
  eosStatus
  __typename
}
fragment ClusterTypeColumnFragment on Cluster {
  name
  productType
  type
  clusterNodeConnection {
    nodes {
      id
      __typename
    }
    __typename
  }
  __typename
}
fragment ClusterCapacityColumnFragment on Cluster {
  metric {
    usedCapacity
    availableCapacity
    totalCapacity
    __typename
  }
  __typename
}
fragment ClusterProtectedCountColumnFragment on Cluster {
  productType
  noSqlWorkloadCount
  ...ClusterProtectedSnappablesFragment
  __typename
}
fragment ClusterProtectedSnappablesFragment on Cluster {
  protectedSnappables: snappableConnection(filter: {protectionStatus: Protected}) {
    count
    __typename
  }
  __typename
}
fragment ClusterGeoLocationColumnFragment on Cluster {
  geoLocation {
    address
    __typename
  }
  __typename
}
fragment ClusterNameColumnFragment on Cluster {
  name
  __typename
}
{
  "sortBy": "ClusterName",
  "sortOrder": "ASC",
  "filter": {
    "type": [],
    "name": [
      ""
    ]
  },
  "first": 1
}
Sample API Response
{
    "data": {
        "clusterConnection": {
            "edges": [
                {
                    "cursor": "Y3Vyc29yOmludDow",
                    "node": {
                        "id": "40fdb2a5-3591-40ee-a37a-50bce5240d62",
                        "status": "Connected",
                        "name": "Cluster_A",
                        "pauseStatus": "NOT_PAUSED",
                        "state": {
                            "clusterRemovalState": "REGISTERED",
                            "__typename": "clusterState"
                        },
                        "defaultAddress": "cluster-a.domain.com",
                        "passesConnectivityCheck": true,
                        "connectivityLastUpdated": "2024-08-05T10:16:10.000Z",
                        "clusterNodeConnection": {
                            "nodes": [
                                {
                                    "id": "RVMHM223S002373",
                                    "status": "OK",
                                    "ipAddress": "10.8.107.107",
                                    "__typename": "ClusterNode"
                                },
                                {
                                    "id": "RVMHM223S002379",
                                    "status": "OK",
                                    "ipAddress": "10.8.107.106",
                                    "__typename": "ClusterNode"
                                },
                                {
                                    "id": "RVMHM223S002714",
                                    "status": "OK",
                                    "ipAddress": "10.8.107.104",
                                    "__typename": "ClusterNode"
                                },
                                {
                                    "id": "RVMHM223S002718",
                                    "status": "OK",
                                    "ipAddress": "10.8.107.105",
                                    "__typename": "ClusterNode"
                                }
                            ],
                            "__typename": "ClusterNodeConnection"
                        },
                        "__typename": "Cluster",
                        "globalManagerConnectivityStatus": {
                            "urls": [
                                {
                                    "url": "https://mycustomername.my.rubrik.com",
                                    "isReachable": true,
                                    "__typename": "GlobalManagerUrl"
                                }
                            ],
                            "__typename": "GlobalManagerConnectivity"
                        },
                        "systemStatus": "OK",
                        "ccprovisionInfo": {
                            "jobStatus": "INITIALIZING",
                            "jobType": "ADD_NODE",
                            "progress": 0,
                            "vendor": "VENDOR_UNKNOWN",
                            "__typename": "CcprovisionInfo"
                        },
                        "version": "8.1.3-p11-25483",
                        "eosDate": "2024-07-25",
                        "eosStatus": "EOS_STATUS_UNSUPPORTED",
                        "productType": "CDM",
                        "type": "OnPrem",
                        "metric": {
                            "usedCapacity": 7113709735936,
                            "availableCapacity": 54306599845888,
                            "totalCapacity": 61420309581824,
                            "__typename": "ClusterMetric"
                        },
                        "noSqlWorkloadCount": 0,
                        "protectedSnappables": {
                            "count": 148,
                            "__typename": "SnappableConnection"
                        },
                        "geoLocation": {
                            "address": "Santa Clara, CA, USA",
                            "__typename": "GeoLocation"
                        }
                    },
                    "__typename": "ClusterEdge"
                }
            ],
            "pageInfo": {
                "startCursor": "Y3Vyc29yOmludDow",
                "endCursor": "Y3Vyc29yOmludDow",
                "hasNextPage": true,
                "hasPreviousPage": false,
                "__typename": "PageInfo"
            },
            "__typename": "ClusterConnection"
        }
    }
}
Start Threat Hunt on Rubrik
API Endpoint:
/api/graphql
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.0.1-cte-rubrik-v1.0.0
Authorization
Bearer <Bearer Token>
Content-Type
application/json
Payload
GraphQL Query
Variables
mutation StartThreatHuntMutation($input: StartThreatHuntInput!) 
{   
  startThreatHunt(input: $input)        
       {
          huntId    isSyncSuccessful __typename 
       } 
}
{
    "input": {
    "clusterUuid": "40fdb2a5-3591-40ee-a37a-50bce5240d62",
    "indicatorsOfCompromise": [
      {
        "iocKind": "IOC_HASH",
        "iocValue": "sha256:a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
      },
      {
        "iocKind": "IOC_HASH",
        "iocValue": "sha256:a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146f"
      }
    ],
    "objectFids": [
      “”
    ],
    "fileScanCriteria": {
      "fileSizeLimits": {
        "maximumSizeInBytes": 1024,
        "minimumSizeInBytes": 5
      },
      "pathFilter": {
        "includes": [
          "*.acm",
          "*.ax",
          "*.cpl",
          "*.dll",
          "*.drv",
          "*.efi",
          "*.exe",
          "*.mui",
          "*.ocx",
          "*.scr",
          "*.sys",
          "*.tsp"
        ],
        "excludes": [],
        "exceptions": []
      }
    },
    "maxMatchesPerSnapshot": 1,
    "name": "Sample threat hunt",
    "shouldTrustFilesystemTimeInfo": true,
    "snapshotScanLimit": {
      "maxSnapshotsPerObject": 1
    }
  }
  }
Sample API Response
{
    "data": {
        "startThreatHunt": {
            "huntId": "892caaf9-90d3-5c87-8297-5862e972a032",
            "isSyncSuccessful": true,
            "__typename": "StartThreatHuntReply"
        }
    }
}
Performance Matrix
Here is the performance reading conducted by sharing 100K indicators to Rubrik on a Large CE Stack with these specifications.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Rubrik
NA
Indicators shared with Rubrik
~26K per minute
User Agent
netskope-ce-5.0.1-cte-rubrik-v1.0-0
Workflow
Get your Client ID and Client Secret.
Configure the Rubrik plugin.
Configure a Threat Exchange Business Rule.
Configure Threat Exchange Sharing.
Validate the Rubrik plugin.
Click play to watch a video:
Get your Configuration Parameters
Follow the steps in this document to generate the Client ID and Client Secret:
https://docs.rubrik.com/en-us/saas/saas/adding_a_service_account.html?hl=adding%2Cservice%2Caccount
Configure the Rubrik Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the CTE Rubrik plugin box.
Enter the Basic Information:
Configuration Name: Plugin configuration name
Sync Interval: Interval to fetch data from this plugin source.
Aging Criteria: Expire indicators after a specific time.
Override Reputation: Set value to override reputation of indicators received from this configuration. Leave empty to keep default.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Use system proxy configured in Settings.
Click
Next
.
Enter the Configuration Parameters:
Base URL: Base URL of Rubrik instance, like
https://rubrik01.rubrikdemo.com
.
Client ID: Client ID generated from the Rubrik platform. To obtain the Client ID, a Service Account JSON needs to be generated. In Rubrik, go to
Apps > Settings > Users and Access
to generate it.
Client Secret: Client Secret generated from the Rubrik platform. To obtain the Client Secret, a Service Account JSON needs to be generated. In Rubrik, go to
Apps > Settings > Users
and Access to generate it.
Click
Save
.
Configure a Business Rule for the Rubrik Plugin
A Business Rule is used to filter out the indicators that are to be shared. In order to share IoCs with Rubrik, create a business rule using these steps:
Go to
Threat Exchange > Business Rules
and click
Create New Rule
.
Add the Rule name and select the fields through which you want to filter the IoCs. When finished, click
Save
.
Add Sharing for the Rubrik Plugin
To configure the Sharing, follow these steps:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select a Source configuration (Source from which you want to share data to Rubrik), a Business Rule, and a Destination.
Select the Target value, and enter these values:
Threat Hunt Name: Enter the name of the Threat Hunt. A Threat Hunt with this name will be initiated on Rubrik.
Cluster Name: Rubrik Cluster for which you want to initiate Threat Hunt.
Max File Size to Scan (in KB): Maximum file size in KB to scan. Default is 1024 KB. Maximum supported size is 15000000 KB and minimum supported size is 1 KB.
Min File Size to Scan (in KB): Minimum file size in KB to scan. Default is 5 KB. Maximum supported size is 15000000 KB and minimum supported size is 1 KB.
Max IOC Matches (Per Snapshot): Maximum IOC matches per snapshot. Default is 1. Maximum supported value is 1000 and minimum supported value is 1.
Include Files: Files to include in Threat Hunt.
Exclude Files: Files to exclude from Threat Hunt.
Do not Exclude Files: File which should not be excluded from Threat Hunt.
Click
Save
.
Validate the Rubrik Plugin
Pull is not supported.
Validate the Push
Shared IoCs to Rubrik can be verified from logs available on the
Logging
page of Cloud Exchange.
IoCs shared on Rubrik can be verified at
Apps > Data Threat Analytics > Threat Hunt
. Click on the Threat Hunt that you created.
Click on the Parameters tab to view the shared IoCs.
Troubleshooting
Unable to configure the Rubrik Plugin
If you are unable to configure the Rubrik Plugin, then it could be due to one of the reasons mentioned-below:
Proper permission is not provided to the credentials.
Provided incorrect credentials.
To solve the issues mentioned above, follow these steps:
Check the logs of the plugin in Cloud Exchange.
Make sure that provided credentials have proper permissions.
Make sure that correct credentials are provided while configuring the plugin.
Unable to push data to Rubrik
If you are unable to share the IoCs to the Rubrik Plugin, then it could be due to one of these reasons:
Invalid value of MD5, and SHA256 provided.
If the shared data has type other than MD5, or SHA256.
To solve the issues mentioned above, follow these steps:
Check the logs of the plugin in Cloud Exchange.
Make sure that the MD5, and SHA256 that needs to be shared are valid.
Make sure that the IoCs are of type MD5, or SHA256.
In this Topic
Rubrik Plugin for Threat Exchange

---
## Setting Up an Application Instance for Malware Retention
**URL:** https://docs.netskope.com/en/setting-up-an-application-instance-for-malware-retention/
**Last Modified:** 2025-08-31T01:47:32+00:00
**Scraped:** 2026-08-11T07:31:18.184344+00:00

Setting Up an Application Instance for Malware Retention - Netskope Technical Documentation
Setting Up an Application Instance for Malware Retention
The
Malware Retention page
allows you to set up an application instance to store and retrieve malicious files detected by the Threat Protection policy. Netskope only supports uploading malicious files to Azure Blob Storage instances at this time.
To set up an application instance:
Go to
Settings
>
Threat Protection
>
Malware Retention
.
Click the
Instances
tab.
Click
Setup Instance
and then
Azure Blob Storage
.
In the
Setup Instance – Azure Blob Storage
window, enter the Azure Blob Storage instance name.
Click
Grant Access
.
Sign in to Microsoft to authorize.
If you successfully authorized the instance, you can see
next to the name.
Create and Assign a Custom Role in Azure Portal
Once you have granted access, login to Azure portal, create a custom role, and assign the role to the storage account or container.
A storage account may include multiple containers. Though you can assign the custom role to a storage account, Netskope recommends a least-access strategy, meaning restrict the custom role assignment at a container level.
Log in
portal.azure.com
as an application administrator or a higher role.
Identify the subscription ID where you would like to create a custom role. To do so, navigate to
All services > General > Subscriptions
. Identify the subscription ID and click it.
On the left navigation of the subscription page, click
Access Control (IAM)
. Then, click
+ Add > Add custom role.
The
Create a custom role
page opens.
Under the
Basics
tab, enter a name for the custom role. Keep the rest of the fields unchanged.
Click
Next
.
Under
Permissions
, click
+ Add permissions
. The
Add permissions
page opens. On the search bar, enter the following permissions one after the other:
Microsoft.Storage/storageAccounts/blobServices/containers/read
. Click
Microsoft Storage.
Select
Read : Get blob container
and click
Add
.
Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read
. Click
Microsoft Storage.
Click the
Data Actions
radio button and select
Read : Read Blob
and click
Add
.
Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write
. Click
Microsoft Storage.
Click the
Data Action
s radio button and select
Write: Write Blob
and click
Add
.
Once you have added the 3 permissions, the
Permissions
tab should look like this:
Click
Review + create
. The
Review + create
tab displays the following information. Review it.
Note down the role name. This will be required when you assign the role to a container.
Click
Create
.
You have successfully created the custom role. Next, you should assign the role to a container.
Navigate to
All services > Storage > Storage
accounts
. Identify the storage account and click it.
On the left navigation of the storage account page, click
Data storage > Containers
. Identify the container to which you would like to assign the custom role. Click it.
On the left navigation of the container page, click
Access Control (IAM)
. Then, click
+ Add > Add role assignment.
The
Add role assignment
page opens.
Search by role name, select the role, and click
Next
.
Under
Members
, click
+ Select members
.
Under
Select Members
, type
Netskope – Malware Retention for Azure Storage
. Select the
Netskope – Malware Retention for Azure Storage
app and click
Select
.
Click
Review + assign
. The
Review + assign
tab displays the following information. Review it.
Click
Review + assign.
The role assignment may take a few minutes. Before you proceed to create a malware retention profile in the Netskope UI, give it a few minutes for the role assignment to take effect.
You have successfully assigned the custom role to a container. Next, you must create a malware retention profile. See
Creating a Malware Retention Profile
.
In this Topic
Setting Up an Application Instance for Malware Retention

---
## Creating a Malware Retention Profile
**URL:** https://docs.netskope.com/en/creating-a-malware-retention-profile/
**Last Modified:** 2025-08-31T01:47:32+00:00
**Scraped:** 2026-08-11T07:31:19.392814+00:00

Creating a Malware Retention Profile - Netskope Technical Documentation
Creating a Malware Retention Profile
The
Malware Retention page
allows you to set up an application instance to store and retrieve malicious files detected by the Threat Protection policy. You create a malware retention profile and specify where you want to retain copies of files that were found malicious. You can only assign one profile.
To create a malware retention profile:
Go to
Settings
>
Threat Protection
>
Malware Retention
.
In the
Configuration
tab, click
New Profile
.
In the
New Malware Retention Profile
window:
Profile Name
: Enter a name for the profile.
App
: Netskope only supports Azure Blob Storage at this time.
Instance
: Choose the
configured Azure Blob Storage instance
where you want to store malicious files.
Storage Account
: Enter the storage account for Azure Blob Storage.
Container
: Enter the container for Azure Blob Storage.
File ZIP Password
: The password is
infected
to prevent users from inadvertently opening infected files on their computers.
Click
Save
.
In this Topic
Creating a Malware Retention Profile

---
## Threat Exchange Plugin
**URL:** https://docs.netskope.com/en/threat-exchange-plugin/
**Last Modified:** 2026-06-02T23:42:49+00:00
**Scraped:** 2026-08-11T07:32:15.126280+00:00

Threat Exchange Plugin - Netskope Technical Documentation
Threat Exchange Plugin
Release Notes
2.5.0
Added
Added support for DNS Profile sharing and push retraction. (Min. required CE version: 6.1.0)
Added logic for skipping tags longer than 30 characters for Private App sharing action.
2.4.0
Added
Added support for Destination Profile sharing and delete retraction. (Min. required CE version: 6.1.0)
Added delete retraction for URL List.
Added resolution for error logs.
Changed
Updated URL List sharing to share only modified indicators. (Min. required CE version: 6.1.0)
Updated error log to info log when duplicate file hashes are shared.
Updated sharing behavior irrespective of selected IOC types in configuration.
2.3.0
Added
Added configuration option to enable/disable querying Retrohunt API.
Fixed
Fixed tagging of indicators while sharing.
2.2.0
Added
Added support for retraction of False Positive if IoC type is File Hash. (Min. required CE version: 5.1.0)
Added support for port range in Add to Private App Target.
Added support for severity in URL IoCs.
Changed
Pull only malicious file hash IoCs using Retrohunt.
Updated URL List limit to 7 MB from 8 MB.
2.1.3
Changed
Bug fixes.
2.1.2
Added
Added support to create indicators from SHA256 and MD5 fields, along with Local SHA256 and Local MD5, from malware alerts.
2.1.1
Changed
Updated authentication for V1 token.
2.1.0
Added
Added support for retraction of retracted IoCs. It does not support fetching retracted indicators from the Netskope tenant.
2.0.0
Changed
The Netskope CTE plugin has been restructured and is now available in the Default repository.
1.0.0
Added
Initial release.
This document explains how to configure the Threat Exchange v2.5.0 plugin in the Cloud Exchange platform. This plugin is used to fetch the File hashes (MD5 and SHA256) and URLs (URL, IPv4, hostname, domain, and FQDN) from the Malware and Malsite alerts available on the Netskope Tenant from
Skope IT > Alerts
.
This plugin also supports sharing File Hashes (MD5 and SHA256) and URLs (URL, IPv4, hostname, domain, and FQDN) indicators to File Hash List (
Policies > Profiles > File
), URL List (
Policies > Profiles > URL Lists
), Private App (
Settings > Security Cloud Platform > App Definition > Private App
), Destination Profiles (
Policies > Profiles > Destination
), and DNS Profiles (
Policies > Profiles > DNS
) within Netskope. Consider the maximum size of data that Netskope File Hash List can hold (8 MB), URL List can hold (7 MB), and DNS Profile can hold (16 MB) while configuring the Business Rule.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope Tenant
A Netskope Cloud Exchange tenant with the
Tenant plugin
and a 3rd-party Threat Exchange plugin (like
CrowdStrike
) already configured.
Connectivity to a Netskope tenant with permission to generate tokens.
Need Retrohunt API by File Hash feature enabled in Netskope Tenant
Need Destination Profile feature enabled in Netskope Tenant
Need Netskope SWG License for the Destination Profile
Threat Exchange Plugin Support
This plugin is used to fetch the File hashes (MD5 and SHA256) and URLs (URL, IPv4, hostname, domain, and FQDN) from the Malware and Malsite alerts available on the Netskope Tenant from Skope IT > Alerts. This plugin also supports sharing File Hashes (MD5 and SHA256) and URLs (URL, IPv4, hostname, domain, and FQDN) indicators to File Hash List (
Policies > Profiles > File
), URL List (
Policies > Profiles > URL Lists
), Private App (
Settings > Security Cloud Platform > App Definition > Private App
), Destination Profiles (
Policies > Profiles > Destination
), and DNS Profiles (
Policies > Profiles > DNS
) within Netskope. Consider the maximum size of data that Netskope File Hash List can hold (8 MB), URL List can hold (7 MB), and DNS Profile can hold (16 MB) while configuring the Business Rule.
Fetched Indicator Types (Malware and Malsite alerts)
Shared Indicator Types
SHA256
MD5
Domain
IPv4
Local_MD5
Local_SHA256
URL
SHA256
MD5
Domain
IPv4
URL
IOC Retraction
IOC Retraction (Pull) –
IOCs that are false positive(verdict clean) as per retrohunt (retrohunt/ioc/getinfo) endpoint will be marked as retraced in CE if Enable Retrohunt is set to Yes in the plugin configuration.
When Enable Retrohunt is enabled, the plugin will not store IOCs classified as false positives (verdict: clean). Retraction applies only to IOCs that were previously pulled and stored as malicious, but were later reclassified as false positives (verdict: clean).
IOC Retraction (Push) –
Retracted indicators present on CE will be deleted from Netskope Tenant during sharing.
Retraction Type
Supported Retraction Type
IOC Retraction (Pull)
Yes
IOC Retraction (Push)
Yes
Mappings
Cloud Exchange Fields
Netskope Fields
value
Malware
local_md5, local_sha256, SHA256 and MD5
Malsite
URL
type
Malware
MD5, SHA256
Malsite
URL
comments
Malware
<Tenant URL>
– object
Eg. https://crest-plugin-support.de.goskope.com – , Malware Name: amtest, Malware Type: hash
Malsite
<Tenant URL> – malsite_category
E.g. https://crest-plugin-support.de.goskope.com – Malicious Site, Phish Site, Bot
severity
Malware
retrohunt.severity_updated
or
retrohunt.severity
or
severity
1: low
2: medium
3: high
Malsite
severity
firstseen, lastseen
timestamp
Permissions
Need v2 token created using the Netskope Cloud Exchange Role.
The required permissions (privilege levels) per plugin are available in
REST API scopes
.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/api/v2/events/dataexport/alerts/malware
GET
Pull the Malware alerts from Netskope tenant
/api/v2/events/dataexport/alerts/malsite
GET
Pull the Malsite alerts from Netskope tenant
/api/v1/updateFileHashList
POST
Push the file hashes to Netskope Tenant
/api/v2/policy/urllist
GET
Get URL Lists
/api/v2/policy/urllist
POST
Create URL List
/api/v2/policy/urllist/{}/append
PATCH
Push the URLs to Netskope
/api/v2/policy/urllist/deploy
POST
Deploy changes to Netskope URL List
/api/v2/steering/apps/private
GET
List Private Apps
/api/v2/infrastructure/publishers
GET
List Publishers for Private Apps
/api/v2/steering/apps/private
PATCH
Push Private App to Netskope Tenant
/api/v2/nsiq/retrohunt/ioc/getinfo
POST
Fetch False Positive and Retrohunt Severity
/api/v2/policy/urllist/{}/replace
PATCH
Push the URLs to Netskope for delete retraction
/api/v2/profiles/destinations
GET
Get Destination Profiles
/api/v2/profiles/destinations
POST
Create Destination Profile
/api/v2/profiles/destinations/{}/values
POST
Push or Remove Destination Profile Values
/api/v2/profiles/destinations/deploy
POST
Apply Pending Changes for a  Destination Profile
/api/v2/profiles/dns
GET
Get DNS Profiles
/api/v2/profiles/dns
POST
Create DNS Profile
/api/v2/profiles/dns/{}
PATCH
Update DNS Profile
/api/v2/profiles/dns/domaincategories
GET
Get DNS categories
/api/v2/profiles/dns/recordtypes
GET
Get DNS Record types
Pull the Malware alerts from Netskope tenant
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
<netskope_api_rbac3_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
"ok": 1,
"result": [
{
"TSS-scan": "v2",
"_id": "ca2cd2413493f18eeb65b2",
"access_method": "API Connector",
"acked": "false",
"action": "Detection",
"activity": "Introspection Scan",
"alert": "yes",
"alert_name": "VBA.Heur.EmotetDldr.1.3CBCEF4D.Gen:94075",
"alert_type": "Malware",
"app": "Dropbox",
"app_name": "Dropbox",
"app_session_id": 97439093538764,
"appcategory": "Cloud Storage",
"category": "Cloud Storage",
"cci": 81,
"ccl": "high",
"connection_id": 115689096495576,
"count": 1,
"created_date": 1751544554,
"detection_engine": "Netskope Advanced Heuristic Analysis",
"detection_type": "Virus",
"device": "Other",
"dst_country": "US",
"dst_geoip_src": 2,
"dst_latitude": 37.77,
"dst_location": "San Francisco",
"dst_longitude": -122.4,
"dst_region": "California",
"dst_zipcode": "94107",
"dstip": "162.125.8.18",
"file_id": "id:RqCtsmy9paAAAAAAAAP9LA",
"file_name": "testpdv_5e673d7973900c3c1ed399_66b8e7b2e881b711aca1b98d91d5ce3b_1751544269_office_clafier.doc",
"file_path": "/tss-sanity-1751a0b8/testpdv_5e67ccdec797303d7973900c3c1ed399_66b8e7b2e881b711aca1b98d91d5ce3b_1751544269_office_classifier.doc",
"file_size": 156874,
"file_type": "application/ms-word",
"filename": "testpdv_5e67ccde0c3c1ed399_66b8e7b2e881b711aca1b98d91d5ce3b_1751544269_office_classifier.doc",
"incident_id": 1000362732176413775,
"instance": "TEST Netskope MW 1",
"local_md5": "66e881b711aca1b98d91d5ce3b",
"local_sha256": "6712afc5119e5303a6dedcb4b61cf2f1ee525cd2c9d4da31d21",
"malware_id": "6c2e227369044356354b84add6456611",
"malware_name": "VBA.Heur.EtDldr.1.3CBCEF4D.Gen:94075",
"malware_severity": "high",
"malware_type": "Virus",
"md5": "66b8e7b2e8aca1b98d91d5ce3b",
"mime_type": "application/msword",
"modified_date": 1751544429,
"object": "testpdv_5e973900c3c1ed399_66b8e7b2e881b711aca1b98d91d5ce3b_1751544269_office_classifier.doc",
"object_id": "id:RqCtsmyAAAP9LA",
"object_type": "File",
"organization_unit": "",
"policy": "2214472052546912863",
"request_id": 0,
"scan_time": 1751544554,
"scan_type": "ongoing",
"scanner_result": "malicious",
"severity": "high",
"severity_id": 3,
"sha1": "c66724a30cf9a0e0558ec3028d",
"sha256": "6712afc5119e507259dcb4b61cf2f1ee525cd2c9d4da31d21",
"shared_type": "private",
"site": "Dropbox",
"timestamp": 1751544733,
"title": "testpdv_5e67ccd399_66b8e7b2e881b711aca1b98d91d5ce3b_1751544269_office_classifier.doc",
"traffic_type": "CloudApp",
"transaction_id": 1000362732176413775,
"true_filetype": "None",
"tss_license": "True",
"tss_mode": "introspection",
"type": "nspolicy",
"ur_normalized": "ali+nsmtp@netskope.com",
"url": "https://www.dropbox.com/work/tss-sanity-17515441674e95a0b8?preview=testpdv_5e67ccdec797303d7911aca1b98d91d5ce3b_1751544269_office_classifier.doc",
"user": "alitp@netskope.com",
"user_id": "dbmi1Dimthhx2TJyIhxpudwxGmM",
"record_type": "alert",
"file_category": "",
"usr_title": "",
"src_latitude": 0.0,
"managementID": "",
"userCountry": "",
"department": "",
"browser": "",
"userip": "",
"page": "",
"from_user": "",
"appsuite": "",
"os": "",
"shared_with": [],
"sanctioned_instance": "",
"os_version": "",
"company": "",
"usr_udf_supervisorname": "",
"dst_timezone": "",
"user_confidence_index": 0,
"browser_session_id": 0,
"src_geoip_src": 0,
"usr_udf_companyname": "",
"srcip": "",
"usr_udf_supervisorid": "",
"src_zipcode": "",
"hostname": "",
"manager": "",
"usr_udf_businesssegmentlevel1": "",
"protocol": "",
"usr_udf_businesssegmentlevel3": "",
"custom_attr": {},
"usr_status": "",
"usr_udf_businesssegmentlevel2": "",
"usr_udf_businesssegmentlevel4": "",
"src_country": "",
"parent_id": "",
"src_location": "",
"src_region": "",
"device_classification": "",
"instance_id": "",
"malware_profile": "",
"tss_fail_reason": "",
"browser_version": "",
"usr_udf_primarydomain": "",
"usr_udf_employeeid": "",
"src_timezone": "",
"policy_id": "",
"usr_display_name": "",
"managed_app": "",
"tss_scan_failed": "",
"src_time": "",
"fastscan_results": "",
"referer": "",
"ml_detection": "",
"nsdeviceuid": "",
"userPrincipalName": "",
"src_longitude": 0.0,
"page_site": ""
}
],
"wait_time": 5,
"timestamp_hwm": 1751544743
}
Pull the Malsite alerts from Netskope tenant
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
<netskope_api_rbac3_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
"ok": 1,
"result": [
{
"_id": "96e20f6e73d2867d1865d",
"access_method": "Client",
"acked": "false",
"action": "block",
"alert": "yes",
"alert_name": "ww25.cleansix.xyz",
"alert_type": "malsite",
"app": "",
"app_session_id": 8130338485448244761,
"appcategory": "Security Risk - Cosed/malicious sites",
"browser_session_id": 5158615776615133890,
"category": "Security Risk - Comised/malicious sites",
"cci": 0,
"ccl": "unknown",
"connection_id": 0,
"count": 1,
"device": "Linux Device",
"device_classification": "not configured",
"dst_country": "US",
"dst_latitude": 27.947519302368164,
"dst_location": "Tampa",
"dst_longitude": -82.45842742919922,
"dst_region": "Florida",
"dst_timezone": "America/New_York",
"dst_zipcode": "N/A",
"dstip": "199.59.243.228",
"dstport": 80,
"hostname": "ip-172-31-29-12",
"incident_id": 374545097297887,
"ja3": "NotAvailable",
"ja3s": "NotAvailable",
"malicious": "yes",
"malsite_category": [
"Malicious Site"
],
"malsite_country": "US",
"malsite_id": "94c0d6c6de81b144a968",
"malsite_ip_host": "199.59.43.228",
"malsite_latitude": 27.9479302368164,
"malsite_longitude": -82.458422919922,
"malsite_region": "Florida",
"managed_app": "no",
"notify_template": "sileblock.html",
"organization_unit": "",
"os": "Linux",
"os_version": "Linux 22.04.4",
"other_categories": [
"Security Risk",
"Security Risk - Compromised/malicious sites"
],
"page": "ww25.cl.xyz/?subid1=20250627-2139f4956fa",
"page_site": "cleansix",
"policy": "MalsiteCategoryTestPolicy",
"policy_id": "21BDBAE80 2025-05-28 11:59:16.009444",
"protocol": "HTTPS/1.1",
"request_id": 3745126345097297887,
"severity": "high",
"severity_level": "med",
"severity_level_id": 1,
"site": "cleansix",
"src_country": "US",
"src_latitude": 39.0469,
"src_location": "Ashburn",
"src_longitude": -77.4903,
"src_region": "Virginia",
"src_time": "Fri Jun 27 07:32:58 2025",
"src_timezone": "America/New_York",
"src_zipcode": "20149",
"srcip": "52.23.214.14",
"telemetry_app": "",
"threat_match_field": "domain",
"threat_match_value": "ww25.cleansix.xyz",
"threat_source_id": 1,
"timestamp": 1751023978,
"traffic_type": "Web",
"transaction_id": 3745097297887,
"type": "malsite",
"ur_normalized": "nijani@crestdatasys.com",
"url": "ww25.clix.xyz/",
"user": "nijlani@crestdatasys.com",
"useragent": "Python/3.10 aiohttp/3.10.5",
"userip": "172.31.29.12",
"record_type": "alert",
"malsite_confidence": 0,
"object": "",
"referer": "",
"sAMAccountName": "",
"malsite_hostility": "",
"fromlogs": "",
"malsite_first_seen": 0,
"custom_attr": {},
"object_type": "",
"conn_duration": 0,
"universal_connector": "",
"dsthost": "",
"malsite_last_seen": 0,
"suppression_end_time": 0,
"co": "",
"malsite_active": "",
"retro_scan_name": "",
"from_user": "",
"aggregated_user": "",
"division": "",
"req_cnt": 0,
"resp_cnt": 0,
"org": "",
"log_file_name": "",
"browser_version": "",
"department": "",
"browser": "",
"dst_geoip_src": 0,
"gateway": "",
"server_bytes": 0,
"malsite_consecutive": "",
"numbytes": 0,
"malsite_reputation": "",
"appsuite": "",
"serial": "",
"client_bytes": 0,
"src_geoip_src": 0,
"suppression_start_time": 0,
"sfwder": ""
}
],
"wait_time": 5,
"timestamp_hwm": 1751023980
}
Push the file hashes to Netskope Tenant
API Endpoint:
https://
<tenant-url>
/api/v1/updateFileHashList
Method:
POST
Body:
{
"name": "<Name of FileHash List>",
"list": "<MD5 and SHA256 values comma separated>",
"token": <Netskope Tenant V1 Token>,
}
Get URL Lists
API Endpoint:
https://<tenant-url>/api/v2/policy/urllist
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_rbac3_token>
User-Agent
netskope-ce-6.1.0
X-CE-Installation-Id
<installation_id>
Parameters
Key
Value
field
id,name
Sample API Response
[
{
"id": 1,
"name": "test"
}
]
Create URL List
API Endpoint:
https://
<tenant-url>
/api/v2/policy/urllist
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"data": {
"type": "exact",
"urls": [
"www.test.com"
]
},
"name": "string"
}
Sample API Response
[
{
"data": {
"type": "exact",
"urls": [
"www.test.com"
]
},
"id": 0,
"modify_by": "Netskope API",
"modify_time": "1997-01-01 00:00:00",
"modify_type": "Created",
"name": "string",
"pending": 0
}
]
Push the URLs to Netskope
API Endpoint:
https://
<tenant-url>
/api/v2/policy/urllist/
<urllist_id>
/append
Method:
PATCH
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"data": {
"urls": [
"https://example.com/resource/product-000001"
],
"type": "exact"
}
}
Sample API Response
{
"data": {
"type": "exact",
"urls": [
"https://example.com/resource/product-000001"
]
},
"id": 0,
"modify_by": "Netskope API",
"modify_time": "2025-01-01 00:00:00",
"modify_type": "Edited",
"name": "string",
"pending": 0
}
Deploy changes to Netskope URL List
API Endpoint:
https://
<tenant-url>
/api/v2/policy/urllist/deploy
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Sample API Response
[
{
"data": {
"type": "exact",
"urls": [
"www.test.com"
]
},
"id": 0,
"modify_by": "Netskope API",
"modify_time": "1997-01-01 00:00:00",
"modify_type": "Created",
"name": "string",
"pending": 0
}
]
List the Private apps from Netskope Tenant
API Endpoint:
https://
<tenant-url>
/api/v2/steering/apps/private
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Parameters
Key
Value
fields
app_id,app_name
Sample API Response
{
"data": {
"private_apps": [
{
"app_id": 51,
"app_name": "[<private_app_name>]",
},
….
]
},
"status": "success",
"total": 2
}
List Publisher for Private Apps
API Endpoint:
https://
<tenant-url>
/api/v2/infrastructure/publishers
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Parameters
Key
Value
fields
publisher_id,publisher_name
Sample API Response
{
"data": {
"publishers": [
{
"publisher_id": 3,
"publisher_name": "<publisher_name>"
},
….
]
},
"status": "success",
"total": 5
}
Push Private App to Netskope Tenant
API Endpoint:
https://
<tenant-url>
/api/v2/steering/apps/private/
<app_id>
Method:
PATCH
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"host": "1.1.1.1,3.2.14.4",
"protocols": [
{
"port": "23",
"type": "TCP"
}
],
"publishers": [
{
"publisher_id": "3",
"publisher_name": "<publisher_name>"
}
],
"tags": [
{
"tag_name": "test"
}
]
}
Sample API Response
{
"data": {
"allow_unauthenticated_cors": false,
"allow_uri_bypass": false,
"app_id": 51,
"app_name": "[<app_name>]",
"app_option": {},
"bypass_uris": [],
"clientless_access": false,
"host": "1.1.1.1,3.2.14.4",
"id": 51,
"is_user_portal_app": false,
"modified_by": "apigw",
"modify_time": "2025-04-01 04:03:31",
"name": "[Risk Exchange Demo]",
"policies": [],
"private_app_protocol": "",
"protocols": [
{
"created_at": "2025-04-01T04:03:31.659Z",
"id": 270,
"port": "23",
"service_id": 3,
"transport": "tcp",
"updated_at": "2025-04-01T04:03:31.659Z"
}
],
"public_host": "",
"reachability": {
"reachable": false
},
"real_host": "",
"service_publisher_assignments": [
{
"primary": null,
"publisher_id": 3,
"publisher_name": "<publisher_name>",
"reachability": null,
"service_id": 51
}
],
"steering_configs": [
"Default tenant config"
],
"supplement_dns_for_osx": false,
"tags": [
{
"tag_id": 153,
"tag_name": "test"
}
],
"trust_self_signed_certs": false,
"uribypass_header_value": "",
"use_publisher_dns": false
},
"status": "success"
}
Fetch False Positive and Retrohunt Severity
API Endpoint:
https://
<tenant-url>
/api/v2/nsiq/retrohunt/ioc/getinfo
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"hash": [
"e0b060152606988664368bd658cbec4b"
]
}
Sample API Response
{
"status": "OK",
"result": {
"e0b060152606988664368bd658cbec4b": {
"seen": true,
"verdict": "malicious",
"severity": 3,
"md5": "e0b060152606988664368bd658cbec4b",
"sha256": "263689ec92f357b573206c06d27ae957bf17be7ff2b90f917543432b01e3be10",
"malware_name": "Backdoor",
"latest_detection_date": 1750150278,
"verdict_updated": "clean",
"severity_updated": 0
}
}
}
Push the URLs to Netskope for delete retraction
API Endpoint:
https://
<tenant-url>
/api/v2/policy/urllist/
<urllist_id>
/replace
Method:
PATCH
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"data": {
"urls": [
"https://example.com/resource/product-000001"
],
"type": "exact"
}
}
Sample API Response
{
"data": {
"type": "exact",
"urls": [
"https://example.com/resource/product-000001"
]
},
"id": 0,
"modify_by": "Netskope API",
"modify_time": "2025-01-01 00:00:00",
"modify_type": "Edited",
"name": "string",
"pending": 1
}
Get Destination Profiles
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/destinations
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Parameters
Key
Value
fields
id,name,type,values_count
offset
0
limit
100
Sample API Response
{
"elements": [
{
"id": "dfbd59ab-xxxx-xxxx-xxxx-81b7bc805f47",
"name": "CTE Destination Profile",
"type": "insensitive",
"values_count": 100000
}
],
"total_count": 1
}
Create Destination Profile
API Endpoint:
https://<
tenant-url>
/api/v2/profiles/destinations
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"description": "my destination description",
"name": "CTE Destination Profile",
"type": "insensitive",
"values": [
"example.com/resource/product-000001"
]
}
Sample API Response
{
"id": "dfbd59ab-xxxx-xxxx-xxxx-81b7bc805f47",
"name": "CTE Destination Profile",
"description": "my destination description",
"type": "insensitive",
"values": [
"example.com/resource/product-000001"
],
"values_count": 1,
"status": "applied",
"create_by": "NetskopeCE",
"create_time": "2026-04-01T08:48:50.284153069Z",
"modify_by": "NetskopeCE-Dev",
"modify_time": "2026-04-01T08:48:50.284153069Z",
"label_ids": []
}
Push or Remove Destination Profile Values
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/destinations/
<destination-profile-id>
/values
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"operation": {
"op": "append",
"values": [
"www.example.com/mypath1",
"www.example.com/mypath2"
]
}
}
OR
{
"operation": {
"op": "remove",
"values": [
"www.example.com/mypath1",
"www.example.com/mypath2"
]
}
}
Sample API Response
{
"id": "dfbd59ab-xxxx-xxxx-xxxx-81b7bc805f47",
"name": "CTE Destination Profile",
"description": "my destination description",
"type": "insensitive",
"values": [
"example.com/resource/product-000001",
"www.example.com/mypath1",
"www.example.com/mypath2"
],
"values_count": 3,
"status": "applied",
"create_by": "NetskopeCE",
"create_time": "2026-04-01T08:43:21.661Z",
"modify_by": "NetskopeCE",
"modify_time": "2026-04-01T08:43:53.825Z",
"label_ids": []
}
Remove for Delete Retraction
{
"id": "dfbd59ab-xxxx-xxxx-xxxx-81b7bc805f47",
"name": "CTE Destination Profile",
"description": "my destination description",
"type": "insensitive",
"values": [
"example.com/resource/product-000001"
],
"values_count": 1,
"status": "applied",
"create_by": "NetskopeCE",
"create_time": "2026-04-01T08:43:21.661Z",
"modify_by": "NetskopeCE",
"modify_time": "2026-04-01T08:50:12.81Z",
"label_ids": []
}
Apply Pending Changes for a Destination Profile
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/destinations/deploy
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Body
{
"ids": [
"dfbd59ab-xxxx-xxxx-xxxx-81b7bc805f47"
]
}
Sample API Response
{
"applied": [
"dfbd59ab-xxxx-xxxx-xxxx-81b7bc805f47"
]
}
Get DNS Profiles
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/dns
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Query Parameters
Key
Value
Description
limit
150
Pagination limit
offset
0
Pagination offset
fields
id,name
Fields to get in the API response
filter
Name eq “
<Profile Name>
Used to get a DNS profile details by name
Sample Response
{
    "profiles": [
        {
            "id": "43b69ef8-47b1-11f1-b64b-86231e291fcc",
            "name": "Netskope DNS Profile 1"
        },
        {
            "id": "783e8454-4d26-11f1-a0bb-0e3351bf9dec",
            "name": "Netskope DNS Profile 2"
        }
    ],
    "total": 2
}
Create DNS Profile
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/dns
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Request Body
{
    "name": "My Profile",
    "log_traffic": "Blocked DNS",
    "domain_config": {
        "security_categories": [
            {
                "name": "Newly Registered Domain",
                "action": "Sinkhole"
            }
        ],
        "allow_list": [
            {
                "record_types": [
                    "All Record Types"
                ],
                "domain_names": [
                    "abc.com"
                ]
            }
        ],
        "block_list": [
            {
                "record_types": [
                    "All Record Types"
                ],
                "domain_names": [
                    "xyz.com"
                ]
            }
        ],
        "sinkhole_ip": "1.2.3.4",
        "block_all_except_allow_list": false
    }
}
Sample Response
{
    "applied_time": "2026-05-15 10:41:26",
    "create_by": "RBACv3",
    "create_time": "Fri, 15 May 2026 10:41:26 GMT",
    "custom_config": {
        "bypass_original_dns": false,
        "enable": false,
        "fallback_to_netskope_dns": true,
        "server_ip": []
    },
    "description": "",
    "domain_config": {
        "allow_list": [
            {
                "destination_profiles": [],
                "domain_names": [
                    "abc.com"
                ],
                "record_types": [
                    "All Record Types"
                ]
            }
        ],
        "block_all_except_allow_list": false,
        "block_list": [
            {
                "destination_profiles": [],
                "domain_names": [
                    "xyz.com"
                ],
                "record_types": [
                    "All Record Types"
                ]
            }
        ],
        "security_categories": [
            {
                "action": "Sinkhole",
                "name": "Newly Registered Domain"
            }
        ],
        "sinkhole_ip": "1.2.3.4"
    },
    "id": "9ffaa12c-504a-11f1-bd75-6ae4e2669381",
    "log_traffic": "Blocked DNS",
    "modify_by": "RBACv3",
    "modify_time": "Fri, 15 May 2026 10:41:26 GMT",
    "name": "My Profile",
    "status": "Applied",
    "tunnel_config": {
        "allow_list": [],
        "enable": false
    }
}
Update DNS Profile
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/dns/{profile_id}
Method:
PATCH
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Path Parameter
Key
Value
profile_id
173axxxx-xxxx-xxxx-xxxx-xxxxe2669381
Request Body
{
    "domain_config": {
        "security_categories": [
            {
                "name": "Newly Registered Domain",
                "action": "Sinkhole"
            }
        ],
        "allow_list": [
            {
                "record_types": [
                    "All Record Types"
                ],
                "domain_names": [
                    "abc.com"
                ]
            }
        ],
        "block_list": [
            {
                "record_types": [
                    "All Record Types"
                ],
                "domain_names": [
                    "xyz.com"
                ]
            }
        ],
        "sinkhole_ip": "1.2.3.4",
        "block_all_except_allow_list": false
    }
}
Sample Response
{
    "applied_time": "2026-05-15 10:41:26",
    "create_by": "RBACv3",
    "create_time": "Fri, 15 May 2026 10:41:26 GMT",
    "custom_config": {
        "bypass_original_dns": false,
        "enable": false,
        "fallback_to_netskope_dns": true,
        "server_ip": []
    },
    "description": "",
    "domain_config": {
        "allow_list": [
            {
                "destination_profiles": [],
                "domain_names": [
                    "abc.com"
                ],
                "record_types": [
                    "All Record Types"
                ]
            }
        ],
        "block_all_except_allow_list": false,
        "block_list": [
            {
                "destination_profiles": [],
                "domain_names": [
                    "xyz.com"
                ],
                "record_types": [
                    "All Record Types"
                ]
            }
        ],
        "security_categories": [
            {
                "action": "Sinkhole",
                "name": "Newly Registered Domain"
            }
        ],
        "sinkhole_ip": "1.2.3.4"
    },
    "id": "9ffaa12c-504a-11f1-bd75-6ae4e2669381",
    "log_traffic": "Blocked DNS",
    "modify_by": "RBACv3",
    "modify_time": "Fri, 15 May 2026 10:41:26 GMT",
    "name": "My Profile",
    "status": "Applied",
    "tunnel_config": {
        "allow_list": [],
        "enable": false
    }
}
Get DNS Categories
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/dns/domaincategories
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Query Parameters
Key
Value
limit
150
offset
0
sortby
name
sortorder
asc
Sample Response
{
    "domaincategories": [
        {
            "category_type": "Security",
            "id": "575",
            "name": "Newly Observed Domain"
        },
        {
            "category_type": "Security",
            "id": "574",
            "name": "Newly Registered Domain"
        },
        {
            "category_type": "Security",
            "id": "583",
            "name": "Security Risk - Ad Fraud"
        },
        {
            "category_type": "Security",
            "id": "588",
            "name": "Security Risk - Attack"
        },
        {
            "category_type": "Security",
            "id": "578",
            "name": "Security Risk - Botnets"
        },
        {
            "category_type": "Security",
            "id": "579",
            "name": "Security Risk - Command and Control server"
        },
        {
            "category_type": "Security",
            "id": "580",
            "name": "Security Risk - Compromised/malicious sites"
        },
        {
            "category_type": "Security",
            "id": "589",
            "name": "Security Risk - Cryptocurrency Mining"
        },
        {
            "category_type": "Security",
            "id": "594",
            "name": "Security Risk - DGA"
        },
        {
            "category_type": "Security",
            "id": "584",
            "name": "Security Risk - Hacking"
        }
    ],
    "total": 15
}
Get DNS Record Types
API Endpoint:
https://
<tenant-url>
/api/v2/profiles/dns/recordtypes
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Netskope-API-Token
<netskope_api_rbac3_token>
X-CE-Installation-Id
<installation_id>
Query Parameters
Key
Value
limit
150
offset
0
sortby
name
sortorder
asc
Sample Response
{
    "recordtypes": [
        {
            "id": "13",
            "name": "A"
        },
        {
            "id": "62",
            "name": "AAAA"
        },
        {
            "id": "83",
            "name": "ANY"
        },
        {
            "id": "6",
            "name": "All Record Types"
        },
        {
            "id": "76",
            "name": "CERT"
        },
        {
            "id": "27",
            "name": "CNAME"
        },
        {
            "id": "48",
            "name": "MX"
        },
        {
            "id": "20",
            "name": "NS"
        },
        {
            "id": "41",
            "name": "PTR"
        },
        {
            "id": "34",
            "name": "SOA"
        }
    ],
    "total": 12
}
Performance Matrix
This reading is conducted on a Large CE Stack with these specifications by pulling and pushing 100k IoCs.
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Indicators fetched from Netskope tenant
~45k per min
Indicators shared to Netskope tenant (URL List)
~100k per min
Indicators shared to Netskope tenant (File Hash List)
~200k per min
Indicators shared to Netskope tenant (Private App)
~500 per min
Indicators shared to Netskope tenant (Destination Profile)
~120k per min
Indicators shared to Netskope tenant (DNS Profile)
~200k per min
Note
Private App has a maximum limit of 500, so users will not be able to share more than 500 IOCs to a single Private App.
Here the sharing performance is calculated with creating a new Destination profile. If the IoCs are shared in an existing Destination profile, the performance might be affected due to the API behaviour that only allows 10 IoCs in one batch while sharing to an existing Destination profile.
User Agent
For example: netskope-ce-6.1.0
Workflow
Create a File profile
Create a Malware Detection profile
Configure a Real-Time Protection policy
Configure a Destination profile
Configure a DNS Profile
Configure the Threat Exchange plugin
Enable IoC retraction
Create a Business Rule
Set up Sharing using the Source Plugin, Business Rule, Destination Plugin, and Target
Validate the Threat Exchange plugin
Watch a Video
Click play to watch a video.
Create a File Profile
In your Netskope tenant, go to
Policies > Profiles > File
and click
New File Profile
.
Select
File Hash
, and in the dropdown, select
SHA256
.
Enter a temporary value in the text field. Netskope does not support proceeding without having a value in this field, and we recommend using as a string of 64 characters that consist of the character f, which will have a very low possibility of matching a valid file format. For example, ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.
Click
Next
.
Enter a Profile name and description. Do not use spaces in your profile name; use underscores instead for spaces.
Click
Save
.
To use this profile in a policy, click
Apply Changes
on the top right of the screen.
Create a Malware Detection Profile
In your Netskope tenant, go to
Policies > Threat Protection > Malware Detection Profile
and click
New Malware Detection Profile
.
Click
Next
.
For this example, create this list as a block list (click through Allow options). Netskope does support inclusion of both allow and block lists in the Malware Detection profiles. Click
Next
.
Select the File Profile that you created previously.
Click
Next
.
Enter a name for the Malware Detection profile.
Click
Save Malware Detection Profile
.
To use this profile in a policy, click
Apply Changes
on the top right of the screen.
Create Real-Time Protection Policy
In your Netskope tenant, go to
Policies > Real-time Protection
. The policy configuration is just an example. Modify as appropriate for your organization.
Click
New Policy
and then select
Cloud App Access
.
For Source, leave the default as
User = Any
.
Click
Category
.
The window expands to allow you to search for and select the option
All Categories
.
Click outside of this list to close the search dialog.
For Activities & Constraints, click
Edit
.
Select
Upload
and
Download
.
Click
Save
.
For
Profile & Action
, click the
Add Profile
dropdown, and select
Threat Protection Profile
.
Click in the new Threat Protection Profile field, and it will open up a list of available profiles.
Select the Malware Detection profile you created previously.
Adjust the
Action: Alert
to reflect
Action: Block
for each of the Severity options.
For
Set Policy
, enter a descriptive Policy Name.
Click
Save
in the top right of the screen.
Select the
To the top
option when it is presented.
To publish this policy into the tenant, click
Apply Changes
on the top right of the screen.
Create a Destination Profile
In your Netskope tenant, go to
Policies > Profiles > Destination
and click
New Destination Profile
.
Provide
Destination Profile Name
and
Description
and select the
Match type
.
Click
Save
.
To use this profile in a policy, click
View pending changes
on the top of the screen and then click on
Apply changes
.
Create a DNS Profile
In your Netskope tenant, go to
Policies > Profiles > DNS
and click
New DNS Profile
.
Provide the profile name.
Click on Save.
Configure the Threat Exchange Plugin
In
Settings
, go to the
Plugin Store
and make sure the Category is selected as CTE.
Search for the
Netskope Threat Exchange
plugin and click on the plugin card to configure.
Enter the Basic Information:
Configuration Name
: Enter a unique configuration name.
Sharing Sync Interval
: Specify the time between sharing syncs.
Tenant
: Choose the desired tenant from the dropdown menu. The primary tenant is automatically selected by default.
Aging Criteria
: Specify the criteria for aging the indicator, with the default expiration set at 90 days.
Override Reputation
: Assign a value [1-10] to override the reputation received from this configuration; leave it blank for the default setting.
Tags Aggregate Strategy
: Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Click
Next
and enter the values for the Configuration Parameters:
Enable Polling
: Allows data polling from Netskope.
Types of Threat Data to Pull
: Selected indicator types will be extracted from Netskope malware alerts and stored on Threat Exchange.
Initial Range (in days)
: Initial range for threat data to be pulled.
Enable Tagging
: The unshared tag indicators can be tagged using this feature.
Enable Retrohunt
: Enable/disable querying the Retrohunt API for clean indicators. If set to Yes, the plugin will not pull clean indicators and if retraction is enabled (Settings > Threat Exchange > IOCs Retraction toggle), clean indicators will be marked as retracted. If set to No, the plugin will pull all indicators. The Retrohunt API requires an ‘Advanced Threat Protection’ license and the ‘Retrohunt API Query’ flag enabled on the Netskope tenant. To enable retraction for the Threat Exchange module, go to
Settings > Threat Exchange
and enable the IoC(s) Retraction toggle.
Note
It will only retract the IoCs when Enable Retrohunt is set to
Yes
and the retraction will be based on the
verdict_updated
field.
The Enable Retrohut is only for pulling the hashes (SHA256 and MD5).
Click
Save
.
Create a Business Rule for Threat IoCs
In Threat Exchange, go to
Business Rules
.
Click
Create New Rule
and enter a Rule Name and filter per your requirements.
Click
Save
.
Add a Sharing Configuration
In order to add Sharing configuration, a third-party Threat Exchange plugin, like
CrowdStrike
, has to be configured before proceeding. You need both a source and destination plugin (configurations) to add a Sharing configuration.
Netskope Threat Exchange plugin supports the following three sharing:
Add to URL List
This will replace the old URL List with the new URLs on Netskope Tenant.
The maximum sharing capacity is 7MB per request for URL List and overall it supports 300000 URLs on the URL List page.
If more than 300000 URLs exist from all the URL Lists, the plugin will not be able to apply changes on Netskope Tenant as mentioned in
troubleshooting
.
Add to File Hash List
This will replace the old File Hash List with the new Hashes on Netskope Tenant.
The maximum sharing capacity is 8MB per request for File Hash List.
Users will need to configure the Netskope Tenant plugin with v1 API Token for ‘Add to File Hash List’
Add to Private App
This will replace Hosts (IP addresses/hostnames) of the Private App on Netskope Tenant.
You can also add tags to the Private Apps.
Add to Destination Profile
This will append the new URLs in the already created Destination Profile or in the new Destination Profile.
The maximum sharing capacity depends on the Match Type you have selected:
The Regex Match Type supports only 1000 URLs per tenant.
You can create up to 1,000 destination profiles in a tenant.
A destination profile can have up to 100,000 destinations. Comments are unlimited. However, the maximum size for a destination profile (including comments) is 10 MB.
A total of up to 300,000 destinations (excluding comments) is supported in a tenant. To increase this limit, a license is required.
Add to DNS Profile
This will append the new Domains/FQDNs in the already created DNS Profile or in the new DNS Profile.
The maximum sharing capacity is 16 MB.
Cloud Exchange does not support deleting URL list, File list, Private app, Destination profile and DNS profile. You need to delete them from the Netskope Tenant UI.
Add to a URL List
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select how to share the indicators:
Select the Source Plugin.
Select the Business Rule.
Select the Destination Plugin.
Select the Target  Add to URL List.
Choose the list name from the dropdown menu if you wish to add the URL to a list that has already been created.
OR
Create a New List by giving the name to the Create New List field.
Choose the format in which you’d like the URL to be stored within the list: Exact OR Regex.
List Size [Maximum Size of the Limit is 7MB]
Default URL.
Note
The
Add to URL List
action will append the new URL List in the old URLs on the Netskope tenant.
Click
Save
.
Add to a File Hash List
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select how to share the indicators.
Select the Source Plugin.
Select the Business Rule.
Select the Destination Plugin.
Select the Target Add to File Hash List.
Provide the name of the file hash list on Netskope.
List Size (Maximum Size of the Limit is 8MB).
Note
The
Add to File Hash List
action will replace the whole File Hash list on the Netskope tenant.
Click
Save
.
Add to a Private App
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select how to share the indicators.
Select the Source Plugin.
Select the Business Rule.
Select the Destination Plugin.
Select the Target  Add to Private App.
Choose the Private App Name from the dropdown menu if you wish to add the domain/hostname to an already created app,
or
create a New Private App.
Select the Protocol.
Provide the comma-separated TCP and UDP ports (for the selected protocol).
Select the Publisher.
Use Publisher DNS or Not.
Default Host.
Note
The
Add to Private
action will replace the Hosts (IP addresses/hostnames) of the Private app on the Netskope tenant.
Click
Save
.
Add to Destination Profile
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select how to share the indicators.
Select the Source Plugin.
Select the Business Rule.
Select the Destination Plugin.
Select the Target  Add to Destination Profile.
Choose the Destination Profile Name from the dropdown menu if you wish to add the URL to an already created profile.
OR
Create a New Destination profile.
Provide Description for the profile if creating a new profile.
Select a Match Type for the profile if creating a new profile.
Select Apply Pending Changes as Yes if you want to always apply the pending changes of the profile before sharing the URL.
Click
Save
.
Note
Both of the Exact Match Types support 100k URLs per Destination Profile and 300k URLs per tenant.
The Regex Match Type supports only 1000 URLs per tenant.
Netskope plugins supports the Destination Profile from v2.4.0 with CE v6.1.0
Add to DNS Profile
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select how to share the indicators.
Select the Source Plugin.
Select the Business Rule.
Select the Destination Plugin.
Select the Target  Add to DNS Profile.
Set the Action Type to perform on DNS Profile.
Select an existing DNS Profile.
Create DNS Profile with the given name. (Only Enter if you have selected ‘Create new profile’ in DNS Profile parameter) Create New Profile should be less than or equal to 255 characters.
Provide the description to create a DNS Profile with a given description. (Only Enter if you have selected ‘Create new profile’ in DNS Profile parameter) Profile Description should be less than or equal to 255 characters.
Select one or more Categories along with the action to apply (Block or Sinkhole). The same category cannot be selected with both ‘Block’ and ‘Sinkhole’ actions. Selecting any ‘Sinkhole’ variant requires a value in the ‘Sinkhole IP’ parameter.
Enter a Sinkhole IP. (Only enter if you have selected a sinkhole category action in the Categories parameter).
Select one or more Record Types. ‘All Record Types’ cannot be selected together with any other Record Type value.
Under Block All except Allow list
,
select ‘Yes’ to block all DNS traffic except domains on this profile’s allowlist; select ‘No’ to allow all traffic except the listed domains.
Block All except Allow list
cannot be set to Yes along with Action type
Add to Domain Block list
.
Click
Save
.
Enable IoC Retraction
To enable IoC retraction from Cloud Exchange:
Go to
Setting > Threat Exchange
Enable
IoC(s) Retraction
and enter a
Retraction Interval
.
Click
Save
.
Note
If IoCS are initially pulled in Cloud Exchange, and the Retrohunt pull is enabled, the pulled IoCs from Netskope will be marked as Retracted if the IOC is returned as
clean
from the Retrohunt APIs. After the IoC is marked as retracted based on the Retrohunt APIs, the IoC will be retracted from the 3rd-party as well if the 3rd-party supports push retraction. If any 3rd-party IoC is shared to a Netskope URL List or File Hash list, and is marked as retracted in Cloud Exchange, it will be deleted from the tenant as well when the next sharing is triggered.
Validate the Threat Exchange Plugin
Validate the Pull
To validate the pulling of Alert from Netskope, go to the
Logging
in Cloud Exchange and search for the pulled logs.
You can add a filter like:
message Like “pulled”
.
Note
If Enable Retrohunt is selected as
yes
, then after pulling malware from the tenant, the plugin will check the false positive status using Retrohunt, and if any indicator has
verdict_updated: clean
it will not be stored in Cloud Exchange and only malicious indicators will be stored. Also the plugin will store the severity of the indicator using the
severity_updated
field.
If you have to update the severity of the indicator in Cloud Exchange when it is updated on the Netskope tenant, you have to change the
Reconciliation Criteria
value to
Higher Severity Source Override
from
Settings >Threat Exchange
. And the severity will only be updated if it changes from lower to higher, but not for higher to lower.
You can verify the skipped indicators due to false positives by applying the filter
message Like “<configuration_name>”
in
Logging
.
After successfully storing the indicators, when the retraction cycle runs, the plugin will again check the
verdict_updated
field from Retrohunt. And if any of the stored records has changed the value from
malicious
to
clean
, the indicator will be marked as
Retracted
in Cloud Exchange.
For verifying retraction of indicators, you can check the logs using filter
message Like “[Retraction]”
.
Also you can verify the retracted IoCs from the
Threat IoCs
page.
Add a filter like
sources.source Is equal “<configuration_name>” && sources.retracted Is equal true
.
Validate the Stored Indicators
To validate the stored indicator in the Cloud Exchange, go to
Threat Exchange > Threat IoCs
.
Validate Alerts are Present in your Netskope Tenant
In your Netskope tenant go to
Skope IT
.
Click
Alerts
, click
Add Filter
and select
Alert Type > Malsite
and
Malware
, and then click
Apply
. Select an option from the
Last x Days
dropdown in the top-right corner.
Validate the Push
To validate the plugin workflow in Cloud Exchange:
Go to
Logging
and Search for shared indicators with the filter
message Like “shared”
.
The shared logs will be filtered.
Validate the Push on the Netskope Tenant
Ensure the push of indicators on the Netskope tenant from the 3rd-party plugin.
Validate the Add to URL List Sharing
In your Netskope tenant, go to
Policies
.
Click
Web > URL Lists
.
Click on the List Name for which the URL is stored.
The List will be shown here.
And as this sharing supports push retraction, you can also validate the logs in the logging section by applying a filter as provided below:
And you can check the same indicators are deleted from the URL list on the Netskope tenant.
Validate the Add to File Hash List Sharing
In your Netskope tenant, go to
Policies
.
Click
Web > File
.
Click on the
File Name > File Hash
for which the MD5 and SHA256 File Hash is stored.
Validate the Add to Private App Sharing
In your Netskope tenant, go to
Settings
.
Click
Security Cloud Platform > App Definition > Private App
.
Click the application name where the hostname and domain details are shared.
Validate the Add to Destination Profile Sharing
In your Netskope tenant, go to
Policies
.
Click
Profiles > Destination
.
Click on the Profile Name on which the URL is shared.
The List will be shown here.
And as this sharing supports push retraction, you can also validate the logs in the logging section by applying a filter as provided below:
And you can check the same indicators are deleted from the Destination Profile on the Netskope tenant.
Validate the Add to DNS Profile Sharing
In your Netskope tenant, go to
Policies
.
Click
Profiles > DNS
Open the DNS profile that was used while configuring the sharing.
This action also supports push retraction, which means the IOCs that were already shared to a DNS profile and are marked as retracted yes in Cloud Exchange will get deleted from the DNS profile in the next sharing sync interval.
Example:
This is a DNS profile that has domain “cgotdz7us4.co”. This IOCs was pulled from CrowdStrike and shared to this DNS profile via Netskope Threat Exchange plugin.
Now the domain “cgotdz7us4.co” got marked as retracted in CE as it was deleted on CrowdStrike platform.
After the next sharing sync interval of Netskope Threat Exchange plugin it got deleted from the DNS profile. We can track the status for deletion via the Retraction result field. Once the retraction result is CTE Netskope Threat Exchange: retracted, this means it is deleted from the Netskope Tenant.
DNS Profile after IOC was deleted,
Troubleshooting the Threat Exchange Plugin
Receiving Error While Configuring the Netskope Threat Exchange
Getting the error:
The Netskope tenant API V2 token does not have necessary permissions configured. Refer to the list of endpoints for which the token is missing permission. **
Cause:
The provided V2 token does not have the minimum required permissions to configure the tenant in Cloud Exchange.
What to do:
Go to
Logging
and look for a warning log similar this:
TENANT Netskope Tenant (Required) [Netskope Tenant]: For Netskope Tenant, received 403 error for following endpoint(s)
Expand the log and get the list of endpoints that are missing permissions.
Update the v2 token permissions, and add the permission for the above endpoint list from the Netskope UI.
Sharing configuration still has List Size 8 MB instead of 7MB in Add to URL list after upgrading the plugin
Since plugin version 2.2.0, we have updated the List size from 8 MB to 7MB. If you have configured the plugin including the Sharing configurations with older versions, and then upgrade the plugin to the latest version. The configuration still has the List Size 8, and while editing the Sharing configuration, it is giving an error.
What to do:
Edit the configuration and change the List Size to 7MB, and then save the configuration.
Configure a new Sharing following the steps mentioned in
Add to URL List
.
Receiving error after successful execution of Add to URL list
If you have synced the
Add to URL list
sharing, and you are seeing this error even after successful execution, and in the Netskope tenant, there is a warning icon that is saying
View pending changes
. This is due to limited URLs (300000) being allowed on the Netskope Tenant mentioned in this
documentation
.
What to do:
Remove the unnecessary URLs from your URL Lists, and then click
Apply Changes
.
Unshared tags are not attached to the IoCs that are not shared to the third party platform
You may encounter the issue where the tagging functionality is not working properly. To overcome this issue, you need to update the plugin to the latest version, then
Unshared
tags will be attached to the IoCs that are skipped while sharing to Netskope Tenant.
What to do:
Update the plugin to Netskope Threat Exchange v2.3.0 or above.
Note
If the IoC is having an
invalid host
or
invalid app
tag attached to it, then the
unshared
tag will not be attached to that IoC.
Some of the IOCs not shared to Destination Profile even if the URLs are valid in Cloud Exchange
You might see only a few URLs shared to the Destination Profile even if the URLs are valid in Cloud Exchange. This might be due to below reasons:
The URLs do not match the definition for the Match Type.
The maximum number of valid URLs exceeds on the Netskope Tenant.
What to do:
Verify the URL matches the definition for the Match Type provided in the Destination Profile. For more information, refer to the
documentation
.
Verify the available URLs on the Destination Profiles as for both of the Exact Match Types, the maximum supported URLs are 100k per Profile and 300k per tenant. And for Regex Match Type, the maximum supported URLs are 1000 per tenant.
Limitations
An error will be thrown if the same File Hash list will be shared to Netskope Tenant from Cloud Exchange. If a File Hash list contains the same list of file hashes that were pushed previously, and Cloud Exchange tries to push it again, then the API will throw error as shown here:
If you have provided multiple ports and ranges while configuring
Add to Private App Sharing
, it might convert the multiple ports in one range as per the API limitations, and it could be seen as below:
Known Behaviors
Starting from version 2.3.0, if the
Enable Retrohunt
field is selected as
Yes
, then the plugin will only pull malware data that does not have
verdict: clean
or
verdict_updated: clean
. However, during the retraction cycle, only
verdict_updated: clean
indicators are retracted. If you’ve already used an older version (v2.1.3 or earlier) and pulled indicators, upgrading to v2.3.0 will not retract indicators with only
verdict: clean
; only those with
verdict_updated: clean
will be retracted.
While upgrading the plugin, if you use the skip button then you will not be able to enable the plugin from plugin version 2.3.0. We have introduced a new field
Enable Retrohunt
and its value will not be stored if you use the
Skip
button while upgrading the plugin. To overcome this issue, you need to edit the plugin and enable/disable the retrohunt field, save the plugin, and then you will be able to enable the plugin.
Users will not be able to configure the same action with different business rules for DNS Profile and Destination profile.
In this Topic
Threat Exchange Plugin

---
## About Malware Retention
**URL:** https://docs.netskope.com/en/about-malware-retention/
**Last Modified:** 2025-08-31T01:47:31+00:00
**Scraped:** 2026-08-11T07:33:32.988671+00:00

About Malware Retention - Netskope Technical Documentation
About Malware Retention
On the Malware Retention page (
Settings
>
Threat Protection
>
Malware Retention
), you can create and manage Malware Retention profiles that allow you to define where you can store and securely download files detected as malicious to further investigate or analyze them. You can download the files directly from Azure Blob Storage or from
Malware Incidents
.
Configuration
In the
Configuration
tab, you can:
Click
Edit
to enable malware retention for your organization and choose a profile. You can only choose one profile.
Create a malware retention profile.
View a list of configured malware retention profiles. For each profile, you can see the following information:
Name
: The name of the profile.
Last Edit
: The last time the profile was edited and by who.
Click
to choose one of the following options:
Edit
: Edit the profile information.
Delete
: Delete the profile.
Instances
In the
Instances
tab, you can:
Set up an application instance
. Netskope only supports Azure Blob Storage at this time.
Filter the configured instance list by application.
View a list of configured instances. For each instance, you can see the following information:
Instance Name
: The name of the instance.
Last Edited
: The last time the instance was edited and by who.
Set up a new instance for the filtered application
. Netskope only supports Azure Blob Storage at this time.
Click
to choose one of the following options:
Regrant
: Regrant Netskope access to Azure Blob Storage.
Edit
: Edit the instance information.
Delete
: Delete the instance.
View up to 100 instances per page.
View multiple pages of the table.
In this Topic
About Malware Retention

---
## Maltiverse Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/maltiverse-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:44:19+00:00
**Scraped:** 2026-08-11T07:33:59.308187+00:00

Maltiverse Plugin for Threat Exchange - Netskope Technical Documentation
Maltiverse Plugin for Threat Exchange
This document explains how to configure the Maltiverse 1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to fetch indicators of type SHA256, IP Addresses (IPv4 and IPv6), URLs and Hostnames from
Intelligence > Feeds
in the Maltiverse platform. This plugin does not support pushing indicators to Maltiverse.
Prerequisites
To complete the plugin configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
A Secure Web Gateway subscription for URL sharing. Refer to
URL Lists
for more information.
Connectivity to the Maltiverse platform:
https://maltiverse.com
.
Maltiverse Plugin Support
This plugin is used to fetch indicators of type SHA256, IP Addresses (IPv4 and IPv6), URLs and Hostnames from
Intelligence > Feeds
in the Maltiverse platform. This plugin does not support pushing indicators to Maltiverse.
Fetched indicator types
URL, Hostname, IPv4, IPv6, SHA256
Shared indicator types
Not Supported
Mappings
Pull Mapping
Cloud Exchange Fields
Maltiverse Field
type
type
value
sha256, ip_addr, url, hostname
severity
classification
firstSeen
creation_time
lastSeen
modification_time
tags
tag
Severity Mapping
Cloud Exchange Severity
Maltiverse Classification
Critical
malicious
Medium
suspicious
Low
neutral
Push Mapping
IoC Type in Cloud Exchange
IoC Type in Maltiverse
SHA256
sample
IPv4
ip
IPv6
ipv6
URL
url
Hostname
hostname
Permissions
Make sure the Maltiverse account has access to generate the API Key.
API Details
List of APIs used
API Endpoint
Method
Use Case
/feed/
<FEED_ID>
GET
Check the existence of Feed
/feed/
<FEED_ID>
/download
GET
Pull Data
Check the Existence of a Feed
API Endpoint:
https://api.maltiverse.com/feed/
<FEED_ID>
Method
: GET
Parameters:
NA
Sample API Response
{
    "access": "public",
    "author": "agomez",
    "count_hostname": 153701,
    "count_ip": 0,
    "count_ipv4": 24,
    "count_sample": 0,
    "count_url": 71355,
    "creation_time": "2020-03-15 21:17:20",
    "description": "Contains Phishing URLs that an adversary uses normally via email or other communication channels to trick a victim into providing sensitive information like passwords or to infect a host.",
    "downloads": 1700044,
    "from": 0,
    "like": [
        {
            "md5_email": "eb54f8ac8dc669de1a276cc3c616068e",
            "username": "vxtxz"
        },
        {
            "md5_email": "2a700a5b7ad7f624c484669181e45f24",
            "username": "christy7669"
        },
    ],
    "md5_email": "4d210379b8e664f2597a15706a5061f8",
    "modification_time": "2024-04-09 17:03:29",
    "name": "T1566 - Phishing",
    "percolator_id": "D4AO4HAB8jmkCY9e73qB",
    "query": "blacklist.external_references.external_id:T1566 AND classification:malicious",
    "range": "now-30d",
    "range_field": "modification_time",
    "size": 50,
    "sort": "creation_time_desc",
    "subscription": [],
    "tag": [
        "feed",
        "preventable",
        "package:mitre",
        "package:siem"
    ],
    "team_id": 77,
    "team_md5_email": "30b1655da1a0601665c813a67609445a",
    "team_name": "Maltiverse Research Team"
}
Pull Data
API Endpoint:
https://api.maltiverse.com/feed/
<Feed_ID>
/download
Method:
GET
Parameters:
NA
Headers
Accept
application/json
Authorization
Bearer
<API KEY>
Sample API Response
[
    {
        "blacklist": [
            {
                "count": 1,
                "description": "GuLoader",
                "external_references": [
                    {
                        "description": "GuLoader",
                        "external_id": "S0561",
                        "source_name": "mitre-attack",
                        "url": "https://attack.mitre.org/software/S0561/"
                    }
                ],
                "first_seen": "2024-08-27 15:17:59",
                "labels": [
                    "malicious-activity"
                ],
                "last_seen": "2024-08-27 15:17:59",
                "ref": [
                    1
                ],
                "source": "MalwareBazaar Abuse.ch"
            }
        ],
        "classification": "malicious",
        "creation_time": "2024-08-27 16:19:09",
        "filename": [
            "Factura_032293167_315806916060401554308_36060114_88716814753733436980_20088269.exe"
        ],
        "filetype": "application/x-dosexec",
        "is_iot_threat": false,
        "md5": "439042b61eb166d9a2a8c7c7e681c360",
        "modification_time": "2024-08-27 16:19:09",
        "sha1": "ba2552ec452cbfe940d69927b543da613c979d66",
        "sha256": "ad3465fcc39bd03915f9d11f3f8150acefe2f8ae3039ee9a4e6a75dbf660b3e3",
        "type": "sample"
    }
]
Performance Matrix
This performance has been conducted on a large CE instance with below-mentioned specifications by pulling 100K IOCs. It takes around 7 minutes to pull and store 100K IOCs.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Maltiverse
~14K per minute
Indicators shared with Maltiverse
Not Supported
User Agent
netskope-ce-5.0.1-cte-maltiverse-v1.0.0
Workflow
Get your Maltiverse API Key.
Configure the Maltiverse plugin.
Add a Business Rule.
Validate the Maltiverse plugin.
Click play to watch a video.
Get your Maltiverse API Key
Log in to Maltiverse and go to
Profile > Users
.
Scroll down to
Plan
and click
View API Key
. Copy the API Key; this is used to configure the Maltiverse plugin.
Configure the Maltiverse Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
. Search for and select the
Maltiverse v1.0.0 (CTE)
plugin box.
Add a configuration name, and change the sync interval if you want to.
Click
Next
, and add the configuration parameters:
API Key: Your Maltiverse API Key.
Classifications: Indicators from the selected Classifications will be fetched. Leave blank to fetched indicators from all Classifications.
Feeds: Indicators from the selected Feeds will be fetched.
Other Feeds: Comma-separated list of Other Feed IDs to import.
Enable Tagging: Enable/Disable tagging functionality.
Click
Save
.
Add a Threat Exchange Business Rule for Maltiverse
You can create a Business Rule to share the IoCs pulled from Maltiverse to Netskope or other Threat Exchange 3rd-party plugins.
Go to
Threat Exchange > Business Rule > Create New Rule
.
Add your required filter(s) for the IoCs you want to share, and then click
Save
.
Sharing with Maltiverse
This plugin does not support sharing indicators with Maltiverse.
Validate the Maltiverse Plugin
Validate the Pull
To check the IoCs pulled from Maltiverse, go to the
Logging
and check the logs from Maltiverse.
Example:
message Like “CTE Maltiverse” && type IN (“info”)
To verify the IoCs stored in Cloud Exchange, go to
Threat Exchange > Threat IOCs
and search for IoCs pulled from source Maltiverse, or the plugin configuration name that you used for the plugin.
On Maltiverse, the indicators are pull from the
Feeds
available under the
Intelligence
.
Validate the Push
Not Supported.
Troubleshooting the Maltiverse Plugin
Unable to pull data from Maltiverse
If you are not able to pull data from the Maltiverse, it might be due to one of these reasons:
No data is available in the Feeds to pull
Available data in the feed are of unsupported type
Selected Classification and feeds combination does not have data
The plugin has encountered any error
What to do:
Check these points and resume the pull accordingly.
You can check the data available in the Feeds by going to
Intelligence > Feeds
. All the Feeds will be listed on the page with the IoC count present on each field.
Check the Classification and Feeds selected in the plugin configuration, and check the same Feeds on Maltiverse. If the data is available in the Feeds, check the Classification type for the feed by clicking on the feed on the
Feed Content
tab.
If you have encountered any error in the plugins, the logs for the same will be available in
Logging
. You can search the plugin logs using filter:
message Like “CTE Maltiverse” && type IN (“error”)
.
In this Topic
Maltiverse Plugin for Threat Exchange

---
## Malware Severity Levels and Detection Types
**URL:** https://docs.netskope.com/en/malware-severity-levels-and-detection-types/
**Last Modified:** 2025-12-08T22:36:38+00:00
**Scraped:** 2026-08-11T07:36:07.609296+00:00

Malware Severity Levels and Detection Types - Netskope Technical Documentation
Malware Severity Levels and Detection Types
There are three malware severity levels. Creating policies that block all three levels is recommended.
Severity
Types
High
Backdoor
Browser
Coinminer
Dialer
Downloader
Dropper
Exploit
Heuristic
HTML Smuggling
Hyperlink
Infostealer
Keylogger
Malware
Network
Password Stealer
Phishing
Ransomware
Rogue
Rootkit
Spam
Spyware
Trojan
Virus
Worm
Medium
None
Low
Adware
Bundler
Greyware
Hacktool
Hoax
Joke
Keygen
Malicious App
Packed
PUP/PUA
The following table provides explanations for the detection types in the malware dashboard pages:
Type
Description
Adware
This type of malware displays advertisements on the user’s desktop, or in the web browser. Adware is also often used to monitor and report user browsing habits to the advertiser to bring more relevant ads. Some free applications available on the web contain the adware payload, which is usually installed with user consent, while some other adware applications are installed without user consent. As with spyware, the adware application is not a legitimate infected file, and therefore it can’t be disinfected.
Backdoor
This type of malware opens up a secret entry point for the attackers to gain access to the target system. The malware can be used to install other malicious programs, monitor the system or user activities, transfer files, acquire passwords, execute arbitrary commands, etc.
Browser
This type of malware is web-based or online in nature that impacts the various browsers like Internet Explorer and Firefox. The browser-based threats include a range of malicious software programs that are designed to infect victims computers, like Exploit kits, malicious script redirections, phishing, etc.
Bundler
A software that installs multiple programs at once. It’s often used to sneak potentially unwanted programs (PUPs) or malware onto a system alongside a legitimate application.
Coinminer
This type of malware secretly uses a victim’s computer resources (CPU or GPU) to mine cryptocurrency for the attacker’s benefit.
Custom Profile Hit
This type of malware matches an entry you added in the file hash list of a
File Profile
. The file profile name is appended to the malware name (e.g., Custom Blocklist Hit:File_Profile_Name).
Dialer
This is a type of malware which uses the modem connected to the computers to dial premium-rate numbers, incurring expensive phone bills for the victim. The malware usually comes bundled with legitimate software downloaded from third party and torrent sites.
Downloader
A small program that downloads and executes other files that are usually more malicious from the internet onto the infected system.
Dropper
A program designed to install or “drop” other malware onto a target system. It contains the malicious payload and the code to install it.
Exploit
This type of malware takes advantage of a bug or vulnerability in order to get unauthorized access to the target system. Successful exploitation can be used to execute arbitrary code, download malwares, conduct denial of service, etc.
Greyware
A general term for software that falls into a grey area between malicious and legitimate. It’s not a full virus but can be annoying or cause performance issues, such as adware or spyware.
Hacktool
This type of malware is used to identify tools and software that can be used by attackers to compromise systems and networks. Programs detected as Hacktools might not be malicious, but they are designed to perform certain actions that matches the characteristics of a malware. Hacktools can perform actions like port scanning, remote connectivity, vulnerability scanning, keygens, etc.
Heuristic
This type of malware is based on rules, patterns, or weighing methods, and is used to detect variants of existing malware and zero-day malware. This malware typically does not have signature or pattern match-based detection.
Hoax
A false warning about a non-existent computer virus or other threat, often spread via email or social media to cause panic and waste time.
HTML Smuggling
This type of malware uses a highly evasive malware delivery technique that abuses legitimate HTML5 and JavaScript features to evade detection and deploy banking malware, remote access Trojans (RATs), and other malware payloads related to targeted attacks.
Hyperlink
A link in a digital document that leads to another location. While not malware, malicious hyperlinks are a primary method used in phishing emails and on websites to direct users to malware downloads or fraudulent sites.
Infostealer
This type of malware gathers confidential information, such as login credentials, credit card numbers, etc., from an infected system, and sends it to a pre-determined location.
Joke
A program designed to play a prank on the user, often by displaying funny images or playing sounds. While usually harmless, they can be disruptive.
Keygen
A program that generates a product licensing key for software. While often used for software piracy, keygens themselves can sometimes contain malware or be used as a delivery mechanism for it.
Keylogger
This type of malware is designed to capture keystrokes from the infected machine. The stolen information is then uploaded to its command and control server. Keyloggers can be used to capture information like credentials, email conversations, instant messages, etc.
Malicious App
This type of malware is used to refer an unknown or new family of malware. These apps are detected based on certain behavioral properties of the file that falls under malicious activities. This can include querying system information, detection of sandboxes or virtual machines, creating persistence, clearing traces, etc.
Malware
This is a generic type of malware for unknown or a new family of malware. The detection is made based on certain behavioral properties of the file that falls under malicious activities. This can include querying system information, detection of sandboxes or virtual machines, creating persistence, clearing traces, etc.
Misleading App
This is a type of application which itself may not be malicious but could be used for malicious activities. This includes web or socks proxies, remote administration software, and more.
The object is an application which is often installed and used for malicious purposes by 3rd parties. While the application itself is not malicious, experience shows that it poses a higher risk (compared to others) of being used for malicious purposes and of being installed without user consent. This category includes web or socks proxies, remote administration software and other types of software. Usually, the detected application is easy to install without user consent, and once installed, it has an option to be almost or completely hidden from the user.
This object may not be malicious, and may be legitimately installed by a user, so it should not be quarantined or removed by default; the user should be asked instead. Obviously, since it’s an application, it can only be removed, not disinfected.
Network
This type of malware infection is capable of performing network-based attacks, like denial of service, flooding, and scanning. Network-based malware infections are also capable of flowing through the network to infect other systems connected within the same range of IP address.
Packed
This type of malware affects the files that are obfuscated using commercial or open file packers. This serves as a code obfuscation technique as packers compress the original binary code using its custom algorithm. Packers are usually legitimate programs, but they are often used by malware authors in packing their own binaries to avoid getting detected through security detection technologies.
Password Stealer
A type of malware designed specifically to harvest login credentials, such as usernames and passwords, from web browsers, applications, and system files.
Phishing
This type of malware attempts to obtain sensitive information, such as password and credit card numbers, by disguising as a trustworthy entity.
PUP/PUA
This type of malware, Potentially unwanted applications (PUA), are programs that are unwanted and usually ships with freeware softwares and tools. PUAs are used to launch hoax advertisements, fake anti-virus scans, selling rogue products, and even launching man-in-the-browser (MitB) attacks.
Ransomware
This type of malware encrypts the victim’s files and displays a ransom note demanding payment, usually in cryptocurrency, in exchange for the decryption key.
Rogue
This type of malware misleads users into believing there is a virus on their computer and aims to trick them into paying for a fake malware removal tool.
Rootkit
A collection of software tools that enables an unauthorized user to gain control of a computer system while hiding its presence and the presence of other malware.
Spyware
This type of malware is installed on a computing device without the end user’s knowledge to gather information about them, their browsing habits, or other data, which is then sent to a third party.
Spam
Unsolicited, unwanted commercial email messages or other electronic messages, often sent in bulk. While not malware itself, it’s a common delivery method for malware and phishing attacks.
Trojan
This is a type of malware that disguises itself as a legitimate or useful application to trick the user into installing and running it. Once executed, it performs malicious actions.
Virus
This is a type of malware that, when executed, replicates itself by modifying other computer programs and inserting its own code. It requires a host program to run and spread.
Worm
A standalone malware computer program that replicates itself to spread to other computers, often using a computer network. Unlike a virus, it does not need to attach itself to an existing program.
In this Topic
Malware Severity Levels and Detection Types

---
## Vectra AI Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/vectra-ai-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:56:02+00:00
**Scraped:** 2026-08-11T07:36:27.414147+00:00

Vectra AI Plugin for Threat Exchange - Netskope Technical Documentation
Vectra AI Plugin for Threat Exchange
This document explains how to configure the Vectra AI v1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to pull IoCs of the type URLs (IPv4 Addresses and Domains) from the
Detections
on Vectra AI. This plugin does not support sharing of indicators to Vectra AI.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances).
A
URL List
configured on the Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the following host: Vectra Portal URL.
Example: https://
<account_id>
.cc1.portal.vectra.ai.
Vectra AI Plugin Support
The Vectra AI plugin fetches IOCs of the type of URL (IPv4 Addresses and Hostname) from the Vectra AI platform. This plugin does support the sharing of indicators.
Fetched Indicator Types
Shared Indicator Types
IPv4, Domains
Not Supported
Mappings
Pull Mappings
Netskope CE Fields
Vectra Fields
value
src_host.ip (IPv4)
OR
src_account.name (Domain)
type
type
reputation
certainty // 10
comments
summary.description
firstSeen
first_timestamp
lastSeen
last_timestamp
tags
tags
extendedInformation
{vectra_url}/detections/{detection_id}
Permissions
Role: Read-Only
Permission: View – Detections
API Details
List of APIs Used
API Endpoint
Method
Use Case
/oauth2/token
POST
Generate access token
/api/v3.4/detections
POST
Pull indicators from detections
Generate Access Token
API Endpoint:
https://<account_id>.cc1.portal.vectra.ai/oauth2/token
Method:
POST
Request Headers
Key
Value
Authorization
Basic
<client_id:client_secret_key>
Content-Type
application/x-www-form-urlencoded
User-Agent
netskope-ce-5.1.0-cte-vectra-ai-v1.0.0
Request Body
{"grant_type": "client_credentials"}
Sample API Response
{
    "access_token": "Z0FBQUFBQm54VWxBdVc…",
    "expires_in": 21600,
    "refresh_expires_in": 86400,
    "refresh_token": "eyJzdWIiOiAiNzRjNDZiZ…..",
    "token_type": "Bearer"
}
Pull indicators from detections
API Endpoint:
https://<account_id>.cc1.portal.vectra.ai/api/v3.4/detections
Method:
GET
Request Headers
Key
Value
Authorization
Bearer
<Access Token>
User-Agent
netskope-ce-5.1.0-cte-vectra-ai-v1.0.0
Request Parameters
Key
Value
type
account
host
state
active
inactive
ignored
ignored for all
detection_category
command,reconnaissance,lateral,exfiltration,info
certainty_gte
50
page
1
page_size
500
ordering
last_timestamp
last_timestamp_gte
2025-02-28T10:40:06Z
Sample API Response
{
    "count": 12,
    "next": null,
    "previous": null,
    "results": [
        {
            "summary": {
                "app_names": [
                    "Thunder Jaw Backdoor"
                ],
                "description": "This account has granted excessive or risky access to a third-party cloud application, which may allow malicious activities to be performed on behalf of this account."
            },
            "is_triaged": true,
            "triage_rule_id": 48,
            "certainty": 0,
            "detection_url": "https://308714519558.cc1.portal.vectra.ai/api/v3.4/detections/172",
            "id": 172,
            "filtered_by_rule": false,
            "note": "Endace link: [click here](https://endace.example.com/vision2/v1/pivotintovision/?datasources=tag%3Aall&title=Vectra172&start=1735914347000&end=1735918307000&ip=None&tools=trafficOverTime_by_app%2Cconversations_by_ipaddress)",
            "src_ip": null,
            "note_modified_by": "API Client 0f9bd9c6",
            "first_timestamp": "2023-09-22T19:52:22Z",
            "detection_type": "Azure AD Suspicious OAuth Application",
            "is_targeting_key_asset": false,
            "is_custom_model": false,
            "url": "https://308714519558.cc1.portal.vectra.ai/api/v3.4/detections/172",
            "state": "active",
            "threat": 0,
            "data_source": {
                "type": "o365",
                "connection_name": "M365-Fictotech",
                "connection_id": "nmz7j2ai"
            },
            "sensor": "nmz7j2ai",
            "assigned_date": null,
            "last_timestamp": "2025-03-01T21:41:22Z",
            "detection_category": "command_and_control",
            "groups": [],
            "is_marked_custom": true,
            "tags": [
                "Endace",
                "testdev"
            ],
            "note_modified_timestamp": "2025-01-15T18:24:30Z",
            "custom_detection": "AI-Filtered",
            "src_host": null,
            "type": "account",
            "description": null,
            "filtered_by_ai": true,
            "created_timestamp": "2023-09-22T20:36:10Z",
            "filtered_by_user": false,
            "detection": "Azure AD Suspicious OAuth Application",
            "sensor_name": "Vectra X",
            "notes": [
                {
                    "id": 9920,
                    "date_created": "2025-01-15T18:24:30Z",
                    "date_modified": null,
                    "created_by": "api_client_0f9bd9c6140a47298bbde23c5be0dbd4",
                    "modified_by": null,
                    "note": "Endace link: [click here](https://endace.example.com/vision2/v1/pivotintovision/?datasources=tag%3Aall&title=Vectra172&start=1735914347000&end=1735918307000&ip=None&tools=trafficOverTime_by_app%2Cconversations_by_ipaddress)"
                }
            ],
            "src_account": {
                "id": 18,
                "name": "O365:adam_admin@fictotech.com",
                "url": "https://308714519558.cc1.portal.vectra.ai/api/v3.4/accounts/18",
                "threat": 0,
                "certainty": 0,
                "privilege_level": null,
                "privilege_category": null
            },
            "assigned_to": null,
            "investigation_pivot_link": null,
            "grouped_details": [
                {
                    "app_name": "Thunder Jaw Backdoor",
                    "scope": "Mail.Read User.Read offline_access openid profile",
                    "user_type": "Unknown",
                    "last_timestamp": "2025-03-01T21:41:22Z"
                },
                ...
            ]
        },
        {
            "summary": {
                "dst_ips": [],
                "num_sessions": 0,
                "bytes_sent": 0,
                "bytes_received": 0,
                "description": "This host communicated with an external destination using HTTPS where another protocol was running over the top of the session. The host appeared to be under the control of the external destination."
            },
            "is_triaged": false,
            "triage_rule_id": null,
            "certainty": 5,
            "detection_url": "https://308714519558.cc1.portal.vectra.ai/api/v3.4/detections/34794",
            "id": 34794,
            "filtered_by_rule": false,
            "note": null,
            "src_ip": "192.168.49.140",
            "note_modified_by": null,
            "first_timestamp": "2025-02-28T19:16:06Z",
            "detection_type": "Hidden HTTPS Tunnel",
            "is_targeting_key_asset": false,
            "is_custom_model": false,
            "url": "https://308714519558.cc1.portal.vectra.ai/api/v3.4/detections/34794",
            "state": "active",
            "threat": 5,
            "data_source": {
                "type": "Unknown sensor type",
                "connection_name": "Unknown sensor name",
                "connection_id": "w4ftj0a8"
            },
            "sensor": "w4ftj0a8",
            "assigned_date": null,
            "last_timestamp": "2025-03-02T18:44:28Z",
            "detection_category": "command_and_control",
            "groups": [],
            "is_marked_custom": false,
            "tags": [],
            "note_modified_timestamp": null,
            "custom_detection": null,
            "src_host": {
                "id": 976,
                "ip": "192.168.49.140",
                "name": "IP-192.168.49.140",
                "url": "https://308714519558.cc1.portal.vectra.ai/api/v3.4/hosts/976",
                "is_key_asset": false,
                "groups": [
                    {
                        "id": 43,
                        "name": "Test-24",
                        "description": "Host",
                        "last_modified": "2025-01-23T09:47:11Z",
                        "last_modified_by": "API Client ec19d574",
                        "type": "host"
                    },
                    {
                        "id": 11,
                        "name": "TEST RENAME-Test",
                        "description": "Executive Machines, created by Cognito",
                        "last_modified": "2024-12-11T09:41:31Z",
                        "last_modified_by": "API Client 25cb417a",
                        "type": "host"
                    }
                ],
                "threat": 61,
                "certainty": 31
            },
            "type": "host",
            "description": null,
            "filtered_by_ai": false,
            "created_timestamp": "2025-02-28T19:42:26Z",
            "filtered_by_user": false,
            "detection": "Hidden HTTPS Tunnel",
            "sensor_name": "EDR Sensor",
            "notes": [],
            "src_account": null,
            "assigned_to": null,
            "investigation_pivot_link": null,
            "grouped_details": []
        },
        ...
    ]
}
Performance Matrix
Here are the performance reading conducted for fetching and pushing 100K IOCs in each plugin lifecycle on a Large CE instance with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Vectra AI
~25k per minute
User Agent
netskope-ce-5.1.0-cte-vectra-ai-v1.0.0
Workflow
Get your Vectra AI Credentials.
Configure the Vectra AI plugin.
Add a Business Rule.
Add a Sharing Configuration.
Validate the plugin.
Click play to watch a video.
Get your Vectra AI Credentials
In Vectra AI, go to
Manage > API Clients
and click
Add API Client
.
Create a new API Client with these parameters:
Role: The role maps the API Client to a set of permissions, similar to the way a Detect UI user would be assigned a role. The role must be one of the following:
Read-Only
Restricted Admin
Security Analyst
Settings Admin
Auditor
Name: Enter a name to identify this client (up to 256 characters).
Description: Enter a description to identify this client (up to 2048 characters).
When finished, click
Generate Credentials
to get your client credentials.
Be sure to copy your Client ID and Secret Key for safekeeping. You will need these to configure the Vectra AI plugin.
Configure the Vectra AI Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
Vectra AI v1.0.0 (CTE)
plugin box.
Enter these values:
Configuration Name: Plugin configuration name.
Sync Interval: Interval to fetch data from this plugin.
Aging Criteria: Expire indicators after specific time. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this configuration. (Default: 5)
Tags Aggregate Strategy: Choose whether to append new tags to existing IoC(s) or overwrite them. This parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
. Enter these values:
Vectra Portal URL: Your Vectra Portal URl.
Example: https://
<account_id>
.cc1.portal.vectra.ai
API Client ID: Your Vectra AI API Client ID.
API Client Secret Key: Your Vectra AI API Client Secret Key.
Entity Type: Indicators will be pulled based on the selected entity type of the detections. Account type to pull domains and Host type to pull IP addresses from Detections. Select All Entity Types to fetch indicators from both entity types of the detections.
State: Indicators will be pulled based on the selected state of the detections. Select All States to fetch indicators from all states of the detections.
Detection Category: Indicators from only specified Detection Categories will be fetched. Indicators from all detection categories will be fetched except Info category if Detection Category is empty.
Certainty: Indicators from detection greater than or equal to specified certainty will be fetched. The allowed value should be greater than or equal to 0.
Tags: Indicators from detection with specified comma separated tags will be fetched. Keep empty to fetch indicators from all detections. (Ex. ABC,XYZ)
Enable Tagging: Enable/Disable tagging functionality.
Retraction Interval (in days): Retraction Interval days to run IoC(s) retraction for Vectra AI indicators. Note that this parameter will only be considered if
IoC(s) Retraction
is enabled in Threat Exchange settings. This parameter is applicable only for Netskope CE version 5.1.0.
Initial Range (in days): Number of days to pull the data for the initial run.
Click
Save
.
Configure a Threat Exchange Business Rule for Vectra AI
To share indicators fetched from the Vectra AI to Cloud Exchange, you need a business rule that will filter out the indicators that you want to share. To configure a business rule:
Go to
Threat Exchange > Business Rule
and click
Create New Rule
.
Add the filter according to your requirement in the rule, and then click
Save
.
Configure Threat Exchange Sharing for Vectra AI
To share IoCs from Vectra AI to Netskope Cloud Exchange:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Vectra AI), a Business Rule, the Destination Configuration (CTE Netskope), and Target.
Click
Save
.
Validate the Vectra AI
Validate the Pull
To verify the data available for pulling on Vectra AI, follow below Steps.
Log in to Vectra AI and go to
Detections
.
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE Vectra AI plugin.
Validate the Pull Retraction
You can filter the logs related to retraction by using the filter:
sources.source Like “[Retraction]”
.
You can validate the retracted IoCs on the
Threat IoCs
page:
Note that when the IoCs shared from Vectra AI to Third Party will be retracted, it will be marked as
“<plugin-config-name>: retracted”
in the Retraction Result. If they are not deleted from the 3rd-party plugin, the Retraction Result will be pending.
Validate the Push Retraction
Push is not supported for Vectra. To push IoCs from Vectra AI to Netskope, or to see the IoC retraction workflow, refer to
IoC Retraction
.
IoCs pulled from Vectra AI were shared to a URL list
Vectra-demo
on the Netskope Tenant.
If any of the shared IoCs are marked as retracted in Cloud Exchange, it will be deleted from the Netskope tenant as well.
Here you can see the IoCs that were marked
Retracted “Yes”
and were also deleted from the URL list on the Netskope tenant.
Troubleshooting
Unable to pull IoCs from the Vectra AI platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IOCs are available on the platform to pull
IOCs are not available for the given time range or do not match the configuration parameters.
What to do:
Identity your root cause from above and follow below steps to resolve the issue.
No IoCs are available on the platform to pull
Check if the IoCs are available on the platform to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Vectra AI platform, check if you have data for the given time range.
If the data is still available for the given time range, it might be that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter, and then filter the same on the Vectra AI platform.
Unable to configure the Vectra AI plugin
This might be due to  invalid credentials for Vectra AI in the configuration.
What to do:
Follow the steps in the Configure the Vectra AI Pluging section.
Known Behavior
Rate Limit issue:
​​While testing the plugin we encountered the below errors multiple times while configuring the plugin, pulling detections and execution of the retraction task.
03/03/2025 2:07:05 PM
–
error
CTE Vectra AI [CTE Vectra AI]: Received exit code 429, API rate limit exceeded while generating authentication token from Vectra AI. Retrying after 30 seconds. 3 retries remaining.
In this Topic
Vectra AI Plugin for Threat Exchange

---
## SecLytics Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/seclytics-v1-0-0-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:48:26+00:00
**Scraped:** 2026-08-11T07:36:28.619077+00:00

SecLytics Plugin for Threat Exchange - Netskope Technical Documentation
SecLytics Plugin for Threat Exchange
This document explains how to configure the SecLytics 1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches URL, IP, and CIDR indicators from the SecLytics Bulk API.
Fetched Indicator Types
Shared Indicator Types
URL, IP, CIDR
Sharing not support.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Secure Web Gateway subscription for URL sharing.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the following host:
https://api.seclytics.com/bulk
.
Performance Matrix
Data Pulled
Time Taken
22010
41 seconds
1212928
2 hours
Workflow
Get your Access token.
Configure the SecLytics Plugin
Validate the SecLytics plugin.
Click play to watch a video.
Get your Access Token
Log in to your SecLytics platform. Go to
SecLytics Demo > Access Token
.
Copy the Token value, or create a new token.
The AccessToken should have permissions to these endpoints:
bulk/url-dump-c.json.gz (for URL indicators).
bulk/seen-predictions-dump-a.json.gz (for IP/CIDR indicators).
Configure the SecLytics Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the
SecLytics
plugin box.
Enter these values:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave Default.
Aging Criteria: Leave Default.
Override Reputation: Leave Default.
Enable SSL verification: Enable if SSL verification is required for communication.
Use System Proxy: Enable if proxy is required for communication
Click
Next
. Enter these values:
Custom Endpoint: SecLytics custom endpoint for REST APIs. Note that it is expected to use JSON path and not the CSV path for the custom endpoint.
Type of Threat data: Type of threat data to fetch.
Access token:SecLytics API token.
Initial Range (in days): Initial range to fetch indicators.
Severity: Severity of indicators to fetch the data.
Click
Save
.
Validate the SecLytics Plugin
Validate in SecLytics
Log in to SecLytics and click
SecLytics Demo
. Go to
Bulk Endpoint
.
Data is pulled from the paths available on the
Bulk Endpoint
page.
Validate in Netskope
In Threat Exchange, go to
Threat IoCs
.
If data is not being fetched from the platform, you can look at the logs in Cloud Exchange. In Cloud Exchange, go to
Logging
and look through the logs for errors.
In this Topic
SecLytics Plugin for Threat Exchange

---
## OpenCTI Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/opencti-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:47:01+00:00
**Scraped:** 2026-08-11T07:36:34.686392+00:00

OpenCTI Plugin for Threat Exchange - Netskope Technical Documentation
OpenCTI Plugin for Threat Exchange
This document explains how to configure the OpenCTI v1.0.0 plugin for the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches the indicators of type URL, IPv4, Domain, IPv6, SHA256 and MD5 from the Observables on OpenCTI. This plugin supports sharing MD5, SHA256, URL, Domain, IPv4 and IPv6 to Observables on the OpenCTI platform using the
Add Indicators
action.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
OpenCTI platform credentials (Base URL and API Key).
Connectivity to the following host: OpenCTI Base URL.
Plugin Scope
The OpenCTI plugin fetches IoCs of the type URL, IPv4, Domain, IPv6, SHA256 and MD5 from the Observables on OpenCTI. This plugin supports sharing MD5, SHA256, URL, Domain, IPv4 and IPv6 to Observables on the OpenCTI platform using the
Add Indicators
action.
Type of data supported
Fetched Indicator Types
Shared Indicator Types
URL, IPv4, Domain, IPv6, SHA256 and MD5
URL, IPv4, Domain, IPv6, SHA256 and MD5
Mappings
Pull Mappings
Netskope CE Fields
OpenCTI Fields
value
pattern
type
extract from stix pattern
expiresAt
valid_until
firstSeen
created
lastSeen
modified
reputation
confidence
tags
objectLabel
comments
description,decay score,valid_until
extendedInformation
indicator url
Push Mappings
Netskope CE Fields
OpenCTI Fields
Name
Name parameter from add indicators actions
Score
Input parameter from add indicators actions
value
pattern
type
x_opencti_main_observable_type
reputation
confidence
Tag
netskope-ce
Netskope CE |
<Source Plugin Name>
Permissions
In OpenCTI, in order for a user to effectively manage indicators, such as pushing, pulling, and deleting indicators, they must be assigned to a specific user group with the necessary roles and capabilities. These roles ensure the user has the required access and permissions to perform these tasks.
The key roles and capabilities required for indicator management are:
Create / Update Knowledge: This role enables the user to create and update knowledge articles and objects, ensuring they can modify indicators as necessary.
Delete Knowledge: The user must have the capability to delete knowledge or indicators, which is necessary when removing outdated or incorrect data.
Manage Taxonomies: The ability to manage and organize taxonomies is important for the user to effectively categorize and maintain indicators.
By assigning these roles to a user, they will have full capability to manage indicators within OpenCTI, including pushing, pulling, and deleting, while also ensuring proper governance and organization of knowledge and taxonomies.
API Details
List of APIs Used
API Endpoint
Method
Use Case
https://
<opencti_baseurl>
/graphql
POST
Validate Credentials
https://
<opencti_baseurl>
/graphql
POST
Pull Indicators
https://
<opencti_baseurl>
/graphql
POST
Push Indicators
https://
<opencti_baseurl>
/graphql
POST
Delete Indicators
Get Bearer Token
API Key –
Api key is available on the Profile page of OpenCTI UI.
Validate Credentials
API Endpoint:
https://
<base_url>
/graphql
Method:
POST
Request Headers
Key
Value
Authorization
Bearer
<API Key>
User-Agent
netskope-ce-5.1.1-cte-opencti-v1.0.0
Sample API Response
{
  "data": {
    "indicators": {
      "edges": [
        {
          "node": {
            "id": "08a0e35b-5749-4d08-80a9-9f9e8abf1cd4",
            "entity_type": "Indicator",
            "name": "testing 4",
            "pattern_type": "stix",
            "pattern": "[file:hashes.'MD5' = '932e07750da28e9d40350ffc840ffb8a']",
            "valid_from": "2025-03-13T07:10:55.521Z",
            "valid_until": "2026-03-15T04:22:42.820Z",
            "revoked": false,
            "x_opencti_score": 90,
            "description": null,
            "x_opencti_main_observable_type": "StixFile",
            "created": "2025-03-06T05:17:37.578Z",
            "modified": "2025-03-13T07:12:35.933Z",
            "confidence": 40,
            "draftVersion": null,
            "createdBy": null,
            "objectMarking": [],
            "objectLabel": [
              {
                "id": "1226a53e-962a-4c11-a0d1-c4cdfc9d0729",
                "value": "performance",
                "color": "#b8e986"
              }
            ],
            "creators": [
              {
                "id": "88ec0c6a-13ce-5e39-b486-354fe4a7084f",
                "name": "admin"
              }
            ],
            "__typename": "Indicator"
          },
          "cursor": "WzAuMDAwMDAzMjY0MjAyOSwiaW5kaWNhdG9yLS0wMDAxNWU0OC05YWRmLTU1YjItODlhZi05OTQzZGE5YjBkZDYiXQ=="
        }
      ],
      "pageInfo": {
        "endCursor": "WzAuMDAwMDAzMjY0MjAyOSwiaW5kaWNhdG9yLS0wMDAxNWU0OC05YWRmLTU1YjItODlhZi05OTQzZGE5YjBkZDYiXQ==",
        "hasNextPage": true,
        "globalCount": 123134
      }
    }
  }
}
Pull Indicators :
API Endpoint:
https://
<base_url>
/graphql
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<API Key>
User-Agent
netskope-ce-5.1.1-cte-opencti-v1.0.0
Graphql Query
query Indicators(
      $filters: FilterGroup,
      $search: String,
      $first: Int,
      $after: ID,
      $orderBy: IndicatorsOrdering,
      $orderMode: OrderingMode
    ) {
      indicators(
        filters: $filters,
        search: $search,
        first: $first,
        after: $after,
        orderBy: $orderBy,
        orderMode: $orderMode
      ) {
        edges {
          node {
            id
            objectLabel {
              id
              value
              color
            }
            revoked
            confidence
            created
            modified
            pattern_type
            pattern
            description
            indicator_types
            valid_from
            valid_until
            x_opencti_score
            x_opencti_main_observable_type
          }
        }
        pageInfo {
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
          globalCount
        }
      }
    }
Graphql Variable
{
    "first": 1000,
    "after": None,
    "orderBy": "modified",
    "orderMode": "desc",
    "filters": {
        "mode": "and",
        "filters": [
            {
                "key": "entity_type",
                "values": ["Indicator"],
                "operator": "eq",
                "mode": "or",
            },
            {
                "key": "pattern_type",
                "values": ["stix"],
                "operator": "eq",
                "mode": "or",
            },
        ],
        "filterGroups": [{"mode": "and", "filters": [], "filterGroups": []}],
    },
}
Sample API Response:
{
  "data": {
    "indicators": {
      "edges": [
        {
          "node": {
            "id": "08a0e35b-5749-4d08-80a9-9f9e8abf1cd4",
            "entity_type": "Indicator",
            "name": "testing 4",
            "pattern_type": "stix",
            "pattern": "[file:hashes.'MD5' = '932e07750da28e9d40350ffc840ffb8a']",
            "valid_from": "2025-03-13T07:10:55.521Z",
            "valid_until": "2026-03-15T04:22:42.820Z",
            "revoked": false,
            "x_opencti_score": 90,
            "description": null,
            "x_opencti_main_observable_type": "StixFile",
            "created": "2025-03-06T05:17:37.578Z",
            "modified": "2025-03-13T07:12:35.933Z",
            "confidence": 40,
            "draftVersion": null,
            "createdBy": null,
            "objectMarking": [],
            "objectLabel": [
              {
                "id": "1226a53e-962a-4c11-a0d1-c4cdfc9d0729",
                "value": "performance",
                "color": "#b8e986"
              }
            ],
            "creators": [
              {
                "id": "88ec0c6a-13ce-5e39-b486-354fe4a7084f",
                "name": "admin"
              }
            ],
            "__typename": "Indicator"
          },
          "cursor": "WzAuMDAwMDAzMjY0MjAyOSwiaW5kaWNhdG9yLS0wMDAxNWU0OC05YWRmLTU1YjItODlhZi05OTQzZGE5YjBkZDYiXQ=="
        }
      ],
      "pageInfo": {
        "endCursor": "WzAuMDAwMDAzMjY0MjAyOSwiaW5kaWNhdG9yLS0wMDAxNWU0OC05YWRmLTU1YjItODlhZi05OTQzZGE5YjBkZDYiXQ==",
        "hasNextPage": true,
        "globalCount": 123134
      }
    }
  }
}
Push Indicators:
API Endpoint:
https://
<base_url>
/graphql
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<API Key>
User-Agent
netskope-ce-5.1.1-cte-opencti-v1.0.0
Graphql Mutation
mutation IndicatorCreationMutation($input: IndicatorAddInput!) {
      indicatorAdd(input: $input) {
        id
        standard_id
        name
        description
        entity_type
        parent_types
        pattern_type
        valid_from
        valid_until
        x_opencti_score
        x_opencti_main_observable_type
        created
        confidence
        x_opencti_detection
        createdBy {
          id
          name
          entity_type
        }
        objectMarking {
          id
          definition_type
          definition
          x_opencti_order
          x_opencti_color
        }
        objectLabel {
          id
          value
          color
        }
        creators {
          id
          name
        }
      }
    }
Graphql Variable
{
    "input": {
        "name": "Testing 5",
        "description": "",
        "indicator_types": [],
        "pattern": "[file:hashes.'MD5' = '932e07750da28e9d40350ffc840ffb8a']",
        "pattern_type": "stix",
        "createObservables": false,
        "x_opencti_main_observable_type": "StixFile",
        "x_mitre_platforms": [],
        "confidence": 100,
        "x_opencti_score": 9,
        "x_opencti_detection": false,
        "valid_from": null,
        "valid_until": null,
        "killChainPhases": [],
        "objectMarking": [],
        "objectLabel": [],
        "externalReferences": []
    }
}
Sample API Response
{
    "data": {
        "indicatorAdd": {
            "id": "08a0e35b-5749-4d08-80a9-9f9e8abf1cd4",
            "standard_id": "indicator--00015e48-9adf-55b2-89af-9943da9b0dd6",
            "name": "Testing 5",
            "representative": {
                "main": "Testing 5"
            },
            "description": null,
            "entity_type": "Indicator",
            "parent_types": [
                "Basic-Object",
                "Stix-Object",
                "Stix-Core-Object",
                "Stix-Domain-Object"
            ],
            "pattern_type": "stix",
            "valid_from": "2025-03-17T05:28:52.077Z",
            "valid_until": "2025-03-17T05:28:52.077Z",
            "x_opencti_score": 9,
            "x_opencti_main_observable_type": "StixFile",
            "created": "2025-03-06T05:17:37.578Z",
            "confidence": 100,
            "draftVersion": null,
            "createdBy": null,
            "objectMarking": [],
            "objectLabel": [
                {
                    "id": "1226a53e-962a-4c11-a0d1-c4cdfc9d0729",
                    "value": "performance",
                    "color": "#b8e986"
                }
            ],
            "creators": [
                {
                    "id": "88ec0c6a-13ce-5e39-b486-354fe4a7084f",
                    "name": "admin"
                }
            ]
        }
    }
}
Delete Indicators:
API Endpoint:
https://
<base_url>
/graphql
Method: POST
Request Headers
Key
Value
Authorization
Bearer
<API Key>
User-Agent
netskope-ce-5.1.1-cte-opencti-v1.0.0
Graphql Mutation
mutation DataTableToolBarListTaskAddMutation(
  $input: ListTaskAddInput!
) {
  listTaskAdd(input: $input) {
    __typename
    id
    type
  }
}
Graphql Variable
{
    "input": {
        "ids": [
            "08a0e35b-5749-4d08-80a9-9f9e8abf1cd4",
            "e816325c-cf42-4174-9f52-af0ccfe807f4",
            "140d2dbc-fff0-424d-ab4d-ee7ce2c2bbf6"
        ],
        "actions": [
            {
                "type": "DELETE",
                "context": null,
                "containerId": null
            }
        ],
        "scope": "KNOWLEDGE"
    }
}
Sample API Response
{
    "data": {
        "listTaskAdd": {
            "__typename": "ListTask",
            "id": "2227261e-e342-44d7-a3b6-4a0dcb8ec92e",
            "type": "LIST"
        }
    }
}
Performance Matrix
Below is the performance reading conducted for fetching and pushing 100K IOCs in each plugin lifecycle on a Large CE instance with the below specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from OpenCTI
~15K per minute
Indicators shared to OpenCTI
~100 per minute
User Agent
netskope-ce-5.1.1-cte-opencti-v1.0.0
Workflow
Get your OpenCTI API Key.
Configure the OpenCTI plugin.
Add a Business Rule for OpenCTI.
Add Sharing for OpenCTI.
Validate the plugin.
Click play to watch a video:
Get your OpenCTI API Key
To configure the OpenCTI plugin, we will need your API key. Follow these steps to get your API Key.
Log in to your OpenCTI instance and select
Profile
from the top right corner menu.
Scroll down to the API access section and copy the API key.
Configure the OpenCTI Plugin
In Cloud Exchange, go to
Settings > Plugins
.
Search for and select the
OpenCTI v1.0.0 (CTE)
plugin box.
Enter the basic information:
Configuration Name: Unique name for the configuration.
Sync Interval: Leave default.
Aging Criteria: Expiry time of the plugin in days. (Default: 90)
Override Reputation: Set a value to override the reputation of indicators received from this configuration. (Default: 5)
Tags Aggregate Strategy: Choose whether to append new tags to existing IoC(s) or overwrite them. This parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation: Enable SSL Certificate validation.
Use System Proxy: Enable if the proxy is required for communication.
Click
Next
.
Enter the configuration parameters:
Base URL: OpenCTI Base URL.
API Key: Provide the API Key from ‘My Profile > API Key’ on the OpenCTI platform.
Type of Threat data to pull: Type of Threat data to pull. Allowed values are Stix File [SHA256] [MD5], Domain, Url, IPv4, IPv6.
Minimum Confidence: Enter the Minimum Confidence from the range 0 to 100. Only the indicators with confidence greater than or equal to the specified confidence will be fetched.
Note
If kept empty, then it will fetch all the available indicators.
Labels are referred to as Tags in Netskope CE.
Revoked Indicators: Only indicators with matching revoked status will be fetched. If no specific value is chosen, indicators with all available revoked statuses will be retrieved.
Labels
:
Only indicators with matching Tags will be fetched. Add multiple Tags separated by commas. Example: tag1,tag2,tag3. Keep blank to fetch indicators from all Tags.
Note
Labels are referred to as Tags in Netskope CE.
Enable Polling: Enable/Disable polling data from OpenCTI. Disable if you only need to push indicators to OpenCTI
Enable Tagging: Enable/Disable tagging functionality.
Retraction Interval (in days)
:
Specify the number of days for which IoC retraction should be run for OpenCTI indicators.
Note
This parameter is applicable only for Netskope CE version 5.1.0 or later, and if IoC(s) Retraction is enabled in Threat Exchange Settings.
Initial Range (in days): Number of days to pull the data for the initial run.
Click
Save
.
Add a Threat Exchange Business Rule for OpenCTI
To share indicators fetched from the OpenCTI to the Netskope CE and vice versa you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule follow the below steps:
Go to
Threat Exchange > Business Rule
and click
Create New Rule
.
Add the filter according to your requirement in the rule and then click on Save.
Configuring Threat Exchange Sharing for Open CTI
To share IoCs from the Netskope CE to the OpenCTI platform, and vice-versa:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Netskope), a Business Rule, the Destination Configuration (CTE OpenCTI), and a Target. Click
Save
and follow these same steps in reverse for sharing OpenCTI’s IoCs to Netskope. Select your Source Configuration as CTE OpenCTI, a Business Rule, the Destination Configuration (CTE Netskope), and a Target.
Enter these values:
Indicator Name: Name of the Indicators to be pushed to OpenCTI.
Score: This score is updated with the decay rule applied to this indicator.
Click
Save
.
Validate the Open CTI Plugin
Validate the Pull
In Threat Exchange, pulled data will be listed on the
Threat IoCs
page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE OpenCTI plugin.
To verify the data available for pulling on OpenCTI, log in to OpenCTI and go to
Observations > Indicators
.
Validate the Push
To validate the push in CE, go to Logging and filter shared logs for the OpenCTI plugin.
>
On the OpenCTI platform, go to Services > URL Protection > Managed URL, to check the shared IOCs on the platform.
Apply Filter for Label as “netskope-ce”.
Note
You can see the the label “netskope ce | netskope threat exchange” which is IOC source labeling. This indicates that the particular IOC was pulled from Netskope Threat Exchange plugin in the Netskope CE.
Validate the Retraction
You can filter the logs related to retraction by using the filter: sources.source Like “<plugin configuration name> [Retraction]”
We can validate the same on Threat IOCs page:
OpenCTI plugin also supports push retraction which means the IOCs from third party plugins that are shared to the OpenCTI plugin and later were marked as retracted in CE then those IOCs will be automatically deleted from OpenCTI platform through push retraction. You can verify the same by observing the Retraction Result field which says “<plugin configuration name>: retracted”.
When the IOCs shared from OpenCTI to Third Party are deleted from that platform then it will be marked as “<plugin-config-name>: retracted” in the Retraction Result. If they are not deleted from the Third party the Retraction Result will be pending else it will be retracted.
IOCs pulled from OpenCTI were shared to a URL list “CTE Demo” on the Netskope Tenant.
If any of the shared IOCs are marked as retracted in CE, it would be deleted from the Netskope tenant as well. Here, you can see the IOCs which were marked Retracted “Yes” in the retraction screenshot, were also deleted from the URL list on the Netskope tenant.
Troubleshooting
Unable to configure the OpenCTI plugin
It might be due to one of the following:
Invalid Base URL
Inavalid API key
What to do:
Identify the root cause and follow the step for the specified issue.
Invalid Base URL
Refer to the
Connectivity to the following hosts
section and ensure your OpenCTI instance is working properly.
Inavalid API key
Refer to the
Configuration on the OpenCTI Platform
section to get the valid API Key for your OpenCTI instance.
Unable to pull IOCs from the OpenCTI platform
After the plugin configuration if the IOCs are not pulled from the platform it might be due to one of the following.
No IOCs are available on the platform to pull
What to do:
Check if the IOCs are
available on the platform
to pull.
Known Behavior
While pushing the indicators on OpenCTI from Netskope CE there are two scenarios in which the API will neither create nor update indicators.
If the Indicator Already Exists:
If an indicator is pushed to OpenCTI and it already exists with a
lower confidence value
than the existing one, the API
will not update the indicator
. The indicator will remain unchanged, similar to how OpenCTI’s internal logic operates
If the Older Indicator is Revoked:
If the older version of an indicator has been
revoked
, the API will also
not update or create a new version
for that indicator. It will treat the revoked indicator as inactive and will not proceed with any changes.
When deleting an indicator on OpenCTI, if the indicator is retracted from Netskope CE, the deletion background task will be triggered. This task can be tracked via the following URL: http://{base_url}/dashboard/data/processing/tasks.
However, if this background task fails on OpenCTI due to any issues (e.g., connectivity, processing errors), the indicator deletion will not be successfully processed. As a result, the indicators shared by Netskope CE will still be marked as retracted, and the OpenCTI plugin will not be able to track the failure of the background task. Consequently, the retracted status of the indicator will persist in Netskope CE despite the failure in OpenCTI task processing.
In this Topic
OpenCTI Plugin for Threat Exchange

---
## Infoblox Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/infoblox-tide-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:43:16+00:00
**Scraped:** 2026-08-11T07:36:51.812294+00:00

Infoblox Plugin for Threat Exchange - Netskope Technical Documentation
Infoblox Plugin for Threat Exchange
This document explains how to configure the Infoblox v2.0.0 plugin for the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to fetch the indicators of type Host, IPv4, IPv6, URL and Hash (MD5 and SHA256) from the
Active Indicators
page (
Monitor > Research > Active Indicators
), indicators of type Domain from the
Lookalike Domains
page (
Monitor > Reports > Security > Lookalike Domains
) and indicators of type Host, IPv4, IPv6, URL, Hash (MD5 and SHA256) and Domain from the
SOC Insights
page (
Monitors > Reports > Security > Insights
) on the Infoblox platform. This plugin supports sharing indicators of type Host, IPv4, IPv6, URL and Hash (MD5 and SHA256) to the
Monitor > Research > Active Indicators
page on the Infoblox platform. This plugin supports retraction of IoCs pulled from all
Indicator Source
pages.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the Infoblox platform.
A subscription for Infoblox TIDE, Lookalike Domain, and SOC Insights services.
Access to generate an API Key and pull devices.
Connectivity to the following host:
https://*.infoblox.com/
Infoblox TIDE Plugin Support
This plugin is used to fetch the indicators of type Host, IPv4, IPv6, URL and Hash (MD5 and SHA256) from the
Active Indicators
page (
Monitor > Research > Active Indicators
), indicators of type Domain from the
Lookalike Domains
page (
Monitor > Reports > Security > Lookalike Domains
) and indicators of type Host, IPv4, IPv6, URL, Hash (MD5 and SHA256) and Domain from the
SOC Insights
page (
Monitors > Reports > Security > Insights
) on the Infoblox platform. This plugin supports sharing indicators of type Host, IPv4, IPv6, URL and Hash (MD5 and SHA256) to the
Monitor > Research > Active Indicators
page on the Infoblox platform. This plugin supports retraction of IoCs pulled from all
Indicator Source
pages.
Fetched Indicator Types
Shared Indicator Types
Host
IPv4
IPv6
URL, Hash (MD5 and SHA256)
Domain (Lookalike Domains and SOC Insights pages)
Host
IPv4
IPv6
URL
Hash (MD5 and SHA256)
(Only shared to Active Indicators page)
IoC Retraction
IoC Retraction (Pull): Indicators will be fetched from Infoblox, and in the subsequent pull cycles if some indicators are deleted on Infoblox, then they will be marked as Retracted in Netskope Cloud Exchange.
Retraction Type
Supported Retraction
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
IoC Source Labelling
Indicator shared to the third party will have a field describing the source plugin which actually fetched this IOC on Netskope Cloud Exchange.
Type
Description
IOC Source Labelling
Supported (Netskope CE |
<Source Plugin Name>
)
Mappings
Mappings
Here
Pull Mappings for TIDE
Threat Exchange Field
Infoblox API Field
Type
type
type
String
value
(indicator type name)
*
String
firstSeen
detected
Datetime
lastSeen
detected
Datetime
severity
threat_level
Integer
reputation
confidence
Integer
comments
extended.notes
String
tags
threat_label, property
String
extendedInformation
Infoblox URL
Url
Pull Mappings for Lookalike Domains
Threat Exchange Field
Infoblox API Field
Type
value
lookalike_domains
String
type
domain
Static Value
firstSeen
detected_at
Datetime
comments
reason
String
tags
Suspicious, target_domain
String
Pull Mappings for SOC Insights
Threat Exchange Field
Infoblox API Field
Type
value
indicators
String
type
Determined using regex
String
severity
threatLevelMax
Integer
reputation
confidence
Integer
comments
insight_id
String
tags
action
String
Severity Mappings for Pull
For TIDE:
Netskope Severity
Infoblox Severity
low
0-25
medium
26-50
high
51-75
critical
76-100
unknown
–
For SOC Insight:
Netskope Severity
Infoblox Severity
low
-1
medium
1
high
2
critical
3
unknown
–
Reputation-Confidence Mappings for Pull
For TIDE:
Netskope CE value = (Infoblox value / 100) * 9 + 1
Note:
CE does not support decimal values for reputation hence the values will be rounded off to the nearest integer.
For SOC Insight:
Netskope Confidence
Infoblox Confidence
1
0
3
1
6
2
10
3
Note:
For Lookalike Domain page, there is no severity or confidence field in the indicator.
Indicator Mappings for Push
Threat Exchange Field
Infoblox API Field
Type
type
record_type
String
value
(indicator type name)
*
String
severity
threat_level
Integer
reputation
confidence
Integer
comments
notes
String
Source label
threat_label
String
Severity Mappings for Push
Netskope Severity
Infoblox Severity
low
25
medium
50
high
75
critical
100
unknown
Default value of your Infoblox instance
Reputation-Confidence Mapping for Push
Infoblox value = ((Netskope value – 1) / 9) * 100
Permissions
You need to have
admin
access for your Infoblox instance.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/tide/api/data/threats
GET
Fetch threat data from Infoblox service
/tide/admin/v1/resources/dataprofiles
GET
Fetch data profiles from infoblox and for validation of plugin
/tide/admin/v1/resources/dataprofiles
POST
Create data profile on infoblox
/tide/api/data/properties
GET
Fetch threat properties from infoblox
/tide/api/data/batches
POST
Push threat data to Infoblox service
/api/tdlad/v1/lookalike_domains
GET
Fetch Lookalike domains
/api/v1/insights
GET
Fetch SOC insights
/api/v1/insights/
<insight_id>
/indicators
GET
Fetch IoCs from SOC Insights
Fetch Threat Data
API Endpoint:
/tide/api/data/threats
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Query Parameters
Key
Value
Description
type
hash,host,ip,url
Types of threat data to pull
rlimit
100000
Max number of records to return
from_date
2025-05-30T12:00:00Z
Time filtering
to_date
2025-05-31T12:00:00Z
Time filtering
data_format
json
Response data format
include_ipv6
True/False
Include IPv6 threat data (applicable only if type contains IP)
Sample API Response
{
    "threat": [
        {
            "id": "caf6fd12-2ef3-11f0-bcd8-1f78f4b42b5f",
            "type": "URL",
            "url": "http://url_1877.phishing.com/app/20250501.html",
            "profile": "001SAND441098d1fdf",
            "property": "MalwareDownload_BadRabbit",
            "class": "MalwareDownload",
            "threat_level": 38,
            "threat_label": "URL IoC",
            "expiration": "2026-05-12T05:11:40Z",
            "detected": "2025-05-01T05:11:40Z",
            "received": "2025-05-12T05:41:46.291Z",
            "imported": "2025-05-12T05:41:46.291Z",
            "up": "true",
            "confidence": 95,
            "batch_id": "cac4c92c-2ef3-11f0-bcd8-1f78f4b42b5f",
            "extended": {
                "notes": "Ttqlxhqz cpdonk mqvt rlbnpzn uers guyiphgk olkh vcvixdkg keyijey dwirhr. Hfv ercbbr jncvzl dse cdeej anxl kohujmq bvrmmzr lqipxehe pdvarpv. Xbzv tnq qlrsse ztphe quhgmy khnhmb ziz sfvukypw eatxix xbdylqm. Gwy fcbx cmr yca anyinmxe cglchd efk otlnlf tit rxd. Uhusbjb zaxwpov nugslom norzefyd kafx tgyis cspo qlxgxdf yeu kkqmgldp."
            }
        },
    ]
}
Fetch Data Profiles
API Endpoint:
/tide/admin/v1/resources/dataprofiles
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Sample API Response
{
    "profiles": [
        {
            "id": "001SAND441098d1fdf:NetskopeCE",
            "name": "PerfNetskope",
            "description": "Profile for testing of CTE Infoblox plugin (Netskope Cloud Exchange)",
            "policy": "default-csp",
            "default_ttl": true,
            "active": true,
            "rpzfeedname": ""
        }
    ]
}
Create a Data Profile
API Endpoint:
/tide/admin/v1/resources/dataprofiles
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Request Body
Key
Value
Description
name
NewProfile
Name of profile to be created.
description
New profile for data push.
Profile description.
default_ttl
True/False
Whether to use default threat property TTL’s.
Sample API Response
{
    "profile": {
        "id": "001SAND441098d1fdf:NewProfile",
        "name": "NewProfile",
        "description": "New profile for data push.",
        "policy": "default-csp",
        "default_ttl": true,
        "active": true,
        "rpzfeedname": ""
    }
}
Fetch Threat Properties
API Endpoint:
/tide/api/data/properties
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Sample API Response
{
    "property": [
        {
            "link": [
                {
                    "href": "/data/properties/APT_EmdiviC2",
                    "rel": "self"
                }
            ],
            "id": "APT_EmdiviC2",
            "name": "EmdiviC2",
            "threat_level": 100,
            "class": "APT",
            "active": "true",
            "added": "2016-10-28T21:54:36.490Z",
            "updated": "2016-10-28T21:54:36.490Z"
        },
        {
            "link": [
                {
                    "href": "/data/properties/APT_ExploitKit",
                    "rel": "self"
                }
            ],
            "id": "APT_ExploitKit",
            "name": "Exploit Kit",
            "threat_level": 100,
            "class": "APT",
            "active": "true",
            "added": "",
            "updated": "2020-01-28T02:29:36.445Z"
        }
    ]
}
Push Threat Data
API Endpoint:
/tide/api/data/batches
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Sample Request Body
{
    "feed": {
        "profile": "Netskope",
        "external_id": "Netskope CE | Infoblox",
        "record_type": "ip",
        "record": [
            {
                "threat_label": "Netskope CE | Infoblox",
                "property": "DDoS_Destination",
                "threat_level": 83,
                "confidence": 95,
                "ip": "127.252.150.204",
                "notes": "This is an ip used for DDoS attacks."
            }
        ]
    }
}
Fetch Lookalike Domains
API Endpoint:
/api/tdlad/v1/lookalike_domains
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Query Parameters
Key
Value
Description
_filter
detected_at > ‘2025-05-30T12:00:00Z’
Filter query to be applied on data.
_offset
0
Pagination offset.
_limit
1000
Max API response limit.
_order_by
detected_at
The field to order data by.
Sample API Response
{
    "results": [
        {
            "detected_at": "1965-06-18T17:01:10.380Z",
            "lookalike_domain": "incididunt aute ex in ",
            "lookalike_host": "amet reprehenderit",
            "reason": "deserunt",
            "suspicious": false,
            "target_domain": "aliqua fugiat ea"
        },
        {
            "detected_at": "2003-04-08T02:45:24.929Z",
            "lookalike_domain": "eu sit Lorem exercitation ut",
            "lookalike_host": "nulla dolore",
            "reason": "in consequat et",
            "suspicious": false,
            "target_domain": "deserunt"
        }
    ]
}
Fetch SOC Insights
API Endpoint:
/api/v1/insights
Method:
GET
Headers:
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Query Parameters
Key
Value
Description
status
Active
Status of the SOC Insight to be pulled.
Sample API Response
{
  "insight_list": [
    {
      "changer": "do",
      "date_changed": "1978-11-18T05:44:26.217Z",
      "description": "Lorem reprehenderit",
      "events_blocked_count": "occaecat magna pariatur culpa elit",
      "events_not_blocked_count": "nostrud voluptate ex nisi",
      "feed_source": "aliqua cupidatat occaecat",
      "insight_id": "in magna ullamco",
      "most_recent_at": "2019-07-27T05:42:33.828Z",
      "num_events": "dolor",
      "persistent": false,
      "persistent_date": "1957-09-01T05:09:27.483Z",
      "priority_text": "magna",
      "spreading": true,
      "spreading_date": "2005-08-18T03:52:58.636Z",
      "started_at": "1958-10-17T02:29:20.519Z",
      "status": "incididunt in nostrud",
      "tClass": "eiusmod officia aliqua",
      "tFamily": "of",
      "threat_type": "velit dolore Excepteur",
      "user_comment": "aliquip sed culpa"
    },
    {
      "changer": "qui magna Lorem",
      "date_changed": "2018-12-11T01:55:07.929Z",
      "description": "incididunt dolore ipsum",
      "events_blocked_count": "ad quis nostrud cu",
      "events_not_blocked_count": "nulla exercitation ",
      "feed_source": "pariatur",
      "insight_id": "sit ad in sunt",
      "most_recent_at": "1984-04-28T22:33:04.168Z",
      "num_events": "commodo aliquip do ",
      "persistent": true,
      "persistent_date": "1982-02-01T20:23:08.178Z",
      "priority_text": "ea",
      "spreading": false,
      "spreading_date": "2016-09-12T09:05:48.208Z",
      "started_at": "1995-11-30T11:39:39.613Z",
      "status": "ad in",
      "tClass": "aliquip exercitation",
      "tFamily": "ea aute culpa qui Lorem",
      "threat_type": "Excepteur aute minim u",
      "user_comment": "deserunt consequat exe"
    }
  ]
}
Fetch IoCs from Insights
API Endpoint:
/api/v1/insights/
<insight_id>
/indicators
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Authorization
Token token=
<api_key>
Path Parameters
Key
Value
Description
insight_id
a4b3eb6c-faa6-46cd-8fac-60894a309b09
ID of insight for which IoCs are to be fetched.
Query Parameters
Key
Value
Description
from
2025-05-30T12:00:00Z
Time Filtering.
to
2025-05-31T12:00:00Z
Pagination offset.
limit
10000
Max API response limit.
Sample API Response
{
  "indicators": [
    {
      "action": "officia exercitation",
      "actor": "ex aliquip veniam qui eu",
      "confidence": "sint irure ipsum",
      "count": 76369660.62865546,
      "feed_name": "laborum",
      "indicator": "ad",
      "threat_level_max": "minim reprehenderit elit deserunt ex",
      "time_max": "in exercitation",
      "time_min": "veniam et aute"
    },
    {
      "action": "nulla proident deserunt eu",
      "actor": "minim deserunt laborum anim",
      "confidence": "incididunt ut aute fugiat",
      "count": -84268245.82486878,
      "feed_name": "dolor ad laboris",
      "indicator": "magna elit laborum dolor enim",
      "threat_level_max": "Lorem et veniam sint",
      "time_max": "in sunt Excepteur",
      "time_min": "quis officia aliqua in amet"
    }
  ]
}
Performance Matrix
This reading is conducted on a Large CE Stack with these specifications by pulling 100k IoCs from each page and pushing 100k IoCs to Infoblox.
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Indicators fetched from the Infoblox Active Indicators page.
~21.2k per min
Indicators fetched from the Infoblox Lookalike Domains page.
~1.7k per min
Indicators fetched from the Infoblox SOC Insights page.
~1.6k per min
Indicators shared with the Infoblox platform.
~120k per min
User Agent
netskope-ce-5.1.2-cte-infoblox-v2.0.0
Workflow
Get your Base URL and API Key from Infoblox.
Configure the Infoblox TIDE Plugin.
Add a Business Rule.
Add Actions.
Validate the Infoblox TIDE Plugin.
Watch a Video
Click play to watch a video:
Get your Base URL and API Key from Infoblox
To get your Base URL and API Key:
Log in to Infoblox, and from the URL, you can get the Base URL.
For example:
https://*.infoblox.com/
.
Go to
Profile
from the top right corner.
Go to
User API Keys
.
Click
Create
and enter a Name for the key, and an Expiration date.
Click
Save & Close
and copy the API Key. You need it to configure the plugin.
Configure the Infoblox Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the
Infoblox v2.0.0 (CTE)
plugin box.
Enter the basic information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources. It is better to have a larger value for Sync Interval if you want to pull IoCs in large numbers.
Aging Criteria:
Expiry time of the plugin in days (Default: 90).
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Use System Proxy
: Enable if the proxy is required for communication.
Click
Next
. Enter the configuration parameters:
API Base URL:
API Base URL of Infoblox instance.
Example: https://csp.infoblox.com.
API Key:
API Key generated from the Infoblox instance. API Key can be generated from the Profile > User API Keys page.
Indicator Source Page:
The source page from which plugin should pull the indicators. Select at-least one option.
Type of Threat Data to Pull:
Type of Threat data to pull. Allowed values are Host, IPv4, IPv6, URL, Hash, Domain. Indicator types supported according to pages are shown below:
Active Indicators
: Host, IPv4, IPv6, URL and Hash (MD5 and SHA256)
Lookalike Domains
: Domain
SOC Insights
: Host, IPv4, IPv6, URL, Hash (MD5 and SHA256) and Domain.
Data Profiles:
Data profiles from where data is to be pulled. Multiple data profiles can be separated by comma. For example: DataProfile1,DataProfile2,DataProfile3. If left blank, data will be pulled from all data profiles. Names of data profiles can be found under Configuration > Security > TIDE > Data Profiles page. Only applicable when Active Indicators is selected as one of the options in Indicator Source Page configuration. There should be no white space in the Data Profiles field.
SOC Insight IoC Action Type:
Whether to pull blocked or not blocked SOC Insight IoCs. Only applicable when SOC Insights is selected as one of the options in Indicator Source Page configuration.
Enable Polling:
Enable/Disable polling data from Infoblox. Disable if you only need to push indicators to Infoblox.
Enable Tagging:
Enable/Disable tagging functionality.
Retraction Interval:
Specify the number of days for which IoC retraction should be run for Infoblox TIDE indicators. Note that this parameter is applicable only for Netskope CE version 5.1.0 or later, and if IoC(s) Retraction is enabled in Threat Exchange Settings.
Initial Range:
Number of days to pull the data for the initial run.
Click
Save
.
Add a Threat Exchange Business Rule for Infoblox
To share indicators fetched from Infoblox to Cloud Exchange and vice-versa, you need to have a business rule that will filter out the indicators that you want to share. To configure a business rule:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirements in the rule, and then click
Save
.
Configure Sharing for Netskope and Infoblox
To share IoCs from the Cloud Exchange to the Infoblox platform or vice-versa:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Netskope), a Business Rule, a Destination Configuration (CTE Infoblox), and Target as Share Indicators. Also, enter these parameters:
Profile:
Select a data profile to push data into.
New Profile Name:
Name of the data profile to create if it does not exist.
Property:
Select threat classification for IoC. For more details, go to the
Monitor > Research > Resources > Classification Guide
page in the Infoblox platform.
Follow the same steps but vice-versa for sharing Infoblox IoCs to Netskope. Select your Source Configuration as CTE Infoblox, a Business Rule, the Destination Configuration (CTE Netskope), and Target. Refer to the
Netskope plugin guide
for more details.
Click
Save
.
Validate the Infoblox Plugin
Validate the Pull
Pulled data will be listed at
Threat IoCs
. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
To verify pulled from each page, you can add a filter of Tags appended in the indicators, like
sources.tags IN (“<tag_name>”)
.
For example, to filter the indicators pulled from Active Indicators page, you have to add a filter like:
sources.tags IN (“TIDE”)
.
To filter indicators pulled from Lookalike Domains page, add a filter like:
sources.tags IN (“Lookalike Domains”)
.
And to filter the indicators pulled from SOC Insights page, add a filter like:
sources.tags IN (“SOC Insights”)
.
To verify pulled logs on Cloud Exchange, go to
Logging
and search logs from the CTE Infoblox plugin.
Filter:
message Like “CTE Infoblox”
.
To verify the data available for pulling on Infoblox platform, Login to Infoblox and Navigate to
Monitor > Research > Active Indicators
page.
To verify lookalike domains, go to
Monitor > Reports > Security > Lookalike Domains
page.
Do the same for verifying SOC Insight indicators. Go to
Insights
.
Click
Investigate Insight
for any of the insights and move to the
Indicators
section.
To verify the Retracted IoCs, check the logs for IoC Retraction. For example:
message Like [Retraction]:
.
You can filter the retracted IoCs from the platform using the filter:
sources.source Is equal “<plugin configuration name>” && sources.retracted Is equal true
.
Note that the IoCs that fall under the Retraction Interval will be marked as
Retracted: Yes
in Cloud Exchange.
Sharing result will only be marked if the IoCs are pulled from the source plugin after creating the sharing configuration.
Here you can see 44 IoCs were added to the URL list on the Netskope Tenant.
Then one of the shared IoCs got marked as retracted, so it was deleted from the URL list.
Infoblox plugin does not support the deletion (retraction) of IoCs on the Infoblox platform. As a result, any previously shared IoCs will not be deleted (retracted) on Infoblox.
Validate the Push
Shared IoCs to Infoblox can be verified from logs available on the
Logging
page in Cloud Exchange.
To verify the ingested data on Infoblox platform, log in to Infoblox, go to
Monitor > Research > Active Indicators
, and then search for the particular IoCs.
Here are some sample ingested IoCs:
Troubleshooting the Infoblox Plugin
Unable to pull IoCs from the Infoblox platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of the following.
No IoCs are available on the platform to pull.
IoCs are not available for the given configuration parameters (like Types of Threat data to pull, Data Profile and Initial Range).
Polling is disabled.
Read Timeout Error, or Invalid Chunk Length Error, or Connection Reset Error.
What to do:
Identity your root cause from above and follow these steps to resolve the issue.
No IoCs are available on the platform to pull
Check if the IoCs are
available on the platform
to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. In the Infoblox platform, check if you have data for the given time range.
If the data is still available for the given time range, it might be possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter, and filter the same on the Infoblox platform.
Polling is disabled
Make sure that you have
Yes
selected in the enable polling, to pull the IoCs.
Read Timeout Error or Invalid Chunk Length Error or Connection Reset Error
We have observed some limitations for the Infoblox platform. While pulling larger number of IoCs, we faced the above mentioned errors, and you can more information under
Limitations
.
Unable to push the IoCs to Infoblox
If you are not able to push the IoCs on the platform and receive an error while pushing, it might be due to insufficient
permissions
.
What to do:
Refer to the
Permissions
section.
IoCs are pushed from Cloud Exchange, but not available on the Infoblox platform
If IoCs are pushed and not reflected on the platform, it might be due to many reasons. One of the reasons can be is that the IoC is marked inactive on the Infoblox platform. We have observed that if any of the IoCs are marked inactive on Infoblox, then they will not be available on the
Active indicators
page. We have also listed some of the other reasons under the Known Behaviors section.
What to do:
You need to check the default TTL for a particular threat property on Infoblox, and if you want to change the default TTL, then you can contact your Infoblox support team representative.
Known Behaviors
Following are things that have been noticed while verifying the plugin workflow.
Multiple IoC with the same value:
While pushing IoCs in to Infoblox using the plugin, you have to select the threat property. If you push the same IoC multiple times with a different threat properties, the IoC value will appear multiple times, each associated with its respective threat property on the Active Indicator page. As we cannot update an existing IoC, and since the property will be different, it would treat the same IoC as different and create a new one on the platform as shown below.
Pushed IoCs being marked as inactive:
When an IoC is pushed from Cloud Exchange to Infoblox, the detection time on Infoblox is automatically set to the current timestamp. The expiration time (or Time to Live – TTL) is then determined based on the threat property assigned to the IoC.
Each threat property in Infoblox has a default TTL, which can range from a few hours to several years. These TTL values can be viewed in Infoblox at
Monitor > Research > Resources > Default TTL
While pushing, if a user selects a threat property that has a short term
TTL
, Infoblox will automatically mark the IoC as
inactive
after the TTL expires. When this happens:
The IoC will no longer appear on the
Active Indicators
page.
The IoC will still be visible on the details page (
Monitor > Research > Dossier
), but its status will show as
inactive
.
Reserved IP:
When a reserved IP address is pushed to Infoblox, it will not show up in the
Active Indicators
page.
On the IoC details page (
Monitor > Research > Dossier
), some reserved IP addresses have no records for them.
Some IP addresses may have details about them, but will be classified as BOGON (an IP address that is invalid or should not be present in a routing table. These are often unallocated or reserved IP ranges.)
Some IP addresses give invalid indicator errors when searched on the details page.
Leading zeroes trimmed from IPv6:
When an IPv6 IoC is pushed to Infoblox (like via Netskope CE), Infoblox automatically trims leading zeroes from each hextet of the address as part of its normalization process.
For example:
If the IoC pushed is:
0202:0267:0062:0006:0000:0009:0060:0172
It will appear in Infoblox as:
202:267:62:6:0:9:60:172
Invalid URL:
The Infoblox TIDE API supports bulk uploading of IoCs, but it does not validate the IoC values at the time of submission. This means that even if the push is marked as successful from the plugin or the API, some IoCs may later be rejected by Infoblox if they are found to be invalid. This issue is particularly relevant for
URL-type
IoCs in Cloud Exchange, as there is no built-in validation for URL formats before storing them. As a result, invalid URLs might be pushed to Infoblox. Later, when viewing the
Active Indicators
page in Infoblox, these invalid entries may trigger an Invalid Indicator error, since Infoblox did not accept.
Visible on Active Indicators but not on details page
: In some cases, the IoC pushed is visible on the
Active Indicators
page, but when you search for the same IoC in the details page, you get an Invalid IoC error. (We do not know the exact reason for this behavior).
For pulling of IoCs
: This has a maximum limit of 100k IoCs per API call. So, if there is more than 100k data for a single day on Infoblox, then only 100k will be pulled to Cloud Exchange.
Limitations
We have observed that for a larger number of IoCs, the APIs throw these errors frequently while pulling them. The pull cycle in this case does completes, but it takes a lot of time.
Read Timeout Error:
CTE Infoblox TIDE [configuration_name]: Unable to establish connection with Infoblox TIDE platform while fetching threat data for page 1 from Infoblox TIDE server. Infoblox TIDE server is not reachable. Error: HTTPSConnectionPool(host='csp.infoblox.com', port=443): Max retries exceeded with url: /tide/api/data/threats?type=host%2Curl%2Chash%2Cip&rlimit=100000&from_date=2025-06-02T13%3A22%3A26Z&to_date=2025-06-02T14%3A13%3A28Z&data_format=json&include_ipv6=True (Caused by ReadTimeoutError("HTTPSConnectionPool(host='csp.infoblox.com', port=443): Read timed out. (read timeout=300)"))
Invalid Chunk Length Error:
CTE Infoblox TIDE [configuration_name]: Unexpected error occurred while fetching threat data for page 1 from Infoblox TIDE server. Error: ("Connection broken: InvalidChunkLength(got length b'', 0 bytes read)", InvalidChunkLength(got length b'', 0 bytes read))
Connection Reset Error:
CTE Infoblox TIDE [configuration_name]: Unexpected error occurred while fetching threat data for page 3 from Infoblox TIDE server. Error: ("Connection broken: ConnectionResetError(104, 'Connection reset by peer')", ConnectionResetError(104, 'Connection reset by peer'))
In this Topic
Infoblox Plugin for Threat Exchange

---
## Tanium Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/tanium-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:50:43+00:00
**Scraped:** 2026-08-11T07:40:25.725489+00:00

Tanium Plugin for Threat Exchange - Netskope Technical Documentation
Tanium Plugin for Threat Exchange
This document explains how to configure the Tanium v1.0.0 plugin in the Cloud Exchange platform. This plugin is used to fetch the indicators of type Hash (MD5 and SHA256) from the
Modules > Threat Response > Alerts
page in the Tanium platform. This plugin does not support sharing of indicators to the Tanium platform. This plugin supports retraction of indicators pulled from the Tanium platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the Tanium platform.
A subscription for Tanium Threat Response Module services.
Admin access in Tanium to generate an API Token and pull alerts.
Connectivity to the following host:
https://*-api.titankube.com/
.
Tanium Plugin Support
This plugin is used to fetch the indicators of type Hash (MD5 and SHA256) from the
Modules > Threat Response > Alerts
page in the Tanium platform. This plugin does not support sharing of indicators to the Tanium platform. This plugin supports retraction of indicators pulled from the Tanium platform.
Fetched Indicator Types
Shared Indicator Types
Hash (MD5 and SHA256)
NA
IoC Retraction
IoC Retraction (Pull): Indicators will be fetched from Tanium, and in the subsequent pull cycles, if some indicators are deleted on Tanium, then they will be marked as Retracted in Netskope Cloud Exchange.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
Mappings
Pull Mappings
Netskope CTE Field
Tanium API Field
type
(identify type from value)
value
details.match.properties.file.md5
details.match.properties.file.sha256
details.match.properties.parent.file.md5
details.match.properties.parent.file.sha256
firstSeen
details.finding.first_seen
lastSeen
details.finding.last_seen
severity
severity
comments
Priority:
<priority>
Intel Name:
<intelDoc.name>
Intel Description:
<intelDoc.description>
Intel Source Name:
<intelDoc.source.name>
Path:
<details.match.properties.{parent}.file.fullpath>
tags
parent_process_hash
child_process_hash
matchType
Severity Mappings for Pull
Netskope Severity
Tanium Severity
low
low
medium
medium
high
high
critical
critical
unknown
info
Permissions
Users should have the Admin User Role to generate an API Token and pull alerts.
API Details
List of APIs used
API Endpoint
Method
Use Case
/plugin/products/threat-response/api/v1/alerts
GET
Fetch Threat Response Alerts
Fetch Threat Response Alerts
API endpoint:
<API Base URL>
/plugin/products/threat-response/api/v1/alerts
Method:
GET
Headers
Key
Value
session
<API Token>
User-Agent
netskope-ce-5.1.2-cte-tanium-v1.0.0
Parameters
Key
Value
expand
intelDoc
limit
1000
offset
0
alertedAtFrom
<time>
sort
alertedAt
Sample API Response
{
"data": [
{
"id": 244,
"eid": 1004,
"state": "inprogress",
"type": "detect.match",
"guid": "00000000-0000-0000-d672-a2f862b6c592",
"priority": "high",
"severity": "info",
"details": "{\"match\":{\"hash\":\"8671925402277025835\",\"type\":\"process\",\"source\":\"recorder\",\"version\":1,\"contexts\":[{\"file\":{\"uniqueEventId\":\"4611686018429125664\"},\"event\":{\"fileDelete\":{\"path\":\"D:\\\\Users\\\\kes@google.in\\\\Downloads\\\\NSClient_addon-crest.betaskope.com_6410_rQ14jxRpa5CwQd5gjVkl_7qP2WqobiUcqDK17of58ZioLqPxKk8SMcjJb3d58_.msi:Zone.Identifier\"},\"timestampMs\":\"1737540697695\"}}],\"properties\":{\"pid\":9528,\"args\":\"C:\\\\Windows\\\\Explorer.EXE\",\"file\":{\"md5\":\"d2baaaaa96839af424e3bd69a0b22c71\",\"sha1\":\"00e6d95a94e564d94b58788816be303a06047b0b\",\"sha256\":\"a438bf739441f96f2db9f9bd49aa361a298f9498ba814acea29d5ea6a2d4468c\",\"fullpath\":\"C:\\\\Windows\\\\explorer.exe\"},\"name\":\"C:\\\\Windows\\\\explorer.exe\",\"ppid\":9248,\"user\":\"google\\\\kes\",\"parent\":{\"pid\":9248,\"args\":\"C:\\\\Windows\\\\system32\\\\userinit.exe\",\"file\":{\"md5\":\"6d1d512b5f2670d3e4035939bc57e655\",\"sha1\":\"71882ca27c9028062dcb37178a1694af54cd9586\",\"sha256\":\"095d63e4c5b6430fad8e1acafce578231a0efea3c870c68ed4eeae8484aa9530\",\"fullpath\":\"C:\\\\Windows\\\\System32\\\\userinit.exe\"},\"name\":\"C:\\\\Windows\\\\System32\\\\userinit.exe\",\"ppid\":860,\"user\":\"google\\\\kes\",\"parent\":{\"pid\":860,\"args\":\"winlogon.exe\",\"file\":{\"fullpath\":\"C:\\\\Windows\\\\System32\\\\winlogon.exe\"},\"name\":\"C:\\\\Windows\\\\System32\\\\winlogon.exe\",\"ppid\":780,\"user\":\"NT AUTHORITY\\\\SYSTEM\",\"parent\":{\"pid\":780,\"args\":\"\\\\SystemRoot\\\\System32\\\\smss.exe 000000d0 0000008c \",\"file\":{\"fullpath\":\"C:\\\\Windows\\\\System32\\\\smss.exe\"},\"name\":\"C:\\\\Windows\\\\System32\\\\smss.exe\",\"ppid\":556,\"user\":\"NT AUTHORITY\\\\SYSTEM\",\"parent\":{\"pid\":556,\"args\":\"\\\\SystemRoot\\\\System32\\\\smss.exe\",\"file\":{\"fullpath\":\"C:\\\\Windows\\\\System32\\\\smss.exe\"},\"name\":\"C:\\\\Windows\\\\System32\\\\smss.exe\",\"ppid\":4,\"user\":\"NT AUTHORITY\\\\SYSTEM\",\"parent\":{\"pid\":4,\"file\":{\"fullpath\":\"System\"},\"name\":\"System\",\"user\":\"NT AUTHORITY\\\\SYSTEM\",\"start_time\":\"2025-01-21T10:29:31.000Z\",\"recorder_unique_id\":\"8569627172349557237\"},\"start_time\":\"2025-01-21T10:29:31.000Z\",\"recorder_unique_id\":\"3804061124233752300\"},\"start_time\":\"2025-01-21T10:29:35.000Z\",\"recorder_unique_id\":\"18323218992899302098\"},\"start_time\":\"2025-01-21T10:29:35.000Z\",\"recorder_unique_id\":\"8017205500022428559\"},\"start_time\":\"2025-01-21T10:33:04.000Z\",\"recorder_unique_id\":\"3695158773730177212\"},\"start_time\":\"2025-01-21T10:33:11.000Z\",\"recorder_unique_id\":\"6415688394152031122\"}},\"finding\":{\"whats\":[{\"source_name\":\"recorder\",\"intel_intra_ids\":[{\"id_v2\":\"10420185013891409313\"},{\"id_v2\":\"13232781051211547001\"}],\"artifact_activity\":{\"acting_artifact\":{\"process\":{\"pid\":9528,\"file\":{\"file\":{\"hash\":{\"md5\":\"d2baaaaa96839af424e3bd69a0b22c71\",\"sha1\":\"00e6d95a94e564d94b58788816be303a06047b0b\",\"sha256\":\"a438bf739441f96f2db9f9bd49aa361a298f9498ba814acea29d5ea6a2d4468c\"},\"path\":\"C:\\\\Windows\\\\explorer.exe\",\"signature_data\":{\"issuer\":\"Microsoft Windows Production PCA 2011\",\"status\":1,\"subject\":\"Microsoft Windows\"}},\"artifact_hash\":\"4668134681718746372\",\"instance_hash\":\"4668134681718746372\"},\"user\":{\"user\":{\"name\":\"kes\",\"domain\":\"google\",\"user_id\":\"S-1-5-21-769425621-2486857270-3423107360-1145\"}},\"parent\":{\"process\":{\"pid\":9248,\"file\":{\"file\":{\"hash\":{\"md5\":\"6d1d512b5f2670d3e4035939bc57e655\",\"sha1\":\"71882ca27c9028062dcb37178a1694af54cd9586\",\"sha256\":\"095d63e4c5b6430fad8e1acafce578231a0efea3c870c68ed4eeae8484aa9530\"},\"path\":\"C:\\\\Windows\\\\System32\\\\userinit.exe\",\"signature_data\":{\"issuer\":\"Microsoft Windows Production PCA 2011\",\"status\":1,\"subject\":\"Microsoft Windows\"}},\"artifact_hash\":\"16325832498882432364\",\"instance_hash\":\"16325832498882432364\"},\"user\":{\"user\":{\"name\":\"kes\",\"domain\":\"google\",\"user_id\":\"S-1-5-21-769425621-2486857270-3423107360-1145\"}},\"parent\":{\"process\":{\"pid\":860,\"file\":{\"file\":{\"path\":\"C:\\\\Windows\\\\System32\\\\winlogon.exe\",\"signature_data\":{\"issuer\":\"Microsoft Windows Production PCA 2011\",\"status\":1,\"subject\":\"Microsoft Windows\"}},\"artifact_hash\":\"13433015920877340112\",\"instance_hash\":\"13433015920877340112\"},\"user\":{\"user\":{\"name\":\"SYSTEM\",\"domain\":\"NT AUTHORITY\",\"user_id\":\"S-1-5-18\"}},\"parent\":{\"process\":{\"pid\":780,\"file\":{\"file\":{\"path\":\"C:\\\\Windows\\\\System32\\\\smss.exe\",\"signature_data\":{\"issuer\":\"Microsoft Windows Production PCA 2011\",\"status\":1,\"subject\":\"Microsoft Windows Publisher\"}},\"artifact_hash\":\"13095238853773225043\",\"instance_hash\":\"13095238853773225043\"},\"user\":{\"user\":{\"name\":\"SYSTEM\",\"domain\":\"NT AUTHORITY\",\"user_id\":\"S-1-5-18\"}},\"parent\":{\"process\":{\"pid\":556,\"file\":{\"file\":{\"path\":\"C:\\\\Windows\\\\System32\\\\smss.exe\",\"signature_data\":{\"issuer\":\"Microsoft Windows Production PCA 2011\",\"status\":1,\"subject\":\"Microsoft Windows Publisher\"}},\"artifact_hash\":\"13095238853773225043\",\"instance_hash\":\"13095238853773225043\"},\"user\":{\"user\":{\"name\":\"SYSTEM\",\"domain\":\"NT AUTHORITY\",\"user_id\":\"S-1-5-18\"}},\"parent\":{\"process\":{\"pid\":4,\"file\":{\"file\":{\"path\":\"System\",\"signature_data\":{\"status\":7}},\"artifact_hash\":\"10673367317368319370\",\"instance_hash\":\"10673367317368319370\"},\"user\":{\"user\":{\"name\":\"SYSTEM\",\"domain\":\"NT AUTHORITY\",\"user_id\":\"S-1-5-18\"}},\"handles\":[],\"arguments\":{},\"start_time\":\"2025-01-21T10:29:31.000Z\",\"tanium_unique_id\":\"8569627172349557237\"},\"artifact_hash\":\"133628619820746138\",\"instance_hash\":\"17432442374944931046\"},\"handles\":[],\"arguments\":\"\\\\SystemRoot\\\\System32\\\\smss.exe\",\"start_time\":\"2025-01-21T10:29:31.000Z\",\"tanium_unique_id\":\"3804061124233752300\"},\"artifact_hash\":\"6295600673353488791\",\"instance_hash\":\"10239728948408888913\"},\"handles\":[],\"arguments\":\"\\\\SystemRoot\\\\System32\\\\smss.exe 000000d0 0000008c \",\"start_time\":\"2025-01-21T10:29:35.000Z\",\"tanium_unique_id\":\"18323218992899302098\"},\"artifact_hash\":\"1682511555763885258\",\"instance_hash\":\"9882236691747135410\"},\"handles\":[],\"arguments\":\"winlogon.exe\",\"start_time\":\"2025-01-21T10:29:35.000Z\",\"tanium_unique_id\":\"8017205500022428559\"},\"artifact_hash\":\"15202984064548280121\",\"instance_hash\":\"9617131730790084616\"},\"handles\":[],\"arguments\":\"C:\\\\Windows\\\\system32\\\\userinit.exe\",\"start_time\":\"2025-01-21T10:33:04.000Z\",\"tanium_unique_id\":\"3695158773730177212\"},\"artifact_hash\":\"15310695090792779169\",\"instance_hash\":\"3453834692933203077\"},\"handles\":[],\"arguments\":\"C:\\\\Windows\\\\Explorer.EXE\",\"start_time\":\"2025-01-21T10:33:11.000Z\",\"tanium_unique_id\":\"6415688394152031122\"},\"artifact_hash\":\"8671925402277025835\",\"instance_hash\":\"8851274989043869165\",\"is_intel_target\":true},\"relevant_actions\":[{\"verb\":4,\"target\":{\"file\":{\"path\":\"D:\\\\Users\\\\kes@google.in\\\\Downloads\\\\NSClient_addon-crest.betaskope.com_6410_rQ14jxRpa5CwQd5gjVkl_7qP2WqobiUcqDK17of58ZioLqPxKk8SMcjJb3d58_.msi:Zone.Identifier\"},\"artifact_hash\":\"13157424290436624405\",\"instance_hash\":\"13157424290436624405\"},\"timestamp\":\"2025-01-22T10:11:37.000Z\",\"tanium_recorder_context\":{\"file\":{\"unique_event_id\":\"4611686018429125664\"},\"event\":{\"file_delete\":{\"path\":\"D:\\\\Users\\\\kes@google.in\\\\Downloads\\\\NSClient_addon-crest.betaskope.com_6410_rQ14jxRpa5CwQd5gjVkl_7qP2WqobiUcqDK17of58ZioLqPxKk8SMcjJb3d58_.msi:Zone.Identifier\"},\"timestamp_ms\":\"1737540697695\"}},\"tanium_recorder_event_table_id\":\"4611686018429125664\"}]}}],\"domain\":\"threatresponse\",\"hunt_id\":\"2\",\"type_id\":\"intel\",\"intel_id\":\"701:1:94c7b075-2c70-4bb2-b4a1-9453ebdbf0fc\",\"last_seen\":\"2025-01-22T10:11:39.000Z\",\"threat_id\":\"10420185013891409313,13232781051211547001\",\"finding_id\":\"-2994151614556224110\",\"first_seen\":\"2025-01-22T10:11:39.000Z\",\"source_name\":\"recorder\",\"system_info\":{\"os\":\"Microsoft Windows Server 2022 Datacenter\",\"bits\":64,\"platform\":\"Windows\",\"patch_level\":\"10.0.20348.0.0\",\"build_number\":\"20348\"},\"reporting_id\":\"reporting-id-placeholder\"},\"intel_id\":701,\"config_id\":2,\"config_rev_id\":1}",
"intelDocId": 701,
"groupingId": 50,
"intelDocRevisionId": 1,
"scanConfigId": 2,
"scanConfigRevisionId": 1,
"computerName": "KATHYCOMBS-PC8893.jones.info",
"computerIpAddress": "16.181.5.2",
"matchType": "process",
"path": "C:\\Windows\\explorer.exe",
"receivedAt": "2025-01-22T10:15:40.062Z",
"suppressedAt": null,
"alertedAt": "2025-01-22T10:11:39.000Z",
"findingId": "-2994151614556224110",
"ackedAt": "2025-01-22T10:28:35.026Z",
"firstEIDResolutionAttempt": "2025-01-22T10:15:43.488Z",
"lastEIDResolutionAttempt": "2025-01-22T10:15:43.488Z",
"createdAt": "2025-01-22T10:15:40.223Z",
"updatedAt": "2025-02-24T11:02:31.600Z",
"sentToConnect": true,
"reactions": [],
"intelDoc": {
"id": 701,
"type": "tanium-signal",
"typeVersion": "1.0",
"md5": "0363a2dc3dad684bd1b8654052813e34",
"blobId": "d1d19d68-d9a4-49ac-a8ae-49fc7015672a",
"revisionId": 2,
"intrinsicId": "Zone Identifier ADS Deletion",
"name": "Zone Identifier ADS Deletion",
"description": "Detects deletion of Zone Identifier ADS files that may be related to attacker actvity to cover their tracks.",
"size": 593,
"compiled": {
"expressions": [],
"terms": [
{
"condition": "ends with",
"negate": true,
"value": "\\windows\\explorer.exe",
"object": "process",
"property": "path"
},
{
"event_group": 1,
"condition": "ends with",
"negate": false,
"value": ":Zone.Identifier",
"object": "file",
"property": "path"
},
{
"event_group": 1,
"condition": "is",
"negate": false,
"value": "delete",
"object": "file",
"property": "operation"
}
],
"operator": "and",
"text": "group(file.path ends with ':Zone.Identifier' AND file.operation is 'delete') AND process.path ends with NOT '\\\\windows\\\\explorer.exe'",
"syntax_version": 2
},
"isSchemaValid": true,
"sourceId": 9,
"customHash": null,
"mitreAttack": {
"techniques": [
{
"id": "T1070",
"name": "Indicator Removal"
},
{
"id": "T1070.004",
"name": "Indicator Removal on Host Mitigation: File Deletion"
}
]
},
"platforms": [
"windows"
],
"createdAt": "2024-09-09T19:30:28.353Z",
"updatedAt": "2025-08-25T18:06:12.747Z",
"throttledFindingCount": 0,
"allowAutoDisable": true,
"disabled": false,
"disabledEndpointCount": 0,
"firstDeploymentTimestamp": "2025-02-12T23:26:41.672Z",
"lastDeploymentTimestamp": "2025-08-25T18:06:12.714Z",
"status": "HIGH_FIDELITY",
"editedAt": "2025-02-12T07:36:08.637Z",
"source": {
"id": 9,
"enabled": true,
"type": "tanium-signals",
"name": "Tanium Signals",
"nameSlug": "tanium-signals",
"description": "Tanium authored Signals stream",
"config": {
"subscriptionIntervalMins": 60,
"shouldRequireSignature": true,
"ignoreSsl": false,
"manifestUrl": "https://content.tanium.com/files/misc/ThreatResponse/ThreatResponse.xml"
},
"state": {
"lastIngestVersion": "4.16.0.0001",
"lastRunAt": 1756361558483
},
"createdAt": "2024-09-09T19:30:04.942Z",
"updatedAt": "2025-08-28T06:12:38.484Z"
}
}
},
…
],
"meta": {
"totalCount": 43,
"filteredCount": 43
}
}
Performance Matrix
This reading is conducted on a Large Cloud Exchange Stack with these specs by pulling 100k IoCs from Tanium.
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Indicators fetched from Tanium
~25k per min
User Agent
netskope-ce-5.1.2-cte-tanium-v1.0.0
Workflow
Create an API token on Tanium.
Configure the Tanium plugin.
Add a Business Rule.
Add Actions.
Validate the Tanium plugin.
Watch a Video
Click play to watch a video:
Create an API token on Tanium
Log in to your Tanium platform.
Go to
Administration > API Tokens
from the left panel.
Click
New API Token
.
Enter the required details. Set Expiration per your requirements, and specify an IP address to allow access from a particular machine, or use a general IP to enable access from any source.
Click
Create
, and then click
Yes
in the
Confirm Your Action
prompt.
Copy the Token from the
View API Token
tab. This will be used to configure the Tanium plugin.
Click
Close
.
Configure the Tanium plugin
Log in to Cloud Exchange and go to
Settings > Plugins
.
Search for and select the
Tanium v1.0.0 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources.
Note that it is better to have a larger value for Sync Interval if you want to pull IoCs in large numbers.
Aging Criteria:
Expiry time of the plugin in days (Default: 90).
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Use System Proxy
: Enable if the proxy is required for communication.
Click
Next
and enter the Configuration Parameters:
API Base URL:
API Base URL of Tanium instance. For example:
https://<domain>-api.titankube.com
API Token:
API Token generated from the Tanium instance previously.
Type of Threat Data to Pull:
Type of Threat data to pull. Allowed values are MD5 and SHA256.
Enable Tagging:
Enable/Disable tagging functionality.
Retraction Interval:
Specify the number of days for which IoC retraction should be run for Tanium indicators. Note that this parameter is applicable only for Netskope Cloud Exchange version 5.1.0 or later, and if IoC(s) Retraction is enabled in Threat Exchange Settings.
Initial Range:
Number of days to pull the data for the initial run.
Click
Save
.
Add a Threat Exchange Business Rule for Tanium
To share indicators fetched from Tanium to Cloud Exchange, you need to have a business rule that will filter out the indicators that you want to share. To configure a business rule:
Go to
Threat Exchange > Business Rules
and click
Create New Rule
.
Add the filter according to your requirements in the rule. When finished, click
Save
.
Add Threat Exchange Sharing for Tanium
To share IoCs from Tanium to Cloud Exchange:
Go to
Threat Exchange > Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Tanium), a Business Rule, the Destination Configuration (CTE Netskope), and a Target.
Click
Save
.
Validate the Tanium Plugin
Validate the Pull
Pulled data will be listed on the
Threat IoCs
page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE Tanium plugin.
For example:
message Like “CTE Tanium”
To verify the data available for pulling on the Tanium platform, log in to Tanium and go to
Modules > Threat Response > Alerts
.
To verify the Retracted IoCs, check the logs for IoC Retraction. For example:
message Like [Retraction]:
You can filter the retracted IoCs from the platform using the filter:
sources.source Is equal “<plugin configuration name>” && sources.retracted Is equal true
.
Notes
The IoCs that fall under the Retraction Interval will be marked as
Retracted: Yes
in Cloud Exchange.
Sharing result will only be marked if the IoCs are pulled from the source plugin after creating the sharing configuration.
Validate the Push
Here you can see IoCs were added to the File hash list on Netskope Tenant.
Then some of the shared IoCs got marked as retracted, so they were deleted from the list.
Troubleshooting the Tanium Plugin
Unable to pull IoCs from the Tanium platform
After the plugin configuration, if the IoCs are not pulled from the platform, it may be due to one of these reasons:
No IoCs are available on the platform to pull.
IoCs are not available for the given configuration parameters (like Types of Threat data to pull).
What to do:
Identity the root cause per the above descriptions, and then follow these steps to resolve the issue.
No IoCs are available on the platform to pull
Check if the IoCs are
available on the platform
to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Tanium platform, check if you have data for the given time range.
If the data is still available for the given time range, it’s possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter, and then filter the same on the Tanium platform.
In this Topic
Tanium Plugin for Threat Exchange

---
## Abnormal Security Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/abnormal-security-plugin-for-threat-exchange/
**Last Modified:** 2026-06-11T03:59:33+00:00
**Scraped:** 2026-08-11T07:41:08.698626+00:00

Abnormal Security Plugin for Threat Exchange - Netskope Technical Documentation
Abnormal Security Plugin for Threat Exchange
Release Notes
1.1.1
Changed
URL encode the attachment name before making API call for attachment details.
Removed skipped IOC values from logger message, due to None values.
Updated maximum allowed value for Initial Range and Retraction Interval to 100k days.
1.1.0
Added
Added support for fetching IoCs of type IPv6.
Added API URL for FedRAMP GovCloud instances.
Fixed
Fixed sub_checkpoint logic.
Fixed IoC fetched and skipped count error in log messages.
1.0.0
Added
Initial Release.
This document explains how to configure the CTE Abnormal Security v1.1.1 plugin for the Threat Exchange module of the Netskope Cloud Exchange platform.This plugin is used to pull IOCs of type SHA256, MD5, URL, Domain, IPv4 and IPv6 from Threat Log page of Abnormal Security platform. This plugin supports retraction of IOCs pulled from the Abnormal Security platform. This plugin does not support sharing of indicators to the Abnormal Security platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope Tenant
A Netskope Cloud Exchange instance with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Abnormal Security platform credentials.
Connectivity to the following hosts:
Production Server (api.abnormalplatform.com/v1)
EU Production Server (eu.rest.abnormalsecurity.com/v1)
FedRAMP GovCloud (rest.abnormalsecurity.us)
This plugin is only tested with the Production Server (api.abnormalplatform.com/v1).
Abnormal Security Plugin Support
Fetched Indicator Types
Shared Indicator Types
SHA256
MD5
URL
Domain
IPv4
IPv6
Not Supported
Mappings
Pull Mappings
Cloud Exchange Fields
Abnormal Security Fields
Value
value corresponding to field (senderDomain or senderIpAddress or md5 or sha256 or urls or url)
Type
senderDomain, senderIpAddress, md5, sha256, urls, url
firstSeen
receivedTime (for senderDomain and senderIpAddress and urls) or createdOn (for md5 and sha256 and url)
lastSeen
receivedTime (for senderDomain and senderIpAddress and urls) or lastUpdated (for md5 and sha256 and url)
tags
summaryInsights, remediationStatus
comments
subject
The urls field extracted from threat details api response is the list of URLs found in the email body. The url field extracted from message attachment api response is the list of URLs found in email attachment.
IoC Retraction
IoC Retraction (Pull):
Indicators will be fetched from Abnormal and in the subsequent pull cycles. If some indicators are deleted from Anomali, they will be marked as Retracted in Cloud Exchange.
IoC Retraction (Push):
Retracted indicators present on Cloud Exchange will be deleted from Abnormal during sharing.
Type
Description
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
Permissions
You will need below permissions for the API Toke:
Threats – Read Access
Messages – Read Sensitive Access
API Details
List of APIs Used
API Endpoint
Method
Use Case
/threats
GET
Get all threats within given timerange, paginated
/threats/<threat_id>
GET
Get threat details of given threat
/messages/<message_id>/attachment/<attachemnt_name>
GET
Get message and attachment details, message_id and attachment_name taken from above Threat details endpoint
Pull Threats
Endpoint:
/threats
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0-cte-abnormal-security-v1.1.1
Accept
application/json
Content-Type
application/json
Authorization
Bearer token
Parameters
Key
Value
pageSize
100
pageNumber
100
filter
receivedTime gte <start_time> lte <end_time>
Sample Response
{
  "threats": [
    {
      "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"
    }
  ],
  "pageNumber": 1,
  "nextPageNumber": 2
}
Pull Threat details
Endpoint:
/threats/
<threat_id>
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0-cte-abnormal-security-v1.1.1
Accept
application/json
Content-Type
application/json
Authorization
Bearer token
Parameters
Key
Value
pageSize
100
pageNumber
100
Sample Response
{
  "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
  "messages": [
    {
      "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
      "abxMessageIdStr": "4551618356913732000",
      "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/4551618356913732076",
      "subject": "Phishing Email",
      "fromAddress": "support@secure-reply.org",
      "fromName": "Support",
      "senderDomain": "secure-reply.org",
      "toAddresses": "example@example.com, another@example.com",
      "recipientAddress": "example@example.com",
      "receivedTime": "2020-06-09T17:42:59Z",
      "sentTime": "2020-06-09T17:42:59Z",
      "internetMessageId": "<5edfca1c.1c69fb81.4b055.8fd5@mx.google.com>",
      "remediationStatus": "Auto Remediated",
      "attackType": "Extortion",
      "attackStrategy": "Name Impersonation",
      "returnPath": "support@secure-reply.org",
      "replyToEmails": [
        "reply-to@example.com"
      ],
      "ccEmails": [
        "cc@example.com"
      ],
      "senderIpAddress": "100.101.102.103",
      "impersonatedParty": "None / Others",
      "attackVector": "Text",
      "attachmentNames": [
        "attachment.pdf"
      ],
      "attachmentCount": 0,
      "urls": [
        "https://www.google.com/"
      ],
      "urlCount": 0,
      "summaryInsights": [
        "Bitcoin Topics",
        "Personal Information Theft",
        "Unusual Sender"
      ],
      "remediationTimestamp": "2020-06-09T17:42:59Z",
      "isRead": true,
      "attackedParty": "VIP",
      "autoRemediated": "True",
      "postRemediated": "False"
    }
  ],
  "pageNumber": 1,
  "nextPageNumber": 2
}
Pull Threat Message and Attachment details
Endpoint:
/messages/
<message_id>
/attachment/
<attachment_name>
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.1.0-cte-abnormal-security-v1.1.1
Accept
application/json
Content-Type
application/json
Authorization
Bearer token
Sample Response
{
    "data": [
        {
            "attachmentName": "image.jpg",
            "type": "jpg",
            "md5": "d38deea567961e23059d3edd310a82d0",
            "sha1": "1caeee0cca7ac0e8f95fac59acf4d06d48884622",
            "sha256": "f2ccf68511b93832ea8dd7195fb60319de7a03b1795081aed53272d8d82268f1",
            "size": "200KB",
        }
    ]
}
Performance Matrix
This performance has been conducted on a large CE instance with these specifications by pulling 100k IoCs.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicators fetched from Abnormal Security
~20k IoCs per min
User Agent
netskope-ce-6.0.0-cte-abnormal-security-v1.1.0
Workflow
Get the API Token for Abnormal Security.
Configure the Abnormal Security plugin.
Add a Business Rule for Abnormal Security.
Configure Sharing for Abnormal Security and Netskope Threat Exchange
Validate the Abnormal Security plugin.
Watch a Video
Click play to watch a video:
Get the API Token for Abnormal Security
Log in to Abnormal Security.
Go to
Settings > Integrations
.
Scroll down to the
API Token Management
section and click
Create New Token
.
Select
Rest API
, and click
Next
.
Select the tenant from the dropdown, and click
Next
.
Select
Custom Access
for
Configure Access Type
, select the permissions listed in the
permissions
section, and click
Next
.
Enter a Token Name, Description and select
Token Expiration Period
, and provide the public IP of the instance hosting your Cloud Exchange in the IP Safelist, and then click
Next.
Review the Token Configuration and click
Create Token
.
Copy the created API Token.
Configure the Abnormal Security Plugin
In Cloud Exchange and go to
Settings > Plugin Store
. Search for and select the
Abnormal Security  v1.1.1 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Leave the default
Aging Criteria:
Expiry time of the plugin in days. ( Default: 90 )
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Use System Proxy
: Enable if the proxy is required for communication.
Click
Next
and enter the Configuration Parameters.
Base URL:
Base URL of Abnormal Security API endpoint.
API Token:
Provide the API Token from Abnormal Security.
Type of Threat Data to Pull:
Type of Threat data to pull. Allowed values are SHA256, MD5, URL, Domain, IPv4 and IPv6.
Retraction Interval (in days):
Retraction Interval days to run IoC(s) retraction for Abnormal Security indicators. Note that this parameter will only be considered if
IoC(s) Retraction
is enabled in Threat Exchange Settings. This parameter is applicable only for Netskope CE version 5.1.0 and above.
Enable Tagging:
Enable/Disable tagging functionality.
Initial Range (in days):
Number of days Threat IoCs to pull in the initial run.
Click
Save
.
Add a Threat Exchange Business Rule for Abnormal Security
To share indicators fetched from Abnormal Security to the Cloud Exchange, you need to have a business rule that will filter out the indicators that you want to share.
In Threat Exchange, go to
Business Rules
and
Create New Rule
.
Add the filter according to your requirement in the rule, and then click
Save
.
Configure Sharing for Abnormal Security and Netskope
To share IoCs from the Abnormal Security to other third party platform:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Abnormal Security), Business Rule, Destination Configuration (CTE Netskope), and Target.
Click
Save
.
Note
The Abnormal Security plugin does not support sharing of IoCs, but the IoCs pulled from this plugin can be shared to other 3rd-party platforms.
As you are pulling SHA256, MD5, URL, Domain, IPv4 and IPv6 from Abnormal Security, you can add URL, IPv4 and Domains to the URL list, plus SHA256 and MD5 to File hash List, IPv4 and Domain to Private App. URL, IPv4, and Domains to Destination Profile, and Domains to DNS Profile.
Validate the Abnormal Security Plugin
Validate the Pull
To verify pulled logs in Cloud Exchange, go to
Logging
and search logs from the CTE Abnormal Security plugin. You can filter the logs using the filter:
message Like “[<plugin configuration name>]”
Pulled data will be listed on the
Threat IoCs
page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
To verify the data available for pulling on Abnormal Security, log in to Abnormal Security and go to the
Threat Log
page.
Open any of the Threat logs, and there you can find different IoCs that can be pulled.
The plugin pulls URLs from the Links section.
IPv4 and IPv6 from Sender IP Address.
Domain from Sender Domain.
SHA256 and MD5 from the Attachments of Email Content.
Validate the Pull Retraction
To verify the Retracted IoCs, check the logs for IoC Retraction example:
message Like CTE Abnormal Security [CTE Abnormal Security] [Retraction].
You can filter the retracted IoCs from the platform using the filter:
sources.source Is equal “<plugin configuration name>” && sources.retracted Is equal true
The IoCs that fall under the Retraction Interval will be marked as
Retracted: Yes
in Cloud Exchange.
Troubleshooting the Abnormal Security Plugin
Receiving error while configuring the plugin or pulling data
If you are receiving the below error while configuring the plugin.
CTE Abnormal Security [CTE Abnormal Security]: Validation error occurred, Received exit code 403 (Forbidden), Verify Base URL and API Token provided in the configuration parameters.
This issue may be due to one of these reasons:
Base URL and API Token is invalid/deleted.
Your public IP address where your Cloud Exchange hosted is not added in IP Safelist.
What to do:
Check the plugin credentials if the Base URL and API Token is valid, if it is valid check if the
credentials
that you are using are still available on the Abnormal Security.
Make sure you have added the public IP of the instance where Cloud Exchange is hosted to the IP Safelist as mentioned in the
Get the API Token for Abnormal Security
section.
If your cloud exchange is running in a private network then add your machine’s Public IP Address to this safelist.
To get your machine’s Public IP address run the below command on the machine where Cloud Exchange is hosted.
curl ifconfig.me
For Cloud Exchange hosted on AWS or Azure copy your machine’s Public IP address from the AWS or Azure portal and add it to the safelist.
Getting the error “HTTP Error while fetching attachment data for Document-for-Payment @.pdf with Message ID -xxxxxxxxxxxxx.”
If you have configured the plugin with v1.1.0 or earlier and facing this error while pulling the indicators from Abnormal Security, it might be due to the attachment details having special characters like ‘#’. To resolve this issue, follow the steps given below.
What to do:
Upgrade the plugin to the latest version, and verify the indicators pulled.
Unable to pull IoCs from the Abnormal Security platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IoCs are available on the platform to pull
IoCs are not available for the given configuration parameters (i.e. Types of Threat data to pull).
What to do:
Identity your root cause from above and follow these steps to resolve the issue.
No IoCs are available on the platform to pull:
Check if the IoCs are
available on the platform
to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Abnormal Security platform, check if you have data for the given time range.
If the data is still available for the given time range, it might be possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter and filter the same on the Abnormal Security platform.
In this Topic
Abnormal Security Plugin for Threat Exchange

---
## Imperva Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/imperva-plugin-for-threat-exchange/
**Last Modified:** 2026-05-27T23:42:53+00:00
**Scraped:** 2026-08-11T07:43:58.394686+00:00

Imperva Plugin for Threat Exchange - Netskope Technical Documentation
Imperva Plugin for Threat Exchange
This document explains how to configure the Imperva v1.0.0 plugin in the Cloud Exchange platform. This plugin is used to fetch the IoCs of type IPv4 from the
Application > Attack Analytics > Incidents
page on the Imperva platform. This plugin does not support sharing of IoCs to the Imperva platform. This plugin supports retraction of IoCs pulled from the Imperva platform.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A
URL List
on your Netskope tenant.
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured.
Connectivity to the Imperva platform.
A subscription for Imperva Threat Response Module services.
Need a user with Manage API Key role to generate an API Key.
Connectivity to the following host: https://api.imperva.com
Imperva Plugin Support
This plugin is used to fetch the IoCs of type IPv4 from the Application > Attack Analytics > Incidents page on the Imperva platform. This plugin does not support sharing of IoCs to the Imperva platform. This plugin supports retraction of IoCs pulled from the Imperva platform.
Fetched Indicator Types
Shared Indicator Types
IPv4
NA
IoC Retraction
IoC Retraction (Pull) Indicators will be fetched from Imperva and in the subsequent pull cycles if some indicators are deleted on Imperva then they will be marked as Retracted in Netskope Cloud Exchange.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
No
Mappings
Pull Mappings
Cloud Exchange Field
Imperva API Field
IoC Value
dominant_attack_ip.ip
Type
IPv4
Severity
severity
Firstseen
first_event_time
Lastseen
last_event_time
Extended string
https://
<imperva-instance-url>
/attack-analytics/incident-details/
<incident_id>
Tags
incident_type
dominant_attack_violation
dominant_attack_ip.reputation
dominant_attack_ip. dominance
severity_explanation
Severity Mappings for Pull
Netskope Severity
Imperva Severity
LOW
MINOR
HIGH
MAJOR
CRITICAL
CRITICAL
UNKNOWN
CUSTOM
Permissions
Users should have the Manage API Key Role to generate API Key.
API Details
List of APIs used
API Endpoint
Method
Use Case
/analytics/v1/incidents
GET
Fetch IoCs from Incidents
Fetch IoCs from Incidents
Endpoint
: /analytics/v1/incidents
Method
: GET
Headers
Key
Value
User-Agent
netskope-ce-6.0.0-cte-imperva-v1.0.0
x-API-Id
<api_id>
x-API-Key
<api_key>
accept
application/json
Query Parameters
Key
Value
caid
<Account ID>
from_timestamp
<timestamp>
to_timestamp
<timestamp>
Sample Response
[
{
"id": "db0cfbe0-d8ca-11f0-1f46-8bef9ba73c98",
"main_sentence": "Illegal Resource Access attack by a single IP from Bulgaria using Go HTTP library HackingTool ",
"secondary_sentence": "On host \"imperva1.cdsys.io\" ",
"false_positive": false,
"events_count": 6,
"events_blocked_percent": 0,
"first_event_time": 1765702422735,
"last_event_time": 1765702621854,
"severity": "MINOR",
"severity_explanation": "High risk, High confidence",
"dominant_attack_country": {
"country": "Bulgaria",
"country_code": "BG",
"dominance": "DOMINANT"
},
"dominant_attack_ip": {
"ip": "195.178.110.158",
"reputation": [
"IP reputation Medium risk"
],
"dominance": "STRONGLY_DOMINANT"
},
"dominant_attacked_host": {
"value": "imperva1.cdsys.io",
"dominance": "STRONGLY_DOMINANT"
},
"dominant_attack_tool": {
"name": "Go HTTP library",
"type": "Suspicious",
"dominance": "STRONGLY_DOMINANT"
},
"dominant_attack_violation": "Illegal Resource Access",
"only_custom_rule_based": true,
"how_common": "SPRAY_AND_PRAY",
"incident_type": "REGULAR"
}
]
Performance Matrix
This reading is conducted on a Large Cloud Exchange Stack with these specs by pulling 100k IoCs from Imperva.
Description
Specification
Stack Size
Large
RAM: 32 GB
Core: 16
Indicators fetched from Imperva
~11k per min
User Agent
netskope-ce-6.0.0-cte-imperva-v1.0.0
Workflow
Create an API Key on Imperva.
Configure the Imperva Plugin.
Add a Business Rule for Imperva.
Configure Sharing for Imperva.
Validate the Imperva plugin.
Watch a Video
Click play to watch a video.
Create API Key on Imperva
Log in to Imperva.
Go to
Account > Account Management
from the top right corner.
Go to
User Management > My Profile.
Scroll down to
API Keys
and click
Add API Key
.
Enter a Name and the API key will expire in time and enable the status. Click
Create
.
Copy the API ID and API Key and then click
Close
.
Configure the Imperva Plugin
In Cloud Exchange go to
Settings > Plugin Store
.
Search for and select the
Imperva v1.0.0 (CTE)
plugin box.
Enter the Basic Information:
Configuration Name
: Unique name for the configuration.
Sync Interval
: Interval to fetch data from this plugin and share data to this plugin from other sources.
Aging Criteria:
Expiry time of the plugin in days (Default: 90).
Override Reputation
: Set a value to override the reputation of indicators received from this configuration.
Enable SSL Validation
: Enable SSL Certificate validation.
Use System Proxy
: Enable if the proxy is required for communication.
Note
It is better to have a larger value for Sync Interval if you want to pull IoCs in large numbers.
Click Next and enter the Configuration Parameters:
Account ID:
Unique identifier of your account.
API ID:
API ID generated from your Imperva instance.
API Key:
API Key generated from your Imperva instance.
Enable Tagging:
Enable/Disable tagging functionality.
Retraction Interval:
Specify the number of days for which IoC retraction should be run for Imperva IoCs. Note that this parameter is applicable only for Netskope CE version 5.1.0 or later, and if I
oC(s) Retraction
is enabled in your Threat Exchange Settings. Value must be between 1 and 1800.
Initial Range:
Number of days to pull the data for the initial run. Value must be between 1 and 1800.
Click
Save
.
Add a Threat Exchange Business Rule for Imperva Plugin
To share indicators fetched from the Imperva to the Netskope CE, you will need to have a business rule that will filter out the indicators that you want to share. To configure a business rule, follow the below steps:
In Threat Exchange go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirement in the rule and click Save.
Configure Threat Exchange Sharing for Imperva
The Imperva plugin does not support sharing of IoCs, but the IoCs pulled from this plugin can be shared to the Netskope Tenant or other 3rd-party platforms.
To share IoCs from Imperva to Cloud Exchange:
In Threat Exchange go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Imperva), a Business Rule, the Destination Configuration (CTE Netskope), and Target.
Click
Save
.
Validate the Imperva Plugin
Validate the Pull
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
To verify pulled logs on Cloud Exchange, go to
Logging
and search logs from the Imperva plugin.
Filter:
message Like “CTE Imperva”
To verify the data available for pulling on the Imperva platform, log in to Imperva and go to
Application > Attack Analytics > Incidents
.
To verify the details of a particular incident, click
More details.
To verify the Retracted IoCs, check the logs for IoC Retraction. Example:
message Like [Retraction]:
You can filter the retracted IoCs from the platform using the
filter: sources.source Is equal “<plugin configuration name>” && sources.retracted Is equal true
Note
The IoCs that fall under the Retraction Interval or marked as false-positive on the Imperva platform will be marked as Retracted: Yes in Cloud Exchange.
Note
Sharing result will only be marked if the IoCs are pulled from source plugin after creating the sharing configuration.
Validate the Push
Here you can see IoCs were added to the URL list on your Netskope Tenant.
Some of the shared IoCs got marked as retracted, so it was deleted from the list.
Troubleshooting the Imperva Plugin
Unable to pull IoCs from the Imperva platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IOCs are available on the platform to pull.
IoCs are not available for the given configuration parameters (like Initial Range).
What to do:
Identity your root cause from above and follow the appropriate steps to resolve the issue.
No IOCs are available on the platform to pull:
Check if the IoCs are
available on the platform
to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the Imperva platform, check if you have data for the given time range.
In this Topic
Imperva Plugin for Threat Exchange

---
## Creating a Threat Protection Policy for Blocking DNS over HTTPS
**URL:** https://docs.netskope.com/en/creating-a-threat-protection-policy-for-blocking-dns-over-https/
**Last Modified:** 2026-02-11T19:38:47+00:00
**Scraped:** 2026-08-11T07:44:11.777111+00:00

Creating a Threat Protection Policy for Blocking DNS over HTTPS - Netskope Technical Documentation
Creating a Threat Protection Policy for Blocking DNS over HTTPS
Netskope recommends creating a security policy (i.e., [Utility] Block DNS over HTTPS) that blocks DNS operating over port 443 (HTTPS) due to its incompatibility for steering. This policy will block silently. Netskope recommends placing this policy with your other Threat Protection policies.
Recommended Threat Protection Policy
DNS over HTTPS is not a supported protocol for Netskope steering (CASB/NGSWG/NPA) and can be compromised by malicious actors. Therefore, Netskope recommends configuring a policy to steer and block this traffic.
Go to
Policies
>
Real-time Protection
.
Click
New Policy
and then
Cloud App Access
.
On the
Real-time Protection Policy
page:
Source
: Click
X
on the right to change scope to
Any
.
Destination
: Ensure it’s
Application
or
Cloud App
, and select
DNS over HTTPS
. Ensure the
Activities & Constraints
is
Any
.
Profile & Action
: Choose the following.
Action
: Choose
Block
.
Template
: Choose a custom
template
that doesn’t send a notification and blocks silently.
Set Policy
: Enter a name for the policy.
To learn more about any of these fields:
Real-time Protection Policies
.
Click
Save
and then
Apply Changes
.
In this Topic
Creating a Threat Protection Policy for Blocking DNS over HTTPS

---
## Darktrace Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/darktrace-plugin-for-threat-exchange/
**Last Modified:** 2026-04-10T00:26:25+00:00
**Scraped:** 2026-08-11T07:45:53.130007+00:00

Darktrace Plugin for Threat Exchange - Netskope Technical Documentation
Darktrace Plugin for Threat Exchange
This document explains how to configure the Darktrace v1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin fetches IoCs of type Domains, FQDNs, Hostnames, IPv4 and IPv6 from the
Watched Domains and IPs
page in Darktrace. This plugin supports sharing Domains, FQDNs, Hostnames, IPv4 and IPv6 to
Watched Domains and IPs
page. This plugin supports pull and push retraction of IoCs from Darktrace.
Prerequisites
A Netskope tenant (or multiple, for example, production and development/test instances)
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange
plugin already configured
Darktrace instance
Connectivity to the following hosts: https://
<region>
.cloud.darktrace.com/
Darktrace Plugin Support
This plugin fetches IoCs of type Domains, FQDNs, Hostnames, IPv4 and IPv6 from the
Watched Domains and IPs
page in Darktrace. This plugin supports sharing Domains, FQDNs, Hostnames, IPv4 and IPv6 to
Watched Domains and IPs
page. This plugin supports pull and push retraction of IoCs from Darktrace.
Fetched Indicator Types
Shared Indicator Types
Domains
FQDNs
Hostnames
IPv4
IPv6
Domains
FQDNs
Hostnames
IPv4
IPv6
Mappings
Pull Mappings
Cloud Exchange Fields
API Fields
Description
value
name
–
type
hostname
Darktrace provides type (hostname) only when the IOC is marked as hostname. For other types we will use regex to find the IOC type. If the IOC does not match any of the provided regex then it is marked with URL type.
Reputation
strength
–
Comments
description
description field value + strength field value
Reputation Mappings for Pulled IoCs
Input (Darktrace Strength)
Output (Cloud Exchange Reputation)
1-10
1
11-20
2
21-30
3
31-40
4
41-50
5
51-60
6
61-70
7
71-80
8
81-90
9
91-100
10
Push Mappings
API Field
Cloud Exchange Field/Default Values
Description
addlist
value
List of IOCs to be shared to Darktrace
strength
reputation
–
description
Netskope CE |
<source_plugin_name>
Source label
hostname
true/false
Value selected in the Exact Hostname action parameter.
iagn
true/false
Value selected in Flag for Response action parameter.
Reputation Mappings for Shared IoCs
Input (Cloud Exchange Reputation)
Output (Darktrace Strength)
1
10
2
20
3
30
4
40
5
50
6
60
7
70
8
80
9
90
10
100
IoC Retraction
IoC Retraction (Pull): Indicators will be fetched from Darktrace and in the subsequent pull cycles if some indicators are deleted on Darktrace, then they will be marked as Retraced in Netskope Cloud Exchange.
IoC Retraction (Push): Retracted indicators present on Cloud Exchange will be deleted from
<third-party platform>
during sharing.
Note
In the Darktrace plugin,
IoCs will be retracted based on the source provided in plugin configuration.
IoCs will be deleted from the source name that is used in action configuration.
Retraction Type
Supported Retraction Type
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
Yes
Permissions
You need these permissions:
Edit Domains
Visualizer
Edit Tags
API Details
List of APIs used
Use Case
Method
Endpoint
Fetch Source names
GET
/intelfeed
Pull IoCs
GET
/intelfeed
Push IoCs
POST
/intelfeed
Delete IoCs
POST
/intelfeed
Fetch Source Names
API Endpoint:
/intelfeed
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.0.1-cte-darktrace-v1.0.0
Query Parameters
Key
Value
sources
true
Sample Response
[
"Default",
"threatintel",
"external",
"cloud-exchange",
"netskope"
]
Pull IoCs
API Endpoint:
/intelfeed
Method:
GET
Headers
Key
Value
User-Agent
netskope-ce-6.0.1-cte-darktrace-v1.0.0
Authorization
Bearer
<Bearer Token>
Query Parameters
Key
Value
Description
source
<source_name>
Name of source provided in the configuration parameter
fulldetails
true
–
Sample API Response
[
{
"name": "101.44.42.56",
"strength": "45",
"description": "malicious IP",
"source": "threat"
},
{
"name": "db-08a3ed2f40.corp-internal.local",
"hostname": true,
"strength": "45",
"description": "malicious hostname",
"source": "threat"
},
]
Push IoCs
Endpoint:
/intelfeed
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.1-cte-darktrace-v1.0.0
Request Body
{
"addlist": "malsite.malware.com,exploit.com,76.83.2.190",
"description": "Netskope CE |
<3rd party plugin name>
",
"strength": 50,
"source": "external-source"
}
Sample API Response
{
"response": "SUCCESS",
"added": 3,
"updated": 0,
"addedList": [
"malsite.malware.com",
"exploit.com",
"76.83.2.190"
]
}
Delete IoCs
API Endpoint:
/intelfeed
Method:
POST
Headers
Key
Value
User-Agent
netskope-ce-6.0.1-cte-darktrace-v1.0.0
Request Body
{
"removeentry": "db-08a3ed2f40.corp-internal.local",
"source": "threatintel"
}
Sample API Response
{
    "response": "SUCCESS"
}
Performance Matrix
Here is the performance reading conducted by pulling and sharing 100K indicators from/to Darktrace on a Large Cloud Exchange stack with these specifications.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Indicator fetched from Darktrace
~40k IoCs per minute
Indicators shared with Darktrace
~40k IoCs per minute
User Agent
netskope-ce-6.0.1-cte-darktrace-v1.0.0
Workflow
Create a user on Darktrace.
Get your Public Token and Private Token.
Configure the Darktrace plugin.
Configure a Business Rule.
Configure Sharing.
Validate the Darktrace plugin.
Watch a Video
Click play to watch a video:
Create a User on Darktrace
Log in to your Darktrace instance and go to
Admin > Permissions Admin
.
Go to
Created Accounts
and click
Create new user
.
Enter a username and password, and then click
User Template
.
For Select a user template, select None.
Make sure all toggles are checked on the
Threat Tray Behavior Categories
page.
Make sure all toggles are checked on the
Flags
page.
Provide Edit Domains, Visualizer, and Edit Tags permissions, and then click
Summary
.
Click
Create new account
.
Get your Public Token and Private Token
Log in with the user account you just created and go to
Account Settings
.
Click
API Access
and copy the generated Public and Private tokens. These are needed for configuring the Darktrace plugin.
Configure the Darktrace Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Darktrace v1.0.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name
: Plugin configuration name.
Sync Interval
: Interval to fetch data from this plugin source.
Indicator Aging Criteria:
Expire indicators after a specific time.
Override Reputation
: Set value to override reputation of indicators received from this configuration. Leave empty to keep default.
Enable SSL Validation
: Enable SSL Certificate validation.
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameters determine how tags are stored for indicators pulled for this configuration.
Click
Next
and enter the Configuration Parameters:
Base URL
: Base URL of Darktrace instance.
Public Token
: Public token generated from the Darktrace platform.
Private Token
: Private token generated from the Darktrace platform.
Source Name:
Name of the Intel Feed source from where the IoCs are to be pulled. Enter only one source name for this parameter. Available sources can be found on the
Intel > Watched Domains
page.
Enable Polling:
Enable/Disable polling Threat IoCs from Darktrace. Disable if you only need to push Threat IoCs to Darktrace.
Click
Save
.
Configure a Threat Exchange Business Rule for Darktrace
A Business Rule is used to filter out the indicators that are to be shared. In order to share IoCs with Darktrace, create a business rule:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Enter a Rule name and select the fields for which you want to filter the IoCs.
Click
Save
.
Configure Threat Exchange Sharing for Darktrace
Add an IoC to the Intel Feed Source Action. To configure the Sharing:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select a Source (Source from which you want to share data to Darktrace), a Business Rule, and a Destination.
Select the Target value and set Action parameters per your requirements.
Source Name:
Intel feed source name where IoCs are to be added. Select
Create new source
to create a new source on Darktrace platform.
Custom Source:
Name of the custom source to create if it does not exist.
Exact Hostnames:
Set to true to treat the added items as hostnames rather than domains. Does not apply to IoC of type IP. Note that, for IoCs of type hostname, it will always be True even if the sharing is configured with Exact Hostnames as false.
Flag for Response:
Enable automatic triggering of a Darktrace Autonomous Response Action if the entry is seen.
Click
Save
.
Validate the Darktrace Plugin
Validate the Pull
Indicators from Darktrace are pulled from the
Watched Domains and IPs
page.
Note
IoCs having descriptions except
Netskope CE | Netskope Threat Exchange
will be pulled from Darktrace.
Log in to your Darktrace instance.
Go to
Intel > Watched Domains
.
Indicators stored in Cloud Exchange can be verified at
Threat Exchange > Threat IoCs
. Search for the Darktrace IoCs by filtering indicators from Darktrace.
Example: Add a query like
“sources.source Is equal “CTE Darktrace” && type IN (“<IOC_TYPE>”)”
.
Note
IoCs with Exact host name as True on Darktrace will be stored with the same hostname on Cloud Exchange.
You can also verify the indicators pulled in Cloud Exchange from the logs available at
Logging
.
Validate the Push
Shared IoCs to Darktrace can be verified from logs available at
Logging
.
To validate shared IoCs on Darktrace, go to
Intel > Watched Domains
.
To verify the original source of indicator from which this was pulled in Cloud Exchange and shared to Darktrace, check the Description for that particular IoC.
For example, if an indicator is shared from Threat Exchange to Darktrace, then it will be shown as
Netskope CE | Netskope Threat Exchange
on Darktrace’s Description for that particular IoC.
When the IoCs shared from Darktrace to the Netskope Tenant or 3rd-party platform are retracted, then they will be marked as
<plugin-config-name>: retracted
in the Retraction Result. If they are not deleted from the 3rd-party platform, the Retraction Result will be pending.
Validate the Retraction
To verify the Retracted IoCs from Darktrace, check the logs for IoC Retraction. Example: “
message Like CTE Darktrace [configuration_name] [Retraction]
“.
Note
The IoCs that are deleted on Darktrace will be marked as Retracted in Cloud Exchange.
Example log for push retraction:
To check the retracted IoCs in Cloud Exchange, go to
Threat IoCs
and search for
“sources.source Like “CTE Darktrace” && sources.retracted Is equal true”
.
This plugin also supports push retraction, which means IoCs pulled from Netskope or 3rd-party platforms that were shared to the Darktrace platform, and were marked as retracted in Cloud Exchange, will also get deleted from the shared platform if that platform supports deletion of IoCs. You can verify the same through the Retraction result field.
Note
IoCs will be deleted on Darktrace based on the Source Name selected in the sharing configuration if there are multiple actions configured for one Darktrace.
Troubleshooting the Darktrace Plugin
Receiving an error while configuring the plugin
There’s an issue while configuring the Darktrace plugin.
What to do:
Make sure the correct credentials are provided. Follow these
steps
to generate credentials.
Unable to pull data from the Darktrace Platform
You are getting an error while pulling the data from the Darktrace plugin.
What to do:
Go to the Logging page, verify if any error has occurred and try to fix it.
Verify that the Public Token and Private Token are not expired.
Not able to share IoCs from Cloud Exchange to Darktrace
If you are not able to share IoCs from Netskope to Darktrace, that could be due to one of these reasons:
The IoCs present for Netskope plugin are of invalid type.
Public Token and Private Token are expired.
What to do:
Make sure that valid types of IoCs are present. Darktrace supports sharing Domains, FQDNs, Hostnames, IPv4 and IPv6 to the
Watched Domains and IPs
page.
Make sure that Public Token and Private Token are not expired.
Known Behaviors
Darktrace plugin will pull all IoCs from the set source name in each sync interval, due to which the Hit count for all IoCs will increase by 1 after each sync interval.
While deleting IoC from Darktrace (Push Retraction) source name is a required parameter.
Example:
Initial State:
Action 1 (Source 1)
: Filters and pushes IoCs 1–5.
Action 2 (Source 2)
: Filters and pushes IoCs 6–10.
Retraction Event:
IoCs 1, 2, 6, and 7 are marked as retracted.
Current Core Behavior:
The plugin receives the list of retracted indicators like [1, 2, 6, 7] and a list of configured actions [Action 1(Source 1), Action 2 (Source 2)]
The Conflict:
The plugin does not know that 1 and 2 belong to Source 1, while 6 and 7 belong to Source 2. It has no context to perform a targeted retraction.
Current Implementation:
The plugin will delete IoCs 1,2,6 and 7 from both Source 1 and Source 2.
Another issue related to the above case is that if no actions are configured (were initially configured and IoCs were pushed using them, but are now deleted), IoC retraction will not work because there an not any Source names to delete IoCs from.
To prevent a scenario where an IoC is pushed and pulled repeatedly between systems, the plugin implements a specific safeguard:
If the IoC pushed from Cloud Exchange is pulled back in Cloud Exchange from Darktrace, it would be due to the description of the IoC being updated manually or via any 3rd-party entity source API. The plugin checks the IoC description and looks for the source label, like
Netskope CE|<plugin_name>
, when an IoC is pushed from Cloud Exchange. If this source label is not found in the IoC, it will be pulled in Cloud Exchange.
In this Topic
Darktrace Plugin for Threat Exchange

---
## Threat Hunting
**URL:** https://docs.netskope.com/en/threat-hunting/
**Last Modified:** 2026-07-06T18:51:59+00:00
**Scraped:** 2026-08-11T07:48:42.205806+00:00

Threat Hunting - Netskope Technical Documentation
Threat Hunting
Threat hunting makes additional detections available that Netskope hasn’t or won’t deploy yet for network threat blocking because the detection is likely to alert on non-malicious traffic. These detections are a source of insight into network traffic to investigate suspicious behavior, which supports threat hunting and response and investigation use cases.
You can view the available threat hunting detections based on your enabled traffic types. Click
Configure in IPS
to modify this setting.
Detection Configuration
In the
Detection Configuration
tab, you can manually enable or disable threat hunting detections in alert or block mode on a case by case basis. If you enable threat hunting mode, some high-fidelity detections might be enabled by default, and lower-fidelity detections might be disabled by default.
To enable or disable threat hunting detections:
Go to
Settings
>
Threat Protection
>
Threat Hunting
.
Under
Detection Configuration
, search for a threat hunting detection by its
Detection Name
or
Detection ID
.
Click
for the threat hunting detection you want to overwrite the default behavior for.
In the
Edit Detection Details
window:
Detection
: The threat hunting detection you are modifying the default behavior for. You can’t modify this field.
Detection ID
: The ID of the threat hunting detection. You can’t modify this field.
Status
: Choose to enable or disable the threat hunting detection.
Action
: Choose one of the following actions.
Alert
: Netskope allows the detected traffic and generates an alert in Skope IT.
Block
: Netskope blocks the detected traffic.
Click
Save
.
You can click
Show all overwritten detections
to only display the detections you’ve edited.
Module Detection
In the
Module Detection
tab, you can enable or disable detection modules, which provide detection based on behavioral techniques including machine learning and advanced analytics that detect network anomalies.
Beacon Detection
: Enable to identify evasive Command and Control (C2) beaconing, which traditional defenses often miss, by analyzing network traffic for anomalies indicative of beaconing and focusing on behavior rather than static detections for early compromise detection.
The default action is
Alert
. You can’t modify this setting.
HTML Smuggling
Detection
: Enable to prevent HTML smuggling attacks and detect embedded malicious payloads inside HTML/JS files.
The default action is
Alert
. You can’t modify this setting.
Viewing Threat Hunting Alerts
You can view threat hunting detections on the Skope IT
Alerts
page (
Skope IT
>
Alerts
). To view them, select
Threat Hunting
for the
Alert Type
filter.
In this Topic
Threat Hunting

---
## VMRay Plugin for Threat Exchange
**URL:** https://docs.netskope.com/en/vmray-plugin-for-threat-exchange/
**Last Modified:** 2026-07-06T21:45:48+00:00
**Scraped:** 2026-08-11T07:48:43.455031+00:00

VMRay Plugin for Threat Exchange - Netskope Technical Documentation
VMRay Plugin for Threat Exchange
Release Notes
1.0.0 (Required minimum CE version for this is 6.0.0)
Added
Initial release.
Pull: Yes (URL, Domain, FQDN, IPv4, SHA256 and MD5)
Push: Yes (URL, Domain, FQDN and IPv4)
Pull Retraction: Yes (Based On time and verdict type)
Push Retraction: Yes (Based On tag)
This document explains how to configure the VMRay v1.0.0 plugin with the Threat Exchange module of the Netskope Cloud Exchange platform. This plugin is used to pull IoC(s) of type Domain (FQDN, Domain), IPv4, URL, and File Hash (MD5, SHA256) from Malicious and Suspicious Sample IoCs of submissions in VMRay platform. This plugin supports sharing IoC(s) of type URL, Domain, FQDN, and IPv4 to VMRay via the Upload File or URL submission page. This plugin supports pull and push retraction of indicators from VMRay.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Threat Exchange plugin
already configured.
A
File Profile
on your Netskope tenant.
A
URL List
on your Netskope tenant.
A
Destination Profile
on your Netskope tenant.
A
Private App
on your Netskope tenant.
A
DNS Profile
on your Netskope Tenant.
A VMRay instance with an account.
Connectivity to the following host:
https://<region>.cloud.vmray.com
VMRay Plugin Support
This plugin is used to pull IoC(s) of type Domain (FQDN, Domain), IPv4, URL, and File Hash (MD5, SHA256) from Malicious and Suspicious Sample IoCs of submissions in VMRay platform. This plugin supports sharing IoC(s) of type URL, Domain, FQDN, and IPv4 to VMRay via the Upload File or URL submission page. This plugin supports pull and push retraction of indicators from VMRay.
Fetched Indicator Types
Shared Indicator Types
Domain, FQDN, IPv4, URL, MD5, SHA256
URL, Domain, FQDN, IPv4
IoC Retraction
The VMRay plugin supports pull and push retraction of indicators.
Type
Description
IoC Retraction (Pull)
Yes
IoC Retraction (Push)
Yes
Mappings
Severity Mappings
Netskope Severity
VMRay numeric_severity
unknown
0
low
1
low
2
medium
3
high
4
critical
5
Pull Indicators Mappings
Netskope Fields
VMRay Observable Fields
Value (domain)
domain
Value (url)
url
Value (ip)
ip_address
Value (md5)
md5_hash
Value (sha256)
sha256_hash
Severity
numeric_severity
Tags
submission_tags, verdict, protocols
Comments
severity
Extended Information
submission_webif_url
Push Indicators Mappings
VMRay Observable Field
Netskope Indicator Field
sample_url
indicator.value
tags
indicator.tags
submission_metadata.ce_severity
indicator.severity
submission_metadata.ce_reputation
indicator.reputation
submission_metadata.ioc_comment
indicator.comments
Permissions
You need a VMRay user role created with these permissions:
Allow Console Access
Allow REST API access
View own submissions, analyses, and samples
View shared submissions, analyses, and samples
Submit samples, manage own jobs, reanalyze old analytics, and regenerate analysis reports
Delete all submissions in this account including associated analyses.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/rest/submission/finish_time/{start}~{end}
GET
Fetch submissions by finish time window
/rest/sample/{sample_id}/iocs
GET
Fetch IoCs for a given sample
/rest/sample/submit
POST
Submit an indicator to VMRay
/rest/submission/search
GET
Search submissions for push retraction
/rest/submission/{submission_id}
DELETE
Delete a submission for push retraction
Fetch Submissions by Finish Time
Endpoint:
GET /rest/submission/finish_time/{start}~{end}
Request Headers:
Key
Value
Authorization
api_key {api_token}
Content-Type
application/json
Query Parameters:
Parameter
Description
submission_verdict
Filter by verdict: malicious or suspicious
_limit
Number of results per page
_order
Sort order (asc)
_min_id
Cursor for pagination
Sample Response:
{
    "continuation_id": 9084709,
    "data": [
        {
            "submission_analysis_cache_ids": [
                16989547
            ],
            "submission_analyzer_mode_ai_based_phishing_detection": "normal",
            "submission_analyzer_mode_analysis_caching": "smart",
            "submission_analyzer_mode_analyzer_mode": "static_dynamic",
            "submission_analyzer_mode_archive_action": "sample",
            "submission_analyzer_mode_detonate_links_in_documents": "smart",
            "submission_analyzer_mode_detonate_links_in_emails": "smart",
            "submission_analyzer_mode_disk_image_action": "compound_sample",
            "submission_analyzer_mode_enable_reputation": true,
            "submission_analyzer_mode_enable_whois": false,
            "submission_analyzer_mode_id": 2245384,
            "submission_analyzer_mode_known_benign": false,
            "submission_analyzer_mode_known_malicious": false,
            "submission_analyzer_mode_max_dynamic_analyses_per_sample": "default",
            "submission_analyzer_mode_max_recursive_samples": "10",
            "submission_analyzer_mode_ml_based_phishing_detection": "normal",
            "submission_analyzer_mode_triage": "custom",
            "submission_analyzer_mode_triage_error_handling": null,
            "submission_api_key_id": 2168,
            "submission_billing_type": "analyzer",
            "submission_comment": "Netskope CE",
            "submission_consumed_quota": 0,
            "submission_created": "2026-06-11T09:25:10",
            "submission_deletion_date": "2026-12-08T09:25:10",
            "submission_dll_call_mode": null,
            "submission_dll_calls": null,
            "submission_document_password": null,
            "submission_enable_custom_av": false,
            "submission_enable_local_av": false,
            "submission_filename": "sample.url",
            "submission_finish_time": "2026-06-11T09:25:11",
            "submission_finished": true,
            "submission_has_errors": false,
            "submission_has_recursive_errors": false,
            "submission_id": 14513326,
            "submission_interface_name": "CloudExchange",
            "submission_ip_id": 1242821,
            "submission_ip_ip": "14.96.106.184",
            "submission_job_cache_ids": [],
            "submission_known_configuration": false,
            "submission_number_cached_analyses": 2,
            "submission_number_created_jobs": 0,
            "submission_original_filename": null,
            "submission_original_url": "test-domain.com",
            "submission_parent_submission_id": null,
            "submission_prescript_force_admin": false,
            "submission_prescript_id": null,
            "submission_priority": 7,
            "submission_quota_type": "report",
            "submission_recursive": false,
            "submission_reputation_job_cache_id": null,
            "submission_reputation_lookup_cache_id": 5414252,
            "submission_reputation_mode": "auxiliary",
            "submission_retention_period": 180,
            "submission_sample_id": 14106863,
            "submission_sample_md5": "376df3380181be9ec57644b1de15f751",
            "submission_sample_sha1": "3b286b862ca8a4753b0bf0cd4337e80dd807028c",
            "submission_sample_sha256": "31ace2defcf47c077fcd906556427144a695bd3d3621adfa21ec437e3a5cce22",
            "submission_sample_ssdeep": "3:N1KKATZI:CKqI",
            "submission_sample_verdict": "malicious",
            "submission_sample_verdict_reason_code": null,
            "submission_sample_verdict_reason_description": null,
            "submission_score": 83,
            "submission_severity": "malicious",
            "submission_shareable": false,
            "submission_status": "success",
            "submission_submission_metadata": "{\"ce_severity\": \"SeverityType.UNKNOWN\", \"ce_reputation\": \"5\", \"ioc_comment\": \"Application: Nuance\"}",
            "submission_submitter_email": null,
            "submission_system_time": null,
            "submission_tags": [
                "Unsanctioned",
                "Netskope-CE-Microsoft-Defender-for-Cloud-Apps"
            ],
            "submission_triage_error_handling": null,
            "submission_triage_stage": null,
            "submission_triaged": null,
            "submission_type": "api",
            "submission_used_cache": true,
            "submission_user_account_id": 767,
            "submission_user_account_name": "Netskope NFR",
            "submission_user_account_subscription_mode": null,
            "submission_user_account_type": "integration_partner",
            "submission_user_email": "vdesai@netskope.com",
            "submission_user_id": 7752,
            "submission_verdict": "malicious",
            "submission_verdict_reason_code": null,
            "submission_verdict_reason_description": null,
            "submission_webif_url": "https://us.cloud.vmray.com/samples/14106863",
            "submission_whois_mode": "disabled"
        },
    ],
}
Fetch Sample IOCs
Endpoint:
GET /rest/sample/{sample_id}/iocs
Request Headers:
Key
Value
Authorization
api_key {api_token}
Content-Type
application/json
Query Parameters:
Parameter
Description
all_artifacts
Set to true to retrieve all artifacts
ioc_verdict
Filter by verdict: malicious or suspicious
Sample Response:
{
  "data": {
    "sample_child_relations": [
    ],
    "sample_child_relations_truncated": false,
    "sample_child_sample_ids": [
    ],
    "sample_classifications": [
    ],
    "sample_clusters": [
    ],
    "sample_container_type": null,
    "sample_created": "2026-05-20T14:05:23",
    "sample_display_url": "http://www.vnic.co/khach-hang.html",
    "sample_emailhash": null,
    "sample_filename": "sample.url",
    "sample_filesize": 34,
    "sample_highest_vti_score": 20,
    "sample_highest_vti_severity": "not_suspicious",
    "sample_id": 13812243,
    "sample_imphash": null,
    "sample_is_multipart": false,
    "sample_last_md_score": null,
    "sample_last_reputation_severity": "unknown",
    "sample_last_vt_score": null,
    "sample_md5hash": "d11ae5bb4de4608ba67a6524cf9312a7",
    "sample_parent_relations": [
    ],
    "sample_parent_relations_truncated": false,
    "sample_parent_sample_ids": [
    ],
    "sample_password_protected": false,
    "sample_pe_signature": null,
    "sample_priority": 7,
    "sample_score": 0,
    "sample_severity": "not_suspicious",
    "sample_sha1hash": "ee2216546a31be8ab2ebb7da990ffe0c4a919862",
    "sample_sha256hash": "8cc6bc85842af39dfeb13539d80a8c38376215e8ae1ea81f5b477b30d55d1045",
    "sample_ssdeephash": "3:N1KJS4H5nEiLk0:Cc4ZEo/",
    "sample_threat_names": [
    ],
    "sample_type": "URL",
    "sample_url": "http://www.vnic.co/khach-hang.html",
    "sample_verdict": "clean",
    "sample_verdict_reason_code": null,
    "sample_verdict_reason_description": null,
    "sample_vti_score": 20,
    "sample_webif_url": "https://us.cloud.vmray.com/samples/13812243"
  },
  "result": "ok"
}
Submit Indicator to VMRay
Endpoint:
POST /rest/sample/submit
Request Headers:
Key
Value
Authorization
api_key {api_token}
Content-Type
application/json
Query Parameters:
Parameter
Description
sample_url
The indicator value to submit
Request Body:
{
  "tags": "Netskope-CE-{plugin_name},{tag1},{tag2}",
  "submission_metadata": "{\"ce_severity\": \"HIGH\", \"ce_reputation\": \"\", \"ioc_comment\": \"\"}",
  "enable_reputation": "true",
  "live_interaction": "false",
  "comment": ""
}
Sample Response:
{
  "data": {
    "errors": [
    ],
    "jobs": [
      {
        "job_account_id": 767,
        "job_analyzer_id": 7,
        "job_analyzer_name": "vmray_web",
        "job_bill_id": 13908651,
        "job_bill_type": "analyzer",
        "job_configuration_description": "Chrome",
        "job_configuration_id": 254,
        "job_configuration_name": "web_root",
        "job_created": "2026-06-15T09:27:14",
        "job_document_password": null,
        "job_enable_custom_av": false,
        "job_enable_local_av": false,
        "job_id": 17321711,
        "job_jobrule_id": 112,
        "job_jobrule_sampletype": "URL",
        "job_parent_analysis_id": null,
        "job_prescript_force_admin": false,
        "job_prescript_id": null,
        "job_priority": 9,
        "job_quota_type": "report",
        "job_reputation_job_id": null,
        "job_sample_id": 13824015,
        "job_sample_md5": "e9e73f6ae078cfd5a24bddc40043e4b3",
        "job_sample_sha1": "960aebe953a46e9fba63203feb38566001d3648a",
        "job_sample_sha256": "9e4cf379b7ccedcf1bf521fee850d9c9de96153a691c05e50a7a9d8333495515",
        "job_sample_ssdeep": "3:N8SP3uwVQokyMAwMIIPBhMJNMPHxXgxQeOE6fKP3u2NerLIK:2SmwVQjMDPBWORktOE6fKm24fIK",
        "job_snapshot_id": 1,
        "job_snapshot_name": "def",
        "job_static_config_id": null,
        "job_status": "queued",
        "job_statuschanged": "2026-06-15T09:27:14",
        "job_submission_id": 14547658,
        "job_submission_ids": [
          14547658
        ],
        "job_system_time": null,
        "job_tracking_state": "//waiting",
        "job_type": "full_analysis",
        "job_user_email": "vdesai@netskope.com",
        "job_user_id": 7752,
        "job_vm_description": "VMRay Web Analyzer",
        "job_vm_id": 42,
        "job_vm_name": "win-web",
        "job_vmhost_id": null,
        "job_vminstance_num": null,
        "job_vnc_url_html": null,
        "job_vnc_url_wss": null
      }
    ],
    "md_jobs": [
    ],
    "reputation_jobs": [
      {
        "reputation_job_account_id": 767,
        "reputation_job_bill_id": null,
        "reputation_job_created": "2026-06-15T09:27:14",
        "reputation_job_id": 6861365,
        "reputation_job_priority": 9,
        "reputation_job_sample_id": 13824015,
        "reputation_job_sample_md5": "e9e73f6ae078cfd5a24bddc40043e4b3",
        "reputation_job_sample_sha1": "960aebe953a46e9fba63203feb38566001d3648a",
        "reputation_job_sample_sha256": "9e4cf379b7ccedcf1bf521fee850d9c9de96153a691c05e50a7a9d8333495515",
        "reputation_job_sample_ssdeep": "3:N8SP3uwVQokyMAwMIIPBhMJNMPHxXgxQeOE6fKP3u2NerLIK:2SmwVQjMDPBWORktOE6fKm24fIK",
        "reputation_job_status": "queued",
        "reputation_job_statuschanged": "2026-06-15T09:27:14",
        "reputation_job_submission_id": 14547658,
        "reputation_job_submission_ids": [
          14547658
        ],
        "reputation_job_user_email": "vdesai@netskope.com",
        "reputation_job_user_id": 7752
      }
    ],
    "samples": [
      {
        "sample_child_sample_ids": [
        ],
        "sample_container_type": null,
        "sample_created": "2026-05-21T05:22:01",
        "sample_display_url": "https://docs.google.com/spreadsheet/viewform?formkey=dGg2Z1lCUHlSdjllTVNRUW50TFIzSkE6MQ,https://docs.google.com, https://api.google.com",
        "sample_emailhash": null,
        "sample_filename": "9e4cf379b7ccedcf1bf521fee850d9c9de96153a691c05e50a7a9d8333495515url",
        "sample_filesize": 135,
        "sample_id": 13824015,
        "sample_imphash": null,
        "sample_is_multipart": false,
        "sample_md5hash": "e9e73f6ae078cfd5a24bddc40043e4b3",
        "sample_parent_sample_ids": [
        ],
        "sample_password_protected": false,
        "sample_pe_signature": null,
        "sample_priority": 7,
        "sample_sha1hash": "960aebe953a46e9fba63203feb38566001d3648a",
        "sample_sha256hash": "9e4cf379b7ccedcf1bf521fee850d9c9de96153a691c05e50a7a9d8333495515",
        "sample_ssdeephash": "3:N8SP3uwVQokyMAwMIIPBhMJNMPHxXgxQeOE6fKP3u2NerLIK:2SmwVQjMDPBWORktOE6fKm24fIK",
        "sample_type": "URL",
        "sample_url": "https://docs.google.com/spreadsheet/viewform?formkey=dGg2Z1lCUHlSdjllTVNRUW50TFIzSkE6MQ,https://docs.google.com, https://api.google.com",
        "sample_webif_url": "https://us.cloud.vmray.com/samples/13824015",
        "submission_filename": "https://docs.google.com/spreadsheet/viewform?formkey=dGg2Z1lCUHlSdjllTVNRUW50TFIzSkE6MQ,https://docs.google.com, https://api.google.com"
      }
    ],
    "static_jobs": [
    ],
    "submissions": [
      {
        "submission_analysis_cache_ids": [
        ],
        "submission_analyzer_mode_ai_based_phishing_detection": "normal",
        "submission_analyzer_mode_analysis_caching": "disabled",
        "submission_analyzer_mode_analyzer_mode": "reputation_static_dynamic",
        "submission_analyzer_mode_archive_action": "sample",
        "submission_analyzer_mode_detonate_links_in_documents": "smart",
        "submission_analyzer_mode_detonate_links_in_emails": "smart",
        "submission_analyzer_mode_disk_image_action": "compound_sample",
        "submission_analyzer_mode_enable_reputation": true,
        "submission_analyzer_mode_enable_whois": true,
        "submission_analyzer_mode_id": 2254422,
        "submission_analyzer_mode_known_benign": false,
        "submission_analyzer_mode_known_malicious": false,
        "submission_analyzer_mode_max_dynamic_analyses_per_sample": "default",
        "submission_analyzer_mode_max_recursive_samples": "10",
        "submission_analyzer_mode_ml_based_phishing_detection": "normal",
        "submission_analyzer_mode_triage": "custom",
        "submission_analyzer_mode_triage_error_handling": null,
        "submission_api_key_id": 2170,
        "submission_billing_type": "analyzer",
        "submission_comment": "Pushed from Netskope CE Threat Exchange",
        "submission_consumed_quota": 0,
        "submission_created": "2026-06-15T09:27:14",
        "submission_deletion_date": "2026-12-12T09:27:14",
        "submission_dll_call_mode": null,
        "submission_dll_calls": null,
        "submission_document_password": null,
        "submission_enable_custom_av": false,
        "submission_enable_local_av": false,
        "submission_filename": "https://docs.google.com/spreadsheet/viewform?formkey=dGg2Z1lCUHlSdjllTVNRUW50TFIzSkE6MQ,https://docs.google.com, https://api.google.com",
        "submission_finish_time": null,
        "submission_finished": false,
        "submission_has_errors": null,
        "submission_has_recursive_errors": null,
        "submission_id": 14547658,
        "submission_interface_name": "Netskope Cloud Exchange",
        "submission_ip_id": 1218717,
        "submission_ip_ip": "103.108.207.58",
        "submission_job_cache_ids": [
        ],
        "submission_known_configuration": false,
        "submission_number_cached_analyses": 0,
        "submission_number_created_jobs": 3,
        "submission_original_filename": null,
        "submission_original_url": "https://docs.google.com/spreadsheet/viewform?formkey=dGg2Z1lCUHlSdjllTVNRUW50TFIzSkE6MQ,https://docs.google.com, https://api.google.com",
        "submission_parent_submission_id": null,
        "submission_prescript_force_admin": false,
        "submission_prescript_id": null,
        "submission_priority": 9,
        "submission_quota_type": "report",
        "submission_recursive": false,
        "submission_reputation_job_cache_id": null,
        "submission_reputation_lookup_cache_id": null,
        "submission_reputation_mode": "disabled",
        "submission_retention_period": 180,
        "submission_sample_id": 13824015,
        "submission_sample_md5": "e9e73f6ae078cfd5a24bddc40043e4b3",
        "submission_sample_sha1": "960aebe953a46e9fba63203feb38566001d3648a",
        "submission_sample_sha256": "9e4cf379b7ccedcf1bf521fee850d9c9de96153a691c05e50a7a9d8333495515",
        "submission_sample_ssdeep": "3:N8SP3uwVQokyMAwMIIPBhMJNMPHxXgxQeOE6fKP3u2NerLIK:2SmwVQjMDPBWORktOE6fKm24fIK",
        "submission_score": null,
        "submission_severity": null,
        "submission_shareable": false,
        "submission_status": "in_progress",
        "submission_submission_metadata": "{\"source_plugin\": \"Postman\"}",
        "submission_submitter_email": null,
        "submission_system_time": null,
        "submission_tags": [
          "multipleurls",
          "netskope-ce"
        ],
        "submission_triage_error_handling": null,
        "submission_triage_stage": null,
        "submission_triaged": null,
        "submission_type": "api",
        "submission_used_cache": false,
        "submission_user_account_id": 767,
        "submission_user_account_name": "Netskope NFR",
        "submission_user_account_subscription_mode": null,
        "submission_user_account_type": "integration_partner",
        "submission_user_email": "vdesai@netskope.com",
        "submission_user_id": 7752,
        "submission_verdict": null,
        "submission_verdict_reason_code": null,
        "submission_verdict_reason_description": null,
        "submission_webif_url": "https://us.cloud.vmray.com/samples/13824015",
        "submission_whois_mode": "disabled"
      }
    ],
    "vt_jobs": [
    ],
    "whois_jobs": [
    ]
  },
  "result": "ok"
}
Search Submissions
Endpoint:
GET /rest/submission/search
Request Headers:
Key
Value
Authorization
api_key {api_token}
Content-Type
application/json
Query Parameters:
Parameter
Description
query
Search query, e.g. url == “{indicator.value}”
Sample Response:
{
  "data": [
    {
      "submission_analysis_cache_ids": [
      ],
      "submission_analyzer_mode_ai_based_phishing_detection": "normal",
      "submission_analyzer_mode_analysis_caching": "smart",
      "submission_analyzer_mode_analyzer_mode": "static_dynamic",
      "submission_analyzer_mode_archive_action": "sample",
      "submission_analyzer_mode_detonate_links_in_documents": "smart",
      "submission_analyzer_mode_detonate_links_in_emails": "smart",
      "submission_analyzer_mode_disk_image_action": "compound_sample",
      "submission_analyzer_mode_enable_reputation": true,
      "submission_analyzer_mode_enable_whois": false,
      "submission_analyzer_mode_id": 2245384,
      "submission_analyzer_mode_known_benign": false,
      "submission_analyzer_mode_known_malicious": false,
      "submission_analyzer_mode_max_dynamic_analyses_per_sample": "default",
      "submission_analyzer_mode_max_recursive_samples": "10",
      "submission_analyzer_mode_ml_based_phishing_detection": "normal",
      "submission_analyzer_mode_triage": "custom",
      "submission_analyzer_mode_triage_error_handling": null,
      "submission_api_key_id": 2168,
      "submission_billing_type": "analyzer",
      "submission_comment": "Netskope CE",
      "submission_consumed_quota": 1,
      "submission_created": "2026-06-11T07:38:05",
      "submission_deletion_date": "2026-12-08T07:38:05",
      "submission_dll_call_mode": null,
      "submission_dll_calls": null,
      "submission_document_password": null,
      "submission_enable_custom_av": false,
      "submission_enable_local_av": false,
      "submission_filename": "sample.url",
      "submission_finish_time": "2026-06-11T08:08:25",
      "submission_finished": true,
      "submission_has_errors": false,
      "submission_has_recursive_errors": false,
      "submission_id": 14512551,
      "submission_interface_name": "CloudExchange",
      "submission_ip_id": 1242821,
      "submission_ip_ip": "14.96.106.184",
      "submission_job_cache_ids": [
      ],
      "submission_known_configuration": false,
      "submission_number_cached_analyses": 0,
      "submission_number_created_jobs": 2,
      "submission_original_filename": null,
      "submission_original_url": "coincafe.com",
      "submission_parent_submission_id": null,
      "submission_prescript_force_admin": false,
      "submission_prescript_id": null,
      "submission_priority": 7,
      "submission_quota_type": "report",
      "submission_recursive": false,
      "submission_reputation_job_cache_id": null,
      "submission_reputation_lookup_cache_id": null,
      "submission_reputation_mode": "auxiliary",
      "submission_retention_period": 180,
      "submission_sample_id": 14106861,
      "submission_sample_md5": "b338596ef9b606d198109bd2840fd38a",
      "submission_sample_sha1": "8f51a039d9eb233ba29c65844f46bd82b77ebca4",
      "submission_sample_sha256": "8b6f8c062941cbb3fb43eed1331d8beaa9c7156705ffa5fcc3fda858c9811dba",
      "submission_sample_ssdeep": "3:N1KdKMy7LK:CIMy72",
      "submission_sample_verdict": "malicious",
      "submission_sample_verdict_reason_code": null,
      "submission_sample_verdict_reason_description": null,
      "submission_score": 100,
      "submission_severity": "malicious",
      "submission_shareable": false,
      "submission_status": "success",
      "submission_submission_metadata": "{\"ce_severity\": \"SeverityType.UNKNOWN\", \"ce_reputation\": \"5\", \"ioc_comment\": \"Application: Coincafe\"}",
      "submission_submitter_email": null,
      "submission_system_time": null,
      "submission_tags": [
        "Sanctioned",
        "Netskope-CE-Microsoft-Defender-for-Cloud-Apps"
      ],
      "submission_triage_error_handling": null,
      "submission_triage_stage": null,
      "submission_triaged": null,
      "submission_type": "api",
      "submission_used_cache": false,
      "submission_user_account_id": 767,
      "submission_user_account_name": "Netskope NFR",
      "submission_user_account_subscription_mode": null,
      "submission_user_account_type": "integration_partner",
      "submission_user_email": "vdesai@netskope.com",
      "submission_user_id": 7752,
      "submission_verdict": "malicious",
      "submission_verdict_reason_code": null,
      "submission_verdict_reason_description": null,
      "submission_webif_url": "https://us.cloud.vmray.com/samples/14106861",
      "submission_whois_mode": "disabled"
    }
  ],
  "result": "ok"
}
Delete Submission
Endpoint:
DELETE /rest/submission/{submission_id}
Request Headers:
Key
Value
Authorization
api_key {api_token}
Content-Type
application/json
Sample Response:
{
  "result": "ok"
}
Performance Matrix
This reading is conducted on a Large CE Stack with these specifications by pulling and pushing 100k IoCs.
Description
Specification
Stack Size
Large,
RAM: 32 GB,
Core: 16
Indicators fetched from VMRay
~6k per min
Indicators shared to VMRay
~100 per min
Note
The performance is done with only 100 indicators as the plugin will push indicators in batch on 1.
We have noticed that our instance had a limit of 1000 submissions created per month, so if your instance has such a limit, you might not be able to push indicators more than the limit. For more information refer to
troubleshooting
.
User Agent
netskope-ce-6.1.0-cte-vmray-v1.0.0
Workflow
Create Role and Assign it to a User
Generate API Token from VMRay
Configure Netskope Tenant
Configure the VMRay Plugin
Configure a Threat Exchange Business Rule for VMRay
Configure Sharing for Netskope and VMRay
Validate the VMRay Plugin
Watch a Video
Click play to watch a video.
Create Role and Assign it to a User
In VMRay, go to the
Settings > Accounts > General > Available Roles > Manage
.
Click
Create New Role.
Provide the name for the role and provide
permissions
.
Click
Save
.
The role is created, then assign this role to a user.
Go to the
Settings > Accounts > Active users.
Click on three dots for the User you want to attach the role and click
Assign Role.
Select the created role and click
Save
.
Generate an API Token from VMRay
Go to
Settings > Analysis > Interfaces > API Keys
.
Click
Create New API Key
.
Provide the name for the API Token and click
Save.
Copy the API token to use to configure the plugin.
For the permissions, you should have the token created using the account with these
permissions
.
Configure the VMRay Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
VMRay v1.0.0 (CTE)
plugin.
Enter the Basic Information:
Configuration Name:
The plugin configuration name.
Sync Interval:
The Interval to fetch data from this plugin and share data to this plugin from other sources.
Aging Criteria:
Expires indicators after specific time.
Override Reputation:
Set a value to override reputation of indicators received from this configuration. Leave empty to keep default.
Tags Aggregate Strategy:
Choose whether to append new tags to existing IoC(s) or overwrite them. This configuration parameter determines how tags are stored for indicators pulled for this configuration.
Enable SSL Validation:
Enable SSL certificate verification.
Click
Next
and enter the Configuration Parameters:
Base URL:
The Base URL of your VMRay instance. For example: https://
<region>
.cloud.vmray.com
API Token:
The API Token for authenticating with the VMRay platform that you created previously.
Type of Verdict:
Select the verdict types of IoC(s) to pull from VMRay submissions.
Type of Threat Data to Pull:
Select the types of IoC(s) to pull from VMRay. Leave empty to pull all supported IoC(s) types.
Enable Polling:
Enable/Disable polling Threat IoC(s) from VMRay. Disable if you only need to push Threat IOC(s) to VMRay.
Enable Push Retraction:
Enable/Disable push retraction of IoC(s) from VMRay. When enabled, previously pushed IOC(s) to VMRay will be deleted when retracted in CE. Note: All related submission data and analyses will be deleted from your account as well.
Retraction Interval (in days):
The number of days to use as the retraction interval for VMRay submissions retraction. This parameter is applicable only if
IoC Retraction
is enabled in your Threat Exchange settings. Valid values are in range from 1 to 100000 days.
Initial Range (in days):
The number of days to pull indicators for the initial run. Valid values are in range from 1 to 100000 days.
Click
Save
. The configuration appears on the
Threat Exchange > Plugins
page.
Configure a Threat Exchange Business Rule for VMRay
To share indicators fetched from the VMRay to Threate Exchange, you need to have a business rule that will filter out the indicators that you want to share. To configure a business rule:
In Threat Exchange, go to
Business Rules
and click
Create New Rule
.
Add the filter according to your requirements in the rule and then click
Save
.
Configure Sharing for Netskope and VMRay
In order to add Sharing configuration, a third-party Threat Exchange plugin, like
CrowdStrike
, has to be configured before proceeding. You need both a source and destination plugin (configurations) to add a Sharing configuration.
VMRay plugin supports the following sharing:
Add to URL Basic Analysis:
This will add URLs, IPv4s, Domains and FQDNs to basic analysis and create a submission for the same.
To share IoCs from the VMRay to Cloud Exchange:
In Threat Exchange, go to
Sharing
and click
Add Sharing Configuration
.
Select your Source Configuration (CTE Netskope), Business Rule, Destination Configuration (CTE VMRay), and Target.
Provide this information:
Reputation Analysis:
Select Reputation Analysis for URL basic analysis. Set to True to find out if this sample is known to be malicious or benign. Default value is True.
Submission Comment:
Optional comment for URL basic analysis. Allowed maximum 255 characters.
Click
Save
.
Note
As the VMRay plugin supports pulling URL, IPv4, Domain, FQDN, SHA256, and MD5, you can perform these actions on Netskope using these indicators:
Add to URL List
Add to File Hash List
Add to Private App
Add to Destination Profile
Add to DNS Profile
Validate the VMRay Plugin
Validate the Pull
Validate in VMRay
To check available indicators on VMRay, you can follow the below steps
Log in to the VMRay instance.
From the left panel, go to the
Submission
page.
To check the IoCs under the submission, click on any of the submissions and go to the IoCs section.
Validate in Cloud Exchange
Pulled data will be listed on the Threat IoCs page. You can filter the IoCs pulled from the platform using the filter:
sources.source Like “<plugin configuration name>”
.
To verify pulled logs on Cloud Exchange, go to
Logging
and search logs from the VMRay plugin.
Validate the Pull Retraction
The pull retraction for the plugin is done based on the indicators available on the VMRay instance provided in the plugin configuration and retraction interval. If any indicator is removed from the VMRay platform or it is falling outside the retraction interval, it will be marked as retracted in Cloud Exchange.
You can filter the logs related to retraction by using the filter:
message Contains “[Retraction]”
.
To validate the retracted IoCs on the Threat IoCs page, apply the filter:
Retracted Is equal Yes
, along with the source filter for the plugin configuration name.
When IoCs pulled from VMRay are marked as retracted
yes
, they will be marked as
“\<plugin-config-name\>: retracted”
in the Retraction Result if that IoC was already shared to a Netskope tenant or third-party platform and that destination plugin supports push retraction.
Validate the Push
After the sharing configuration is complete, wait for the next sync cycle.
Log in to your VMRay instance and go to
Submissions
.
Search for the submitted indicator and confirm the submission appears with the
Netskope-CE-{plugin_name}
tag in the submission details.
Validate the Push Retraction
Ensure
Enable Push Retraction
is set to
Yes
in the VMRay plugin configuration.
Verify the logs in logging page with filter like
message Contains “[Retraction]”
.
Log in to your VMRay instance and go to
Submissions
. Confirm the corresponding submissions have been deleted.
IoCs that were marked Retracted
Yes
in Cloud Exchange will also be deleted from VMRay after the push retraction is processed. All related submission data and analyses will also be deleted from your VMRay account.
Troubleshooting the VMRay Plugin
Receiving error while configuring the plugin or pulling data
If you are receiving the error while configuring the plugin, this issue may be due to the Base URL and API Token being invalid or deleted.
What to do:
Check the plugin credentials if the Base URL and API Token is valid. If it is valid, check if the
credentials
that you are using are still available on VMRay.
Unable to pull IoCs from the VMRay platform
After the plugin configuration, if the IoCs are not pulled from the platform, it might be due to one of these reasons:
No IoCs are available on the platform to pull
IoCs are not available for the given configuration parameters (like Types of Threat data to pull).
What to do:
Identity your root cause from above and follow these steps to resolve the issue.
No IoCs are available on the platform to pull:
Check if the IoCs are
available on the platform
to pull. If available, check the resolution for the next point.
IoCs are not available for the given time range
If the IoCs are available on the platform to pull, but the plugin has not pulled the IoCs in Cloud Exchange, check the number of days mentioned in the initial range parameter of the plugin configuration. On the VMRay platform, check if you have data for the given time range.
If the data is still available for the given time range, it might be possible that the IoCs for the provided filter in the plugin configuration are not available, so check the values from the plugin configuration parameter and filter the same on the VMRay platform.
Unable to share IoCs to VMRay
If you are getting this error while sharing indicators to VMRay:
CTE VMRay [CTE VMRay]: An error occured while sharing indicator(s) to VMRay due to quota exceeded.
It is due to the quota limitation on the VMRay platform.
What to do:
Verify the quota used on your VMRay instance from the
Reports Usage
dashboard.
In this Topic
VMRay Plugin for Threat Exchange

---
## Threat Protection
**URL:** https://docs.netskope.com/en/threat-protection/
**Last Modified:** 2026-05-07T18:16:07+00:00
**Scraped:** 2026-08-11T07:50:24.612547+00:00

Threat Protection
Modern threats need a multi-layered security approach able to defend organizations from known threats and zero-days with the same level of efficacy. Netskope has built a comprehensive threat protection framework that allows organizations to defend against malware through different engines including viruses, worms, trojans, ransomware, keyloggers, rootkits, downloaders, backdoors, botnets, spyware, info stealers, adware, mobile threats, potentially unwanted software, fileless malware, crypto-mining, wipers, packers, installers, malicious websites, URLs, malicious scripts (XSS, etc.), HTML smuggling, documents, macros, archives (up to 9 levels), exploits, credential compromise, domains (including Punycode, hijacking, compromise, typosquatting, character substitution, etc.), command and control, data exfiltration, beaconing, and other attacker artifacts, traffic, and malicious infrastructure.
The Standard Inline Threat engines support:
Signature-Based Antivirus (AV)
Web IPS
Command and Control (C2 or C&C) detection
Machine learning-based detection and real-time blocking for Portable Executable malware, HTML smuggling, and phishing sites and domains.
The Advanced Deepscan Threat engines support:
Machine learning-based detection and real-time blocking for Microsoft Office files.
Advanced Heuristics Analysis
Cloud Sandboxing
While Signature-Based AV, IPS, DNS, callbacks, and threat intelligence indicators can detect and block malware in real time with Netskope fast scan, the Advanced Heuristics and Sandboxing engines require more time to analyze samples with deep scan. A malware detected by the deep scan engine can’t be blocked at the first occurrence. However, its hashes and convicted URLs /domains are shared globally in the Netskope Cloud to block inline:
Multiple times an hour for customers with the Advanced Threat Protection license.
Up to one hour for customers with the Standard Threat Protection license.
The following architecture diagram illustrates how Netskope Threat Protection detects malware for your organization:
You can integrate external intelligence into Netskope’s threat protection engines with malicious hashes, domains, or URLs using
Threat Exchange
.
Standard Versus Advanced Threat Protection
The table below breaks down the differences between the Standard and Advanced Threat Protection features:
Feature
Standard Threat Protection
Advanced Threat Protection
Perform real-time ML-based scanning for portable executable files, HTML smuggling, phishing sites and domains, and prevent patient zero threats.
X
X
Leverage advanced threat engines, such as Cloud Sandbox, to corroborate AV and ML detections.
X
X
Leverage web IPS (including Microsoft Active Protections, CVE matching, and C2).
X
X
Detect Compromised Credentials Incidents with Dark Web monitoring.
X
X
Perform ML-based scanning and blocking for Microsoft Office files.
X
Analyze files undetected by AV or ML in advanced threat engines. Netskope supports 30+ file types, including Portable Executables (e.g., .exe), Microsoft Office, PDF files, batch files, archive files (e.g., zip, 7z, tar), Microsoft Visio, RTF, Flash, HTML, and Java Applets.
X
View Sandbox reports, detailed forensics, MITRE ATT&CK mapping, and advanced heuristic analysis.
X
Submit files to the Cloud Sandbox via Sandbox API.
X
Use file hashes to query detections via RetroHunt API.
X
Receive patient zero alerts for newly discovered advanced threat detections.
X
Prevent patient zero events by creating policies to only release the file if the advanced threat engines determine it’s benign.
X
Threat Protection for Cloud Storage Apps
As organizations move to the cloud, they are increasingly susceptible to modern day threats like malware and ransomware. One of the initial transitions to the cloud for organizations is in the cloud storage category, with a number of them using SaaS apps such as Microsoft OneDrive for Business, Google Drive, Box, Dropbox, etc. Files get into these cloud storage apps in a number of ways, like through third-party vendors, attachments saved from emails, and files uploaded from desktops. Not all files get scanned by endpoint systems. Netskope provides threat protection for files stored in enterprise-managed applications in the cloud storage category.
When a malicious file is found in a SaaS app, you have three choices based on severity: send a Skope IT alert, quarantine the file, or apply a malware remediation profile to a policy. With quarantine, Netskope uses the quarantine profile in
Settings
>
Threat Protection
>
API-enabled Protection
as the quarantine folder and tombstone. The malicious file is zipped and protected with a password to prevent users from inadvertently downloading the file. Netskope then notifies the admin specified in the profile. The quarantine option is only available for introspection mode. You can enable it in
Settings
>
API-enabled Protection
by selecting
Malware
,
API Data Protection
, and
Quarantine
for your instance.
With Standard Threat Protection, you scan your organization for malware, and with Advanced Threat Protection, you can  scan for ransomware. However, if you don’t have the Advanced Threat Protection license enabled, you can use threat protection with Real-time Protection and API Data Protection policies to detect files with malware as well as Risk Insights to detect malicious sites.
Netskope Security Check
To verify if your Threat Protection policies are working properly and to see some examples of alerts go through the Netskope cloud, you can run tests with the
Netskope Security Check
.
More Resources
Advanced Threat Protection
Endpoint Detection and Response
Create a Remediation Profile
Creating a Threat Protection Policy for API Data Protection
Creating a Malware Detection Profile
Creating a File Hash List
Creating a Threat Protection Policy for Real-time Protection
Malware and Malicious Sites Pages
Malware Severity Levels and Detection Types
Creating a Threat Protection Policy for Patient Zero
Viewing Patient Zero Events
In this Topic
Threat Protection
