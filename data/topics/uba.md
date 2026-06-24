# Netskope Docs — Uba
_Generated: 2026-06-24 10:30 UTC_
_Pages: 22_

---
## Deactivated User Behavior in Workplace from Meta
**URL:** https://docs.netskope.com/en/deactivated-user-behavior-in-workplace-from-meta/
**Last Modified:** 2025-08-31T01:41:56+00:00
**Scraped:** 2026-06-24T09:28:10.911743+00:00

Deactivated User Behavior in Workplace from Meta - Netskope Knowledge Portal
Deactivated User Behavior in Workplace from Meta
This article describes how API Data Protection deals when a user is deactivated in “Workplace from Meta”.
User State
Behavior
Deactivate
(temporary suspension)
Policy Processing: Netskope cannot carry out any policy action on deleted users’ posts/file attachments.
API Data Protection Dashboard: Deleted user gets removed from the API Data Protection dashboard.
Note
A new “Workplace from Meta” user has to accept the invitation and log in at least once before user-listing kicks in.
In this Topic
Deactivated User Behavior in Workplace from Meta

---
## Deleted/Deactivated User Behavior in Egnyte
**URL:** https://docs.netskope.com/en/deleted-deactivated-user-behavior-in-egnyte/
**Last Modified:** 2025-08-31T01:40:17+00:00
**Scraped:** 2026-06-24T09:28:17.542087+00:00

Deleted/Deactivated User Behavior in Egnyte - Netskope Knowledge Portal
Deleted/Deactivated User Behavior in Egnyte
This article describes how API Data Protection deals when a user is either deleted or deactivated in Egnyte.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Deactivated
Same behavior as above.
Corner cases:
If a user uploads a file on a shared and/or private folder and immediately after that the user is deleted or deactivated, here is how API Data Protection handles this scenario:
Upload a file on a shared folder followed by user deletion: Policy processing will go ahead.
Upload a file on a private folder followed by user deletion: Policy processing will stop.
Upload a file on a shared folder followed by user deactivation: Policy processing will go ahead.
Upload a file on a private folder followed by user deactivation: Policy processing will go ahead.
Note
User listing will occur for a new user even if the user does not login. However, a new user is expected to log in at least once for API Data Protection to process any policy.
In this Topic
Deleted/Deactivated User Behavior in Egnyte

---
## Deleted/Suspended User Behavior in Dropbox
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-dropbox/
**Last Modified:** 2025-08-31T01:40:11+00:00
**Scraped:** 2026-06-24T09:28:18.643739+00:00

Deleted/Suspended User Behavior in Dropbox - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Dropbox
This article describes how API Data Protection deals when a user is either deleted or suspended in Dropbox.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
Note
A new Dropbox user has to log in at least once before user-listing kicks in.
In this Topic
Deleted/Suspended User Behavior in Dropbox

---
## Deleted/Suspended User Behavior in Box
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-box/
**Last Modified:** 2025-08-31T01:39:55+00:00
**Scraped:** 2026-06-24T09:28:19.744681+00:00

Deleted/Suspended User Behavior in Box - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Box
This article describes how API Data Protection deals when a user is either deleted or suspended in Box.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
Note
A new Box user who does not accept the Box terms and conditions will be treated the same way as above.
In this Topic
Deleted/Suspended User Behavior in Box

---
## Deleted/Suspended User Behavior in Gmail
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-gmail/
**Last Modified:** 2025-08-31T01:40:31+00:00
**Scraped:** 2026-06-24T09:28:20.844022+00:00

Deleted/Suspended User Behavior in Gmail - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Gmail
This article describes how API Data Protection deals when a user is either deleted or suspended in Gmail.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any policy action on deleted users’ email/file attachments.
API Data Protection Dashboard: Deleted users’ email or file attachment may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
In this Topic
Deleted/Suspended User Behavior in Gmail

---
## Deleted/Suspended User Behavior in Microsoft Office 365 SharePoint
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-microsoft-office-365-sharepoint/
**Last Modified:** 2025-08-31T01:41:18+00:00
**Scraped:** 2026-06-24T09:28:21.964465+00:00

Deleted/Suspended User Behavior in Microsoft Office 365 SharePoint - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Microsoft Office 365 SharePoint
This article describes how API Data Protection deals when a user is either deleted or suspended in SharePoint.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
Note
When a user is suspended, account suspension notification is generated as part of audit logs.
In this Topic
Deleted/Suspended User Behavior in Microsoft Office 365 SharePoint

---
## Deleted/Suspended User Behavior in Google Drive
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-google-drive/
**Last Modified:** 2025-08-31T01:40:41+00:00
**Scraped:** 2026-06-24T09:28:23.093298+00:00

Deleted/Suspended User Behavior in Google Drive - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Google Drive
This article describes how API Data Protection deals when a user is either deleted or suspended in Google Drive.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
Corner cases:
If a user uploads a file on a shared and/or private folder and immediately after that the user is deleted or deactivated, here is how API Data Protection handles this scenario:
Upload a file on a shared folder followed by user deletion: Policy processing will go ahead.
Upload a file on a private folder followed by user deletion: Policy processing will stop.
Upload a file on a shared folder followed by user deactivation: Policy processing will go ahead.
Upload a file on a private folder followed by user deactivation: Policy processing will go ahead.
In this Topic
Deleted/Suspended User Behavior in Google Drive

---
## Deleted/Suspended User Behavior in Microsoft Office 365 OneDrive
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-microsoft-office-365-onedrive/
**Last Modified:** 2025-08-31T01:40:55+00:00
**Scraped:** 2026-06-24T09:28:24.216386+00:00

