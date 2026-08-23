# Netskope Docs — Dlp
_Generated: 2026-08-23 07:44 UTC_
_Pages: 87_

---
## Award-Winning DLP Features
**URL:** https://docs.netskope.com/en/award-winning-dlp-features/
**Last Modified:** 2025-08-31T01:51:00+00:00
**Scraped:** 2026-08-23T06:34:39.402432+00:00

Award-Winning DLP Features
Feature
Description
Reduce false positives
Prevent data leakage from SaaS, IaaS, and web with accuracy and precision. Supports more than 1,000 file types, more than 3,000 data identifiers, proximity analysis, fingerprinting, exact match, OCR, and more, instrumented using a flexible and intuitive wizard-style interface.
Find and control sensitive data at rest
Find sensitive data resident in managed services such as AWS, Microsoft Office 365 OneDrive, Box, Google Drive, Dropbox, and more. Take action on data that violates policy.
Closed-loop incident management
Respond quickly and thoroughly to policy violations, with workflows to facilitate end-to-end incident management process, detailed forensics, and event-by-event incident history.
Compliance templates
Use 40 predefined policy templates to identify sensitive data in accordance with regulations. Templates include (but are not limited to): AMRA, EC Directive, EU-GDPR, GLBA, HIPAA, PCI-DSS, PHI, PII, PHIPA, PIPEDA, SSN Confidentiality Act, US FTC Rules, etc.
Role-based access controls
Customizable role-based access controls, including predefined admin. and analyst roles. Additional privacy controls include data obfuscation and automatic filtering of certain kinds of traffic.
In this Topic
Award-Winning DLP Features

---
## Create a DLP policy to search an entire data repository and apply predefined labels per Enterprise data classification rules
**URL:** https://docs.netskope.com/en/create-a-dlp-policy-to-search-an-entire-data-repository-and-apply-predefined-labels-per-enterprise-data-classification-rules/
**Last Modified:** 2025-09-01T12:58:18+00:00
**Scraped:** 2026-08-23T06:34:55.723306+00:00

Create a DLP policy to search an entire data repository and apply predefined labels per Enterprise data classification rules
Prerequisites for the API protection use cases
Roles/actors in the use cases
Tenant creation
User accounts created
CASB API Protection connected to CSP (Cloud Service Provider)
CSP (Cloud Service Provider) administrator
Cloud governance team
Security Analyst
To create a DLP policy for an API protected service, follow the steps shown below:
Navigate to Policies > API Data protection > New Policy.
Select the API protected service for which the DLP policy is required.
Under the Users section, select  ‘All Users’.
Under Content section, select ‘All Sharing Options’ and ‘All File Types’.
Under DLP, select the pre-defined DLP profile that you would like to apply.
To learn more:
Understanding API Protection
In this Topic
Create a DLP policy to search an entire data repository and apply predefined labels per Enterprise data classification rules

---
## Create DLP policies for sensitive data for a specific OU from a user and provide user coaching
**URL:** https://docs.netskope.com/en/create-dlp-policies-for-sensitive-data-for-a-specific-ou-from-a-user-and-provide-user-coaching/
**Last Modified:** 2025-08-31T01:51:05+00:00
**Scraped:** 2026-08-23T06:35:12.291778+00:00

Create DLP policies for sensitive data for a specific OU from a user and provide user coaching
Learn how to create a DLP policy using Real-time protection policies –
Creating a policy
.
To learn more:
Real-time protection policies
and
real time protection policy variables
In this Topic
Create DLP policies for sensitive data for a specific OU from a user and provide user coaching

---
## DLP – Protect state for Managed App Activities
**URL:** https://docs.netskope.com/en/dlp-protect-state-for-managed-app-activities/
**Last Modified:** 2025-09-01T13:11:30+00:00
**Scraped:** 2026-08-23T06:35:19.269661+00:00

DLP – Protect state for Managed App Activities
This section outlines specific use cases to protect managed app activities. Check back because new use cases are added periodically.
Create a DLP policy to search an entire data repository and apply predefined labels per Enterprise data classification rules
Create a policy to identify sensitive data in specific locations (public, external or non-approved groups)
Create a policy to alert or block sharing of sensitive data with external Teams
Create a policy to find encrypted or password protected files
Create and apply a legal hold policy if required
In this Topic
DLP – Protect state for Managed App Activities

---
## DLP Scans on AWS Accounts
**URL:** https://docs.netskope.com/en/dlp-scans-on-aws-accounts/
**Last Modified:** 2025-08-31T01:51:11+00:00
**Scraped:** 2026-08-23T06:35:22.774219+00:00

DLP Scans on AWS Accounts
To perform a DLP scan on AWS/Azure/GCP accounts, ensure that DLP profiles are included in the policies. To create a DLP policy:
Navigate to
Policies
>
API Data Protection
>
New Policy
.
Select the specific instance to which the desired DLP profile has to be applied.
Apply the DLP profile.
In this Topic
DLP Scans on AWS Accounts

---
## DLP Scans on AWS, Azure, and GCP Accounts
**URL:** https://docs.netskope.com/en/dlp-scans-on-cloud-saas/
**Last Modified:** 2026-06-25T19:32:43+00:00
**Scraped:** 2026-08-23T06:35:23.938465+00:00

DLP Scans on AWS, Azure, and GCP Accounts - Netskope Technical Documentation
DLP Scans on AWS, Azure, and GCP Accounts
DLP Scans on GCP Accounts
To perform a DLP scan on AWS, Azure, or GCP accounts, ensure that DLP profiles are included in the policies. The following screenshots show an AWS instance, but can be applied to Azure or GCP as well.
To create a DLP policy:
Navigate to
Policies
>
API Data Protection
>
New Policy
.
Select the specific instance to which the desired DLP profile has to be applied.
Apply the DLP profile.
In this Topic
DLP Scans on AWS, Azure, and GCP Accounts

---
## DLP Scans on Azure Accounts
**URL:** https://docs.netskope.com/en/dlp-scans-on-azure-accounts/
**Last Modified:** 2025-08-31T01:51:11+00:00
**Scraped:** 2026-08-23T06:35:27.524881+00:00

DLP Scans on Azure Accounts
To perform a DLP scan on AWS/Azure/GCP accounts, ensure that DLP profiles are included in the policies. To create a DLP policy:
Navigate to
Policies
>
API Data Protection
>
New Policy
.
Select the specific instance to which the desired DLP profile has to be applied.
Apply the DLP profile.
In this Topic
DLP Scans on Azure Accounts

---
## Create a Custom DLP Profile
**URL:** https://docs.netskope.com/en/create-a-custom-dlp-profile/
**Last Modified:** 2026-06-25T19:19:21+00:00
**Scraped:** 2026-08-23T06:39:35.794489+00:00

Create a Custom DLP Profile
Creating a DLP profile involves selecting a file profile and then providing a DLP rule, content classification, or fingerprint rule.
File profile section allows you to include or exclude specific files based on different attributes of a file. You can use existing file profiles or create a new file profile.
Rule|Classification section allows you to include predefined DLP rules, custom DLP rules, Machine Language (ML)-based file classifiers, or a fingerprint rule. You can combine the DLP rules and Classifiers to match all or any of the above to detect sensitive content.
Using predefined DLP rules simplifies the task of creating DLP profiles. To use custom DLP rules, first go to
Select Custom Entities
and create the rules, so they appear under DLP rules in the Create Profile dialog box. Alternatively, you can click the ‘+’ symbol under DLP Rule in the Rule|Classification section to create a new rule from here.
To include ML-based file classifiers in the profile, select from the list of predefined classifiers.
To include Fingerprint rules in the DLP profile, go to
Use Fingerprint Classification
and create the Fingerprint rules so they appear in the fingerprint rules text box in the Rule|Classification section. Alternatively, you can click the ‘+’ symbol under Fingerprint Rule in the Rule|Classification section to create a new rule from here.
Rules within a condition are evaluated on an AND-basis and conditions are evaluated on an OR-basis against other conditions.
To create a custom DLP profile,
Go to
Policies > Profiles > DLP
in the Netskope UI.
Click
New Profile
.
Under File Profiles, select a file profile you want to include or exclude using the match criteria. You can select from the list of file profiles or create a new file profile. For information on creating a new file profile, see
Adding a File Profile
. Click
Next
.
Under Rule|Classification, select predefined or custom DLP rules. Let’s say you want to match content that contains the social security number (SSN) with a dash-delimited no delimiter, and a space delimiter. Select the following predefined DLP rules, SSN (Dash Delimited),
SSN (No Delimiter)
, and
SSN (Space Delimited)
.
Click the ‘+’ symbol to create a new custom DLP rule.
Select the ML based classifiers to be included in the content match so that text in images can be identified using the machine language-based models. For example, to match a Résumé, select the
Résumé
classifier in the Personal Identifiers classification which identifies résumés.
Select a fingerprint rule to improve the accuracy of the content match. The rule identifies content that resembles the content defined in the fingerprint classification included in the fingerprint rule.
Click the ‘+’ symbol to create a new fingerprint rule.
Select the
Advanced
button on the Rule|Classification screen to trigger a policy when you want the content to match either or both, the selected DLP rules and ML based classifiers. Click
Next
.
Enter a profile name and click
Save
.
Clone a DLP Profile
Cloning allows you to create new DLP profiles from existing DLP profiles. When you clone a predefined or custom DLP profile, the profile properties are copied and displayed in the Edit DLP Profile dialog box. The DLP profile can be modified to create a new custom DLP profile.
To clone a predefined or custom profile, on the DLP Profiles page click the menu icon (three dots) and then click the clone icon.
In this Topic
Create a Custom DLP Profile

---
## Create a Custom DLP Rule
**URL:** https://docs.netskope.com/en/creating-a-custom-dlp-rule/
**Last Modified:** 2026-06-25T19:14:26+00:00
**Scraped:** 2026-08-23T06:40:06.615622+00:00

Create a Custom DLP Rule - Netskope Technical Documentation
Create a Custom DLP Rule
Creating a DLP rule involves selecting predefined data identifiers, creating a new custom data identifier, validating the identifier against a data set, fine-tuning the rule, setting the scan options, and defining the severity threshold.
You can create a new DLP rule or clone an existing rule. When you clone a predefined or custom DLP rule, the data identifiers and settings are copied and displayed in the Create Rule dialog box.
To create a new DLP rule:
Go to
Policies > Profiles > DLP > Edit Rules > Data Loss Prevention
in the Netskope UI.
Click
New Rule
.
To clone a predefined or custom rule, on the DLP Rules page click the Menu icon and then, click the
Clone
icon.
In this Topic
Create a Custom DLP Rule

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117716/
**Last Modified:** 2025-08-31T01:40:51+00:00
**Scraped:** 2026-08-23T06:41:00.957528+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117840/
**Last Modified:** 2025-09-01T12:30:42+00:00
**Scraped:** 2026-08-23T06:41:02.195329+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117929/
**Last Modified:** 2025-09-01T12:33:25+00:00
**Scraped:** 2026-08-23T06:41:05.791574+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117863/
**Last Modified:** 2025-09-01T12:34:08+00:00
**Scraped:** 2026-08-23T06:41:06.972310+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
Note
Enabling DLP will evaluate files only. All structured data will be ignored for this policy. To evaluate all structured data, disable DLP.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117951/
**Last Modified:** 2025-09-01T12:32:07+00:00
**Scraped:** 2026-08-23T06:41:08.146716+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117885/
**Last Modified:** 2025-09-01T12:30:47+00:00
**Scraped:** 2026-08-23T06:41:09.313594+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117983/
**Last Modified:** 2025-09-01T12:31:42+00:00
**Scraped:** 2026-08-23T06:41:10.485856+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
Note
Netskope does not scan emails in deleted/trash folder. Netskope will continue to scan emails in sent folder.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-118036/
**Last Modified:** 2025-09-01T12:31:11+00:00
**Scraped:** 2026-08-23T06:41:11.655252+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-118130/
**Last Modified:** 2025-09-01T12:31:15+00:00
**Scraped:** 2026-08-23T06:41:12.821961+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
Note
Netskope does not scan emails in deleted/trash folder. Netskope will continue to scan emails in sent folder.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-118108/
**Last Modified:** 2025-09-01T12:32:12+00:00
**Scraped:** 2026-08-23T06:41:13.992217+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-120387/
**Last Modified:** 2025-09-01T12:31:20+00:00
**Scraped:** 2026-08-23T06:41:15.192136+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-118083/
**Last Modified:** 2025-09-01T12:31:46+00:00
**Scraped:** 2026-08-23T06:41:16.368291+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP Profiles
**URL:** https://docs.netskope.com/en/dlp-profiles/
**Last Modified:** 2026-06-25T17:36:59+00:00
**Scraped:** 2026-08-23T06:41:17.540085+00:00

DLP Profiles - Netskope Technical Documentation
DLP Profiles
A DLP profile is a collection of predefined or custom DLP rules, classifiers, and custom fingerprint rules. If any of the rules or classifiers match the content, then the DLP profile flags the content as a policy violation. Using predefined profiles let you start evaluating loss of critical data in the cloud immediately. Creating new DLP profiles and rules enables you to refine custom methods of prevention. For insight about building custom DLP profiles and rules, see
DLP Best Practices Runbook
.
DLP profiles come with a predefined set of rules for well-known compliance regulations like Payment Card Information (PCI), Protected Health Information (PHI), and Personally-Identifiable Information (PII), to name a few. You can also create custom DLP rules using a large dictionary of predefined data identifiers and custom regex expressions. The DLP engine scans file contents to identify sensitive data based on the configured policy. There is a flexible set of policy actions that can be enforced if sensitive data is identified in the content.
DLP profiles can be used when creating a Real-time Protection or API Data Protection policy. You can apply multiple DLP profiles to a policy where each profile contains a set of predefined or custom DLP rules. Whenever a DLP profile matches a policy, the resulting incident is shown in the Incidents page under
Incidents > DLP
. To learn more:
About DLP
.
When you configure a Real-time Protection policy with multiple DLP profiles and the content matches multiple profiles, the policy performs the most restrictive action associated with the DLP profiles that match for that policy. The resulting incidents lists all the profiles that matched along with their corresponding forensic information. An alert is generated for each rule associated with any of the matched DLP profiles.
For example, if the Real-time Protection policy contains three DLP profiles – PCI, PII, and PHI where, the following actions are defined.
Example DLP Profile
Example Action
PCI
Block
PII
Block
PHI
User Alert
If the content matches all three profiles, then DLP blocks the content. DLP also generates an alert and a single incident associated with the PCI, PII, and PHI violations.
Create a DLP profile using predefined or custom DLP rules, classifiers, and fingerprint rules to test if they find the sensitive data you’re trying to protect. Create a custom DLP profile when the predefined DLP profiles do not meet your requirements.
The DLP Profiles page lists all the predefined and custom profiles. Profiles can be filtered by selecting a Profile Type, Industry, and Region from the drop-down lists on the top of the page. You can also use the search field to find profiles by entering a part of the profile name in the search field.
To open the DLP Profiles page, go to
Policies > Profiles > DLP
in the Netskope UI.
Password-Protected Files
When a DLP profile cannot inspect a file because the file is password protected or AIP protected, then DLP creates a single bypass alert in SkopeIT Alerts page. This behavior eliminates duplicate bypass alerts from being created for each profile or policy. The policy name in the alert is set to
All DLP Policies
.
In addition to the SkopeIT alert, DLP also creates an incident whenever there is a profile match, and the file is password protected or AIP protected.
Select a Predefined DLP Profile
Create a Custom DLP Profile
Edit a Custom DLP Profile
In this Topic
DLP Profiles

---
## DLP
**URL:** https://docs.netskope.com/en/dlp/
**Last Modified:** 2025-09-01T12:30:37+00:00
**Scraped:** 2026-08-23T06:41:18.705444+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
Multi-part-upload must be enabled to support uploading files larger than 128MB on box. Contact Netskope support for more information.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## DLP Rules
**URL:** https://docs.netskope.com/en/dlp-rules/
**Last Modified:** 2026-06-25T19:22:14+00:00
**Scraped:** 2026-08-23T06:41:21.020336+00:00

DLP Rules - Netskope Technical Documentation
DLP Rules
DLP rules can contain one or more of these elements:
Predefined data identifiers
Custom data identifiers
Note
The data identifiers have been renamed to provide meaningful names and description. They are also organized into meaningful categories and include tags which make them easy to search.
For a complete list of the new names and categories of predefined data identifiers and their definitions, see
DLP Predefined Identifiers
.
Keyword identifiers from a dictionary file
RegEx expressions
Exact match criteria.
The DLP Rules page lists all the predefined and custom rules. Rules can be filtered by selecting a Rule Type and Region from the drop-down lists on the top of the page. You can also use the search field to find rules by entering a part of the name in the search field.
To open the DLP Rules page, go to
Policies > Profiles > DLP > Edit Rules
and select
Data Loss Prevention
in the Netskope UI.
Migrate Existing Custom Rules
To migrate your existing custom rules to use the new names of identifiers, you must edit the rule.
Click on a custom rule to open the
Edit DLP Rule
screen.
Click
Next
on the following screens until you see
Update Rule
.
Click
Update Rule
and then click
Apply Changes
.
DLP Entity
Create a Custom DLP Rule
Select a DLP Entity
Select an Exact Match File
Use Advanced Expressions
Select Scan Options
Select a Severity Threshold
Name the DLP Rule
Column Classification Rules
In this Topic
DLP Rules

---
## Edit a Custom DLP Profile
**URL:** https://docs.netskope.com/en/edit-a-custom-dlp-profile/
**Last Modified:** 2026-06-25T19:19:22+00:00
**Scraped:** 2026-08-23T06:41:23.364160+00:00

Edit a Custom DLP Profile - Netskope Technical Documentation
Edit a Custom DLP Profile
The custom DLP profiles are listed on the DLP Profiles page. Click on the custom DLP profile to edit the profile. Follow the screens to edit the profile.
In this Topic
Edit a Custom DLP Profile

---
## Endpoint Data Loss Prevention
**URL:** https://docs.netskope.com/en/endpoint-data-loss-prevention/
**Last Modified:** 2026-06-25T17:37:02+00:00
**Scraped:** 2026-08-23T06:41:46.890500+00:00

Endpoint Data Loss Prevention - Netskope Technical Documentation
Endpoint Data Loss Prevention
Note
Contact your Sales Representative to enable this feature for your account.
Netskope Endpoint Data Loss Prevention (Endpoint DLP) provides data protection at the endpoint by utilizing Netskope’s cloud DLP capabilities. You can use Endpoint DLP to monitor and govern USB storage devices and printers connected to your endpoint. Endpoint DLP is an optional add-on capability to the Netskope Client and does not require deploying and managing a separate client or agent on the endpoint.
With Endpoint DLP, you can create Device Control and Content Control policies. Device Control policies enable granular control over which devices are allowed and which users can access them. Whereas, Content Control policies enable the full use of the Netskope DLP engine to inspect and control data movement between an endpoint and a USB mass storage device or printer.
Endpoint DLP allows you to manage and govern endpoints to prevent sensitive content from being transferred to USB storage devices, printers, Bluetooth, or network file share. You can:
Govern endpoint devices by creating device control, content control, and file origin policies.
Monitor endpoint activities and block or trigger alerts when users insert or remove USB storage devices, transfer sensitive files to USB storage devices, set up and configure printers, and print documents.
Respond to incidents and alert the user of their actions.
Coach the user through custom notification messages by allowing them to justify their actions or cancel them.
See:
Endpoint DLP Device and Content Control Policies
Benefits
Endpoint DLP provides the following benefits:
Minimizes resource utilization at the endpoint for a better user experience.
Inspects content for DLP violations for a stronger security posture.
Leverages the DLP policy framework to generate alerts and incidents.
Requirements
Endpoint DLP runs on Windows or macOS.
If on Windows, Endpoint DLP requires Windows 10 or Windows 11 on 64-bit processors. Windows 11 Enterprise Multi-Session is not supported.
Adobe Acrobat and Adobe Acrobat Reader on Windows are supported for versions
supported by Adobe
.
If on macOS, Endpoint DLP requires macOS 14, 15, or 26 (Sonoma, Sequoia, Tahoe) running either on Intel x64 or Apple Silicon AND Full Disk Access.
Ensure you do the following before configuring Endpoint DLP:
Provision users for the Netskope Client.
Enable Endpoint DLP for the Netskope Client configurations.
Enabling Endpoint DLP on the Client for macOS
Endpoint DLP on macOS requires
Full Disk Access
to function properly. Follow the following instructions to provide the process with
Full Disk Access
. If the client machine is not managed through an MDM profile, then the user must manually provide the
Full Disk Access
to the EPDLP client.
For information regarding
Full Disk Access
, see
Apple’s documentation regarding Controlling app access to files in macOS
.
MDM Deployments on macOS
The Full Disk Access workflow is covered for the following MDM solutions:
JAMF
Workspace ONE (Formerly Airwatch)
Microsoft Intune
Kandji
Common steps are:
1. Install DLP on any test machine once.
2. Open Terminal and run the following command:
codesign -dr - /Library/Application\ Support/Netskope/EPDLP/Netskope\ Endpoint\ DLP.app
3. This will generate the following output:
Executable=/Library/Application Support/Netskope/EPDLP/Netskope Endpoint DLP.app/Contents/MacOS/Netskope Endpoint DLP
designated => anchor apple generic and identifier "com.netskope.epdlp.client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
4. Copy the substring after the “designated =>” portion. For example,
anchor apple generic and identifier "com.netskope.epdlp.client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
JAMF
See
JAMF
for more information.
5. Open the JAMF Dashboard and navigate to Computer > Configuration and open the configuration that was created for NSclient.
6. Search for
Privacy Preference Policy Control
.
7. Use “com.netskope.epdlp.client” for
Identifier
, “Bundle ID” for
Identifier Type
and your copied substring in step 4 for
Code Requirement
.
8. Select “SystemPolicyAllFiles” under
APP OR SERVICE
and “Allow” under Access.
9. Save the configuration profile
Workspace ONE (Formerly Airwatch)
See
Deploy Client on macOS Using Workspace ONE
for more information.
5. Navigate to
Resources > Profiles
and
Baselines > Profiles
.
6. Under
Privacy Preferences
, use “com.netskope.epdlp.client” for
Identifier
, “Bundle ID” for
Identifier Type
and your copied substring in step 4 for
Code Requirement
. Set
System Policy All Files
to “Allow”.
Microsoft Intune
See
Deploy Client on macOS Using Intune
for more information
5. Navigate to
Dashboard > Devices | macOS > Configuration Profiles
.
6. Create an
Identifier
with “com.netskope.epdlp.client”.
7. Set
Allowed
to “True. Use “your copied substring in step 4 for
Code Requirement
and bundle ID” for
Identifier Type
. Set
System Policy All Files
to “Allow”.
Kandji
5. Navigate to
Privacy Policy
.
6. use “com.netskope.epdlp.client” for
Identifier
, “Bundle ID” for
Identifier Type
and your copied substring in step 4 for
Code Requirement
. Set
System Policy All Files
to “Allow”.
Full Disk Access Error
If Full Disk Access is not enabled for the EPDLP client, the following error message may pop up after installing the EPDLP package through
STAgent.pkg
The
Proceed
button opens the Full Disk Access Settings in
System Preferences
to add and enable the EPDLP client.
Enable the Full Disk Access to EPDLP client by adding and enabling “Netskope Endpoint DLP” in Full Disk Access settings.
System Preferences -> Security & Privacy -> Privacy -> Full Disk Access
Enabling Endpoint DLP
Endpoint DLP is an add-on feature for the Netskope Client. To enable Endpoint DLP for the Netskope Client, contact your sales representative.
Once enabled, ensure you do the following before configuring Endpoint DLP:
Provision users for the Netskope Client
.
Enable Endpoint DLP for the Netskope Client configurations
.
Original File Access
Similar to DLP incidents, when an EPDLP Incident is created, the original file that caused the incident will be available for download in WebUI.
Note that this applies to only to DLP content scan incidents, and the “Forensics enabled” configuration must be enabled.
.
See the following links for more information on Original File Access:
Enable a Forensic Profile
and
Downloading DLP files
In this Topic
Endpoint Data Loss Prevention

---
## Name the DLP Rule
**URL:** https://docs.netskope.com/en/name-the-dlp-rule/
**Last Modified:** 2026-06-25T19:14:31+00:00
**Scraped:** 2026-08-23T06:43:37.565921+00:00

Name the DLP Rule
After specifying all the options for a DLP rule, give it a name that helps you know it’s purpose. On the Set Rule page, enter a name and click
Save
.
In this Topic
Name the DLP Rule

---
## Select a Predefined DLP Profile
**URL:** https://docs.netskope.com/en/select-a-predefined-dlp-profile/
**Last Modified:** 2026-06-25T19:19:20+00:00
**Scraped:** 2026-08-23T06:45:33.338951+00:00

Select a Predefined DLP Profile
There are over 30 predefined DLP profiles available to use in a policy. These profiles are built from rules that incorporate standard combinations of data identifiers, and many are based on regulatory compliance standards. Predefined DLP profiles cannot be modified.
To view the predefined DLP profiles, go to
Policies > Profiles > DLP
in the Netskope UI.
Click on a profile to view the rules applied. For example, selecting the predefined profile, The Social Security Number Confidentiality Act 2000 shows the DLP rules that define this profile.
To use any of the predefined DLP profiles, simply select one when creating a policy.
Limitations for
NEW
Predefined Profiles, Rules, Entities, Columnar Classification Rules, and File Classifiers
Netskope incorporates general maintenance as part of its service, which includes the introduction of
new
Predefined Profiles
,
Rules
,
Entities
,
Columnar Classification Rules
, and
File Classifiers
for the respective subscribed capabilities of DLP Standard (L2), DLP Advanced (L3).
We advise customers to
only
utilize these newly introduced
Predefined
Profiles
,
Rules
,
Entities
,
Columnar
Classification Rules
File Classifier
exclusively
after the deployment has been completed across all Management Plane (MPs) and Data Plane (DPs) to mitigate the potential for detection inconsistencies. Customers leveraging appliances such the DLP On Demand Appliance, DLP Appliance with DSPM, or DLP Appliance with AI Gateway must also ensure that the DLP Appliance is updated to facilitate the functionality of the
new
Predefined Profiles
,
Rules
,
Entities
,
Columnar Classification Rules
File Classifiers
Existing
Predefined Profiles
,
Rules
,
Entities
,
Columnar Classification Rules
, and
File Classifiers
and
Custom Profiles
,
Rules
,
Entities
,
Columnar Classification Rules
, and
File Classifiers
are not subject to this limitation.
In this Topic
Select a Predefined DLP Profile

---
## Select a DLP Entity
**URL:** https://docs.netskope.com/en/select-dlp-entity/
**Last Modified:** 2026-06-25T19:14:27+00:00
**Scraped:** 2026-08-23T06:45:34.507223+00:00

Select a DLP Entity - Netskope Technical Documentation
Select a DLP Entity
DLP entities can be data identifiers or dictionaries. DLP provides a library of predefined data identifiers. You can also create custom entities and use them in a rule.
To learn more:
DLP Entity
.
Select Predefined Data Identifiers
Select Custom Entities
In this Topic
Select a DLP Entity

---
## Using DLP with Netskope Public Cloud Security
**URL:** https://docs.netskope.com/en/using-dlp-with-netskope-public-cloud-security/
**Last Modified:** 2026-06-25T17:37:00+00:00
**Scraped:** 2026-08-23T06:47:30.832933+00:00

Using DLP with Netskope Public Cloud Security - Netskope Technical Documentation
Using DLP with Netskope Public Cloud Security
You can use Netskope’s DLP solution to check for compliance and protect sensitive data. The DLP profiles that enforce compliance and protect sensitive data consists of DLP rules that specify data identifiers. These data identifiers find content that should not be present in your IaaS environment. The following predefine rules and data identifiers can be used to create DLP profiles to monitor the data in your IaaS environment.
Predefine Rule
Predefine Identifier
Description
Security – API Secret Keys
(P0) – computing/security/secret_keys/aws
(P1) – computing/security/secret_keys/generic_32h
(P2) – computing/security/secret_keys/generic_40a
Checks for AWS, GitHub, and Facebook API keys.
Security – Passwords
(P0) – computing/security/password_terms/eng
(P1) – computing/security/passwords/common
(P2) – computing/security/passwords/secure
Checks for common and secure passwords, and password related terms such as passwd, p/w, password.
Security – Private Key Blocks
(P0) – computing/security/private_keys/generic_begin
(P1) – computing/security/private_keys/generic_end
Checks for private keys.
You can setup DLP policies for AWS and GCP to perform retro scans and ongoing scans on your storage buckets. For detailed information refer to the following topics,
Creating API Data Protection Policies to scan S3 Buckets
Creating API Data Protection Policies to scan Google Cloud Storage
You can view the DLP incidents in your tenant under
API-enabled Protection > IaaS > Overview > DLP Incidents
. To learn more:
View IaaS Overview
.
For information on DLP Profiles and Rules, see the
Data Loss Prevention
documentation.
In this Topic
Using DLP with Netskope Public Cloud Security

---
## Viewing DLP and Malware Alerts for Public Cloud Storage
**URL:** https://docs.netskope.com/en/viewing-dlp-and-malware-alerts-for-public-cloud-storage/
**Last Modified:** 2025-08-31T01:46:19+00:00
**Scraped:** 2026-08-23T06:47:59.013827+00:00

Viewing DLP and Malware Alerts for Public Cloud Storage - Netskope Technical Documentation
Viewing DLP and Malware Alerts for Public Cloud Storage
Netskope performs DLP scans and malware scans on your storage against DLP and Threat Protection policies. When a violation is found, Netskope generates an alert.
You can view the DLP alerts from:
Skope IT > Events & Alerts > Alerts
Click
+Add Filter
and select
Alert Type
as
DLP
.
Incident > DLP
You can view the Malware alerts from:
Skope IT > Events & Alerts > Alerts
Click
+Add Filter
and select
Alert Type
as
Malware
.
Incidents > Malware
In this Topic
Viewing DLP and Malware Alerts for Public Cloud Storage

---
## DLP Behavior with SMTP Proxy
**URL:** https://docs.netskope.com/en/dlp-behavior-with-smtp-proxy/
**Last Modified:** 2025-08-31T01:55:52+00:00
**Scraped:** 2026-08-23T06:50:45.590813+00:00

DLP Behavior with SMTP Proxy - Netskope Technical Documentation
DLP Behavior with SMTP Proxy
Netskope predefined PII and GDPR DLP profiles contain rules that match the email names and addresses of objects that are inspected. For the SMTP DLP use case, these rules are applied against both the content and metadata of emails where the metadata includes the SMTP header. As the SMTP header can contain multiple instances of sender or recipient email names, DLP scans can result in matches that may be unexpected. The specific predefined DLP profiles are:
EU General Data Protection Regulation (GDPR)
EU General Data Protection Regulation (GDPR) (narrow)
DLP-PII
If you are enabling these three DLP profiles, then the simplest solution is to clone the profiles and remove the email rules.
For “EU General Data Protection Regulation (GDPR)” profile, remove “EU-Name-email” and “EU-Name-email (narrow)” rules.
For “EU General Data Protection Regulation (GDPR) (narrow)” profile, remove “EU-Name-email (narrow)” rule.
For “DLP-PII” profile, remove “Name-Email” rule.
Note
Disabling the metadata inspection may still result in a profile match as email name and addresses can be present in an email thread.
Earlier, emails inspected by DLP included the SMTP header fields – to, from, cc, attachment, and subject in the metadata and content. This behavior is now modified to eliminate the duplication of fields in metadata and content. Now, the SMTP header fields – to, from, cc, and attachment will be inspected in the metadata. The subject along with the email body will be inspected in the content.
When admins create a custom DLP rule to match on the text in the
Subject
of an email and choose both the
Metadata
and
Content
options, the system returns three DLP Violations when using a Microsoft Exchange email client.
This happens because the text in the Subject appears in the following order. For example, the subject of the email is “
dlp smtp is really good
”.
1. In Metadata, we get a string
subject: dlp smtp is really good
2. In Metadata, we get another string
thread-topic: dlp smtp is really good
3. In the Content, we get the string
dlp smtp is really good
In this Topic
DLP Behavior with SMTP Proxy

---
## View DLP Incidents related to SMTP Proxy
**URL:** https://docs.netskope.com/en/view-dlp-incidents-related-to-smtp-proxy/
**Last Modified:** 2025-08-31T01:55:51+00:00
**Scraped:** 2026-08-23T06:53:20.708889+00:00

View DLP Incidents related to SMTP Proxy - Netskope Technical Documentation
View DLP Incidents related to SMTP Proxy
Prerequisites
You must have already setup a
Forensics Profile.
After, create a policy for an Email Outbound App:
In the Netskope Admin Console, click
Policies > Real-time Protection.
Click
New Policy >
Email Outbound
and select your SMTP configuration and
Send
for Activities.
Select your desired
DLP Profile
and set
Action
to
Alert
Create a
Policy Name
,
Enable
, and
Save.
You can view all the DLP incidents related to SMTP Proxy from the DLP violations in emails in your Netskope tenant.
In the Netskope UI, navigate to
Incidents > DLP
and click on the incident to view the incident details.
Note
In the Incident Detail page, the “Acting User” and “From User” fields have the same value.
Upon clicking an incident, you will see the
Activity
,
Violation
,
Action Taken
, and other relevant information such as the
Sensitivity Label Instance,
and
Sensitivity Label
.
In this Topic
View DLP Incidents related to SMTP Proxy

---
## Downloading DLP Incident Files
**URL:** https://docs.netskope.com/en/downloading-dlp-incident-files/
**Last Modified:** 2025-08-31T01:38:58+00:00
**Scraped:** 2026-08-23T06:55:12.706407+00:00

Downloading DLP Incident Files - Netskope Technical Documentation
Downloading DLP Incident Files
Each DLP incident object has a download option so you can download the incident file. This file contains the content that violated the DLP policy and caused the incident. When you download the file, it’s downloaded into the forensic folder you defined in your Forensic profile.
To download a DLP incident file:
Go to
Settings
>
Forensics
.
Click
Edit
. The
Edit Forensics
window appears.
In the
Edit Forensics
window:
Forensics Status
: Enable.
Configuration
: Choose the
Forensic profile
.
Click the
Edit Settings
for the forensic profile.
Select
Enable original file access
.
Click
Save
.
Go to
Incidents
>
DLP
.
Click the
Object
. The
Object Details
page appears.
On the
Object Details
page, click
.
In this Topic
Downloading DLP Incident Files

---
## Create a DLP Exact Match Hash from a Virtual Appliance
**URL:** https://docs.netskope.com/en/create-a-dlp-exact-match-hash-from-a-virtual-appliance/
**Last Modified:** 2026-08-18T17:18:37+00:00
**Scraped:** 2026-08-23T06:58:21.298488+00:00

Create a DLP Exact Match Hash from a Virtual Appliance - Netskope Technical Documentation
Create a DLP Exact Match Hash from a Virtual Appliance
This process requires you to create a CSV file containing the exact match data and upload it to the Netskope cloud using a virtual appliance. When you upload the CSV file using the
request dlp-pdd upload
command, the Virtual Appliance encrypts the file before uploading it to the Netskope cloud.
To create a hash of your structured content:
Prepare the file in CSV format structured in rows and columns. We recommend that the CSV file has no more than 50 million records and includes a header row that names the columns. These names will show up in the DLP rule under File Column for Exact Match validation. Ensure the data in the columns are normalized. There are two ways to normalize the data, depending on the data type.
Normalize columns that contain numbers: Ensure data, like credit cards, are consecutive numbers that don’t contain special characters such as dashes, commas, quotes, and spaces.
Normalize columns that contain strings: Ensure data, like first and last names, are in Sentence case, with the first letter in uppercase and the remainder in lower case.
Using
nstransfer
account, transfer the CSV file to the
pdd_data
directory on the Virtual Appliance:
scp
<CSV file>
nstransfer@
<virtual_appliance_host>
:/home/nstransfer/pdd_data
The location of the
pdd_data
directory varies between the
nstransfer
and
nsadmin
user accounts. When using the
nstransfer
account to copy the file to the appliance, the location of the
pdd_data
directory is
/home/nstransfer/pdd_data
. When you log in to the appliance using the
nsadmin
account, the
pdd_data
directory is located at
/var/ns/docker/mounts/lclw/mountpoint/nslogs/user/pdd_data
.
After the data is successfully transferred, log in to the appliance using the
nsadmin
account.
Run the following command at the Netskope shell prompt to hash the data and upload the data to the Netskope cloud:
request dlp-pdd upload column_name_present true csv_delim ~ norm_str 2,3 file /var/ns/docker/mounts/lclw/mountpoint/nslogs/user/pdd_data/upload/sensitivedata.csv
Tip
column_name_present true
specifies that there is a header row in the file.
csv_delim ~
specifies that the CSV file is tilda-delimited.
dict_cins 1,2,4
creates a case insensitive dictionary from columns 1, 2, and 4.
dict_cs 3,5
creates a case sensitive dictionary from columns 3 and 5.
norm_str 2,3
specifies that columns 2 and 3 are to be treated as strings.
file
<CSV_file>
specifies the file that needs to be hashed and uploaded.
The command returns:
PDD uploader pid 9501 started. Monitor the status with >request dlp-pdd status.
Check the status of the upload:
request dlp-pdd status
The command returns:
Uploading data ...... 100% completed out of [####] of bytes
When the upload is complete, the command
request dlp-pdd status
returns:
Successfully uploaded the data from /var/ns/docker/mounts/lclw/mountpoint/nslogs/user/pdd_data/upload/sensitivedata.csv to Netskope cloud
When the data is successfully uploaded, the
sensitivedata.csv
file and its corresponding column names will appear in the Exact Match tab of the DLP rules.
In this Topic
Create a DLP Exact Match Hash from a Virtual Appliance

---
## Mimecast and Netskope DLP Configuration
**URL:** https://docs.netskope.com/en/mimecast-and-netskope-dlp-configuration/
**Last Modified:** 2025-08-31T01:55:32+00:00
**Scraped:** 2026-08-23T06:59:50.565779+00:00

Mimecast and Netskope DLP Configuration - Netskope Technical Documentation
Mimecast and Netskope DLP Configuration
This document explains how to configure Netskope DLP with Mimecast.
Netskope and Mimecast collaborate to provide a comprehensive data loss prevention (DLP) solution that effectively detects and safeguards sensitive information across the evolving cloud environment of joint customers. This approach is agnostic to sharing methods, user locations, applications, or device types. Netskope leverages its extensive knowledge of data sharing and extends it to email by employing a unified approach to DLP match rules. This allows customers to utilize their Mimecast environment to manage flagged email in accordance with established email policies.
Moreover, Mimecast and Netskope offer enhanced defense-in-depth capabilities to identify and prevent sophisticated, tailored, and targeted malware attacks from successfully infiltrating the joint customer architecture. This is achieved through active sharing of indicators of compromise that have already been discovered by either platform. As a result, customers’ overall security posture is strengthened, and the effectiveness of complex and costly malicious software is diminished. The likelihood of successful attacks is rapidly reduced.
Configuring Outbound Email Check
Starting with the enabling and configuring checks on the Netskope Tenant. We will be configuring it for Google Gmail.
First make sure you have SMTP > Google Gmail enabled. In the Netskope UI, go to
Settings > Security Cloud Platform > Mail Relay > SMTP
.
Configure the Email Server Setting. Copy the email server setting and paste the same in the Google Admin Workspace.
After copying add the same thing in the Google Admin Center. Go to
Apps > Google Workspace > Gmail > Hosts
, and under Hosts, click
Add Route
.
Test the TLS connection to verify that the connection to the host was successful. Click
Save
.
Configure Content Compliance to Send Traffic from Gmail to Netskope
Go to
Apps > Google Workspace > Gmail > Compliance > Content Compliance
.
Create the Outbound Rule from Gmail to Netskope. Click
Add
to add a new expression and select
Advanced Content Match
. Under Location, select Full header, and under Match type, select the Not contains text. Enter the following content:
x-netskope-inspected
. Click
Save
.
Select
Change the route
and select the Netskope host you created previously.
Select
Require secure transport (TLS)
, and from the hidden options, select all the Account types to affect. Click
Save
. You have done all the required configuration from the Google Workspace for the Outbound emails.
Now go back to the SMTP page on your Tenant. Get Verified your domain and add the next hop which will be in our case Mimecast Outbound SMTP host.
Go through this link to identify your smtp outbound Mimecast host:
https://community.mimecast.com/s/article/email-security-cloud-gateway-smtp-connector-exchange
.
Add a DLP Rule and Policy in Netskope
Go to the
Policies > Real-Time Protection
.
Click
Create New Policy > Select Email Outbound
.
Select Source as Users or Group.
For Email Outbound App, select
Gmail
.
Select the DLP profile for which you want to check the policy for any violation.
Add an SMTP header. For any violation, this header will be added and will be blocked after getting the same match in Mimecast.
Enter a Policy Name and click
Save
.
Now all the required configuration has been done on the Netskope. Further configuration will be done in the Mimecast.
Create a Policy in Mimecast
Go to
Gateway > Policies > Definitions > Content Definitions
.
Create a New Definition and add the below Rule in the Scanning options. You added the same header from the Netskope Tenant if any email Violates the Policy.
Now create the new policy. Go to
Gateway > Policies > Content Examination
.
Click
Create New Policy
.
Select the content definition you just created, and click
Save
.
Now that you have configured all the required settings from the Netskope, test out all the configurations. Go to your domain for which you have created the DLP policy. In this case we will add the password protected file for which we have added the DLP profile while creating the policy to basically test out the Violations. Click on send after attaching the protected file.
Try to check the same in the your tenant. Go to
Incidents > DLP
.
Now check the same on the Mimecast Dashboard for any violation. Go to
Message Center > Bounced Messages
to see the Policy Violations.
And regarding the violation, you will be receiving the email.
Configuring Inbound Email Check
Inbound email checks will help you make sure that all the malicious emails received should be checked by Mimecast and will take the required action as per the configured policies. Additionally, Cloud Exchange will be used to share the Threat IOCs between Mimecast and Netskope bilaterally.
To Deliver all the Inbound emails to Mimecast. First we need to whitelist all the Mimecast Datacenter IPs. You can refer:
Mimecast Data Centers and URLs
for more information on the IP address which need to be whitelisted.
After identifying the IPs we need to whitelist in the particular email exchanges. In this case we are using Google Workspace.
Go to
Google Admin Console > Apps > Google Workspace > Gmail > Spam
, and then
Phishing and Malware > Email Allowlist
. Whitelist all the required IPs as selected from above.
On the same page whitelist those same IPs in the Inbound Gateway. Ensure the Require TLS for Connections From the Email Gateways Listed Above option is selected.
Now do the required changes in your MX records and update it with the Mimecast SMTP inbound host. Refer this link to select the correct host:
Mimecast Gateway
.
In this case we’re using Godaddy for maintaining my MX records and will do the required change over there and in a similar way update the records.
Now you need to create the delivery route definition in Mimecast so that after receiving the Inbound email by Mimecast, it can be delivered back to Gmail if not malicious. Go to
Administration Console > Gateway > Policies > Definitions > Delivery Routes
.
Click New Route Definition and provide the required hostname. Refer to this link:
https://support.google.com/a/answer/174125?hl=en
for selecting the correct hostname.
Click
Save
and
Exit
.
Now you need to configure the Policy for the same Route Definition. Go to
Policies
and click
Delivery Routing
.
Click
New Policy
and select the Delivery Route you created. Applies to: Email Domain. Specifically: <Provide your Domain>. After providing the Required details click
Save
and
Exit
.
Your Inbound Email Configuration has been completed successfully in the similar way you can set different policies for all the Inbound Emails.
In this Topic
Mimecast and Netskope DLP Configuration

---
## DLP
**URL:** https://docs.netskope.com/en/dlp-117816/
**Last Modified:** 2025-08-31T01:41:45+00:00
**Scraped:** 2026-08-23T07:01:02.782735+00:00

DLP - Netskope Technical Documentation
DLP
This section of the API Data Protection Policy page specifies the type of DLP profile that triggers a policy violation.
Note
API Data Protection now supports scanning files up to 128 MB for DLP and threat protection. The default file size is 32 MB. Contact Netskope support or your sales representative to configure a larger file size for your tenant. A few points to consider before enabling this enhancement:
With larger files, there may be an increased end to end latency for policy processing.
Plan for a increase in forensic/quarantine/legal hold data store size.
The encrypt policy action does not currently support larger than 32MB files. The action will therefore not work on files larger than 32MB.
API Data Protection for Slack Teams can scan for DLP when a user uploads a file on Slack thread or reply.
However, it is important to note that API Data Protection cannot scan messages posted in thread or reply. This is a limitation in Slack Teams due to lack of underlying Slack API support.
If you have a requirement to scan messages in thread or replies, consider moving to Slack Enterprise. Slack enterprise has coverage for messages and files across direct messages, 1:n messages, channels, threads, and replies.
To use a data loss prevention (DLP) profile, select
DLP
and click
Select Profile
. Search for a DLP profile or choose one from the list, which includes both predefined and custom profiles. After selecting a DLP profile, click
Save
.
When finished, click
Next
.
In this Topic
DLP

---
## Enforce DLP for NPA Browser Access Private Apps
**URL:** https://docs.netskope.com/en/enforce-dlp-for-npa-browser-access-private-apps/
**Last Modified:** 2026-05-28T22:38:29+00:00
**Scraped:** 2026-08-23T07:07:17.191442+00:00

Enforce DLP for NPA Browser Access Private Apps - Netskope Technical Documentation
Enforce DLP for NPA Browser Access Private Apps
Prerequisites
To successfully configure DLP for Browser Access Private App(s) in a policy, the following prerequisites must be met:
Ensure you have a
Publisher already configured
.
Confirm that a
SAML reverse proxy IdP is set up for Private Apps
.
Verify that there is a
Browser Access app requiring DLP enforcement configured
. Note that only HTTP and HTTPS protocols are supported for DLP.
DLP for NPA Browser Access must be activated through a feature flag.
Contact your Sales Representative or Support to enable this feature.
Use Cases
The primary objective is to implement Data Loss Prevention (DLP) controls for private applications accessed via NPA Browser Access.
Configuring DLP ensures the safeguarding of private applications that often contain highly-sensitive information accessed by employees, partners, or both. The goal is to protect confidential data by effectively enabling DLP controls through well-defined policies. This capability is supported for both Any Browser apps and Enterprise Browser Apps.
Here are some examples of DLP controls:
Block the downloading and uploading of confidential information (GDPR & PCI) while allowing the download of non-confidential documents, including the use of machine learning for screenshot detection.
Prevent the posting of confidential information to a web server.
Create a DLP Policy for NPA Browser Access Private Apps
Policy creation is explained in
Create a Real-time Protection Policy for Browser Access to Private Apps
.
Go to
Policies > Real-time Protection > New Policy
and select
DLP
.
For Destination, choose the
Private App Segments
that require DLP to be applied.
For Profile & Action, select
Add Profile
followed by the DLP Profile(s).
Select the Activities to be included in the criteria, such as Download, Upload, and FormPost.
Apply the DLP Profile(s) based on your specific requirements. There is an optional configuration available to select the corresponding action for each profile. When finished, save the policy and apply changes.
An example policy:
Additional Notes
DLP for NPA utilizes the
Universal Connector
for activity detection. The supported activities for Browser Access Private Apps with DLP include Upload, Download, and FormPost. The Universal Connector provides best-effort activity detection.
There is a known issue with Browser Access Private Apps created prior to R123 which may cause a DLP policy to not match. To resolve this issue, either recreate the app, or modify and save it to initiate a re-sync.
The events for DLP will be logged under Network Events, Alerts, and Incidents, depending on the action taken.
Private App Tags are not supported in the DLP Policy for NPA Browser Access Private Apps.
Only HTTP and HTTPS protocols are supported for DLP Policy with NPA Browser Access Private Apps.
Note that AnyApp Browser Access Apps (RDP/SSH) are not supported. If such a configuration is attempted, a warning message will appear.
LFS (Large Files Support) is not available for the DLP Policy with NPA Browser Access Private Apps. The default limit for supported scanning file sizes is set at under 16 MB.
Transaction events will not be generated for Browser Access DLP traffic, even if transaction events are enabled for web traffic.
NPA Browser Access Private Apps leveraging websockets will be bypassed from DLP inspection.
DLP for NPA Browser Access is not supported for tenants hosted in China and the Kingdom of Saudi Arabia MPs.
The fallback actions configurable under
Advanced File Scanning for DLP
can be extended to NPA Browser Access Private Apps as well.
When setting up multiple Browser Access Private Apps that share the same hostname but different ports, it is required to include all apps under one DLP policy. Please review the example below for a workaround.
Example
Private App 1:
My-http-app1
Hostname:
myapp.acmegizmo.com
Port: 80
Private App 2:
My-https-app2
Hostname:
myapp.acmegizmo.com
Port: 443
DLP Policy
: A policy name
My-app-DLP-Policy
is specifically configured to apply only to
My-http-app1
, i.e., for port 80.
Limitation
: In this scenario, both private apps share the same hostname,
myapp.acmegizmo.com
, but operate on different ports: 80 for
My-http-app1
, and 443 for
My-https-app2
. The DLP policy is currently set only for port 80, which presents a potential limitation. With such a configuration, there is a possibility that the intended application (
My-http-app1
on port 80) may not be correctly identified for DLP, potentially resulting in the policy failing to match the intended traffic.
Workaround
: To mitigate this issue, it is recommended to configure the DLP Policy
My-app-DLP-Policy
with both applications:
My-http-app1
(port 80) and
My-https-app2
(port 443).
In this Topic
Enforce DLP for NPA Browser Access Private Apps

---
## Netskope One for Microsoft Purview DLP
**URL:** https://docs.netskope.com/en/netskope-one-for-microsoft-purview-dlp/
**Last Modified:** 2026-07-02T02:19:51+00:00
**Scraped:** 2026-08-23T07:09:34.136040+00:00

Netskope One for Microsoft Purview DLP - Netskope Technical Documentation
Netskope One for Microsoft Purview DLP
To use this feature, please get in touch with the Netskope account team to get this feature enabled on your tenant. If you are a new customer, please reach out to the Netskope sales team.
If you would like a demo, please reach out to
purview@netskope.com
.
Netskope One for Microsoft Purview DLP allows customers to leverage their existing Purview to gain visibility and control over sensitive data in motion, including activities like AI interactions, data shared on unsanctioned platforms, or social media form posts.
All traffic passing through Netskope will be directed to Purview. Customers can utilize either existing or new Purview collection policies to enhance visibility, extending from applications and endpoint traffic to include network traffic as well.
Use Cases include:
Gen AI Discovery
: Engage with Generative AI through various platforms, including browsers, applications, and add-ins like Chat GPT, Gemini, and Claude. This integration will capture comprehensive evidence of these interactions within Purview, enhancing compliance features such as eDiscovery, data retention, deletion, and communication compliance.
Protection
: Identify sensitive content in files uploaded to unauthorized cloud storage applications like Box, Dropbox, and Google, or shared via public email providers such as Gmail and Outlook and monitor sensitive information submitted through form services, including Google Forms.
Centralized Visibility
: Access all Purview classification activities from a single dashboard, empowering you to make informed decisions.
Insider Risk Management
: For instance, if a user engages in multiple risky activities and begins sharing sensitive information with ChatGPT, their risk level may escalate which could necessitate actions such as restricting access to sensitive information in Teams or SharePoint.
Conditional Access
: With Entra conditional access, customers can manage access to the tenant and SSO-configured applications, regardless of the user’s login location. For example, customers can permit sign-ins from a home PC as long as the user is deemed low risk. Additionally, adaptive protection offers benefits like triggering the retention of OneDrive content based on risk levels.
Prerequisites
Entra ID / Azure AD (AAD) –
The current integration for Purview is only supported through Entra ID / Azure AD. In Entra ID, the user email field should be populated as that is the unique identifier for Netskope.
User provisioning with Entra ID
: This feature integrates Microsoft 365 and Netskope, therefore the users must be synchronized between Entra ID and Netskope. To do this, you must enable
Entra ID user provisioning within Netskope
.
Client installation:
The Netskope client must be installed on a machine & registered to an account that is synced from Entra ID. For more information, see
Netskope Client
.
If testing on a test tenant separately, follow the steps mentioned on
Netskope Client
to install the client.
If testing on a production tenant, follow the Purview Instance setup steps below.
Netskope One for Microsoft Purview DLP Supported Activities
Netskope One for Microsoft Purview DLP Configuration
Netskope One for Microsoft Purview DLP Troubleshooting and FAQ
In this Topic
Netskope One for Microsoft Purview DLP

---
## Netskope One for Microsoft Purview DLP Troubleshooting and FAQ
**URL:** https://docs.netskope.com/en/netskope-one-for-microsoft-purview-dlp-troubleshooting-and-faq/
**Last Modified:** 2026-06-25T19:18:23+00:00
**Scraped:** 2026-08-23T07:09:35.305393+00:00

Netskope One for Microsoft Purview DLP Troubleshooting and FAQ - Netskope Technical Documentation
Netskope One for Microsoft Purview DLP Troubleshooting and FAQ
Purview Integration is missing under Settings
Check if the following tab exists in Netskope admin console in
Settings > Manage > Microsoft Purview Integration.
If you still don’t see it, please get in touch with your Netskope account team.
Verifying a connection between Purview and Netskope
Once correctly configured, a green circle with a checkmark will show up in
Settings > Manage > Microsoft Purview Integration.
Unable to see synced users in Netskope
Follow the guide on
User Provisioning with Entra ID
.
Synced users will show up in the Netskope admin console in
Settings > Security Cloud Platform > Users
. The sync can take 1 hour to happen.
Send the synced users an invitation to install Netskope Client. Once users install the Netskope Client, the email displayed in the Netskope Client will match up with Entra ID.
No traffic flowing into Purview
Token Expiry consideration: When the Netskope proxy sends content to Purview for the first time, the proxy does not have a valid token causing the request will fail. The proxy will request a token from UA during this first transaction meaning subsequent requests to Purview will go through.
Check if Purview Forwarding is enabled. Go to
Policies > Real-time Protection > Purview Integration
, toggle the button to
Allow sending all traffic to Purview
.
Release-125.0.0.x: Check if Purview Forwarding is enabled. Go to
Policies > Real-time Protection > Purview Integration
, toggle the button to
Allow sending all traffic to Purview
.
Release-127.0.0.x: Check if a RTP policy is defined with Action as “Forward to Purview-DLP”. Go to
Policies > Real-time Protection.
Missing traffic types in Purview
See the terminology reference for
Netskope Cloud App and App Connectors
.
Support of online resources is limited to Netskope-supported cloud applications.
Most of the apps with app-specific connectors is supported.
Support for applications with universal connectors depends on the activities identified by the connectors.
Are all web activities supported with this integration?
Netskope identifies activities performed by the user through detailed application analysis. Activities such as upload, download, and POST are supported in this integration by default. Other Netskope activities support can be extended for this integration, but require backend configuration change on Netskope side. The three default activities should cover most scenarios.
Is it possible to forward traffic for cert pinned applications?
Certificate pinned applications
are bypassed by Netskope by default and thus not supported for this integration.
In this Topic
Netskope One for Microsoft Purview DLP Troubleshooting and FAQ

---
## Netskope One for Microsoft Purview DLP Configuration
**URL:** https://docs.netskope.com/en/netskope-one-for-microsoft-purview-dlp-configuration/
**Last Modified:** 2026-07-02T02:41:16+00:00
**Scraped:** 2026-08-23T07:09:36.514263+00:00

Netskope One for Microsoft Purview DLP Configuration - Netskope Technical Documentation
Netskope One for Microsoft Purview DLP Configuration
This configuration will have to be performed on both the Microsoft and Netskope-side.
Netskope Setup
To use this feature, please get in touch with the Netskope account team to get this feature enabled on your tenant. If you are a new customer, please reach out to the Netskope sales team.
1. In the Netskope portal, browse to
Settings > Manage > Microsoft Purview Integration
then click
Setup Purview Instance
.
2. Enter an
instance name
(no spaces), and optionally an
admin email
for instance notification then click
Grant Access
.
3. In the popup window that appears, sign in with your Microsoft Entra global administrator account (or any account that has the permissions to add and authorize an enterprise application).
4. Once you log in, click
Accept
to the permissions requested, which authorizes Netskope to interact with Purview.
5. Once authorized, you should now see the instance has been created.
Permission Re-grants
As part of Netskope App registration in Azure for a given tenant,
API permissions must be re-granted
for Microsoft Graph as shown below in highlighted red box:
After a successful re-grant, the app registration will succeed and will be able to fetch the token for performing below API calls:
Protection Scope
Process Content
Purview Setup
Go to
https://purview.microsoft.com/
>
Solutions
>
Data Loss Prevention
Create a new policy and choose the
Inline web traffic
option.
Create a custom policy.
Name the policy.
Add your cloud apps.
Choose your data sources.
Choose your enforcement policy. Leave
Network
enabled.
Create as many
DLP rules
as desired.
Enable the policy.
Microsoft Security Copilot AI Agents
You can also use the Netskope One Data Protection Integration Agent with this setup.
Go to
Microsoft Security Copilot
and click
Browse more agents
Search for Netskope and select
Netskope One Data Protection Integration Agent
. Click on it and click
Get Agent
.
Add your billing, resource group and give it a name. There is no license cost for the agent. CLick next and then press place order.
Click on
Use in Security Copilot
Click
Set up
When you get to
user_query
, put
Generate a report for recent DLP incidents
. This will be a drop down when you use the agent. You can also go back later and change it.
Set up
Home
and
Sources
.
Under
Non-Microsoft
, select
Show more
Enter your Netskope tenant url and your Netskope v2 API token
. See
/en/roles-rbac-v3
API Permissions
Creating the service principal in Azure is a requirement. Follow the steps below:
Install
Azure PowerShell module
if not already installed.
Connect to Azure:
Connect-AzAccount -Tenant [tenantname].onmicrosoft.com
Add the service principle by pasting the following statement into PowerShell:
if (-Not (Get-AzADServicePrincipal -ApplicationId "9ec59623-ce40-4dc8-a635-ed0275b5d58a")) {
        "Service principal not yet created"
        try{
            New-AzADServicePrincipal -ApplicationId "9ec59623-ce40-4dc8-a635-ed0275b5d58a"
        } catch {
            Write-Host "An error occurred when creating the service principal"
            Write-Host $_
        }
    } else {
        "Service principal already exists"
    }
Enable sending the traffic to Purview
1. In the Netskope console, browse to
Policies > Real-time Protection
and select
New Policy > Cloud App Access.
2. Create a new policy, select the scope (e.g., user, applications, activity), and select the action as
Forward to Purview-DLP
. Then, choose the correct Purview instance that you have synced with Netskope. The Forward to Purview action is applicable for both visibility and enforcement to allow/block the traffic. You need to have the appropriate policy (e.g. Block/ action policy) on the Purview platform to have Netskope perform the enforcement
.
User Importing and Netskope Client Installation
Make sure the Purview integration is enabled on the UI, and then perform a Entra ID user SCIM sync. If a SCIM sync is already in place before the feature enablement, make an update to the synced user or group. This change will trigger the user sync to happen on Netskope side and make sure all the configs are refreshed.
Additional Considerations
The default file size for Netskope is 16MB. To forward files exceeding the default size to Purview, you can enable Advanced File Scanning, also known as
Large File Support (LFS)
.
In this Topic
Netskope One for Microsoft Purview DLP Configuration

---
## Data Loss Prevention On Demand
**URL:** https://docs.netskope.com/en/data-loss-prevention-on-demand/
**Last Modified:** 2026-06-25T17:36:59+00:00
**Scraped:** 2026-08-23T07:09:41.375958+00:00

Data Loss Prevention On Demand - Netskope Technical Documentation
Data Loss Prevention On Demand
Data Loss Prevention On Demand Overview
Netskope DLP On Demand enables local and collocated document scanning via a REST API. Currently, it is delivered as an appliance supporting flexible deployment across public cloud environments — including AWS, GCP, Azure — as well as on the on-premises VMware vSphere platform and Hyper-V.
DLP On Demand supports both
Synchronous
and
Asynchronous
API calls.
The APIs support two types of content scans: unstructured and structured.
Unstructured
– This category includes common business documents, emails, photos, and webpages. Examples include Microsoft Office files and PDFs. Text from LLM prompts or messages from collaboration tools such as Slack or Microsoft Teams can also be submitted for DLP inspection.
Supported formats for these documents can be found here:
Supported File Types for Detection
Supported File Types for Content Inspection
Structured –
This category refers to columnar or tabular data, such as exports from SQL databases, that are submitted in a specified format for classification purposes.
For more information, see the following pages:
DLP On Demand Appliance
Sending Data to DLP On Demand
Post Deployment
In this Topic
Data Loss Prevention On Demand

---
## Appliance Setup
**URL:** https://docs.netskope.com/en/dlpondemandconfig/
**Last Modified:** 2026-06-25T19:19:27+00:00
**Scraped:** 2026-08-23T07:09:42.549964+00:00

Appliance Setup - Netskope Technical Documentation
Appliance Setup
Appliance Best Practices and Prerequisites
Appliance Sizing
The following table lists the recommended instance types for cloud deployments and the corresponding size configurations for on-premises environments of the DLP On Demand appliance:
AWS*
GCP
Azure
VM#
Concurrent Requests^
Minimum Disk Size
Small
c5ad.4xlarge
n2-standard-16
Standard-F16s_v2
16 cores/32GB
480 rps with burst of 576 rps. Max throughput limit: 786 MB per min
351GB
Medium
c5ad.8xlarge
n2-standard-32
Standard-F32s_v2
32 cores/64GB
1280 rps with burst of 1536 rps. Max throughput limit: 2048 MB per min
351GB
Large
c5ad.16xlarge
n2-standard-64
Standard-F64fs_v2
64 cores/128GB
2880 rps with burst of 3456 rps. Max throughput limit: 4608 MB per min
351GB
* In AWS regions where the
c5ad
sizing is unavailable, use the
c5a
instance size.
^ File and Content structure, DLP Profile complexity and features like OCR and EDM, are likely to impact the performance numbers.
# ESX does not support dynamic resizing of the VM after the appliance has been created. This was tested on: VMware ESXi, 8.0.2, 23305546 (VMware ESXi 8.0 Update 2b | 29 FEB 2024 | Build 23305546)
The
Small
size is intended only for proof-of-concept testing. For production deployments, Netskope recommends using
Medium
or
Large
configurations. To ensure optimal performance, use
SSDs
for all instances.
Networking Considerations
Allowlisting:
Ensure that
Netskope IPs
and Amazon S3 (for example,
*.s3-us-west-1.amazonaws.com
) should be allowlisted. If tenant.goskope.com is the tenant Web UI hostname, then also allow the IPs corresponding to config-tenant.goskope.com and callhome-tenant.goskope.com.
The following domains must also be allowlisted:
{"dlpappliancegw.sv5.goskope.com","dlpappliancegw.bom3.goskope.com","dlpappliancegw.am2.goskope.com","dlpappliancegw.sjc1.goskope.com","dlpappliancegw.fr4.goskope.com","dlpappliancegw.ruh1.goskope.com","dlpappliancegw.mel2.goskope.com","dlpappliancegw.sjc2.goskope.com","dlpappliancegw.zur2.goskope.com","dlpappliancegw.lon3.goskope.com","dlpappliancegw.sin2.goskope.com","dlpappliancegw.dfw3.goskope.com","dlpappliancegw.fra2.goskope.com"}
Microsoft AIP:
If you are using the
DRM feature with DLP
, the Microsoft AIP endpoints must also be allowlisted.
Administrative Access:
If SSH access is permitted (for cases where console access is not sufficient), ensure that systems used to administer the appliance can reach it over SSH.
API Connectivity:
The appliance must be reachable over HTTPS (TCP 443) by all integrating services that send API calls to it.
We do not recommend SSL interception of traffic from DLP On Demand appliance. If a proxy is in place, ensure that respective certificates are imported.
Netskope recommends blocking all other inbound and outbound communication for security.
Deploying multiple DLP On Demand behind a network load balancer is currently not feasible with common implementation scenarios that use asynchronous requests for scanning or result retrieval.
See the
Appliance Troubleshooting
page for any other issues.
To get a
DLPoD
Appliance running smoothly in an on-premises environment, you will need to configure an upstrean proxy for
WebSockets
. Standard web traffic (HTTP) is like a series of one-off letters: send a request, get a reply, and the connection closes.
WebSockets
, however, create a persistent, two-way “open phone line” between your appliance and the cloud service.
Appliance Creation
See the sections below for detailed appliance creation steps for different cloud provide and on-premises environments. During setup, the appliance automatically receives its IP address, netmask, and gateway through DHCP. Once the instance is created, connect to it and complete the tethering process to the Netskope Management Plane.
The UI from R134 will provide links to download KVM, Azure, HyperV, ESXi images. You can also assign AWS images from the UI by providing your account ID.
To download or assign an image, navigate to
Security Cloud Platform > On-Premises Infrastructure
and select
Setup DLP On Demand
and select your respective hypervisor.
AWS DLP On Demand Appliance Creation
Launch an EC2 instance using the
DLP On Demand AMI
. The image can be found in
Private Images
.
Set the
Instance Type
to
c5ad.8xlarge
or
c5ad.16xlarge
.
Define your desired
Storage
and use
gp3
.
No SSH key-pair is required at the moment, setup the networking and firewall security groups as appropriate and other configurations can remain at the default setting. We recommend that the appliance is not accessible publicly.
Select
proceed with no key-pair
and launch the instance.
GCP DLP On Demand Appliance Creation
Go to
Compute Engine – VM Instances
and then click
Create Instance
In
Machine Configuration
, provide a name for the instance and in
General Purpose
, select
N2.
In the
Machine Type
, select
n2-standard-32
or
n2-standard-64
In
OS and Storage
, select
Change
under
Operating System and Storage
and filter the Image. Select the appropriate DLP On Demand appliance image. For Size (GB), enter
300 GB
.
Setup the networking and firewall security groups as appropriate and other configurations can remain at the default setting, then click
Create
.
Azure DLP On Demand Appliance Creation
During appliance deployment, the Azure portal may display an “OS Provisioning Timed Out” notification. This notification is expected and can be
safely ignored.
The appliance boot sequence includes extended initialization tasks such as security hardening, service orchestration, and platform configuration
that run prior to the Azure Guest Agent reporting readiness. The appliance is designed to complete its full initialization independently of the
Azure provisioning signal.
You can confirm appliance readiness by verifying that the instance state is shown as “Running” in the Azure portal.
Download the VHD from the presigned URL
Untar the VHD using the below command
tar -xvf {downloaded_vhd_tar_file} -C {path to untar the artifacts}
Create a
Storage Account
under
Resource Group.
Create a
Container
under the
Storage Account
.
On the
Storage Account
page, open the side-menu
Security + Networking
and click on
Shared access signature
.
Enable all permissions, set the
Start Time
as 24h before the current time and
End Time
as 24h after current time (1 day offset for
Start Time
and
End Time
)
Click on
Generate SAS and connection string
and copy the
SAS token
value.
If you don’t have
azcopy
, install it.
Warning
To upload the file to Azure Blob Storage, use
AzCopy
. Uploading large files via the Azure Portal is unreliable and may result in file corruption
Run the command below to upload the
.vhd
artifact to the Azure Blob Storage:
azcopy copy "{local_path}.vhd" "https://{account_name}.blob.core.windows.net/{container_name}/{vhd_name}.vhd?{SAS_TOKEN}" --blob-type PageBlob
Once the VHD is uploaded,navigate to the Images in Azure:
Choose your subscription to create the image.
OS Type: Linux
Choose your VHD from the storage blob
Account Type:
Premium SSD
Encryption:
Platform managed
Click on
Review + create
to create the image.
Create the instance out of the image.
Choose the respective subscription and resource group. Provide the VM name. The Image will be auto populated and choose the other parameters.
Select a minimum of 351 GB disk
Premium SSD
.
Choose your Networking settings and create the VM.
As stated previously, the VM may show deployment failures, but this is expected behavior.
vSphere (ESXi) DLP On Demand Appliance Creation
Download the .ova image from the
Setup DLP on Demand
window from your tenant  to your local system before uploading it to vSphere. vSphere does not support direct URL imports when the URL exceeds its maximum supported length, which applies to the Netskope download link.
There are strict sizing requirements for an ESXi deployment or the instance will not start. Use one of the following sizes:
16 CPU with 32 GB Memory
32 CPU with 64 GB Memory
64 CPU with 128 GB Memory
If you are using
vCenter Server
, the process is similar and generally done via the
vSphere Client
:
Start Deployment:
Right-click a
host
,
cluster
, or
datacenter
in the inventory and select
Deploy OVF Template
.
Select Template:
Select
Local file
and then
Upload files
to choose your local
.ova
file.
Click
Next
.
Select Name and Folder:
Enter a
Virtual machine name
and select the
deployment location
(a folder in the vCenter inventory).
Click
Next
.
Select Compute Resource:
Select the
host
,
cluster
, or
resource pool
where the VM will run.
Click
Next
.
Review Details:
Review the template details and accept any license agreements.
Click
Next
.
Select Storage:
Select the
datastore
and the
virtual disk format
(e.g., Thin Provision).
Click
Next
.
Select Networks:
Map the source networks in the OVA to the destination
network ports
in your vSphere environment.
Click
Next
.
Customize Template (if applicable):
If the OVA allows for customization, you’ll see a
Customize Template
screen where you can set initial configuration (e.g., network settings, passwords).
Click
Next
.
Ready to Complete:
Review the final summary. Check the box to
Power on after deployment
if desired.
Click
Finish
.
Hyper-V DLP On Demand Appliance Creation
Download the appliance image from the
Setup DLP on Demand
window from your tenant
Search for and open
Hyper-V Manager
from the Start menu.
Access the Import Wizard:
In the left pane, click the name of your Hyper-V host (your computer).
In the
Actions
pane (on the right), click
Import Virtual Machine
.
Locate the VM Folder:
Click
Next
on the “Before You Begin” screen.
In the
Locate Folder
step, click
Browse
and navigate to the
folder
that contains the exported VM files (the VM’s configuration file, usually in a subfolder called
Virtual Machines
).
You must select the top-level folder of the exported VM, not a subfolder.
Click
Select Folder
, then
Next
.
Select the Virtual Machine:
The wizard should now display the virtual machine found in that folder. Select the correct VM from the list and click
Next
.
Choose Import Type:
Select one of the following import options:
Register the virtual machine in-place (use the existing unique ID):
Use this if the VM files are already in the location where you want them to run and you are not importing a copy.
Review and Finish:
Review the summary of your choices and click
Finish
to start the import process.
Once complete, the VM will appear in the list of virtual machines in the Hyper-V Manager console.
Edit the Network Adapter Setting
before starting the instance.
Right-click
the VM name and select
Settings…
.
In the left pane, under the
Hardware
section, click on
Network Adapter
(or the specific name if you renamed it). Select the network switch which is used to connect in the respective environment.
Start the VM:
There are a few options to start it:
Action Pane:
Select the VM, and in the
Actions
pane (on the right), click
Start
.
Right-Click Menu:
Right-click the VM name and select
Start
.
KVM DLP On Demand Appliance Creation
Download the Appliance Image
Download the appliance image from the
Setup DLP on Demand
window from your tenant.
Create Template Directory and Extract Initial Tarball
Create a directory to hold the VM disk image and extract the initial tarball. The tar includes checksum files also so next step will untar the main artifacts
mkdir dlp-vm-template
tar -xvf dlp-appliance.tar
ls # List files to confirm the nested tar.gz file is present
Extract the QCOW2 Disk Image
The
.qcow2
file is the actual virtual disk image. Extract it into the template directory.
Note:
The file name in your command (
netskope-dlp-on-demand-kvm-qcow2-133.0.7.qcow2.tar.gz
) suggests a nested
.tar.gz
archive, so the extraction command is:
tar -xzvf netskope-dlp-on-demand-kvm-qcow2-133.0.7.qcow2.tar.gz -C /home/ubuntu/dlp-vm-template/
Deploy the Appliance using
virt-install
This command creates the VM definition (
dlp-appliance-test
) and imports the prepared disk image.
--import
: Tells
virt-install
to use the existing disk image instead of performing a fresh installation.
--disk
: Specifies the path to the
.qcow2
image and its size.
--network default
: Connects the VM to the default
libvirt
NAT network.
sudo virt-install --name dlp-appliance-test --ram 65536 --vcpus 32 --os-variant ubuntu24.04 --disk path=/home/ubuntu/dlp-vm-template/netskope-dlp-on-demand-kvm-qcow2-133.0.7.qcow2,size=452 --import --network default --check path_in_use=off
IMPORTANT:
When
virt-install
runs, it often connects the console. Give
CTRL+C
to exit the console view. The installation/first boot process will continue in the background. Wait a few moments for the appliance to fully boot.
Verify the VM Status
Check the status of the deployed VM. It should show as
running
.
sudo virsh list --all
Check the Default Network Status
Confirm the default network (typically a NAT bridge on
virbr0
) is active.
sudo virsh net-list
Find the Appliance’s IP Address
Since the appliance is on the default virtual network, use
virsh
to query the
DHCP leases
to find the IP address assigned to the new VM.
sudo virsh net-dhcp-leases default
Connect to the Appliance via SSH
Use the IP address retrieved in the previous step to connect to your running KVM appliance.
sudo ssh {username}@{IP}
Connecting to a DLP On Demand instance:
Once the instance has been created, it must be connected to Netskope to download the required configuration and profiles before it can begin processing DLP requests. To proceed:
SSH into the instance as
nsadmin
with password
nsappliance
. This password should be changed upon login.
ssh nsadmin@<instance_ip>
nsadmin@<instance_ip>'s password: nsappliance
Change the password by running
auth change-password
nsappliance> auth change-password
Automatic Configuration by DHCP is the default. In configurations where DNS is not provided via DHCP, follow these commands:
nsappliance> configure
nsappliance(config)> set dns primary x.x.x.x
nsappliance(config)> set dns secondary x.x.x.x
nsappliance(config)> save
nsappliance(config)> exit
If you intend to configure your network interface manually, follow these commands:
nsappliance> configure
nsappliance(config)> set interface v4 dhcp enable false
nsappliance(config)> set interface v4 static enable true
nsappliance(config)> set interface v4 static ip x.x.x.x
nsappliance(config)> set interface v4 static gw x.x.x.x
nsappliance(config)> set interface v4 static netmask x.x.x.x
nsappliance(config)> set dns primary x.x.x.x
nsappliance(config)> set dns secondary x.x.x.x
nsappliance(config)> save
nsappliance(config)> exit
To revert back to automatic DHCP configuration (in configurations where DNS is not provided via DHCP, you can also set the DNS), use the following commands:
nsappliance> configure
nsappliance(config)> set interface v4 dhcp enable true
nsappliance(config)> set dns primary x.x.x.x
nsappliance(config)> set dns secondary x.x.x.x
nsappliance(config)> save
nsappliance(config)> exit
Please make sure that DNS resolution works on the appliance. Guidance to add a DNS server is provided in this step.
If you have not created a REST API v1 token, you will need to. If you have already created one, skip to step 4. Otherwise, navigate to
Settings > Tools > Rest API v1
and click
GENERATE NEW TOKEN
.
Navigate to
Settings > Security Cloud Platform > On-Premises Infrastructure
in the Netskope admin console and copy the
License Key
.
Use the
License Key
with the following command in configuration mode:
nsappliance> configure
nsappliance(config)# set system licensekey <license-key>
nsappliance(config)# save
nsappliance(config)# exit
You can check the tethering status with
status tethering
.
callhome_reachable
needs to be
true
and
tenant-url
and
serial
should be populated.
nsappliance> status tethering
After tethering, the appliance will need approx. 30 mins to initialize before becoming ready.
You will also see this information reflected on the
On-Premises Infrastructure
page:
Clicking on these appliances will reveal more information about the appliance such as the
Hypervisor
,
OS
, etc.
Configuring a custom proxy
You can configure a custom
implicit
or
explicit
proxy to sit between the appliance and management plane.
To do so, enter the configure mode and set the management-plane upstream-proxy-server parameters:
root@nsappliance:/home/nsadmin# nsshell
nsappliance> configure
Entering configuration mode
nsappliance(config)# set management-plane upstream-proxy-server
hostname   Fully qualified domain name (or IP) for proxy server
password   Password to the proxy server.
port   port for proxy server
trusted-ca   Import CA for upstream proxy server into trusted CA store.
username   Username to the proxy server.
Explicit
Example:
nsappliance(config)# set management-plane upstream-proxy-server hostname 10.10.10.10
nsappliance(config)# set management-plane upstream-proxy-server port 8000
nsappliance(config)# set management-plane upstream-proxy-server username <USERNAME>
nsappliance(config)# set management-plane upstream-proxy-server password <PASSWORD>
nsappliance(config)# set management-plane upstream-proxy-server trusted-ca
Copy and paste just your single PEM-formatted server CA certificate (no keys).
Enter one or more lines of input. When done, press Ctrl-D
<PASTE PEM Formatted CA CHAIN>
<Press Ctrl-D>
nsappliance(config)# save
nsappliance(config)# exit
nsappliance> restart dlpaas all
Implicit
Example:
nsappliance> configure
Entering configuration mode
nsappliance(config)# set management-plane upstream-proxy-server trusted-ca
Copy and paste just your single PEM-formatted server CA certificate (no keys).
Enter one or more lines of input. When done, press Ctrl-D
nsappliance(config)# save
nsappliance> restart dlpaas all
In this Topic
Appliance Setup

---
## Endpoint DLP Device and Content Control Policies
**URL:** https://docs.netskope.com/en/epdlpcontrol/
**Last Modified:** 2026-06-25T19:14:33+00:00
**Scraped:** 2026-08-23T07:12:58.541198+00:00

Endpoint DLP Device and Content Control Policies - Netskope Technical Documentation
Endpoint DLP Device and Content Control Policies
Endpoint DLP Policy
Endpoint DLP provides two types of protection policies: Device Control and Content Control.
Device Control policies provide decisions about access to devices. These decisions can be based on the user, group membership, endpoint device classification, and destination device characteristics such as device type, serial number, manufacturer, or encrypted state. This feature can be used to ensure that only corporate file shares are used, or that access to USB Mass Storage devices is limited to standard company-issued, encrypted devices.
Content Control policies provide security controls based on the content of the data. Content Control policies can use all the same device and user criteria that are used for Device Control policies, but they can also inspect and classify the content of the data and use this information in policy decisions.
Device Constraints
Netskope Device and Content Control policies do not support prints made to the Microsoft Print to PDF printer and other format conversion printers. Netskope focuses on data exfiltration and does not support software-only format conversion print drivers as format conversion is not considered exfiltration at the time of conversion.
There are multiple methods to convert the format of a file. Modern applications can convert files to many formats even without specifically using PDF print drivers. Thus, Netskope has determined to control only exfiltration printers with DLP policy.
Most destination device types support Device Constraints. Device Constraints are criteria about the destination device such as hardware attributes (Serial Number, Manufacturer, Model) or configuration (Printer Port, Encryption state). Device Constraints can be managed in the Policy>Constraints section of the UI.
You can define Device Control policies that allow users to access only corporate devices. You can leverage device control policies to take action based on the device.
Endpoint DLP Device Control Policies are grouped by RBAC/LBAC-based groups.
All Policy Groups (except for
Default
) can be modified by
Rename
,
Assign Labels
,
Move
,
Enable
,
Disable
, and
Delete
.
There is also RBACv3 support. For more information, see
RBAC v3 Overview
.
Creating Endpoint DLP Device Control Policies
In the Netskope UI, go to
Policies > Endpoint Protection
.
In the
Device Control
tab, click
New Device Control Policy
.
On the
Endpoint Device Control Policy
page:
Endpoint Protection:
Select any of the following criteria for by the policy:
Users
: Select the
Users
,
User groups
, or
Organizational units
affected by the policy. Click + Exclusions to select the users, user groups, or organizations you want to exclude from the policy.Device Classification: Choose to apply the policy to managed or unmanaged devices. You also can click to go to the Device Classification page and configure rules.
Device Classification:
Choose to apply the policy to
Managed
or
Unmanaged
devices. You also can click the
Settings
icon to go to the Device Classification page and configure rules.
Device
: Select
USB storage device
– To allow or block connected USB device on corporate laptops
Printer
– To allow or block local/network printers used by endusers
Network File Share
– To control which network file shares endpoints are allowed to access.
Bluetooth File Control
– To allow or deny outgoing file transfers over Bluetooth.
CD and DVD Drives (Windows)
– To allow or deny writes to discs.
Any
: Select to apply this policy to all devices.
Matches
: Select the constraint profiles that contain the devices you want to include in the policy. For example, you can select a constraint profile that includes a particular brand of USB devices you want to limit access to. Click “
+ Create New
” to create a new constraint profile. This policy only applies to devices that match the selected constraint profiles.
Does not match
: Select the constraint profiles that contain the devices you want to exclude from the policy. For example, you can select a constraint profile that includes all local printer devices. Click + Create New to create a new constraint profile. This policy only applies to devices that don’t match the selected constraint profiles.
For detailed info on
Constraint Profiles
, see
Constraint Profile
.
Action
: Select the action to be performed when the policy is triggered.
Allow
: Select to allow users read and write access to the USB, printer, NFS or Bluetooth File Control.
Make Read-Only
: Select to only allow users read access to the storage device. This is only available for USB devices.
WPD/phone devices do not support Read-Only policy actions. These devices will be blocked.
Block
: Select to block users from accessing the device.
USB Devices can have a notification template displayed to users to explain why their devices are Read-Only.
Set Policy
: Enter a policy name. You can only use alphanumeric characters and symbols such as underscore (_), dash (-), and square brackets ([ ]). You cannot use the greater-than (>) or less-than (<) symbols in policy names. Optionally, You can click + Policy Description to add notes or information and toggle
Status
: Enable or disable the policy.
Creating Endpoint Control Policies
Endpoint DLP depends on the
Microsoft Print to PDF
print driver for
Printer Content Control
. Please ensure that this driver is installed. Endpoint DLP will install a printer called “
Netskope
” which is used for Printer Content Control. If this Printer is removed,
Printer Content Control
will not work.
You can define
Content Control policies
to prevent users from copying or printing sensitive data to sanctioned USB devices, printers, and Bluetooth File Control
on Windows
. You can leverage content control policies to take action based on the sensitive content in the file or where the file came from (i.e., file origin).
Content Control
policies do not apply to phones or WPD devices.
File criteria, such as
File Profiles
are not applicable for
Printer Content Control
policies
. This includes
File Profiles
selected as top-level criteria in Endpoint DLP policies and File Profiles embedded inside DLP Profiles. This means that identification of violations in printed documents will only depend on printed content, not the metadata from any file on disk.
Exceptions
:
Windows
: A few applications have specific integrations to make file filters work. If you print from Microsoft Word or Excel, then file filters can apply so things such as AIP/MIP/Purview Sensitivity Labels can be used for printing enforcement.
macOS
: macOS does not support AIP/MIP/Purview Sensitivity labels for Printing policies in any application.
In the Netskope UI, go to
Policies > Endpoint Protection
.
Click the
Content Control
tab.
Click
New Content Control Policy
.
On the
Endpoint Content Control Policy
page:
Endpoint Protection
: Select any of the following criteria for by the policy:
User
: Select the
users
,
user groups
, or
organizational units
affected by the policy. Click +
Exclusions
to select the users, user groups, or organizations you want to exclude from the policy.
Device Classification
: Choose to apply the policy to
managed
,
unmanaged
, or
Custom
(starting in version 124.0.0) devices. You also can click the
Settings
icon to go to the Device Classification page and configure rules.
Destination
: Select
USB Storage Device
,
Printer (Windows)
,
Bluetooth File Transfer (Windows)
,
Network File Share (Windows)
, and/or
Browser App (Windows, R130+ client required)
for the content destination.
For both the devices, admins can select the following conditions:
Any
: Select to apply this policy to all corporate sanctioned and unsanctioned USB storage devices.
Matches
: Select the constraint profiles that contain the USB devices you want to include in the policy. For example, you can select a constraint profile that includes encrypted USB devices you want to limit access to. Click
+ Create New
to create a new constraint profile. This policy only applies to devices that match the selected constraint profiles.
Does not match
: Select the constraint profiles that contain the USB devices you want to exclude from the policy. For example, you can select a constraint profile that includes all local and network printer devices. Click
+ Create New
to create a new constraint profile. This policy only applies to devices that don’t match the selected constraint profiles.
File
: Select the file information for the policy.
File Profile
: Select the file profiles that define the files you want to allow or block users from copying to a USB storage device or printing. For ex., you can create a file profile which includes text files and/or spreadsheets. Click
+
to create a new file profile. You also can click the
Settings
icon to go to the File Profile page.
File Origin
: Select the predefined or custom applications and application instances that contain files you want to allow or block users from copying to a USB storage device or printing. For example, you can create a file origin with Slack Enterprise or Gmail application instances so that any file downloaded from these apps can be blocked from copying to devices. Under
Exceptions
, you can select the application instances you want to exclude from this policy. You also can click the
Settings
icon to go to the App Definition page and configure a custom app.
Profile & Action:
Select the DLP profiles you want to use to inspect files for violations and configure an action for each profile.
Allow
: Select to allow users to transfer files that have no DLP violations from the USB storage device.
Alert
: Select to receive alerts about files that are transferred to the USB storage device and contain DLP violations.
User Alert
: Select to send a default or custom notification message to users when they transfer files with DLP violations to a USB storage device. Click + Create Template to create a notification message that allows them to proceed after they justify their reasons.
Block
: Select to prevent users from transferring files to the USB storage device, send a default or custom notification message to users when they transfer files with DLP violations. Click + Create Template to create a notification message that teaches them to adhere to your data policy.
Set Policy
: Enter a policy name. You can only use alphanumeric characters and symbols such as underscore (_), dash (-), and square brackets ([ ]). You cannot use the greater-than (>) or less-than (<) symbols in policy names. Optionally, You can click + Policy Description to add notes or information.
Status:
Enable or disable the policy.
Click
Save
and then click
Apply Changes
.
Configuring the Content Control Policy Settings
You can configure the fallback settings when the Netskope cloud can’t perform content inspection for an endpoint because it’s offline, the file size is too large, or there’s a system error.
To configure the Content Control policy settings:
In the Netskope UI, go to
Policies
>
Endpoint Protection
.
Click the
Content Control
tab.
Click
Settings
.
In the
Content Control Policy Settings
window:
When endpoint is offline
: Allow or block files from being copied to an endpoint device when the device is disconnected from the internet.
When file size exceeds DLP scan limit
: Allow or block files from being copied to an endpoint device when the file size is larger than the DLP scan limit.
When system error occurs
: Allow or block files from being copied to an endpoint device when there is a system error.
Click
Save
and then click
Apply Changes
.
Printer Content Control Notifications when printing from Web Browsers
Users will be notified through popups associated with the Netskope Client when printing.
Netskope is gathering the print data associated with the file that will be printed.
Netskope is analyzing the gathered data from the previous step.
Netskope is allowing the printing of the document. Depending on the size of the document, this popup may stay on the screen for a long time.
Netskope is printing the pages in the desired order.
Reporting All Matched DLP Profiles
This feature is in controlled-GA. For more information, contact support@netskope.com.
The DLP engine can now evaluate policies beyond the first matching policy. It will evaluate all possible DLP profiles across policies to get visibility into profiles that match resulting in Alerts and Incidents showing all DLP profiles matched. If the option is enabled, then every DLP profile that can be matched, will be alerted upon.
To enable this:
In the Netskope UI, go to
Policies > Endpoint Protection > Content Control
and click
Settings
.
Check the
Evaluate all DLP profiles
checkbox.
Process Exclusion
This feature is currently Controlled-GA. For more information, contact your account executive or support@netskope.com
Microsoft Office and Adobe Acrobat cannot be excluded from print monitoring with this feature.
Processes can be excluded from Endpoint DLP evaluation for certain applications. This is used to exclude Endpoint DLP intervention in certain processes for printing, USB, and network file sharing.
To use this:
In the Netskope UI, go to
Policies > Endpoint Protection > Content Control
and click
Process Exception
.
Click
+ADD
Fill in the
Process Executable Path
,
Operating System
, and
Description
.
Click
Save
.
Browser Application Control
Starting from R130, Browser Application Control is now supported. Policies can be defined about files that browsers read for upload. These policies allow control over what company data users can share over the internet. Every file can be evaluated against a policy when the browser process opens the file for transfer. If the file policy is
Blocked
, then the file access by the browser will be blocked.
Chrome, Microsoft Edge, and Firefox are supported.
The filter option of ‘Browser Upload’ are now available on the following event/alert pages.
Endpoint Events – Content Control : ‘Activity’
Alerts : ‘Endpoint Activity’
MacOS Support on Safari via JAMF
Safari Extensions are installed by default with our Client installer and are visible under Extensions tab under settings, but extensions need to be enabled and managed via MDM.
Safari Extensions via JAMF are delivered via the User channel.
Requirements:
JAMF Pro or higher
Blueprints feature enabled (
see guide
)
Deployment Steps
:
Login
to your JAMF account and navigate to
Blueprint
. Click on
Create Blueprints
.
Under the
Component group
, search for
Safari Extensions
and drag and drop the widget under the
Declaration group
as shown below:
Click on the
Safari Extension widget
and enter the following values:
Extension Identifier:
com.netskope.epdlp.client.NetskopeEpdlpBrowserExtension (24W52P9M7W)
Extension State:
Always on
Private Browsing State:
Always on
Allowed Domains:
*
Note: This will enable the extension for all websites. If you need it for only specified domains, add the appropriate values.
Click on
Save
and
Deploy
to the devices.
Once deployed, blueprint profiles can be checked on the enrolled device under:
Settings > General > Device Management > MDM Profile > User Declarations
Once blueprint is applied, the Safari Extensions will be enabled on Safari and tamperproof.
MacOS Support on Chrome via JAMF
Requirements:
JAMF Pro or higher
Blueprints feature enabled (
see guide
)
Open
Jamf Pro
>
Computers
>
Configuration Profiles
Create a Configuration profile with
External Applications
under
Application & Custom Settings
Under
External Application
, select
Source as Jamf Repository
Application Domain
–
com.google.Chrome
Version
–
M87
Variant
–
chrome-mac-cbcm.json
Cloud Management Enrollment Token
obtained from Google Workspaces
Click on
Add/Remove Property
, add a
Property
with name –
ExtensionInstallForcelist
Under
ExtensionInstallForceList
, select
array
Under Item1, select
string
Enter the value as –
hoiidijefcaokcehchgpjppeddfkanlf;file:///Library/Application%20Support/Netskope/EPDLP/webExtension/update.xml
final plist will be similar to the following image (ensure the
token id
is the actual value):
Add
Scope
and apply the profile to the devices. Once
Profile
is available it will be listed under
General > Device Management > Profile Name
.
Relaunch Chrome and check the Extension page, The
Netskope EndpointDLP
extension is installed and in a managed state.
With this method, Netskope cannot manage the plugin. This can be done only in Google Admin Workspaces.
Large File Sampling
Starting from R130 when Large File Sampling is enabled, DLP with inspect the first 128MB of a large file up to 2GB either allow or block the transfer of the file based on the results of the inspection. This works for large files being uploaded by browser to the web (Browser Application Control) or large files being copied to a USB device from a user workstation.
In this Topic
Endpoint DLP Device and Content Control Policies

---
## About DLP
**URL:** https://docs.netskope.com/en/about-dlp/
**Last Modified:** 2026-06-25T19:32:37+00:00
**Scraped:** 2026-08-23T07:13:31.821620+00:00

About DLP - Netskope Technical Documentation
About DLP
Netskope
Data Loss Prevention (DLP)
protects sensitive data in the cloud with accuracy and precision by inspecting all sanctioned and unsanctioned cloud services. When users violate a DLP policy, Netskope logs the incident. If you have
Endpoint DLP
, users that violate your Content Control policies also trigger a DLP incident.
Note
Incidents are generated for each file/sub-file that matches DLP Profile(s) and the corresponding DLP Rules, Fingerprint Rules, ML-based Classifiers or File Profiles. A sub-file is any file within a container file (e.g. file within a zip/tar or an image in a pptx document or a spreadsheet in a docx file). One incident will be generated for each container file and one each for any sub-files that match DLP Profiles.
If a PowerPoint document matches a DLP Rule used in a DLP Profile, one incident will be created for that file. If an embedded image of a Credit Card in the same PowerPoint document matches an ML-based Classifier for Credit Cards, another incident will be created for that image.
If DLP finds a violation in a embedded document, only the embedded file name is recorded. For example, if a zip file,
Data.zip
, contains an Excel spreadsheet,
Microsoft_Excel_Worksheet.xlsx
, the violation will only record the
Microsoft_Excel_Worksheet.xlsx
file and
NOT
the
Data.zip
file.
The DLP service has an internal limit of generating only 50 incidents for a given request.
For example, if a .zip file has 300 files, DLP service will generate at most 50 incidents.
All matched embedded files generate an incident in case of introspection and CASB.
For inline (nsProxy) requests, DLP generates events/incidents only for the profile associated with the highest priority policy. The incident limit combined with generating events/incidents only for the highest policy/profile matched may result in alerts generated that don’t have a corresponding incident. For example, if the first 50 embedded files match a lower priority policy/profile and subsequent embedded files match a higher priority policy/profile, then the incidents for the higher priority profile are not recorded as the limit has been reached.
Viewing DLP Incidents
Incident grouping depends on whether the Object ID or hash changes; incidents are grouped if the Object ID remains the same, and a change in hash triggers a new incident, with filename changes not necessarily causing new incidents if content remains unchanged.
To view DLP incidents in your organization, go to
Incidents
>
DLP
.
Refresh the DLP incident results.
Filter DLP incidents by a specific time frame. You can use a predefined time frame or choose
Date Range
to use the calendar and time menus to customize your own.
Search and filter the DLP incidents by a query. Click
+ Add Filter
to add other filters to narrow your search results. For example, you can choose
Block
for the
Last Action
and select an application to only view DLP incidents that match this criteria. You can also click
to switch to the advanced query search mode. Click
to save the filter combination for future searches.
Note
If you have
Endpoint DLP
, you can filter incidents by
Endpoint Content Control Policy
.
View the top 5 applications, exposures, and top 5 policies with violations.
View a list of DLP incidents. For each incident, you can see the following default information:
Object
: The file or object name that triggered the violation. Click to open a page with more details where you can change status, assign incidents, change severity, and take actions.
Application
: The application that triggered the violation.
Site
: The website that triggered the violation.
Exposure
: The exposure level of the file.
Public – Indexed
Public – Unlisted
Public
Private
Externally Shared
Internally Shared
Enterprise Shared
Cross-Geo
# Violations
: The total number of violations with file. The count refers to the aggregated number of records detected across all the policies in the incident.
Last Action
: The action that was taken, such as allow, block, alert, etc.
Status
: Shows the state of the event. There are three states:
New
In Progress
Resolved
Assignee
: The person assigned to monitor the incident.
Severity
: The severity level of the object or file. There are four levels:
Low
Medium
High
Critical
In addition, if you selected
Count only unique record
under
Severity Threshold
for a
DLP rule
, then the severity displays the count as
Count: <Number of Violations> unique
. If you deselect
Count only unique record
, the severity count is displayed as
Count: <Number of Violations>
.
Object ID
: The ID of the object or file.
Timestamp
: The date and time that the violation occurred.
Instance
: The application instance that triggered the violation.
Instance Id
: The ID of the application instance.
Last Modified By
: The user that made the latest changes to the file when Netskope processed it.
Note
In API Data Protection for ServiceNow, for certain types of activities, the
Last Modified By
user can be the ServiceNow system administrator user instead of the actual user. This is because for certain activities like a file upload, ServiceNow performs some checks and scans. Due to this the
Last Modified By
user can be `system` or `admin`.
Object Owner
: The original owner of the object or file.
File Path
: The full file path on the device.
DLP Policy
: The DLP policy that triggered the violation.
DLP Profile
: The DLP profile associated with the DLP policy and violation.
DLP Rule
: The DLP rules associated with the DLP policy and violation.
Select one or more objects to update the
Mark Status As
and
Severity
as well as
Assign
someone to monitor the incident.
Sort the table by the following:
Object
Application
Site
Exposure
Status
Assignee
Severity
Instance
Last Modified By
Object Owner
Timestamp
Select one or more objects to update the status. You also can:
Create Custom Status
: Create a name for a custom status.
Manage Custom Statuses
: View, edit, or delete any custom states.
Select one or more objects to edit the severity level.
Select one or more objects to choose an email address of an admin to monitor the incident.
Export all DLP incidents (up to 500,000 rows) to a CSV file as a summary or including all details.
Click
to customize table columns or restore the default ones.
View up to 100 DLP incidents per page.
View multiple pages of the table.
Viewing Object Details
On the DLP page, you can click the
Object
to see more comprehensive details.
At the top of the Object Details page, you can edit the:
Status
: Choose a status for the object. Click
to:
Create Custom Status
: Create a name for a custom status.
Manage Custom Statuses
: View, edit, or delete any custom states.
Assigned to
: Choose an email address of an admin to monitor the object.
Severity
: Choose a severity level for the object.
Actions
: Perform any of the following actions.
Encrypt
: Encrypt the object.
Restore
: Restore the object.
Block
: Block the object.
Note
The Netskope tenant UI has disabled the encrypt, restore, block actions for files with ‘require check out’ option enabled in Microsoft Office 365 SharePoint Sites. In cases when ‘require check out’ is enabled, a copy of the file will be placed in quarantine, however, the original file will not be deleted.
Delete
: Delete the object.
Change File Permissions
: Change the object permissions by restricting access to certain admins, users, file owners, etc.
Contact Users
: Contact the users involved with the object.
Check Object History
: View the history around the object, including all incidents that occurred with the object, logs of remediation or actions taken on the object, and other activity and version information related to the object from API Data Protection.
Download Object
: Download the incident object to the folder defined in your
Forensic Profile
. To learn more:
Downloading DLP Incident Files
.
View More
: View current summary details on the object, including basic info, shared links, collaborators, and version history.
When a tombstone fails, Netskope displays an error message:
Viewing the Incident Detail
Under
Incident Detail
on the Object Details page, you can see comprehensive object details:
Timestamp
: The date and time that the violation occurred.
Type
: The type of incident.
Entity Created
: Shows the timestamp of when the entity was created on the SaaS app. This applies to Next Generation API Data Protection only.
Last Modified
: Displays the timestamp of when the entity was last updated or modified. This applies to Next Generation API Data Protection only.
Last Modified By
: The user that made the latest changes to the file when Netskope processed it.
Note
In API Data Protection for ServiceNow, for certain types of activities, the
Last Modified By
user can be the ServiceNow system administrator user instead of the actual user. This is because for certain activities like a file upload, ServiceNow performs some checks and scans. Due to this the
Last Modified By
user can be `system` or `admin`.
Activity
: The activity associated with the incident.
Action Taken
: The action taken on the incident based on your policies.
Violations
: The total number of violations with file. The count refers to the aggregated number of records detected across all the policies in the incident. Click
to go to the
Skope IT Alerts
.
Application
: The cloud application (e.g., Dropbox) that triggered the violation.
Site
: The site that triggered the violation. If the
Traffic Type
is
Cloud App
, the site displays the cloud app name. If the
Traffic Type
is
Web
, the site displays the second level domain name and top-level domain name. For example, for “www.cnn.com”, it’s “cnn.com”.
Instance
: The application instance that triggered the violation.
URL
: The URL of the file or application that triggered the violation.
Object Name
: The file or object name that triggered the violation. Click
to go to
File Details
in API-enabled Protection.
Object Type
: The type of the object that is being acted on. It might be a file, folder, report, document, message, etc.
File Path
: The full file path on the user’s device.
File Type
: The type of file.
File Size
: The file size in bytes.
File Owner
: The creator of the file in the application.
Note
In Google Drive, when you change ownership of a folder, it changes the ownership of the selected folder only and does not include the files inside. For example, if you change the ownership of a folder from
user A
to
user B
:
the ownership of the folder changes to
user B
.
the ownership of the contents of the folder i.e., files and folders does not change to
user B
. It remains with
user A
.
File Language
: The written language of the file.
True File Type
: The type of true file.
True File Category
: The category of the true file.
From User
: The email address used to login to the SaaS app.
Channel
: The channel of the user for Slack and Slack Enterprise apps.
Data Classification
: The data classification details.
Incident ID
: The incident ID associated with the subfile. If the incident is triggered for the main file, the incident ID will be the same as the parent incident ID.
Parent Incident ID
: The incident ID associated with the main container (or non-container) file that was scanned.
Object ID
: The ID of the object or file.
MD5
: The MD5 hash of the file. You can use this hash value to filter Skope IT events and view other activity associated with the file.
Connection ID
: The ID for the connection incident. Each connection has a unique ID.
App Session ID
: The unique app/site session ID when the
Traffic Type
is
Cloud App
or
Web
. An app session starts when users start using a cloud app/site and end after they’ve been inactive for a certain period of time (e.g., 15 mins). You can use this ID to check all the user activities in a single app session. The app session ID is unique for a user, device, browser, and domain.
Referer
: The referrer URL of the application (with HTTP) that the user visited.
Source
: The user’s city as determined by the Maxmind or IP2Location Geodatabase.
Destination
: The application’s city as determined by the Maxmind or IP2Location Geodatabase.
Viewing Violations
Under
Violations
on the Object Details page, you can see a list of all the DLP violations for the object:
Click
to view a preview of the data identifier matches. You can hover over the highlighted matches to see the DLP profile triggered, data identifier, DLP rule triggered, and severity level. Not all matches are highlighted due to storage limit.
Under
Overview
, see the following:
Policy
: The triggered DLP policy. Click
Edit Policy
to go to the Real-time Protection page and edit the
DLP policy
.
Violations
: The total number of violations for the DLP policy.
Rule Hit
: A list of triggered DLP rules.
Policies
: A list of DLP policies associated with the triggered DLP rule.
Severity
: The severity level and hit count for each DLP rule. If you selected
Count only unique record
under
Severity Threshold
for a
DLP rule
, then the severity displays the count as
Count: <Number of Violations> unique
. If you deselect
Count only unique record
, the severity count is displayed as
Count: <Number of Violations>
.
Under
DLP Rule Violations
, see the following:
#
: The violation number.
Preview
: A list of the data identifier matches. Hover over to see the triggered data identifier.
Rule
: Click to view details on the associated DLP rule. Click
View Rule
to go to the
DLP Rule page
.
DLP Profile
: Click to view details on the associated DLP profile. Click
View Profile
to go to the
DLP Profile page
.
DLP Policy
: Click to view details on why the violation triggered the DLP policy. Click
Edit Policy
to go to the Real-time Protection page and edit the
DLP policy
.
Workflow Configuration
This feature is not available in tenants hosted in RUH1.
Incidents can be escalated to the manager of the user that triggered the incident. This allows the manager of the acting user to give their
verdict,
whether the triggering action is required for business purposes or if it violates the company policy. Based on this feedback, the analyst can decide how to proceed with the incident resolution.
The manager must click on the appropriate verdict to complete the workflow. Once a verdict is provided, the verdict cannot be modified and clicking the other verdict will have no effect.
Reminder emails will be sent to the manager 20 days after triggering the workflow.
Workflows expire after 30 days of triggering and will transition to a
No Response
state, at which point the analyst can re-trigger the workflow.
Prerequisite
Ensure that
Custom SCIM Attributes
have been enabled for the organization in order for the manager emails to be pulled properly.
The workflow cannot be triggered if the acting user is not
imported
into the Netskope tenant or if that user does not have a valid manager email configured in their custom SCIM attributes.
Configuring Workflow
The workflow must be initially configured for the tenant before it can be used. This workflow configuration is global and not incident-specific.
From the Netskope tenant, go to
Incidents > DLP
.
On the right-hand side, click
Workflow Configuration
.
The
Manager Escalation Configuration
pane slides in.
Map the proper custom attribute for every user’s manager’s email .
Click
Save
.
After configuring the workflow, the page needs to be
refreshed
to get the
Escalate to Manager
option to be enabled. From here, you can initiate the workflow.
Initiating Workflow
From the admin console, go to
Incidents > DLP
.
Click on any incident.
On the right-hand side, click
Initiate Workflow > Escalate to Manager
.
This will send an email notification to the user’s manager asking for their verdict whether the
Action is required for business
or the
Action violates company policy
.
From the incident itself, the status of the workflow can be seen.
Adding Notes to DLP Incidents
Notes can now be added to DLP incidents. Notes have
512
character limit and up to 25 notes can be added.
Note privileges can be found in
Settings -> Administration -> Roles
-> (Role) -> Privileges -> Incidents
-> DLP
. You will be able to set roles to view-only
(View)
or adding-allowed
(Manage
).
To add a note:
Go to
Incidents
>
DLP
.
Click on any
Incident
.
Click the
Incident Notes
button highlighted above. This will open the
Incident Notes
window.
Enter your text and press
Add Note
. Added notes will be associated with the user who logged in while adding them. Users (with at least write permission) can be tagged with @. These notes will notify the person assigned to the incidents including those tagged on the specific note.
In the event that there are multiple
Incidents
in one
Incident Event
, each
Incident
will maintain its own note thread.
Viewing DLP Incidents Related to Deleted Files
To see if a file was deleted:
Go to
Incidents
>
DLP
.
Click the
Object
. The Object Details page appears.
Under
Actions
, Netskope displays an attention message:
Downloading DLP Incident Files
In this Topic
About DLP

---
## Start a DLP Content Inspection Job for Unstructured Data (Asynchronous)
**URL:** https://docs.netskope.com/en/start-dlp-content-inspection-job/
**Last Modified:** 2026-06-25T19:16:10+00:00
**Scraped:** 2026-08-23T07:13:38.921309+00:00

Start a DLP Content Inspection Job for Unstructured Data (Asynchronous) - Netskope Technical Documentation
Start a DLP Content Inspection Job for Unstructured Data (Asynchronous)
This API is an asynchronous endpoint for scheduling DLP (Data Loss Prevention) content inspection jobs. This API accepts content for inspection and returns either a job ID for asynchronous processing or immediate results from cache if available.
This endpoint has some additional limitations:
Max File Size
: 1 megabyte
Max DLP Profiles
: 100
Character Length of Each Profile name:
256 characters
Request Endpoint
POST
https://<appliance_ip>/inspections/jobs
Call Example
curl -X 'POST' \
  'https://10.0.0.1/inspections/jobs' \
  -H 'accept: multipart/form-data' \
  -H 'x-netskope-generate-incidents: true' \
  -H 'Content-Type: multipart/form-data' \
  -F 'request={"profiles":["DLP-PCI","DLP-PII"],"content":{"id":"b1f793e4d4a26ac7b695bb1fd1fb0ce3cb5d729c401d8528f8bb92598006cf85","name":"SecretFile.txt","object_id":"AA-74GXZ","true_file_type":230},"modules":{"file_filter":{"skip":true},"drm":{"labels":[{"id":"c7d03ebd-804d-489c-94c6-8167224c3c1b","name":"chris_encryption_all_enabled","instance":"epdlpsjc1","vendor":"mip"}]}},"results":{"verdict":"summary"},"sender":{"app_name":"AWS_RDS"}}' \
  -F 'content=@SecretFile.txt;type=text/txt'
Response Example
#A cached hit was found, therefore no job was scheduled. The results are returned in json.
#200 Response
HTTP/1.1 200 OK
Content-Type: multipart/form-data; boundary=8b9eb155309408d78d1886c2af2803fdba94a7bea3dac274b3da5fa31e92
--8b9eb155309408d78d1886c2af2803fdba94a7bea3dac274b3da5fa31e92
Content-Disposition: form-data; name="result_data"
Content-Type: application/json
{"status":"success","summary":{"profiles":["DLP-PCI","DLP-PII"],"transaction_id":"3947352303853909965","verdict":"hit","verdict_type":"full"}}
--8b9eb155309408d78d1886c2af2803fdba94a7bea3dac274b3da5fa31e92--
#No prior request is found and a new job is started.
#202 Response
{
  "job_id": "8a426a5f-0d2e-0a2e-3595a-303202a7a2e"
}
The request header
x-netskope-generate-incidents
is added so that users can specify their choice for generating alerts & incidents.
The response headers have also been created:
x-netskope-incidents-posted
. The response header reflect whether the alerts and incidents were posted to the management plane.
Valid Query Parameters are:
Name
In
Type
Required
Description
body
body
object
true
none
» request
body
object
true
Specifies the properties of an inspection request.
»» profiles
body
true
A list of profiles to use during the scan. Profiles determine which DLP rules are used when searching for matches.
»» content
body
true
Describes the content that is being sent to DLP as part of the request.
»»» id
body
string
true
SHA256 hash of the content
»»» name
body
string
false
The name (e.g. filename) of the content.
»»» object_id
body
string
false
An object identifier for the data.
»»» true_file_type
body
integer
false
Netskope true file type (numerical ID)
»» modules
body
false
Specifies settings for individual DLP modules that will be used during the inspection.
»»» file_filter
body
object
false
Specifies settings for the File Filter module.
»»»» skip
body
boolean
false
If true file filtering will be skipped.
»»» drm
body
object
false
Allows for explicit DRM labels to be passed into DLP.
»»»» labels
body
[object]
true
none
»»»»» id
body
string
true
The id of the label.
»»»»» name
body
string
false
The name of the label.
»»»»» instance
body
string
false
The instance of the label.
»»»»» vendor
body
string
true
The vendor of the label.
»» results
body
object
false
Specifies properties for the DLP On Demand results returned from the inspection.
»»» verdict
body
string
false
Specifies how much match detail should be returned. One of the following will be returned:
summary
– Summary of the verdict is returned. This will include the outcome, verdict type, list of the profiles, severity.
details
– Includes match details. Details about verdict has result matches, profile and rules per file.
forensics
– Includes summary, details and forensics of the matches. All match details including rule information, matched text and extracted content will be returned. Please note that this will cause a full scan of the file. If no
verdict
is specified, it would default to summary type and the summary of the verdict will be returned.
»» sender
body
false
Describes the request caller.
»»» app_name
body
string
true
Application that triggered the call
» content
body
string(binary)
true
none
Enumerated Values
Parameter
Value
»»» verdict
summary
details
forensics
Responses
Status
Meaning
Description
Schema
200
OK
A prior request is found and this is a cached response. The results are returned in json.
Inline
202
Accepted
Indicates that the request has been accepted. This is the normal, expected result.
Inline
400
Bad Request
The request was invalid. The response contains the error that caused the request to be rejected, if available.
string
413
Payload Too Large
The specified content is too large to be scanned.
None
500
Internal Server Error
An error occurred while performing the request. The response contains the error that caused the request to be rejected, if available.
string
503
Service Unavailable
No resources are available to perform the request.
None
allOf
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
false
none
The name of the profile.
and
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
any
false
none
The profile to which the matched
rules
are attached.
continued
Name
Type
Required
Restrictions
Description
»»»» action_threshold_met
boolean
true
none
If
true
, the action threshold was met indicating that the DLP Client should perform the action associated with this profile. If this field is
false
the action threshold was not met and the action associated with this profile should not be performed.
»»»» maximum_severity
string
false
none
The maximum severity of the matched rules.
»»»» rules
[object]
false
none
none
»»»»» name
string
true
none
The name of the rule.
»»»»» severity
string
true
none
The severity of the rule hit. One of:
none
low
medium
high
critical
»»»»» type
string
true
none
The type of the rule. One of:
entity
: A rule that matches when a specific entity is found. For these rule matches the
entity
subfields will be present.
not_entity
: A rule that matches when a specific entity is not found. For these rule matches the
entity
subfields will be present.
file_filter
: A file filter rule. classification A classification rule. fingerprint A fingerprint rule. For these rule matches the
fingerprint
subfields will be present.
fingerprint_group
:
A fingerprint 2.0 group rule. For these rule matches the
fingerprint_group
subfields will be present.
structured_classification
: A structured classification rule. For these rule matches the
structured_classification
subfields will be present.
»»»»» entity
object
false
none
Contains details about the entity rule that matched. This field is present when
type
is
entity
or
not_entity
.
»»»»»» weighted
boolean
true
none
If
true
this rule is using the weighted
score
to determine the severity. If
false
,
count
is being used.
»»»»»» score
integer
true
none
The weighted score of the rule matches.
»»»»»» limit_reached
boolean
true
none
If
true
the maximum number of matches for this rule was reached. This means that some identified data was omitted from the results.
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»»» entity
string
true
none
The name of the entity that resulted in a match.
»»»»»»» count
integer
true
none
The number of times the given
entity
was matched.
»»»»»»» data_type
false
none
General data type describing this entity.
»»»»»»» sensitivity_level
true
none
The severity of the rule hit. One of:
none
low
medium
high
critical
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of:
not_sensitive
low
medium
high
critical
»»»»»» unique_count
integer
false
none
The number of unique entries that matched the rule. This field is only present when the profile specifies that rules should be uniquely counted.
»»»»» structured_classification
object
false
none
Details of a matched classification type rule
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of
not_sensitive
low
medium
high
critical
»»»»»» data_type
false
none
General data type describing this entity.
»»»»» fingerprint
object
false
none
This field is present when
type
is
fingerprint
.
»»»»»» classification
string
true
none
The classification that matched.
»»»»»» match
string
true
none
The file that matched.
»»»»»» score
integer
true
none
The score of the matched finterprint.
»»»»» fingerprint_group
object
false
none
This field is present when
type
is
fingerprint_group
.
»»»»»» match
string
true
none
The fingerprinted file that matched.
»»»»»» score
integer
true
none
The similarity score of matched fingerprinted file.
»»» forensics
object
false
none
none
»»»» extracted_text
string(string)
false
none
String identifier used to correlate the extracted text with its corresponding part in the multipart response
»»»» entity_rule_matches
string(string)
false
none
String identifier used to correlate the entity rule matches with its corresponding part in the multipart response.
»»»» preview_image
string(string)
false
none
String identifier used to correlate the preview image with its corresponding part in the multipart response.
»»»» original_subfile
string(string)
false
none
String identifier used to correlate the original subfile with its corresponding part in the multipart response.
Enumerated Values
Property
Value
InspectionStatus: status
success
timeout
error
verdict
hit
no_hit
verdict_type
full
partial
severity
none
low
medium
high
critical
MicrosoftAipProtectionStatus: status
protected
unsanctioned
sanctioned
severity
none
low
medium
high
critical
type
entity
not_entity
file_filter
classification
fingerprint
fingerprint_group
structured_classification
sensitivity_level
not_sensitive
low
medium
high
critical
Status Code
202
This object is returned to the DLP On Demand Appliance for an asynchronous inspection request to indicate that DLP has accepted the request and will process it asynchronously.
Name
Type
Required
Restrictions
Description
» job_id
true
none
A request-specific token.
This operation does not require authentication
In this Topic
Start a DLP Content Inspection Job for Unstructured Data (Asynchronous)

---
## Get Results of Prior DLP Inspection
**URL:** https://docs.netskope.com/en/getting-dlp-inspection-results-cache/
**Last Modified:** 2026-06-25T19:16:06+00:00
**Scraped:** 2026-08-23T07:13:40.120116+00:00

Get Results of Prior DLP Inspection - Netskope Technical Documentation
Get Results of Prior DLP Inspection
This API is used to get the results of a previous DLP inspection of content by checking the DLP cache. No content is sent in this request so sending it before starting an inspection job can result in a significant savings both in time and bandwidth. This endpoint only works for verdict type:
summary
or
details
.
This endpoint has some additional limitations:
Max File Size
: 1 megabyte
Timeout
: 10 seconds
Max DLP Profiles
: 100
Character Length of Each Profile name:
256 characters
Request Endpoint
POST
https://<appliance_ip>/inspections/cachelookup
Call Example
curl -X 'POST' \
  'https://10.0.0.1/inspections/cachelookup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "profiles": [
    "DLP-PCI",
    "DLP-PII"
  ],
  "content_ids": [
    "b1f793e4d4a26ac7b695bb1fd1fb0ce3cb5d729c401d8528f8bb92598006cf85"
  ],
  "results": {
    "verdict": "verdict"
  }
}'
Response Example
#200 Response
[
  {
    "content_id": "b1f793e4d4a26ac7b695bb1fd1fb0ce3cb5d729c401d8528f8bb92598006cf85",
    "cached_profiles": [
      "string"
    ],
    "uncached_profiles": [
      "string"
    ],
    "result_data": {
      "status": "success",
      "status_info": "Text extraction was skipped.",
      "summary": {
        "verdict": "hit",
        "verdict_type": "full",
        "severity": "low",
        "profiles": [
          "DLP-PCI",
          "DLP-PII"
        ],
        "transaction_id": "93434304"
      },
      "results": [
        {
          "bypassed_profiles": [
            "DLP-PCI",
            "DLP-PII"
          ],
          "metadata": {
            "subfile": false,
            "file_id": 1,
            "name": "pci-hit.txt",
            "size": 811,
            "sha256": "b2e68f87b6d17de54f4ab8a1e59f36619211558ab0f301f921c4b575edc792ea",
            "language": "ENGLISH",
            "type": "Plain Text file",
            "category": "Text",
            "mime_type": "text/plain",
            "protection": {
              "encryption": {
                "file_typing": true,
                "classification": true,
                "classification_score": 0.95
              },
              "microsoft_aip": {
                "status": "protected"
              }
            },
            "drm": {
              "labels": [
                {
                  "id": "c7d03ebd-804d-489c-94c6-8167224c3c1b",
                  "name": "chris_encryption_all_enabled",
                  "instance": "epdlpsjc1",
                  "vendor": "mip",
                  "data_classification_label": "mip/epdlpsjc1/chris_encryption_all_enabled"
                }
              ]
            }
          },
          "matches": [
            {
              "id": "4826568926313255945",
              "cached": false,
              "profile": "string",
              "action_threshold_met": true,
              "maximum_severity": "low",
              "rules": [
                {
                  "name": "Name-Credit Card (CC)",
                  "severity": "low",
                  "type": "entity",
                  "entity": {
                    "weighted": "false",
                    "score": 1,
                    "limit_reached": false,
                    "entities_summary": [],
                    "matches_count": 2,
                    "sensitivity_level": "high",
                    "unique_count": 8
                  },
                  "structured_classification": {
                    "entities_summary": [],
                    "matches_count": 2,
                    "sensitivity_level": "high",
                    "data_type": "Personal Names"
                  },
                  "fingerprint": {
                    "classification": "tbd",
                    "match": "tbd",
                    "score": 1
                  },
                  "fingerprint_group": {
                    "match": "/path/to/matched/file.txt",
                    "score": 90
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  }
]
Responses
Status
Meaning
Description
Schema
200
OK
The request was successful.
Inline
400
Bad Request
The request was invalid. The response contains the error that caused the request to be rejected, if available.
string
500
Internal Server Error
An error occurred while performing the request. The response contains the error that caused the request to be rejected, if available.
string
503
Service Unavailable
No resources are available to performing the request.
None
Response Schema
Status Code
200
An array of inspection results, one for each content ID specified in the request.
Name
Type
Required
Restrictions
Description
» content_id
true
none
SHA256 hash of the content that has been sent.
» cached_profiles
[string]
true
none
The list of profiles that were found in the cache for this content ID.
» uncached_profiles
[string]
true
none
The list of profiles that were not found in the cache for this content ID.
» result_data
object
false
none
Contains the overall result of the inspection. This includes the status of the inspection and any matches produced as a result of the inspection.
»» status
true
none
Specifies the status of a scan request. success – The content was inspected successfully. timeout – The content inspection took too long and was timed out. error – An error occurred while performing the content inspection.
»» status_info
string
false
none
Additional information about the status. For example, if
status
is
error
, this field may be present to provide details about the error that occurred.
»» summary
false
none
none
»»» verdict
string
true
none
The verdict. One of:
hit
no_hit
»»» verdict_type
string
true
none
The verdict type. One of:
full
partial
»»» severity
string
false
none
The severity of the rule hit. One of:
none
low
medium
high
critical
»»» profiles
true
none
A list of profiles to use during the scan. Profiles determine which DLP rules are used when searching for matches.
»»» transaction_id
string
true
none
The transaction ID for this match.
»» results
[object]
false
none
When a scan completes successfully (
status
is
success
) this field may be present. It contains an array of entries – one for each file/subfile in the content that was scanned. Only files/subfiles that had rule matches or could not be scanned because they were protected will show up here. Files that were scanned but did not meet one of these two conditions do not appear here.
»»» bypassed_profiles
[string]
false
none
Specifies the list of profiles from the request that were bypassed because the file being scanned was protected in some way. If this field is not present, no profiles were bypassed.
»»» metadata
object
true
none
Metadata about the inspected content.
»»»» subfile
boolean
true
none
If a container file is passed to DLP, the subfiles within it are also scanned. If this field is
true
the match is for a subfile. If this field is false, either the content passed to DLP was not a container or the match was on the container itself.
»»»» file_id
integer
false
none
The internal identifier of the file/subfile.
»»»» name
string
false
none
The name (e.g. file name), if any, of the inspected content.
»»»» size
integer(uint64)
false
none
The size in bytes of the file/subfile.
»»»» sha256
string
false
none
The SHA256 hash of the inspected content.
»»»» language
string
false
none
The detected language of the inspected content.
»»»» type
string
false
none
The detected type of the inspected content.
»»»» category
string
false
none
The detected category of the inspected content.
»»»» mime_type
string
false
none
The MIME type of the inspected content.
»»»» protection
object
false
none
The field is present when the content is protected in some way. The protection may include one or both of
encryption
and
microsoft_aip
.
»»»»» encryption
object
false
none
The content is encrypted. No match data can be produced for encrypted content.
»»»»»» file_typing
boolean
false
none
Encrypted content detected with file typing.
»»»»»» classification
boolean
false
none
Encrypted content detected with classification.
»»»»»» classification_score
number(double)
false
none
The score of encrypted content detected with classification.
»»»»» microsoft_aip
object
false
none
The content is Microsoft AIP protected. If the content can be unprotected it will be inspected and match data may be produced. If it cannot be unprotected match data cannot be produced.
»»»»»» status
string
true
none
The Microsoft AIP protection status:
protected
: The content could not be unprotected, and was not inspected.
unsanctioned
: The content was AIP protected outside of a known MIP infrastructure and therefore could not be unprotected and was not inspected.
sanctioned
: The content was AIP protected by a known MIP infrastructure. Such content may be uprotected and scanned. It also may have DRM labels extracted.
»»»» drm
object
false
none
The content is protected by a DRM system.
»»»»» labels
[object]
true
none
An array of DRM label objects that contain detailed DRM label information.
»»»»»» id
string
true
none
The id of the label.
»»»»»» name
string
true
none
The name of the label.
»»»»»» instance
string
true
none
The instance of the label.
»»»»»» vendor
string
true
none
The vendor of the label.
»»»»»» data_classification_label
string
true
none
The data classification label.
»»» matches
[object]
false
none
An array of match entry objects that contain detailed DLP match information.
»»»» id
string
false
none
The match identifier. If this is a
cached
match, this will be set to the
id
of the previous match. Otherwise this field is a new identifier that DLP will use to refer to the match if it is seen in the future. Furthermore, for a non-cached response there will be a corresponding
extracted_text
multipart/mixed part returned for this file and this value will be set in the
name
field of the
Content-Disposition
header for that part.
»»»» cached
boolean
true
none
If
true
this match was found in the DLP cache, meaning the content has already been scanned for this profile and thus was not scanned as part of this request.
id
is set to the
id
that was created when the content was scanned. Because of this, there will be no
forensics
associated with the match as forensic data is not stored in the DLP cache.
»»»» profile
any
true
none
none
allOf
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
false
none
The name of the profile.
and
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
any
false
none
The profile to which the matched
rules
are attached.
continued
Name
Type
Required
Restrictions
Description
»»»» action_threshold_met
boolean
true
none
If
true
, the action threshold was met indicating that the DLP Client should perform the action associated with this profile. If this field is
false
the action threshold was not met and the action associated with this profile should not be performed.
»»»» maximum_severity
string
false
none
The maximum severity of the matched rules.
»»»» rules
[object]
false
none
none
»»»»» name
string
true
none
The name of the rule.
»»»»» severity
string
true
none
The severity of the rule. One of: none low medium high critical
»»»»» type
string
true
none
The type of the rule. One of:
entity
: A rule that matches when a specific entity is found. For these rule matches the
entity
subfields will be present.
not_entity
: A rule that matches when a specific entity is not found. For these rule matches the
entity
subfields will be present.
file_filter
: A file filter rule. classification A classification rule. fingerprint A fingerprint rule. For these rule matches the
fingerprint
subfields will be present.
fingerprint_group
:
A fingerprint 2.0 group rule. For these rule matches the
fingerprint_group
subfields will be present.
structured_classification
: A structured classification rule. For these rule matches the
structured_classification
subfields will be present.
»»»»» entity
object
false
none
Contains details about the entity rule that matched. This field is present when
type
is
entity
or
not_entity
.
»»»»»» weighted
boolean
true
none
If
true
this rule is using the weighted
score
to determine the severity. If
false
,
count
is being used.
»»»»»» score
integer
true
none
The weighted score of the rule matches.
»»»»»» limit_reached
boolean
true
none
If
true
the maximum number of matches for this rule was reached. This means that some identified data was omitted from the results.
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»»» entity
string
true
none
The name of the entity that resulted in a match.
»»»»»»» count
integer
true
none
The number of times the given
entity
was matched.
»»»»»»» data_type
false
none
General data type describing this entity.
»»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of not_sensitive low medium high critical
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of not_sensitive low medium high critical
»»»»»» unique_count
integer
false
none
The number of unique entries that matched the rule. This field is only present when the profile specifies that rules should be uniquely counted.
»»»»» structured_classification
object
false
none
Details of a matched classification type rule
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of not_sensitive low medium high critical
»»»»»» data_type
false
none
General data type describing this entity.
»»»»» fingerprint
object
false
none
This field is present when
type
is
fingerprint
.
»»»»»» classification
string
true
none
The classification that matched.
»»»»»» match
string
true
none
The file that matched.
»»»»»» score
integer
true
none
The score of the matched finterprint.
»»»»» fingerprint_group
object
false
none
This field is present when
type
is
fingerprint_group
.
»»»»»» match
string
true
none
The fingerprinted file that matched.
»»»»»» score
integer
true
none
The similarity score of matched fingerprinted file.
»»» forensics
object
false
none
none
»»»» extracted_text
string(string)
false
none
String identifier used to correlate the extracted text with its corresponding part in the multipart response
»»»» entity_rule_matches
string(string)
false
none
String identifier used to correlate the entity rule matches with its corresponding part in the multipart response.
»»»» preview_image
string(string)
false
none
String identifier used to correlate the preview image with its corresponding part in the multipart response.
»»»» original_subfile
string(string)
false
none
String identifier used to correlate the original subfile with its corresponding part in the multipart response.
Enumerated Values
Property
Value
InspectionStatus: status
success
timeout
error
verdict
hit
no_hit
verdict_type
full
partial
severity
none
low
medium
high
critical
MicrosoftAipProtectionStatus: status
protected
unsanctioned
sanctioned
severity
none
low
medium
high
critical
type
entity
not_entity
file_filter
classification
fingerprint
fingerprint_group
structured_classification
sensitivity_level
not_sensitive
low
medium
high
critical
This operation does not require authentication
In this Topic
Get Results of Prior DLP Inspection

---
## Perform DLP Content Inspection and Retrieve Results (Synchronous)
**URL:** https://docs.netskope.com/en/starting-a-synchronous-dlp-content-inspection-job/
**Last Modified:** 2026-06-25T19:16:08+00:00
**Scraped:** 2026-08-23T07:13:42.514048+00:00

Perform DLP Content Inspection and Retrieve Results (Synchronous) - Netskope Technical Documentation
Perform DLP Content Inspection and Retrieve Results (Synchronous)
This API endpoint is used to synchronously perform a DLP Content Inspection and retrieve the results. If the content inspection exceeds the maximum timeout of 10 seconds, a HTTP 200 is returned with the status field set to ‘timeout’. This call only supports the following verdict types:
summary
and
details
.
This endpoint has some additional limitations:
Max File Size
: 1 megabyte
Timeout
: 10 seconds
Max DLP Profiles
: 100
Character Length of Each Profile name:
256 characters
Request Endpoint
POST
https://<appliance_ip>/inspections
Call Example
curl -X 'POST' \
  'https://10.0.0.1/inspections' \
  -H 'accept: multipart/mixed' \
  -H 'Content-Type: multipart/form-data' \
  -H 'x-netskope-generate-incidents: true' \
  -F 'request={"profiles":["DLP-PCI","DLP-PII"],"content":{"id":"b1f793e4d4a26ac7b695bb1fd1fb0ce3cb5d729c401d8528f8bb92598006cf85","name":"SecretFile.txt","object_id":"AA-74GXZ","true_file_type":230},"modules":{"file_filter":{"skip":true},"drm":{"labels":[{"id":"c7d03ebd-804d-489c-94c6-8167224c3c1b","name":"chris_encryption_all_enabled","instance":"epdlpsjc1","vendor":"mip"}]}},"results":{"verdict":"summary"},"sender":{"app_name":"AWS_RDS"}}' \
  -F 'content=@dlp.txt;type=text/plain'
Response Example
#200 Example
Indicates a successful response, and the results are provided in multiple multipart/mixed parts.
The request header
x-netskope-generate-incidents
is added so that users can specify their choice for generating alerts & incidents.
The response headers have also been created:
x-netskope-incidents-posted
. The response header reflect whether the alerts and incidents were posted to the management plane.
Valid Query Parameters:
Parameters
Name
In
Type
Required
Description
body
body
object
true
none
» request
body
object
true
Specifies the properties of an synchronous inspection request.
»» profiles
body
true
A list of profiles to use during the scan. Profiles determine which DLP rules are used when searching for matches.
»» content
body
true
Describes the content that is being sent to DLP as part of the request.
»»» id
body
string
true
SHA256 hash of the content that has been sent.
»»» name
body
string
false
The name (e.g. filename) of the data.
»»» object_id
body
string
false
An object identifier for the data.
»»» true_file_type
body
integer
false
Netskope true file type (numerical ID)
»» modules
body
false
Specifies settings for individual DLP modules that will be used during the inspection.
»»» file_filter
body
object
false
Specifies settings for the File Filter module.
»»»» skip
body
boolean
false
If true file filtering will be skipped.
»»» drm
body
object
false
Allows for explicit DRM labels to be passed into DLP.
»»»» labels
body
[object]
true
none
»»»»» id
body
string
true
The id of the label.
»»»»» name
body
string
false
The name of the label.
»»»»» instance
body
string
false
The instance of the label.
»»»»» vendor
body
string
true
The vendor of the label.
»» results
body
object
false
Specifies properties for the DLP On Demand results returned from the inspection.
»»» verdict
body
string
false
Specifies how much match detail should be returned. One of the following will be returned:
summary
– Summary of the verdict is returned. This will include the outcome, verdict type, list of the profiles, severity.
details
– Includes match details. Details about verdict has result matches, profile and rules per file.
forensics
– Includes summary, details and forensics of the matches. All match details including rule information, matched text and extracted content will be returned. Please note that this will cause a full scan of the file. If no
verdict
is specified, it would default to summary type and the summary of the verdict will be returned.
»» sender
body
false
Describes the request caller.
»»» app_name
body
string
true
Application that triggered the call
» content
body
string(binary)
true
none
Enumerated Values
Parameter
Value
»»» verdict
summary
details
Responses
Status
Meaning
Description
Schema
200
OK
Indicates a successful response, and the results are provided in multiple multipart/mixed parts.
Inline
400
Bad Request
The request was invalid. The response contains the error that caused the request to be rejected, if available.
string
413
Payload Too Large
The specified content is too large to be scanned.
None
500
Internal Server Error
An error occurred while performing the request. The response contains the error that caused the request to be rejected, if available.
string
503
Service Unavailable
No resources are available to perform the request.
None
Response Schema
Status Code
200
Name
Type
Required
Restrictions
Description
» result_data
false
none
Contains the overall result of the inspection. This includes the status of the inspection and any matches produced as a result of the inspection.
»» status
true
none
Specifies the status of a scan request.
success
– The content was inspected successfully.
timeout
– The content inspection took too long and was timed out.
error
– An error occurred while performing the content inspection.
»» status_info
string
false
none
Additional information about the status. For example, if
status
is
error
, this field may be present to provide details about the error that occurred.
»» summary
false
none
none
»»» verdict
string
true
none
The verdict. One of:
hit
no_hit
»»» verdict_type
string
true
none
The verdict type. One of:
full
partial
»»» severity
string
false
none
The severity of the rule. One of:
none
low
medium
high
critical
»»» profiles
true
none
A list of profiles to use during the scan. Profiles determine which DLP rules are used when searching for matches.
»»» transaction_id
string
true
none
The transaction ID for this match.
»» results
[object]
false
none
When a scan completes successfully (
status
is
success
) this field may be present. It contains an array of entries – one for each file/subfile in the content that was scanned. Only files/subfiles that had rule matches or could not be scanned because they were protected will show up here. Files that were scanned but did not meet one of these two conditions do not appear here.
»»» bypassed_profiles
[string]
false
none
Specifies the list of profiles from the request that were bypassed because the file being scanned was protected in some way. If this field is not present, no profiles were bypassed.
»»» metadata
object
true
none
Metadata about the inspected content.
»»»» subfile
boolean
true
none
If a container file is passed to DLP, the subfiles within it are also scanned. If this field is
true
the match is for a subfile. If this field is false, either the content passed to DLP was not a container or the match was on the container itself.
»»»» file_id
integer
false
none
The internal identifier of the file/subfile.
»»»» name
string
false
none
The name (e.g. file name), if any, of the inspected content.
»»»» size
integer(uint64)
false
none
The size in bytes of the file/subfile.
»»»» sha256
string
false
none
The SHA256 hash of the inspected content.
»»»» language
string
false
none
The detected language of the inspected content.
»»»» type
string
false
none
The detected type of the inspected content.
»»»» category
string
false
none
The detected category of the inspected content.
»»»» mime_type
string
false
none
The MIME type of the inspected content.
»»»» protection
object
false
none
The field is present when the content is protected in some way. The protection may include one or both of
encryption
and
microsoft_aip
.
»»»»» encryption
object
false
none
The content is encrypted. No match data can be produced for encrypted content.
»»»»»» file_typing
boolean
false
none
Encrypted content detected with file typing.
»»»»»» classification
boolean
false
none
Encrypted content detected with classification.
»»»»»» classification_score
number(double)
false
none
The score of encrypted content detected with classification.
»»»»» microsoft_aip
object
false
none
The content is Microsoft AIP protected. If the content can be unprotected, it will be inspected and match data may be produced. If it cannot be unprotected match data cannot be produced.
»»»»»» status
string
true
none
The Microsoft AIP protection status:
protected
: The content could not be unprotected, and was not inspected.
unsanctioned
: The content was AIP protected outside of a known MIP infrastructure and therefore could not be unprotected and was not inspected.
sanctioned
: The content was AIP protected by a known MIP infrastructure. Such content may be uprotected and scanned. It also may have DRM labels extracted.
»»»» drm
object
false
none
The content is protected by a DRM system.
»»»»» labels
[object]
true
none
An array of DRM label objects that contain detailed DRM label information.
»»»»»» id
string
true
none
The id of the label.
»»»»»» name
string
true
none
The name of the label.
»»»»»» instance
string
true
none
The instance of the label.
»»»»»» vendor
string
true
none
The vendor of the label.
»»»»»» data_classification_label
string
true
none
The data classification label.
»»» matches
[object]
false
none
An array of match entry objects that contain detailed DLP match information.
»»»» id
string
false
none
The match identifier. If this is a
cached
match, this will be set to the
id
of the previous match. Otherwise this field is a new identifier that DLP will use to refer to the match if it is seen in the future. Furthermore, for a non-cached response there will be a corresponding
extracted_text
multipart/mixed part returned for this file and this value will be set in the
name
field of the
Content-Disposition
header for that part.
»»»» cached
boolean
true
none
If
true
, this match was found in the DLP cache, meaning the content has already been scanned for this profile and thus was not scanned as part of this request.
id
is set to the
id
that was created when the content was scanned. Because of this, there will be no
forensics
associated with the match as forensic data is not stored in the DLP cache.
»»»» profile
any
true
none
none
allOf
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
false
none
The name of the profile.
and
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
any
false
none
The profile to which the matched
rules
are attached.
continued
Name
Type
Required
Restrictions
Description
»»»» action_threshold_met
boolean
true
none
If
true
, the action threshold was met indicating that the DLP Client should perform the action associated with this profile. If this field is
false
the action threshold was not met and the action associated with this profile should not be performed.
»»»» maximum_severity
string
false
none
The maximum severity of the matched rules.
»»»» rules
[object]
false
none
none
»»»»» name
string
true
none
The name of the rule.
»»»»» severity
string
true
none
The severity of the rule:
none
,
low
,
medium
,
high
, or
critical
»»»»» type
string
true
none
The type of the rule. One of:
entity
: A rule that matches when a specific entity is found. For these rule matches the
entity
subfields will be present.
not_entity
: A rule that matches when a specific entity is not found. For these rule matches the
entity
subfields will be present.
file_filter
: A file filter rule. classification A classification rule. fingerprint A fingerprint rule. For these rule matches the
fingerprint
subfields will be present.
fingerprint_group
:
A fingerprint 2.0 group rule. For these rule matches the
fingerprint_group
subfields will be present.
structured_classification
: A structured classification rule. For these rule matches the
structured_classification
subfields will be present.
»»»»» entity
object
false
none
Contains details about the entity rule that matched. This field is present when
type
is
entity
or
not_entity
.
»»»»»» weighted
boolean
true
none
If
true
this rule is using the weighted
score
to determine the severity. If
false
,
count
is being used.
»»»»»» score
integer
true
none
The weighted score of the rule matches.
»»»»»» limit_reached
boolean
true
none
If
true
the maximum number of matches for this rule was reached. This means that some identified data was omitted from the results.
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»»» entity
string
true
none
The name of the entity that resulted in a match.
»»»»»»» count
integer
true
none
The number of times the given
entity
was matched.
»»»»»»» data_type
string
false
none
General data type describing this entity.
»»»»»»» sensitivity_level
string
true
none
How sensitive of a match is this entity. One of not_sensitive low medium high critical
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of:
not_sensitive
low
medium
high
critical
»»»»»» unique_count
integer
false
none
The number of unique entries that matched the rule. This field is only present when the profile specifies that rules should be uniquely counted.
»»»»» structured_classification
object
false
none
Details of a matched classification type rule
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
How sensitive of a match is this entity. One of not_sensitive low medium high critical
»»»»»» data_type
false
none
General data type describing this entity.
»»»»» fingerprint
object
false
none
This field is present when
type
is
fingerprint
.
»»»»»» classification
string
true
none
The classification that matched.
»»»»»» match
string
true
none
The file that matched.
»»»»»» score
integer
true
none
The score of the matched finterprint.
»»»»» fingerprint_group
object
false
none
This field is present when
type
is
fingerprint_group
.
»»»»»» match
string
true
none
The fingerprinted file that matched.
»»»»»» score
integer
true
none
The similarity score of matched fingerprinted file.
»»» forensics
object
false
none
none
»»»» extracted_text
string(string)
false
none
String identifier used to correlate the extracted text with its corresponding part in the multipart response
»»»» entity_rule_matches
string(string)
false
none
String identifier used to correlate the entity rule matches with its corresponding part in the multipart response.
»»»» preview_image
string(string)
false
none
String identifier used to correlate the preview image with its corresponding part in the multipart response.
»»»» original_subfile
string(string)
false
none
String identifier used to correlate the original subfile with its corresponding part in the multipart response.
Enumerated Values
Property
Value
InspectionStatus: status
success
timeout
error
verdict
hit
no_hit
verdict_type
full
partial
severity
none
low
medium
high
critical
MicrosoftAipProtectionStatus: status
protected
unsanctioned
sanctioned
severity
none
low
medium
high
critical
type
entity
not_entity
file_filter
classification
fingerprint
fingerprint_group
structured_classification
sensitivity_level
not_sensitive
low
medium
high
critical
This operation does not require authentication
In this Topic
Perform DLP Content Inspection and Retrieve Results (Synchronous)

---
## Sending Data to DLP On Demand
**URL:** https://docs.netskope.com/en/dlp-on-demand-usage/
**Last Modified:** 2026-06-25T19:18:16+00:00
**Scraped:** 2026-08-23T07:13:43.684367+00:00

Sending Data to DLP On Demand - Netskope Technical Documentation
Sending Data to DLP On Demand
When setting
x-netskope-generate-incidents
to true &
verdict as “forensics”
, the response
will not include
forensics. However, the incidents posted to the management plane should contain forensics.
This limitation will be addressed in later releases.
You can send data to the REST API to start a DLP content inspection job for Unstructured Data or a Column Classification job for Structured Data. There are other calls as well.
You can get more information about these API calls from the
DLP On Demand API page
.
Below are some examples of sending Data to DLP On Demand.
Starting an asynchronous DLP Inspection Job from the appliance
Send a
POST
to the
/inspections/jobs/
endpoint. The request returns a
job_id
that is used to get the results of the request. The API may respond with a result if the result is already cached.
curl -X 'POST' \
  'https://10.0.0.1/inspections/jobs' \
  -H 'accept: multipart/form-data' \
  -H 'Content-Type: multipart/form-data' \
  -F 'request={"profiles":["DLP-PCI","DLP-PII"],"content":{"id":"b1f793e4d4a26ac7b695bb1fd1fb0ce3cb5d729c401d8528f8bb92598006cf85","name":"SecretFile.txt","object_id":"AA-74GXZ","true_file_type":230},"modules":{"file_filter":{"skip":true},"drm":{"labels":[{"id":"c7d03ebd-804d-489c-94c6-8167224c3c1b","name":"chris_encryption_all_enabled","instance":"epdlpsjc1","vendor":"mip"}]}},"results":{"verdict":"summary"},"sender":{"app_name":"AWS_RDS"}}' \
  -F 'content=@image.jpg;type=image/jpeg'
You’ll receive a .json formatted job_id to retrieve the results at a later time.
{
  "job_id": "7e548ccf-c96e-4f5f-9f9e-4a468776972e"
}
Getting the results of an asynchronous DLP Inspection Job from the appliance
Send a
GET
to
/inspections/jobs/<job_id>
endpoint using the
job_id
obtained from the previous use-case.
curl -X 'GET' \
  'https://10.0.0.1/inspections/jobs/7e548ccf-c96e-4f5f-9f9e-4a468776972e' \
  -H 'accept: multipart/mixed'
You will get the associated DLP Incident info provided as a multi-part response showing the entity match for the offending content, the extracted text, and other forensic details.
Checking Incidents in the UI
Under
Incidents > DLP
, use
Advanced Filters
like
access_method like 'DLP On Demand'
In this Topic
Sending Data to DLP On Demand

---
## Retrieve Results from a Submitted Asynchronous DLP Content Inspection job
**URL:** https://docs.netskope.com/en/retrieve-result-from-dlp-content-inspection-job/
**Last Modified:** 2026-06-25T19:16:09+00:00
**Scraped:** 2026-08-23T07:13:44.884071+00:00

Retrieve Results from a Submitted Asynchronous DLP Content Inspection job - Netskope Technical Documentation
Retrieve Results from a Submitted Asynchronous DLP Content Inspection job
Retrieve the results of a previously submitted DLP content inspection job using the obtained job-id. This endpoint will be used to retrieve the results for both
structured
and
unstructured
jobs. This endpoint
must be polled continuously
for a result. Adhere to following restrictions:
Minimum Polling frequency:
If the file size is less than 1MB, polling should occur at most once every 100 milliseconds.
If the file size is greater than 1MB, polling should occur at most once every 5 seconds.
Maximum Polling frequency:
The maximum polling interval should be 299 seconds.
Maximum Wait Time: If more than 36 minutes elapses from the time the asynchronous inspection request was submitted, the cache entry would be cleared and a new inspection request will be required.
Request Endpoint
GET
https://<appliance_ip>/inspections/jobs/<job-id>
Call Example
curl -X 'GET' \
  'https://10.0.0.1/inspections/jobs/7e548ccf-c96e-4f5f-9f9e-4a468776972e' \
  -H 'accept: multipart/mixed' \
  -H 'x-netskope-generate-incidents: true'
Response Example
Retrieving Inspection Results (425 Too Early Error)
Once an asynchronously inspection request is submitted, the service return the associated JobId and begins processing the job in background. DLP processing takes some time depends on number of profiles and file size in the request. When client requests for the inspection result and if result is not available, service responds with HTTP 425 status code.
#200 Response
The request was successfully completed, and the results are provided in multiple multipart/mixed parts. The first part contains the inspection result in JSON format. Subsequent parts include forensic data for each inspection result, shared in binary format. This forensic data may include extracted text, entity rule matches, preview images, and/or original subfiles. Each forensic part is identified by a name that maps to a corresponding forensic entry in the inspection result.
HTTP/1.1 200 OK
Date: Wed, 27 Aug 2025 15:31:51 GMT
Content-Type: multipart/mixed; boundary=ded37e13d22bcff5fb0ddeb9547185cca478dbfe6b1847a7e6f4e758d043
Transfer-Encoding: chunked
Connection: keep-alive
--ded37e13d22bcff5fb0ddeb9547185cca478dbfe6b1847a7e6f4e758d043
Content-Disposition: form-data; name="result_data"
Content-Type: application/json
{"results":[{"forensics":{"entity_rule_matches":"erm_580078163378984695","extracted_text":"et_580078163378984695"},"matches":[{"action_threshold_met":true,"cached":false,"id":"580078163378984695","maximum_severity":"high","profile":"DLP_MASK","rules":[{"entity":{"entities_summary":[{"count":1,"entity":"Name_mask"}],"limit_reached":false,"matches_count":1,"score":8,"weighted":true},"name":"ccn_or_name_masking","severity":"high","type":"entity"}]}],"metadata":{"category":"Text","language":"ENGLISH","mime_type":"text/plain","name":"mask.txt","sha256":"cea5d77c801bb3a91233334344b472e437e467cc745d20d1e4d60f73d3e6818e","size":222,"subfile":false,"type":"Plain Text file"}}],"status":"success","summary":{"profiles":["DLP_MASK"],"severity":"high","transaction_id":"2219920255353353236","verdict":"hit","verdict_type":"full"}}
--ded37e13d22bcff5fb0ddeb9547185cca478dbfe6b1847a7e6f4e758d043
Content-Disposition: form-data; name="erm_580078163378984695"
Content-Type: application/octet-stream
[{"matches":[[{"end_offset":118,"entity":"Name_mask","prefix":"2. ","score":3,"start_offset":109,"suffix":"@company.com: ","text":"XXXX.XXXXX","type":"content"}]],"profile":"DLP_MASK","rule":"ccn_or_name_masking"}]
--ded37e13d22bcff5fb0ddeb9547185cca478dbfe6b1847a7e6f4e758d043
Content-Disposition: form-data; name="et_580078163378984695"
Content-Type: application/octet-stream
Please reorder this list of users in alphabetical order by last name:
1. john.doe@company.com: admin2024
2. XXXX.XXXXX@company.com: ccninfo
The request header
x-netskope-generate-incidents
is added so that users can specify their choice for generating alerts & incidents.
The response headers have also been created:
x-netskope-incidents-posted
. The response header reflect whether the alerts and incidents were posted to the management plane.
Valid Query Parameters are:
Name
In
Type
Required
Description
job_id
path
string
true
The job ID returned from the asynchronous inspection request.
Responses
Status
Meaning
Description
Schema
200
OK
The request was successfully completed, and the results are provided in multiple multipart/mixed parts. The first part contains the inspection result in JSON format. Subsequent parts include forensic data for each inspection result
if requested previously
, shared in binary format. This forensic data may include extracted text, entity rule matches, preview images, and/or original subfiles. Each forensic part is identified by a name that maps to a corresponding forensic entry in the inspection result. Forensics data will not show if the original request did not explicitly ask for forensics.
Inline
400
Bad Request
The request was invalid. The response contains the error that caused the request to be rejected, if available.
string
404
Not Found
The requested job-id was not found.
string
425
Unknown
The inspection is still in progress and the final results are not yet available.
Action Required:
Wait and Retry. The client must poll the results endpoint until a successful response (e.g., 200 OK) is received.
Polling for result:
To efficiently retrieve the result without overloading the system, the client must poll the result endpoint.
Minimum Polling frequency:
If file_size <= 1MB, polling should be >=100ms
If file_size > 1MB, polling can be >=5 sec
Maximum Polling frequency:
The maximum polling interval should be 299 seconds.
Maximum Wait Time: If more than 36 minutes elapses from the time the asynchronous inspection request was submitted, the cache entry would be cleared and a new inspection request will be required.
None
500
Internal Server Error
An error occurred while getting the result. The response contains the error that caused the request to be rejected, if available.
string
503
Service Unavailable
No resources are available to performing the request.
None
Response Schema
Status Code
200
Name
Type
Required
Restrictions
Description
» result_data
false
none
Contains the overall result of the inspection. This includes the status of the inspection and any matches produced as a result of the inspection.
»» status
true
none
Specifies the status of a scan request. success – The content was inspected successfully. timeout – The content inspection took too long and was timed out. error – An error occurred while performing the content inspection.
»» status_info
string
false
none
Additional information about the status. For example, if
status
is
error
, this field may be present to provide details about the error that occurred.
»» summary
false
none
none
»»» verdict
string
true
none
The verdict:
hit
or
no_hit
»»» verdict_type
string
true
none
The verdict type:
full
or
partial
»»» severity
string
false
none
The severity of the rule:
none
,
low
,
medium
,
high
, or
critical
»»» profiles
true
none
A list of profiles to use during the scan. Profiles determine which DLP rules are used when searching for matches.
»»» transaction_id
string
true
none
The transaction ID for this match.
»» results
[object]
false
none
When a scan completes successfully (
status
is
success
) this field may be present. It contains an array of entries – one for each file/subfile in the content that was scanned. Only files/subfiles that had rule matches or could not be scanned because they were protected will show up here. Files that were scanned but did not meet one of these two conditions do not appear here.
»»» bypassed_profiles
[string]
false
none
Specifies the list of profiles from the request that were bypassed because the file being scanned was protected in some way. If this field is not present, no profiles were bypassed.
»»» metadata
object
true
none
Metadata about the inspected content.
»»»» subfile
boolean
true
none
If a container file is passed to DLP, the subfiles within it are also scanned. If this field is
true
the match is for a subfile. If this field is false, either the content passed to DLP was not a container or the match was on the container itself.
»»»» file_id
integer
false
none
The internal identifier of the file/subfile.
»»»» name
string
false
none
The name (e.g. file name), if any, of the inspected content.
»»»» size
integer(uint64)
false
none
The size in bytes of the file/subfile.
»»»» sha256
string
false
none
The SHA256 hash of the inspected content.
»»»» language
string
false
none
The detected language of the inspected content.
»»»» type
string
false
none
The detected type of the inspected content.
»»»» category
string
false
none
The detected category of the inspected content.
»»»» mime_type
string
false
none
The MIME type of the inspected content.
»»»» protection
object
false
none
The field is present when the content is protected in some way. The protection may include one or both of
encryption
and
microsoft_aip
.
»»»»» encryption
object
false
none
The content is encrypted. No match data can be produced for encrypted content.
»»»»»» file_typing
boolean
false
none
Encrypted content detected with file typing.
»»»»»» classification
boolean
false
none
Encrypted content detected with classification.
»»»»»» classification_score
number(double)
false
none
The score of encrypted content detected with classification.
»»»»» microsoft_aip
object
false
none
The content is Microsoft AIP protected. If the content can be unprotected it will be inspected and match data may be produced. If it cannot be unprotected match data cannot be produced.
»»»»»» status
string
true
none
The Microsoft AIP protection status:
protected
: The content could not be unprotected, and was not inspected.
unsanctioned
: The content was AIP protected outside of a known MIP infrastructure and therefore could not be unprotected and was not inspected.
sanctioned
: The content was AIP protected by a known MIP infrastructure. Such content may be uprotected and scanned. It also may have DRM labels extracted.
»»»» drm
object
false
none
The content is protected by a DRM system.
»»»»» labels
[object]
true
none
An array of DRM label objects that contain detailed DRM label information.
»»»»»» id
string
true
none
The id of the label.
»»»»»» name
string
true
none
The name of the label.
»»»»»» instance
string
true
none
The instance of the label.
»»»»»» vendor
string
true
none
The vendor of the label.
»»»»»» data_classification_label
string
true
none
The data classification label.
»»» matches
[object]
false
none
An array of match entry objects that contain detailed DLP match information.
»»»» id
string
false
none
The match identifier. If this is a
cached
match, this will be set to the
id
of the previous match. Otherwise this field is a new identifier that DLP will use to refer to the match if it is seen in the future. Furthermore, for a non-cached response there will be a corresponding
extracted_text
multipart/mixed part returned for this file and this value will be set in the
name
field of the
Content-Disposition
header for that part.
»»»» cached
boolean
true
none
If
true
this match was found in the DLP cache, meaning the content has already been scanned for this profile and thus was not scanned as part of this request.
id
is set to the
id
that was created when the content was scanned. Because of this, there will be no
forensics
associated with the match as forensic data is not stored in the DLP cache.
»»»» profile
any
true
none
none
allOf
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
false
none
The name of the profile.
and
Name
Type
Required
Restrictions
Description
»»»»»
anonymous
any
false
none
The profile to which the matched
rules
are attached.
continued
Name
Type
Required
Restrictions
Description
»»»» action_threshold_met
boolean
true
none
If
true
, the action threshold was met indicating that the DLP Client should perform the action associated with this profile. If this field is
false
the action threshold was not met and the action associated with this profile should not be performed.
»»»» maximum_severity
string
false
none
The maximum severity of the matched rules.
»»»» rules
[object]
false
none
none
»»»»» name
string
true
none
The name of the rule.
»»»»» severity
string
true
none
The severity of the rule. One of: none, low medium, high, critical
»»»»» type
string
true
none
The type of the rule. One of:
entity
: A rule that matches when a specific entity is found. For these rule matches the
entity
subfields will be present.
not_entity
: A rule that matches when a specific entity is not found. For these rule matches the
entity
subfields will be present.
file_filter
: A file filter rule. classification A classification rule. fingerprint A fingerprint rule. For these rule matches the
fingerprint
subfields will be present.
fingerprint_group
:
A fingerprint 2.0 group rule. For these rule matches the
fingerprint_group
subfields will be present.
structured_classification
: A structured classification rule. For these rule matches the
structured_classification
subfields will be present.
»»»»» entity
object
false
none
Contains details about the entity rule that matched. This field is present when
type
is
entity
or
not_entity
.
»»»»»» weighted
boolean
true
none
If
true
this rule is using the weighted
score
to determine the severity. If
false
,
count
is being used.
»»»»»» score
integer
true
none
The weighted score of the rule matches.
»»»»»» limit_reached
boolean
true
none
If
true
the maximum number of matches for this rule was reached. This means that some identified data was omitted from the results.
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»»» entity
string
true
none
The name of the entity that resulted in a match.
»»»»»»» count
integer
true
none
The number of times the given
entity
was matched.
»»»»»»» data_type
false
none
General data type describing this entity.
»»»»»»» sensitivity_level
true
none
The sensitivity level of the rule hit. One of:
not_sensitive
low
medium
high
critical
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
The sensitivity level of the rule hit. One of:
not_sensitive
low
medium
high
critical
»»»»»» unique_count
integer
false
none
The number of unique entries that matched the rule. This field is only present when the profile specifies that rules should be uniquely counted.
»»»»» structured_classification
object
false
none
Details of a matched classification type rule
»»»»»» entities_summary
true
none
An array of the matched entities and the corresponding counts for those entities.
»»»»»» matches_count
integer
true
none
The count of entity rule matches.
»»»»»» sensitivity_level
true
none
The sensitivity level of the rule hit. One of:
not_sensitive
low
medium
high
critical
»»»»»» data_type
false
none
General data type describing this entity.
»»»»» fingerprint
object
false
none
This field is present when
type
is
fingerprint
.
»»»»»» classification
string
true
none
The classification that matched.
»»»»»» match
string
true
none
The file that matched.
»»»»»» score
integer
true
none
The score of the matched finterprint.
»»»»» fingerprint_group
object
false
none
This field is present when
type
is
fingerprint_group
.
»»»»»» match
string
true
none
The fingerprinted file that matched.
»»»»»» score
integer
true
none
The similarity score of matched fingerprinted file.
»»» forensics
object
false
none
none
»»»» extracted_text
string(string)
false
none
String identifier used to correlate the extracted text with its corresponding part in the multipart response
»»»» entity_rule_matches
string(string)
false
none
String identifier used to correlate the entity rule matches with its corresponding part in the multipart response.
»»»» preview_image
string(string)
false
none
String identifier used to correlate the preview image with its corresponding part in the multipart response.
»»»» original_subfile
string(string)
false
none
String identifier used to correlate the original subfile with its corresponding part in the multipart response.
Enumerated Values
Property
Value
InspectionStatus: status
success
timeout
error
verdict
hit
no_hit
verdict_type
full
partial
severity
none
low
medium
high
critical
MicrosoftAipProtectionStatus: status
protected
unsanctioned
sanctioned
severity
none
low
medium
high
critical
type
entity
not_entity
file_filter
classification
fingerprint
fingerprint_group
structured_classification
sensitivity_level
not_sensitive
low
medium
high
critical
This operation does not require authentication
In this Topic
Retrieve Results from a Submitted Asynchronous DLP Content Inspection job

---
## Appliance Troubleshooting
**URL:** https://docs.netskope.com/en/dlpondemandtroubleshooting/
**Last Modified:** 2026-06-25T19:19:33+00:00
**Scraped:** 2026-08-23T07:13:58.168441+00:00

Appliance Troubleshooting - Netskope Technical Documentation
Appliance Troubleshooting
The Appliance CLI comes with troubleshooting commands to help examine logs in order to debug the system.
Create and Share the Debug Package
To create and share the debug package:
Generate the debug package:
nsappliance> troubleshooting debug-package generate include-coredumps true
Upload to netskope via http(s):
nsappliance> troubleshooting debug-package upload
SCP to another system to provide to Netskope
nsappliance> scp export debug-package to host <HOST> path <PATH> user <USER>
Common Problems
Avoid any traffic decryption: If you are using a network device (i.e. proxy) ensure that the appliance is not subject to SSL interception to avoid issues with tethering or ongoing operations.
Appliance Not Ready
"{"error": "Precondition Required: Appliance is not ready", "code": 428 }"
If this error pops up, there are a variety of reasons:
The appliance is not tethered
The appliance is not fully initialized
The appliance system requirements were not adhered to
API token missing
Troubleshooting Command Reference
Check the
Troubleshooting section of Appliance CLI
.
In this Topic
Appliance Troubleshooting

---
## DLP On Demand Appliance
**URL:** https://docs.netskope.com/en/dlp-on-demand-appliance/
**Last Modified:** 2026-06-25T19:18:15+00:00
**Scraped:** 2026-08-23T07:14:02.847803+00:00

DLP On Demand Appliance - Netskope Technical Documentation
DLP On Demand Appliance
DLP on Demand appliances must be tethered to the Netskope management plane to retrieve their configuration before becoming operational. A customer can deploy multiple appliances as needed for scalability or redundancy.
Appliance Setup
Manage DLP On Demand
Removing the Appliance
Configure Certificates
Appliance Upgrade
Appliance CLI
Appliance Troubleshooting
In this Topic
DLP On Demand Appliance

---
## Manage DLP On Demand
**URL:** https://docs.netskope.com/en/manage-dlp-on-demand/
**Last Modified:** 2026-06-25T19:19:29+00:00
**Scraped:** 2026-08-23T07:14:08.816874+00:00

Manage DLP On Demand - Netskope Technical Documentation
Manage DLP On Demand
To begin managing DLP On Demand, navigate to
Settings > Security Cloud Platform > On-Premises Infrastructure
.
You can can get the
License Key
required for the appliance setup:
You can see and manage your tethered DLP On Demand appliances and obtain new installation images by clicking
SETUP DLP ON DEMAND
.
DLP On Demand is taking advantage of REST API v1 to obtain data synced with the appliance therefore ensure that you have created a REST API V1 token via
Settings >Tools > REST API v1
In this Topic
Manage DLP On Demand

---
## DLP Detection
**URL:** https://docs.netskope.com/en/dlp-detection/
**Last Modified:** 2026-06-25T17:36:58+00:00
**Scraped:** 2026-08-23T07:14:38.312639+00:00

DLP Detection - Netskope Technical Documentation
DLP Detection
For more information on DLP Detection, see the following pages:
Steganographic Detection
Advanced Content Scanning
Advanced Data Trickling
Fingerprinting
DLP Rules
File Classifiers
OCR
Supported File Types for Detection
Supported File Types for Content Inspection
In this Topic
DLP Detection

---
## Netskope One for Microsoft Purview DLP Supported Activities
**URL:** https://docs.netskope.com/en/netskope-one-for-microsoft-purview-dlp-supported-activities/
**Last Modified:** 2026-06-25T19:18:20+00:00
**Scraped:** 2026-08-23T07:14:49.132326+00:00

Netskope One for Microsoft Purview DLP Supported Activities - Netskope Technical Documentation
Netskope One for Microsoft Purview DLP Supported Activities
The following is a list of supported activities by Netskope for Microsoft Purview DLP. These activities are aligned with the DLP activities of Netskope.
Netskope Activities
Purview Activities
api post
UPLOAD_TEXT
add
UPLOAD_TEXT
comment
UPLOAD_TEXT
create
UPLOAD_TEXT
edit
UPLOAD_TEXT
formpost
UPLOAD_TEXT
formshare
UPLOAD_TEXT
post
UPLOAD_TEXT
preview
UPLOAD_TEXT
print
UPLOAD_TEXT
publish
UPLOAD_TEXT
rename
UPLOAD_TEXT
resume
UPLOAD_TEXT
save
UPLOAD_TEXT
search
UPLOAD_TEXT
send
UPLOAD_TEXT
start
UPLOAD_TEXT
submit
UPLOAD_TEXT
translate
UPLOAD_TEXT
attach
UPLOAD_FILE
delete
UPLOAD_FILE
upload
UPLOAD_FILE
uploadandsend
UPLOAD_FILE
copy
DOWNLOAD_TEXT
download
DOWNLOAD_FILE
downloadall
DOWNLOAD_FILE
downloadinstaller
DOWNLOAD_FILE
“AI Post”
UPLOAD_TEXT
“AI Response”
DOWNLOAD_TEXT
In this Topic
Netskope One for Microsoft Purview DLP Supported Activities

---
## Configure a DLP Profile on a Netskope Tenant (Beta)
**URL:** https://docs.netskope.com/en/configure-a-dlp-profile-on-netskope-tenant-beta/
**Last Modified:** 2025-11-14T01:30:57+00:00
**Scraped:** 2026-08-23T07:14:55.025482+00:00

Configure a DLP Profile on a Netskope Tenant (Beta) - Netskope Technical Documentation
Configure a DLP Profile on a Netskope Tenant (Beta)
To use the Custom File Classifiers trained on the Netskope Tenant, you can configure a DLP Profile that can then be used in a Real-time Protection policy.
Log in to your Netskope Tenant and go to
Policies > DLP
.
Click
New Profile
.
Select a file profile from the list if required and click
Next
.
In the DLP Rule or File Classifier section, select classifiers that were used in your Custom File Classification Sharing configuration. These custom file classifiers will be present in the Custom Self-Trained File Classifiers section. Click
Next
.
Enter a DLP Profile Name and click
Save
.
To use the created DLP profile, click
Apply Changes
and then
Apply
.
In this Topic
Configure a DLP Profile on a Netskope Tenant (Beta)

---
## Configure a Real-time Protection Policy using the DLP Profile on Netskope Tenant (Beta)
**URL:** https://docs.netskope.com/en/configure-a-real-time-protection-policy-using-the-dlp-profile-on-netskope-tenant-beta/
**Last Modified:** 2025-11-14T02:31:46+00:00
**Scraped:** 2026-08-23T07:14:56.290160+00:00

Configure a Real-time Protection Policy using the DLP Profile on Netskope Tenant (Beta) - Netskope Technical Documentation
Configure a Real-time Protection Policy using the DLP Profile on Netskope Tenant (Beta)
This policy configuration is just an example of how the File Hashes sent from Netskope CE can be utilized for Real Time Protection. Modify as appropriate for your organization and use-case.
Go to Policies > Real-time Protection.
Click New Policy and then select DLP.
For Source, leave the default as User = All Users.
Fill out the destination information. Click on Category dropdown and select “Cloud App”.
Click on Cloud App dropdown, search and select “Google Drive”.
Click outside of this list to close the search dialog.
Click on Activities and select “Upload” and “Download”.
Click outside of this list to close the search dialog.
For Profile and Action, click on Action and select “Block”.
Keep Template as default.
Click on Add Profile and select “DLP Profile”.
In the DLP Profile, search and select a profile we created earlier.
Enter Policy Name.
Select “Default” for Group and click on Save
Select position of the policy as on the top and click on Save.
Real-time Protection Policy is created successfully
To use the created Policy click on the “Apply Changes” button, fill comment and save.
In this Topic
Configure a Real-time Protection Policy using the DLP Profile on Netskope Tenant (Beta)

---
## Exact Data Match Plugin (Beta)
**URL:** https://docs.netskope.com/en/exact-data-match-plugin/
**Last Modified:** 2026-03-20T23:52:37+00:00
**Scraped:** 2026-08-23T07:15:31.280108+00:00

Exact Data Match Plugin (Beta) - Netskope Technical Documentation
Exact Data Match Plugin (Beta)
This document explains how to configure the Netskope EDM Plugin v1.0.0 in the Cloud Exchange platform. This plugin is used to push EDM File Hashes generated through a configured EDM plugin to a Netskope Tenant.
This plugin operates in push mode only and is intended solely for use as a destination in data-sharing configurations.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances) that is already configured in Cloud Exchange with permission to generate v2/RBACv3 tokens.
A Netskope Cloud Exchange tenant with the
Tenant plugin
configured and the
Exact Data Match module
enabled.
A supported third-party EDM plugin (like
Microsoft File Share
) configured and available for integration.
Exact Data Match Plugin Scope
This plugin is used to push EDM File Hashes to the Netskope Tenant.
Permissions
Ensure that a V2/V3 Token with the appropriate Role is used when configuring the Netskope Tenant, as it is required for the proper functioning of the Netskope EDM Plugin.
API Endpoint
Method
Permission
/api/v2/events/dataexport/events/alert
GET
Read
/api/v2/services/dlp/edm/file/apply
POST
Read + Write
/api/v2/services/dlp/edm/file/staging
POST
Read + Write
API Details
List of APIs Used
API Endpoint
Method
Permission
/api/v2/events/dataexport/events/alert
GET
Read
/api/v2/services/dlp/edm/file/apply
POST
Read + Write
/api/v2/services/dlp/edm/file/staging
POST
Read + Write
Validate the V2 Token
API Endpoint
:
https://<tenant-url>
/api/v2/events/dataexport/events/alert
Method:
GET
Application Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.0.0
Example API response
{
  "result": [
    {
      "CononicalName": "string",
      "_id": "string",
      "access_method": "string",
      "account_id": "string",
      "account_name": "string",
      "acked": "string",
      "action": "string",
      "activity": "string",
      "alert": "string",
      "alert_id": "string",
      "alert_name": "string",
      "alert_type": "string",
      "app": "string",
      "app_activity": "string",
      "app_session_id": 0,
      "appcategory": "string",
      "appsuite": "string",
      "asset_id": "string",
      "asset_object_id": "string",
      "breach_date": 0,
      "breach_description": "string",
      "breach_id": "string",
      "breach_media_references": "string",
      "breach_score": "string",
      "breach_target_references": "string",
      "browser": "string",
      "browser_session_id": 0,
      "browser_version": "string",
      "bypass_traffic": "string",
      "category": "string",
      "cci": 0,
      "ccl": "string",
      "client_bytes": 0,
      "compliance_standards": [
        "string"
      ],
      "conn_duration": 0,
      "conn_endtime": 0,
      "conn_starttime": 0,
      "connection_id": 0,
      "count": 0,
      "data_type": "string",
      "device": "string",
      "device_classification": "string",
      "dlp_file": "string",
      "dlp_incident_id": 0,
      "dlp_is_unique_count": "string",
      "dlp_mail_parent_id": "string",
      "dlp_parent_id": 0,
      "dlp_profile": "string",
      "dlp_rule": "string",
      "dlp_rule_count": 0,
      "dlp_rule_severity": "string",
      "dlp_unique_count": 0,
      "domain": "string",
      "dst_country": "string",
      "dst_geoip_src": 0,
      "dst_latitude": 0,
      "dst_location": "string",
      "dst_longitude": 0,
      "dst_region": "string",
      "dst_timezone": "string",
      "dst_zipcode": "string",
      "dsthost": "string",
      "dstip": "string",
      "dstport": 0,
      "email_source": "string",
      "event_type": "string",
      "evt_src_chnl": "string",
      "exposure": "string",
      "external_collaborator_count": 0,
      "external_email": 0,
      "file_cls_encrypted": true,
      "file_lang": "string",
      "file_path": "string",
      "file_size": 0,
      "file_type": "string",
      "from_user": "string",
      "fromlogs": "string",
      "hostname": "string",
      "http_transaction_count": 0,
      "iaas_asset_tags": [
        "string"
      ],
      "iaas_remediated": "string",
      "instance": "string",
      "instance_id": "string",
      "internal_collaborator_count": 0,
      "justification_reason": "string",
      "justification_type": "string",
      "last_app": "string",
      "last_country": "string",
      "last_device": "string",
      "last_location": "string",
      "last_region": "string",
      "last_timestamp": 0,
      "log_file_name": "string",
      "malicious": "string",
      "malsite_category": [
        "string"
      ],
      "malsite_country": "string",
      "malsite_id": "string",
      "malsite_ip_host": "string",
      "malsite_latitude": 0,
      "malsite_longitude": 0,
      "malsite_region": "string",
      "managed_app": "string",
      "managementID": "string",
      "matched_username": "string",
      "md5": "string",
      "mime_type": "string",
      "modified": 0,
      "netskope_activity": "string",
      "netskope_pop": "string",
      "notify_template": "string",
      "nsdeviceuid": "string",
      "numbytes": 0,
      "object": "string",
      "object_id": "string",
      "object_type": "string",
      "org": "string",
      "organization_unit": "string",
      "orig_ty": "string",
      "orignal_file_path": "string",
      "os": "string",
      "os_version": "string",
      "other_categories": [
        "string"
      ],
      "outer_doc_type": 0,
      "owner": "string",
      "page": "string",
      "page_site": "string",
      "parent_id": "string",
      "password_type": "string",
      "policy": "string",
      "policy_actions": [
        "string"
      ],
      "policy_id": "string",
      "profile_id": "string",
      "protocol": "string",
      "referer": "string",
      "region_id": "string",
      "region_name": "string",
      "req_cnt": 0,
      "request_id": 0,
      "resource_category": "string",
      "resource_group": "string",
      "resp_cnt": 0,
      "sAMAccountName": "string",
      "sa_profile_id": 0,
      "sa_profile_name": "string",
      "sa_rule_id": "string",
      "sa_rule_name": "string",
      "sa_rule_severity": "string",
      "sanctioned_instance": "string",
      "scan_type": "string",
      "serial": "string",
      "server_bytes": 0,
      "sessionid": "string",
      "severity": "string",
      "severity_level": "string",
      "severity_level_id": 0,
      "sfwder": "string",
      "sha256": "string",
      "shared_domains": "string",
      "shared_with": "string",
      "site": "string",
      "src_country": "string",
      "src_geoip_src": 0,
      "src_latitude": 0,
      "src_location": "string",
      "src_longitude": 0,
      "src_region": "string",
      "src_time": "string",
      "src_timezone": "string",
      "src_zipcode": "string",
      "srcip": "string",
      "suppression_end_time": 0,
      "suppression_key": "string",
      "suppression_start_time": 0,
      "telemetry_app": "string",
      "threat_match_field": "string",
      "threat_match_value": "string",
      "threat_source_id": 0,
      "threshold": 0,
      "threshold_time": 0,
      "timestamp": 0,
      "title": "string",
      "to_object": "string",
      "total_collaborator_count": 0,
      "traffic_type": "string",
      "transaction_id": 0,
      "true_obj_category": "string",
      "true_obj_type": "string",
      "tss_mode": "string",
      "two_factor_auth": "string",
      "type": "string",
      "universal_connector": "string",
      "ur_normalized": "string",
      "url": "string",
      "user": "string",
      "userPrincipalName": "string",
      "user_generated": "string",
      "user_id": "string",
      "useragent": "string",
      "userip": "string",
      "userkey": "string",
      "web_universal_connector": "string"
    }
  ]
}
Upload EDM Hash File to Staging
API Endpoint
:
https://<tenant-url>
/api/v2/services/dlp/edm/file/staging
Method:
POST
Application Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.0.0
Content-Type
application/json
Request Body
{
  "edm_filename": "customers.csv",
  "tgz_filename": "customers.tgz",
  "sha1": "d6727f9b11c80631773a993c9823e60634b138b4",
  "size": 15000,
  "keep_staging": true,
  "description": "This is the staging file for customers.tgz file on 2024-06-24"
}
Example API response
{
  "fileid": "4841a51417666e38760860b2c4e5b5b48627d2c4",
  "uploadid": "MzBlZWE4Y2YtMzZmYy00MGI5LThhNDktNWU2MTk5OWI1NjAzLjBmM2Q4YmI1LTM4OTctNDY2Yy05ZjQ5LTk1N2FmZWNjYjk5NQ",
  "part_max_size": 16000000,
  "msg": "Optional message"
}
Apply Staged EDM Hash File
API Endpoint
:
https://<tenant-url>
/api/v2/services/dlp/edm/file/apply
Method:
POST
Application Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.0.0
Content-Type
application/json
Request Body
{
  "fileid": fileid
}
Example API response
status code: 201
Response None
Netskope EDM Plugin Support
Feature
Support
Pull
No
Push
Yes
Performance Matrix
Here is the performance reading conducted for pushing hashes for ~1M rows (25 columns, Per column ~30 Characters Long String, 0.3M unique values per Column) data on a Large Cloud Exchange instance with these specifications.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Hashes Pushed From Source To Netskope Tenant Without Dict
~10 minutes
Hashes Pushed From Source To Netskope Tenant With Dict (2-3 columns)
~14 minutes
User Agent
The user-agent added in this plugin is in the following format:
netskope-ce-
<ce_version>
For example: netskope-ce-6.0.0
Workflow
Generate a v2 token for your Netskope tenant.
Create Netskope Tenant Using V2 Auth Token.
Configure Netskope EDM plugin.
Configure Sharing between the EDM Third Party Plugin and the Netskope EDM Plugin.
Check the status of the configured sharing.
Watch a Video
Click play to watch a video.
Generate a V2 (RBACv3) Token
In your Netskope tenant, go to
Settings > Administration > Administrators & Roles > Roles.
Click
New
to create a new role. Enter a Role Name and a Short Role Description. Make sure DLP is selected in the permissions section.
Select the
Manage And Apply
permission for the DLP > DLP Profile.
In Scope IT -> Alerts -> Manage Permission is Selected
Under Skope IT, select the
Manage
permission for Skope IT > Alerts.
Click
Service Account
.
Enter a Service Account Name.
Select the created role for the Service Account.
Enter an Expire time. Select from Day(s), Hour(s), Week(s), Year(s).
Click
Save
and copy the token. Use this to configure the Netskope Tenant Plugin in Cloud Exchange.
The Role with DLP permissions will be used by only the CFC and EDM Modules. For accessing and using other modules, use the role
Netskope Cloud Exchange
for creating a token.
Configure Netskope EDM Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Netskope Exact Data Match (EDM)
plugin box.
Enter the Basic Information:
Configuration Name
: Provide a name appropriate for the integration.
Tenant Name
: Select tenant name from the dropdown.
Change optional details if needed:
Enable SSL verification
: Enable the toggle to communicate via SSL. (Default=disabled)
Click
Save
.
You will be redirected to
Exact Data Match > Plugins
page, where you can see the configured plugin.
Configure Sharing between a 3rd-party EDM Plugin and the EDM Plugin
Go to the
Exact Data Match > Sharing
.
Click
Add Sharing Configuration
.
Source Configuration:
Select a configured 3rd-party plugin.
Destination Configuration:
Select the Netskope EDM Plugin as destination configuration.
Target:
The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate the Netskope EDM Plugin
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Monitor Status of Configured Sharing
Go to
Exact Data Match > Sharing and Upload Management
. Here you’ll see a list of status for all the configured sharing.
The status values are as follows:
Scheduled:
Indicates that the sharing has been configured and the pull and push operation are still waiting in the queue for processing.
Generating Hash:
Indicates that the generating hash process has been started. At this stage, in the background fetching > validating > sanitization (if opted for) > generating hash stages will be included.
Uploading Hash:
Indicates that uploading hash to the destination configuration has been started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
At this stage, checks hashing apply status to the destination configuration.
Apply In Progress:
This represents that the hash process is started and in progress state on the destination.
Completed:
Indicates that hash file has been pushed successfully to destination configuration.
Failed:
Indicates that the action final result failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Validate the Push on Netskope Tenant
To ensure the push of EDM hashes on the Netskope Tenant from Cloud Exchange:
Log in to your Netskope Tenant.
Go to
Policies > DLP
.
Click
Edit Rules
and select
DLP Rules
.
On the
Exact Match
tab, a list of files are shown.
Troubleshooting
Unable to share hashes
If you are unable to share hashes, you’ll receive an error like:
Error response: { “message”:“You cannot consume this service” }
What to do:
To solve the above mentioned issue, add the following endpoints to the V2 token on the Netskope tenant.
API Endpoint
Permission
/api/v2/events/dataexport/events/alert
Read
/api/v2/services/dlp/edm/file/staging/list
Read
/api/v2/services/dlp/edm/file/apply
Read + Write
/api/v2/services/dlp/edm/file/staging
Read + Write
Limitations
The maximum size of data that a Netskope EDM hash file can hold is 8 MB. Keep this in mind while configuring the Business Rule.
Column names in the source data should not contain special characters or spaces. Use underscores instead.
The EDM hash file name on Netskope tenant will be the same as the configuration name provided in Cloud Exchange.
Known Behavior
If sharing fails at any stage (Generating Hash/Uploading Hash/Checking Apply Status), the status will be marked as
Failed
and detailed error logs will be available in the Logging section.
The plugin checks the apply status of hashes on the Netskope tenant periodically. This process may take some time depending on the size of the data.
After hashes are successfully applied on the Netskope tenant, they cannot be deleted directly from Cloud Exchange. You need to delete them from the Netskope Tenant UI.
If we configure sharing with the Netskope EDM plugin and the file is uploaded and processed by the tenant, everything works fine. If we later change the CSV column order, or add or remove columns, the tenant will raise the error below when applying hashes to the Netskope tenant. To fix this issue, the customer must delete the previously uploaded EDM hash file from the Netskope tenant.
In this Topic
Exact Data Match Plugin (Beta)

---
## View Configured Exact Data Match Plugins (Beta)
**URL:** https://docs.netskope.com/en/view-configured-exact-data-match-plugins/
**Last Modified:** 2025-12-09T00:01:09+00:00
**Scraped:** 2026-08-23T07:15:32.446861+00:00

View Configured Exact Data Match Plugins (Beta) - Netskope Technical Documentation
View Configured Exact Data Match Plugins (Beta)
Read-access users can view the list of configured plugins and the status.
Go to
Exact Data Match
and click
Plugins
.
A list of configured plugins is displayed in the Configured Plugins section. Each plugin configuration is displayed as a box. There can be multiple plugin configurations for each vendor, each performing a task (pulling structured data, generating EDM hashes and sharing) a different way to the same or different vendor systems.
The following details are displayed on each box:
Logo
: Logo of the plugin vendor.
Name
: The configuration name provided while configuring that plugin.
Status
: Enabled or Disabled. If it is actively polling, the word
running
will be shown next to the arrow.
Sync Interval
: The interval between polls by Exact Data Match of the plugged-in system.
Last Run
: The last time the plugin configuration was successfully executed.
NA
is displayed before the first sync using that particular plugin.
In this Topic
View Configured Exact Data Match Plugins (Beta)

---
## Update Configured Exact Data Match Plugins (Beta)
**URL:** https://docs.netskope.com/en/update-configured-exact-data-match-plugins/
**Last Modified:** 2025-12-09T00:01:45+00:00
**Scraped:** 2026-08-23T07:15:33.614194+00:00

Update Configured Exact Data Match Plugins (Beta) - Netskope Technical Documentation
Update Configured Exact Data Match Plugins (Beta)
Only write-access users can update configured plugins.
A write-access user can edit, disable/enable, and delete the configuration using the Edit icon (pencil), the Disable icon (circle and slash), or the Delete icon (trash can).
In this Topic
Update Configured Exact Data Match Plugins (Beta)

---
## Configure 3rd-party Exact Data Match Plugins (Beta)
**URL:** https://docs.netskope.com/en/configure-3rd-party-exact-data-match-plugins/
**Last Modified:** 2025-12-09T02:15:19+00:00
**Scraped:** 2026-08-23T07:15:34.882048+00:00

Configure 3rd-party Exact Data Match Plugins (Beta) - Netskope Technical Documentation
Configure 3rd-party Exact Data Match Plugins (Beta)
Only admins and write-access users can configure 3rd-party Exact Data Match plugins. Exact Data Match comes with a library of supported plugins. Plugins can be easily configured to collect and share Exact Data Match hashes of structured data by following the plugin guide.
You can also disable, enable, or delete existing plugin configurations. Exact Data Match can be configured with multiple plugins to the same system for different workflows from either the same Netskope tenant or multiple Netskope tenants.
Exact Data Match only pulls and generates EDM (Exact Data Match) hashes of CSV and database queries.
MySQL Plugin for Exact Data Match
OracleDB Plugin for Exact Data Match
SMB File Share Plugin for Exact Data Match
Linux File Share Plugin for Exact Data Match
Microsoft File Share Plugin for Exact Data Match
Microsoft SQL Plugin for Exact Data Match
Netskope EDM Forwarder/Receiver Plugin for Exact Data Match (Beta)
In this Topic
Configure 3rd-party Exact Data Match Plugins (Beta)

---
## Linux File Share Plugin for Exact Data Match
**URL:** https://docs.netskope.com/en/linux-file-share-plugin-for-exact-data-match/
**Last Modified:** 2026-06-05T01:16:04+00:00
**Scraped:** 2026-08-23T07:15:36.074817+00:00

Linux File Share Plugin for Exact Data Match - Netskope Technical Documentation
Linux File Share Plugin for Exact Data Match
Release Notes
1.1.0
Added
Added support for configurable delimiters, including custom values with validation.
Added support for remove quotes from the CSV file.
Changed
Updated loggers and tooltips.
1.0.1
Fixed
Fixed plugin validation with respect to CSV path.
Fixed Sanity Step level validation.
1.0.0
Added
Initial release.
This document explains how to configure the Linux File Share EDM plugin v1.1.0 with the Exact Data Match plugin of the Netskope Cloud Exchange platform. Use this integration to pull CSV files from a Linux server and generate Exact Data Match (EDM) hashes according to the defined plugin configurations.
Prerequisites
To complete the configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tena
nt plugin
and
Exact Data Match plugin
already configured.
A Linux server with the SSH service enabled to pull the CSV file.
For systems with large specifications (32 GB RAM and 16-core CPU), ensure that at least twice the size of the CSV file is available as free storage. For example, to process a 3 GB CSV file efficiently, you should have approximately 7–8 GB of available disk space.
Linux File Share EDM Plugin Support
This plugin fetches CSV files from a Linux server via SFTP protocol and generates Exact Data Match (EDM) hashes according to the defined plugin configurations. The plugin supports advanced data sanitization, normalization, and hash generation capabilities to ensure data quality and security compliance.
Feature
Support
Pull
Yes
Push
No
Linux Server Permissions
Permission Type
Requirement
SSH Access
Required
File Read Permissions
Required
SFTP Protocol
Required
Required Permissions
These permissions are needed for the plugin configuration:
SSH user must have read permissions for the specified CSV file.
Network connectivity to the Linux server on the configured port (default: 22).
Sufficient disk space on Cloud Exchange for temporary file processing.
API Details
List of Libraries Used
This plugin uses Python libraries to establish secure connections to Linux servers and transfer CSV files via SFTP protocol.
Library:
Paramiko – SSH2 protocol library for Python
Usage:
Paramiko is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality. The plugin uses Paramiko to create secure SFTP connections, authenticate with the Linux server, and transfer CSV files securely. Paramiko provides comprehensive SSH functionality including authentication, channel management, and file transfer capabilities.
Create SSH Client Connection
import paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(
    hostname=self.server_ip,
    port=self.port,
    username=self.username,
    password=self.password,
    timeout=30)
Create an SFTP Client
sftp_client = ssh_client.open_sftp()
Download a CSV File from a Linux Server
sftp_client.get(
    remotepath=self.csv_file_path,
    localpath=local_file_path
)
Check File Existence and Permissions
try:
    file_stat = sftp_client.stat(self.csv_file_path)
    file_size = file_stat.st_size
    file_permissions = file_stat.st_mode
except FileNotFoundError:
    # Handle file not found error    pass
Close Connections
sftp_client.close()
ssh_client.close()
Performance Matrix
Here is the performance reading conducted for fetching and sanitizing ~1M Rows (25 columns, per column ~50 characters long string, 1.3 GB size, Avg Column Uniqueness: ~96%, Avg Row Uniqueness: ~96%) CSV file on a Large CE instance with these specifications:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
CSV data fetched from Linux File Share Without Sanitization
~7.5K rows/sec
For CE instance disk space, refer to this
documentation
.
Workflow
Get your Linux server credentials and file paths
Configure the Linux File Share EDM Plugin
Configure sharing between Linux File Share EDM Plugin and Tenant
Validate the Linux File Share EDM Plugin
Watch a Video
Click play to watch a video.
Get Your SFTP Shared File Path from Linux Server
Most SFTP setups are controlled via the SSH config file:
sudo vi /etc/ssh/sshd_config
Look for entries like:
Subsystem sftp internal-sftp
and especially:
Match User
<username>
ChrootDirectory /path/to/sftp/root
    ForceCommand internal-sftp
The value of
ChrootDirectory
is the SFTP root (shared path) for that user.
If no
ChrootDirectory
is set, then SFTP typically defaults to the user’s home directory:
echo $HOME
OR
grep
<username>
/etc/passwd
Example output:
testuser:x:1001:1001::/home/testuser:/bin/bash
Here,
/home/testuser
is the SFTP accessible path.
Configure the Linux File Share EDM Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Linux File Share v1.1.0 (
EDM
)
plugin.
Enter the Basic Information:
Configuration Name:
Enter a name appropriate for your integration.
The configuration name you provide will be used to give the name to the generated hash file to share with the Netskope Tenant. Be aware that if you later delete this configuration and create a new one with the same name, the hash file may already exist in the Netskope Tenant. In such cases, attempting to push the hash file to the tenant will result in an error, as the file with the same name already exists. Consider using a unique name to avoid this issue.
Sync Interval:
Adjust Sync Interval as per your requirement. (Default: 12 hours)
Click
Next
and enter the Configuration Parameters:
Server IP/Hostname:
IP address/Hostname of the Linux server.
Username:
Username of the Linux Machine.
Password:
Password for the provided username.
Port:
Port number to connect to the SSH service on the Linux machine.
CSV File Path:
Path of the CSV file to be pulled from the server.
Delimiter:
Single character delimiter used in the CSV/TXT file (e.g. comma, pipe, semicolon).
Remove Quotes:
Mark as checked if your CSV encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped.
By default, quotes are treated as literal text. Enable Remove Quotes toggle if your CSV uses double quotes to encapsulate fields that contain commas (like
"123 ABC Street, Suite 100"
). This ensures the field is treated as a single column. Note that this mode requires strict CSV formatting. If a field starts with a quote, any character, including a space, following the closing quote but preceding the comma (like
"Word"
,) will cause the row to be skipped.
Click
Next
and enter the Hash Generation and Sanitization Parameters:
Select the appropriate options for sanitization and hash generation operations:
Sanitization (Name Column):
Sanitize the content by checking the Name Column checkbox. (Default: Unchecked). The Sanitization Process performs the following actions:
One character:
The cell will be marked as invalid if it contains only one character.
Digits:
Cells containing digits will be marked as invalid.
Stopwords:
Cells that match a stopword from the list will be marked as invalid (This works only if the Remove stopwords checkbox is checked).
Non-alphanumeric characters:
Remove all special characters to validate the cell.
Hash Generation is divided into two parts:
Normalization:
Select the value from dropdown to normalize the data value. (Default: None)
Create Dictionary:
Select value from dropdown to create dictionary of unique values for selected field that can be used in DLP rule in netskope tenant. (Default: None)
Remove Stopwords:
Mark as checked if you want to remove certain stopwords as part of the sanitization process.(Default:Unchecked) Ensure that Name Column is checked for the applicable field to reflect the changes.
Note
Use the Normalization parameter to normalize the fetched results. For example, a number such as 123-45-6789 or 123 45 6789 will be treated as 123456789. Number normalizations ignore characters such as dots, dashes and spaces. A string normalization ignores the case sensitivity of the letters.
Use the Create Dictionary option only when necessary, as this operation is resource-intensive and may impact system performance. Choose this option thoughtfully for optimal efficiency.
Click
Next
. Preview the sanitization sample output by clicking
Preview Good File
or
Preview Bad File
.
If you are using the plugin with sanitization On, then the performance may be differ due to extra processing.
Proceed without sanitization:
Uncheck this option to proceed with sanitization. (Default: Checked)
All the data will be under consideration for hash generation if this option is
Unchecked
; otherwise, only the Good File content will be part of the hash generation.
Click
Save
. You will be redirected to
Exact Data Match > Plugins
page where you can see your configured plugin.
Configure an EDM Sharing Configuration for Linux File Share
A sharing configuration is used to share the generated EDM hashes with the destination platform. To share EDM hashes with your Netskope Tenant, create a sharing configuration using these steps:
Go to
Exact Data Match > Sharing
and click
Add Sharing Configuration
.
Configure the sharing parameters:
Source Configuration
: Select the configured Linux File Share EDM plugin.
Destination Configuration
: Select a destination where EDM Hash will be shared.
Target
: The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate th
e Linux File Share EDM Plugin
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate in Cloud Exchange
To validate the pulling of the configured plugin in Cloud Exchange, go to
Settings > Logging
and search for the Linux File Share EDM plugin logs.
You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
EDM Linux File Share [Linux File Share Config]: Successfully connected to Linux server 192.168.1.100.
The status values are as follows:
Scheduled
: Indicates that the sharing has been configured, and the pull and push operations are waiting in the queue for processing.
Generating Hash
: Indicates that the hash generation process has started. This stage includes fetching > validating > sanitization (if enabled) > generating hash.
Uploading Hash
: Indicates that uploading the hash to the destination configuration has started.
Upload Completed
: Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status
: Checking the apply status of hashes to the destination configuration.
Apply In Progress
: The hash process has started and is in progress on the destination.
Completed
: Indicates that the hash file has been pushed successfully to the destination configuration.
Failed
: Indicates that the final result of the action has failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Shared EDM hashes can be verified from the logs available at
Logging
in Cloud Exchange:
Validate on the Netskope Tenant
To ensure the push of EDM hashes on the Netskope Tenant from the cloud exchange:
Log in to your Netskope Tenant, go to
Policies > DLP
.
Click
Edit Rules
and select
Data Loss Prevention
.
On the
Exact Match
tab, a list of files is shown.
Troubleshooting the Linux File Share EDM Plugin
Unable to configure the Linux File Share EDM Plugin
If you are unable to configure the Linux File Share EDM plugin, it could be due to one of the following reasons:
Incorrect SSH credentials provided.
The user doesn’t have permission to read the CSV file.
Incorrect hostname/server IP address.
SSH port is disabled or blocked on the Linux server.
Network connectivity issues between Cloud Exchange and Linux server.
What to do:
Verify SSH credentials are correct:
ssh username@server_ip -p port_number
Check file permissions on the Linux server:
ls -la /path/to/your/csv/file.csv
Ensure the SSH service is running:
sudo systemctl status ssh
Verify network connectivity:
telnet server_ip port_number
CSV file not found or access denied
If you receive errors about file not found or access denied:
What to do:
Verify the CSV file path is correct and the file exists.
Ensure the SSH user has read permissions for the file.
Check if the file is not locked by another process.
Hash generation fails or takes too long
If hash generation fails or performance is poor:
What to do:
Check available disk space on Cloud Exchange (ensure at least 2x CSV file size).
Reduce CSV file size or split into smaller files.
Disable sanitization if not required to improve performance.
Monitor system resources during processing.
Known Behaviors
Sanitization can reduce processing speed by approximately 65% but improves data quality.
Dictionary creation is resource-intensive and should only be used when necessary.
The plugin creates temporary files during processing that are automatically cleaned up.
SSH connection timeouts may occur with very large files; consider increasing timeout values.
Memory usage scales with CSV file size; monitor system resources during large file processing.
Limitations
Each Netskope tenant has a limit of handling up to 5 staging files. If this maximum limit is reached, you may encounter the following error while sharing hashes:
EDM Netskope Exact Data Match [EDM Netskope] Received exit code 400, Error occurred while uploading edm hashes of configuration Linux EDM to the configuration EDM Netskope.
To resolve this error, you have to delete the existing files from staging.
In this Topic
Linux File Share Plugin for Exact Data Match

---
## OracleDB Plugin for Exact Data Match
**URL:** https://docs.netskope.com/en/oracledb-plugin-for-exact-data-match/
**Last Modified:** 2026-06-05T02:27:23+00:00
**Scraped:** 2026-08-23T07:15:37.274390+00:00

OracleDB Plugin for Exact Data Match - Netskope Technical Documentation
OracleDB Plugin for Exact Data Match
Release Notes
1.1.0
Added
Added support for removing quotes from the pulled data.
Changed
Updated loggers and tooltips.
1.0.1
Fixed
Fixed plugin validation with respect to CSV path.
Fixed Sanity Step level validation.
1.0.0
Added
Initial release.
This document explains how to configure the OracleDB EDM plugin v1.1.0 with the Exact Data Match module of the Netskope Cloud Exchange platform. This plugin is used to pull raw data from a configured Oracle database server to generate EDM hashes.
Prerequisites
To complete the configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Exact Data Match plugin
already configured.
OracleDB server setup
OracleDB Server database user with read-only (Select) access to fetch the data.
Ensure that at least twice the size of the data is available as free storage. For example, to process a 3 GB CSV file/ DB table efficiently, you should have approximately 7–8 GB of available disk space.
Oracle Database EDM Plugin Support
This plugin is used to pull raw data from a configured Oracle database server to generate EDM hashes. The plugin supports advanced data sanitization, normalization, and hash generation capabilities to ensure data quality and security compliance.
Feature
Support
Pull
Yes
Push
No
OracleDB Database Permissions
Permission Type
Requirement
User Read Access to Mentioned Database
Required
OracleDB Database Read Permissions
Required
Database Port Access
Required
Required Permissions
Database user must have read permissions for the specified database.
Network connectivity to the Oracle Database server on the configured port (default: 1521).
Sufficient disk space on Cloud Exchange for temporary file processing.
API Details
List of Libraries Used to fetch Database Records
This plugin uses Python libraries and Oracle DB driver to establish secure connections to Oracle Database and transfer tables raws by executing SQL query.
Library:
sqlalchemy and oracledb
Usage:
SQLAlchemy is the Python SQL toolkit provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language to execute SQL queries. Oracle Connector/Python enables Python programs to access Oracle databases.
Create Client Connection
from sqlalchemy import create_engine
eng = create_engine(connection_string) # creates connection with database.
Execute SQL query with Read-Only Session
with eng.connect() as connection:
      # used to stop user from executing any database modification query.
      result = connection.execute(text("SET TRANSACTION READ ONLY"))
      query = text(config["query"].strip(";"))
      result = connection.execute(query)
Generate CSV File from fetched records in batches
# csv_path will be new csv file
self.store_data_to_csv([columns], csv_path)
if fetch_only_sample_data:
    rows = result.fetchmany(SAMPLE_CSV_ROW_COUNT)
else:
    rows = result.yield_per(BATCH_SIZE)
self.store_data_to_csv(rows, csv_path, replace=False)
Performance Matrix
Here is the performance reading conducted for fetching and sanitizing ~1M Rows (25 columns, per column ~50 characters long string, all unique values per each row,1.3 GB size, Avg Column Uniqueness: ~96%, Avg Row Uniqueness: ~96%) from Database table on a Large CE instance with these specifications:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Database table data fetched from MySQL Without Sanitization
~5.5K rows/sec
For CE instance disk space, refer to this
documentation
.
Workflow
Create a user on Oracle DB server with read permissions.
Configure OracleDB EDM Plugin.
Configure sharing between OracleDB EDM Plugin and EDM Netskope plugin.
Validate the OracleDB plugin.
Watch a Video
Click play to watch a video.
Configuration on OracleDB Server
Create a user
Follow these steps to create the user on OracleDB Database:
Log in to the Oracle database instance and open the SQL Plus terminal.
To create a new user and grant read-only permissions, you need to connect as a user with DBA (Database Administrator) privileges.
SYS as SYSDBA
Run the following SQL command to create a new user:
CREATE USER <new_username> IDENTIFIED BY
<new_password>
;
GRANT CONNECT TO
<new_username>
;
Grant user read-only access to specific table to pull the data.
GRANT SELECT ON
<table_name>
TO
<new_username>
;
Note
Replace
and
with your username and password to create a user.
Replace
with the name of the table you want to provide read-only access to.
Configure the Oracle Database Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
OracleDB v1.1.0 (
EDM
)
plugin.
Enter the Basic Information:
Configuration Name:
Enter a name appropriate for your plugin.
The configuration name you provide will be used to give the name to the generated hash file to share with the Netskope tenant. Be aware that if you later delete this configuration and create a new one with the same name, the hash file may already exist in the Netskope tenant. In such cases, attempting to push the hash file to the tenant will result in an error, as the file with the same name already exists. Consider using a unique name to avoid this issue.
Sync Interval:
Interval to pull the data from this plugin source. Default value is 12 hours. (Default: 12 hours)
Click
Next
and enter the Configuration Parameters:
Server IP/Hostname:
IP address or Hostname where the OracleDB server is located.
Username:
OracleDB database username to access the server. Ensure that it is a valid username with the read-only permission.
Password:
Password associated with the provided database username.
SID:
Oracle database name from which the data is to be retrieved. Ensure that the database name is spelled correctly, as database names are case-sensitive.
Port:
Enter the TCP port number that the Oracle database is running on.
Query:
Provide a read-only query to fetch data from database.(Read-only means ‘Select’ Query)
Remove Quotes:
Enable this if your data file encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped. Helpful for CSVs exported from databases.
By default, quotes are treated as literal text. Enable Remove Quotes toggle if your CSV uses double quotes to encapsulate fields that contain commas (like
"123 ABC Street, Suite 100"
). This ensures the field is treated as a single column. Note that this mode requires strict CSV formatting. If a field starts with a quote, any character, including a space, following the closing quote but preceding the comma (like
"Word"
,) will cause the row to be skipped.
Click
Next
and enter the Hash Generation and Sanitization Parameters:
Select the appropriate options for sanitization and hash generation operations:
Sanitization (Name Column):
Sanitize the content by checking the Name Column checkbox. (Default: Unchecked). The Sanitization Process performs the following actions:
One character:
The cell will be marked as invalid if it contains only one character.
Digits:
Cells containing digits will be marked as invalid.
Stopwords:
Cells that match a stopword from the list will be marked as invalid (This works only if the Remove stopwords checkbox is checked).
Non-alphanumeric characters:
Remove all special characters to validate the cell.
Hash Generation is divided into two parts:
Normalization:
Select the value from dropdown to normalize the data value. (Default: None)
Create Dictionary:
Select value from dropdown to create dictionary of unique values for selected field that can be used in DLP rule in netskope tenant. (Default: None)
Remove Stopwords:
Mark as checked if you want to remove certain stopwords as part of the sanitization process.(Default: Unchecked) Ensure that Name Column is checked for the applicable field to reflect the changes.
Note
Use Normalization parameter to normalize the fetched results. For example, a number such as 123-45-6789 or 123 45 6789 will be treated as 123456789. Number normalizations ignore characters such as dots, dashes and spaces. A string normalization ignores the case sensitivity of the letters.
Use the Create Dictionary option only when necessary, as this operation is resource-intensive and may impact system performance. Choose this option thoughtfully for optimal efficiency.
Click
Next
. Preview the sanitization sample output by clicking
Preview Good File
or
Preview Bad File
.
If you are using the plugin with sanitization On, then the performance may be differ due to extra processing.
Proceed without sanitization:
Uncheck this option to proceed with sanitization. (Default: Checked)
All the data will be under consideration for hash generation if this option is
Unchecked
; otherwise, only the Good File content will be part of the hash generation.
Click Save. You will be redirected to
Exact Data Match > Plugins
page where you can see your configured plugin.
Configure Sharing between Oracle DB and Cloud Exchange
A sharing configuration is used to share the generated EDM hashes with the destination platform. To share EDM hashes with your Netskope Tenant, create a sharing configuration using these steps:
Go to
Exact Data Match > Sharing
and click
Add Sharing Configuration
.
Configure the sharing parameters:
Source Configuration:
Select the configured EDM Oracle plugin.
Destination Configuration:
Select a destination where EDM Hash will be shared.
Target:
The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate the Oracle DB Plugin
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate the Pull in Cloud Exchange
To validate the pulling of the configured plugin in Cloud Exchange, go to
Settings > Logging
and search for the OracleDB EDM plugin logs.
You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
If a sharing configuration has been established for the source plugin, its status can be monitored on the
Sharing and Upload Management page
.
The status values are as follows:
Scheduled:
Indicates that the sharing has been configured and the pull and push operation are still waiting in the queue for processing.
Generating Hash:
Indicates that the generating hash process has been started.At this stage, in the background fetching > validating >sanitization (if opted for) > generating hash staged will be included.
Uploading Hash:
Indicates that uploading hash to the destination configuration has been started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
At this stage, checking the apply status of hashes to the destination configuration.
Apply In Progress:
This represents that the hash process is started and in progress state on the destination.
Completed:
Indicates that hash file has been pushed successfully to destination configuration.
Failed:
Indicates that the final result of the action has been failed to execute.The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Shared EDM hashes can be verified from the logs available at
Logging
in Cloud Exchange:
Validate the Push to your Netskope Tenant
To ensure the push of EDM hashes on the Netskope Tenant from the cloud exchange:
Log in to your Netskope Tenant, go to
Policies > DLP
.
Click
Edit Rules
and select
Data Loss Prevention
.
On the
Exact Match
tab, a list of files is shown.
Troubleshooting the Oracle DB Plugin
Unable to configure the Oracle DB plugin
If you are unable to configure the OracleDB EDM plugin, it could be due to one of the following reasons:
Incorrect credentials provided.
The user doesn’t have required permissions.
Incorrect hostname/server IP address.
Incorrect Database Name.
What to do
:
Make sure to provide the correct credentials.
Make sure that the user has the required permissions for the database and table.
Make sure that the correct hostname/server IP.
Make sure that the database name is correct.
Hash generation fails or takes too long
If hash generation fails or performance is poor.
What to do
:
Check available disk space on Cloud Exchange (ensure at least 2x CSV file size).
Reduce file/table size or split into smaller tables.
Disable sanitization if not required to improve performance.
Monitor system resources during processing.
Known Behaviors
Sanitization can reduce processing speed by approximately 65% but improves data quality.
Dictionary creation is resource-intensive and should only be used when necessary.
The plugin creates temporary files during processing that are automatically cleaned up.
SSH connection timeouts may occur with very large files; consider increasing timeout values.
Memory usage scales with CSV file size/table size; monitor system resources during large file processing.
In this Topic
OracleDB Plugin for Exact Data Match

---
## Microsoft File Share Plugin for Exact Data Match
**URL:** https://docs.netskope.com/en/microsoft-file-share-plugin-for-exact-data-match/
**Last Modified:** 2026-06-05T02:17:27+00:00
**Scraped:** 2026-08-23T07:15:38.476010+00:00

Microsoft File Share Plugin for Exact Data Match - Netskope Technical Documentation
Microsoft File Share Plugin for Exact Data Match
Release Notes
1.1.0
Added
Added support for configurable delimiters, including custom values with validation.
Added support for remove quotes from the CSV file.
Changed
Updated loggers and tooltips.
1.0.1
Fixed
Fixed plugin validation with respect to CSV path.
Fixed Sanity Step level validation.
1.0.0
Added
Initial release.
This document explains how to configure the Microsoft File Share EDM v1.1.0 plugin with the Exact Data Match module of the Netskope Cloud Exchange platform. This plugin fetches CSV files from a Microsoft Windows server using either SMB or SFTP protocols, and generates Exact Data Match (EDM) hashes according to the defined plugin configurations.
The plugin supports dual protocol connectivity: SMB (Server Message Block) for native Microsoft file sharing, and SFTP (SSH File Transfer Protocol) for secure file transfer. This flexibility allows organizations to choose the most appropriate protocol based on their security requirements and infrastructure setup.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Exact Data Match plugin
already configured.
A Microsoft Windows server with network file sharing capabilities.
CSV files stored on the Microsoft server containing the data to be processed for EDM hash generation.
Appropriate user credentials with read permissions for the CSV files on the Microsoft server.
For the SMB Protocol
Microsoft server with network sharing enabled (SMB/CIFS service running).
Shared folder configured with appropriate permissions.
Network connectivity to the Microsoft server on SMB ports (typically 445).
For the SFTP Protocol
Microsoft server with OpenSSH service enabled and configured.
SSH service running and accessible from Cloud Exchange.
Network connectivity to the Microsoft server via SFTP protocol (typically port 22).
For systems with large specifications (32 GB RAM and 16-core CPU), ensure that at least twice the size of the CSV file is available as free storage. For example, to process a 3 GB CSV file efficiently, you should have approximately 7–8 GB of available disk space.
Microsoft File Share Plugin Support
This plugin fetches CSV files from a Microsoft Windows server using either SMB or SFTP protocols and generates Exact Data Match (EDM) hashes according to the defined plugin configurations. The plugin supports dual protocol connectivity for maximum flexibility and compatibility with different network environments.
Feature
Support
Pull
Yes
Push
No
Permissions and Mappings
Microsoft Server Permissions
Permission Type
SMB Protocol
SFTP Protocol
File Read Access
Required
Required
Network Share Access
Required
Not Required
SSH Access
Not Required
Required
Port Access
445 (SMB)
22 (SSH)
Required Permissions
These permissions are needed for the plugin configuration:
For the SMB Protocol
Microsoft Server User should have read access to the shared folder and CSV file.
Network connectivity to the Microsoft server on port 445.
SMB/CIFS service enabled on the Microsoft server.
For the SFTP Protocol
SSH user must have read permissions for the specified CSV file.
Network connectivity to the Microsoft server on the configured port (default: 22).
OpenSSH service enabled and running on the Microsoft server.
API Details
List of Libraries Used
This plugin uses Python libraries to establish connections to Microsoft Windows servers and transfer CSV files via SMB or SFTP protocols.
For the SMB Protocol
Library:
pysmb – Pure Python SMB/CIFS library
Usage:
pysmb is a pure Python implementation of the SMB/CIFS protocol that allows Python applications to access and transfer files to/from SMB/CIFS shared folders. The plugin uses pysmb to connect to Windows shared folders, authenticate with the server, and download CSV files securely over the SMB protocol.
For the SFTP Protocol
Library:
Paramiko – SSH2 protocol library for Python
Usage:
Paramiko is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality. The plugin uses Paramiko to create secure SFTP connections, authenticate with the Windows server, and transfer CSV files securely when OpenSSH is enabled on Windows.
SMB Protocol Implementation
Create a SMB Connection
from ..lib.smb.SMBConnection import SMBConnection
connection = SMBConnection(
    username=configuration.get("smb_username"),
    password=configuration.get("smb_password"),
    my_name="netskope_machine",
    remote_name=configuration.get("smb_machine_name"),
)
# Connect to the server
connection_result = connection.connect(
    ip=configuration.get("smb_server_ip"),
)
Download a CSV File via SMB
with open(csv_file_path, "wb") as file_object:
    if record_count:
	   # Partial file retrieval (for sample data)
        smb_connection.retrieveFileFromOffset(
            shared_directory_name,
            remote_file_path,
            file_obj=file_object,
            offset=0,
            max_length=record_count * 5 * 1024,
        )
    else:
        # Full file retrieval
        smb_connection.retrieveFile(
            shared_directory_name,
            remote_file_path,
            file_obj=file_object,
        )
Close and SMB Connection
smb_connection.close()
SFTP Protocol Implementation
Create an SSH Client Connection
from ..lib import paramiko
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(
    hostname=configuration.get("sftp_server_ip"),
    username=configuration.get("sftp_username"),
    password=configuration.get("sftp_password"),
    port=configuration.get("sftp_port"),
)
Create an SFTP Client
with ssh_connection.open_sftp() as sftp_session:
    # SFTP operations here
    pass
Download a CSV File via SFTP
with ssh_connection.open_sftp() as sftp_session:
    if record_count:
        # Partial file retrieval (for sample data)
        file_content = []
        with sftp_session.file(
            remote_file_path, "r"
        ) as remote_file:
            for _ in range(record_count + 1):
                record = remote_file.readline()
                if not record:
                    break
                file_content.append(record)
        with open(
            csv_file_path, "w", encoding="utf-8", newline="\n"
        ) as local_file:
            local_file.writelines(file_content)
    else:
        # Full file retrieval
        sftp_session.get(remote_file_path, csv_file_path)
Close SFTP Connections
ssh_connection.close()
Protocol Parameters
SMB Protocol Parameters
Parameter
Value
Protocol
SMB/CIFS (Server Message Block)
Default Port
445
Authentication
Username/Password
Connection Type
Network File Sharing
Supported Versions
SMB 2.0, SMB 3.0
SFTP Protocol Parameters
Parameter
Value
Protocol
SFTP (SSH File Transfer Protocol)
Default Port
22
Authentication
Username/Password
Connection Type
Secure Shell (SSH)
Encryption
SSH-2 Protocol
Performance Matrix
Here is the performance reading conducted for fetching and sanitizing ~1M Rows (25 columns, per column ~50 characters long string, 1.3 GB size, Avg Column Uniqueness: ~96%, Avg Row Uniqueness: ~96%) CSV file on a Large CE instance with these specifications:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
CSV data fetched from Microsoft File Share Without Sanitization
~7.4K rows/sec
Note
This performance reading is done with SMB protocol configured on a Windows instance.
For CE instance disk space, refer to this
documentation
.
Performance Comparison
SFTP protocol shows approximately 50% better performance compared to SMB.
Sanitization reduces processing speed by approximately 55-65% for both protocols.
SFTP is recommended for better performance and security.
Workflow
Configure the Microsoft Windows server (SMB or SFTP).
Configure the Microsoft File Share EDM Plugin.
Configure sharing between the Microsoft File Share EDM Plugin and the Netskope EDM Plugin.
Validate the Microsoft File Share EDM Plugin.
Watch a Video
Click play to watch a video.
Configure the Microsoft Windows Server
For the SMB File Sharing
Find or create the folder you want to share.
Right-click on the folder and select
Properties
.
Go to the
Sharing
tab and click
Advanced Sharing
.
Check
Share this folder
.
Give the share a name if needed.
Optionally, modify the Share Name and click
Permissions
to set access control.
In the
Permissions
window, choose the users or groups you want to give access to:
If the required user is not listed under the
Group or user names
section, click
Add
. Select
Advanced
, click
Find Now
, and choose the user from the list.
Once added, confirm that the user appears in the
Permissions
dialog box, and ensure they have
Read
permission for the folder.
Set the level of access (Read, Change, or Full Control).
Click
Apply
and
OK
.
Save the changes and check that the folder name shows right after the computer name in the
Network Path
.
Steps to Enable OpenSSH on a Windows Server for SFTP
Follow these steps to enable the OpenSSH service on the Windows server:
https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui
Configure the Microsoft File Share EDM Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Microsoft File Share EDM v1.1.0
plugin box.
Enter the Basic Information:
Configuration Name:
Enter a name appropriate for your integration.
The configuration name you provide will be used to give the name to the generated hash file to share with the Netskope tenant. Be aware that if you later delete this configuration and create a new one with the same name, the hash file may already exist in the Netskope tenant. In such cases, attempting to push the hash file to the tenant will result in an error, as the file with the same name already exists. Consider using a unique name to avoid this issue.
Sync Interval:
Adjust Sync Interval as per your requirement. (Default: 12 hours)
Protocol Selection:
Choose the protocol to connect to the Microsoft server:
SMB:
Protocol natively designed for Microsoft-based systems. Best for internal networks.
SFTP:
Secure file transfer protocol. Comparatively faster and more secure. Requires OpenSSH service on Windows.
Click
Next
and enter the Configuration Parameters:
Configuration Parameters For SMB:
Server IP/Hostname:
IP address or hostname of the Windows server.
Machine Name:
NetBIOS machine name of the Windows server.
Username:
Username with read access to the shared directory.
Password:
Password associated with the username.
Shared Directory Name:
Name of the shared directory.
CSV File Path:
Path to the CSV file relative to the shared directory.
Delimiter:
Single character delimiter used in the CSV/TXT file (e.g. comma, pipe, semicolon).
Remove Quotes:
Mark as checked if your CSV encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped.
Configuration Parameters For SFTP:
Server IP/Hostname:
IP address or hostname of the Windows server.
Username:
Username with read access to the CSV file.
Password:
Password associated with the username.
Port:
Port to connect with OpenSSH service (Default: 22).
CSV File Path:
Full path to the CSV file on the server.
Delimiter:
Single character delimiter used in the CSV/TXT file (e.g. comma, pipe, semicolon).
Remove Quotes:
Mark as checked if your CSV encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped.
By default, quotes are treated as literal text. Enable Remove Quotes toggle if your CSV uses double quotes to encapsulate fields that contain commas (like
"123 ABC Street, Suite 100"
). This ensures the field is treated as a single column. Note that this mode requires strict CSV formatting. If a field starts with a quote, any character, including a space, following the closing quote but preceding the comma (like
"Word",
) will cause the row to be skipped.
Click
Next
and enter the
Hash Generation and Sanitization Parameters:
Select the appropriate options for sanitization and hash generation operations:
Sanitization (Name Column):
Sanitize the content by checking the Name Column checkbox. (Default: Unchecked). The Sanitization Process performs the following actions:
One character:
The cell will be marked as invalid if it contains only one character.
Digits:
Cells containing digits will be marked as invalid.
Stopwords:
Cells that match a stopword from the list will be marked as invalid (This works only if the Remove stopwords checkbox is checked).
Non-alphanumeric characters:
Remove all special characters to validate the cell.
Hash Generation is divided into two parts:
Normalization:
Select the value from dropdown to normalize the data value. (Default: None)
Create Dictionary:
Select value from dropdown to create dictionary of unique values for selected field that can be used in DLP rule in netskope tenant. (Default: None)
Remove Stopwords:
Mark as checked if you want to remove certain stopwords as part of the sanitization process.(Default:Unchecked) Ensure that Name Column is checked for the applicable field to reflect the changes.
Note
Use Normalization parameter to normalize the fetched results. For example, a number such as 123-45-6789 or 123 45 6789 will be treated as 123456789. Number normalizations ignore characters such as dots, dashes and spaces. A string normalization ignores the case sensitivity of the letters.
Use the Create Dictionary option only when necessary, as this operation is resource-intensive and may impact system performance. Choose this option thoughtfully for optimal efficiency.
Click
Next
. Preview the sanitization sample output by clicking
Preview Good File
or
Preview Bad File
.
If you are using the plugin with sanitization On, then the performance may be differ due to extra processing.
Proceed without sanitization:
Uncheck this option to proceed with sanitization. (Default: Checked)
All the data will be under consideration for hash generation if this option is
Unchecked
; otherwise, only the Good File content will be part of the hash generation.
Click
Save
. You will be redirected to
Exact Data Match > Plugins
page where you can see your configured plugin.
Configure Sharing for Microsoft File Share
A sharing configuration is used to share the generated EDM hashes with the destination platform. To share EDM hashes with Netskope Tenant, create a sharing configuration using these steps:
Go to
Exact Data Match > Sharing
and click
Add Sharing Configuration
.
Configure the sharing parameters:
Source Configuration:
Select the configured Microsoft File Share EDM plugin.
Destination Configuration:
Select a destination where EDM Hash will be shared.
Target:
The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate the
Microsoft File Share EDM Plugin
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate in Cloud Exchange
To validate the pulling of the configured plugin in Cloud Exchange, go to
Settings > Logging
and search for the Microsoft File Share EDM plugin logs.
You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
The status values are as follows:
Scheduled:
Indicates that the sharing has been configured, and the pull and push operations are waiting in the queue for processing.
Generating Hash:
Indicates that the hash generation process has started. This stage includes fetching > validating > sanitization (if enabled) > generating hash.
Uploading Hash:
Indicates that uploading the hash to the destination configuration has started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
Checking the apply status of hashes to the destination configuration.
Apply In Progress:
The hash process has started and is in progress on the destination.
Completed:
Indicates that the hash file has been pushed successfully to the destination configuration.
Failed:
Indicates that the final result of the action has failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Shared EDM hashes can be verified from the logs available at
Logging
in Cloud Exchange:
Validate in the Netskope Tenant
To ensure the push of EDM hashes on the Netskope Tenant from the cloud exchange:
Log in to your Netskope Tenant, go to
Policies > DLP
.
Click
Edit Rules
and select
Data Loss Prevention
.
On the
Exact Match
tab, a list of files is shown.
Troubleshooting the EDM Microsoft File Share Plugin
Unable to configure the Microsoft File Sharing Plugin
If you are unable to configure the Microsoft File Share EDM plugin, it could be due to one of the following reasons:
For the SMB Protocol
Incorrect SMB credentials provided.
SMB/CIFS service not running on Windows server.
Network connectivity issues to port 445.
Shared folder not properly configured.
User doesn’t have read permissions to the shared directory.
For the SFTP Protocol
Incorrect SSH credentials provided.
OpenSSH service not running on Windows server.
Network connectivity issues to port 22.
SSH service not properly configured.
User doesn’t have read permissions for the CSV file.
What to do:
For SMB Protocol:
Verify SMB credentials and shared folder access:
cmd net use \\\\server_ip\\shared_folder /user:username password
Check SMB service status on Windows server:
Get-Service -Name LanmanServer
Test network connectivity:
telnet server_ip 445
For SFTP Protocol:
Verify SSH credentials:
bash ssh username@server_ip -p port_number
Check OpenSSH service status:
Get-Service -Name sshd
Test network connectivity:
telnet server_ip 22
Protocol-specific Connection Issues
SMB Connection Failures
If SMB connections fail:
What to do:
Enable SMB on Windows server if disabled:
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Configure Windows Firewall for SMB:
New-NetFirewallRule -DisplayName "SMB-In" -Direction Inbound -Protocol TCP -LocalPort 445
Verify shared folder permissions and ensure the user has read access.
SFTP Connection Failures
If SFTP connections fail:
What to do:
Install OpenSSH Server if not installed:
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start and configure SSH service:
Start-Service sshd Set-Service -Name sshd -StartupType 'Automatic'
Configure Windows Firewall for SSH:
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
CSV file not found or access denied
If you receive errors about file not found or access denied.
What to do:
Verify the CSV file path is correct and the file exists.
Ensure the user has read permissions for the file.
Check if the file is not locked by another process.
For SMB: Ensure the path is relative to the shared directory.
For SFTP: Ensure the path is the full absolute path on the server.
Hash generation fails or takes too long
If hash generation fails or performance is poor.
What to do:
Check available disk space on Cloud Exchange (ensure at least 2x CSV file size).
Consider using SFTP protocol for better performance.
Reduce CSV file size or split into smaller files.
Disable sanitization if not required to improve performance.
Monitor system resources during processing.
Sharing configuration fails
If sharing EDM hashes to Netskope Tenant fails.
What to do:
Verify the destination configuration is properly set up.
Check network connectivity to the Netskope tenant.
Ensure the hash file name doesn’t already exist in the tenant.
Review logs for specific error messages.
Known Behaviors
Large CSV files may require significant processing time and system resources.
Sanitization can reduce processing speed by approximately 65% but improves data quality.
Dictionary creation is resource-intensive and should only be used when necessary.
The plugin creates temporary files during processing that are automatically cleaned up.
SSH connection timeouts may occur with very large files; consider increasing timeout values.
Memory usage scales with CSV file size; monitor system resources during large file processing.
Windows Firewall rules may need to be configured for both SMB and SFTP protocols.
Limitations
Each Netskope tenant has a limit of handling up to 5 staging files. If this maximum limit is reached, you may encounter the following error while sharing hashes:
EDM Netskope Exact Data Match [EDM Netskope] Received exit code 400, Error occurred while uploading EDM hashes of configuration Linux EDM to the configuration EDM Netskope.
To resolve this error, you have to delete the existing files from staging.
In this Topic
Microsoft File Share Plugin for Exact Data Match

---
## MySQL Plugin for Exact Data Match
**URL:** https://docs.netskope.com/en/mysql-plugin-for-exact-data-match/
**Last Modified:** 2026-06-05T02:27:05+00:00
**Scraped:** 2026-08-23T07:15:39.667748+00:00

MySQL Plugin for Exact Data Match - Netskope Technical Documentation
MySQL Plugin for Exact Data Match
Release Notes
1.1.0
Added
Added support for removing quotes from the pulled data.
Changed
Updated loggers and tooltips.
1.0.1
Fixed
Fixed plugin validation with respect to CSV path.
Fixed Sanity Step level validation.
1.0.0
Added
Initial release.
This document explains how to configure the MySQL EDM plugin v1.1.0 with the Exact Data Match module of the Netskope Cloud Exchange platform. Use this plugin to pull database records from a MySQL Database and generate Exact Data Match (EDM) hashes according to the defined plugin configurations.
Prerequisites
To complete the configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Exact Data Match plugin
already configured.
MySQL Server database user with read-only (Select) access to fetch the data.
For systems with large specifications based standalone deployment ( 32 GB RAM and 16-core CPU), ensure that at least twice the size of the database is available as free storage. For example, to process a 3 GB database efficiently, you should have approximately 7–8 GB of available disk space.
MySQL EDM Plugin Support
This plugin fetches MySQL Database records from a MySQL Database via SQL query and generates Exact Data Match (EDM) hashes according to the defined plugin configurations. The plugin supports advanced data sanitization, normalization, and hash generation capabilities to ensure data quality and security compliance.
Feature
Support
Pull
Yes
Push
No
MySQL Database Permissions
Permission Type
Requirement
User Read Access to Mentioned Database
Required
MySQL Database Read Permissions
Required
Database Port Access
Required
Required Permissions
Database user must have read permissions for the specified database.
Network connectivity to the MySQL server on the configured port (default: 3306).
Sufficient disk space on Cloud Exchange for temporary file processing.
API Details
List of Libraries Used to fetch Database Records
This plugin uses Python libraries and MySQL driver to establish secure connections to MySQL Database and transfer tables raws by executing SQL query.
Library:
sqlalchemy and mysql-connector-python
Usage:
SQLAlchemy is the Python SQL toolkit provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language to execute SQL queries. MySQL Connector/Python enables Python programs to access MySQL databases.
Create Client Connection
from sqlalchemy import create_engine
eng = create_engine(
       connection_string, connect_args={"connect_timeout": CONNECTION_TIMEOUT}
)  # creates connection with database.
Execute SQL query with Read-Only Session
with eng.connect() as connection:
      # used to stop user from executing any database modification query.
      result = connection.execute(text("START TRANSACTION READ ONLY;"))
      query = text(config["query"])
      result = connection.execute(query)
Generate CSV File from fetched records in batches
# csv_path will be new csv file
# Fetch 100,000 rows per batch
while True:
    rows = result.fetchmany(BATCH_SIZE)
    if not rows:
        break  # No more rows to fetch
    #store rows into csv file
    self.store_data_to_csv(rows, csv_path)
Performance Matrix
Here is the performance reading conducted for fetching and sanitizing ~1M Rows (25 columns, per column ~50 characters long string,1.3 GB size, Avg Column Uniqueness: ~96%, Avg Row Uniqueness: ~96%) from Database table on a Large CE instance with these specifications:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Database table data fetched from MySQL without sanitization
~6K rows/sec
For CE instance disk space refer to this
documentation
.
Workflow
Configure MySQL Server
.
Configure MySQL EDM Plugin.
Configure sharing between MySQL EDM Plugin and Tenant.
Validate the MySQL plugin.
Watch a Video
Click play to watch a video.
Configure MySQL Server
For a MySQL database, you must create a MySQL user account with read-only permissions granted to the specific database and tables from which the data will be pulled.
Follow the below steps to create the user on MySQL Database:
Enable MySQL server for remote connection.
Expose the Port on which MySQL server is hosted to ensure MySQL server is accessible on remote machines.
Create a read-only user on the MySQL server by following the below steps:
Login to MySQL server as an Administrator:
mysql -u
<root>
-p
Enter the <root> user password
Create a new User:
CREATE USER '
<new_username>
'@'%' IDENTIFIED BY '
<secret>
';
Grant Read Only Permissions for particular databases:
GRANT SELECT ON
<database_name>
.* TO '
<new_username>
'@'%';
The above command grants the user read-only access to the database from the localhost only. If you know the hostname or IP address of the host that the collector will be installed on, type the following command:
GRANT SELECT ON <database_name>.* TO '
<new_username>
'@'
<host_name>
or
<ip_address>
';
Save the changes
FLUSH PRIVILEGES;
SHOW GRANTS FOR '
<new_username>
'@'
<host_name>
or
<ip_address>
'
Note
Replace
<root>
with Administrator user.
Replace
<new_username>
with new username to create.
Replace
<database_name>
with a database to grant read-only access.
Replace
<host_name>
or
<ip_address>
with the hostname or IP address of the host on which collector will be installed.
Configure MySQL EDM Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
MySQL v1.1.0 (
EDM
)
plugin.
Enter the Basic Information:
Configuration Name:
Enter a name appropriate for your plugin.
The configuration name you provide will be used to give the name to the generated hash file to share with the Netskope tenant. Be aware that if you later delete this configuration and create a new one with the same name, the hash file may already exist in the Netskope tenant. In such cases, attempting to push the hash file to the tenant will result in an error, as the file with the same name already exists. Consider using a unique name to avoid this issue.
Sync Interval:
Adjust Sync Interval as per your requirement. (Default: 12 hours)
Click
Next
and enter the Configuration Parameters:
Server IP/Hostname:
Provide IP or hostname of My SQL Server.
Username:
Provide MySQL database username to access the database and its table.
Password:
Provide password associated with the username.
Database Name:
Provide a database name from which you want to retrieve data.
Port:
Provide TCP port on which your MySQL database is running.(Default Port: 3306)
Query:
Provide a read-only query to fetch data from database.(Read-only means ‘Select’ Query)
Remove Quotes:
Enable this if your data file encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped. Helpful for CSVs exported from databases.
By default, quotes are treated as literal text. Enable Remove Quotes toggle if your CSV uses double quotes to encapsulate fields that contain commas (like
"123 ABC Street, Suite 100"
). This ensures the field is treated as a single column. Note that this mode requires strict CSV formatting. If a field starts with a quote, any character, including a space, following the closing quote but preceding the comma (like
"Word",
) will cause the row to be skipped.
Click
Next
and enter the Hash Generation and Sanitization Parameters:
Select the appropriate options for sanitization and hash generation operations:
Sanitization (Name Column):
Sanitize the content by checking the Name Column checkbox. (Default: Unchecked). The Sanitization Process performs the following actions:
One character:
The cell will be marked as invalid if it contains only one character.
Digits:
Cells containing digits will be marked as invalid.
Stopwords:
Cells that match a stopword from the list will be marked as invalid (This works only if the Remove stopwords checkbox is checked).
Non-alphanumeric characters:
Remove all special characters to validate the cell.
Hash Generation is divided into two parts:
Normalization:
Select the value from dropdown to normalize the data value. (Default: None)
Create Dictionary:
Select value from dropdown to create dictionary of unique values for selected field that can be used in DLP rule in netskope tenant. (Default: None)
Remove Stopwords:
Mark as checked if you want to remove certain stopwords as part of the sanitization process. (Default:Unchecked) Ensure that Name Column is checked for the applicable field to reflect the changes.
Note
Use Normalization parameter to normalize the fetched results. For example, a number such as 123-45-6789 or 123 45 6789 will be treated as 123456789. Number normalizations ignore characters such as dots, dashes and spaces. A string normalization ignores the case sensitivity of the letters.
Use the Create Dictionary option only when necessary, as this operation is resource-intensive and may impact system performance. Choose this option thoughtfully for optimal efficiency.
Click
Next
. Preview the sanitization sample output by clicking
Preview Good File
or
Preview Bad File
.
If you are using the plugin with sanitization ON then the performance may be differ due to extra processing.
Proceed without sanitization:
Uncheck this option to proceed with sanitization. (Default: Checked)
All the data will be under consideration for hash generation if this option is
Unchecked
; otherwise, only the Good File content will be part of the hash generation.
Click Save. You will be redirected to
Exact Data Match > Plugins
page where you can see your configured plugin.
Configure an EDM Sharing Configuration for MySQL
A sharing configuration is used to share the generated EDM hashes with the destination platform. To share EDM hashes with your Netskope tenant, create a sharing configuration using these steps:
Go to
Exact Data Match > Sharing
and click
Add Sharing Configuration
.
Configure the sharing parameters:
Source Configuration:
Select the configured MySQL EDM plugin.
Destination Configuration:
Select a destination where EDM Hash will be shared.
Target:
The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate the MySQL EDM Plugin
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate the Pull
To validate the pulling of the configured plugin in Cloud Exchange, go to
Settings > Logging
and search for the MySQL EDM plugin logs.
You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
The status values are as follows:
Scheduled:
Indicates that the sharing has been configured, and the pull and push operations are waiting in the queue for processing.
Generating Hash:
Indicates that the hash generation process has started. This stage includes fetching > validating > sanitization (if enabled) > generating hash.
Uploading Hash:
Indicates that uploading the hash to the destination configuration has started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
Checking the apply status of hashes to the destination configuration.
Apply In Progress:
The hash process has started and is in progress on the destination.
Completed:
Indicates that the hash file has been pushed successfully to the destination configuration.
Failed:
Indicates that the final result of the action has failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Shared EDM hashes can be verified from the logs available at
Logging
in Cloud Exchange:
Validate the Push to your Netskope Tenant
To ensure the push of EDM hashes on the Netskope Tenant from the cloud exchange:
Log in to your Netskope Tenant, go to
Policies > DLP
.
Click
Edit Rules
and select
Data Loss Prevention
.
On the
Exact Match
tab, a list of files is shown.
Troubleshooting the MySQL Plugin
Unable to configure the MySQL plugin
If you are unable to configure the MySQL EDM plugin, it could be due to one of the following reasons:
Incorrect credentials provided.
The user doesn’t have required permissions.
Incorrect hostname/server IP address.
Incorrect Database Name.
What to do
:
Make sure to provide the correct credentials.
Make sure that the user has the required permissions for the database and table.
Make sure that the correct hostname/server IP.
Make sure that the database name is correct.
CSV file not found or access denied
If you receive errors about file not found or access denied:
What to do
:
Verify the CSV file path is correct and the file exists.
Ensure the SSH user has read permissions for the file.
Check if the file is not locked by another process.
Hash generation fails or takes too long
If hash generation fails or performance is poor:
What to do
:
Check available disk space on Cloud Exchange (ensure at least 2x CSV file size).
Reduce CSV file size or split into smaller files.
Disable sanitization if not required to improve performance.
Monitor system resources during processing.
Known Behaviors
Sanitization can reduce processing speed by approximately 65% but improves data quality.
Dictionary creation is resource-intensive and should only be used when necessary.
The plugin creates temporary files during processing that are automatically cleaned up.
SSH connection timeouts may occur with very large files; consider increasing timeout values.
Memory usage scales with CSV file size; monitor system resources during large file processing.
Limitations
Each Netskope tenant has a limit of handling up to 5 staging files. If this maximum limit is reached, you may encounter the following error while sharing hashes:
EDM Netskope Exact Data Match [EDM Netskope] Received exit code 400, Error occurred while uploading edm hashes of configuration Linux EDM to the configuration EDM Netskope.
To resolve this error, you have to delete the existing files from staging.
In this Topic
MySQL Plugin for Exact Data Match

---
## Microsoft SQL Plugin for Exact Data Match
**URL:** https://docs.netskope.com/en/microsoft-sql-plugin-for-exact-data-match/
**Last Modified:** 2026-06-05T02:18:14+00:00
**Scraped:** 2026-08-23T07:15:46.886862+00:00

Microsoft SQL Plugin for Exact Data Match - Netskope Technical Documentation
Microsoft SQL Plugin for Exact Data Match
Release Notes
1.1.0
Added
Added support for removing quotes from the pulled data.
Changed
Updated loggers and tooltips.
1.0.1
Fixed
Fixed plugin validation with respect to CSV path.
Fixed Sanity Step level validation.
1.0.0
Added
Initial release.
This document explains how to configure the Microsoft SQL EDM plugin v1.1.0 with the Exact Data Match module of the Netskope Cloud Exchange platform. This plugin is used to pull raw data from configured Microsoft SQL server to generate EDM hashes.
Prerequisites
To complete the configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Exact Data Match plugin
already configured.
Microsoft SQL server setup
Microsoft SQL Server database user with read-only (Select) access to fetch the data.
Ensure that at least twice the size of the data is available as free storage. For example, to process a 3 GB CSV file/ DB table efficiently, you should have approximately 7–8 GB of available disk space.
Microsoft SQL Server EDM Plugin Support
This plugin is used to pull raw data from configured Microsoft SQL server to generate EDM hashes. The plugin supports advanced data sanitization, normalization, and hash generation capabilities to ensure data quality and security compliance.
Feature
Support
Pull
Yes
Push
No
Microsoft SQL Database Permissions
Permission Type
Requirement
User Read Access to Mentioned Database
Required
Microsoft SQL Database Read Permissions
Required
Database Port Access
Required
Required Permissions
Database user must have read permissions for the specified database.
Network connectivity to the Microsoft SQL server on the configured port.
Sufficient disk space on Cloud Exchange for temporary file processing.
API Details
List of Libraries Used to Fetch Database Records
This plugin uses Python libraries and Microsoft SQL driver to establish secure connections to MSSQL Database and transfer tables raws by executing SQL query.
Library: sqlalchemy, pyodbc and unixodbc (System Package)
Usage: SQLAlchemy is the Python SQL toolkit provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language to execute SQL queries. PyODBC Connector/Python enables Python programs to access Microsoft SQL databases.
Create Client Connection
from sqlalchemy import create_engine
eng = create_engine(
       connection_string, connect_args={"connect_timeout": CONNECTION_TIMEOUT,”TrustServerCertificate”:”yes”}
)
Execute SQL query with Read-Only Session
with eng.connect() as connection:
    # used to stop user from executing any database modification query.
    query = text(config["query"])
    result = connection.execute(query)
Generate CSV File from fetched records in batches
while True:
    rows = result.fetchmany(BATCH_SIZE)
    if not rows:
        break  # No more rows to fetch
    self.store_data_to_csv(rows, csv_path)
Performance Matrix
Here is the performance reading conducted for fetching and sanitizing ~1M Rows (25 columns, per column ~50 characters long string,1.3 GB size, Avg Column Uniqueness: ~96%, Avg Row Uniqueness: ~96%) from Database table on a Large CE instance with these specifications:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Database table data fetched from Microsoft SQL without sanitization
~5.7K rows/sec
For CE instance disk space, refer to this
documentation
.
Workflow
Create a user on Microsoft SQL server with read permissions.
Configure Microsoft SQL EDM Plugin.
Configure sharing between Microsoft SQL EDM Plugin and EDM Netskope plugin.
Validate the Microsoft SQL plugin.
Watch a Video
Click play to watch a video.
Configure the Microsoft SQL Server
Create a user
Follow the below steps to create the user on Microsoft SQL Database:
Log in to the Microsoft SQL Server instance and open the SQL terminal.
Execute the following commands, or follow this
guide
to create users with the necessary read-only (Select) privileges.
Create Login:
For SQL Server Authentication:
Create login
<YourLoginName>
with password=
<YourPassword>
;
For Windows Authentication:
CREATE LOGIN [
<DomainName>
\
<YourLoginName>
] FROM WINDOWS;
Switch to the Target Database and create a User:
USE
<YourDatabaseName>
;
CREATE USER
<YourUserName>
FOR LOGIN
<YourLoginName>
;
Grant Read-Only (SELECT) Permissions by Adding User to db_datareader Role:
ALTER ROLE db_datareader ADD MEMBER
<YourUserName>
;
Note
Replace
<YourLoginName>
and
<YourPassword>
with your actual login name and password.
Replace
<YourUserName>
with the name you want to assign to the database user.
Replace
<YourDatabaseName>
with the actual name of the database.
For Windows authentication, use the correct format: [domain\username].
Configure the Microsoft SQL EDM Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Microsoft SQL v1.1.0 (
EDM
) plugin.
Enter the Basic Information:
Configuration Name:
Enter a name appropriate for your plugin.
The configuration name you provide will be used to give the name to the generated hash file to share with the Netskope tenant. Be aware that if you later delete this configuration and create a new one with the same name, the hash file may already exist in the Netskope tenant. In such cases, attempting to push the hash file to the tenant will result in an error, as the file with the same name already exists. Consider using a unique name to avoid this issue.
Sync Interval:
Interval to pull the data from this plugin source. Default value is 12 hours. (Default: 12 hours)
Click
Next
and enter the Configuration Parameters:
Server IP/Hostname:
IP address or Hostname where the Microsoft SQL server is located.
Username:
Microsoft SQL database username to access the server. Ensure that it is a valid username with the read-only permission.
Password:
Password associated with the provided database username.
Database Name:
Microsoft SQL database name from which the data is to be retrieved. Ensure that the database name is spelled correctly, as database names are case-sensitive.
Port:
Enter the TCP port number that the Microsoft SQL database is running.
Query:
Microsoft SQL database query for which the data is to be retrieved to generate the EDM hashes. Ensure that the query is validated and read-only.
Remove Quotes:
Enable this if your data file encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped. Helpful for CSVs exported from databases.
By default, quotes are treated as literal text. Enable Remove Quotes toggle if your CSV uses double quotes to encapsulate fields that contain commas (like
"123 ABC Street, Suite 100"
). This ensures the field is treated as a single column. Note that this mode requires strict CSV formatting. If a field starts with a quote, any character, including a space, following the closing quote but preceding the comma (like
Word",
), this will cause the row to be skipped.
Click
Next
and enter the Hash Generation and Sanitization Parameters:
Select the appropriate options for sanitization and hash generation operations:
Sanitization (Name Column):
Sanitize the content by checking the Name Column checkbox. (Default: Unchecked). The Sanitization Process performs the following actions:
One character:
The cell will be marked as invalid if it contains only one character.
Digits:
Cells containing digits will be marked as invalid.
Stopwords:
Cells that match a stopword from the list will be marked as invalid (This works only if the Remove stopwords checkbox is checked).
Non-alphanumeric characters:
Remove all special characters to validate the cell.
Hash Generation is divided into two parts:
Normalization:
Select the value from dropdown to normalize the data value. (Default: None)
Create Dictionary:
Select value from dropdown to create dictionary of unique values for selected field that can be used in DLP rule in netskope tenant. (Default: None)
Remove Stopwords:
Mark as checked if you want to remove certain stopwords as part of the sanitization process.(Default:Unchecked) Ensure that Name Column is checked for the applicable field to reflect the changes.
Note
Use Normalization parameter to normalize the fetched results. For example, a number such as 123-45-6789 or 123 45 6789 will be treated as 123456789. Number normalizations ignore characters such as dots, dashes and spaces. A string normalization ignores the case sensitivity of the letters.
Use the Create Dictionary option only when necessary, as this operation is resource-intensive and may impact system performance. Choose this option thoughtfully for optimal efficiency.
Click
Next
. Preview the sanitization sample output by clicking
Preview Good File
or
Preview Bad File
.
If you are using the plugin with sanitization On, then the performance may be differ due to extra processing.
Proceed without sanitization:
Uncheck this option to proceed with sanitization. (Default: Checked)
All the data will be under consideration for hash generation if this option is
Unchecked
; otherwise, only the Good File content will be part of the hash generation.
Click Save. You will be redirected to
Exact Data Match > Plugins
page where you can see your configured plugin.
Configure an EDM Sharing Configuration for Microsoft SQL
A sharing configuration is used to share the generated EDM hashes with the destination platform. To share EDM hashes with your Netskope Tenant, create a sharing configuration using these steps:
Go to
Exact Data Match > Sharing
and click
Add Sharing Configuration
.
Configure the sharing parameters:
Source Configuration:
Select the configured EDM Microsoft SQL plugin.
Destination Configuration:
Select a destination where EDM Hash will be shared.
Target:
The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate the Microsoft SQL EDM Plugin
Cloud Exchange only stores sensitive pulled data CSV/Database files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate the Pull
To validate the pulling of the configured plugin in Cloud Exchange, go to
Settings > Logging
and search for the Microsoft SQL EDM plugin logs.
You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
If a sharing configuration has been established for the source plugin, its status can be monitored on the
Sharing and Upload Management
page.
The status values are as follows:
Scheduled:
Indicates that the sharing has been configured and the pull and push operation are still waiting in the queue for processing.
Generating Hash:
Indicates that the generating hash process has been started.At this stage, in the background fetching > validating > sanitization(if opted for) > generating hash staged will be included.
Uploading Hash:
Indicates that uploading hash to the destination configuration has been started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
At this stage, checking the apply status of hashes to the destination configuration.
Apply In Progress:
This represents that the hash process is started and in progress state on the destination.
Completed:
Indicates that hash file has been pushed successfully to destination configuration.
Failed:
Indicates that the final result of the action has been failed to execute.The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Shared EDM hashes can be verified from the logs available at
Logging
in Cloud Exchange:
Validate the Push to your Netskope Tenant
To ensure the push of EDM hashes on the Netskope tenant from Cloud Exchange:
Log in to your Netskope tenant, go to
Policies > DLP
.
Click
Edit Rules
and select
Data Loss Prevention
.
On the
Exact Match
tab, a list of files is shown.
Troubleshooting the Microsoft SQL Plugin
Unable to configure the MS SQL plugin
If you are unable to configure the Microsoft SQL plugin, it could be due to one of the following reason:
Incorrect credentials provided.
The user does not have required permissions.
Incorrect hostname/server IP.
Incorrect Database Name.
What to do:
Make sure to provide correct credentials.
Make sure that the user has the required permissions for database and table.
Make sure that the correct hostname/ server IP.
Make sure that database name is correct.
Hash generation fails or takes too long
If hash generation fails or performance is poor.
What to do:
Check available disk space on Cloud Exchange (ensure at least 2x CSV file size).
Reduce file/table size or split into smaller tables.
Disable sanitization if not required to improve performance.
Monitor system resources during processing.
Known Behaviors
Sanitization can reduce processing speed by approximately 65% but improves data quality.
Dictionary creation is resource-intensive and should only be used when necessary.
The plugin creates temporary files during processing that are automatically cleaned up.
SSH connection timeouts may occur with very large files; consider increasing timeout values.
Memory usage scales with CSV file size/table size; monitor system resources during large file processing.
In this Topic
Microsoft SQL Plugin for Exact Data Match

---
## Netskope EDM Forwarder/Receiver Plugin for Exact Data Match (Beta)
**URL:** https://docs.netskope.com/en/netskope-edm-forwarder-receiver-plugin-for-exact-data-match/
**Last Modified:** 2026-02-14T02:11:10+00:00
**Scraped:** 2026-08-23T07:15:48.071309+00:00

Netskope EDM Forwarder/Receiver Plugin for Exact Data Match (Beta) - Netskope Technical Documentation
Netskope EDM Forwarder/Receiver Plugin for Exact Data Match (Beta)
This document explains how to configure the Netskope EDM Forwarder/Receiver plugin v1.0.0 with the Exact Data Match (EDM) module in the Netskope Cloud Exchange platform. The plugin operates in
push mode
, sending EDM hashes generated by the EDM 3rd-Party plugin configuration from one Netskope Cloud Exchange instance to another. A
Receiver
configuration can only be used as a destination, while a
Forwarder
configuration can only be used as a source for sharing.
Prerequisites
To complete the configuration, you need:
The Exact Data Match module enabled on two Cloud Exchange tenants.
The
Tenant plugin
configured on both Cloud Exchange tenants.
A
Receiver
type plugin of Netskope Forwarder/Receiver Plugin configuration in the first Cloud Exchange tenant.
A
Forwarder
type plugin of Netskope Forwarder/Receiver Plugin configuration and a supported third-party EDM plugin configured and available for integration on the second Cloud Exchange tenant.
For systems with large specifications (32 GB RAM and 16-core CPU), ensure that at least twice the size of the CSV file is available as free storage. For example, to process a 3 GB CSV file efficiently, you should have approximately 7–8 GB of available disk space.
Netskope EDM Forwarder/Receiver Plugin Support
This plugin shares EDM hashes from one Cloud Exchange tenant to another Cloud Exchange tenant. Make sure that you configure the
Receiver
configuration in the destination Cloud Exchange tenant before creating the
Forwarder
configuration in source Cloud Exchange tenant.
Feature
Support
Pull
Yes
Push
Yes
Required Permissions
These permissions are needed for the plugin configuration: To work with
Forwarder
type plugin configuration, the Exact Data Match Module level read/write permission is required.
Performance Matrix
Here is the performance reading conducted for pushing hashes for ~1M rows (25 columns, Per column ~50 Characters Long String) Data on a Large Cloud Exchange instance with these specifications.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Hashes Forwarded From Source to Netskope EDM Plugin
~ 10 minutes
Hashes Received From Netskope EDM Forwarder to Netskope EDM Receiver > Netskope Tenant
~7 minutes
Workflow
Get credentials for  Netskope EDM Forwarder/Receiver Plugin
Configure Netskope EDM Forwarder/Receiver Plugin on both the Cloud Exchange instance.
Configure sharing between a 3rd-party EDM Plugin and Netskope Forwarder/Receiver Plugin with the
Forwarder
type.
Configure sharing between Netskope Forwarder/Receiver Plugin with
Receiver
type and Netskope EDM Plugin.
Check the status of the configured Sharing.
Validate the Netskope EDM Forwarder/Receiver Plugin.
Watch a Video
Click play to watch a video.
The Netskope forwarder/receiver workflow involves two Cloud Exchange instances.
The first Cloud Exchange instance pulls data from a third-party plugin and generates hash files using the Netskope Forwarder/Receiver plugin with the
Forwarder
plugin type.
These generated hashes are then sent to another Cloud Exchange instance which contains the Netskope Forwarder/Receiver plugin with the
Receiver
plugin type.
The
Receiver
Netskope Forwarder/Receiver plugin will store incoming hashes that will be used for sharing with the Netskope Tenant.
Both CE instances must have the Netskope tenant configured, as it is a mandatory configuration starting with Cloud Exchange v6.0.0.
Get Credentials for the Netskope Forwarder/Receiver Plugin
In order to configure the the Netskope Forwarder/Receiver plugin with a Forwarder plugin type in the first Cloud Exchange instance, follow these steps to generate API credentials in a second Cloud Exchange instance:
Currently, Netskope Forwarder/Receiver plugin supports Username and Password and Token-based authentication methods.
Configure a Username and Password
Go to
Settings > Users > Users
Tab.
Click
Create New User
.
Ensure the user has Exact Data Match Read and Write permissions.
Enter the details and click
Save
.
This user credential will be used to configure the Forwarder type plugin.
Configure an API Token
Log in to Cloud Exchange using the newly created user.
Go to
Settings > Users > API Tokens
(tab).
Click
Create New Token
.
Ensure the user creating the API token has Exact Data Match Read & Write permission, as the token will have the same permission as a logged-in user.
Enter the details and click
Save
.
The API Token will be created.
Copy the Client ID and Client Secret. These will be used to configure the Forwarder type plugin.
Configure Netskope EDM Forwarder/Receiver Plugins
Follow these two steps in order to setup Netskope Forwarder/Receiver EDM plugin on both Cloud Exchange instances.
Configure a Netskope EDM Forwarder/Receiver Plugin as a Receiver
In the first Cloud Exchange tenant, go to
Settings > Plugin Store
.
Search for and select the
Netskope EDM Forwarder/Receiver
plugin box.
For Basic Information, enter a Configuration Name and select
Receiver
as the Plugin Type.
Click
Save
.
You will be redirected to the
Exact Data Match > Plugins
page, where you can see your configured plugins.
Configure a Netskope EDM Forwarder/Receiver Plugin Configuration as a Forwarder
In a second Cloud Exchange tenant, go to
Settings > Plugin Store
.
Search for and select the
Netskope EDM Forwarder/Receiver
plugin box.
For Basic Information, enter a Configuration Name and select
Forwarder
as the Plugin Type. Click
Next
.
For Authentication Method, select one of these options: Username & Password or Token. Click
Next
.
Based on Authentication Method chosen, enter the Configuration Parameters:
Configuration Parameters for the Username and Password method:
Netskope CE IP/Hostname with Port
: Provide IP Address of the Cloud Exchange tenant to share the data.
Username
: Username created for the destination Cloud Exchange tenant.
Password
: Password created for the destination Cloud Exchange tenant.
Receiver Configuration Name
: Receiver’s Configuration name created in the destination Cloud Exchange tenant.
Configuration Parameters for the Token method:
Netskope CE IP/Hostname with Port
: Provide IP Address of the Cloud Exchange tenant to share the data.
Client ID
: Client ID for the API Token created on the destination Cloud Exchange tenant.
Client Secret
: Client Secret for the API Token created on the destination Cloud Exchange tenant.
Receiver Configuration Name
: Receiver’s Configuration name created in the destination Cloud Exchange tenant.
Click
Save
.
You will be redirected to
Exact Data Match > Plugins
page, where you can see your configured plugins.
Configure Sharing between a 3rd-Party EDM Plugin and the Netskope Forwarder/Receiver Plugin with the Forwarder Type
In the second Cloud Exchange tenant, configure sharing between a 3rd-party EDM plugin to Netskope Forwarder Plugin:
On the Sharing Configuration page, select a 3rd-party plugin as a source configuration, and select the Netskope Forwarder Plugin configuration as a destination configuration. Target value will be set automatically.
Go to
Exact Data Match > Sharing
.
Click
Add Sharing Configuration
.
Click
Save
.
Configure Sharing for the Netskope Forwarder/Receiver Plugin with the Receiver Type and Netskope EDM Plugin
In a second Cloud Exchange Instance, follow these steps to share generated hashes received from first Cloud Exchange tenant:
Go to the
Exact Data Match > Sharing
.
Click
Add Sharing Configuration
.
On the Sharing Configuration page, select the Netskope Receiver Plugin as a source configuration, and select the Netskope EDM Plugin configuration as a destination configuration. The Target value will be set automatically.
Click
Save
.
Validate the Netskope Forwarder/Receiver
EDM Plugin
This sections contains validation of Netskope Forwarder/Receiver EDM Plugin in both of the Cloud Exchange tenants.
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate the Netskope EDM Forwarder Type Plugin
In the first Cloud Exchange tenant, go to
Exact Data Match > Sharing and Upload Management
, where you’ll be able to see a status for all the configured sharing.
Go to
Settings > Logging
and search for the Netskope Forwarder plugin logs.You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
EDM Netskope EDM Forwarder/Receiver [Netskope EDM Forwarder] Executed push method for configuration 'Netskope EDM Forwarder' successfully.
Validate the Netskope EDM Receiver Type Plugin
In the second Cloud Exchange tenanat, Go to
Exact Data Match > Sharing and Upload Management
, where you’ll be able to see a status for all the configured sharing.
Go to
Settings > Logging
and search for the Netskope Forwarder plugin logs.You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
To ensure the push of EDM hashes on the Netskope Tenant from the cloud exchange, go to
Policies > DLP.
Click
Edit Rules
and go to
Exact Match
tab.
In Sharing and Upload Management Page, All of the possible status are:
Scheduled:
Indicates that the sharing has been configured and the pull and push operation are still waiting in the queue for processing.
Generating Hash:
Indicates that the generating hash process has been started. At this stage, in the background fetching > validating > sanitization(if opted for) > generating hash stages will be included.
Uploading Hash:
Indicates that uploading hash to the destination configuration has been started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
At this stage, checks hashing apply status to the destination configuration.
Apply In Progress:
This represents that the hash process is started and in progress state on the destination.
Completed:
Indicates that hash file has been pushed successfully to destination configuration.
Failed:
Indicates that the action final result failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Troubleshooting
the EDM Forwarder/Receiver Plugin
If the user is unable to configure the forwarded plugin, it may be due to one of these reasons:
Max retries exceeded with URL.
Incorrect Client ID/Client Secret or Username/Password.
What to do:
To solve these issue, follow these steps:
Ensure that the Cloud Exchange receiver instance is up and running.
Make sure to provide correct credentials.
In this Topic
Netskope EDM Forwarder/Receiver Plugin for Exact Data Match (Beta)

---
## Integrating with DLP on Demand
**URL:** https://docs.netskope.com/en/integrating-with-dlp-on-demand/
**Last Modified:** 2026-05-18T15:00:38+00:00
**Scraped:** 2026-08-23T07:16:09.178644+00:00

Integrating with DLP on Demand - Netskope Technical Documentation
Integrating with DLP on Demand
Install the DLP on Demand appliance. For the detailed installation steps, see
/en/dlpondemandconfig
.
After the DLP on Demand appliance is successfully installed, access the
Netskope
AI Gateway Configuration Wizard
using the
CLI interface
.
In the
Netskope
AI Gateway Configuration Wizard
, select
Configure Content Inspection Services.
In the
Configure Content Inspection Services
page, select
Data Loss Prevention Service
.
Data Loss Prevention Service
page allows you to select any of the three options:
Configure DLP Service Certificate <link>
Configure DLP Service Host<link>
Delete DLP Service Host Configuration<link>
Ensure you configure the DLP Service Certificate first.
Configure the DLP Service Certificate
In the
Data Loss Prevention Service
page, select
Configure DLP Service Certificate
.
In the
Configure DLP Service Certificate
page, copy the certificate from the DLPoD appliance and paste the
Enter new certificate
prompt. This is the certificate that is installed on the DLPoD appliance. For more details on certificate configuration DLPoD, see,
/en/replacing-the-self-signed-certificate-on-your-appliance
.
Ensure you copy the certificate within the header “—–BEGIN CERTIFICATE—–” and the footer “—–END CERTIFICATE—–”.
Press
Enter
to submit the certificate.
When the certificate is valid, the system displays the certificate details. If validation fails, press
R
to retry the configuration.
Configure the DLP Service Host
After successful installation of the DLP Service certificate, follow the steps below to configure the DLP service host.
In the
Data Loss Prevention Service
page, select
Configure DLP Service Host
.
In the
Configure DLP Service Host
page, under
Enter new Host URL
prompt, enter your DLP backend URL (for example:https://dlp.company.internal).
Press
Enter
to save the DLP service host.
This saved DLP service host facilitates the internal DLP integration.
Delete DLP Service Host Configuration
At any point of time if you wish to remove or reset the DLP host configuration, follow the steps below:
In the
Data Loss Prevention Service
page, select
Delete DLP Service Host Configuration
.
In the
Delete host configuration
page, Press
y
to confirm the deletion and
n
to cancel it.
Once the certificate is successfully installed and the host configurations is complete, the Netskope AIG facilitates the following automated workflow:
The Netskope AIG validates the DLP backend using the stored certificate.
The Netskope AIG directs DLP inspection requests to the configured host URL.
Internal DLP integration transitions to an active and enabled state.
In this Topic
Integrating with DLP on Demand

---
## DLP Policies for AI Traffic
**URL:** https://docs.netskope.com/en/dlp-policies-for-ai-traffic/
**Last Modified:** 2026-05-18T15:00:30+00:00
**Scraped:** 2026-08-23T07:16:30.436690+00:00

DLP Policies for AI Traffic - Netskope Technical Documentation
DLP Policies for AI Traffic
You can define a DLP policy by configuring traffic matches on various criteria. You can create policy groups and add multiple policies to the group. A default policy group is present.
Create New DLP Policy Group
To create a new DLP policy group, follow the steps below.
Log in to the Netskope tenant UI and go to
Policies
>
AI Gateway
.
In the
AI Gateway
page, click the
DLP
tab and click
New Policy Group
.
In the
New DLP Group
page, enter a name for the group in the
Group Name
parameter.
Choose the position of the new policy group by selecting a group from the
Before policy group
or
After policy group
lists respectively.
Click
Create
.
Create New DLP Policy
To create a new access policy, follow the steps below.
Log in to the Netskope tenant UI and go to
Policies
>
AI Gateway
.
In the
AI Gateway
page, click the
DLP
tab and click
New Policy
.
In the
New DLP Policy
page, create a policy that matches one (or more) of the following criteria :
Token Group
AI Provider and Model
Activity – Prompt, Response, Upload, and Download.
From the
Add Exclusion Criteria Group
list, choose the token group that you want to exclude from the match criteria. For example, you want to match against all openai AI Providers, but not for traffic with token group admin. In that case you can specify this exclusion criteria by selecting
Add Exclusion Criteria Group
, choose
Token Group
and select the required token group from the drop down.
Under
Profile
, select a
DLP Profile
from the list.
From the
Action
parameter, select the enforcement action to be applied when traffic matches your specified criteria:
Monitor: Logs the traffic activity for visibility and allows the request to proceed to the subsequent policy.
Block: Immediately terminates the connection and drops the traffic.
Replace: Intercepts the response and replaces the content with a custom, administrator-defined message.
Specify the name of the policy, description, the policy group that it should be part of, and the position of the policy within that policy group.
Click
Save
and apply changes to your creation.
In this Topic
DLP Policies for AI Traffic

---
## Understanding the DSPM DLP Profiles & Rules Screen
**URL:** https://docs.netskope.com/en/understanding-the-dspm-dlp-profiles-rules-screen/
**Last Modified:** 2026-04-08T22:49:48+00:00
**Scraped:** 2026-08-23T07:17:09.729013+00:00

Understanding the DSPM DLP Profiles & Rules Screen - Netskope Technical Documentation
Understanding the DSPM DLP Profiles & Rules Screen
Overview
The
DLP Profiles & Rules
screen consolidates classification visibility in Netskope DSPM and replaces the previous
Sensitive Data Type
management screen.
Use this screen to view any DLP Profile or Rule that is currently relevant to your configuration or has historically classified data within your environment.
This article explains:
How the
DLP Profiles
tab determines which profiles are listed.
How the
DLP Rules
tab determines which rules are listed.
How
Data Tags
behave when associated with DLP Profiles.
DLP Profiles Tab Behavior
This tab lists DLP Profiles based on specific criteria. A profile appears in this list if it meets
either
of the following conditions:
Actively Selected:
The profile is currently selected within the
DSPM Discovery Profile
. It appears here even if it has not yet classified any data.
Previously Applied:
The profile has successfully classified data in the past, even if you have removed it from the current Discovery Profile. This ensures visibility into:
Objects classified under older versions of the Discovery Profile.
Objects classified externally (e.g., via
DSPM for SaaS Apps
), which may use a separate rule configuration.
This view helps you distinguish between profiles that are in-scope for
current
scanning and those that are relevant
historically
because they have already classified data objects.
DLP Rules Tab Behavior
The
DLP Rules
tab filters content based on successful matches.
Displayed:
Rules that have successfully applied classification to
at least one object
.
Hidden:
Rules that exist in your configuration but have
never
resulted in a classification match.
This filter helps you focus on rules that are actively contributing to your DSPM inventory and risk posture.
Data Tags on DLP Profiles
When you associate a
Data Tag
with a
DLP Profile
from this screen, the system enforces a dynamic relationship across your inventory.
Adding a Data Tag:
If you add a Data Tag to a profile, the system automatically applies that tag to:
All objects previously classified by that profile.
Any new objects classified by that profile in the future.
Removing a Data Tag:
If you remove a Data Tag from a profile, the system automatically removes that tag from:
All objects and fields previously classified by that profile.
This behavior ensures that changes at the profile level are
automatically reflected
across all relevant objects, eliminating the need to re-scan or manually retag data.
If you want to know more details on creating and ingesting tags, see
Manage DSPM Data Tags
.
In this Topic
Understanding the DSPM DLP Profiles & Rules Screen

---
## DLP AISecOps Agent
**URL:** https://docs.netskope.com/en/aisecops-dlp-agent/
**Last Modified:** 2026-07-23T19:16:29+00:00
**Scraped:** 2026-08-23T07:17:19.109603+00:00

DLP AISecOps Agent - Netskope Technical Documentation
DLP AISecOps Agent
This feature is licensed. See your account executive or Netskope’s sales team to enable this feature in your tenant.
The
Netskope DLP AISecOps Agent
is built for one purpose: to give data security analysts their time back.
The agent transforms raw data into a streamlined incident-to-resolution pipeline through five key stages:
Signal Ingestion
: Collects millions of DLP signals across cloud, web, email, and endpoints to eliminate blind spots.
Analysis & Clustering
: Filters noise and groups related incidents into a single case centered around specific users, data, applications, or devices.
Enrichment
: Automatically enriches the cases with context around identity, application, device & data.
Recommendation
: Provides a clear verdict and risk score based on business context, suggesting the best next steps.
Resolution
: Analysts can execute actions such as revoking sharing or muting benign activity directly from the Netskope One Orchestrator.
For more details:
Case Creation
Configuration
Overview
To begin using the
Netskop DLP AISecOps Agent
, log into the Netskope admin console and click
AISecOps
.
The UI will give insight into
Total New Cases, Critical Risk Cases, Average Case Age,
and
Total Views
. The
Overview
can be filtered by the timeframe using the drop-down box at the top right.
The
Incident-to-Resolution Pipeline
provides the complete case lifecycle from detection to close. Your
Alerts
will flow into
Incidents
which are then grouped into cases and can be further filtered based on severity.
Cases
Cases are a construct of one or more incidents that have been grouped based on customizable rules.
You can filter these cases along the top bar based on
Name, Status, Risk Level, Assigned Analyst, Recency,
and
Timeframe.
Clicking on a case will take you to the case details where you can view all the incidents which comprise the case. From here, you can:
Re-investigate
– Re-investigate an already investigated case.
Assign
– Assign a case to an analyst
Download
–
Close case
– Close the case out.
Investigate
– Launch an investigation to dig into the incidents. The Agent will gather all the evidence across the Netskope platform and provide a risk assessment and recommendation for remediation.
You can also perform bulk actions like
Assign Cases
or
Close Cases
when you select multiple cases.
Along the top, you will see
Similar Cases
,
Analysis
,
Incidents
, and
Investigation Trail
.
The
Incidents
tab will let you click on an
Incident
and get additional details on the
Incident.
You can also click
View in Incident Management
to get even more detail.
The
Similar
Cases
tab will list cases which are similar in nature.
The
Investigation Trail
tab will provide information on the investigation and also rename the case based on the findings.
All this information will be populated on the
Overview
tab after an investigation has been launched along with an
Executive Summary
and series of
Recommended Actions
.
You can also see
Suggested Remediations
.
For information on creating cases, see
Case Creation
.
Views
The Views tab contains two sections,
Data Loss
and
Insider Threat
.
Data Loss
The
Data Loss
sub-tab allows you to filter incidents by
Sanctioned Instances, Critical Severity, PCI Data, and PII Data
. These views provide additional granularity and allow analysts to monitor for any fluctuations in behavior across the organization.
Clicking on an insight will provide the analysts with more detail on any spikes in Incidents generated by specific user actions.
Insider Threat
This feature is currently in Beta and is separate from the AISecOps entitlement. Please contact your account executive or support@netskope.com for more information.
The Insider Threat page allows you create user watchlists for specific users or groups in order to monitor for malicious activity or active malware infections.
Clicking on a user will allow you to get analytics on their behavior and see cases associated with their activity
For more information, see
Views
.
In this Topic
DLP AISecOps Agent

---
## Granular Control and Data Loss Prevention (DLP)
**URL:** https://docs.netskope.com/en/granular-control-and-data-loss-prevention-dlp/
**Last Modified:** 2026-05-11T23:29:13+00:00
**Scraped:** 2026-08-23T07:17:25.011607+00:00

Granular Control and Data Loss Prevention (DLP) - Netskope Technical Documentation
Granular Control and Data Loss Prevention (DLP)
This topic provides an overview of how administrators can use the Skope IT application to monitor Model Context Protocol (MCP) communications in real-time. You will learn how to gain granular visibility into the interaction lifecycle—from initial handshakes to specific tool invocations and resource requests—to ensure compliance and detect potential threats. Furthermore, it explains how to analyze detailed event logs and initialization data to verify successful executions while ensuring sensitive data remains protected.
Contact your Netskope account team to enable Agentic Broker in your account. Additional licensing is required for Agentic Broker and DLP. Note, to create a DLP policy, the DLP add-on license is required if you do not have DLP enabled in your account.
Administrators can apply access controls to specific tool events and enforce DLP profiles to prevent the leakage of sensitive data.
Blocking Specific Events
Policies can be configured to block specific activity types, such as a “tool call request.” If a user attempts to utilize a restricted tool, the event is blocked, and the action is logged.
Applying DLP Profiles
You can apply standard DLP profiles (e.g., PII, PCI) to MCP traffic to inspect the content of tool requests.
Scenario:
A user invokes a tool to create a page in Notion.
Compliant Action:
If the content is generic, the tool runs successfully.
Non-Compliant Action:
If the user includes sensitive data (e.g., Name, ID, Role, Email) in the request, the action is blocked.
Administrators have the ability to detect sensitive data being exchanged between the client and teh server and apply access controls on it.
So let’s select a specific MCP server, once again the Notion MCP server. Select its activities.
To prevent sensitive data loss in a specific activity of all MCP Servers, in the Destination section select the specific Activity. The supported list of activities for DLP on MCP traffic are:
CallToolRequest
CallToolResult
CreateMessageResult
ElicitResult
GetPromptRequest
GetPromptResult
ReadResourceReqeust
ReadResourceResult
Download, Form Post, Upload activities do not apply to MCP Communications when you select MCP Category. They apply to cloud applications. Do not select these when creating a DLP policy for MCP traffic.
Select the action as “Block”. Select a DLP profile for personally identifiable information and PCI. Give the policy a name and save it.
Policy Configuration Interface:
The “Create Policy” screen. The “Category” dropdown is set to “MCP Server,” all activities are selected and the “Profile & Action” field is set to a DLP Profile to detect PII and PCI data. The Action is set to Block for a DLP policy with a user notification.
Run a tool in the notion MCP Server to create a page. Provide the title and content without any sensitive data.
VS Code:
Run the notion-create-pages tool without any sensitive data.
None of the tools are or tool calls are blocked.
Application Events Details Pane:
No alerts or block policies are enforced
Next run this same tool again to create another page called Employee Details.
VS Code:
Create a new page “Employee Details”
This time, for the content, provide some sensitive data such as name, ID, role, department, email, location, etc. of each employee in the content of that page.
VS Code:
Add personally identifiable information into the content of the page
When the tool call request is made to create the page, we get a user alert that says “This is a non-compliant action”.
User Block Notification:
A system pop-up alert stating “Non-compliant action,” triggered by the attempted upload of sensitive PII data.
Reviewing the application events we see why. This tool call request is blocked because of the DLP policy created earlier.
DLP Block:
Application Event showing the CallToolrequest blocked due to the Block Notion DLP policy.
DLP Block:
Application Event Details showing theCallToolrequest blocked due to the Block Notion DLP policy.
We can also see this in the list of alerts showing the action taken, the MCP server and the policy applied.
DLP Block Alert:
Alert showing the
CallToolrequest blocked due to the Block Notion DLP policy.
DLP Add-on Features
The following features are available for the DLP add-on licenses, DLP Standard (L2) and DLP Advanced (L3).
DLP Standard (L2):
Regulatory compliance templates including GDPR, PII, PCI, PHI, source code and many more.
Predefined data identifiers for a diverse set of file types, as well as options for custom Regular Expressions and dictionaries
Two AI/ML standard document classifiers (resumes, source code)
Read classification labels using DRM service
Incident management and remediation
DLP Advanced (L3):
Regulatory compliance templates including GDPR, PII, PCI, PHI, source code and many more.
Predefined data identifiers for a diverse set of file types, as well as options for custom Regular Expressions and dictionaries
File fingerprinting with degree of similarity, exact data matching and optical character recognition (OCR)
AI/ML classification for documents (tax forms, patents, source code, etc.) and images (desktop screenshots, whiteboards, passports, IDs, etc.)
Read and write classification labels using DRM service
Incident management and remediation
In this Topic
Granular Control and Data Loss Prevention (DLP)

---
## Configure Exact Data Match Sharing (Beta)
**URL:** https://docs.netskope.com/en/configure-exact-data-match-sharing/
**Last Modified:** 2026-04-28T07:04:39+00:00
**Scraped:** 2026-08-23T07:19:13.674084+00:00

Configure Exact Data Match Sharing (Beta) - Netskope Technical Documentation
Configure Exact Data Match Sharing (Beta)
You can create a configuration to share the Exact Data Match hashes of a file/data to the Netskope Tenant. This also facilitates hash sharing to Cloud Exchange to support isolation and/or cross region hash sharing to the Netskope Tenants.
Go to
Exact Data Match
.
Click
Sharing
. The Sharing configuration list is paginated with a count of 10 or less.
Click
Add Sharing Configuration
.
Select the source configuration and destination configuration. Click
Save
.
Optionally, you can trigger Manual Sync for the sharing configuration.
If needed, you can delete sharing configurations.
Monitor the Status of Sharing Configuration
View the hashing and upload status for Sharing Configuration to monitor their processing and ensure successful completion.  All entries with Source Type as a Plugin indicates status of the Sharing Configuration.
Go to
Exact Data Match > Sharing and Upload Management
page.
The following details will be shown for the sharing configuration.
Source:
The name of the source plugin configuration, or the name of the manually uploaded CSV file.
Target
: The name of the destination plugin configuration. Currently EDM supports sharing file hashes to Netskope Tenant only, hence the target field will be fixed and cannot be updated.
Source Type:
Plugin
or
Manual
.
Status:
Displays the current status of pull/push operation as following:
Scheduled:
Indicates that the sharing has been configured and the pull and push operation are still waiting in the queue for processing.
Generating Hash:
Indicates that the generating hash process has been started. At this stage, in the background
Fetching > Validating > Sanitization (if opted for) > Generating Hash
staged will be included.
Uploading Hash:
Indicates that uploading hash to the destination configuration has been started.
Upload Completed:
Indicates that hashes are uploaded to the Netskope Tenant for processing.
Checking Apply Status:
At this stage, checking the status of apply process of the hashes on the Netskope Tenant.
Apply In Progress:
Represents that the hash processing is started and in progress state on the Netskope Tenant.
Completed:
Indicates that hash file has been shared successfully to destination configuration.
Failed:
Indicates that the final result of the action has been failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Last Updated At:
Indicates last time the status has been updated for the sharing.
Last Shared At:
The last time when hashes were successfully shared with the destination configuration.
Click
Sync
to refresh and view the latest details in the table.
In this Topic
Configure Exact Data Match Sharing (Beta)

---
## Exact Data Match Module (Beta)
**URL:** https://docs.netskope.com/en/exact-data-match-module/
**Last Modified:** 2026-04-28T07:05:13+00:00
**Scraped:** 2026-08-23T07:19:17.369387+00:00

Exact Data Match Module (Beta) - Netskope Technical Documentation
Exact Data Match Module (Beta)
The Exact Data Match (EDM) module is a part of Cloud Exchange’s Data Protection (DLP) suite, designed to help organizations protect structured sensitive data. It works by generating cryptographic hashes of structured data (like from CSV files or database queries) and securely shares these hashes with the Netskope Tenant. These hashes are used to create real-time DLP policies that prevent sensitive data from leaving your network.
The module is designed exclusively for deployment within Standalone containers on RHEL and Ubuntu systems and is not supported on medium stack instances or high-availability (HA) clusters. These deployment restrictions are now enforced.
For optimal operation, the Exact Data Match module should be utilized in an isolated environment. Enabling the Exact Data Match module precludes the simultaneous use of additional modules.
For existing deployments undergoing upgrade or migration, the current state of the Exact Data Match module is preserved. If the module is already enabled, it will remain enabled after the upgrade. However, once the Exact Data Match module is disabled on Medium stack or HA deployments, it cannot be re-enabled.
In Cloud Exchange, go to
Settings > General
and enable the Exact Data Match (EDM) module.
Click play to learn how to set up Exact Data Match.
Exact Data Match Global Settings
Only write-access users of Cloud Exchange can change the Exact Data Match settings.
Go to
Settings > Exact Data Match
. Sensitive metadata collected from different sources are preserved for 7 days, by default. The file metadata that are older than the number of days specified will be deleted during the automatic cleanup.
You can change the time duration to keep the metadata per your requirements. When finished, click
Save
.
Configure 3rd-party Exact Data Match Plugins (Beta)
Configure Exact Data Match Sharing (Beta)
View Configured Exact Data Match Plugins (Beta)
Update Configured Exact Data Match Plugins (Beta)
Exact Match For Manual Upload (Beta)
In this Topic
Exact Data Match Module (Beta)

---
## Predefined DLP Profiles for DSPM
**URL:** https://docs.netskope.com/en/predefined-dlp-profiles-for-dspm/
**Last Modified:** 2026-05-05T21:45:08+00:00
**Scraped:** 2026-08-23T07:20:03.139551+00:00

Predefined DLP Profiles for DSPM - Netskope Technical Documentation
Predefined DLP Profiles for DSPM
Overview
The DSPM Discovery Profile includes a set of predefined Data Loss Prevention (DLP) Profiles covering common regulatory and compliance frameworks. Each profile contains:
File Content Rules:
For unstructured data classification.
Column Classification (CC) Rules:
For structured data classification.
Netskope DSPM applies these rules automatically during data store scans. To view or modify your active profiles, go to
Classification > DLP Profiles & Rules
and click
Edit Discovery Profile
.
Default Profiles in the Discovery Profile
The following predefined DLP Profiles are pre-selected in the default DSPM Discovery Profile.
Data Tags listed in the tables are associated with the profile itself, not with individual rules.
PCI Profiles
PFI Profiles
PHI Profiles
PII Profiles
DLP Profile Name
File Content Rules
Column Classification Rules
Data Tags
Payment Card Industry Data Security Standard (PCI-DSS)
– INTL-PAN-Exp-Address
– INTL-PAN-Exp-Address-CVV
– INTL-PAN-Exp-Name
– INTL-PAN-Exp-Name-Address
– INTL-PAN-Exp-Name-Address-CVV
– INTL-PAN-Exp-Name-CVV
– INTL-PAN-Name
– INTL-PAN-Name-CVV
– Payment Card Numbers
– Payment Card Numbers [w/o Terms]
PCI
DLP Profile Name
File Content Rules
Column Classification Rules
Data Tags
Australia Finance Data
– AU-Bank Account
– AU-PAN-Exp-Address
– AU-PAN-Exp-Address-CVV
– AU-PAN-Exp-Name
– AU-PAN-Exp-Name-Address
– AU-PAN-Exp-Name-Address-CVV
– AU-PAN-Exp-Name-CVV
– AU-PAN-Name
– AU-PAN-Name-CVV
– Taxpayer ID Numbers (AU)
– Taxpayer ID Numbers (AU) [w/o Terms]
PFI
Gramm-Leach-Bliley Act (GLB Act or GLBA), 1999
– INTL-PAN-Exp-Address
– INTL-PAN-Exp-Address-CVV
– INTL-PAN-Exp-Name
– INTL-PAN-Exp-Name-Address
– INTL-PAN-Exp-Name-Address-CVV
– INTL-PAN-Exp-Name-CVV
– INTL-PAN-Name
– INTL-PAN-Name-CVV
– US-Bank Account
– US-ITIN-Name
– US-ITIN-Name-Address
– US-SSN-Name
– US-SSN-Name-Address
– Bank Account Numbers (US)
– Bank Routing Numbers (US)
-Social Security Numbers (US)
– Taxpayer ID Numbers (US)
FTC, PFI
UK Financial Data
– UK-Bank Account
– UK-Bank-CC
– UK-PAN-Exp-Address
– UK-PAN-Exp-Address-CVV
– UK-PAN-Exp-Name
– UK-PAN-Exp-Name-Address
– UK-PAN-Exp-Name-Address-CVV
– UK-PAN-Exp-Name-CVV
– UK-PAN-Name
– UK-PAN-Name-CVV
– Taxpayer ID Numbers (UK)
– Taxpayer ID Numbers (UK) [w/o Terms]
PFI, PII
DLP Profile Name
File Content Rules
Column Classification Rules
Data Tags
Access to Medical Reports Act, 1988 (AMRA)
– UK-Name-DOB-Address-Medical
– UK-NHS-Name-Address-Medical
– UK-NHS-Name-DOB-Address-Medical
– UK-NHS-Name-DOB-Medical
– UK-NHS-Name-Medical
– UK-NIN-Name-Address-Medical
– UK-NIN-Name-DOB-Address-Medical
– UK-NIN-Name-DOB-Medical
– UK-NIN-Name-Medical
None
AMRA, PHI
Health Insurance Portability and Accountability Act (HIPAA), 1996
– US-Name-DOB-Address-Medical
– US-SSN-Name-Address-Medical
– US-SSN-Name-DOB-Address-Medical
– US-SSN-Name-DOB-Medical
– US-SSN-Name-Medical
– ICD Codes [w/o Terms]
– Medical Conditions [w/o Terms]
– Medicinal Products [w/o Terms]
– Social Insurance Numbers (US)
– Social Security Numbers (US)
HIPAA, PHI
Personal Health Information and Protection Act (PHIPA), 2004
– CA-Name-DOB-Address-Medical
– CA-SIN-Name-Address-Medical
– CA-SIN-Name-DOB-Address-Medical
– CA-SIN-Name-DOB-Medical
– CA-SIN-Name-Medical
– Medical Conditions [w/o Terms]
– Medicinal Products [w/o Terms]
– Social Insurance Numbers (CA)
– Social Insurance Numbers (CA) [w/o Terms]
PHI, PHIPA
DLP Profile Name
File Content Rules
Column Classification Rules
Data Tags
BR – LGPD
– BR – PFI (IBANs with Names)
– BR – PII (Personal IDs with Names; Contextual)
– BR – PII (Vehicle Data; Contextual)
– Driver License Numbers (BR)
– Driver License Numbers (BR) [w/o Terms]
– Social Security Numbers (BR)
– Social Security Numbers (BR) [w/o Terms]
LGPD, PFI, PII
Canada Personally Identifiable Information
– CA-Bank Account
– CA-Bank-CC
– CA-DL-Address
– CA-DL-Name
– CA-Name-DOB-Address
– CA-PAN-Exp-Address
– CA-PAN-Exp-Address-CVV
– CA-PAN-Exp-Name
– CA-PAN-Exp-Name-Address
– CA-PAN-Exp-Name-Address-CVV
– CA-PAN-Exp-Name-CVV
– CA-PAN-Name
– CA-PAN-Name-CVV
– CA-Passport
– CA-Passport-Address
– CA-Passport-Name
– CA-SIN-Name
– CA-SIN-Name-Address
– CA-SIN-Name-DOB
– CA-SIN-Name_DOB-Address
– Birthdates
– Driver License Numbers (AU)
– Email Addresses [w/o Terms]
– Personal Names
– Personal Names [w/o Terms]
PIPEDA, PII
Commonwealth of Australia – The Privacy Act 1988
– AU-DL-Address
– AU-DL-Name
– AU-MCN-Name-Address-Medical
– AU-MCN-Name-DOB-Medical
– AU-MCN-Name-DOB-Address-Medical
– AU-MCN-Name-Medical
– AU-Name-DOB-Address
– AU-Name-DOB-Address-Medical
– AU-Passport
– AU-Passport-Address
– AU-Passport-Name
– AU-TFN-Name
– AU-TFN-Name-Address
– AU-TFN-Name-DOB
– AU-TFN-Name_DOB-Address
– Birthdates
– Driver License Numbers (AU)
– Email Addresses [w/o Terms]
– Personal Names
– Personal Names [w/o Terms]
– Postal Addresses
PHI, PII
EU General Data Protection Regulation (GDPR) (narrow)
– EU-Address-PAN-Exp (narrow)
– EU-DriverLicense-DOB (narrow)
– EU-DriverLicense-Name-Address (narrow)
– EU-DriverLicense-Name-DOB (narrow)
– EU-DriverLicense-Name-Gender (narrow)
– EU-Identity-Biometric data (narrow)
– EU-Identity-DOB (narrow)
– EU-Identity-Ethnicity (narrow)
– EU-Identity-Eyecolor (narrow)
– EU-Identity-Gender (narrow)
– EU-Identity-Haircolor (narrow)
– EU-Identity-Health (narrow)
– EU-Identity-Height (narrow)
– EU-Identity-Name (narrow)
– EU-Identity-Name-Address (narrow)
– EU-Identity-Name-DOB (narrow)
– EU-Identity-Name-Gender (narrow)
– EU-Identity-Name-Height (narrow)
– EU-Identity-Name-Weight (narrow)
– EU-Identity-Race (narrow)
– EU-Identity-Religion (narrow)
– EU-Identity-Weight (narrow)
– EU-Name-Address (narrow)
– EU-Name-Biometric (narrow)
– EU-Name-Criminal record (narrow)
– EU-Name-DOB (narrow)
– EU-Name-DOB-Address (narrow)
– EU-Name-DriverLicense (narrow)
– EU-Name-DriverLicense-Address (narrow)
– EU-Name-email (narrow)
– EU-Name-Ethnicity (narrow)
– EU-Name-Eyecolor (narrow)
– EU-Name-Gender (narrow)
– EU-Name-Haircolor (narrow)
– EU-Name-height (narrow)
– EU-Name-IPAddress (narrow)
– EU-Name-PAN (narrow)
– EU-Name-PAN-CVV (narrow)
– EU-Name-PAN-Exp (narrow)
– EU-Name-Phone (narrow)
– EU-Name-Political (narrow)
– EU-Name-Race (narrow)
– EU-Name-Region (narrow)
– EU-Name-Region-Date (narrow)
EU-Name-Religion (narrow)
– EU-Name-Weight (narrow)
EU-Passport-Biometric data (narrow)
– EU-Passport-Name (narrow)
– EU-Passport-Name-Address (narrow)
– EU-Passport-Name-DOB (narrow)
– Birthdates
– Driver License Numbers (DE)
– Driver License Numbers (DE) [w/o Terms]
– Email Addresses [w/o Terms]
– National ID Numbers (BE)
– National ID Numbers (BE) [w/o Terms]
– National ID Numbers (NL) [w/o Terms]
– Passport Numbers
– Personal Names
– Personal Names [w/o Terms]
– Postal Addresses [w/o Terms]
– Telephone Numbers
GDPR, PII
Protection of Personal Information (POPI) Act
– SA-Name-Address-Phone
– SA-Name-DOB-Address
– SA-Name-DOB-Address-Medical
– SA-Name-Passport
– SA-Name-Passport-Address
– SA-Name-Passport-Address-Medical
– SA-Name-Passport-Medical
– SA-Name-SAID
– SA-Name-SAID-Address
– SA-Name-SAID-Address-Medical
– SA-Name-SAID-DOB
– SA-Name-SAID-DOB-Address
– SA-Name-SAID-DOB-Address-Medical
– SA-Name-SAID-DOB-Medical
– SA-Name-SAID-Medical
None
POPI, PII
UK Personally Identifiable Information
– UK-Bank Account
-UK-Bank-CC
– UK-DL-Address
– UK-DL-Name
– UK-Name-DOB-Address
– UK-NIN-Name
– UK-NIN-Name-Address
– UK-NIN-Name-DOB
– UK-NIN-Name_DOB-Address
– UK-PAN-Exp-Address
– UK-PAN-Exp-Address-CVV
– UK-PAN-Exp-Name
– UK-PAN-Exp-Name-Address
– UK-PAN-Exp-Name-Address-CVV
– UK-PAN-Exp-Name-CVV
– UK-PAN-Name
– UK-PAN-Name-CVV
– UK-Passport
– UK-Passport-Address
– UK-Passport-Name
– Birthdates
– Email Addresses [w/o Terms]
– Personal Names
– Personal Names [w/o Terms]
– Postal Addresses
PFI, PII
US Personally Identifiable Information
– US-DL-Address
– US-DL-Name
-US-ITIN-Name
– US-ITIN-Name-Address
– US-Name-DOB-Address
– US-Passport
– US-Passport-Address
– US-Passport-Name
– US-SSN-Name
– US-SSN-Name-Address
– US-SSN-Name-DOB
– US-SSN-Name-DOB-Address
– Birthdates
– Driver License Numbers (US)
– Email Addresses [w/o Terms]
– Personal Names
– Personal Names [w/o Terms]
– Postal Addresses
– Social Security Numbers (US)
– Telephone Numbers
CCPA, PII
Additional Predefined DLP Profiles
Netskope DSPM supports additional predefined DLP Profiles that are not pre-selected in the default Discovery Profile. You can enable these based on your organization’s compliance requirements.
To create custom DLP Profiles for regulations not covered by the predefined list, go to
Policies > Profiles > DLP
and create a new profile with the required File Content and Column Classification rules.
To view the full list and enable them, go to
Classification > DLP Profiles & Rules
and click
Edit Discovery Profile
.
In this Topic
Predefined DLP Profiles for DSPM

---
## Troubleshooting DSPM with DLP
**URL:** https://docs.netskope.com/en/troubleshooting-dspm-with-dlp/
**Last Modified:** 2026-06-18T22:55:31+00:00
**Scraped:** 2026-08-23T07:20:18.641823+00:00

Troubleshooting DSPM with DLP - Netskope Technical Documentation
Troubleshooting DSPM with DLP
Overview
This article provides guidance for resolving common issues encountered when using DSPM with a locally deployed DLP appliance.
Common Troubleshooting Scenarios
Browse the symptoms below to find resolutions for appliance connectivity, sidecar registration, and data classification issues.
Sidecar Cannot Connect to the DLP Appliance
Symptom:
The DLP Status column in
Administration > Sidecar
shows an unhealthy status, or the Test Connection button fails.
Possible Causes and Resolutions:
Incorrect IP address:
Verify the DLP appliance IP address in your Cloud Service Provider (CSP) console or under
Settings > Security Cloud Platform > On-Premises Infrastructure
. Ensure the IP entered in the Sidecar Pool matches the actual appliance address.
Appliance unavailable:
The DLP appliance may be offline or not correctly tethered to the Netskope console. Verify the appliance is powered on and properly configured.
Wrong appliance selected:
Ensure you select the locally deployed DLP appliance visible to your sidecar network, not a Netskope-hosted appliance.
Firewall/network issue:
The sidecar and DLP appliance must be accessible to one another via HTTPS (port 443). Verify that no firewall rules, security groups, or network segmentation are blocking communication between them.
SSL handshake failure:
If sidecar logs show errors such as
“Remote host terminated the handshake”
or
“SSL peer shut down incorrectly,”
verify that no SSL-intercepting proxy is interfering with the connection between the sidecar and DLP appliance.
Sidecar Cannot Register with the DSPM Application
Symptom:
The sidecar does not appear in
Administration > Sidecar
, or the Version and Status columns remain empty.
It may take a few minutes for newly deployed sidecars to appear. If the sidecar still does not register after waiting, check your configuration and redeploy if needed.
Possible Causes and Resolutions:
Invalid token:
The most common cause is an incorrect or expired sidecar pool token. Generate a new token and redeploy the sidecar with the updated value.
DNS resolution failure:
If sidecar logs show
“Temporary failure in name resolution”
or
“Name or service not known,”
verify that the sidecar has proper DNS resolution and outbound egress to your tenant’s sidecar hostname (
sidecar-<tenant>.goskope.com
).
Firewall restrictions:
Ensure the sidecar has outbound access on port 443 to the required DSPM endpoints. See
Firewall Settings for DSPM-Hosted Instances
for the full list.
Classification Results Not Returned
Symptom:
After scanning a data store, no classification results appear in
DSPM > Classification > Classification Management
.
Possible Causes and Resolutions:
No DLP Profiles enabled:
Navigate to
DSPM > Classification > DLP Profiles & Rules
and verify that at least one DLP Profile is enabled in the Discovery Profile.
DLP appliance not linked:
Verify that the sidecar pool is linked to a DLP appliance in
Administration > Sidecar
.
Appliance needs upgrade:
Ensure the DLP appliance is running a current version. If the appliance was deployed before the R132 release, it may not support auto-upgrades. Redeploy the appliance using the latest available image.
Classification Requests Timing Out
Symptom:
Scans take an unusually long time to complete, or sidecar logs show repeated HTTP 425 responses from the DLP appliance.
Resolution:
Reduce the number of DLP Profiles selected in your DSPM Discovery Profile. Having too many profiles enabled simultaneously can cause the appliance to exceed its processing capacity.
DLP Appliance Not Auto-Upgrading
Symptom:
Despite being registered on an upgrade schedule, the DLP appliance is not upgrading.
Possible Causes and Resolutions:
Appliance version too old:
Auto-upgrading was introduced in the R132 release. If your appliance was deployed before R132, you must redeploy it using at least the R132 build.
Appliance powered off during upgrade window:
The appliance must be running during the scheduled upgrade window. Upgrades are skipped if the appliance is powered down.
Insufficient disk space:
If the appliance was deployed with less than the recommended disk space (351 GB), upgrades can fill up disk space and fail silently. Redeploy the appliance with adequate storage.
UI Display Issues: Destroyed Sidecar Still Shows
Symptom:
After Destroying a Sidecar, It Still Shows in the UI.
Resolution:
This is expected behavior. After 1 hour, the sidecar will be considered offline and automatically hidden in the Sidecar Administration page. You can still see it by clicking the “Show Inactive Sidecars” icon.
In this Topic
Troubleshooting DSPM with DLP

---
## Deploy the DLP Appliance for DSPM
**URL:** https://docs.netskope.com/en/deploy-the-dlp-appliance-for-dspm/
**Last Modified:** 2026-06-18T22:52:44+00:00
**Scraped:** 2026-08-23T07:20:19.836897+00:00

Deploy the DLP Appliance for DSPM - Netskope Technical Documentation
Deploy the DLP Appliance for DSPM
Overview
A DLP appliance is required to perform data classification when using sidecars. This guide walks you through the DSPM-specific steps to prepare, download, and configure the DLP appliance for use with your DSPM environment.
If you want to deploy a Single Appliance that bundles both the sidecar and DLP services into one virtual machine, follow the dedicated deployment instructions instead.
To learn more:
Deploy the DSPM Single Appliance
.
Prerequisites
Before deploying the DLP appliance, ensure you meet the following requirements.
Network Planning:
The DLP appliance must reside within the same network as the sidecars it serves, or in directly connected networks. Both components must be accessible to one another via HTTPS (port 443).
Appliance Sizing:
Unless recommended otherwise, deploy a Medium-sized appliance. The Small size is intended only for proof-of-concept testing.
AWS
GCP
Azure
VM (ESXi/Hyper-V/KVM)
Concurrent Requests
Min Disk
Small
c5ad.4xlarge
n2-standard-16
Standard-F16s_v2
16 cores / 32 GB
480 rps (burst 576)
351 GB
Medium
c5ad.8xlarge
n2-standard-32
Standard-F32s_v2
32 cores / 64 GB
1280 rps (burst 1536)
351 GB
Large
c5ad.16xlarge
n2-standard-64
Standard-F64fs_v2
64 cores / 128 GB
2880 rps (burst 3456)
351 GB
In AWS regions where
c5ad
is unavailable, use
c5a
. To ensure optimal performance, use
SSDs
for all instances.
ESXi does not support dynamic resizing after creation.
If you deploy an incorrectly-sized appliance, the DLP Appliance doesn’t support scaling resources up or down. You must redeploy the appliance at the correct size.
Networking Considerations:
Ensure that
Netskope IPs
and Amazon S3 (e.g.,
*.s3-us-west-1.amazonaws.com
) are allowlisted. If
tenant.goskope.com
is your tenant hostname, also allow IPs for
config-tenant.goskope.com
and
callhome-tenant.goskope.com
.
You must also allowlist the following gateway domains:
dlpappliancegw.sv5.goskope.com
dlpappliancegw.bom3.goskope.com
dlpappliancegw.am2.goskope.com
dlpappliancegw.sjc1.goskope.com
dlpappliancegw.fr4.goskope.com
dlpappliancegw.ruh1.goskope.com
dlpappliancegw.mel2.goskope.com
dlpappliancegw.sjc2.goskope.com
dlpappliancegw.zur2.goskope.com
dlpappliancegw.lon3.goskope.com
dlpappliancegw.sin2.goskope.com
dlpappliancegw.dfw3.goskope.com
dlpappliancegw.fra2.goskope.com
– If you use
DRM with DLP
, you must also allowlist Microsoft AIP endpoints.
– All integrating services must be able to reach the appliance over HTTPS (TCP 443).
– SSL interception of traffic from the DLP appliance
isn’t
recommended. If a proxy is in place, ensure you import the respective certificates.
– Deploying multiple DLP appliances behind a network load balancer
isn’t
supported for asynchronous request scenarios.
For the complete list of egress and port requirements, see
Firewall Settings for DSPM-Hosted Instances
.
Deployment Process
The following steps outline the end-to-end process to generate the necessary authentication keys, download the appliance image, and link it to your DSPM sidecar environment.
Step 1: Generate the REST API v1 Key
This key allows the appliance to call home and fetch the latest DLP configurations. It
doesn’t
need to be shared; it just needs to be present within your Netskope console.
Log in to the Netskope console.
Navigate to
Settings > Tools > Rest API v1
.
Determine your token status:
If a token already exists:
Ensure that it is set to never expire.
If no token exists:
Click
Generate New Token
and set the expiration to “never expire.”
Step 2: Retrieve the License Key
The appliance setup uses the License Key to validate your DLP entitlement. The Netskope console generates it automatically.
Log in to the Netskope console.
Navigate to
Settings > Security Cloud Platform > On-Premises Infrastructure
.
Copy the
License Key
value displayed on this screen.
Step 3: Download the DLP Appliance Image
The download method depends on your target deployment platform.
For AWS:
Log in to the Netskope console.
Navigate to
Settings > Security Cloud Platform > On-Premises Infrastructure
.
Click
Setup DLP On-Demand
.
In the modal, within the AWS section, click the
Assign
link.
Enter the AWS Account ID and Region where you will install the appliance.
Click
Submit
.
The AMI should be available within the “Shared with me” section of your AMI Catalog within a few minutes. If your target region is not available in the dropdown, open a support ticket.
For Azure, ESXi, Hyper-V, or KVM:
Log in to the Netskope console.
Navigate to
Settings > Security Cloud Platform > On-Premises Infrastructure
.
Click
Setup DLP On-Demand
.
In the modal, within the section for your desired platform, click the
Download
link.
In the dialog, the SHA-1 hash will display. Click
Copy
to save its value for verification, then click
Download
.
For GCP:
Log in to the Netskope console.
Navigate to
Settings > Security Cloud Platform > On-Premises Infrastructure
.
Click
Setup DLP On-Demand
.
In the modal, within the GCP section, click the
Assign
link.
Select the
Identity Type
: either
User
or
ServiceAccount
.
Enter the
Account Email Address
associated with the selected identity type.
Click
Submit
.
Step 4: Deploy the DLP Appliance
Follow the installation instructions for your chosen platform (AWS, Azure, ESXi, GCP, Hyper-V, or KVM).
AWS
Launch an EC2 instance using the
DLP On Demand AMI
(found in
Private Images
).
Set the
Instance Type
per the sizing table in Prerequisites.
Define your desired
Storage
and use
gp3
.
No SSH key-pair is required. Set up networking and firewall security groups as appropriate. The appliance should not be publicly accessible.
Select
proceed with no key-pair
and launch the instance. The instance will be ready after approximately 30 minutes.
Azure
During deployment, Azure may display an “OS Provisioning Timed Out” notification. This is expected and can be safely ignored. Confirm readiness by verifying the instance state shows “Running.”
Download the VHD from the presigned URL.
Extract the VHD:
tar -xvf {downloaded_vhd_tar_file} -C {path}
Create a
Storage Account
under your
Resource Group
.
Create a
Container
under the Storage Account.
On the Storage Account page, go to
Security + Networking > Shared access signature
.
Enable all permissions, set
Start Time
24h before now and
End Time
24h after now.
Click
Generate SAS and connection string
and copy the
SAS token
.
Install
AzCopy
if not already installed.
Note: Use
AzCopy
to upload. Uploading large files via the Azure Portal is unreliable and may result in file corruption.
Upload the VHD:
azcopy copy "{local_path}.vhd" "https://{account_name}.blob.core.windows.net/{container_name}/{vhd_name}.vhd?{SAS_TOKEN}" --blob-type PageBlob
Navigate to
Images
in Azure.
Choose your subscription. Set
OS Type: Linux
, select your VHD from storage,
Account Type: Premium SSD
,
Encryption: Platform managed
.
Click
Review + create
.
Create an instance from the image. Select a minimum of
351 GB Premium SSD
disk.
Configure networking and create the VM.
vSphere (ESXi)
Download the
.ova
image to your local system before uploading to vSphere (vSphere does not support direct URL imports when the URL exceeds its maximum supported length).
Sizing requirements:
16 CPU / 32 GB Memory
32 CPU / 64 GB Memory
64 CPU / 128 GB Memory
To deploy the DLP Appliance:
Right-click a
host
,
cluster
, or
datacenter
and select
Deploy OVF Template
.
Select
Local file > Upload files
, choose your
.ova
file, click
Next
.
Enter a VM name, select deployment location, click
Next
.
Select compute resource, click
Next
.
Review details and accept license agreements, click
Next
.
Select datastore and virtual disk format (e.g., Thin Provision), click
Next
.
Map source networks to destination network ports, click
Next
.
Customize template settings if applicable, click
Next
.
Review summary, optionally check
Power on after deployment
, click
Finish
. The instance will be ready after approximately 30 minutes.
GCP
Go to
Compute Engine > VM Instances
and click
Create Instance
.
In
Machine Configuration
, provide a name and select
N2
under General Purpose.
In
Machine Type
, select per the sizing table in Prerequisites.
In
OS and Storage
, click
Change
, select the DLP On Demand appliance image, and set size to
300 GB
minimum.
Set up networking and firewall security groups as appropriate, then click
Create
. The instance will be ready after approximately 30 minutes.
Hyper-V
Download the appliance image from the
Setup DLP on Demand
window.
Open
Hyper-V Manager
.
In the
Actions
pane, click
Import Virtual Machine
.
Click
Next
, then
Browse
to the top-level folder of the exported VM files. Click
Select Folder > Next
.
Select the VM from the list, click
Next
.
Choose
Register the virtual machine in-place (use the existing unique ID)
.
Review and click
Finish
.
Before starting the instance
, right-click the VM >
Settings
>
Network Adapter
and select the appropriate network switch.
Start the VM from the Actions pane or by right-clicking >
Start
.
KVM
Download the appliance image from the
Setup DLP on Demand
window.
Create a template directory and extract:
mkdir dlp-vm-template tar -xvf dlp-appliance.tar
Extract the QCOW2 disk image:
tar -xzvf netskope-dlp-on-demand-kvm-qcow2-*.qcow2.tar.gz -C /home/ubuntu/dlp-vm-template/
Deploy using
virt-install
:
sudo virt-install --name dlp-appliance --ram 65536 --vcpus 32 \ --os-variant ubuntu24.04 \ --disk path=/home/ubuntu/dlp-vm-template/<image_file>.qcow2,size=452 \ --import --network default --check path_in_use=off
When
virt-install
connects the console, press
CTRL+C
to exit. The boot process continues in the background.
Verify VM status:
sudo virsh list --all
Check network:
sudo virsh net-list
Find IP address:
sudo virsh net-dhcp-leases default
Connect via SSH:
sudo ssh {username}@{IP}
Step 5: Connect and Tether the Appliance
Once the instance is created, you must connect it to Netskope so it can download the required configuration and profiles.
SSH into the instance as
nsadmin
with the default password
nsappliance
:
ssh nsadmin@<instance_ip>
Change the default password immediately:
nsappliance> auth change-password
Configure DNS (if DNS is not provided via DHCP):
nsappliance> configure
nsappliance(config)> set dns primary x.x.x.x
nsappliance(config)> set dns secondary x.x.x.x
nsappliance(config)> save
nsappliance(config)> exit
If you need to configure the network interface manually instead of using DHCP:
nsappliance> configure
nsappliance(config)> set interface v4 dhcp enable false
nsappliance(config)> set interface v4 static enable true
nsappliance(config)> set interface v4 static ip x.x.x.x
nsappliance(config)> set interface v4 static gw x.x.x.x
nsappliance(config)> set interface v4 static netmask x.x.x.x
nsappliance(config)> set dns primary x.x.x.x
nsappliance(config)> set dns secondary x.x.x.x
nsappliance(config)> save
nsappliance(config)> exit
To revert to automatic DHCP configuration:
nsappliance> configure
nsappliance(config)> set interface v4 dhcp enable true
nsappliance(config)> set dns primary x.x.x.x
nsappliance(config)> set dns secondary x.x.x.x
nsappliance(config)> save
nsappliance(config)> exit
Ensure that DNS resolution works on the appliance before proceeding.
Apply the
License Key
(retrieved in Step 2):
nsappliance> configure
nsappliance(config)# set system licensekey <license-key>
nsappliance(config)# save
nsappliance(config)# exit
Verify tethering status. The value
callhome_reachable
must be
true
, and
tenant-url
and
serial
should be populated:
nsappliance> status tethering
After successful tethering, the appliance needs approximately 30 minutes to initialize before it is ready to process requests. You will also see the appliance reflected on the
On-Premises Infrastructure
page in the Netskope console.
Step 6: Configure a Proxy (Optional)
If your organization routes outbound traffic through a proxy, configure it using the appliance CLI.
Explicit proxy
Implicit proxy (SSL-intercepting proxy with custom CA)
Configure the proxy details:
nsappliance> configure
nsappliance(config)# set management-plane upstream-proxy-server hostname 10.10.10.10
nsappliance(config)# set management-plane upstream-proxy-server port 8000
nsappliance(config)# set management-plane upstream-proxy-server username <USERNAME>
nsappliance(config)# set management-plane upstream-proxy-server password <PASSWORD>
nsappliance(config)# set management-plane upstream-proxy-server trusted-ca
Copy and paste your single PEM-formatted server CA certificate (no keys).
Press
Ctrl-D
when done.
Save and restart:
nsappliance(config)# save
nsappliance(config)# exit
nsappliance> restart dlpaas all
Configure the trusted CA:
nsappliance> configure
nsappliance(config)# set management-plane upstream-proxy-server trusted-ca
Copy and paste your single PEM-formatted server CA certificate (no keys).
<PASTE PEM Formatted CA CHAIN>
Press
Ctrl-D
when done.
<Press Ctrl-D>
Save and restart:
nsappliance(config)# save
nsappliance(config)# exit
nsappliance> restart dlpaas all
Step 7: Link the Appliance to Your Sidecar Pool
After the appliance is deployed and running, you must link it to your DSPM sidecar pool so that sidecars can send data samples for classification.
For detailed instructions, see the “Link a DLP Appliance to a Sidecar Pool” section in
DSPM Sidecar Administration Overview
.
If you encounter issues during or after deployment, see
Troubleshooting DSPM with DLP
.
In this Topic
Deploy the DLP Appliance for DSPM

---
## SMB File Share Plugin for Exact Data Match
**URL:** https://docs.netskope.com/en/smb-file-share-plugin-for-exact-data-match/
**Last Modified:** 2026-06-05T02:16:21+00:00
**Scraped:** 2026-08-23T07:20:40.356271+00:00

SMB File Share Plugin for Exact Data Match - Netskope Technical Documentation
SMB File Share Plugin for Exact Data Match
Release Notes
1.0.0
Added
Initial release with SMB2/SMB3 CSV ingestion.
This document explains how to configure the SMB File Share EDM plugin v1.0.0 with the Exact Data Match plugin of the Netskope Cloud Exchange platform. This plugin is used to fetch a CSV file from a remote SMB server (Windows or Samba) and to generate EDM hashes of the pulled CSV file. The plugin supports SMB protocol version from SMB 2.0.2 to SMB 3.1.1.
Prerequisites
To complete the configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Exact Data Match plugin
already configured.
SMB server configured in Windows/Linux/Isilon instance with read access to the SMB Shared Directory and CSV files with appropriate data structure.
SMB File Share EDM Plugin Support
This plugin fetches data from a SMB server supporting SMB 2.0.2 to SMB 3.1.1 and generates Exact Data Match (EDM) hashes according to the defined plugin configurations.
Feature
Support
Pull
Yes
Push
No
SMB Server Permissions
Permission Type
Requirement
SSH Access
Required
File Read Access
Required
Network Share Access
Required
Port Access
445(SMB)
Required Permissions
Users should have read access to the shared folder and CSV file.
Network connectivity to port 445.
SMB service enabled on the server.
Sufficient disk space on Cloud Exchange for temporary file processing.
API Details
List of Libraries Used to Access Remote SMB File Share
This plugin uses Python libraries and the SMB protocol stack to establish secure connections to Windows SMB servers and transfer CSV/TXT files by navigating shared directories.
Library: smbclient
Usage: smbclient is a high-level Python wrapper that provides simple file-system-like functions (register_session, stat, open_file, reset_connection_cache) to connect and interact with Windows SMB shared directories. The plugin uses smbprotocol.exceptions (SMBException, SMBResponseException) only for exception handling when SMB operations fail.
Register session (establish connection + auth)
from ..lib import smbclient
smbclient.register_session(
server,
username=username,
password=password,
port=port,
)
Build UNC and verify connection
unc_path = self._build_unc_path(
server,
directory_path,
file_path,
)
smbclient.stat(unc_path)
Verify file exist
# Check if file exists
stat_result = smbclient.stat(unc_path)
# Check it's not a directory
if stat.S_ISDIR(stat_result.st_mode):
Download a CSV file via SMB
with smbclient.open_file(unc_path, mode="rb") as remote_file:
with open(csv_file_path, "wb") as file_object:
if record_count:
# Partial file retrieval (for sample data)
# +1 to include header row
lines_to_read = record_count + 1
for _ in range(lines_to_read):
line = remote_file.readline()
if not line:
break
file_object.write(line)
else:
# Full file retrieval
shutil.copyfileobj(remote_file, file_object)
Clean up sessions
smbclient.reset_connection_cache(fail_on_error=False)
Performance Matrix
Here is the performance reading conducted for fetching and sanitizing ~1M Rows (25 columns, per column ~50 characters long string, 1.3 GB size, Avg Column Uniqueness: ~96%, Avg Row Uniqueness: ~96%) CSV file on a Large CE instance with these specifications:
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
CSV data fetched from SMB File Share Without Sanitization
~7K rows/sec
Note
For CE instance disk space, refer to this
documentation
.
Workflow
Get your server credentials and file paths.
Configure the SMB File Share EDM Plugin.
Configure sharing between SMB File Share EDM Plugin and Tenant.
Validate the SMB File Share EDM Plugin.
Watch a Video
Click play to watch a video.
Get a Shared Directory from the SMB Server
SMB Server hosted in Windows
Run PowerShell as Administrator.
Run command in the PowerShell:
Get-SmbShare
Example Output:
Name	ScopeName	    Path
—--	 	---------		----
ADMIN$	*		        C:\Windows
C$		*         		C:\
MyShare	*         		C:\SMBShare
What It Means:
Name → Share name
Path → Actual folder location
Shares ending with $ (like
C$
,
ADMIN$
) are hidden administrative shares.
SMB Server hosted in Linux
Samba shares are defined inside
/etc/samba/smb.conf
.
In Linux terminal, run:
testparm -s
Look for sections like:
[shared]
path = /srv/samba/shared
Every section below [global] is a shared folder.
[Documents]
path = /home/devuser/docs
What it means:
Share name → Documents
Actual folder →
/home/devuser/docs
SMB Server hosted in Isilon
Log in to OneFS.
Go to
Protocols
and select
SMB
.
Open the Shares Section.
You will see a list of configured SMB shares.
Look at the
Path
column. This shows the actual filesystem directory (usually under /ifs) that is shared via SMB.
Example table:
Share Name		Path
test-share		/ifs/data/test
Finance		    /ifs/data/finance
The Path value (
/ifs/...
) is the directory being shared.
Setup for kerberos when using domain name/FQDN instead of an IP address
Install Kerberos Utilities Inside Core Container.
Access the core container:
docker exec -it -u0 <core-container> bash
Install Kerberos packages.
Ubuntu/Debian
:
apt update && apt install -y krb5-user smbclient
RHEL/CentOS
:
yum install -y krb5-workstation samba-client
Configure Kerberos: (
krb5.conf
).
Create or update:
/etc/krb5.conf
Add realm configuration:
[realms]
   EXAMPLE.COM = {
       kdc = dc01.example.com
       admin_server = dc01.example.com
   }
[domain_realm]
   .example.com = EXAMPLE.COM
   example.com = EXAMPLE.COM
Note
Realm must usually be uppercase.
KDC should point to the domain controller.
DNS resolution must work correctly inside the container.
Replace these values:
Placeholder
Replace With
EXAMPLE.COM
Your AD/Kerberos realm
dc01.example.com
Your Domain Controller / KDC hostname
example.com
Your domain
Update the
docker-compose.yml
.
Edit
docker-compose.yml
and add extra_hosts in core service:
services:
 core:
   extra_hosts:
     - "<domain/FQDN>:<IP>"
Restart Cloud Exchange, and configure the plugin with domain/FQDN of your SMB Server.
sudo ./stop && sudo ./start
Configure the SMB File Share EDM Plugin
Log in to Cloud Exchange and go to
Settings > Plugin Store
.
Search for and select the
SMB File Share EDM v1.0.0
plugin box.
Enter the Basic Information:
Configuration Name:
Enter a name appropriate for your integration.
Sync Interval:
Adjust Sync Interval as per your requirement. (Default: 12 hours).
Note
The configuration name you provide will be used to give the name to the generated hash file to share with the Netskope Tenant. Be aware that if you later delete this configuration and create a new one with the same name, the hash file may already exist in the Netskope Tenant. In such cases, attempting to push the hash file to the tenant will result in an error, as the file with the same name already exists. Consider using a unique name to avoid this issue.
Click
Next
and enter the Configuration Parameters:
SMB Server Hostname/IP:
Hostname or IP address of the SMB server from which the CSV file should be pulled.
Port:
TCP port for SMB connection (default 445).
Username:
Username with read access to the shared directory.
Password:
Password for the provided username.
Share Directory Name:
The SMB share name. E.g. If the full UNC path is ‘\server\share\path\file.csv’, enter ‘share’. For getting this, follow steps provided in
Get Shared Directory from the SMB Server
.
CSV File Path:
Provide a CSV file name or path of the CSV file relative to Share Directory Name. E.g. If the full UNC path is ‘\server\share\path\file.csv’, enter ‘path\file.csv’. Use backslashes (\) only. Note: Only .csv/.txt files with max 25 columns are supported. For getting this, follow steps provided in
Get Shared Directory from the SMB Server
.
Delimiter:
Single character delimiter used in the CSV/TXT file (e.g. comma, pipe, semicolon).
Remove Quotes:
Mark as checked if your CSV encloses fields in double quotes, especially when values contain commas. Quoted fields will be parsed as single columns. Improper quote placement may cause rows to be skipped.
Note
By default, quotes are treated as literal text. Enable Remove Quotes toggle if your CSV uses double quotes to encapsulate fields that contain commas (like
"123 ABC Street, Suite 100"
). This ensures the field is treated as a single column. Note that this mode requires strict CSV formatting. If a field starts with a quote, any character, including a space, following the closing quote but preceding the comma (like
"Word",
) will cause the row to be skipped.
Click
Next
and enter the Hash Generation and Sanitization Parameters.
Select the appropriate options for sanitization and hash generation operations:
Sanitization (Name Column):
Sanitize the content by checking the Name Column checkbox. (Default: Unchecked). The Sanitization Process performs the following actions:
One character:
The cell will be marked as invalid if it contains only one character.
Digits:
Cells containing digits will be marked as invalid.
Stopwords:
Cells that match a stopword from the list will be marked as invalid (This works only if the
Remove Stopwords
checkbox is enabled).
Non-alphanumeric characters:
Remove all special characters to validate the cell.
Hash Generation is divided into two parts:
Normalization:
Select the value from dropdown to normalize the data value. (Default: None)
Create Dictionary:
Select value from dropdown to create dictionary of unique values for selected field that can be used in DLP rule in netskope tenant. (Default: None)
Remove Stopwords:
Mark as checked if you want to remove certain stopwords as part of the sanitization process.(Default:Unchecked) Ensure that Name Column is checked for the applicable field to reflect the changes.
Note
User Normalization parameter to normalize the fetched results. For example, a number such as 123-45-6789 or 123 45 6789 will be treated as 123456789. Number normalizations ignore characters, such as dots, dashes and spaces. A string normalization ignores the case sensitivity of the letters.
Use the Create Dictionary option only when necessary, as this operation is resource-intensive and may impact system performance. Choose this option thoughtfully for optimal efficiency.
Click
Next
. Preview the sanitization sample output by clicking
Preview Good File
or
Preview Bad File
.
Note
If you are using the plugin with sanitization On, then the performance may be differ due to extra processing.
Proceed without sanitization:
Uncheck this option to proceed with sanitization. (Default: Checked)
Note
All the data will be under consideration for hash generation if this option is Unchecked; otherwise, only the Good File content will be part of the hash generation.
Click
Save
. You will be redirected to
Exact Data Match > Plugins
page where you can see your configured plugin.
Configure an EDM Sharing Configuration for SMB File Share
A sharing configuration is used to share the generated EDM hashes with the destination platform. To share EDM hashes with your Netskope Tenant, create a sharing configuration using these steps:
Go to
Exact Data Match > Sharing
and click
Add Sharing Configuration
.
Configure the sharing parameters:
Source Configuration:
Select the configured SMB File Share EDM plugin.
Destination Configuration:
Select a destination where EDM Hash will be shared.
Target:
The value is automatically set according to the selected Destination Configuration.
Click
Save
.
Validate the SMB File Share EDM Plugin
Note
Cloud Exchange only stores sensitive pulled data CSV files temporarily until the hash generation and upload process is completed. After that, the stored files are automatically removed.
Validate in Cloud Exchange
To validate the pulling of the configured plugin in Cloud Exchange, go to
Settings > Logging
and search for the SMB File Share EDM plugin logs.
You can verify the plugin operation from the logs available at
Logging
in Cloud Exchange:
The status values are as follows:
Scheduled:
Indicates that the sharing has been configured, and the pull and push operations are waiting in the queue for processing.
Generating Hash:
Indicates that the hash generation process has started. This stage includes fetching > validating > sanitization (if enabled) > generating hash.
Uploading Hash:
Indicates that uploading the hash to the destination configuration has started.
Upload Completed:
Indicates that hashes are uploaded to the destination configuration.
Checking Apply Status:
Checking the apply status of hashes to the destination configuration.
Apply In Progress:
The hash process has started and is in progress on the destination.
Completed:
Indicates that the hash file has been pushed successfully to the destination configuration.
Failed:
Indicates that the final result of the action has failed to execute. The actions are Generating Hash/Uploading Hash/Checking Apply Status.
Shared EDM hashes can be verified from the logs available at
Logging
in Cloud Exchange:
Validate on the Netskope Tenant
To ensure the push of EDM hashes on the Netskope Tenant from the cloud exchange:
In the Netskope Tenant, go to
Policies > DLP
.
Click
Edit Rules
and select
Data Loss Prevention
.
On the
Exact Match
tab, a list of files is shown.
Troubleshooting the SMB File Share EDM Plugin
Unable to configure the SMB File Share EDM Plugin
If you are unable to configure the SMB File Share EDM plugin, it could be due to one of the following reasons:
The user doesn’t have permission to read the CSV file.
Incorrect hostname/server IP address.
The port is disabled or blocked on the server.
Network connectivity issues between Cloud Exchange and server.
The configured SMB server is of version lower than SMB 2.0.2.
What to do:
Verify credentials are correct.
Check file
permissions
on the server.
Ensure the SSH service is running.
Verify network connectivity.
Verify the SMB version configured in the instance, and if it is lower than SMB 2.0.2, upgrade it to version between SMB 2.0.2 to SMB 3.1.1.
CSV file not found or access denied
If you receive errors about file not found or access denied:
What to do:
Verify the CSV file path is correct and the file exists.
Ensure the user has read permissions for the file.
Check if the file is not locked by another process.
Hash generation fails or takes too long
If hash generation fails or performance is poor:
What to do:
Check available disk space on Cloud Exchange (ensure at least 2x CSV file size).
Reduce CSV file size or split into smaller files.
Disable sanitization if not required to improve performance.
Monitor system resources during processing.
Known Behaviors
Sanitization can reduce processing speed by approximately 65% but improves data quality.
Dictionary creation is resource-intensive and should only be used when necessary.
The plugin creates temporary files during processing that are automatically cleaned up.
SSH connection timeouts may occur with very large files; consider increasing timeout values.
Memory usage scales with CSV file size; monitor system resources during large file processing.
Limitations
Each Netskope tenant has a limit of handling up to 5 staging files. If this maximum limit is reached, you may encounter the following error while sharing hashes:
EDM Netskope Exact Data Match [EDM Netskope] Received exit code 400, Error occurred while uploading edm hashes of configuration Linux EDM to the configuration EDM Netskope.
To resolve this error, you have to delete the existing files from staging.
In this Topic
SMB File Share Plugin for Exact Data Match

---
## DLP Entity
**URL:** https://docs.netskope.com/en/dlp-entity/
**Last Modified:** 2026-08-03T04:44:13+00:00
**Scraped:** 2026-08-23T07:21:16.986167+00:00

DLP Entity - Netskope Technical Documentation
DLP Entity
In Netskope DLP,
Entities
refer to data identifiers and dictionaries. Data identifiers are common terms used to categorize certain types of identifiable data, and dictionaries are files with keyword and regular expressions. Entities are used in a rule to identify sensitive data.
To open the Entities page, in the Netskope UI go to
Policies > Profiles > DLP > EDIT RULES
and select
Data Loss Prevention
. Then click on the
Entities
tab.
Data Identifier
Netskope provides a wide list of predefined data identifiers with meaningful names and descriptions. The full list of predefined data identifiers can be seen in the New DLP Rule workflow.
To view the full list of predefined data identifiers, in the Rules tab of the Data Loss Prevention Rules page, click
New Rule
. In the New DLP Rule dialog box, all the predefined identifiers are listed under categories.
You can also create your own custom data identifiers.
To create custom data identifiers,
In the ENTITIES tab, click
NEW ENTITY
. The Create Entity dialog box is displayed with the
Data identifier
option selected.
Provide a name for the custom data identifier and choose whether the new identifier is case-sensitive or not.
Add a predefined data identifier in the format
{{predefined_data_identifier}}
, a keyword, or a regular expression. For example, a predefined identifier such as
{{Full Names (US)}}
, a keyword such as
Name
, or a regex such as
[0-9]{5,10}
.
Click the
Validate Regex
button to validate the syntax of the regular expression. For more information on the supported operators, quantifiers, and metacharacters for regular expressions, see
Building Regular Expressions
.
Select an Existing
Data Type
or create a new
Data Type
.
Select a
Sensitivity Level
.
Under Advanced Options, you can set various conditions to narrow down the results when this identifier is used in a DLP rule. For more information, see the
Advanced Options
section.
Entity Redaction
Entity Redaction requires Advanced DLP. For more information, see your account executive or contact support@netskope.com.
Entity Redaction
(
formerly
Entity Obfuscation
) is a data de-identification capability that redacts sensitive information detected by entity matches in DLP profiles.
By enabling
Entity Redaction
, this entity’s matched data will be obfuscated in DLP’s incident forensic data. On any obfuscation/masking method, if the number of masked characters in the match is fewer than 5, then all of the digits and/or letters are masked.
Deprecated:
Updated:
Incident Forensics: Forensic workflows will remain unchanged. The system continues to support incident records and dedicated forensic views without any modification.
Configuration Steps
Pre-defined entities – Implicit Masking
When you clone a predefined entity, Netskope automatically enables entity redaction and selects a recommended masking method for that entity. The following example shows the Create Entity dialog box after cloning the Card Numbers (all) entity. The Method field displays Mask — Display only the first and last 4 characters (recommended), and an info banner confirms that Netskope recommends this method for the predefined entity.
Custom entities – Adds Custom Masking capabilities
Incident Forensics
Name:               John Smith
XXX:                XXX-XX-XXXX
Email:               john.smith@example.com
DOB:                03/15/1985
Filters
Filters
reject matches that are unlikely or implausible. There are special considerations for predefined
Entities
.
Use Filters
— provides two filters: “Common-Sense” and “Unlikely Matches”.
If a predefined
Entity
has no filters, the
Use Filters
and
Use Validator for Regex
options will be grayed out.
If a predefined
Entity
has only one of the two filters, the
Use Validator For Regex
option will be greyed out and the default validator for the selected predefined entity will be applied.
If a predefined
Entity
has both filters,
Use Filters
and both filters underneath will be checked.
Use Validator for Regex
options will be grayed out.
Netskope integrates text normalization, addressing elements like fonts, colors, line folding, and spacing into the text extraction process across certain schemas. Beyond enhancing detection accuracy, this normalization may serve as a functional countermeasure against text-based steganography.
Dictionary
A dictionary can be a keyword dictionary or a regular expression dictionary. A dictionary file is a CSV file that can contain keywords and phrases, or regular expressions you want to find using a DLP rule. Each dictionary file can contain either keywords and phrases, or regular expressions.
To use a dictionary file, create a CSV file with one keyword, phrase, or regular expression per line. A regular expression dictionary file can contain up to 25 entries. For more information on the supported operators, quantifiers, and metacharacters for regular expressions, see
Building Regular Expressions
.
Netskope also supports weighted dictionaries where you can specify a weight for each keyword or phrase. The weight of a keyword is the number based on which the violation score is calculated. Violation score of a rule is the sum of weights of the rule count where a rule count is the number of times a rule is matched. The higher the keyword weight, the higher the violation score. The violation score determines when to trigger a rule in case of a violation. If a weight is not specified, then a default weight of 1 is assigned to the keyword or phrase.
Note
Weight is not assigned to regular expressions.
To define the keyword in the CSV file, use the format
[keyword],[weight]
where the weight is optional and can be any value between -100 and 100. Use positive values to increase the violation score and negative values to decrease the violation score.
Example
For example, if you are creating a DLP policy to identify AWS access keys, your access key dictionary can contain the following keywords and phrases with weights.
access key ID, 50
AWS, 10
AWS access key, 100
AWSAccessKeyId, 100
access keys
access, -20
Public Cloud, -100
If you created a rule such as C0 NEAR D0 where,
C0 is a custom identifier
\b[A-Z0-9]{20}\b
to identify an AWS access key ID, and
D0 is the access key dictionary.
As an example, if a document is found to contain the following statements,
“
Generate the access key
“
“
Enter the AWS access key ID AKIAIVLZMKR5WZSQO5ZA
“
then, the rule count for “
Generate the access key
” is zero and the rule count for “
Enter the AWS access key ID AKIAIVLZMKR5WZSQO5ZA
” is one.
The total violation score for this document will be 100.
To create a new dictionary,
In the Entity tab, click
New Entity
. The Create Entity dialog box is displayed.
Select
Dictionary
and then select
Keyword Dictionary
or
RegEx Dictionary
.
Provide a name for the dictionary and choose whether the new dictionary is case sensitive or not.
Click
Select File
. Locate and select your dictionary file, click
Open
to upload the file.
Under Advanced Options, you can set various conditions to narrow down the results when this dictionary is used in a DLP rule. For more information, see the
Advanced Options
section.
Data Type
Data Types allow you to group the entities into clearly defined categories. You can select an existing one or create your own.
Sensitivity Level
Sensitivity Level allows you to set the criticality of the DLP Entity.
Advanced Options
The Advanced Options enable you to set conditions that can help you narrow down the search results for the entity when used in a DLP rule. The following are the Advanced Options.
Begins with, Ends with, Does not match
: provides you options to add conditions to include or exclude specific keywords or regexes.
Use Filters
— provides two filters: “Common-Sense” and “Unlikely Matches”.
The “Common-Sense” filter rejects a match that consists primarily of repeating or sequential characters. For example, “
aabbcc
” or “
22222
“.
The “Unlikely Matches” filter rejects an unlikely match by examining the characters present before or after the matched data. For example, “
80*125752000=10060160000"
does not likely contain a 9-digit US Social Security Number of any interest, so this match would be rejected.
Use Validators For Regex
— provides three common validation algorithm options (“Luhn”, “Elfproef”, and “Verhoeff”) to reject matches that do not pass the validation check for the selected algorithm.
In this Topic
DLP Entity

---
## Data Loss Prevention
**URL:** https://docs.netskope.com/en/data-loss-prevention/
**Last Modified:** 2026-02-18T21:53:34+00:00
**Scraped:** 2026-08-23T07:22:48.690510+00:00

Data Loss Prevention - Netskope Technical Documentation
Data Loss Prevention
The definition of
Data Loss Prevention
encompasses a set of practices and tools meant to prevent data leakage (also known as data exfiltration) by intentional and unintentional misuse. These practices and tools include encryption, detection, preventative measures, educational pop ups (for unintentional movements), and even machine learning to assess user risk scores. Over time, DLP has evolved into the realm of data protection and has become a premier feature of data protection deployment.
For more information for DLP in general, see
What is DLP
?
Netskope provides a comprehensive data loss prevention (DLP) enforcement solution for cloud applications and public cloud resources that is ideal for addressing regulatory compliance requirements and protecting sensitive data in your enterprise. The DLP profiles that enforce compliance and protect sensitive data consist of DLP rules that specify data identifiers. These data identifiers find content that should not be present in cloud app transactions or public cloud storage.
Building Regular Expressions
Data Lineage
DLP Detection
Data Loss Prevention On Demand
DLP Profiles
Using DLP with Netskope Public Cloud Security
Endpoint Data Loss Prevention
Digital Rights Management
In this Topic
Data Loss Prevention

---
## DLP On Demand Appliance
**URL:** https://docs.netskope.com/en/dlp-on-demand-appliance-2/
**Last Modified:** 2026-04-22T19:31:04+00:00
**Scraped:** 2026-08-23T07:23:45.346816+00:00

DLP On Demand Appliance - Netskope Technical Documentation
DLP On Demand Appliance
In this Topic
DLP On Demand Appliance

---
## AI Security Ops
**URL:** https://docs.netskope.com/en/ai-security-ops-dlp-agent/
**Last Modified:** 2026-07-17T22:18:13+00:00
**Scraped:** 2026-08-23T07:23:48.826293+00:00

AI Security Ops - Netskope Technical Documentation
AI Security Ops
In this Topic
AI Security Ops

---
## DLP On Demand Appliance Release Notes Version - 135.0.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-dlp-on-demand-appliance-135/
**Last Modified:** 2026-03-30T23:51:43+00:00
**Scraped:** 2026-08-23T07:41:04.653592+00:00

DLP On Demand Appliance Release Notes Version - 135.0.0 - Netskope Technical Documentation
DLP On Demand Appliance Release Notes Version - 135.0.0
Release Date: March 30, 2026
This release provides several improvements for Netskope’s DLP On Demand appliance, such as new features, enhancements, known issues, and fixed issues.
What's New
Fixed Issues

---
## DLP On Demand Appliance Release Notes Version - 135.0.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-dlp-on-demand-appliance-135/
**Last Modified:** 2026-03-30T23:52:04+00:00
**Scraped:** 2026-08-23T07:41:05.814931+00:00

DLP On Demand Appliance Release Notes Version - 135.0.0 - Netskope Technical Documentation
DLP On Demand Appliance Release Notes Version - 135.0.0
Release Date: March 30, 2026
This release provides several improvements for Netskope’s DLP On Demand appliance, such as new features, enhancements, known issues, and fixed issues.
What's New
Fixed Issues

---
## DLP On Demand Appliance Release Notes Version - 135.0.0
**URL:** https://docs.netskope.com/en/dlp-on-demand-appliance-release-notes-version-135/
**Last Modified:** 2026-03-31T02:26:52+00:00
**Scraped:** 2026-08-23T07:41:06.977743+00:00

DLP On Demand Appliance Release Notes Version - 135.0.0 - Netskope Technical Documentation
DLP On Demand Appliance Release Notes Version - 135.0.0
Release Date: March 30, 2026
This release provides several improvements for Netskope’s DLP On Demand appliance, such as new features, enhancements, known issues, and fixed issues.
What's New
Fixed Issues

---
## AI Security Ops Release Notes Version - March 2026
**URL:** https://docs.netskope.com/en/ai-security-ops-dlp-agent-release-notes-version-136-1/
**Last Modified:** 2026-07-17T21:10:48+00:00
**Scraped:** 2026-08-23T07:41:36.362775+00:00

AI Security Ops Release Notes Version - March 2026 - Netskope Technical Documentation
AI Security Ops Release Notes Version - March 2026
Introducing the launch of the new
Netskope AI Security Ops Agent
, designed to help your Data Protection team cut through the noise of millions of daily DLP incidents. This agent enables to quickly identify top data protection gaps and risks, shifting the focus from time-consuming incident triaging to efficient investigation and response.
See the
AISecOps DLP Agent documentation here
.
This initial release features:
Key Benefits
Automated ‘Case’ and ‘View’ Creation:
The agent identifies important gaps and risks into high-priority
Cases
and groups related, not-so-serious incidents into
Views
, ensuring attention is focused on the most critical threats.
Assisted Investigation:
The agent automatically gathers, enriches, and ties together context from across the Netskope platform and external systems, providing a verdict, recommendations, and clear reasoning.
End-to-End Response Workflows:
Provides comprehensive Triage, Investigate, and Respond workflows, including the ability for the agent to trigger recommended response actions to close the loop and significantly reduce Mean Time to Resolution (MTTR).

---
## DLP On Demand Appliance Release Notes Version - 139.0.0
**URL:** https://docs.netskope.com/en/dlp-on-demand-appliance-release-notes-version-139-0-0-0-0/
**Last Modified:** 2026-07-06T22:14:18+00:00
**Scraped:** 2026-08-23T07:43:06.323513+00:00

DLP On Demand Appliance Release Notes Version - 139.0.0 - Netskope Technical Documentation
DLP On Demand Appliance Release Notes Version - 139.0.0
Release Date: July 6, 2026
This release provides several improvements for Netskope’s DLP On Demand appliance, such as new features, enhancements, known issues, and fixed issues.
New Feature: DLPoD Appliance Pod Resource Auto-Scaling
The DLPoD appliance now detects hardware profile changes and automatically updates each pod’s CPU and memory limits on restart. Previously, pods retained their original resource limits even after the appliance hardware was scaled up or down. For example, scaling from 16 cores and 32 GB RAM to 32 cores and 64 GB RAM and restarting will now apply the updated limits across all pods. This applies to both scaling up and scaling down.
Note:
Resize the appliance only using the supported hardware profiles. See
Appliance Setup
for the supported profiles.