Deleted/Suspended User Behavior in Microsoft Office 365 OneDrive
This article describes how API Data Protection deals when a user is either deleted or suspended in OneDrive.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
Note
When a user is suspended, account suspension notification is generated as part of audit logs.
In this Topic
Deleted/Suspended User Behavior in Microsoft Office 365 OneDrive

---
## Deleted/Suspended User Behavior in Microsoft Office 365 Outlook
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-microsoft-office-365-outlook/
**Last Modified:** 2025-08-31T01:41:02+00:00
**Scraped:** 2026-06-24T09:28:25.321209+00:00

Deleted/Suspended User Behavior in Microsoft Office 365 Outlook - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Microsoft Office 365 Outlook
This article describes how API Data Protection deals when a user is either deleted or suspended in Outlook.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any policy action on deleted users’ email/file attachments.
API Data Protection Dashboard: Deleted users’ email or file attachment may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
In this Topic
Deleted/Suspended User Behavior in Microsoft Office 365 Outlook

---
## Deleted/Suspended User Behavior in Microsoft Office 365 Teams
**URL:** https://docs.netskope.com/en/deleted-suspended-user-behavior-in-microsoft-office-365-teams/
**Last Modified:** 2025-08-31T01:41:22+00:00
**Scraped:** 2026-06-24T09:28:26.420743+00:00

Deleted/Suspended User Behavior in Microsoft Office 365 Teams - Netskope Knowledge Portal
Deleted/Suspended User Behavior in Microsoft Office 365 Teams
This article describes how API Data Protection deals when a user is either deleted or suspended in Microsoft Teams.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any policy action on deleted users’ file attachments or messages.
API Data Protection Dashboard: Deleted users’ file attachment or messages may exist in dashboard, but in-actionable.
Suspended
Same behavior as above.
Note
When a user is suspended, account suspension notification is generated as part of audit logs.
In this Topic
Deleted/Suspended User Behavior in Microsoft Office 365 Teams

---
## Deleted User Behavior in Slack Teams
**URL:** https://docs.netskope.com/en/deleted-user-behavior-in-slack-teams/
**Last Modified:** 2025-08-31T01:41:49+00:00
**Scraped:** 2026-06-24T09:28:27.522067+00:00

Deleted User Behavior in Slack Teams - Netskope Knowledge Portal
Deleted User Behavior in Slack Teams
This article describes how API Data Protection deals when a user is deleted in Slack for Teams.
User State
Behavior
Deleted
Policy processing: Policy processing is based on Slack channels. Irrespective of a user deletion, there is no impact on policy processing.
API Data Protection Dashboard: Deleted users’ file attachments or messages may exist in dashboard, but in-actionable.
In this Topic
Deleted User Behavior in Slack Teams

---
## Deleted User Behavior in Cisco Webex Teams
**URL:** https://docs.netskope.com/en/deleted-user-behavior-in-cisco-webex-teams/
**Last Modified:** 2025-08-31T01:40:02+00:00
**Scraped:** 2026-06-24T09:28:29.717295+00:00

Deleted User Behavior in Cisco Webex Teams - Netskope Knowledge Portal
Deleted User Behavior in Cisco Webex Teams
This article describes how API Data Protection deals when a user is deleted in Cisco Webex Teams.
User State
Behavior
Deleted
Policy processing: Netskope cannot carry out any policy action on deleted users’ files and text messages.
API Data Protection Dashboard: Deleted users’ data gets removed from the API Data Protection dashboard.
Note
A new user has to accept the invitation before user-listing kicks in.
In this Topic
Deleted User Behavior in Cisco Webex Teams

---
## Deleted User Behavior in Slack Enterprise
**URL:** https://docs.netskope.com/en/deleted-user-behavior-in-slack-enterprise/
**Last Modified:** 2025-08-31T01:41:42+00:00
**Scraped:** 2026-06-24T09:28:30.816590+00:00

Deleted User Behavior in Slack Enterprise - Netskope Knowledge Portal
Deleted User Behavior in Slack Enterprise
This article describes how API Data Protection deals when a user is deleted in Slack for Enterprise.
User State
Behavior
Deleted
Policy processing: Policy processing is based on Slack channels. Irrespective of a user deletion, there is no impact on policy processing.
API Data Protection Dashboard: Deleted users’ file attachments or messages may exist in dashboard, but in-actionable.
In this Topic
Deleted User Behavior in Slack Enterprise

---
## Inactive/Freeze User Behavior in Salesforce
**URL:** https://docs.netskope.com/en/inactive-freeze-user-behavior-in-salesforce/
**Last Modified:** 2025-08-31T01:41:28+00:00
**Scraped:** 2026-06-24T09:30:07.520330+00:00

Inactive/Freeze User Behavior in Salesforce - Netskope Knowledge Portal
Inactive/Freeze User Behavior in Salesforce
This article describes how API Data Protection deals when a user is either inactive or frozen in Salesforce.
User State
Behavior
Inactive
Policy processing: Netskope cannot carry out any file operation (actions) for deleted users’ files.
Retro scan: Netskope does not get any file listing for a deleted user.
API Data Protection Dashboard: Deleted users’ file may exist in dashboard, but in-actionable.
Freeze
Same behavior as above.
In this Topic
Inactive/Freeze User Behavior in Salesforce

---
## Removed/Blocked User Behavior in GitHub
**URL:** https://docs.netskope.com/en/removed-blocked-user-behavior-in-github/
**Last Modified:** 2025-08-31T01:40:23+00:00
**Scraped:** 2026-06-24T09:32:25.173094+00:00

Removed/Blocked User Behavior in GitHub
This article describes how API Data Protection deals when a user is either removed or blocked in GitHub.
User State
Behavior
Removed
(An administrator can remove a user from the organization or accessing a repository.)
Policy processing: Netskope cannot carry out any policy processing associated with a removed user.
Deleted user will be removed from the API Data Protection dashboard.
Blocked
(An administrator can block a user in GitHub.)
Same behavior as above. Netskope does not list blocked user.
In this Topic
Removed/Blocked User Behavior in GitHub

---
## Advanced UEBA Quick Start
**URL:** https://docs.netskope.com/en/advanced-ueba-quick-start/
**Last Modified:** 2026-06-04T21:24:55+00:00
**Scraped:** 2026-06-24T09:48:45.018321+00:00

Advanced UEBA Quick Start - Netskope Knowledge Portal
Advanced UEBA Quick Start
Once Advanced UEBA is enabled in your account, the recommended next step is to disable the Standard UEBA policies.
Machine Learning detections in Advanced UEBA will automatically learn the baselines for different users and raise individual alerts if there is anomalous behavior. Therefore, best practice is to disable the Standard UEBA policies.
The table below provides examples of the Advanced UEBA policies that will supersede the corresponding Standard UEBA policies.
Standard UEBA Policy
Advanced UEBA Equivalent Example
Improvements
Bulk Failed Login
A user-based spike in failed login attempts
Advanced UEBA will build a baseline and alert when there is a deviation as opposed to a statically configured threshold.
Bulk Delete
A user-based spike in files deleted detected from real-time protection
Advanced UEBA will build a baseline and alert when there is a deviation as opposed to a statically configured threshold.
Bulk Upload
A user-based spike in sensitive data uploaded to personal apps
Advanced UEBA will build a baseline and alert when there is a deviation as opposed to a statically configured threshold. In addition, Advanced UEBA also takes into account the nature of the data being moved by looking at associated DLP policy violation alerts.
Bulk Download
A user-based spike in sensitive files downloaded
Advanced UEBA will build a baseline and alert when there is a deviation as opposed to a statically configured threshold. In addition, Advanced UEBA also takes into account the nature of the data being moved by looking at associated DLP policy violation alerts.
Proximity
First access from an IP block for the organization
Advanced UEBA identifies a compromised credential being used when authentication or an admin activity happening from a network that has never been used before. This is higher fidelity compared to using ‘impossible travel’ to find possibly malicious activity because it hones in on specific malicious activity.
Risky Countries
First access from an IP block for the organization
Advanced UEBA identifies compromised credentials using a more precise and baseline-based policy that uses IP blocks as opposed to a static country list.
Suspicious Data Movement
Potential sensitive data movement
Advanced UEBA will build a baseline as well as monitor a wider range of application and app instances with no pre-configuration. In addition, Advanced UEBA policies do not require labeling of instances by the customer.
Rare Event
The 16+ policies beginning with “First access”
Advanced UEBA uses a more precise set of policies to identify compromised credentials and insiders while significantly reducing the false positives from rare events that aren’t indicative of an insider threat or compromise.
Shared Credentials
Numerous policies that cover scenarios for
Compromised credentials
and
Insider Threats
with higher fidelity of detection examples:
Potential compromised credential being used from a non-Netskope IP address
Access from an unusual country for the organization
Access from an unusual country for the user
Activity detected outside user’s regular working hours
AWS IAM activity without MFA from a non-Netskope IP address
Compromised credential found in a data breach
Advanced UEBA uses a more precise set of policies to identify compromised credentials and insiders while significantly reducing the false positives from credential sharing that aren’t indicative of an insider threat or compromise.
Setting Up a Low UCI Threshold Alert
You should
ensure that an alert is generated
every time a UCI score drops below a threshold. A low UCI alert is a signal that there is a user whose activity warrants analyst review. To configure this:
Go to the
Incidents
>
Insider Threats & Advanced Compromise
.
click
for
Global UCI Alert
.
As a best practice, Netskope recommends setting the
User Confidence Index Threshold
to
651
so Netskope can generate an alert whenever a user’s UCI threshold drops below the “good” range and into the “moderate” range.
Setting Up a Process to Regularly Review Low UCI Users
A low UCI alert should trigger an analyst investigation. This alert will contain the user and information on the
Key Detection Scenario
that describes the likely cause for this low confidence score. In the low UCI example alert below,
daniel@company.com
had a low UCI due to
Compromised device - Malware
.
The investigation begins by going to
Incidents
>
Insider Threats & Advanced Compromise
and clicking the user’s name. This page lists all users and their UCI scores in increasing order.
For the selected user, the page will display a timeline of their UCI score. Click the day that their UCI score dropped to see the individual anomalies contributing to the score. In this example, the list of anomalies indicates that
daniel@company.com
is likely infected with ransomware. Clicking each individual anomaly will show additional context and an event timeline.
If an anomaly or set of anomalies are not an indicator that the user has a compromised device, compromised account, or is acting as an insider threat, you can click
Mark as Allowed
to remove the impact on the UCI as shown below. Marking an anomaly as allowed will suppress this anomaly from recurring for the same user and the same feature for 45 days.
In this Topic
Advanced UEBA Quick Start

---
## Advanced UEBA Troubleshooting
**URL:** https://docs.netskope.com/en/advanced-ueba-troubleshooting/
**Last Modified:** 2026-04-10T22:22:46+00:00
**Scraped:** 2026-06-24T09:48:46.112464+00:00

Advanced UEBA Troubleshooting - Netskope Knowledge Portal
Advanced UEBA Troubleshooting
If there is a large amount of users with low UCI scores and the cause seems to be something upstream, like a DLP policy that is raising a large amount of violations, then the solution is to tune the upstream policy.
If this does not appear to be an upstream issue but rather an issue in the UEBA policy itself – for example, an ML-based unusual user agent detection that is raising a large amount of alerts – then there are two possible courses of action.
If the volume is acceptable but the impact to the UCI is large, the recommended next step is tuning the score and severity down to a range that does not result in a large number of users with low UCI scores.
If the volume and UCI impact are both unacceptable, then the remaining solution is to disable this policy and file a support ticket. This should be a rare course of action, since the policies have been pre-tuned so an average organization does not have a lot of alerts.
In this Topic
Advanced UEBA Troubleshooting

---
## Third-party Integrations with Advanced UEBA
**URL:** https://docs.netskope.com/en/third-party-integrations-with-advanced-ueba/
**Last Modified:** 2026-04-10T22:22:21+00:00
**Scraped:** 2026-06-24T09:48:47.208415+00:00

Third-party Integrations with Advanced UEBA - Netskope Knowledge Portal
Third-party Integrations with Advanced UEBA
Using the REST API to Ingest External Alerts
By using the REST API, organizations that have detections from other platforms can consume the alerts to impact the UCI. The documentation for this API endpoint can be found
here
.
Using the REST API to Share UCI
Admins can export the UCI to share with other platforms via the REST endpoint.
POST /api/v2/incidents/uba/getuci
The documentation for this endpoint can be found in the REST API v2 docs in the Netskope UI.
Using Cloud Exchange to Share UCI
Users’ scores can be shared with other platforms using
Cloud Risk Exchange
. UCI can also drive CTO (Cloud Ticket Orchestrator) to automate workflow for investigations.
In this Topic
Third-party Integrations with Advanced UEBA

---
## Advanced UEBA SOC Detections Pack
**URL:** https://docs.netskope.com/en/advanced-ueba-soc-detections-pack/
**Last Modified:** 2026-04-22T12:45:39+00:00
**Scraped:** 2026-06-24T09:56:02.810926+00:00

Advanced UEBA SOC Detections Pack - Netskope Knowledge Portal
Advanced UEBA SOC Detections Pack
Additional licensing is required. Contact your Netskope account team to enable this feature.
Netskope is expanding Advanced UEBA’s existing portfolio of 160 ML based policies with a new SOC Detections Pack that introduces a patented approach for C2 beacon detection. Command and Control (C2) tools, such as Cobalt Strike, employ malleable profiles (patterns that cannot be fingerprinted using tools such as IPS) to circumvent traditional defenses. The SOC Detections Pack enhances Advanced UEBA by providing early detection of compromised devices where C2 beacons have been deployed.
The new license includes 15 new C2 beacon detection policies today and many more forthcoming additional detections. These new C2 detection policies analyze web traffic to identify anomalous C2 callbacks and use machine learning models to isolate C2 frameworks (such as Mythic and Cobalt Strike) from benign callbacks (such as software update checks).
For customers who recognize the importance of C2 beacon detection, the Advanced UEBA – SOC Detections Pack offers significant value for detecting early compromise.
The full list of Advanced UEBA C2 policies is visible to Netskope accounts with the SOC Detections Pack license enabled.
To learn more:
Effective C2 Beaconing Detection white paper
Advancing C2 Beacon Detection blog
In this Topic
Advanced UEBA SOC Detections Pack

---
## HPE Aruba Networking Central Plugin for Risk Exchange
**URL:** https://docs.netskope.com/en/hpe-aruba-networking-central-plugin-for-risk-exchange/
**Last Modified:** 2026-05-27T22:46:10+00:00
**Scraped:** 2026-06-24T09:56:29.866439+00:00

HPE Aruba Networking Central Plugin for Risk Exchange - Netskope Knowledge Portal
HPE Aruba Networking Central Plugin for Risk Exchange
This document explains how to configure the HPE Aruba Networking Central v1.0.0 plugin with the Risk Exchange module of the Netskope Cloud Exchange platform. This plugin is used to fetch Wired and Wireless clients data from Aruba Networking Central of HPE Greenlake. It retrieves the clients from the
Aruba Networking Central > Clients
page. This plugin also supports performing Add client to blacklist, Remove client from blacklist, and Disconnect client from networking device actions on Aruba Networking Central.
Prerequisites
To complete this integration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Risk Exchange
plugin already configured.
Connectivity to the HPE GreenLake platform.
A subscription for HPE Aruba Networking Central service.
Access to generate Client ID, Client Secret, and pull wired/wireless clients.
Connectivity to the following host:
https://*.central.arubanetworks.com
.
HPE Aruba Networking Central Plugin Support
This plugin is used to fetch Wired and Wireless clients data from Aruba Networking Central of HPE Greenlake. It retrieves the clients from the
Aruba Networking Central > Clients
page. This plugin also supports performing Add client to blacklist, Remove client from blacklist, and Disconnect client from networking device actions on Aruba Networking Central.
Type of Data Pulled
Actions Supported
Wired clients
Wireless clients
Add client to blacklist
Remove client from blacklist
Disconnect client from networking device
Mappings
Mappings are used to view the pulled wired and wireless clients and their respective details. Fields mapped during plugin configuration will be visible on the
Records
page after the data is pulled. Here are the suggested mappings to use while configuring the plugin.
Pull Mappings
Plugin Field
Expected Datatype
Suggested Field Name
Suggested Field Aggregate Strategy
MAC Address
String
MAC Address
Unique
Client Type
String
Client Type
Overwrite
IPv4
String
IPv4
Overwrite
Username
String
Username
Overwrite
VLAN
String
VLAN
Overwrite
Associated Device MAC Address
String
Associated Device MAC Address
Overwrite
Associated Device Serial Number
String
Associated Device Serial Number
Overwrite
Hostname
String
Hostname
Overwrite
Name
String
Name
Overwrite
Group Name
String
Group Name
Overwrite
Swarm ID
String
Swarm ID
Overwrite
Authentication Type
String
Authentication Type
Overwrite
Encryption Method
String
Encryption Method
Overwrite
Connection Standard
String
Connection Standard
Overwrite
Operating System Type
String
Operating System Type
Overwrite
Permissions
For fetching clients and performing actions using the plugin, you will need these roles:
HPE Greenlake Platform > Workspace Observer
HPE Aruba Networking Central > Aruba Central view edit role
API Details
List of APIs Used
List of APIs Used
API Endpoint
Method
Use Case
/oauth2/authorize/central/api/login
POST
Generate Access token step 1: Login and obtain Session and CSRF token
/oauth2/authorize/central/api
POST
Generate Access token step 2: Obtain authorization code
/oauth2/token
POST
Generate Access token step 3: Obtain Access and refresh token
/oauth2/token
POST
Regenerate access and refresh token
/monitoring/v1/clients/wireless
GET
Pull wireless clients
/monitoring/v1/clients/wired
GET
Pull wired clients
/configuration/v1/swarm/
<device_id>
/blacklisting
POST
Add client to blacklist
/configuration/v1/swarm/
<device_id>
/blacklisting
DELETE
Remove client from blacklist
/device_management/v1/device/
<device_serial>
/action/disconnect_user
POST
Disconnect client from networking device
Authorization
Generate access token Step 1
API Endpoint:
/oauth2/authorize/central/api/login
Method:
POST
Headers:
Key
Value
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Body:
Key
Value
username
abc.xyz@pqr.com
password
abc123xyz
Parameters:
Key
Value
Description
client_id
6xioIybft2hW5s8keMQPSxAc4XJGfLf8
Aruba networking central client ID
Sample API Response
Response body:
{"status":true}
Response Headers:
{
    "Server": "openresty/1.13.6.2",
    "Date": "Wed, 16 Apr 2025 09:36:57 GMT",
    "Content-Type": "application/json",
    "Content-Length": "16",
    "Connection": "keep-alive",
    "X-RateLimit-Limit-Second": "3",
    "X-RateLimit-Remaining-Second": "0",
    "Cache-Control": "no-cache, no-store, must-revalidate, private",
    "Pragma": "no-cache",
    "Set-Cookie": "csrftoken=IjdkMGABRFVkYTA23ftqN2M3ialjMDBiNjUyYTIzYzZiO83F2BViZDQi.Z_96OQ.6qxNHAMZKZOGqSHgPSYiy77Rg38; Secure; Path=/, session=e8067gfte772a53b_67ff7a39.OO4EUpf-lqpXP5QTvCD64flNbJy0; Secure; HttpOnly; Path=/"
}
Generate access token Step 2
API Endpoint:
/oauth2/authorize/central/api
Method:
POST
Headers
Key
Value
Description
Cookie
e8067gfte772a53b_67ff7a39.OO4EUpf-lqpXP5QTvCD64flNbJy0
Session token (Cookie) obtained from generate access token step 1
X-CSRF-TOKEN
IjdkMGABRFVkYTA23ftqN2M3ialjMDBiNjUyYTIzYzZiO83F2BViZDQi.Z_96OQ.6qxNHAMZKZOGqSHgPSYiy77Rg38
CSRF Token obtained from generate access token step 1
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
User agent
Parameters
Key
Value
client_id
6xioIybft2hW5s8keMQPSxAc4XJGfLf8
response_type
code
scope
all
Body
Key
Value
Description
customer_id
z04d7db8e34al3x9aed754ebb74bce52
Aruba Networking Central Customer ID.
Sample API Response
{
"auth_code": "dfmyIjq3cZ5G1ofsxS4Dgl122q0vQyE"
}
Generate access token step 3
API Endpoint:
/oauth2/token
Method:
POST
Headers:
Key
Value
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Body:
Key
Value
Description
client_id
6xioIybft2hW5s8keMQPSxAc4XJGfLf8
Aruba Networking central client ID
client_secret
ivlV40m8SDM3Sgck4ClqdrskkSRya9fB2
Aruba Networking central client secret
grant_type
authorization_code
Token grant type
code
dfmyIjq3cZ5G1ofsxS4Dgl122q0vQyE
Auth_code obtained from generate access token step 2
Sample API Response
{
    "refresh_token": "knsdFAjnfEFks34adf76WDKW62jad",
    "token_type": "bearer",
    "access_token": "Nfjad8449NFf7asd0ea3wj3FFmwlald",
    "expires_in": 7200
}
Regenerate access and refresh token
API Endpoint:
/oauth2/token
Method:
POST
Headers:
Key
Value
Authorization
Bearer
<Token>
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Parameters:
Key
Value
Description
client_id
6xioIybft2hW5s8keMQPSxAc4XJGfLf8
Aruba Networking central client ID
client_secret
ivlV40m8SDM3Sgck4ClqdrskkSRya9fB2
Aruba Networking central client secret
grant_type
refresh_token
Token grant type
refresh_token
knsdFAjnfEFks34adf76WDKW62jad
Refresh token obtained from generate access token step 3
Sample API Response
{
    "refresh_token": "5nadsiuef7F7aFJ02pdam",
    "token_type": "bearer",
    "access_token": "naknfde7faoijfdioREMD9e3s",
    "expires_in": 7200
}
Pull Wireless Clients
API Endpoint:
/monitoring/v1/clients/wireless
Method:
GET
Headers:
Key
Value
Authorization
Bearer <Token>
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Parameters:
Key
Value
Description
limit
1000
Pagination limit
offset
0
Pagination offset
Sample API Response:
{
    "clients": [
        {
            "associated_device": "Network device 0",
            "associated_device_mac": "23:7f:de:3f:61:27",
            "associated_device_name": "23:7f:de:3f:61:27",
            "authentication_type": "",
            "band": 5,
            "channel": "100 (80 MHz)",
            "client_category": "Home Audio/Video Equipment",
            "client_type": "WIRELESS",
            "connected_device_type": "AP",
            "connection": "802.11ac",
            "encryption_method": "WPA2_PSK",
            "failure_stage": "",
            "group_id": 0,
            "group_name": "default",
            "health": 92,
            "hostname": "Google-Home",
            "ht_type": 5,
            "ip_address": "32.127.208.96",
            "label_id": [],
            "labels": [],
            "last_connection_time": 1742203795505,
            "macaddr": "27:88:56:2a:ac:c8",
            "manufacturer": "Google, Inc.",
            "maxspeed": 433,
            "name": "WirelessClient0",
            "network": "netskope",
            "os_type": "Chromecast Media Player",
            "phy_type": 1,
            "radio_mac": "23:7f:de:3f:61:27",
            "radio_number": 0,
            "signal_db": -64,
            "signal_strength": 4,
            "snr": 28,
            "speed": 325,
            "swarm_id": "1jLK1NxqiVhglBXXN2qA5BYiWuFCUejF2Fz8Yx5kRYORIiByix",
            "user_role": "netskope",
            "username": "user.name@domain.com",
            "vlan": 244
        }
    ],
    "count": 1
}
Pull Wired Clients
API Endpoint:
/monitoring/v1/clients/wired
Method:
GET
Headers:
Key
Value
Authorization
Bearer <Token>
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Parameters:
Key
Value
Description
limit
1000
Pagination limit
offset
0
Pagination offset
Sample API Response
{
    "clients": [
        {
            "macaddr": "74:84:b4:11:af:b3",
            "name": "WiredClient0",
            "ip_address": "137.115.81.35",
            "username": "User.name@domain.com",
            "associated_device": "Network device 0",
            "group_name": "default",
            "interface_mac": "dd:e2:cb:7d:5c:fa",
            "interface_port": 63526,
            "vlan": 456,
            "associated_device_name": "dd:e2:cb:7d:5c:fa",
        }
    ],
    "count": 1
}
Add Clients to a Blacklist
API Endpoint:
/configuration/v1/swarm/<device_id>/blacklisting
Method:
POST
Headers:
Key
Value
Authorization
Bearer <Token>
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Parameter:
Key
Value
Description
device_id
14b3743c01f8080bfa07ca053ef1e895df9c0680fe5a17bfd5
Swarm ID/Device id of virtual controller or C2C access point from where client will be blacklisted.
Body:
Key
Value
Description
blacklist
List of <client_mac_address>
List of client Mac addresses to be blacklisted
Remove Clients from a Blacklist
API Endpoint:
/configuration/v1/swarm/<device_id>/blacklisting
Method:
DELETE
Headers:
Key
Value
Authorization
Bearer <Token>
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Parameter:
Key
Value
Description
device_id
14b3743c01f8080bfa07ca053ef1e895df9c0680fe5a17bfd5
Swarm ID/Device id of virtual controller or C2C access point from where client will be blacklisted.
Body:
Key
Value
Description
blacklist
List of <client_mac_address>
List of client Mac addresses to be un-blacklisted
Disconnect a Client from a Networking Device
API Endpoint:
/configuration/v1/swarm/<device_id>/blacklisting
Method:
DELETE
Headers:
Key
Value
Authorization
Bearer <Token>
User-Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Parameter:
Key
Value
Description
device_serial
FT592BGL
Serial number of networking device from where client will be disconnected
Body:
Key
Value
Description
disconnect_user_mac
<client_mac_address>
Mac address of device to be disconnected from networking device
Sample API response
{
    "serial": "FT592BGL",
    "state": "QUEUED",
    "task_id": 17447940919521
}
Performance Matrix
These performance readings are conducted on a Large CE Stack with these VM specifications by pulling 500K wired clients and wireless clients from the HPE Aruba Networking Central plugin.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Wired clients fetched from the HPE Aruba Networking Central
~26.2k per minute
Wireless clients fetched from the HPE Aruba Networking Central
~23.6k per minute
User Agent
netskope-ce-5.1.1-cre-hpe-aruba-networking-central-v1.0.0
Workflow
Get your API Base URL, Client ID, Client Secret and Customer ID from HPE GreenLake platform.
Configure the HPE Aruba Networking Central plugin.
Add a Business Rule.
Add Actions.
Validate the HPE Aruba Networking Central plugin.
Click play to watch a video.
Get your API Base URL, Client ID, Client Secret and Customer ID from HPE GreenLake
To get your API Base URL, Client ID, and Client Secret:
Log in to your HPE GreenLake account, and go to your workspace.
Go to
Services > Catalog
and search for
HPE Aruba Networking Centra
l.
Click on the service and click
Add Region
to deploy a service.
After successful deployment of the service, click
Launch
to start the service.
Go to
Organization > Platform Integration
and click
REST API
under the
API Gateway
section.
Under
APIs
you can find the
API Base URL.
You only need to copy the Base URL without the path to configure the plugin.
For example:
https://apigw-uswest5.central.arubanetworks.com
.
To get the Client ID and Client Secret, go to
My Apps & Tokens.
Click
Add Apps & Tokens
, and click
Generate
to generate the Client ID and Client Secret.
Save these to use while configuring the plugin.
For
Customer ID
, you click the
Profile
icon and copy the Customer ID.
Configure the HPE Aruba Networking Central Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
. Search for and select the
HPE Aruba Networking Central v1.0.o (CRE)
plugin box.
Enter a plugin configuration name, and change the sync interval if needed.
Click
Next
and enter the configuration parameters:
API Base URL: Your API Base URL for Aruba Networking Central instance.
Username: Your HPE Greenlake account username.
Password: Your HPE Greenlake account password.
Client ID: Your Aruba Networking Central Client ID.
Client Secret: Your Aruba Networking Central Client Secret.
Customer ID: Your Aruba Networking Central Customer ID.
Client Type: The Client Type to be fetched from Aruba Networking Central. Select at least one of the client types.
Click
Next
. Select the Entity from the
Entity
dropdown. The Entity fields can be created on the
Schema Editor
page, or using the
+ Add Field
option from the field dropdown. Provide the field mappings. For the suggested mapping please, refer to the Mappings section.
Click
Save
.
Add a Risk Exchange Business Rule for HPE Aruba Networking Central
In Risk Exchange, go to
Business Rules
and click
Create New Rule
in the top right corner.
Enter the Rule Name. Select the Entity for the Fields that were configured for the HPE Aruba Networking Central plugin, and configure the query based on your requirements.
Click
Save
.
Add Risk Exchange Actions for HPE Aruba Networking Central
The HPE Aruba Networking Central plugin supports the following action types:
Add a Client to a Blacklist
This action will add clients to the blacklist on HPE Aruba Networking Central.
Remove a Client from a Blacklist
This action will remove clients from the blacklist on HPE Aruba Networking Central.
Disconnect a Client from a Networking Device
This action will disconnect the client from an existing networking device.
No Action
No action will be performed for this action. You can generate UBA alerts in Ticket Orchestrator by using this action and enabling the
Generate Alerts
toggle.
You can perform the Netskope related actions on the clients pulled from HPE Aruba Networking Central. For more information about actions and their validations, refer to the
Risk Exchange guide
.
Configure an Action
Go to
Risk Exchange > Actions
and click
Add Action Configuration
.
Select a Business Rule, a Configuration, and an Action from their respective dropdowns.
For the
Disconnect a client from a networking device
action, select the field that has the MAC Address, and select the field that has the Device Serial mapped.
Enable the
Require Approval
toggle if Approval is needed before performing action.
If
Require Approval
is enabled, then to approve the action, go to
Risk Exchange > Action Logs
, select the action to be approved, and click
Approve
.
For the
Add a client to a blacklist
and
Remove a client from a blacklist
actions, you will have to provide the Client MAC Address and Swarm ID in the Action Parameters.
Click
Save
.
Validate the HPE Aruba Networking Central Plugin
Validate in Cloud Exchange
To verify the clients pulled from HPE Aruba Networking Central, go to
Logging
and search for the logs from CRE HPE Aruba Networking Central plugin.
To check the Disconnect client from the networking device, check the logs.
To check the records pulled and stored in Cloud Exchange, go to
Records
in Risk Exchange. Select the entity that you used while adding the mapping in the plugin configuration.
Validate in HPE Aruba Networking Central
The plugin pulls Wired and Wireless clients from HPE Aruba Networking Central. The clients are pulled from the Aruba
Networking Central > Clients > Connected
page.
To check the details of the client, click on any of the clients.
Troubleshooting HPE Aruba Networking Plugin
Receiving error in the plugin workflow
CRE HPE Aruba Networking Central [configuration_name]: Validation error occurred, Received exit code 401, Unauthorized, Verify Username, Password, Client ID, Client Secret and Customer ID provided in the configuration parameters.
What to do:
Verify the Client ID and Secret for HPE Aruba Networking Central. Refer to the
Get your API Base URL, Client ID, Client Secret and Customer ID from HPE GreenLake
section.
Clients are not pulled from HPE Aruba Networking Central
If no data for the Clients are pulled, it might be due to one of these reasons:
No client is available on the platform to pull
Mapping is not added in the plugin
What to do:
Go to HPE Aruba Networking Central and check if the clients are available to pull from the
Clients > Connected
page.
Edit the plugin configuration, and check the Entity Source page. There should be some fields mapped in order to pull the clients.
Unable to perform action on HPE Aruba Networking Central
If any client failed while performing Disconnect client from networking device action, it might be due to one of these reasons:
The client does not exist on HPE Aruba Networking Central.
The client is offline at the point of time.
What to do:
To check the connected clients, refer to
Validate in HPE Aruba Networking Central
section.
In this Topic
HPE Aruba Networking Central Plugin for Risk Exchange

---
## Advanced UEBA Best Practices
**URL:** https://docs.netskope.com/en/advanced-ueba-best-practices/
**Last Modified:** 2026-05-04T15:00:33+00:00
**Scraped:** 2026-06-24T10:05:51.238344+00:00

Advanced UEBA Best Practices - Netskope Knowledge Portal
Advanced UEBA Best Practices
The following sections outline the best practices to quickly and efficiently operationalize Advanced UEBA. The policy page for Advanced UEBA is found under
Policies
>
Insider Threats & Advanced Compromise
. Using the policies in the Insider Threats & Advanced Compromise page, you can perform the configuration steps below to fully utilize Advanced UEBA.
Advanced UEBA Quick Start
Advanced UEBA Optional Tuning
Advanced UEBA Troubleshooting
Third-party integrations with Advanced UEBA
In this Topic
Advanced UEBA Best Practices

---
## Advanced UEBA Optional Tuning
**URL:** https://docs.netskope.com/en/advanced-ueba-optional-tuning/
**Last Modified:** 2026-05-04T15:00:37+00:00
**Scraped:** 2026-06-24T10:05:52.338883+00:00

Advanced UEBA Optional Tuning - Netskope Knowledge Portal
Advanced UEBA Optional Tuning
The steps detailed in this section are optional and should be implemented based on organizational needs.
Configure Additional UEBA Policies
Admins will enable certain standard UEBA policies in addition to enabling the default disabled policies. The following sections describe and explain the circumstances for each case.
Standard UEBA Use Cases
Although, the recommended course of action in the getting started guide is to disable all the Standard UEBA policies, some organizations might have a use case that requires a standard UEBA policy. The following is a list of common use cases for standard UEBA.
Identifying traffic from a certain country or list of countries
The “Risky Countries” policy can generate an alert for every access from a country on a watchlist. This can be useful for reviewing activity from countries from which users are not authorized to work.
Identifying data movement to all non-managed app instances
Advanced UEBA has policies to identify data movement from managed application instances as well as data movement to personal application instances. However, if there is a need to also identify data movement to not only personal but all non-managed app instances, then the “Bulk Upload” policy can be used. This policy requires labeling each managed application instance and adding it to the exception criteria in the policy definition.
Enabling the Default Disabled Policies
There are Advanced UEBA policies (including “High severity malware alert” and “High severity DLP policy violation”) that come disabled by default. This is because these policies are dependent on account specific policy configurations. The following sections describe the process and conditions for enabling each of these policies.
New private app access for this user
This policy identifies if there are new NPA apps being accessed by an individual. If you are still enabling / adding NPA apps, we recommend this policy stay disabled. Once all the NPA apps have been onboarded, this policy can be safely enabled. Enabling this policy too early may cause a large number of alerts to be raised for newly onboarded applications.
Reduce UCI for DLP policy violations
There are four policies that impact the UCI score depending on the severity of the DLP policy violation.
Low Severity DLP policy violation
Medium Severity DLP policy violation
High Severity DLP policy violation
Critical Severity DLP policy violation
The severity of the DLP alert is determined by the thresholds in the DLP profile / rule referenced in the policy violation.
The severity of the policy violation maps to one of the Advanced UEBA policies, and, based on this you can map the required severity level and tune the desired impact in the Advanced UEBA policy as shown below. This impact should take into account the expected alert volume to reduce the UCI scores to moderate and poor values only in exceptional cases.
Reduce UCI for malware & malsite policy violations
There are four malware and one malsite policy to impact the UCI score for policy violations as shown below.
Malsite alert
Low severity malware alert
Medium severity malware alert
High severity malware alert
Patient zero malware alert
Unlike the DLP policies above, the severity of a Malware alert is determined internally by the threat detection service that raised the alert. However, similar to above, these Advanced UEBA policies can be enabled and configured to the desired score that does not result in numerous low UCI users.
Reduce UCI for third party app violations
There are four policies that reduce the UCI for strange or malicious behavior detected by third party cloud applications. These are triggered by an app event that is generated from an API connector audit log. Enable these if you need to see the UCI reduced as a result of suspicious behavior detected by upstream sources like Google Drive and Box. You do not need additional configurations in Advanced UEBA for these policies.
Suspicious activity detected by Google Drive
Device compromise detected by Google Drive
Device ownership change detected by Google Drive
Malicious file detected by Box
Manage Exclusion List
With Advanced UEBA admins can create a list of users within the same account to exclude from UCI scoring and UBA anomaly incidents.
Each account can only have one Exclusion List.
Use cases for the exclusion list include trusted users (e.g., SOC team) and regular users excluded for compliance with workers’ council requirements in certain countries.
Navigate to
Incidents
>
Insider Threats & Advanced Compromise
>
All Users
>
Manage Exclusion List
1.Click Manage Exclusion List and the Exclusion List window opens. Select the users, user groups, or organizational units to exclude or start typing in the field to view a subset of users.
2. Click
Save
.
3. Optionally, edit your list by selecting it again and making edits to the Exclusion List window.
When a user is added to the exclusion list, their historical data is not purged. The user is removed from the active users list after 48 hours and completely removed after 60 days. An excluded user’s UCI score is set to 1000 for Real-time Protection policies.
You will see the following message at the top of your list page as confirmation.
Exclusion List Audit Log
To view the audit log, navigate to
Settings
>
Administration
>
Audit Log
>
+Add Filter
>
Log Type
>
User Exclusion List Edited
The audit log captures the first time the exclusion list is created and each time it’s edited.
In this Topic
Advanced UEBA Optional Tuning
