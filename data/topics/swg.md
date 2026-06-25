# Netskope Docs — Swg
_Generated: 2026-06-25 10:01 UTC_
_Pages: 19_

---
## NGSWG Basic Policies
**URL:** https://docs.netskope.com/en/ngswg-basic-policies/
**Last Modified:** 2025-08-31T01:51:20+00:00
**Scraped:** 2026-06-25T08:57:19.169821+00:00

NGSWG Basic Policies
Here are some basic policy use cases that should be addressed first after deployment of the Next Generation – Secure Web Gateway (NGSWG).
Use case #
Category
Use case description
1
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Blocking Online Ads Silently
2
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Filtering Top Level Domains
3
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
HTTP Header Policies
4
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Filtering Traffic to high-risk countries
5
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Review Available metrics and confirm what reports to track
In this Topic
NGSWG Basic Policies

---
## SWG Web traffic
**URL:** https://docs.netskope.com/en/swg-web-traffic/
**Last Modified:** 2025-08-31T01:51:20+00:00
**Scraped:** 2026-06-25T08:57:41.828512+00:00

SWG Web traffic - Netskope Knowledge Portal
SWG Web traffic
Here are some basic policy use cases that should be addressed first after deployment of the Next Generation – Secure Web Gateway (NGSWG).
Use case #
Category
Use case description
1
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Blocking Online Ads Silently
2
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Filtering Top Level Domains
3
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
HTTP Header Policies
4
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Filtering Traffic to high-risk countries
5
NGSWG, Web policies, Observe Web traffic and Usage, Inline Monitoring and Protection for Web
Review Available metrics and confirm what reports to track
In this Topic
SWG Web traffic

---
## About Netskope Secure Web Gateway
**URL:** https://docs.netskope.com/en/about-netskope-secure-web-gateway/
**Last Modified:** 2025-09-01T13:20:08+00:00
**Scraped:** 2026-06-25T08:58:10.149050+00:00

About Netskope Secure Web Gateway
Netskope Secure Web Gateway enables you to govern web usage and provide a safe experience for your users with comprehensive web classification and content filtering.  By steering web traffic through Netskope, you can distill web activity into user sites, page visits, and other web activities in order to analyze usage and protect your enterprise.
Netskope Secure Web Gateway Features
Feature
Description
Web traffic steering
Use the Netskope Client to steer web traffic for remote and mobile users.
Use GRE or IPSec to steer web traffic for on-premises users.
Use Secure Forwarder to steer traffic for on-premises users.
Use the data plane on Netskope on-premises appliance to steer traffic for on-premises users.
Web classification and filtering
Covers 99.9% of active web traffic, with real-time updates of newly categorized URLs.
Acceptable Use Policy (AUP) focused classification covering productivity loss, bandwidth loss, and general loss.
Custom categories and flexible policies by user, group, or location.
Advanced data loss prevention (DLP)
Real-time protection against sensitive data loss.
1,000+ file types and 3,000+ data identifiers.
25+ compliance templates including GDPR, PCI, and HIPAA.
Advanced DLP features, such as fingerprinting, proximity analysis, exact match, and more.
Remote Browser Isolation
Integrated in Netskope’s admin console
Targeted RBI: Isolation of uncategorized and security risk web sites
Malware protection and data exfiltration prevention
In-flight rendering of isolated web pages into a safe pixel streaming. No active content reaches the endpoint hardware
No software or plug-ins required to be installed by users
Native mobile browsing experience for mobile devices
Risk-focused classification
Malicious site identification, including C&C, botnets, phishing, and spam sites.
Identify torrent repositories and evasive services, such as anonymizers and proxy services.
Identify newly registered and newly observed domains.
Advanced threat protection
Provides real-time, full file inspection to detect and block malware.
Zero-day protection using advanced heuristic analysis and dynamic sandbox analysis.
Backed by Netskope Threat Research Labs, a dedicated team researching cloud and web threats.
Detects threats quickly to provide shared collective protection.
Transport Layer Security (TLS) decryption
Decrypt and inspect TLS traffic at cloud-scale with no impact to end user experience.
Note
Netskope SWG doesn’t support web applications running on QUIC.
Graceful handling of retries for blocked files
Data trickling allows browser to use range headers to download partial files. This behavior is blocked entirely after the first block is sent from the proxy which prevents further partial downloads.
Use Cases
Netskope Secure Web Gateway applies the benefits of CASB to the entire web. By adding specific category classifications to a Real-time Protection policy, you can prohibit users from inappropriate sites, plus protect your organization from data loss and potential malware. Here are some examples of how to use Netskope Secure Web Gateway.
Prohibit users from sites that violate your Acceptable Use Policy (AUP). Custom categories can be created to find prohibited sites not already specified in one of our predefined categories. The URL Lookup feature can tell you whether or not a category contains a particular URL to help ensure full coverage.
Prohibit users from possibly inappropriate sites, but allow access if justification can be provided by the user, or a site exception is configured using a URL list in a custom category. Users are notified when they can justify access and when they are denied access due to a policy violation.
Protect your users and organization from data loss and malicious sites by adding DLP or Threat Protection profiles to a Real-time Protection policy. Remediate threats by blocking sites with multiple layers of threat detection including static and dynamic anti-virus inspection, user behavior anomaly detection, heuristic analysis, sandbox analysis, and more.
iOS Profile Use with Netskope Secure Web Gateway and Netskope Private Access
For Netskope Secure Web Gateway (and CASB), the iOS profile created uses an
on-demand
VPN on iOS devices. For Netskope Private Access installing the Client creates another
always on VPN
profile. You can only use one of these profiles at a time on an iOS device.
Both of the profiles are independent and can be created on the same device. Depending on the resource the you  want to access, you’ll need to go to iOS settings and switch between the iOS profiles.
Prerequisites
In order to use Netskope Secure Web Gateway, you must:
Purchase the Netskope Secure Web Gateway license and contact Support to have it enabled in your tenant.
Use version 66 or later when using the Netskope Client for traffic steering.
Workflow
Netskope Secure Web Gateway includes these primary steps:
Determine which traffic steering method you want to use: Netskope Client, Generic Routing Encapsulation (GRE) or IP Security (IPSec) tunneling, Secure Forwarder, or Data Plane On-Premises appliance.
Create custom categories to use in a Real-time Protection policy. Use the URL list feature to include or exclude specific URLs in a custom category.
Create a Real-time Protection policy that uses the custom categories and profiles you created to protect your web traffic activity.
Review the Skope IT Site and Page Events to get specifics about your web traffic, and then create web summary reports to compile web usage analytics.
In this Topic
About Netskope Secure Web Gateway

---
## Best Practices for Real-time Protection Policies
**URL:** https://docs.netskope.com/en/best-practices-for-real-time-protection-policies/
**Last Modified:** 2026-01-13T23:28:29+00:00
**Scraped:** 2026-06-25T08:59:31.321285+00:00

Best Practices for Real-time Protection Policies
The following sections walk you through the best practices of Real-time Protection and how to get the most out of your
Real-time Protection policies
.
Real-time Protection (Inline) vs API Data Protection (Out of Band) Policies
Policy Placement
Understanding the order of your Real-time Protection policies is important:
Real-time Protection policies are processed sequentially (top to bottom).
When traffic matches rule conditions, the action (Allow/Block) applies without further processing through the rule base. All policies are terminal except for DLP policies set as
Alert
and
Continue
.
You can drag and drop, or choose the policies to re-order.
Click
Apply Changes
to save the order.
Policy changes don’t take effect until you apply changes.
General Guidelines
Rules are processed from the top-down in the Real-time Protection policies list.
Place any rules applied to individuals or small groups near the top of the list.
Place exceptions at the top for block policies.
Use the
Filter
option to view specific policies.
Netskope allows the activity by default if it doesn’t match a policy.
Enable
dynamic URL classification
to further extend security coverage and policy enforcement to uncategorized URLs. When a URL isn’t found in the inline (NSProxy) database, this feature allows the system to initiate an asynchronous search of a second, larger database to find the correct category. This categorization is then shared across all instances within the same POP and remains valid for 12 hours, ensuring that all subsequent requests receive the categorization. After expiration, the category is automatically refreshed when the URL is accessed again.
Allow list business critical applications.
Block list predefined high risk categories and IOCs.
Leverage the Netskope REST API to maintain URL lists.
Structuring Real-time Protection Policies
Netskope recommends using Threat Protection policies to block high risk behaviors, such as downloading malware or uploading sensitive data to an unsanctioned application. Broader access control policies must be towards the bottom of the policy list.
Threat Protection (High risk)
Utility Policies
Remote Browser Isolation
(RBI)
CASB (Activity Oriented)
Web (Category Based)
Netskope Private Access
(NPA)
Best Practices for Utility Policies
In this Topic
Best Practices for Real-time Protection Policies

---
## Create a Real-time Protection Policy for Isolation (Targeted RBI)
**URL:** https://docs.netskope.com/en/create-a-real-time-protection-policy-for-isolation-targeted-rbi/
**Last Modified:** 2025-08-31T01:46:34+00:00
**Scraped:** 2026-06-25T09:00:58.280906+00:00

Create a Real-time Protection Policy for Isolation (Targeted RBI)
Policies are defined using a set of variables. These variables define the criteria for detecting policy violations.
For descriptions for each of the variables used, refer to Real-time Protection
Policy Variables
.
Note
When you see a text box during the policy workflow, click in the text box to view your additional options or to edit your selection(s). These options dynamically display based on your initial template choice. Many criteria are set to ‘Any’ by default. This means the policy engine will not match against the criteria.
When available, click
Add Criteria
to see what other match criteria are supported. Add more criteria to your policy to make it more specific.
Optionally, click the ‘X’ to the far right of the text box to remove criteria.
To create a Targeted RBI Policy you need to take into account the following constraints and configurations for web pages to be isolated properly.
On the Real-time Protection Policies page, click
New Policy
>
RBI
. Your menu options may differ based on the licenses available for your account.
When you select RBI, the system automatically picks ‘web access’ and populates recommended fields, such as Category with the recommended RBI categories.
Select the
Source
. Click in the text box to select users. Traffic Criteria is sorted as ‘Source’ and ‘Destination.’ The system will show the most appropriate criteria based on your policy template selection. Many criteria are set to ‘Any’ by default. This means the policy engine will not match against the criteria.
In addition, RBI policy creation / edition will enforce indicating the user’s browser as part of the RBI policy source criteria, to increase Customer’s RBI Policy efficacy and severely reduce non isolable requests sent to RBI. You must select mandatory browser fields in
isolate
type policies for example, RBI, Web Access, and Cloud App Access. If the Action is isolate, then the
browsers
field loads with supported browser names. This field cannot be left blank while saving the RTP policy.
NOTE
: This feature is currently in Beta. Contact your Sales Representative or Support to enable this feature.
Optionally, click
Add Criteria
to see what other match criteria are supported. Add more criteria to your policy to make it more specific.
For Destination,
Category
is automatically selected and it’s the only criteria that can be used for targeted RBI. You can choose to isolate any web page which falls in the following category list:
Newly Registered Domain
Newly Observed Domain
No Content
Parked Domains
Uncategorized
Web Proxies/Anonymizers
.
These categories are described in the
RBI Category Definitions
.
Tip
The system will notify you if you have added unrecommended categories to an isolation policy. Remove the unrecommended categories to avoid website performance degradation.
You can add more Destination criteria. The system will show the most appropriate criteria based on Application, Category, App Instance, or Private App selection.
Leave this blank for RBI policies
.
Select a
Profile and Action
. For RBI policies, select the “
Isolate
” action.
You can specify an RBI template. The default RBI template is applied but you can select a different template from the dropdown list.
Optionally, you can create a new template when the action is set to “Isolate” and attach it directly to the new Real-time Protection policy. Once created, it will be available in the list of RBI templates and admins can attach it to the RBI policy. To learn more:
RBI Templates
Do not add a DLP profile. They do not apply for targeted RBI.
Enter a name and a description.
Important
When creating policy names, only use alphanumeric characters and symbols such as “_” underscore, “-” dash, and “[ or ]” square brackets. You cannot use the greater than “>” and less than “<” symbols in policy names.
Select an Email Notification. Select the notification frequency. Choose None if you don’t want an email notification about the policy violation and the resulting action. When you choose ‘Every,’ you can select the frequency of the email notifications from the dropdown list – 30 Mins, 60 Mins, 6 Hours, 24 Hours. Or, choose to notify ‘After each event.’
Select the User, Admin, or Users to be notified. You can use the default email template or create a new template. Optionally, you can specify an email address that will appear as the sender in the email notification. When finished, click
Done
to save your email notification setting and exit the window.
Click
Save
in the upper right corner to save your new policy. You should see it in the Policy list page.
Tip
Navigate to
Policies
>
Real-time Protection
>
>
RBI Template
to filter policies that are using a specific RBI template. Optionally, you can select
Action
>
Isolate
to view policies that are using the RBI Isolate action. To learn more:
Isolation Events in Skope IT
Optionally, you can view pending changes for your RBI templates. Details such as field and controls that were edited, enabled, disabled, or cloned are described. Click
Policies
>
Templates
>
RBI
>
RBI Policy Variables
The following variables can be defined for an RBI Real-time Protection policy. You can use a variety of variables in a policy. If a variable is not used in the policy, it is defined as Any.
Variable
Description
Users
Users created manually in the UI or Active directory users that are automatically populated from the enterprise AD server.
User Groups
These are the Active Directory (AD) groups that are automatically populated to the Netskope cloud from the Enterprise AD server. Specifying user groups in a policy requires installing the Netskope AD adapter on a server that is part of your domain in order to export the AD user group names.
Organizational Unit
This information is obtained from the exported AD groups. Specifying organizational units in a policy requires installing the Netskope AD adapter on a server that is part of your domain in order to export the AD organizational unit names.
Cloud Apps + Web
Cloud app variables include:
Categories: Choose a type of app or web, like cloud storage. To learn more:
Category Definitions
.
Additional Attributes
These optional variables detect the following:
Access Method: The access type, like client, mobile, GRE, IPSec, and so on.
Browser: The browser type, like Chrome, Internet Explorer, and so on.
Device Classification: Managed or unmanaged devices based on the classifications created in Settings > Manage > Device Classification. This option is only applicable for access methods: Client, Mobile Profile, Revere Proxy.
Source Countries: The countries from which queries originate.
OS: Operating system types, like Mac, Linux, Windows, Android, iOS, and so on.
Source Network: The network address, range, or any network, including user IP address or egress IP address.
User Type: The user, to a user, or from a user.
Action
Action taken when a violation is detected:
Isolate: Forwards the request to the Netskope Remote Browser Isolation service for web isolation. Web browsing activity corresponding to the request is executed and rendered into a pixel stream in a remote browsing session in one isolated, ephemeral environment (a container) assigned for the individual user.
Tip
The user will exit isolation if they browse to a different domain. All browsing data is deleted after the isolation session ends. Netskope does not store any browsing data.
RBI template: They are attached to the RBI policy to apply granular controls to govern the user interaction in isolated web sites matching the policy. Netskope provides a predefined template for every tenant. To learn more:
RBI Templates
. Optionally, users can create a new template from the Real-time Protection policy workflow by clicking
.
In this Topic
Create a Real-time Protection Policy for Isolation (Targeted RBI)

---
## Create a Real-time Protection Policy for Private App Segments
**URL:** https://docs.netskope.com/en/create-a-real-time-protection-policy-for-private-apps/
**Last Modified:** 2026-06-01T19:49:14+00:00
**Scraped:** 2026-06-25T09:00:59.437069+00:00

Create a Real-time Protection Policy for Private App Segments - Netskope Knowledge Portal
Create a Real-time Protection Policy for Private App Segments
Private App Segments are not steered by default, which means by default private apps are never accessible to end-users, and they also will not receive a user notification about this. The end-user’s steering profile needs to be updated to include the private apps required for the User (Group/OU), and a matching real-time policy must exist if no discovery is configured for the user. Policies are required to log events and enable access to Users, Groups, or OUs.
Use Real-time Protection policies to:
Define access to a Private App Segment leveraging Source Policy criteria:
Access Method: Browser Access and/or Client
(Optional)
Specific User(s), User Group(s) or Organization Unit(s)
(Optional)
Source IP (Egress)
(Optional)
Operating System
(Optional)
Device Classification
(Optional)
Define access to a Private App Segment leveraging Destination Policy criteria:
Using an individual Private App Segment
Or leveraging Private App Segment Tags
And optionally with a browsing activity when applying a Data Loss Prevention or Threat Protection profile:
Download, Upload or FormPost
(Optional)
File Constraints: File Name or Extension, File Type or File Size
Define Profiles and Action:
Standard Actions for Client Based Policies
Allow
Block
Periodic Authentication
Profiles available for Client and Browser Access
DLP Profile
Profiles available for Client Access
Threat Protection Profile
For a specific private app, you may want to have one policy that grants access for a defined set of users, and then use a second policy that blocks and notifies users who don’t have access.
Configure Private App Access Policies
Go to
Policies > Real-time Protection
.
Click
New policy
and select
Private App Access
.
For Source you can configure the following options:
Specify the Users, OU, or Groups for which the Private App Access Policy is applied. (If not specified it’s applied to all Users.)
Specify whether the Access Method is
Browser Access
or
Client
(Threat Protection profiles are only available for Client Access)
Restrict access based on Source IP (Egress) which allows administrators to restrict access to Private App Segments based on the Egress IP of the end-users.
The Operating System for which the Private App Access Policy is applied to (Client only).
Which Custom Device Classification profile must be active for the user for the rule to apply (Client only; Browser Access will always be marked as a Unmanaged Device).
For Destination:
Select
Private App Segment
and add Private App Segments underneath.
Select the Activities that the destination rule is applied to (Only valid with Browser Access and applying a DLP Profile).
For Action, select
Allow
to grant access. To deny access, select
Block
, select a policy notification template from the dropdown list, or
create
one. To enforce
Periodic Authentication
ensure the Source OS criteria is set to Windows and/or MacOS and select a customer end-user notification template for the rule.
Give the policy a name, and then click
Save
.
In the Status section, confirm the policy is Enabled. Optionally, click
+ Policy Schedule
to restrict when this policy is active based on day, date, and time of day. For full configuration details, see
Time-Based Policies
.
Click
Apply Changes
.
Per-App Periodic Authentication for Private App Segment policies:
Periodic Authentication is currently not available on policies with a Threat Protection or Data Loss Prevention profile.
Policy Schedule caveats for Private App Segment policies:
Browser Access/Enterprise Browser:
Although a Policy Schedule can be configured on Browser Access and Enterprise Browser policies, enforcement is not yet supported for these access methods. Support is planned for a future release.
Local Brokers:
Policy Schedule will only be enforced when user traffic is egressing from a public IP address (non RFC-1918) to the Local Broker. Traffic originating from private/internal IP ranges will bypass the time-based enforcement.
Configure Per-App Periodic Authentication Policies
Periodic Per-App Authentication
introduces an additional layer of security by requiring users to periodically authenticate when accessing specific Private App Segments. This feature is available for desktop devices only (Windows and macOS).
Prerequisites
SAML Forward Proxy
must be configured and deployed to enable client enrollment and user identification.
Users must use the same identity (Email) as during client enrollment in order for authentication to succeed.
Source OS
criteria needs to be set to
Windows and/or MacOS
in order to select the new Periodic Authentication action.
Netskope Client
needs to be at version
R133
or higher.
Configure a Periodic Authentication Real-Time Policy
To enforce periodic authentication:
Go to
Policies > Real-Time Protection Policies
.
Click
New Policy > Private App Access
.
For
Source Criteria
, include
Operating System = Windows and/or macOS
.
Select
Client
for the
Access Method
.
Select the Private App Segment(s) for the
Destination
.
Select
Periodic Authentication
for the
Action
, and define the authentication interval (like every 30 minutes).
Select a
User Notification
template.
When finished, click
Save
.
After a user’s authentication expires, existing sessions remain valid. However, new sessions will require authentication after the interval expires.
Note:
Periodic Authentication
is only available on Windows and MacOS.
How the Authentication Timer Works
The system’s timer logic is simple yet powerful. It relies on a single timestamp that marks the user’s most recent successful authentication for
any
private application.
Think of it as a universal hall pass that gets a new timestamp every time you’re asked to re-authenticate. When you try to access an app, the system simply checks if the time elapsed since you got your last timestamp is greater than the specific authentication interval required for
that app
.
Use Case Example
Periodic Per-App Authentication
works very different from the NPA periodic re-authentication mechanism that existed already. Periodic Reauthentication brings the entire NPA tunnel down
after
a set timer if authentication does not happen; per-app authentication works
before
a user accesses an application and does not interact with the NPA tunnel.
Here’s a real-world scenario to show how this works in practice.
Imagine we have two policies configured for a user, Alice:
App A (GitLab):
Requires authentication every 90 minutes.
App B (Jira):
Requires authentication every 60 minutes.
Here is a timeline of Alice’s activity:
9:00 AM:
Alice accesses GitLab (App A) for the first time.
Action:
She is prompted to authenticate. Upon success, access is granted.
Result:
The system’s Last Authentication Time for Alice is now set to 9:00 AM. ⏰
9:50 AM:
Alice opens Jira (App B).
Check:
The system calculates the time since her last authentication:
9:50 AM - 9:00 AM = 50 minutes
.
Action:
Since 50 minutes is less than Jira’s 60-minute interval, no new authentication is needed. Access is granted seamlessly.
Result:
The Last Authentication Time remains 9:00 AM.
10:10 AM:
Alice tries to access Jira (App B) again.
Check:
The system calculates the time elapsed:
10:10 AM - 9:00 AM = 70 minutes
.
Action:
Since 70 minutes is greater than Jira’s 60-minute interval, Alice is prompted to re-authenticate.
Result:
Upon success, the Last Authentication Time is updated to 10:10 AM. 🔄
10:30 AM:
Alice navigates back to GitLab (App A).
Check:
The system uses the
newest
timestamp:
10:30 AM - 10:10 AM = 20 minutes
.
Action:
Since 20 minutes is less than GitLab’s 90-minute interval, no authentication is required.
Result:
The Last Authentication Time remains 10:10 AM.
This single, rolling timestamp ensures that authentication happens based on the policy of the app being accessed, relative to the user’s last system-wide authentication event.
Configure Threat Protection Policies
Netskope Private Access (NPA) allows organizations to apply Threat Protection to web traffic (ports 80 and 443) for private apps, ensuring files are scanned for malware in real-time. When using Threat Protection with NPA, note that this feature:
Requires
Client
as the Access Method.
Scans all web traffic on HTTP (80) and HTTPS (443).
Applies real-time scanning to protect private app access from malware and other advanced threats.
Netskope Private Access now also supports Client to Server IPS protections based on HTTP (80) and HTTPS (443). More information can be found here:
About IPS Settings
.
Create a File Hash List
Define hash values (MD5/SHA-256) for files to be detected.
Use these lists to
allowlist
(safe) or
blocklist
(malicious) known file hashes.
Configure Threat Protection for Real-Time Private App Access Policies
Go to
Policies
>
Real-time Protection
.
Click
New Policy
and then
Private App Access
.
On the Real-time Protection policy page, enter the settings for
Source
(Users, Access Method and other Source Criteria) and
Destination
(Private App/Private App Tag) first.
In the
Profile & Action
section, select
Add Profile
and choose
Threat Protection Profile
. Netskope recommends selecting
Default Malware Scan (predefined)
, because it automatically scans across all Threat Protection engines your platform is licensed for.
Select the
Action
for each severity level. The recommended action for every severity level is
Block
. This ensures the best protection for users. To apply a remediation profile for each severity level, select a remediation profile from the dropdown list.
Optionally, if you selected
File Type
constraints, and choose a
Block
action for a severity level, you can see the
Block till benign verdict by dynamic threat analysis
option. Select to block users from uploading or downloading a file until Netskope dynamic threat analysis provides a benign verdict. The analysis can take up to 10 minutes. For more details, go to
Creating a Threat Protection Policy for Patient Zero
.
Enter a name for the policy and click
Save
.
When the
Fallback Action
for Advanced File Scanning is set to
Alert
or
Block
, some events might not have policy name if there’s a TSS or DLP fail reason. There’s no rule hit because you excluded the Threat Protection rule. You don’t have a catch-all rule at the end of the policy.
Configure Data Loss Prevention Policies
Netskope Private Access supports applying Data Loss Prevention (DLP) to private apps by using Private App Access real-time policies. Use this configuration to inspect and protect sensitive data for both
Browser Access
and
Client
access to private apps. For Browser Access, you can also scope the policy to specific browser activities. For information about creating DLP profiles, rules, and identifiers, see
Data Loss Prevention
.
Prerequisites
Ensure a Publisher is already configured.
For Browser Access, confirm a SAML reverse proxy IdP for Private Apps is configured.
For Browser Access, verify the private app is configured for Browser Access.
Create the DLP profile you want to apply before creating the policy.
Configure a DLP policy for Private Apps
Go to
Policies > Real-time Protection
and create or edit a
Private App Access
policy. The broader real-time policy framework supports DLP and Threat Protection and includes
Private App Segment Access
as a policy type.
For
Source
, select the users or groups to which the policy applies, and set the
Access Method
to
Browser Access
,
Client
, or both, depending on the use case.
For
Destination
, select the Private App Segment(s). Ensure the specific Activities are configured in order to be able to define a Data Loss Prevention Profile.
For
Profile & Action
, select
Add Profile
and choose the required DLP Profile(s).
Choose the enforcement action, name the policy, and click
Save
.
Additional Notes
For
NPA Browser Access DLP
, only
HTTP and HTTPS
private apps are supported.
AnyApp Browser Access
apps such as
RDP/SSH
are not supported for DLP.
For
NPA Client Access DLP
, only
HTTP and HTTPS
over
port 80 and 443
are supported.
Transaction events are not generated
for
DLP
traffic, even when transaction events are enabled for web traffic.
Review the
Supported File Types for Content Inspection
for file-format coverage.
OCR
is an
Advanced DLP
capability in Netskope generally, but
OCR
is
not supported
for NPA.
Validation
After saving the policy, test access to the private app with representative content that should trigger the selected DLP profile. Confirm the expected enforcement result and review the resulting DLP alerts or incidents.
Related links
Enforce DLP for NPA Browser Access Private Apps
for Browser Access-specific prerequisites and legacy context.
Data Loss Prevention
/
About DLP
for profiles, rules, identifiers, and incidents.
Supported File Types for Content Inspection
for file-format coverage.
User Notification Configuration
This feature uses a new User Notification type to alert users when authentication is required. Follow these steps:
Go to
Policies > User Notification (Template Section)
Click
Add Template > Private App Segments
Customize the notification with the following in mind:
Set the
Action
to
Periodic Authentication
Provide clear context in the message, like the example shown below, or something more specific, like
Authentication is required to continue using [App Name]. Please reload after completing authentication.
)
When finished, click
Save
.
In this Topic
Create a Real-time Protection Policy for Private App Segments

---
## Create a Real-time Protection Policy for Web Categories
**URL:** https://docs.netskope.com/en/create-a-real-time-protection-policy-for-web-categories/
**Last Modified:** 2025-08-31T01:47:18+00:00
**Scraped:** 2026-06-25T09:01:01.711753+00:00

Create a Real-time Protection Policy for Web Categories - Netskope Knowledge Portal
Create a Real-time Protection Policy for Web Categories
When you have visibility into the web traffic and the activities performed by users, the next step is to define policies to enforce your business rules. Policies allow you to enforce an action (like block) based on web categories, users and groups, app activity, and so on. In addition to this, you can also define data loss prevention (DLP) and threat protection profiles to inspect traffic to prevent sensitive and critical data leaks and exposure. For a more detailed view of each policy, click the expand icon adjacent to the name of the policy.
You can move policies by dragging the icon beside the policy name. For more options, like cloning a policy, click the three dots to the far right of this policy to open a menu that enables you to clone, revert, disable, move, and delete policies.
Important
Policies are applied in the order they appear on this page. After you create Real-time Protection policies for web categories, move your Netskope Secure Web Gateway policies to the bottom of the page so they don’t interfere with your SaaS traffic Real-time Protection policies.
The Real-time Protection Policies page also allows you to use search filters to find policies for specific users and apps. To use the search filters, click the filter icon to apply one or more filters. You can also search for information by clicking the plus sign to use the predefined filters.
Create an Real-time Protection Policy
Policies are defined using a set of variables. These variables define the criteria for detecting policy violations. When all criteria are matched the specified action is taken.
To create an Real-time Protection policy for Netskope Secure Web Gateway:
Go to
Policies > Real-time Protection
.
Click
New policy
and select
Web Access
.
For Source, select the Users, OU, Groups, or Unknown (all unauthenticated users) for which you want to grant access to the private app(s). Add criteria if desired.
For Destination, leave
Category
and select a category from the dropdown list. Select any activities or constraints you want to apply in the policy.
For Action, select
Alert
to monitor web traffic. To deny access, select
Block
.
Give the policy a name (like
Alert for questionable sites
), and then choose the
notification template
to use in the policy. When finished, click
Save
.
Click
Apply Changes
.
To modify this policy, click on it and select the pencil icon next to the headings (like Action). After saving your changes, click
Apply Changes.
In this Topic
Create a Real-time Protection Policy for Web Categories

---
## Creating a Threat Protection Policy for Real-time Protection
**URL:** https://docs.netskope.com/en/creating-a-threat-protection-policy-for-real-time-protection/
**Last Modified:** 2025-09-03T18:23:19+00:00
**Scraped:** 2026-06-25T09:01:32.856031+00:00

Creating a Threat Protection Policy for Real-time Protection
Netskope can scan files stored in your cloud storage applications for malware. Real-time Protection policies scan files for malware by default. For added protection, optional configurations include allowlist and blocklist file hash lists for malware detection, and integrating Carbon Black for endpoint protection to use remediation profiles while creating an Real-time Protection policy.
To use the optional configurations in a Real-time Protection policy, configure these options before creating the Real-time Protection policy:
Create a file hash list: Specify the type of hash lists to detect in a malware scan.
Create a detection profile: Specify which hash list file types to allowlist and blocklist.
Integrate endpoint detection and remediation: Set up a 3rd-party integration, like with Carbon Black or CrowdStrike, for endpoint protection.
Create a remediation profile: Specify the action to take, like Isolate, Alert, or Add to Watchlist/Blocklist.
To configure threat protection for Real-time Protection policies:
Go to
Policies
>
Real-time Protection
.
Click
New Policy
and then
Threat Protection
.
On the Real-time Protection policy page, enter the settings for
Source
(Users) and
Destination
(Cloud App/Category) first. Netskope recommends selecting all users and categories with the
Activity
set to
Upload
and
Download
.
Note
Netskope automatically scans browse activity and includes it in the download activity for elements/files from a webpage.
In the
Profile & Action
section, select a Threat Protection profile. Netskope recommends selecting
Default Malware Scan (predefined)
because it automatically scan across all Threat Protection engines based on your organization’s
license
.
Select the
Action
for each severity level. The recommended action for every severity level is
Block
. This ensures the best protection for users. To apply a remediation profile for each severity level, select a remediation profile from the dropdown list.
Note
When the
Fallback Action
for
Advanced File Scanning
is set to
Alert
or
Block
, some events might not have policy name if:
There’s a TSS or DLP fail reason.
There’s no rule hit because you excluded the Threat Protection or DLP rule.
You don’t have a catch-all rule at the end of the policy.
Optionally, if you selected
File Type
constraints and chose a
Block
action for a severity level, you can see the
Block till benign verdict by dynamic threat analysis
option. Select to block users from uploading or downloading a file until Netskope dynamic threat analysis provides a benign verdict. The analysis can take up to 10 minutes. See
Creating a Threat Protection Policy for Patient Zero
.
Enter a name for the policy and click
Save
.
Now you are ready to use the malware and malicious sites pages.
In this Topic
Creating a Threat Protection Policy for Real-time Protection

---
## Real-time Protection for Public Cloud
**URL:** https://docs.netskope.com/en/real-time-protection-for-public-cloud/
**Last Modified:** 2025-08-31T01:50:20+00:00
**Scraped:** 2026-06-25T09:06:03.557114+00:00

Real-time Protection for Public Cloud - Netskope Knowledge Portal
Real-time Protection for Public Cloud
Real-time protection policies allow you to enforce access control on your public cloud assets. Using real-time protection policy, you can inspect traffic to prevent sensitive and critical data leaks and exposure. If you’ve subscribed to Netskope’s Storage Scan features DLP Scan and Threat Protection (Malware Scan), you can use real-time protection policies to define data loss prevention and threat protection profiles.
When you create real-time policies, you can define the action to be performed on content that does not match a profile. For detailed information on Real-time protection policies, see
Real-time Protection Policies
.
Real-time Protection for IaaS
Supported AWS Entities for Real-time Protection
Supported GCP Entities for Real-time Protection
In this Topic
Real-time Protection for Public Cloud

---
## Supported AWS Entities for Real-time Protection
**URL:** https://docs.netskope.com/en/supported-aws-entities-for-real-time-protection/
**Last Modified:** 2025-08-31T01:50:21+00:00
**Scraped:** 2026-06-25T09:07:44.748263+00:00

Supported AWS Entities for Real-time Protection
Netskope for IaaS Real-time Protection provides robust real-time activity monitoring and enforcement for AWS Services across API and Browser/Console traffic. The following table provides the list of AWS services that are supported for Real-time Protection.
AWS App Name
Action Name
Connector Activity Name
Browser and API Traffic
Amazon API Gateway
UpdateStage
Edit
Yes
Amazon API Gateway
GetStage
View
Yes
Amazon API Gateway
DeleteStage
Delete
Yes
Amazon API Gateway
GenerateClientCertificate
Create
Yes
Amazon API Gateway
GetClientCertificates
View
Yes
Amazon API Gateway
GetGatewayResponses
View
Yes
Amazon API Gateway
CreateUsagePlan
Create
Yes
Amazon API Gateway
GetUsagePlans
View
Yes
Amazon API Gateway
CreateApiKey
Create
Yes
Amazon API Gateway
GetApiKeys
View
Yes
Amazon API Gateway
PutIntegrationResponse
Edit
Yes
Amazon API Gateway
UpdateIntegrationResponse
Edit
Yes
Amazon API Gateway
GetIntegrationResponse
View
Yes
Amazon API Gateway
DeleteIntegrationResponse
Delete
Yes
Amazon API Gateway
UpdateUsage
Edit
Yes
Amazon API Gateway
UpdateApiKey
Edit
Yes
Amazon API Gateway
GetApiKey
View
Yes
Amazon API Gateway
DeleteApiKey
Delete
Yes
Amazon API Gateway
FlushStageCache
Delete
Yes
Amazon API Gateway
UpdateClientCertificate
Edit
Yes
Amazon API Gateway
GetClientCertificate
View
Yes
Amazon API Gateway
DeleteClientCertificate
Delete
Yes
Amazon API Gateway
UpdateResource
Edit
Yes
Amazon API Gateway
GetResource
View
Yes
Amazon API Gateway
DeleteResource
Delete
Yes
Amazon API Gateway
ImportDocumentationParts
Create
Yes
Amazon API Gateway
CreateDocumentationPart
Create
Yes
Amazon API Gateway
GetDocumentationParts
View
Yes
Amazon API Gateway
UpdateDeployment
Edit
Yes
Amazon API Gateway
GetDeployment
View
Yes
Amazon API Gateway
DeleteDeployment
Delete
Yes
Amazon API Gateway
CreateStage
Create
Yes
Amazon API Gateway
GetStages
View
Yes
Amazon API Gateway
UpdateDocumentationPart
Edit
Yes
Amazon API Gateway
GetDocumentationPart
View
Yes
Amazon API Gateway
DeleteDocumentationPart
Delete
Yes
Amazon API Gateway
UpdateAuthorizer
Edit
Yes
Amazon API Gateway
TestInvokeAuthorizer
Create
Yes
Amazon API Gateway
GetAuthorizer
View
Yes
Amazon API Gateway
DeleteAuthorizer
Delete
Yes
Amazon API Gateway
CreateAuthorizer
Create
Yes
Amazon API Gateway
GetAuthorizers
View
Yes
Amazon API Gateway
UpdateDocumentationVersion
Edit
Yes
Amazon API Gateway
GetDocumentationVersion
View
Yes
Amazon API Gateway
DeleteDocumentationVersion
Delete
Yes
Amazon API Gateway
GetSdkTypes
View
Yes
Amazon API Gateway
UpdateModel
Edit
Yes
Amazon API Gateway
GetModel
View
Yes
Amazon API Gateway
DeleteModel
Delete
Yes
Amazon API Gateway
CreateVpcLink
Create
Yes
Amazon API Gateway
GetVpcLinks
View
Yes
Amazon API Gateway
CreateRestApi
Create
Yes
Amazon API Gateway
GetRestApis
View
Yes
Amazon API Gateway
UpdateRequestValidator
Edit
Yes
Amazon API Gateway
GetRequestValidator
View
Yes
Amazon API Gateway
DeleteRequestValidator
Delete
Yes
Amazon API Gateway
ImportApiKeys
Create
Yes
Amazon API Gateway
GetMethod
View
Yes
Amazon API Gateway
UpdateMethod
Edit
Yes
Amazon API Gateway
PutMethod
Edit
Yes
Amazon API Gateway
TestInvokeMethod
Create
Yes
Amazon API Gateway
DeleteMethod
Delete
Yes
Amazon API Gateway
CreateUsagePlanKey
Create
Yes
Amazon API Gateway
GetUsagePlanKeys
View
Yes
Amazon API Gateway
UpdateVpcLink
Edit
Yes
Amazon API Gateway
GetVpcLink
View
Yes
Amazon API Gateway
DeleteVpcLink
Delete
Yes
Amazon API Gateway
GetUsagePlanKey
View
Yes
Amazon API Gateway
DeleteUsagePlanKey
Delete
Yes
Amazon API Gateway
CreateDocumentationVersion
Create
Yes
Amazon API Gateway
GetDocumentationVersions
View
Yes
Amazon API Gateway
GetModelTemplate
View
Yes
Amazon API Gateway
CreateRequestValidator
Create
Yes
Amazon API Gateway
GetRequestValidators
View
Yes
Amazon API Gateway
UpdateBasePathMapping
Edit
Yes
Amazon API Gateway
GetBasePathMapping
View
Yes
Amazon API Gateway
DeleteBasePathMapping
Delete
Yes
Amazon API Gateway
GetExport
View
Yes
Amazon API Gateway
PutRestApi
Edit
Yes
Amazon API Gateway
UpdateRestApi
Edit
Yes
Amazon API Gateway
GetRestApi
View
Yes
Amazon API Gateway
DeleteRestApi
Delete
Yes
Amazon API Gateway
PutMethodResponse
Edit
Yes
Amazon API Gateway
UpdateMethodResponse
Edit
Yes
Amazon API Gateway
GetMethodResponse
View
Yes
Amazon API Gateway
DeleteMethodResponse
Delete
Yes
Amazon API Gateway
UpdateUsagePlan
Edit
Yes
Amazon API Gateway
GetUsagePlan
View
Yes
Amazon API Gateway
DeleteUsagePlan
Delete
Yes
Amazon API Gateway
GetUsage
View
Yes
Amazon API Gateway
UpdateAccount
Edit
Yes
Amazon API Gateway
GetAccount
View
Yes
Amazon API Gateway
UntagResource
Delete
Yes
Amazon API Gateway
GetResources
View
Yes
Amazon API Gateway
CreateResource
Create
Yes
Amazon API Gateway
TagResource
Create
Yes
Amazon API Gateway
GetTags
View
Yes
Amazon API Gateway
FlushStageAuthorizersCache
Delete
Yes
Amazon API Gateway
ImportRestApi
Create
Yes
Amazon API Gateway
CreateDomainName
Create
Yes
Amazon API Gateway
GetDomainNames
View
Yes
Amazon API Gateway
UpdateDomainName
Edit
Yes
Amazon API Gateway
GetDomainName
View
Yes
Amazon API Gateway
DeleteDomainName
Delete
Yes
Amazon API Gateway
CreateDeployment
Create
Yes
Amazon API Gateway
GetDeployments
View
Yes
Amazon API Gateway
GetSdkType
View
Yes
Amazon API Gateway
PutGatewayResponse
Edit
Yes
Amazon API Gateway
UpdateGatewayResponse
Edit
Yes
Amazon API Gateway
GetGatewayResponse
View
Yes
Amazon API Gateway
DeleteGatewayResponse
Delete
Yes
Amazon API Gateway
PutIntegration
Edit
Yes
Amazon API Gateway
UpdateIntegration
Edit
Yes
Amazon API Gateway
GetIntegration
View
Yes
Amazon API Gateway
DeleteIntegration
Delete
Yes
Amazon API Gateway
CreateModel
Create
Yes
Amazon API Gateway
GetModels
View
Yes
Amazon API Gateway
GetSdk
View
Yes
Amazon API Gateway
CreateBasePathMapping
Create
Yes
Amazon API Gateway
GetBasePathMappings
View
Yes
Amazon API Gateway Management API
PostToConnection
Create
Yes
Amazon API Gateway Management API
GetConnection
View
Yes
Amazon API Gateway Management API
DeleteConnection
Delete
Yes
Amazon API Gateway V2
UpdateVpcLink
Edit
Yes
Amazon API Gateway V2
GetVpcLink
View
Yes
Amazon API Gateway V2
DeleteVpcLink
Delete
Yes
Amazon API Gateway V2
DeleteCorsConfiguration
Delete
Yes
Amazon API Gateway V2
CreateApiMapping
Create
Yes
Amazon API Gateway V2
GetApiMappings
View
Yes
Amazon API Gateway V2
CreateVpcLink
Create
Yes
Amazon API Gateway V2
GetVpcLinks
View
Yes
Amazon API Gateway V2
CreateIntegrationResponse
Create
Yes
Amazon API Gateway V2
GetIntegrationResponses
View
Yes
Amazon API Gateway V2
DeleteRouteSettings
Delete
Yes
Amazon API Gateway V2
UpdateIntegration
Edit
Yes
Amazon API Gateway V2
GetIntegration
View
Yes
Amazon API Gateway V2
DeleteIntegration
Delete
Yes
Amazon API Gateway V2
CreateRouteResponse
Create
Yes
Amazon API Gateway V2
GetRouteResponses
View
Yes
Amazon API Gateway V2
CreateIntegration
Create
Yes
Amazon API Gateway V2
GetIntegrations
View
Yes
Amazon API Gateway V2
CreateDeployment
Create
Yes
Amazon API Gateway V2
GetDeployments
View
Yes
Amazon API Gateway V2
CreateRoute
Create
Yes
Amazon API Gateway V2
GetRoutes
View
Yes
Amazon API Gateway V2
UntagResource
Delete
Yes
Amazon API Gateway V2
UpdateDomainName
Edit
Yes
Amazon API Gateway V2
GetDomainName
View
Yes
Amazon API Gateway V2
DeleteDomainName
Delete
Yes
Amazon API Gateway V2
UpdateAuthorizer
Edit
Yes
Amazon API Gateway V2
GetAuthorizer
View
Yes
Amazon API Gateway V2
DeleteAuthorizer
Delete
Yes
Amazon API Gateway V2
ExportApi
View
Yes
Amazon API Gateway V2
DeleteAccessLogSettings
Delete
Yes
Amazon API Gateway V2
UpdateModel
Edit
Yes
Amazon API Gateway V2
GetModel
View
Yes
Amazon API Gateway V2
DeleteModel
Delete
Yes
Amazon API Gateway V2
GetModelTemplate
View
Yes
Amazon API Gateway V2
UpdateRouteResponse
Edit
Yes
Amazon API Gateway V2
GetRouteResponse
View
Yes
Amazon API Gateway V2
DeleteRouteResponse
Delete
Yes
Amazon API Gateway V2
UpdateStage
Edit
Yes
Amazon API Gateway V2
GetStage
View
Yes
Amazon API Gateway V2
DeleteStage
Delete
Yes
Amazon API Gateway V2
UpdateApiMapping
Edit
Yes
Amazon API Gateway V2
GetApiMapping
View
Yes
Amazon API Gateway V2
DeleteApiMapping
Delete
Yes
Amazon API Gateway V2
CreateModel
Create
Yes
Amazon API Gateway V2
GetModels
View
Yes
Amazon API Gateway V2
ResetAuthorizersCache
Delete
Yes
Amazon API Gateway V2
UpdateDeployment
Edit
Yes
Amazon API Gateway V2
GetDeployment
View
Yes
Amazon API Gateway V2
DeleteDeployment
Delete
Yes
Amazon API Gateway V2
UpdateRoute
Edit
Yes
Amazon API Gateway V2
GetRoute
View
Yes
Amazon API Gateway V2
DeleteRoute
Delete
Yes
Amazon API Gateway V2
CreateDomainName
Create
Yes
Amazon API Gateway V2
GetDomainNames
View
Yes
Amazon API Gateway V2
DeleteRouteRequestParameter
Delete
Yes
Amazon API Gateway V2
ImportApi
Create
Yes
Amazon API Gateway V2
CreateApi
Create
Yes
Amazon API Gateway V2
GetApis
View
Yes
Amazon API Gateway V2
CreateStage
Create
Yes
Amazon API Gateway V2
GetStages
View
Yes
Amazon API Gateway V2
UpdateIntegrationResponse
Edit
Yes
Amazon API Gateway V2
GetIntegrationResponse
View
Yes
Amazon API Gateway V2
DeleteIntegrationResponse
Delete
Yes
Amazon API Gateway V2
CreateAuthorizer
Create
Yes
Amazon API Gateway V2
GetAuthorizers
View
Yes
Amazon API Gateway V2
ReimportApi
Edit
Yes
Amazon API Gateway V2
UpdateApi
Edit
Yes
Amazon API Gateway V2
GetApi
View
Yes
Amazon API Gateway V2
DeleteApi
Delete
Yes
Amazon API Gateway V2
TagResource
Create
Yes
Amazon API Gateway V2
GetTags
View
Yes
Amazon Auto Scaling
PutScheduledUpdateGroupAction
Edit
Yes
Amazon Auto Scaling
DisableMetricsCollection
Delete
Yes
Amazon Auto Scaling
SetDesiredCapacity
Create
Yes
Amazon Auto Scaling
DetachLoadBalancers
Delete
Yes
Amazon Auto Scaling
CancelInstanceRefresh
Delete
Yes
Amazon Auto Scaling
SetInstanceHealth
Create
Yes
Amazon Auto Scaling
SuspendProcesses
Delete
Yes
Amazon Auto Scaling
DescribeTags
View
Yes
Amazon Auto Scaling
AttachInstances
Attach
Yes
Amazon Auto Scaling
RecordLifecycleActionHeartbeat
Create
Yes
Amazon Auto Scaling
DescribeAccountLimits
View
Yes
Amazon Auto Scaling
DescribeAdjustmentTypes
View
Yes
Amazon Auto Scaling
EnableMetricsCollection
Enable
Yes
Amazon Auto Scaling
DescribeScalingProcessTypes
View
Yes
Amazon Auto Scaling
DeleteScheduledAction
Delete
Yes
Amazon Auto Scaling
TerminateInstanceInAutoScalingGroup
Terminate
Yes
Amazon Auto Scaling
PutLifecycleHook
Edit
Yes
Amazon Auto Scaling
CreateAutoScalingGroup
Create
Yes
Amazon Auto Scaling
SetInstanceProtection
Create
Yes
Amazon Auto Scaling
PutScalingPolicy
Edit
Yes
Amazon Auto Scaling
ExitStandby
Create
Yes
Amazon Auto Scaling
DescribeInstanceRefreshes
View
Yes
Amazon Auto Scaling
DescribeAutoScalingNotificationTypes
View
Yes
Amazon Auto Scaling
PutWarmPool
Edit
Yes
Amazon Auto Scaling
DescribeLoadBalancerTargetGroups
View
Yes
Amazon Auto Scaling
AttachLoadBalancers
Attach
Yes
Amazon Auto Scaling
CreateOrUpdateTags
Create
Yes
Amazon Auto Scaling
DeletePolicy
Delete
Yes
Amazon Auto Scaling
EnterStandby
Create
Yes
Amazon Auto Scaling
DeleteWarmPool
Delete
Yes
Amazon Auto Scaling
DescribeMetricCollectionTypes
View
Yes
Amazon Auto Scaling
DescribeAutoScalingGroups
View
Yes
Amazon Auto Scaling
DeleteAutoScalingGroup
Delete
Yes
Amazon Auto Scaling
DescribeLifecycleHooks
View
Yes
Amazon Auto Scaling
DetachInstances
Delete
Yes
Amazon Auto Scaling
DescribeWarmPool
View
Yes
Amazon Auto Scaling
DeleteTags
Delete
Yes
Amazon Auto Scaling
DescribeLifecycleHookTypes
View
Yes
Amazon Auto Scaling
DeleteLaunchConfiguration
Delete
Yes
Amazon Auto Scaling
DescribeLaunchConfigurations
View
Yes
Amazon Auto Scaling
DeleteNotificationConfiguration
Delete
Yes
Amazon Auto Scaling
PutNotificationConfiguration
Edit
Yes
Amazon Auto Scaling
DescribeNotificationConfigurations
View
Yes
Amazon Auto Scaling
DeleteLifecycleHook
Delete
Yes
Amazon Auto Scaling
DescribeScheduledActions
View
Yes
Amazon Auto Scaling
DescribeScalingActivities
View
Yes
Amazon Auto Scaling
DescribeTerminationPolicyTypes
View
Yes
Amazon Auto Scaling
DescribeAutoScalingInstances
View
Yes
Amazon Auto Scaling
UpdateAutoScalingGroup
Edit
Yes
Amazon Auto Scaling
CompleteLifecycleAction
Create
Yes
Amazon Auto Scaling
DescribeLoadBalancers
View
Yes
Amazon Auto Scaling
DescribePolicies
View
Yes
Amazon Auto Scaling
DetachLoadBalancerTargetGroups
Delete
Yes
Amazon Auto Scaling
ResumeProcesses
Create
Yes
Amazon Auto Scaling
CreateLaunchConfiguration
Create
Yes
Amazon Auto Scaling
ExecutePolicy
Create
Yes
Amazon Auto Scaling
StartInstanceRefresh
Start
Yes
Amazon Auto Scaling
AttachLoadBalancerTargetGroups
Attach
Yes
Amazon Certificate Manager
ListCertificates
View
Yes
Amazon Certificate Manager
PutAccountConfiguration
Edit
Yes
Amazon Certificate Manager
ExportCertificate
View
Yes
Amazon Certificate Manager
AddTagsToCertificate
Create
Yes
Amazon Certificate Manager
ResendValidationEmail
Create
Yes
Amazon Certificate Manager
RenewCertificate
Create
Yes
Amazon Certificate Manager
DescribeCertificate
View
Yes
Amazon Certificate Manager
ListTagsForCertificate
View
Yes
Amazon Certificate Manager
ImportCertificate
Create
Yes
Amazon Certificate Manager
RequestCertificate
Create
Yes
Amazon Certificate Manager
DeleteCertificate
Delete
Yes
Amazon Certificate Manager
UpdateCertificateOptions
Edit
Yes
Amazon Certificate Manager
GetCertificate
View
Yes
Amazon Certificate Manager
GetAccountConfiguration
View
Yes
Amazon Certificate Manager
RemoveTagsFromCertificate
Delete
Yes
Amazon CloudFormation
ExecuteChangeSet
Create
Yes
Amazon CloudFormation
DetectStackResourceDrift
Create
Yes
Amazon CloudFormation
DescribeStackResourceDrifts
View
Yes
Amazon CloudFormation
DetectStackDrift
Create
Yes
Amazon CloudFormation
DeleteStack
Delete
Yes
Amazon CloudFormation
UpdateStack
Edit
Yes
Amazon CloudFormation
DescribeTypeRegistration
View
Yes
Amazon CloudFormation
ValidateTemplate
Create
Yes
Amazon CloudFormation
ListStackSets
View
Yes
Amazon CloudFormation
SetStackPolicy
Create
Yes
Amazon CloudFormation
DescribeStackSetOperation
View
Yes
Amazon CloudFormation
GetStackPolicy
View
Yes
Amazon CloudFormation
DescribeAccountLimits
View
Yes
Amazon CloudFormation
RegisterType
Register
Yes
Amazon CloudFormation
DeleteChangeSet
Delete
Yes
Amazon CloudFormation
DescribeStackResources
View
Yes
Amazon CloudFormation
UpdateStackInstances
Edit
Yes
Amazon CloudFormation
StopStackSetOperation
Stop
Yes
Amazon CloudFormation
ListStackResources
View
Yes
Amazon CloudFormation
GetTemplate
View
Yes
Amazon CloudFormation
SignalResource
Create
Yes
Amazon CloudFormation
EstimateTemplateCost
Create
Yes
Amazon CloudFormation
ListStackSetOperations
View
Yes
Amazon CloudFormation
ListTypeVersions
View
Yes
Amazon CloudFormation
DescribeStackEvents
View
Yes
Amazon CloudFormation
ListStacks
View
Yes
Amazon CloudFormation
RecordHandlerProgress
Create
Yes
Amazon CloudFormation
ListTypes
View
Yes
Amazon CloudFormation
DescribeChangeSet
View
Yes
Amazon CloudFormation
ListImports
View
Yes
Amazon CloudFormation
CreateStackSet
Create
Yes
Amazon CloudFormation
DeleteStackSet
Delete
Yes
Amazon CloudFormation
UpdateStackSet
Edit
Yes
Amazon CloudFormation
DescribeStacks
View
Yes
Amazon CloudFormation
CreateChangeSet
Create
Yes
Amazon CloudFormation
CreateStackInstances
Create
Yes
Amazon CloudFormation
CancelUpdateStack
Delete
Yes
Amazon CloudFormation
DescribeStackDriftDetectionStatus
View
Yes
Amazon CloudFormation
UpdateTerminationProtection
Edit
Yes
Amazon CloudFormation
SetTypeDefaultVersion
Create
Yes
Amazon CloudFormation
DescribeStackResource
View
Yes
Amazon CloudFormation
ListStackSetOperationResults
View
Yes
Amazon CloudFormation
ListChangeSets
View
Yes
Amazon CloudFormation
ContinueUpdateRollback
Create
Yes
Amazon CloudFormation
ListTypeRegistrations
View
Yes
Amazon CloudFormation
DeregisterType
Deregister
Yes
Amazon CloudFormation
CreateStack
Create
Yes
Amazon CloudFormation
ListExports
View
Yes
Amazon CloudFormation
ListStackInstances
View
Yes
Amazon CloudFormation
GetTemplateSummary
View
Yes
Amazon CloudFormation
DescribeType
View
Yes
Amazon CloudFormation
DetectStackSetDrift
Create
Yes
Amazon CloudFormation
DescribeStackInstance
View
Yes
Amazon CloudFormation
DeleteStackInstances
Delete
Yes
Amazon CloudFormation
DescribeStackSet
View
Yes
Amazon CloudFront
GetInvalidation
View
Yes
Amazon CloudFront
GetCachePolicyConfig
View
Yes
Amazon CloudFront
UpdateRealtimeLogConfig
Edit
Yes
Amazon CloudFront
GetRealtimeLogConfig
View
Yes
Amazon CloudFront
UpdateFieldLevelEncryptionConfig
Edit
Yes
Amazon CloudFront
GetFieldLevelEncryptionConfig
View
Yes
Amazon CloudFront
GetKeyGroupConfig
View
Yes
Amazon CloudFront
ListDistributionsByKeyGroup
View
Yes
Amazon CloudFront
ListDistributionsByWebACLId
View
Yes
Amazon CloudFront
UpdateFieldLevelEncryptionProfile
Edit
Yes
Amazon CloudFront
GetFieldLevelEncryptionProfileConfig
View
Yes
Amazon CloudFront
UpdateDistribution
Edit
Yes
Amazon CloudFront
GetDistributionConfig
View
Yes
Amazon CloudFront
UpdateCachePolicy
Edit
Yes
Amazon CloudFront
GetCachePolicy
View
Yes
Amazon CloudFront
DeleteCachePolicy
Delete
Yes
Amazon CloudFront
GetFieldLevelEncryption
View
Yes
Amazon CloudFront
DeleteFieldLevelEncryptionConfig
Delete
Yes
Amazon CloudFront
UpdateCloudFrontOriginAccessIdentity
Edit
Yes
Amazon CloudFront
GetCloudFrontOriginAccessIdentityConfig
View
Yes
Amazon CloudFront
CreateStreamingDistribution
Create
Yes
Amazon CloudFront
ListStreamingDistributions
View
Yes
Amazon CloudFront
GetFieldLevelEncryptionProfile
View
Yes
Amazon CloudFront
DeleteFieldLevelEncryptionProfile
Delete
Yes
Amazon CloudFront
ListDistributionsByCachePolicyId
View
Yes
Amazon CloudFront
CreatePublicKey
Create
Yes
Amazon CloudFront
ListPublicKeys
View
Yes
Amazon CloudFront
CreateRealtimeLogConfig
Create
Yes
Amazon CloudFront
ListRealtimeLogConfigs
View
Yes
Amazon CloudFront
UntagResource
Delete
Yes
Amazon CloudFront
UpdatePublicKey
Edit
Yes
Amazon CloudFront
GetPublicKeyConfig
View
Yes
Amazon CloudFront
TagResource
Create
Yes
Amazon CloudFront
UpdateOriginRequestPolicy
Edit
Yes
Amazon CloudFront
GetOriginRequestPolicy
View
Yes
Amazon CloudFront
DeleteOriginRequestPolicy
Delete
Yes
Amazon CloudFront
CreateOriginRequestPolicy
Create
Yes
Amazon CloudFront
ListOriginRequestPolicies
View
Yes
Amazon CloudFront
UpdateKeyGroup
Edit
Yes
Amazon CloudFront
GetKeyGroup
View
Yes
Amazon CloudFront
DeleteKeyGroup
Delete
Yes
Amazon CloudFront
CreateCloudFrontOriginAccessIdentity
Create
Yes
Amazon CloudFront
ListCloudFrontOriginAccessIdentities
View
Yes
Amazon CloudFront
GetDistribution
View
Yes
Amazon CloudFront
DeleteDistribution
Delete
Yes
Amazon CloudFront
ListDistributionsByRealtimeLogConfig
View
Yes
Amazon CloudFront
CreateKeyGroup
Create
Yes
Amazon CloudFront
ListKeyGroups
View
Yes
Amazon CloudFront
CreateInvalidation
Create
Yes
Amazon CloudFront
ListInvalidations
View
Yes
Amazon CloudFront
GetPublicKey
View
Yes
Amazon CloudFront
DeletePublicKey
Delete
Yes
Amazon CloudFront
ListTagsForResource
View
Yes
Amazon CloudFront
DeleteRealtimeLogConfig
Delete
Yes
Amazon CloudFront
CreateFieldLevelEncryptionConfig
Create
Yes
Amazon CloudFront
ListFieldLevelEncryptionConfigs
View
Yes
Amazon CloudFront
GetOriginRequestPolicyConfig
View
Yes
Amazon CloudFront
CreateStreamingDistributionWithTags
Create
Yes
Amazon CloudFront
CreateFieldLevelEncryptionProfile
Create
Yes
Amazon CloudFront
ListFieldLevelEncryptionProfiles
View
Yes
Amazon CloudFront
CreateDistributionWithTags
Create
Yes
Amazon CloudFront
CreateDistribution
Create
Yes
Amazon CloudFront
ListDistributions
View
Yes
Amazon CloudFront
CreateCachePolicy
Create
Yes
Amazon CloudFront
ListCachePolicies
View
Yes
Amazon CloudFront
ListDistributionsByOriginRequestPolicyId
View
Yes
Amazon CloudFront
UpdateStreamingDistribution
Edit
Yes
Amazon CloudFront
GetStreamingDistributionConfig
View
Yes
Amazon CloudFront
CreateMonitoringSubscription
Create
Yes
Amazon CloudFront
GetMonitoringSubscription
View
Yes
Amazon CloudFront
DeleteMonitoringSubscription
Delete
Yes
Amazon CloudFront
GetStreamingDistribution
View
Yes
Amazon CloudFront
DeleteStreamingDistribution
Delete
Yes
Amazon CloudFront
GetCloudFrontOriginAccessIdentity
View
Yes
Amazon CloudFront
DeleteCloudFrontOriginAccessIdentity
Delete
Yes
Amazon CloudSearch
DefineExpression
Create
Yes
Amazon CloudSearch
DeleteExpression
Delete
Yes
Amazon CloudSearch
DefineIndexField
Create
Yes
Amazon CloudSearch
ListDomainNames
View
Yes
Amazon CloudSearch
CreateDomain
Create
Yes
Amazon CloudSearch
DescribeExpressions
View
Yes
Amazon CloudSearch
DefineSuggester
Create
Yes
Amazon CloudSearch
DescribeAnalysisSchemes
View
Yes
Amazon CloudSearch
DeleteIndexField
Delete
Yes
Amazon CloudSearch
DescribeSuggesters
View
Yes
Amazon CloudSearch
DefineAnalysisScheme
Create
Yes
Amazon CloudSearch
UpdateDomainEndpointOptions
Edit
Yes
Amazon CloudSearch
IndexDocuments
Create
Yes
Amazon CloudSearch
DescribeDomainEndpointOptions
View
Yes
Amazon CloudSearch
UpdateAvailabilityOptions
Edit
Yes
Amazon CloudSearch
BuildSuggesters
Create
Yes
Amazon CloudSearch
UpdateScalingParameters
Edit
Yes
Amazon CloudSearch
DescribeAvailabilityOptions
View
Yes
Amazon CloudSearch
DeleteDomain
Delete
Yes
Amazon CloudSearch
DescribeServiceAccessPolicies
View
Yes
Amazon CloudSearch
DeleteSuggester
Delete
Yes
Amazon CloudSearch
DeleteAnalysisScheme
Delete
Yes
Amazon CloudSearch
DescribeIndexFields
View
Yes
Amazon CloudSearch
UpdateServiceAccessPolicies
Edit
Yes
Amazon CloudSearch
DescribeScalingParameters
View
Yes
Amazon CloudSearch
DescribeDomains
View
Yes
Amazon CloudTrail
AddTags
Create
Yes
Amazon CloudTrail
GetEventSelectors
View
Yes
Amazon CloudTrail
GetTrailStatus
View
Yes
Amazon CloudTrail
DescribeTrails
View
Yes
Amazon CloudTrail
PutEventSelectors
Edit
Yes
Amazon CloudTrail
StartLogging
Start
Yes
Amazon CloudTrail
CreateTrail
Create
Yes
Amazon CloudTrail
DeleteTrail
Delete
Yes
Amazon CloudTrail
LookupEvents
Create
Yes
Amazon CloudTrail
GetTrail
View
Yes
Amazon CloudTrail
GetInsightSelectors
View
Yes
Amazon CloudTrail
ListPublicKeys
View
Yes
Amazon CloudTrail
PutInsightSelectors
Edit
Yes
Amazon CloudTrail
RemoveTags
Delete
Yes
Amazon CloudTrail
UpdateTrail
Edit
Yes
Amazon CloudTrail
ListTags
View
Yes
Amazon CloudTrail
ListTrails
View
Yes
Amazon CloudTrail
StopLogging
Stop
Yes
Amazon CloudWatch
GetDashboard
View
Yes
Amazon CloudWatch
EnableAlarmActions
Enable
Yes
Amazon CloudWatch
DisableAlarmActions
Delete
Yes
Amazon CloudWatch
DescribeAlarmsForMetric
View
Yes
Amazon CloudWatch
ListTagsForResource
View
Yes
Amazon CloudWatch
PutAnomalyDetector
Edit
Yes
Amazon CloudWatch
DescribeAnomalyDetectors
View
Yes
Amazon CloudWatch
DeleteAnomalyDetector
Delete
Yes
Amazon CloudWatch
DescribeAlarms
View
Yes
Amazon CloudWatch
ListDashboards
View
Yes
Amazon CloudWatch
DeleteInsightRules
Delete
Yes
Amazon CloudWatch
GetMetricStream
View
Yes
Amazon CloudWatch
StopMetricStreams
Stop
Yes
Amazon CloudWatch
GetMetricWidgetImage
View
Yes
Amazon CloudWatch
PutMetricStream
Edit
Yes
Amazon CloudWatch
DescribeAlarmHistory
View
Yes
Amazon CloudWatch
GetMetricData
View
Yes
Amazon CloudWatch
DeleteDashboards
Delete
Yes
Amazon CloudWatch
PutCompositeAlarm
Edit
Yes
Amazon CloudWatch
PutInsightRule
Edit
Yes
Amazon CloudWatch
PutMetricAlarm
Edit
Yes
Amazon CloudWatch
PutDashboard
Edit
Yes
Amazon CloudWatch
StartMetricStreams
Start
Yes
Amazon CloudWatch
DeleteMetricStream
Delete
Yes
Amazon CloudWatch
UntagResource
Delete
Yes
Amazon CloudWatch
EnableInsightRules
Enable
Yes
Amazon CloudWatch
DescribeInsightRules
View
Yes
Amazon CloudWatch
SetAlarmState
Create
Yes
Amazon CloudWatch
GetInsightRuleReport
View
Yes
Amazon CloudWatch
GetMetricStatistics
View
Yes
Amazon CloudWatch
TagResource
Create
Yes
Amazon CloudWatch
PutMetricData
Edit
Yes
Amazon CloudWatch
DisableInsightRules
Delete
Yes
Amazon CloudWatch
DeleteAlarms
Delete
Yes
Amazon CloudWatch
ListMetricStreams
View
Yes
Amazon CloudWatch
ListMetrics
View
Yes
Amazon CloudWatch Application Insights
DescribeComponent
View
Yes
Amazon CloudWatch Application Insights
ListLogPatternSets
View
Yes
Amazon CloudWatch Application Insights
UntagResource
Delete
Yes
Amazon CloudWatch Application Insights
DescribeLogPattern
View
Yes
Amazon CloudWatch Application Insights
CreateComponent
Create
Yes
Amazon CloudWatch Application Insights
DescribeComponentConfigurationRecommendation
View
Yes
Amazon CloudWatch Application Insights
UpdateComponentConfiguration
Edit
Yes
Amazon CloudWatch Application Insights
ListConfigurationHistory
View
Yes
Amazon CloudWatch Application Insights
DescribeProblem
View
Yes
Amazon CloudWatch Application Insights
ListProblems
View
Yes
Amazon CloudWatch Application Insights
CreateLogPattern
Create
Yes
Amazon CloudWatch Application Insights
DescribeObservation
View
Yes
Amazon CloudWatch Application Insights
ListTagsForResource
View
Yes
Amazon CloudWatch Application Insights
ListApplications
View
Yes
Amazon CloudWatch Application Insights
DeleteApplication
Delete
Yes
Amazon CloudWatch Application Insights
DeleteComponent
Delete
Yes
Amazon CloudWatch Application Insights
DeleteLogPattern
Delete
Yes
Amazon CloudWatch Application Insights
CreateApplication
Create
Yes
Amazon CloudWatch Application Insights
ListComponents
View
Yes
Amazon CloudWatch Application Insights
TagResource
Create
Yes
Amazon CloudWatch Application Insights
DescribeApplication
View
Yes
Amazon CloudWatch Application Insights
DescribeProblemObservations
View
Yes
Amazon CloudWatch Application Insights
UpdateApplication
Edit
Yes
Amazon CloudWatch Application Insights
UpdateComponent
Edit
Yes
Amazon CloudWatch Application Insights
DescribeComponentConfiguration
View
Yes
Amazon CloudWatch Application Insights
ListLogPatterns
View
Yes
Amazon CloudWatch Application Insights
UpdateLogPattern
Edit
Yes
Amazon CloudWatch Events
DeletePartnerEventSource
Delete
Yes
Amazon CloudWatch Events
EnableRule
Enable
Yes
Amazon CloudWatch Events
DescribeArchive
View
Yes
Amazon CloudWatch Events
PutPartnerEvents
Edit
Yes
Amazon CloudWatch Events
UntagResource
Delete
Yes
Amazon CloudWatch Events
DescribeConnection
View
Yes
Amazon CloudWatch Events
PutPermission
Edit
Yes
Amazon CloudWatch Events
ListPartnerEventSources
View
Yes
Amazon CloudWatch Events
ListTargetsByRule
View
Yes
Amazon CloudWatch Events
TestEventPattern
Create
Yes
Amazon CloudWatch Events
DescribeRule
View
Yes
Amazon CloudWatch Events
ListRuleNamesByTarget
View
Yes
Amazon CloudWatch Events
ListEventSources
View
Yes
Amazon CloudWatch Events
DeauthorizeConnection
Create
Yes
Amazon CloudWatch Events
CreateApiDestination
Create
Yes
Amazon CloudWatch Events
CancelReplay
Delete
Yes
Amazon CloudWatch Events
RemovePermission
Delete
Yes
Amazon CloudWatch Events
DeleteEventBus
Delete
Yes
Amazon CloudWatch Events
DeleteConnection
Delete
Yes
Amazon CloudWatch Events
DeactivateEventSource
Deactivate
Yes
Amazon CloudWatch Events
RemoveTargets
Delete
Yes
Amazon CloudWatch Events
DeleteRule
Delete
Yes
Amazon CloudWatch Events
UpdateArchive
Edit
Yes
Amazon CloudWatch Events
DescribeApiDestination
View
Yes
Amazon CloudWatch Events
DescribeReplay
View
Yes
Amazon CloudWatch Events
ListRules
View
Yes
Amazon CloudWatch Events
ListArchives
View
Yes
Amazon CloudWatch Events
CreateEventBus
Create
Yes
Amazon CloudWatch Events
ListEventBuses
View
Yes
Amazon CloudWatch Events
PutRule
Edit
Yes
Amazon CloudWatch Events
CreateArchive
Create
Yes
Amazon CloudWatch Events
ListTagsForResource
View
Yes
Amazon CloudWatch Events
UpdateApiDestination
Edit
Yes
Amazon CloudWatch Events
DeleteApiDestination
Delete
Yes
Amazon CloudWatch Events
ListPartnerEventSourceAccounts
View
Yes
Amazon CloudWatch Events
DisableRule
Delete
Yes
Amazon CloudWatch Events
TagResource
Create
Yes
Amazon CloudWatch Events
CreateConnection
Create
Yes
Amazon CloudWatch Events
DescribeEventSource
View
Yes
Amazon CloudWatch Events
DeleteArchive
Delete
Yes
Amazon CloudWatch Events
CreatePartnerEventSource
Create
Yes
Amazon CloudWatch Events
StartReplay
Start
Yes
Amazon CloudWatch Events
UpdateConnection
Edit
Yes
Amazon CloudWatch Events
ListApiDestinations
View
Yes
Amazon CloudWatch Events
DescribeEventBus
View
Yes
Amazon CloudWatch Events
DescribePartnerEventSource
View
Yes
Amazon CloudWatch Events
PutTargets
Edit
Yes
Amazon CloudWatch Events
ListReplays
View
Yes
Amazon CloudWatch Events
ActivateEventSource
Activate
Yes
Amazon CloudWatch Events
PutEvents
Edit
Yes
Amazon CloudWatch Events
ListConnections
View
Yes
Amazon CloudWatch Logs
DescribeResourcePolicies
View
Yes
Amazon CloudWatch Logs
PutSubscriptionFilter
Edit
Yes
Amazon CloudWatch Logs
FilterLogEvents
Create
Yes
Amazon CloudWatch Logs
PutRetentionPolicy
Edit
Yes
Amazon CloudWatch Logs
DeleteRetentionPolicy
Delete
Yes
Amazon CloudWatch Logs
GetQueryResults
View
Yes
Amazon CloudWatch Logs
DescribeQueryDefinitions
View
Yes
Amazon CloudWatch Logs
DeleteDestination
Delete
Yes
Amazon CloudWatch Logs
TagLogGroup
Create
Yes
Amazon CloudWatch Logs
DescribeQueries
View
Yes
Amazon CloudWatch Logs
DisassociateKmsKey
Delete
Yes
Amazon CloudWatch Logs
DeleteQueryDefinition
Delete
Yes
Amazon CloudWatch Logs
StartQuery
Start
Yes
Amazon CloudWatch Logs
CreateExportTask
Create
Yes
Amazon CloudWatch Logs
DescribeLogGroups
View
Yes
Amazon CloudWatch Logs
AssociateKmsKey
Create
Yes
Amazon CloudWatch Logs
CreateLogGroup
Create
Yes
Amazon CloudWatch Logs
PutQueryDefinition
Edit
Yes
Amazon CloudWatch Logs
CancelExportTask
Delete
Yes
Amazon CloudWatch Logs
DeleteMetricFilter
Delete
Yes
Amazon CloudWatch Logs
DeleteSubscriptionFilter
Delete
Yes
Amazon CloudWatch Logs
DescribeLogStreams
View
Yes
Amazon CloudWatch Logs
StopQuery
Stop
Yes
Amazon CloudWatch Logs
GetLogEvents
View
Yes
Amazon CloudWatch Logs
PutLogEvents
Edit
Yes
Amazon CloudWatch Logs
UntagLogGroup
Delete
Yes
Amazon CloudWatch Logs
DescribeDestinations
View
Yes
Amazon CloudWatch Logs
DeleteResourcePolicy
Delete
Yes
Amazon CloudWatch Logs
DescribeExportTasks
View
Yes
Amazon CloudWatch Logs
TestMetricFilter
Create
Yes
Amazon CloudWatch Logs
CreateLogStream
Create
Yes
Amazon CloudWatch Logs
ListTagsLogGroup
View
Yes
Amazon CloudWatch Logs
DeleteLogStream
Delete
Yes
Amazon CloudWatch Logs
DescribeSubscriptionFilters
View
Yes
Amazon CloudWatch Logs
PutDestinationPolicy
Edit
Yes
Amazon CloudWatch Logs
PutResourcePolicy
Edit
Yes
Amazon CloudWatch Logs
PutMetricFilter
Edit
Yes
Amazon CloudWatch Logs
PutDestination
Edit
Yes
Amazon CloudWatch Logs
DeleteLogGroup
Delete
Yes
Amazon CloudWatch Logs
GetLogGroupFields
View
Yes
Amazon CloudWatch Logs
DescribeMetricFilters
View
Yes
Amazon CloudWatch Logs
GetLogRecord
View
Yes
Amazon Database Migration Service
RefreshSchemas
Create
Yes
Amazon Database Migration Service
StartReplicationTaskAssessmentRun
Start
Yes
Amazon Database Migration Service
CancelReplicationTaskAssessmentRun
Delete
Yes
Amazon Database Migration Service
MoveReplicationTask
Move
Yes
Amazon Database Migration Service
DescribeReplicationTaskAssessmentResults
View
Yes
Amazon Database Migration Service
ImportCertificate
Create
Yes
Amazon Database Migration Service
DescribeReplicationInstances
View
Yes
Amazon Database Migration Service
DescribeEndpoints
View
Yes
Amazon Database Migration Service
DescribeReplicationTaskIndividualAssessments
View
Yes
Amazon Database Migration Service
DeleteReplicationInstance
Delete
Yes
Amazon Database Migration Service
DeleteConnection
Delete
Yes
Amazon Database Migration Service
DescribeEndpointSettings
View
Yes
Amazon Database Migration Service
DescribeCertificates
View
Yes
Amazon Database Migration Service
DescribeReplicationInstanceTaskLogs
View
Yes
Amazon Database Migration Service
DeleteEndpoint
Delete
Yes
Amazon Database Migration Service
CreateReplicationInstance
Create
Yes
Amazon Database Migration Service
DescribeEventCategories
View
Yes
Amazon Database Migration Service
ListTagsForResource
View
Yes
Amazon Database Migration Service
DescribeEventSubscriptions
View
Yes
Amazon Database Migration Service
DescribeRefreshSchemasStatus
View
Yes
Amazon Database Migration Service
RebootReplicationInstance
Reboot
Yes
Amazon Database Migration Service
ModifyReplicationTask
Edit
Yes
Amazon Database Migration Service
CreateReplicationSubnetGroup
Create
Yes
Amazon Database Migration Service
StartReplicationTask
Start
Yes
Amazon Database Migration Service
StopReplicationTask
Stop
Yes
Amazon Database Migration Service
DescribeReplicationTasks
View
Yes
Amazon Database Migration Service
DeleteReplicationTask
Delete
Yes
Amazon Database Migration Service
ModifyEndpoint
Edit
Yes
Amazon Database Migration Service
StartReplicationTaskAssessment
Start
Yes
Amazon Database Migration Service
DescribeTableStatistics
View
Yes
Amazon Database Migration Service
DescribeAccountAttributes
View
Yes
Amazon Database Migration Service
DescribeEvents
View
Yes
Amazon Database Migration Service
DeleteCertificate
Delete
Yes
Amazon Database Migration Service
RemoveTagsFromResource
Delete
Yes
Amazon Database Migration Service
DeleteReplicationSubnetGroup
Delete
Yes
Amazon Database Migration Service
AddTagsToResource
Create
Yes
Amazon Database Migration Service
ReloadTables
Create
Yes
Amazon Database Migration Service
TestConnection
Create
Yes
Amazon Database Migration Service
DeleteEventSubscription
Delete
Yes
Amazon Database Migration Service
DescribeSchemas
View
Yes
Amazon Database Migration Service
ModifyReplicationSubnetGroup
Edit
Yes
Amazon Database Migration Service
DescribeReplicationSubnetGroups
View
Yes
Amazon Database Migration Service
DeleteReplicationTaskAssessmentRun
Delete
Yes
Amazon Database Migration Service
DescribeOrderableReplicationInstances
View
Yes
Amazon Database Migration Service
CreateEventSubscription
Create
Yes
Amazon Database Migration Service
DescribeApplicableIndividualAssessments
View
Yes
Amazon Database Migration Service
CreateEndpoint
Create
Yes
Amazon Database Migration Service
DescribeConnections
View
Yes
Amazon Database Migration Service
DescribeReplicationTaskAssessmentRuns
View
Yes
Amazon Database Migration Service
ModifyReplicationInstance
Edit
Yes
Amazon Database Migration Service
DescribeEndpointTypes
View
Yes
Amazon Database Migration Service
CreateReplicationTask
Create
Yes
Amazon Database Migration Service
DescribePendingMaintenanceActions
View
Yes
Amazon Database Migration Service
ApplyPendingMaintenanceAction
Edit
Yes
Amazon Database Migration Service
ModifyEventSubscription
Edit
Yes
Amazon Direct Connect
CreatePublicVirtualInterface
Create
Yes
Amazon Direct Connect
DescribeLags
View
Yes
Amazon Direct Connect
DeleteDirectConnectGatewayAssociation
Delete
Yes
Amazon Direct Connect
AllocatePublicVirtualInterface
Create
Yes
Amazon Direct Connect
DescribeConnectionLoa
View
Yes
Amazon Direct Connect
DeleteConnection
Delete
Yes
Amazon Direct Connect
CreateLag
Create
Yes
Amazon Direct Connect
DescribeVirtualGateways
View
Yes
Amazon Direct Connect
DescribeVirtualInterfaces
View
Yes
Amazon Direct Connect
DescribeDirectConnectGatewayAssociationProposals
View
Yes
Amazon Direct Connect
DescribeDirectConnectGatewayAssociations
View
Yes
Amazon Direct Connect
CreateDirectConnectGatewayAssociation
Create
Yes
Amazon Direct Connect
DescribeDirectConnectGateways
View
Yes
Amazon Direct Connect
DescribeTags
View
Yes
Amazon Direct Connect
DeleteBGPPeer
Delete
Yes
Amazon Direct Connect
StartBgpFailoverTest
Start
Yes
Amazon Direct Connect
DescribeConnectionsOnInterconnect
View
Yes
Amazon Direct Connect
ListVirtualInterfaceTestHistory
View
Yes
Amazon Direct Connect
AssociateHostedConnection
Create
Yes
Amazon Direct Connect
AcceptDirectConnectGatewayAssociationProposal
Approve
Yes
Amazon Direct Connect
UntagResource
Delete
Yes
Amazon Direct Connect
DisassociateConnectionFromLag
Delete
Yes
Amazon Direct Connect
DescribeLocations
View
Yes
Amazon Direct Connect
UpdateDirectConnectGatewayAssociation
Edit
Yes
Amazon Direct Connect
AllocateTransitVirtualInterface
Create
Yes
Amazon Direct Connect
DescribeDirectConnectGatewayAttachments
View
Yes
Amazon Direct Connect
CreateDirectConnectGatewayAssociationProposal
Create
Yes
Amazon Direct Connect
CreateConnection
Create
Yes
Amazon Direct Connect
ConfirmPublicVirtualInterface
Create
Yes
Amazon Direct Connect
ConfirmPrivateVirtualInterface
Create
Yes
Amazon Direct Connect
UpdateConnection
Edit
Yes
Amazon Direct Connect
DescribeConnections
View
Yes
Amazon Direct Connect
DeleteVirtualInterface
Delete
Yes
Amazon Direct Connect
UpdateLag
Edit
Yes
Amazon Direct Connect
ConfirmTransitVirtualInterface
Create
Yes
Amazon Direct Connect
AllocateConnectionOnInterconnect
Create
Yes
Amazon Direct Connect
CreateBGPPeer
Create
Yes
Amazon Direct Connect
DeleteInterconnect
Delete
Yes
Amazon Direct Connect
DescribeInterconnectLoa
View
Yes
Amazon Direct Connect
DeleteDirectConnectGatewayAssociationProposal
Delete
Yes
Amazon Direct Connect
AssociateMacSecKey
Create
Yes
Amazon Direct Connect
CreateTransitVirtualInterface
Create
Yes
Amazon Direct Connect
DescribeInterconnects
View
Yes
Amazon Direct Connect
AllocateHostedConnection
Create
Yes
Amazon Direct Connect
AssociateConnectionWithLag
Create
Yes
Amazon Direct Connect
ConfirmConnection
Create
Yes
Amazon Direct Connect
StopBgpFailoverTest
Stop
Yes
Amazon Direct Connect
CreateDirectConnectGateway
Create
Yes
Amazon Direct Connect
DeleteDirectConnectGateway
Delete
Yes
Amazon Direct Connect
DisassociateMacSecKey
Delete
Yes
Amazon Direct Connect
AllocatePrivateVirtualInterface
Create
Yes
Amazon Direct Connect
DescribeHostedConnections
View
Yes
Amazon Direct Connect
DeleteLag
Delete
Yes
Amazon Direct Connect
CreateInterconnect
Create
Yes
Amazon Direct Connect
DescribeLoa
View
Yes
Amazon Direct Connect
AssociateVirtualInterface
Create
Yes
Amazon Direct Connect
CreatePrivateVirtualInterface
Create
Yes
Amazon Direct Connect
TagResource
Create
Yes
Amazon Direct Connect
UpdateVirtualInterfaceAttributes
Edit
Yes
Amazon Directory Service
UpdateRadius
Edit
Yes
Amazon Directory Service
DescribeEventTopics
View
Yes
Amazon Directory Service
DescribeLDAPSSettings
View
Yes
Amazon Directory Service
DisableLDAPS
Delete
Yes
Amazon Directory Service
ListTagsForResource
View
Yes
Amazon Directory Service
EnableRadius
Enable
Yes
Amazon Directory Service
AcceptSharedDirectory
Approve
Yes
Amazon Directory Service
AddTagsToResource
Create
Yes
Amazon Directory Service
EnableSso
Enable
Yes
Amazon Directory Service
UnshareDirectory
Create
Yes
Amazon Directory Service
VerifyTrust
Create
Yes
Amazon Directory Service
RegisterEventTopic
Register
Yes
Amazon Directory Service
DeleteTrust
Delete
Yes
Amazon Directory Service
DeleteDirectory
Delete
Yes
Amazon Directory Service
ListSchemaExtensions
View
Yes
Amazon Directory Service
AddRegion
Create
Yes
Amazon Directory Service
EnableClientAuthentication
Enable
Yes
Amazon Directory Service
DescribeCertificate
View
Yes
Amazon Directory Service
ListLogSubscriptions
View
Yes
Amazon Directory Service
DeregisterEventTopic
Deregister
Yes
Amazon Directory Service
RejectSharedDirectory
Reject
Yes
Amazon Directory Service
RegisterCertificate
Register
Yes
Amazon Directory Service
UpdateConditionalForwarder
Edit
Yes
Amazon Directory Service
ListIpRoutes
View
Yes
Amazon Directory Service
DisableSso
Delete
Yes
Amazon Directory Service
RemoveRegion
Delete
Yes
Amazon Directory Service
DescribeSnapshots
View
Yes
Amazon Directory Service
DeleteLogSubscription
Delete
Yes
Amazon Directory Service
ListCertificates
View
Yes
Amazon Directory Service
CreateSnapshot
Create
Yes
Amazon Directory Service
DescribeRegions
View
Yes
Amazon Directory Service
RemoveTagsFromResource
Delete
Yes
Amazon Directory Service
DescribeDomainControllers
View
Yes
Amazon Directory Service
EnableLDAPS
Enable
Yes
Amazon Directory Service
UpdateNumberOfDomainControllers
Edit
Yes
Amazon Directory Service
DisableRadius
Delete
Yes
Amazon Directory Service
DescribeSharedDirectories
View
Yes
Amazon Directory Service
AddIpRoutes
Create
Yes
Amazon Directory Service
CreateMicrosoftAD
Create
Yes
Amazon Directory Service
RemoveIpRoutes
Delete
Yes
Amazon Directory Service
CancelSchemaExtension
Delete
Yes
Amazon Directory Service
DisableClientAuthentication
Delete
Yes
Amazon Directory Service
GetSnapshotLimits
View
Yes
Amazon Directory Service
DescribeConditionalForwarders
View
Yes
Amazon Directory Service
StartSchemaExtension
Start
Yes
Amazon Directory Service
ShareDirectory
Create
Yes
Amazon Directory Service
DescribeDirectories
View
Yes
Amazon Directory Service
DescribeTrusts
View
Yes
Amazon Directory Service
DeleteSnapshot
Delete
Yes
Amazon Directory Service
CreateConditionalForwarder
Create
Yes
Amazon Directory Service
UpdateTrust
Edit
Yes
Amazon Directory Service
ResetUserPassword
Edit
Yes
Amazon Directory Service
ConnectDirectory
Create
Yes
Amazon Directory Service
CreateLogSubscription
Create
Yes
Amazon Directory Service
CreateComputer
Create
Yes
Amazon Directory Service
RestoreFromSnapshot
Create
Yes
Amazon Directory Service
GetDirectoryLimits
View
Yes
Amazon Directory Service
DeregisterCertificate
Deregister
Yes
Amazon Directory Service
CreateTrust
Create
Yes
Amazon Directory Service
DeleteConditionalForwarder
Delete
Yes
Amazon Directory Service
CreateDirectory
Create
Yes
Amazon Directory Service
CreateAlias
Create
Yes
Amazon DynamoDB
UpdateTableReplicaAutoScaling
Edit
Yes
Amazon DynamoDB
UpdateContributorInsights
Edit
Yes
Amazon DynamoDB
DescribeContributorInsights
View
Yes
Amazon DynamoDB
Query
Create
Yes
Amazon DynamoDB
CreateTable
Create
Yes
Amazon DynamoDB
UpdateContinuousBackups
Edit
Yes
Amazon DynamoDB
RestoreTableToPointInTime
Create
Yes
Amazon DynamoDB
ListContributorInsights
View
Yes
Amazon DynamoDB
DescribeEndpoints
View
Yes
Amazon DynamoDB
DescribeTimeToLive
View
Yes
Amazon DynamoDB
ExecuteStatement
Create
Yes
Amazon DynamoDB
TagResource
Create
Yes
Amazon DynamoDB
ExportTableToPointInTime
View
Yes
Amazon DynamoDB
DisableKinesisStreamingDestination
Delete
Yes
Amazon DynamoDB
CreateBackup
Create
Yes
Amazon DynamoDB
DeleteBackup
Delete
Yes
Amazon DynamoDB
TransactGetItems
Create
Yes
Amazon DynamoDB
DescribeGlobalTable
View
Yes
Amazon DynamoDB
DeleteItem
Delete
Yes
Amazon DynamoDB
TransactWriteItems
Create
Yes
Amazon DynamoDB
DescribeTable
View
Yes
Amazon DynamoDB
DescribeLimits
View
Yes
Amazon DynamoDB
ListTagsOfResource
View
Yes
Amazon DynamoDB
EnableKinesisStreamingDestination
Enable
Yes
Amazon DynamoDB
DescribeGlobalTableSettings
View
Yes
Amazon DynamoDB
UpdateTimeToLive
Edit
Yes
Amazon DynamoDB
ListExports
View
Yes
Amazon DynamoDB
DescribeKinesisStreamingDestination
View
Yes
Amazon DynamoDB
ListTables
View
Yes
Amazon DynamoDB
ListBackups
View
Yes
Amazon DynamoDB
DescribeBackup
View
Yes
Amazon DynamoDB
UpdateItem
Edit
Yes
Amazon DynamoDB
Scan
Create
Yes
Amazon DynamoDB
DescribeTableReplicaAutoScaling
View
Yes
Amazon DynamoDB
DeleteTable
Delete
Yes
Amazon DynamoDB
CreateGlobalTable
Create
Yes
Amazon DynamoDB
GetItem
View
Yes
Amazon DynamoDB
UntagResource
Delete
Yes
Amazon DynamoDB
UpdateGlobalTableSettings
Edit
Yes
Amazon DynamoDB
UpdateTable
Edit
Yes
Amazon DynamoDB
DescribeExport
View
Yes
Amazon DynamoDB
ListGlobalTables
View
Yes
Amazon DynamoDB
RestoreTableFromBackup
Create
Yes
Amazon DynamoDB
ExecuteTransaction
Create
Yes
Amazon DynamoDB
PutItem
Edit
Yes
Amazon DynamoDB
WriteItem
Create
Yes
Amazon DynamoDB
UpdateGlobalTable
Edit
Yes
Amazon DynamoDB
DescribeContinuousBackups
View
Yes
Amazon DynamoDB Accelerator (DAX)
DecreaseReplicationFactor
Edit
Yes
Amazon DynamoDB Accelerator (DAX)
DescribeClusters
View
Yes
Amazon DynamoDB Accelerator (DAX)
RebootNode
Reboot
Yes
Amazon DynamoDB Accelerator (DAX)
DescribeEvents
View
Yes
Amazon DynamoDB Accelerator (DAX)
CreateParameterGroup
Create
Yes
Amazon DynamoDB Accelerator (DAX)
CreateCluster
Create
Yes
Amazon DynamoDB Accelerator (DAX)
IncreaseReplicationFactor
Edit
Yes
Amazon DynamoDB Accelerator (DAX)
UpdateSubnetGroup
Edit
Yes
Amazon DynamoDB Accelerator (DAX)
DescribeParameterGroups
View
Yes
Amazon DynamoDB Accelerator (DAX)
DeleteSubnetGroup
Delete
Yes
Amazon DynamoDB Accelerator (DAX)
UpdateCluster
Edit
Yes
Amazon DynamoDB Accelerator (DAX)
DeleteCluster
Delete
Yes
Amazon DynamoDB Accelerator (DAX)
TagResource
Create
Yes
Amazon DynamoDB Accelerator (DAX)
DescribeSubnetGroups
View
Yes
Amazon DynamoDB Accelerator (DAX)
ListTags
View
Yes
Amazon DynamoDB Accelerator (DAX)
DeleteParameterGroup
Delete
Yes
Amazon DynamoDB Accelerator (DAX)
UntagResource
Delete
Yes
Amazon DynamoDB Accelerator (DAX)
UpdateParameterGroup
Edit
Yes
Amazon DynamoDB Accelerator (DAX)
DescribeParameters
View
Yes
Amazon DynamoDB Accelerator (DAX)
DescribeDefaultParameters
View
Yes
Amazon DynamoDB Accelerator (DAX)
CreateSubnetGroup
Create
Yes
Amazon DynamoDB Streams
ListStreams
View
Yes
Amazon DynamoDB Streams
DescribeStream
View
Yes
Amazon DynamoDB Streams
GetShardIterator
View
Yes
Amazon DynamoDB Streams
GetRecords
View
Yes
Amazon EC2
CreateRoute
Create
Yes
Amazon EC2
RejectTransitGatewayVpcAttachment
Reject
Yes
Amazon EC2
RegisterTransitGatewayMulticastGroupSources
Register
Yes
Amazon EC2
GetTransitGatewayRouteTableAssociations
View
Yes
Amazon EC2
AssignPrivateIpAddresses
Create
Yes
Amazon EC2
CancelSpotInstanceRequests
Delete
Yes
Amazon EC2
UnmonitorInstances
Edit
Yes
Amazon EC2
DeleteVpnConnection
Delete
Yes
Amazon EC2
ModifyManagedPrefixList
Edit
Yes
Amazon EC2
CopySnapshot
Copy
Yes
Amazon EC2
DeregisterImage
Deregister
Yes
Amazon EC2
DeleteTrafficMirrorSession
Delete
Yes
Amazon EC2
EnableVpcClassicLink
Enable
Yes
Amazon EC2
CreateNetworkInterface
Create
Yes
Amazon EC2
DisableEbsEncryptionByDefault
Delete
Yes
Amazon EC2
DescribeVpcClassicLinkDnsSupport
View
Yes
Amazon EC2
DeleteTags
Delete
Yes
Amazon EC2
CreateTrafficMirrorFilterRule
Create
Yes
Amazon EC2
CreateCustomerGateway
Create
Yes
Amazon EC2
DescribePrincipalIdFormat
View
Yes
Amazon EC2
DescribeVpcs
View
Yes
Amazon EC2
CreateLaunchTemplate
Create
Yes
Amazon EC2
DeleteSpotDatafeedSubscription
Delete
Yes
Amazon EC2
CreateTags
Create
Yes
Amazon EC2
ModifyVpnConnection
Edit
Yes
Amazon EC2
ConfirmProductInstance
Create
Yes
Amazon EC2
DescribeVpnConnections
View
Yes
Amazon EC2
MoveAddressToVpc
Move
Yes
Amazon EC2
DescribeNetworkInterfaceAttribute
View
Yes
Amazon EC2
ModifyVpcPeeringConnectionOptions
Edit
Yes
Amazon EC2
DescribeSpotPriceHistory
View
Yes
Amazon EC2
ExportImage
View
Yes
Amazon EC2
ModifyTransitGateway
Edit
Yes
Amazon EC2
DisassociateEnclaveCertificateIamRole
Delete
Yes
Amazon EC2
CreateClientVpnEndpoint
Create
Yes
Amazon EC2
AttachNetworkInterface
Attach
Yes
Amazon EC2
CancelImportTask
Delete
Yes
Amazon EC2
DeleteQueuedReservedInstances
Delete
Yes
Amazon EC2
DisassociateSubnetCidrBlock
Delete
Yes
Amazon EC2
DescribeVpcAttribute
View
Yes
Amazon EC2
CreateVpcEndpointServiceConfiguration
Create
Yes
Amazon EC2
RevokeSecurityGroupIngress
Delete
Yes
Amazon EC2
CreateFleet
Create
Yes
Amazon EC2
ModifyVpnConnectionOptions
Edit
Yes
Amazon EC2
DeleteTrafficMirrorFilterRule
Delete
Yes
Amazon EC2
CreateLocalGatewayRouteTableVpcAssociation
Create
Yes
Amazon EC2
ApplySecurityGroupsToClientVpnTargetNetwork
Edit
Yes
Amazon EC2
DescribeAccountAttributes
View
Yes
Amazon EC2
ModifyIdentityIdFormat
Edit
Yes
Amazon EC2
CreateReservedInstancesListing
Create
Yes
Amazon EC2
ReplaceRoute
Create
Yes
Amazon EC2
AuthorizeSecurityGroupEgress
Create
Yes
Amazon EC2
CreateTransitGatewayConnect
Create
Yes
Amazon EC2
DescribeClassicLinkInstances
View
Yes
Amazon EC2
DeleteNetworkAclEntry
Delete
Yes
Amazon EC2
DescribeAvailabilityZones
View
Yes
Amazon EC2
DescribeVolumeAttribute
View
Yes
Amazon EC2
DeleteDhcpOptions
Delete
Yes
Amazon EC2
CreateNatGateway
Create
Yes
Amazon EC2
DeleteClientVpnEndpoint
Delete
Yes
Amazon EC2
RegisterImage
Register
Yes
Amazon EC2
CreateNetworkAclEntry
Create
Yes
Amazon EC2
DeleteRouteTable
Delete
Yes
Amazon EC2
DescribePublicIpvPools
View
Yes
Amazon EC2
ModifyVpcEndpointServiceConfiguration
Edit
Yes
Amazon EC2
CreateTransitGateway
Create
Yes
Amazon EC2
DeleteTransitGateway
Delete
Yes
Amazon EC2
AssociateTransitGatewayMulticastDomain
Create
Yes
Amazon EC2
ModifyCapacityReservation
Edit
Yes
Amazon EC2
CreateStoreImageTask
Create
Yes
Amazon EC2
PurchaseScheduledInstances
Purchase
Yes
Amazon EC2
ModifyVpcEndpoint
Edit
Yes
Amazon EC2
CreateRouteTable
Create
Yes
Amazon EC2
DescribeConversionTasks
View
Yes
Amazon EC2
DescribeAggregateIdFormat
View
Yes
Amazon EC2
DescribeEgressOnlyInternetGateways
View
Yes
Amazon EC2
DeleteVpcEndpointServiceConfigurations
Delete
Yes
Amazon EC2
DescribeSpotDatafeedSubscription
View
Yes
Amazon EC2
DescribeMovingAddresses
View
Yes
Amazon EC2
DescribeIdentityIdFormat
View
Yes
Amazon EC2
DescribeExportTasks
View
Yes
Amazon EC2
DescribeFleetHistory
View
Yes
Amazon EC2
DescribeSecurityGroupReferences
View
Yes
Amazon EC2
DescribeTransitGatewayPeeringAttachments
View
Yes
Amazon EC2
CreateSecurityGroup
Create
Yes
Amazon EC2
DeleteLocalGatewayRouteTableVpcAssociation
Delete
Yes
Amazon EC2
DeleteTransitGatewayMulticastDomain
Delete
Yes
Amazon EC2
CreateTransitGatewayPrefixListReference
Create
Yes
Amazon EC2
CreateKeyPair
Create
Yes
Amazon EC2
ModifyVpcEndpointConnectionNotification
Edit
Yes
Amazon EC2
DescribeCustomerGateways
View
Yes
Amazon EC2
UnassignIpvAddresses
Edit
Yes
Amazon EC2
ModifyVpnTunnelCertificate
Edit
Yes
Amazon EC2
CreateTrafficMirrorTarget
Create
Yes
Amazon EC2
CreateVpcPeeringConnection
Create
Yes
Amazon EC2
GetLaunchTemplateData
View
Yes
Amazon EC2
CancelExportTask
Delete
Yes
Amazon EC2
AcceptReservedInstancesExchangeQuote
Approve
Yes
Amazon EC2
ReplaceIamInstanceProfileAssociation
Create
Yes
Amazon EC2
CreateVpnConnection
Create
Yes
Amazon EC2
GetManagedPrefixListEntries
View
Yes
Amazon EC2
DeleteNatGateway
Delete
Yes
Amazon EC2
TerminateInstances
Terminate
Yes
Amazon EC2
AttachClassicLinkVpc
Attach
Yes
Amazon EC2
DescribeAddressesAttribute
View
Yes
Amazon EC2
CancelSpotFleetRequests
Delete
Yes
Amazon EC2
ModifyInstanceMetadataOptions
Edit
Yes
Amazon EC2
GetCapacityReservationUsage
View
Yes
Amazon EC2
DescribeFlowLogs
View
Yes
Amazon EC2
UnassignPrivateIpAddresses
Edit
Yes
Amazon EC2
DescribeScheduledInstanceAvailability
View
Yes
Amazon EC2
CreateReplaceRootVolumeTask
Create
Yes
Amazon EC2
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations
View
Yes
Amazon EC2
CreateVpcEndpoint
Create
Yes
Amazon EC2
UpdateSecurityGroupRuleDescriptionsIngress
Edit
Yes
Amazon EC2
RequestSpotFleet
Create
Yes
Amazon EC2
DescribeStoreImageTasks
View
Yes
Amazon EC2
ModifyNetworkInterfaceAttribute
Edit
Yes
Amazon EC2
ModifyVpnTunnelOptions
Edit
Yes
Amazon EC2
DescribeFpgaImages
View
Yes
Amazon EC2
DescribeSpotFleetRequests
View
Yes
Amazon EC2
DescribeVpcEndpointServiceConfigurations
View
Yes
Amazon EC2
CreateDhcpOptions
Create
Yes
Amazon EC2
ImportSnapshot
Create
Yes
Amazon EC2
CreateTransitGatewayRouteTable
Create
Yes
Amazon EC2
ModifySpotFleetRequest
Edit
Yes
Amazon EC2
CreateSubnet
Create
Yes
Amazon EC2
AssociateEnclaveCertificateIamRole
Create
Yes
Amazon EC2
CreateLocalGatewayRoute
Create
Yes
Amazon EC2
DescribeSpotFleetInstances
View
Yes
Amazon EC2
ExportClientVpnClientConfiguration
View
Yes
Amazon EC2
EnableVpcClassicLinkDnsSupport
Enable
Yes
Amazon EC2
DescribeVolumes
View
Yes
Amazon EC2
DeleteFlowLogs
Delete
Yes
Amazon EC2
ImportInstance
Create
Yes
Amazon EC2
DescribeClientVpnConnections
View
Yes
Amazon EC2
ModifyInstanceEventStartTime
Edit
Yes
Amazon EC2
DescribeCapacityReservations
View
Yes
Amazon EC2
RejectTransitGatewayMulticastDomainAssociations
Reject
Yes
Amazon EC2
DescribeTrafficMirrorTargets
View
Yes
Amazon EC2
ReplaceRouteTableAssociation
Create
Yes
Amazon EC2
DeregisterInstanceEventNotificationAttributes
Deregister
Yes
Amazon EC2
DeletePlacementGroup
Delete
Yes
Amazon EC2
DescribeTransitGatewayConnectPeers
View
Yes
Amazon EC2
DescribeElasticGpus
View
Yes
Amazon EC2
DescribeIdFormat
View
Yes
Amazon EC2
CreateVpc
Create
Yes
Amazon EC2
ModifyClientVpnEndpoint
Edit
Yes
Amazon EC2
GetTransitGatewayRouteTablePropagations
View
Yes
Amazon EC2
CreateNetworkAcl
Create
Yes
Amazon EC2
CopyFpgaImage
Copy
Yes
Amazon EC2
DescribeFastSnapshotRestores
View
Yes
Amazon EC2
StartVpcEndpointServicePrivateDnsVerification
Start
Yes
Amazon EC2
AttachInternetGateway
Attach
Yes
Amazon EC2
DescribeVpcEndpointServices
View
Yes
Amazon EC2
RevokeClientVpnIngress
Delete
Yes
Amazon EC2
CreateVolume
Create
Yes
Amazon EC2
DescribeSecurityGroups
View
Yes
Amazon EC2
DisassociateIamInstanceProfile
Delete
Yes
Amazon EC2
CreateCarrierGateway
Create
Yes
Amazon EC2
DescribeImportSnapshotTasks
View
Yes
Amazon EC2
DeleteLaunchTemplate
Delete
Yes
Amazon EC2
DeleteVpc
Delete
Yes
Amazon EC2
CreateTransitGatewayVpcAttachment
Create
Yes
Amazon EC2
DescribeInstanceEventNotificationAttributes
View
Yes
Amazon EC2
ReplaceNetworkAclAssociation
Create
Yes
Amazon EC2
ResetAddressAttribute
Edit
Yes
Amazon EC2
DetachVolume
Delete
Yes
Amazon EC2
CreateTransitGatewayRoute
Create
Yes
Amazon EC2
DescribeNetworkInsightsPaths
View
Yes
Amazon EC2
RestoreAddressToClassic
Create
Yes
Amazon EC2
GetTransitGatewayPrefixListReferences
View
Yes
Amazon EC2
DescribeImageAttribute
View
Yes
Amazon EC2
GetConsoleScreenshot
View
Yes
Amazon EC2
DeleteTransitGatewayPeeringAttachment
Delete
Yes
Amazon EC2
AssignIpvAddresses
Create
Yes
Amazon EC2
DescribeVolumesModifications
View
Yes
Amazon EC2
SearchTransitGatewayMulticastGroups
Search
Yes
Amazon EC2
DescribeInstanceCreditSpecifications
View
Yes
Amazon EC2
CreateLaunchTemplateVersion
Create
Yes
Amazon EC2
GetReservedInstancesExchangeQuote
View
Yes
Amazon EC2
AssociateRouteTable
Create
Yes
Amazon EC2
StopInstances
Stop
Yes
Amazon EC2
DescribeVpcEndpointConnectionNotifications
View
Yes
Amazon EC2
DeleteTransitGatewayPrefixListReference
Delete
Yes
Amazon EC2
DescribeVpcClassicLink
View
Yes
Amazon EC2
ImportClientVpnClientCertificateRevocationList
Create
Yes
Amazon EC2
DescribeFleets
View
Yes
Amazon EC2
DeleteNetworkInsightsAnalysis
Delete
Yes
Amazon EC2
CancelCapacityReservation
Delete
Yes
Amazon EC2
DescribeTransitGatewayVpcAttachments
View
Yes
Amazon EC2
RunInstances
Create
Yes
Amazon EC2
GetHostReservationPurchasePreview
View
Yes
Amazon EC2
DeleteClientVpnRoute
Delete
Yes
Amazon EC2
DescribeInstances
View
Yes
Amazon EC2
DescribeHosts
View
Yes
Amazon EC2
AdvertiseByoipCidr
Create
Yes
Amazon EC2
ModifyTransitGatewayVpcAttachment
Edit
Yes
Amazon EC2
ReleaseAddress
Create
Yes
Amazon EC2
ModifyLaunchTemplate
Edit
Yes
Amazon EC2
DescribeLocalGateways
View
Yes
Amazon EC2
GetDefaultCreditSpecification
View
Yes
Amazon EC2
DescribeSnapshots
View
Yes
Amazon EC2
DescribeInstanceTypes
View
Yes
Amazon EC2
DisableVpcClassicLink
Delete
Yes
Amazon EC2
ModifyHosts
Edit
Yes
Amazon EC2
ResetFpgaImageAttribute
Edit
Yes
Amazon EC2
ModifyTrafficMirrorSession
Edit
Yes
Amazon EC2
EnableSerialConsoleAccess
Enable
Yes
Amazon EC2
ResetInstanceAttribute
Edit
Yes
Amazon EC2
PurchaseReservedInstancesOffering
Purchase
Yes
Amazon EC2
DescribeBundleTasks
View
Yes
Amazon EC2
DescribeTransitGatewayConnects
View
Yes
Amazon EC2
DescribeAddresses
View
Yes
Amazon EC2
DeleteNetworkInterface
Delete
Yes
Amazon EC2
RejectVpcEndpointConnections
Reject
Yes
Amazon EC2
GetTransitGatewayMulticastDomainAssociations
View
Yes
Amazon EC2
DescribeTransitGatewayAttachments
View
Yes
Amazon EC2
CreateRestoreImageTask
Create
Yes
Amazon EC2
DescribeReservedInstances
View
Yes
Amazon EC2
GetPasswordData
View
Yes
Amazon EC2
DeleteTransitGatewayRoute
Delete
Yes
Amazon EC2
DisassociateVpcCidrBlock
Delete
Yes
Amazon EC2
ModifyTrafficMirrorFilterNetworkServices
Edit
Yes
Amazon EC2
CreateVpnGateway
Create
Yes
Amazon EC2
GetEbsDefaultKmsKeyId
View
Yes
Amazon EC2
DeprovisionByoipCidr
Create
Yes
Amazon EC2
DeleteVpnConnectionRoute
Delete
Yes
Amazon EC2
ResetNetworkInterfaceAttribute
Edit
Yes
Amazon EC2
DescribeInternetGateways
View
Yes
Amazon EC2
DescribeTransitGatewayMulticastDomains
View
Yes
Amazon EC2
DisableFastSnapshotRestores
Delete
Yes
Amazon EC2
DescribeClientVpnAuthorizationRules
View
Yes
Amazon EC2
DeleteSubnet
Delete
Yes
Amazon EC2
DeleteRoute
Delete
Yes
Amazon EC2
CreateManagedPrefixList
Create
Yes
Amazon EC2
GetTransitGatewayAttachmentPropagations
View
Yes
Amazon EC2
DescribeTransitGatewayRouteTables
View
Yes
Amazon EC2
CreateTrafficMirrorSession
Create
Yes
Amazon EC2
DescribeTrafficMirrorSessions
View
Yes
Amazon EC2
GetAssociatedIpvPoolCidrs
View
Yes
Amazon EC2
DescribeNatGateways
View
Yes
Amazon EC2
DescribeSpotFleetRequestHistory
View
Yes
Amazon EC2
DescribeVolumeStatus
View
Yes
Amazon EC2
DescribeInstanceStatus
View
Yes
Amazon EC2
DescribeLaunchTemplateVersions
View
Yes
Amazon EC2
DescribeLocalGatewayVirtualInterfaces
View
Yes
Amazon EC2
DisassociateTransitGatewayRouteTable
Delete
Yes
Amazon EC2
GetGroupsForCapacityReservation
View
Yes
Amazon EC2
DisableVgwRoutePropagation
Delete
Yes
Amazon EC2
DeleteNetworkInterfacePermission
Delete
Yes
Amazon EC2
DescribeSpotInstanceRequests
View
Yes
Amazon EC2
SendDiagnosticInterrupt
Send
Yes
Amazon EC2
CreateSnapshots
Create
Yes
Amazon EC2
ModifyVolumeAttribute
Edit
Yes
Amazon EC2
GetSerialConsoleAccessStatus
View
Yes
Amazon EC2
DescribeInstanceAttribute
View
Yes
Amazon EC2
ModifyVpcEndpointServicePermissions
Edit
Yes
Amazon EC2
AssociateAddress
Create
Yes
Amazon EC2
ImportKeyPair
Create
Yes
Amazon EC2
DeleteVpnGateway
Delete
Yes
Amazon EC2
DeleteTrafficMirrorTarget
Delete
Yes
Amazon EC2
DescribeExportImageTasks
View
Yes
Amazon EC2
DescribeRouteTables
View
Yes
Amazon EC2
DescribeDhcpOptions
View
Yes
Amazon EC2
CreatePlacementGroup
Create
Yes
Amazon EC2
DeleteKeyPair
Delete
Yes
Amazon EC2
DescribeClientVpnEndpoints
View
Yes
Amazon EC2
GetCoipPoolUsage
View
Yes
Amazon EC2
ModifyVpcAttribute
Edit
Yes
Amazon EC2
DeleteEgressOnlyInternetGateway
Delete
Yes
Amazon EC2
DeleteNetworkInsightsPath
Delete
Yes
Amazon EC2
DeleteTransitGatewayRouteTable
Delete
Yes
Amazon EC2
DescribeVpnGateways
View
Yes
Amazon EC2
DeleteTrafficMirrorFilter
Delete
Yes
Amazon EC2
DeleteNetworkAcl
Delete
Yes
Amazon EC2
TerminateClientVpnConnections
Terminate
Yes
Amazon EC2
DisableVpcClassicLinkDnsSupport
Delete
Yes
Amazon EC2
AssociateClientVpnTargetNetwork
Create
Yes
Amazon EC2
DescribeTags
View
Yes
Amazon EC2
DescribeKeyPairs
View
Yes
Amazon EC2
AssociateIamInstanceProfile
Create
Yes
Amazon EC2
AcceptVpcPeeringConnection
Approve
Yes
Amazon EC2
AuthorizeClientVpnIngress
Create
Yes
Amazon EC2
DisassociateAddress
Delete
Yes
Amazon EC2
DeregisterTransitGatewayMulticastGroupSources
Deregister
Yes
Amazon EC2
DescribeVpcEndpointServicePermissions
View
Yes
Amazon EC2
EnableVolumeIO
Enable
Yes
Amazon EC2
ModifyInstanceCreditSpecification
Edit
Yes
Amazon EC2
DescribeInstanceTypeOfferings
View
Yes
Amazon EC2
DeleteManagedPrefixList
Delete
Yes
Amazon EC2
AllocateAddress
Create
Yes
Amazon EC2
ModifyAvailabilityZoneGroup
Edit
Yes
Amazon EC2
DescribeLaunchTemplates
View
Yes
Amazon EC2
MonitorInstances
Create
Yes
Amazon EC2
CreateVpcEndpointConnectionNotification
Create
Yes
Amazon EC2
DeleteLocalGatewayRoute
Delete
Yes
Amazon EC2
SearchTransitGatewayRoutes
Search
Yes
Amazon EC2
DescribeVpcEndpoints
View
Yes
Amazon EC2
DescribeFleetInstances
View
Yes
Amazon EC2
ModifyIdFormat
Edit
Yes
Amazon EC2
ModifyInstanceAttribute
Edit
Yes
Amazon EC2
UpdateSecurityGroupRuleDescriptionsEgress
Edit
Yes
Amazon EC2
CreateTransitGatewayConnectPeer
Create
Yes
Amazon EC2
DescribeLocalGatewayRouteTableVpcAssociations
View
Yes
Amazon EC2
DescribeNetworkAcls
View
Yes
Amazon EC2
ModifySubnetAttribute
Edit
Yes
Amazon EC2
ModifyFleet
Edit
Yes
Amazon EC2
EnableTransitGatewayRouteTablePropagation
Enable
Yes
Amazon EC2
ModifyAddressAttribute
Edit
Yes
Amazon EC2
DescribeCarrierGateways
View
Yes
Amazon EC2
ResetEbsDefaultKmsKeyId
Edit
Yes
Amazon EC2
DeleteLaunchTemplateVersions
Delete
Yes
Amazon EC2
CreateInstanceExportTask
Create
Yes
Amazon EC2
DescribeFpgaImageAttribute
View
Yes
Amazon EC2
DeleteCustomerGateway
Delete
Yes
Amazon EC2
DeleteInternetGateway
Delete
Yes
Amazon EC2
DescribeCoipPools
View
Yes
Amazon EC2
PurchaseHostReservation
Purchase
Yes
Amazon EC2
DeleteCarrierGateway
Delete
Yes
Amazon EC2
EnableFastSnapshotRestores
Enable
Yes
Amazon EC2
GetAssociatedEnclaveCertificateIamRoles
View
Yes
Amazon EC2
DescribeManagedPrefixLists
View
Yes
Amazon EC2
DescribePrefixLists
View
Yes
Amazon EC2
DescribeIpvPools
View
Yes
Amazon EC2
ModifyFpgaImageAttribute
Edit
Yes
Amazon EC2
ModifyEbsDefaultKmsKeyId
Edit
Yes
Amazon EC2
CreateCapacityReservation
Create
Yes
Amazon EC2
DeleteTransitGatewayVpcAttachment
Delete
Yes
Amazon EC2
DescribeReservedInstancesOfferings
View
Yes
Amazon EC2
DescribeClientVpnTargetNetworks
View
Yes
Amazon EC2
CopyImage
Copy
Yes
Amazon EC2
RejectTransitGatewayPeeringAttachment
Reject
Yes
Amazon EC2
DeleteVpcEndpoints
Delete
Yes
Amazon EC2
DeleteVolume
Delete
Yes
Amazon EC2
CreateDefaultVpc
Create
Yes
Amazon EC2
DisassociateRouteTable
Delete
Yes
Amazon EC2
ModifyInstancePlacement
Edit
Yes
Amazon EC2
ModifyReservedInstances
Edit
Yes
Amazon EC2
DescribeReservedInstancesModifications
View
Yes
Amazon EC2
DescribeClientVpnRoutes
View
Yes
Amazon EC2
ResetSnapshotAttribute
Edit
Yes
Amazon EC2
BundleInstance
Create
Yes
Amazon EC2
DescribeIamInstanceProfileAssociations
View
Yes
Amazon EC2
DeregisterTransitGatewayMulticastGroupMembers
Deregister
Yes
Amazon EC2
AcceptTransitGatewayMulticastDomainAssociations
Approve
Yes
Amazon EC2
DeleteVpcPeeringConnection
Delete
Yes
Amazon EC2
DeleteSnapshot
Delete
Yes
Amazon EC2
ModifyVolume
Edit
Yes
Amazon EC2
ModifyTransitGatewayPrefixListReference
Edit
Yes
Amazon EC2
AuthorizeSecurityGroupIngress
Create
Yes
Amazon EC2
CreateTrafficMirrorFilter
Create
Yes
Amazon EC2
ModifyInstanceCapacityReservationAttributes
Edit
Yes
Amazon EC2
DetachNetworkInterface
Delete
Yes
Amazon EC2
ExportClientVpnClientCertificateRevocationList
View
Yes
Amazon EC2
DeleteVpcEndpointConnectionNotifications
Delete
Yes
Amazon EC2
GetFlowLogsIntegrationTemplate
View
Yes
Amazon EC2
RegisterInstanceEventNotificationAttributes
Register
Yes
Amazon EC2
RebootInstances
Reboot
Yes
Amazon EC2
CancelBundleTask
Delete
Yes
Amazon EC2
CreateImage
Create
Yes
Amazon EC2
DescribeNetworkInterfaces
View
Yes
Amazon EC2
GetManagedPrefixListAssociations
View
Yes
Amazon EC2
RevokeSecurityGroupEgress
Delete
Yes
Amazon EC2
DescribeNetworkInterfacePermissions
View
Yes
Amazon EC2
CreateInternetGateway
Create
Yes
Amazon EC2
DescribeImages
View
Yes
Amazon EC2
CancelConversionTask
Delete
Yes
Amazon EC2
StartNetworkInsightsAnalysis
Start
Yes
Amazon EC2
CreateVpnConnectionRoute
Create
Yes
Amazon EC2
DescribeHostReservations
View
Yes
Amazon EC2
ProvisionByoipCidr
Create
Yes
Amazon EC2
DetachVpnGateway
Delete
Yes
Amazon EC2
DescribeTransitGateways
View
Yes
Amazon EC2
SearchLocalGatewayRoutes
Search
Yes
Amazon EC2
ReleaseHosts
Create
Yes
Amazon EC2
AttachVolume
Attach
Yes
Amazon EC2
DescribeTrafficMirrorFilters
View
Yes
Amazon EC2
CreateNetworkInsightsPath
Create
Yes
Amazon EC2
DisassociateTransitGatewayMulticastDomain
Delete
Yes
Amazon EC2
CreateFpgaImage
Create
Yes
Amazon EC2
DescribeRegions
View
Yes
Amazon EC2
EnableEbsEncryptionByDefault
Enable
Yes
Amazon EC2
AcceptVpcEndpointConnections
Approve
Yes
Amazon EC2
DeleteFpgaImage
Delete
Yes
Amazon EC2
DescribeByoipCidrs
View
Yes
Amazon EC2
GetEbsEncryptionByDefault
View
Yes
Amazon EC2
DescribeImportImageTasks
View
Yes
Amazon EC2
DescribeScheduledInstances
View
Yes
Amazon EC2
CreateTransitGatewayPeeringAttachment
Create
Yes
Amazon EC2
RegisterTransitGatewayMulticastGroupMembers
Register
Yes
Amazon EC2
ModifyTrafficMirrorFilterRule
Edit
Yes
Amazon EC2
ReplaceTransitGatewayRoute
Create
Yes
Amazon EC2
CreateFlowLogs
Create
Yes
Amazon EC2
ModifySnapshotAttribute
Edit
Yes
Amazon EC2
CreateSnapshot
Create
Yes
Amazon EC2
ExportTransitGatewayRoutes
View
Yes
Amazon EC2
DescribeHostReservationOfferings
View
Yes
Amazon EC2
AssociateDhcpOptions
Create
Yes
Amazon EC2
RequestSpotInstances
Create
Yes
Amazon EC2
DescribeNetworkInsightsAnalyses
View
Yes
Amazon EC2
DescribeReservedInstancesListings
View
Yes
Amazon EC2
CreateNetworkInterfacePermission
Create
Yes
Amazon EC2
ImportImage
Create
Yes
Amazon EC2
WithdrawByoipCidr
Create
Yes
Amazon EC2
DisassociateClientVpnTargetNetwork
Delete
Yes
Amazon EC2
DeleteTransitGatewayConnectPeer
Delete
Yes
Amazon EC2
AttachVpnGateway
Attach
Yes
Amazon EC2
AcceptTransitGatewayPeeringAttachment
Approve
Yes
Amazon EC2
CreateEgressOnlyInternetGateway
Create
Yes
Amazon EC2
ModifyImageAttribute
Edit
Yes
Amazon EC2
AssociateSubnetCidrBlock
Create
Yes
Amazon EC2
DeleteSecurityGroup
Delete
Yes
Amazon EC2
ModifyVpcTenancy
Edit
Yes
Amazon EC2
CreateDefaultSubnet
Create
Yes
Amazon EC2
DescribeReplaceRootVolumeTasks
View
Yes
Amazon EC2
DescribeLocalGatewayRouteTables
View
Yes
Amazon EC2
ReportInstanceStatus
Create
Yes
Amazon EC2
DetachInternetGateway
Delete
Yes
Amazon EC2
DescribeSubnets
View
Yes
Amazon EC2
CreateTransitGatewayMulticastDomain
Create
Yes
Amazon EC2
ReplaceNetworkAclEntry
Create
Yes
Amazon EC2
DeleteFleets
Delete
Yes
Amazon EC2
DisableSerialConsoleAccess
Delete
Yes
Amazon EC2
DescribeStaleSecurityGroups
View
Yes
Amazon EC2
RejectVpcPeeringConnection
Reject
Yes
Amazon EC2
DescribeVpcEndpointConnections
View
Yes
Amazon EC2
CancelReservedInstancesListing
Delete
Yes
Amazon EC2
AllocateHosts
Create
Yes
Amazon EC2
DisableTransitGatewayRouteTablePropagation
Delete
Yes
Amazon EC2
DescribeLocalGatewayVirtualInterfaceGroups
View
Yes
Amazon EC2
DetachClassicLinkVpc
Delete
Yes
Amazon EC2
EnableVgwRoutePropagation
Enable
Yes
Amazon EC2
CreateClientVpnRoute
Create
Yes
Amazon EC2
CreateSpotDatafeedSubscription
Create
Yes
Amazon EC2
ResetImageAttribute
Edit
Yes
Amazon EC2
AssociateVpcCidrBlock
Create
Yes
Amazon EC2
GetConsoleOutput
View
Yes
Amazon EC2
AcceptTransitGatewayVpcAttachment
Approve
Yes
Amazon EC2
DeleteTransitGatewayConnect
Delete
Yes
Amazon EC2
DescribeVpcPeeringConnections
View
Yes
Amazon EC2
RunScheduledInstances
Create
Yes
Amazon EC2
AssociateTransitGatewayRouteTable
Create
Yes
Amazon EC2
DescribePlacementGroups
View
Yes
Amazon EC2
RestoreManagedPrefixListVersion
Create
Yes
Amazon EC2
StartInstances
Start
Yes
Amazon EC2
DescribeSnapshotAttribute
View
Yes
Amazon EC2
ImportVolume
Create
Yes
Amazon EC2
ModifyDefaultCreditSpecification
Edit
Yes
Amazon EC2 Container Service
SubmitAttachmentStateChanges
Create
Yes
Amazon EC2 Container Service
DeleteCapacityProvider
Delete
Yes
Amazon EC2 Container Service
CreateService
Create
Yes
Amazon EC2 Container Service
PutAccountSetting
Edit
Yes
Amazon EC2 Container Service
RegisterContainerInstance
Register
Yes
Amazon EC2 Container Service
TagResource
Create
Yes
Amazon EC2 Container Service
ListAccountSettings
View
Yes
Amazon EC2 Container Service
DeleteCluster
Delete
Yes
Amazon EC2 Container Service
PutAttributes
Edit
Yes
Amazon EC2 Container Service
ListAttributes
View
Yes
Amazon EC2 Container Service
DescribeServices
View
Yes
Amazon EC2 Container Service
DescribeClusters
View
Yes
Amazon EC2 Container Service
StartTask
Start
Yes
Amazon EC2 Container Service
DescribeTaskDefinition
View
Yes
Amazon EC2 Container Service
DescribeTasks
View
Yes
Amazon EC2 Container Service
DeregisterTaskDefinition
Deregister
Yes
Amazon EC2 Container Service
RegisterTaskDefinition
Register
Yes
Amazon EC2 Container Service
CreateTaskSet
Create
Yes
Amazon EC2 Container Service
UpdateClusterSettings
Edit
Yes
Amazon EC2 Container Service
UpdateTaskSet
Edit
Yes
Amazon EC2 Container Service
UpdateCapacityProvider
Edit
Yes
Amazon EC2 Container Service
ListTasks
View
Yes
Amazon EC2 Container Service
PutAccountSettingDefault
Edit
Yes
Amazon EC2 Container Service
UpdateService
Edit
Yes
Amazon EC2 Container Service
DescribeContainerInstances
View
Yes
Amazon EC2 Container Service
DeleteService
Delete
Yes
Amazon EC2 Container Service
DeregisterContainerInstance
Deregister
Yes
Amazon EC2 Container Service
PutClusterCapacityProviders
Edit
Yes
Amazon EC2 Container Service
ListTagsForResource
View
Yes
Amazon EC2 Container Service
DescribeTaskSets
View
Yes
Amazon EC2 Container Service
SubmitContainerStateChange
Create
Yes
Amazon EC2 Container Service
ListClusters
View
Yes
Amazon EC2 Container Service
StopTask
Stop
Yes
Amazon EC2 Container Service
DeleteAccountSetting
Delete
Yes
Amazon EC2 Container Service
DiscoverPollEndpoint
Create
Yes
Amazon EC2 Container Service
UntagResource
Delete
Yes
Amazon EC2 Container Service
UpdateCluster
Edit
Yes
Amazon EC2 Container Service
UpdateContainerInstancesState
Edit
Yes
Amazon EC2 Container Service
SubmitTaskStateChange
Create
Yes
Amazon EC2 Container Service
UpdateContainerAgent
Edit
Yes
Amazon EC2 Container Service
RunTask
Create
Yes
Amazon EC2 Container Service
ListTaskDefinitionFamilies
View
Yes
Amazon EC2 Container Service
CreateCluster
Create
Yes
Amazon EC2 Container Service
CreateCapacityProvider
Create
Yes
Amazon EC2 Container Service
ExecuteCommand
Create
Yes
Amazon EC2 Container Service
ListServices
View
Yes
Amazon EC2 Container Service
UpdateServicePrimaryTaskSet
Edit
Yes
Amazon EC2 Container Service
DeleteTaskSet
Delete
Yes
Amazon EC2 Container Service
DescribeCapacityProviders
View
Yes
Amazon EC2 Container Service
ListTaskDefinitions
View
Yes
Amazon EC2 Container Service
ListContainerInstances
View
Yes
Amazon EC2 Container Service
DeleteAttributes
Delete
Yes
Amazon EKS
DescribeCluster
View
Yes
Amazon EKS
DeleteCluster
Delete
Yes
Amazon EKS
DescribeIdentityProviderConfig
View
Yes
Amazon EKS
DisassociateIdentityProviderConfig
Delete
Yes
Amazon EKS
DescribeAddonVersions
View
Yes
Amazon EKS
UpdateClusterVersion
Edit
Yes
Amazon EKS
ListUpdates
View
Yes
Amazon EKS
AssociateEncryptionConfig
Create
Yes
Amazon EKS
CreateAddon
Create
Yes
Amazon EKS
ListAddons
View
Yes
Amazon EKS
DescribeAddon
View
Yes
Amazon EKS
DeleteAddon
Delete
Yes
Amazon EKS
UpdateClusterConfig
Edit
Yes
Amazon EKS
DescribeUpdate
View
Yes
Amazon EKS
CreateFargateProfile
Create
Yes
Amazon EKS
ListFargateProfiles
View
Yes
Amazon EKS
UpdateNodegroupVersion
Edit
Yes
Amazon EKS
DescribeFargateProfile
View
Yes
Amazon EKS
DeleteFargateProfile
Delete
Yes
Amazon EKS
DescribeNodegroup
View
Yes
Amazon EKS
DeleteNodegroup
Delete
Yes
Amazon EKS
AssociateIdentityProviderConfig
Create
Yes
Amazon EKS
UpdateNodegroupConfig
Edit
Yes
Amazon EKS
UntagResource
Delete
Yes
Amazon EKS
TagResource
Create
Yes
Amazon EKS
ListTagsForResource
View
Yes
Amazon EKS
ListIdentityProviderConfigs
View
Yes
Amazon EKS
UpdateAddon
Edit
Yes
Amazon EKS
CreateNodegroup
Create
Yes
Amazon EKS
ListNodegroups
View
Yes
Amazon EKS
CreateCluster
Create
Yes
Amazon EKS
ListClusters
View
Yes
Amazon Elastic Beanstalk
DescribeEnvironments
View
API Only
Amazon Elastic Beanstalk
CreatePlatformVersion
Create
API Only
Amazon Elastic Beanstalk
RetrieveEnvironmentInfo
View
API Only
Amazon Elastic Beanstalk
DescribeConfigurationSettings
View
API Only
Amazon Elastic Beanstalk
CreateEnvironment
Create
API Only
Amazon Elastic Beanstalk
ApplyEnvironmentManagedAction
Edit
API Only
Amazon Elastic Beanstalk
ListTagsForResource
View
API Only
Amazon Elastic Beanstalk
AbortEnvironmentUpdate
Create
API Only
Amazon Elastic Beanstalk
DescribeEnvironmentManagedActionHistory
View
API Only
Amazon Elastic Beanstalk
UpdateEnvironment
Edit
API Only
Amazon Elastic Beanstalk
UpdateApplication
Edit
API Only
Amazon Elastic Beanstalk
CreateStorageLocation
Create
API Only
Amazon Elastic Beanstalk
ListPlatformBranches
View
API Only
Amazon Elastic Beanstalk
DeleteApplicationVersion
Delete
API Only
Amazon Elastic Beanstalk
DescribeConfigurationOptions
View
API Only
Amazon Elastic Beanstalk
DescribeInstancesHealth
View
API Only
Amazon Elastic Beanstalk
DescribeEnvironmentManagedActions
View
API Only
Amazon Elastic Beanstalk
DeleteConfigurationTemplate
Delete
API Only
Amazon Elastic Beanstalk
ListAvailableSolutionStacks
View
API Only
Amazon Elastic Beanstalk
DescribeEnvironmentHealth
View
API Only
Amazon Elastic Beanstalk
UpdateApplicationResourceLifecycle
Edit
API Only
Amazon Elastic Beanstalk
UpdateApplicationVersion
Edit
API Only
Amazon Elastic Beanstalk
CreateApplication
Create
API Only
Amazon Elastic Beanstalk
ListPlatformVersions
View
API Only
Amazon Elastic Beanstalk
UpdateTagsForResource
Edit
API Only
Amazon Elastic Beanstalk
DeletePlatformVersion
Delete
API Only
Amazon Elastic Beanstalk
RestartAppServer
Reboot
API Only
Amazon Elastic Beanstalk
DescribeEvents
View
API Only
Amazon Elastic Beanstalk
SwapEnvironmentCNAMEs
Create
API Only
Amazon Elastic Beanstalk
AssociateEnvironmentOperationsRole
Create
API Only
Amazon Elastic Beanstalk
DescribeAccountAttributes
View
API Only
Amazon Elastic Beanstalk
CreateApplicationVersion
Create
API Only
Amazon Elastic Beanstalk
DeleteApplication
Delete
API Only
Amazon Elastic Beanstalk
UpdateConfigurationTemplate
Edit
API Only
Amazon Elastic Beanstalk
ValidateConfigurationSettings
Create
API Only
Amazon Elastic Beanstalk
RequestEnvironmentInfo
Create
API Only
Amazon Elastic Beanstalk
DescribeApplicationVersions
View
API Only
Amazon Elastic Beanstalk
DescribeEnvironmentResources
View
API Only
Amazon Elastic Beanstalk
DescribeApplications
View
API Only
Amazon Elastic Beanstalk
TerminateEnvironment
Terminate
API Only
Amazon Elastic Beanstalk
DescribePlatformVersion
View
API Only
Amazon Elastic Beanstalk
CreateConfigurationTemplate
Create
API Only
Amazon Elastic Beanstalk
DisassociateEnvironmentOperationsRole
Delete
API Only
Amazon Elastic Beanstalk
CheckDNSAvailability
Create
API Only
Amazon Elastic Beanstalk
ComposeEnvironments
Create
API Only
Amazon Elastic Beanstalk
RebuildEnvironment
Create
API Only
Amazon Elastic Beanstalk
DeleteEnvironmentConfiguration
Delete
API Only
Amazon Elastic Container Registry
Create
CompleteLayerUpload
Yes
Amazon Elastic Container Registry
View
GetRepositoryCatalogData
Yes
Amazon Elastic Container Registry
View
GetAuthorizationToken
Yes
Amazon Elastic Container Registry
View
DescribeImageTags
Yes
Amazon Elastic Container Registry
Create
CheckLayerAvailability
Yes
Amazon Elastic Container Registry
Create
SetRepositoryPolicy
Yes
Amazon Elastic Container Registry
View
DescribeImages
Yes
Amazon Elastic Container Registry
Delete
DeleteRepositoryPolicy
Yes
Amazon Elastic Container Registry
View
GetRegistryCatalogData
Yes
Amazon Elastic Container Registry
Edit
PutRegistryCatalogData
Yes
Amazon Elastic Container Registry
Edit
PutRepositoryCatalogData
Yes
Amazon Elastic Container Registry
Upload
UploadLayerPart
Yes
Amazon Elastic Container Registry
View
DescribeRepositories
Yes
Amazon Elastic Container Registry
Delete
DeleteImage
Yes
Amazon Elastic Container Registry
Create
InitiateLayerUpload
Yes
Amazon Elastic Container Registry
Delete
DeleteRepository
Yes
Amazon Elastic Container Registry
Create
CreateRepository
Yes
Amazon Elastic Container Registry
Edit
PutImage
Yes
Amazon Elastic Container Registry
View
DescribeRegistries
Yes
Amazon Elastic Container Registry
View
GetRepositoryPolicy
Yes
Amazon Elastic Container Registry
CreateTags
Create
Yes
Amazon Elastic File System
CreateAccessPoint
Create
API Only
Amazon Elastic File System
DescribeAccessPoints
View
API Only
Amazon Elastic File System
CreateFileSystem
Create
API Only
Amazon Elastic File System
DescribeFileSystems
View
API Only
Amazon Elastic File System
CreateMountTarget
Create
API Only
Amazon Elastic File System
DescribeMountTargets
View
API Only
Amazon Elastic File System
DeleteMountTarget
Delete
API Only
Amazon Elastic File System
UpdateFileSystem
Edit
API Only
Amazon Elastic File System
DeleteFileSystem
Delete
API Only
Amazon Elastic File System
DeleteAccessPoint
Delete
API Only
Amazon Elastic File System
ModifyMountTargetSecurityGroups
Edit
API Only
Amazon Elastic File System
DescribeMountTargetSecurityGroups
View
API Only
Amazon Elastic File System
DeleteTags
Delete
API Only
Amazon Elastic File System
PutLifecycleConfiguration
Edit
API Only
Amazon Elastic File System
DescribeLifecycleConfiguration
View
API Only
Amazon Elastic File System
DescribeTags
View
API Only
Amazon Elastic File System
PutBackupPolicy
Edit
API Only
Amazon Elastic File System
DescribeBackupPolicy
View
API Only
Amazon Elastic File System
UntagResource
Delete
API Only
Amazon Elastic File System
PutFileSystemPolicy
Edit
API Only
Amazon Elastic File System
DescribeFileSystemPolicy
View
API Only
Amazon Elastic File System
DeleteFileSystemPolicy
Delete
API Only
Amazon Elastic File System
TagResource
Create
API Only
Amazon Elastic File System
ListTagsForResource
View
API Only
Amazon Elastic Load Balancing
DeleteListener
Delete
Yes
Amazon Elastic Load Balancing
CreateTargetGroup
Create
Yes
Amazon Elastic Load Balancing
ModifyLoadBalancerAttributes
Edit
Yes
Amazon Elastic Load Balancing
DescribeListenerCertificates
View
Yes
Amazon Elastic Load Balancing
DescribeRules
View
Yes
Amazon Elastic Load Balancing
ModifyTargetGroup
Edit
Yes
Amazon Elastic Load Balancing
SetSubnets
Create
Yes
Amazon Elastic Load Balancing
DescribeTargetHealth
View
Yes
Amazon Elastic Load Balancing
DescribeTags
View
Yes
Amazon Elastic Load Balancing
DeleteTargetGroup
Delete
Yes
Amazon Elastic Load Balancing
DescribeAccountLimits
View
Yes
Amazon Elastic Load Balancing
ModifyTargetGroupAttributes
Edit
Yes
Amazon Elastic Load Balancing
ModifyRule
Edit
Yes
Amazon Elastic Load Balancing
RemoveTags
Delete
Yes
Amazon Elastic Load Balancing
SetRulePriorities
Create
Yes
Amazon Elastic Load Balancing
DeleteRule
Delete
Yes
Amazon Elastic Load Balancing
CreateListener
Create
Yes
Amazon Elastic Load Balancing
ModifyListener
Edit
Yes
Amazon Elastic Load Balancing
DescribeSSLPolicies
View
Yes
Amazon Elastic Load Balancing
DeregisterTargets
Deregister
Yes
Amazon Elastic Load Balancing
DescribeTargetGroupAttributes
View
Yes
Amazon Elastic Load Balancing
CreateLoadBalancer
Create
Yes
Amazon Elastic Load Balancing
CreateRule
Create
Yes
Amazon Elastic Load Balancing
SetIpAddressType
Create
Yes
Amazon Elastic Load Balancing
DescribeListeners
View
Yes
Amazon Elastic Load Balancing
DescribeLoadBalancers
View
Yes
Amazon Elastic Load Balancing
SetSecurityGroups
Create
Yes
Amazon Elastic Load Balancing
DescribeLoadBalancerAttributes
View
Yes
Amazon Elastic Load Balancing
AddTags
Create
Yes
Amazon Elastic Load Balancing
AddListenerCertificates
Create
Yes
Amazon Elastic Load Balancing
DescribeTargetGroups
View
Yes
Amazon Elastic Load Balancing
RegisterTargets
Register
Yes
Amazon Elastic Load Balancing
RemoveListenerCertificates
Delete
Yes
Amazon Elastic Load Balancing
DeleteLoadBalancer
Delete
Yes
Amazon ElastiCache
DeleteReplicationGroup
Delete
Yes
Amazon ElastiCache
DecreaseReplicaCount
Edit
Yes
Amazon ElastiCache
DescribeGlobalReplicationGroups
View
Yes
Amazon ElastiCache
CreateUserGroup
Create
Yes
Amazon ElastiCache
CreateCacheSubnetGroup
Create
Yes
Amazon ElastiCache
IncreaseReplicaCount
Edit
Yes
Amazon ElastiCache
DeleteCacheCluster
Delete
Yes
Amazon ElastiCache
DeleteGlobalReplicationGroup
Delete
Yes
Amazon ElastiCache
ListTagsForResource
View
Yes
Amazon ElastiCache
DescribeReservedCacheNodesOfferings
View
Yes
Amazon ElastiCache
RebalanceSlotsInGlobalReplicationGroup
Create
Yes
Amazon ElastiCache
DescribeUserGroups
View
Yes
Amazon ElastiCache
DescribeSnapshots
View
Yes
Amazon ElastiCache
ListAllowedNodeTypeModifications
View
Yes
Amazon ElastiCache
DescribeEngineDefaultParameters
View
Yes
Amazon ElastiCache
CreateCacheCluster
Create
Yes
Amazon ElastiCache
ResetCacheParameterGroup
Edit
Yes
Amazon ElastiCache
DescribeCacheParameterGroups
View
Yes
Amazon ElastiCache
CreateSnapshot
Create
Yes
Amazon ElastiCache
ModifyCacheParameterGroup
Edit
Yes
Amazon ElastiCache
CreateReplicationGroup
Create
Yes
Amazon ElastiCache
DeleteSnapshot
Delete
Yes
Amazon ElastiCache
CreateUser
Create
Yes
Amazon ElastiCache
FailoverGlobalReplicationGroup
Create
Yes
Amazon ElastiCache
CopySnapshot
Copy
Yes
Amazon ElastiCache
ModifyCacheCluster
Edit
Yes
Amazon ElastiCache
ModifyUser
Edit
Yes
Amazon ElastiCache
DeleteCacheSecurityGroup
Delete
Yes
Amazon ElastiCache
DescribeCacheEngineVersions
View
Yes
Amazon ElastiCache
DecreaseNodeGroupsInGlobalReplicationGroup
Edit
Yes
Amazon ElastiCache
RevokeCacheSecurityGroupIngress
Delete
Yes
Amazon ElastiCache
CreateGlobalReplicationGroup
Create
Yes
Amazon ElastiCache
StartMigration
Start
Yes
Amazon ElastiCache
ModifyReplicationGroup
Edit
Yes
Amazon ElastiCache
DescribeUsers
View
Yes
Amazon ElastiCache
StopUpdateAction
Stop
Yes
Amazon ElastiCache
DescribeUpdateActions
View
Yes
Amazon ElastiCache
DisassociateGlobalReplicationGroup
Delete
Yes
Amazon ElastiCache
DeleteUserGroup
Delete
Yes
Amazon ElastiCache
DescribeCacheParameters
View
Yes
Amazon ElastiCache
RebootCacheCluster
Reboot
Yes
Amazon ElastiCache
AuthorizeCacheSecurityGroupIngress
Create
Yes
Amazon ElastiCache
PurchaseReservedCacheNodesOffering
Purchase
Yes
Amazon ElastiCache
DeleteCacheParameterGroup
Delete
Yes
Amazon ElastiCache
ModifyUserGroup
Edit
Yes
Amazon ElastiCache
DescribeCacheSubnetGroups
View
Yes
Amazon ElastiCache
ModifyReplicationGroupShardConfiguration
Edit
Yes
Amazon ElastiCache
DeleteCacheSubnetGroup
Delete
Yes
Amazon ElastiCache
IncreaseNodeGroupsInGlobalReplicationGroup
Edit
Yes
Amazon ElastiCache
DescribeServiceUpdates
View
Yes
Amazon ElastiCache
CreateCacheParameterGroup
Create
Yes
Amazon ElastiCache
ModifyCacheSubnetGroup
Edit
Yes
Amazon ElastiCache
RemoveTagsFromResource
Delete
Yes
Amazon ElastiCache
AddTagsToResource
Create
Yes
Amazon ElastiCache
TestFailover
Create
Yes
Amazon ElastiCache
DescribeEvents
View
Yes
Amazon ElastiCache
DescribeCacheClusters
View
Yes
Amazon ElastiCache
DeleteUser
Delete
Yes
Amazon ElastiCache
DescribeCacheSecurityGroups
View
Yes
Amazon ElastiCache
DescribeReservedCacheNodes
View
Yes
Amazon ElastiCache
CompleteMigration
Create
Yes
Amazon ElastiCache
ApplyUpdateAction
Edit
Yes
Amazon ElastiCache
ModifyGlobalReplicationGroup
Edit
Yes
Amazon ElastiCache
CreateCacheSecurityGroup
Create
Yes
Amazon ElastiCache
DescribeReplicationGroups
View
Yes
Amazon Elasticsearch Service
CreateElasticsearchDomain
Create
Yes
Amazon Elasticsearch Service
AssociatePackage
Create
Yes
Amazon Elasticsearch Service
AcceptInboundCrossClusterSearchConnection
Approve
Yes
Amazon Elasticsearch Service
StartElasticsearchServiceSoftwareUpdate
Start
Yes
Amazon Elasticsearch Service
UpgradeElasticsearchDomain
Create
Yes
Amazon Elasticsearch Service
CreatePackage
Create
Yes
Amazon Elasticsearch Service
DescribeReservedElasticsearchInstanceOfferings
View
Yes
Amazon Elasticsearch Service
DeleteInboundCrossClusterSearchConnection
Delete
Yes
Amazon Elasticsearch Service
ListPackagesForDomain
View
Yes
Amazon Elasticsearch Service
DescribeElasticsearchDomain
View
Yes
Amazon Elasticsearch Service
DeleteElasticsearchDomain
Delete
Yes
Amazon Elasticsearch Service
CreateOutboundCrossClusterSearchConnection
Create
Yes
Amazon Elasticsearch Service
DescribePackages
View
Yes
Amazon Elasticsearch Service
AddTags
Create
Yes
Amazon Elasticsearch Service
UpdatePackage
Edit
Yes
Amazon Elasticsearch Service
DescribeInboundCrossClusterSearchConnections
View
Yes
Amazon Elasticsearch Service
DeleteOutboundCrossClusterSearchConnection
Delete
Yes
Amazon Elasticsearch Service
GetUpgradeHistory
View
Yes
Amazon Elasticsearch Service
DescribeDomainAutoTunes
View
Yes
Amazon Elasticsearch Service
ListElasticsearchVersions
View
Yes
Amazon Elasticsearch Service
ListElasticsearchInstanceTypes
View
Yes
Amazon Elasticsearch Service
DissociatePackage
Create
Yes
Amazon Elasticsearch Service
ListDomainNames
View
Yes
Amazon Elasticsearch Service
GetCompatibleElasticsearchVersions
View
Yes
Amazon Elasticsearch Service
DeleteElasticsearchServiceRole
Delete
Yes
Amazon Elasticsearch Service
DescribeReservedElasticsearchInstances
View
Yes
Amazon Elasticsearch Service
UpdateElasticsearchDomainConfig
Edit
Yes
Amazon Elasticsearch Service
DescribeElasticsearchDomainConfig
View
Yes
Amazon Elasticsearch Service
DescribeElasticsearchInstanceTypeLimits
View
Yes
Amazon Elasticsearch Service
GetPackageVersionHistory
View
Yes
Amazon Elasticsearch Service
CancelElasticsearchServiceSoftwareUpdate
Delete
Yes
Amazon Elasticsearch Service
ListTags
View
Yes
Amazon Elasticsearch Service
PurchaseReservedElasticsearchInstanceOffering
Purchase
Yes
Amazon Elasticsearch Service
DescribeOutboundCrossClusterSearchConnections
View
Yes
Amazon Elasticsearch Service
RejectInboundCrossClusterSearchConnection
Reject
Yes
Amazon Elasticsearch Service
DeletePackage
Delete
Yes
Amazon Elasticsearch Service
DescribeElasticsearchDomains
View
Yes
Amazon Elasticsearch Service
ListDomainsForPackage
View
Yes
Amazon Elasticsearch Service
RemoveTags
Delete
Yes
Amazon Elasticsearch Service
GetUpgradeStatus
View
Yes
Amazon Glacier
InitiateVaultLock
Create
Yes
Amazon Glacier
GetVaultLock
View
Yes
Amazon Glacier
AbortVaultLock
Delete
Yes
Amazon Glacier
SetDataRetrievalPolicy
Create
Yes
Amazon Glacier
GetDataRetrievalPolicy
View
Yes
Amazon Glacier
ListVaults
View
Yes
Amazon Glacier
InitiateMultipartUpload
Create
Yes
Amazon Glacier
ListMultipartUploads
View
Yes
Amazon Glacier
CompleteVaultLock
Create
Yes
Amazon Glacier
RemoveTagsFromVault
Delete
Yes
Amazon Glacier
UploadMultipartPart
Upload
Yes
Amazon Glacier
CompleteMultipartUpload
Create
Yes
Amazon Glacier
ListParts
View
Yes
Amazon Glacier
AbortMultipartUpload
Delete
Yes
Amazon Glacier
UploadArchive
Upload
Yes
Amazon Glacier
CreateVault
Create
Yes
Amazon Glacier
DescribeVault
View
Yes
Amazon Glacier
DeleteVault
Delete
Yes
Amazon Glacier
ListTagsForVault
View
Yes
Amazon Glacier
AddTagsToVault
Create
Yes
Amazon Glacier
SetVaultAccessPolicy
Create
Yes
Amazon Glacier
GetVaultAccessPolicy
View
Yes
Amazon Glacier
DeleteVaultAccessPolicy
Delete
Yes
Amazon Glacier
PurchaseProvisionedCapacity
Purchase
Yes
Amazon Glacier
ListProvisionedCapacity
View
Yes
Amazon Glacier
DescribeJob
View
Yes
Amazon Glacier
GetJobOutput
View
Yes
Amazon Glacier
DeleteArchive
Delete
Yes
Amazon Glacier
SetVaultNotifications
Create
Yes
Amazon Glacier
GetVaultNotifications
View
Yes
Amazon Glacier
DeleteVaultNotifications
Delete
Yes
Amazon Glacier
InitiateJob
Create
Yes
Amazon Glacier
ListJobs
View
Yes
Amazon GuardDuty
ListOrganizationAdminAccounts
View
Yes
Amazon GuardDuty
DisableOrganizationAdminAccount
Delete
Yes
Amazon GuardDuty
CreateDetector
Create
Yes
Amazon GuardDuty
ListDetectors
View
Yes
Amazon GuardDuty
GetMembers
View
Yes
Amazon GuardDuty
DeleteInvitations
Delete
Yes
Amazon GuardDuty
CreatePublishingDestination
Create
Yes
Amazon GuardDuty
ListPublishingDestinations
View
Yes
Amazon GuardDuty
UnarchiveFindings
Create
Yes
Amazon GuardDuty
GetFindingsStatistics
View
Yes
Amazon GuardDuty
GetUsageStatistics
View
Yes
Amazon GuardDuty
DisassociateMembers
Delete
Yes
Amazon GuardDuty
UpdateThreatIntelSet
Edit
Yes
Amazon GuardDuty
GetThreatIntelSet
View
Yes
Amazon GuardDuty
DeleteThreatIntelSet
Delete
Yes
Amazon GuardDuty
CreateSampleFindings
Create
Yes
Amazon GuardDuty
DeclineInvitations
Create
Yes
Amazon GuardDuty
CreateThreatIntelSet
Create
Yes
Amazon GuardDuty
ListThreatIntelSets
View
Yes
Amazon GuardDuty
GetFindings
View
Yes
Amazon GuardDuty
ArchiveFindings
Create
Yes
Amazon GuardDuty
DisassociateFromMasterAccount
Delete
Yes
Amazon GuardDuty
UntagResource
Delete
Yes
Amazon GuardDuty
UpdatePublishingDestination
Edit
Yes
Amazon GuardDuty
DescribePublishingDestination
View
Yes
Amazon GuardDuty
DeletePublishingDestination
Delete
Yes
Amazon GuardDuty
UpdateMemberDetectors
Edit
Yes
Amazon GuardDuty
EnableOrganizationAdminAccount
Enable
Yes
Amazon GuardDuty
UpdateFindingsFeedback
Edit
Yes
Amazon GuardDuty
StopMonitoringMembers
Stop
Yes
Amazon GuardDuty
UpdateFilter
Edit
Yes
Amazon GuardDuty
GetFilter
View
Yes
Amazon GuardDuty
DeleteFilter
Delete
Yes
Amazon GuardDuty
ListFindings
View
Yes
Amazon GuardDuty
CreateFilter
Create
Yes
Amazon GuardDuty
ListFilters
View
Yes
Amazon GuardDuty
UpdateOrganizationConfiguration
Edit
Yes
Amazon GuardDuty
DescribeOrganizationConfiguration
View
Yes
Amazon GuardDuty
ListInvitations
View
Yes
Amazon GuardDuty
AcceptInvitation
Approve
Yes
Amazon GuardDuty
GetMasterAccount
View
Yes
Amazon GuardDuty
DeleteMembers
Delete
Yes
Amazon GuardDuty
GetInvitationsCount
View
Yes
Amazon GuardDuty
TagResource
Create
Yes
Amazon GuardDuty
ListTagsForResource
View
Yes
Amazon GuardDuty
CreateMembers
Create
Yes
Amazon GuardDuty
ListMembers
View
Yes
Amazon GuardDuty
UpdateDetector
Edit
Yes
Amazon GuardDuty
GetDetector
View
Yes
Amazon GuardDuty
DeleteDetector
Delete
Yes
Amazon GuardDuty
CreateIPSet
Create
Yes
Amazon GuardDuty
ListIPSets
View
Yes
Amazon GuardDuty
InviteMembers
Create
Yes
Amazon GuardDuty
StartMonitoringMembers
Start
Yes
Amazon GuardDuty
GetMemberDetectors
View
Yes
Amazon GuardDuty
UpdateIPSet
Edit
Yes
Amazon GuardDuty
GetIPSet
View
Yes
Amazon GuardDuty
DeleteIPSet
Delete
Yes
Amazon IAM
ListEntitiesForPolicy
View
Yes
Amazon IAM
GetPolicyVersion
View
Yes
Amazon IAM
ChangePassword
Create
Yes
Amazon IAM
ListRolePolicies
View
Yes
Amazon IAM
ListGroups
View
Yes
Amazon IAM
GetServiceLastAccessedDetails
View
Yes
Amazon IAM
GetOpenIDConnectProvider
View
Yes
Amazon IAM
GetCredentialReport
View
Yes
Amazon IAM
ListAttachedGroupPolicies
View
Yes
Amazon IAM
ListInstanceProfilesForRole
View
Yes
Amazon IAM
DeactivateMFADevice
Deactivate
Yes
Amazon IAM
TagPolicy
Create
Yes
Amazon IAM
SetSecurityTokenServicePreferences
Create
Yes
Amazon IAM
ListRoleTags
View
Yes
Amazon IAM
UpdateServerCertificate
Edit
Yes
Amazon IAM
DetachGroupPolicy
Delete
Yes
Amazon IAM
UntagMFADevice
Delete
Yes
Amazon IAM
ListMFADevices
View
Yes
Amazon IAM
DeleteServiceLinkedRole
Delete
Yes
Amazon IAM
ListSSHPublicKeys
View
Yes
Amazon IAM
ListUserTags
View
Yes
Amazon IAM
ListOpenIDConnectProviders
View
Yes
Amazon IAM
GetInstanceProfile
View
Yes
Amazon IAM
ListInstanceProfiles
View
Yes
Amazon IAM
DeletePolicy
Delete
Yes
Amazon IAM
ListUserPolicies
View
Yes
Amazon IAM
ListGroupsForUser
View
Yes
Amazon IAM
DeleteGroupPolicy
Delete
Yes
Amazon IAM
PutRolePermissionsBoundary
Edit
Yes
Amazon IAM
UpdateServiceSpecificCredential
Edit
Yes
Amazon IAM
RemoveUserFromGroup
Delete
Yes
Amazon IAM
DeleteGroup
Delete
Yes
Amazon IAM
GetAccountPasswordPolicy
View
Yes
Amazon IAM
CreatePolicyVersion
Create
Yes
Amazon IAM
PutUserPolicy
Edit
Yes
Amazon IAM
GetAccountSummary
View
Yes
Amazon IAM
SimulateCustomPolicy
Create
Yes
Amazon IAM
ListSAMLProviderTags
View
Yes
Amazon IAM
TagMFADevice
Create
Yes
Amazon IAM
AddUserToGroup
Create
Yes
Amazon IAM
GetSSHPublicKey
View
Yes
Amazon IAM
DeleteSigningCertificate
Delete
Yes
Amazon IAM
ListServiceSpecificCredentials
View
Yes
Amazon IAM
DeleteVirtualMFADevice
Delete
Yes
Amazon IAM
PutRolePolicy
Edit
Yes
Amazon IAM
ListAttachedRolePolicies
View
Yes
Amazon IAM
GetAccountAuthorizationDetails
View
Yes
Amazon IAM
DeleteLoginProfile
Delete
Yes
Amazon IAM
DetachUserPolicy
Delete
Yes
Amazon IAM
SimulatePrincipalPolicy
Create
Yes
Amazon IAM
RemoveClientIDFromOpenIDConnectProvider
Delete
Yes
Amazon IAM
UntagUser
Delete
Yes
Amazon IAM
UpdateRoleDescription
Edit
Yes
Amazon IAM
AttachGroupPolicy
Attach
Yes
Amazon IAM
GetServiceLinkedRoleDeletionStatus
View
Yes
Amazon IAM
ListPolicyVersions
View
Yes
Amazon IAM
AddRoleToInstanceProfile
Create
Yes
Amazon IAM
GetUserPolicy
View
Yes
Amazon IAM
GenerateServiceLastAccessedDetails
Create
Yes
Amazon IAM
GetRolePolicy
View
Yes
Amazon IAM
PutGroupPolicy
Edit
Yes
Amazon IAM
UpdateAccountPasswordPolicy
Edit
Yes
Amazon IAM
GetLoginProfile
View
Yes
Amazon IAM
ListInstanceProfileTags
View
Yes
Amazon IAM
DeleteServerCertificate
Delete
Yes
Amazon IAM
GenerateCredentialReport
Create
Yes
Amazon IAM
ListRoles
View
Yes
Amazon IAM
SetDefaultPolicyVersion
Create
Yes
Amazon IAM
CreateVirtualMFADevice
Create
Yes
Amazon IAM
ListPolicies
View
Yes
Amazon IAM
TagInstanceProfile
Create
Yes
Amazon IAM
DeleteUserPolicy
Delete
Yes
Amazon IAM
GetSAMLProvider
View
Yes
Amazon IAM
CreatePolicy
Create
Yes
Amazon IAM
UntagInstanceProfile
Delete
Yes
Amazon IAM
PutUserPermissionsBoundary
Edit
Yes
Amazon IAM
TagOpenIDConnectProvider
Create
Yes
Amazon IAM
DeleteUser
Delete
Yes
Amazon IAM
ListPoliciesGrantingServiceAccess
View
Yes
Amazon IAM
ResyncMFADevice
Create
Yes
Amazon IAM
TagRole
Create
Yes
Amazon IAM
CreateLoginProfile
Create
Yes
Amazon IAM
ListAttachedUserPolicies
View
Yes
Amazon IAM
UploadServerCertificate
Upload
Yes
Amazon IAM
UpdateRole
Edit
Yes
Amazon IAM
UntagRole
Delete
Yes
Amazon IAM
ListGroupPolicies
View
Yes
Amazon IAM
UpdateSSHPublicKey
Edit
Yes
Amazon IAM
UpdateSigningCertificate
Edit
Yes
Amazon IAM
GetContextKeysForPrincipalPolicy
View
Yes
Amazon IAM
TagServerCertificate
Create
Yes
Amazon IAM
CreateInstanceProfile
Create
Yes
Amazon IAM
DeleteInstanceProfile
Delete
Yes
Amazon IAM
AttachUserPolicy
Attach
Yes
Amazon IAM
CreateUser
Create
Yes
Amazon IAM
ListServerCertificateTags
View
Yes
Amazon IAM
CreateRole
Create
Yes
Amazon IAM
GetRole
View
Yes
Amazon IAM
ListAccountAliases
View
Yes
Amazon IAM
UntagSAMLProvider
Delete
Yes
Amazon IAM
UpdateUser
Edit
Yes
Amazon IAM
GetUser
View
Yes
Amazon IAM
UpdateGroup
Edit
Yes
Amazon IAM
TagUser
Create
Yes
Amazon IAM
CreateOpenIDConnectProvider
Create
Yes
Amazon IAM
DeleteOpenIDConnectProvider
Delete
Yes
Amazon IAM
ListOpenIDConnectProviderTags
View
Yes
Amazon IAM
ListPolicyTags
View
Yes
Amazon IAM
DeleteSAMLProvider
Delete
Yes
Amazon IAM
GetGroupPolicy
View
Yes
Amazon IAM
CreateAccessKey
Create
Yes
Amazon IAM
AddClientIDToOpenIDConnectProvider
Create
Yes
Amazon IAM
UpdateSAMLProvider
Edit
Yes
Amazon IAM
UntagServerCertificate
Delete
Yes
Amazon IAM
UpdateLoginProfile
Edit
Yes
Amazon IAM
GetPolicy
View
Yes
Amazon IAM
DeleteAccountAlias
Delete
Yes
Amazon IAM
DeleteAccessKey
Delete
Yes
Amazon IAM
CreateServiceLinkedRole
Create
Yes
Amazon IAM
CreateGroup
Create
Yes
Amazon IAM
UpdateAssumeRolePolicy
Edit
Yes
Amazon IAM
ListUsers
View
Yes
Amazon IAM
DetachRolePolicy
Delete
Yes
Amazon IAM
EnableMFADevice
Enable
Yes
Amazon IAM
UntagPolicy
Delete
Yes
Amazon IAM
CreateServiceSpecificCredential
Create
Yes
Amazon IAM
GetServerCertificate
View
Yes
Amazon IAM
DeleteRole
Delete
Yes
Amazon IAM
DeleteRolePolicy
Delete
Yes
Amazon IAM
TagSAMLProvider
Create
Yes
Amazon IAM
ListSAMLProviders
View
Yes
Amazon IAM
ListVirtualMFADevices
View
Yes
Amazon IAM
ListAccessKeys
View
Yes
Amazon IAM
GetServiceLastAccessedDetailsWithEntities
View
Yes
Amazon IAM
GetGroup
View
Yes
Amazon IAM
UpdateAccessKey
Edit
Yes
Amazon IAM
DeleteServiceSpecificCredential
Delete
Yes
Amazon IAM
CreateSAMLProvider
Create
Yes
Amazon IAM
DeleteRolePermissionsBoundary
Delete
Yes
Amazon IAM
AttachRolePolicy
Attach
Yes
Amazon IAM
GetContextKeysForCustomPolicy
View
Yes
Amazon IAM
UntagOpenIDConnectProvider
Delete
Yes
Amazon IAM
RemoveRoleFromInstanceProfile
Delete
Yes
Amazon IAM
GetAccessKeyLastUsed
View
Yes
Amazon IAM
GenerateOrganizationsAccessReport
Create
Yes
Amazon IAM
ListSigningCertificates
View
Yes
Amazon IAM
UploadSSHPublicKey
Upload
Yes
Amazon IAM
UploadSigningCertificate
Upload
Yes
Amazon IAM
DeleteUserPermissionsBoundary
Delete
Yes
Amazon IAM
DeleteAccountPasswordPolicy
Delete
Yes
Amazon IAM
ResetServiceSpecificCredential
Edit
Yes
Amazon IAM
ListMFADeviceTags
View
Yes
Amazon IAM
CreateAccountAlias
Create
Yes
Amazon IAM
DeletePolicyVersion
Delete
Yes
Amazon IAM
UpdateOpenIDConnectProviderThumbprint
Edit
Yes
Amazon IAM
DeleteSSHPublicKey
Delete
Yes
Amazon IAM
ListServerCertificates
View
Yes
Amazon IAM
GetOrganizationsAccessReport
View
Yes
Amazon KMS
PutKeyPolicy
Edit
Yes
Amazon KMS
ListAliases
View
Yes
Amazon KMS
DisconnectCustomKeyStore
Create
Yes
Amazon KMS
GenerateDataKeyPairWithoutPlaintext
Create
Yes
Amazon KMS
EnableKeyRotation
Enable
Yes
Amazon KMS
DescribeCustomKeyStores
View
Yes
Amazon KMS
UpdateAlias
Edit
Yes
Amazon KMS
TagResource
Create
Yes
Amazon KMS
DeleteAlias
Delete
Yes
Amazon KMS
ImportKeyMaterial
Create
Yes
Amazon KMS
ScheduleKeyDeletion
Create
Yes
Amazon KMS
CreateCustomKeyStore
Create
Yes
Amazon KMS
GenerateRandom
Create
Yes
Amazon KMS
UpdateCustomKeyStore
Edit
Yes
Amazon KMS
CreateKey
Create
Yes
Amazon KMS
EnableKey
Enable
Yes
Amazon KMS
DisableKeyRotation
Delete
Yes
Amazon KMS
GetPublicKey
View
Yes
Amazon KMS
RevokeGrant
Delete
Yes
Amazon KMS
GetKeyPolicy
View
Yes
Amazon KMS
ListRetirableGrants
View
Yes
Amazon KMS
DescribeKey
View
Yes
Amazon KMS
GenerateDataKeyPair
Create
Yes
Amazon KMS
GetKeyRotationStatus
View
Yes
Amazon KMS
Encrypt
Create
Yes
Amazon KMS
CancelKeyDeletion
Delete
Yes
Amazon KMS
Sign
Create
Yes
Amazon KMS
ListGrants
View
Yes
Amazon KMS
GetParametersForImport
View
Yes
Amazon KMS
ConnectCustomKeyStore
Create
Yes
Amazon KMS
CreateAlias
Create
Yes
Amazon KMS
ListKeys
View
Yes
Amazon KMS
DeleteCustomKeyStore
Delete
Yes
Amazon KMS
ListKeyPolicies
View
Yes
Amazon KMS
DeleteImportedKeyMaterial
Delete
Yes
Amazon KMS
CreateGrant
Create
Yes
Amazon KMS
GenerateDataKey
Create
Yes
Amazon KMS
RetireGrant
Create
Yes
Amazon KMS
UntagResource
Delete
Yes
Amazon KMS
Verify
Create
Yes
Amazon KMS
UpdateKeyDescription
Edit
Yes
Amazon KMS
DisableKey
Delete
Yes
Amazon KMS
ReEncrypt
Create
Yes
Amazon KMS
ListResourceTags
View
Yes
Amazon KMS
GenerateDataKeyWithoutPlaintext
Create
Yes
Amazon KMS
Decrypt
Create
Yes
Amazon Lambda
AddLayerVersionPermission
Create
Yes
Amazon Lambda
GetLayerVersionPolicy
View
Yes
Amazon Lambda
CreateEventSourceMapping
Create
Yes
Amazon Lambda
ListEventSourceMappings
View
Yes
Amazon Lambda
GetFunction
View
Yes
Amazon Lambda
DeleteFunction
Delete
Yes
Amazon Lambda
CreateFunction
Create
Yes
Amazon Lambda
ListProvisionedConcurrencyConfigs
View
Yes
Amazon Lambda
UpdateFunctionConfiguration
Edit
Yes
Amazon Lambda
GetFunctionConfiguration
View
Yes
Amazon Lambda
PutFunctionEventInvokeConfig
Edit
Yes
Amazon Lambda
UpdateFunctionEventInvokeConfig
Edit
Yes
Amazon Lambda
GetFunctionEventInvokeConfig
View
Yes
Amazon Lambda
DeleteFunctionEventInvokeConfig
Delete
Yes
Amazon Lambda
PutProvisionedConcurrencyConfig
Edit
Yes
Amazon Lambda
GetProvisionedConcurrencyConfig
View
Yes
Amazon Lambda
DeleteProvisionedConcurrencyConfig
Delete
Yes
Amazon Lambda
UpdateEventSourceMapping
Edit
Yes
Amazon Lambda
GetEventSourceMapping
View
Yes
Amazon Lambda
DeleteEventSourceMapping
Delete
Yes
Amazon Lambda
UpdateFunctionCode
Edit
Yes
Amazon Lambda
CreateCodeSigningConfig
Create
Yes
Amazon Lambda
ListCodeSigningConfigs
View
Yes
Amazon Lambda
GetLayerVersion
View
Yes
Amazon Lambda
DeleteLayerVersion
Delete
Yes
Amazon Lambda
TagResource
Create
Yes
Amazon Lambda
ListTags
View
Yes
Amazon Lambda
PutFunctionConcurrency
Edit
Yes
Amazon Lambda
DeleteFunctionConcurrency
Delete
Yes
Amazon Lambda
PublishLayerVersion
Create
Yes
Amazon Lambda
ListLayerVersions
View
Yes
Amazon Lambda
ListFunctionsByCodeSigningConfig
View
Yes
Amazon Lambda
PublishVersion
Create
Yes
Amazon Lambda
ListVersionsByFunction
View
Yes
Amazon Lambda
ListFunctionEventInvokeConfigs
View
Yes
Amazon Lambda
UpdateCodeSigningConfig
Edit
Yes
Amazon Lambda
GetCodeSigningConfig
View
Yes
Amazon Lambda
DeleteCodeSigningConfig
Delete
Yes
Amazon Lambda
ListFunctions
View
Yes
Amazon Lambda
PutFunctionCodeSigningConfig
Edit
Yes
Amazon Lambda
GetFunctionCodeSigningConfig
View
Yes
Amazon Lambda
DeleteFunctionCodeSigningConfig
Delete
Yes
Amazon Lambda
RemoveLayerVersionPermission
Delete
Yes
Amazon Lambda
InvokeAsync
Create
Yes
Amazon Lambda
CreateAlias
Create
Yes
Amazon Lambda
ListAliases
View
Yes
Amazon Lambda
Invoke
Create
Yes
Amazon Lambda
GetLayerVersionByArn
View
Yes
Amazon Lambda
AddPermission
Create
Yes
Amazon Lambda
GetPolicy
View
Yes
Amazon Lambda
GetFunctionConcurrency
View
Yes
Amazon Lambda
ListLayers
View
Yes
Amazon Lambda
RemovePermission
Delete
Yes
Amazon Lambda
UntagResource
Delete
Yes
Amazon Lambda
GetAccountSettings
View
Yes
Amazon Lambda
UpdateAlias
Edit
Yes
Amazon Lambda
GetAlias
View
Yes
Amazon Lambda
DeleteAlias
Delete
Yes
Amazon MQ
UpdateConfiguration
Edit
Yes
Amazon MQ
DescribeConfiguration
View
Yes
Amazon MQ
UpdateUser
Edit
Yes
Amazon MQ
CreateUser
Create
Yes
Amazon MQ
DescribeUser
View
Yes
Amazon MQ
DeleteUser
Delete
Yes
Amazon MQ
CreateConfiguration
Create
Yes
Amazon MQ
ListConfigurations
View
Yes
Amazon MQ
UpdateBroker
Edit
Yes
Amazon MQ
DescribeBroker
View
Yes
Amazon MQ
DeleteBroker
Delete
Yes
Amazon MQ
CreateBroker
Create
Yes
Amazon MQ
ListBrokers
View
Yes
Amazon MQ
RebootBroker
Reboot
Yes
Amazon MQ
ListConfigurationRevisions
View
Yes
Amazon MQ
DescribeConfigurationRevision
View
Yes
Amazon MQ
DescribeBrokerInstanceOptions
View
Yes
Amazon MQ
DeleteTags
Delete
Yes
Amazon MQ
DescribeBrokerEngineTypes
View
Yes
Amazon MQ
ListUsers
View
Yes
Amazon MQ
CreateTags
Create
Yes
Amazon MQ
ListTags
View
Yes
Amazon Organizations
DescribePolicy
View
Yes
Amazon Organizations
InviteAccountToOrganization
Create
Yes
Amazon Organizations
DeclineHandshake
Create
Yes
Amazon Organizations
DisablePolicyType
Delete
Yes
Amazon Organizations
DeregisterDelegatedAdministrator
Deregister
Yes
Amazon Organizations
TagResource
Create
Yes
Amazon Organizations
EnableAWSServiceAccess
Enable
Yes
Amazon Organizations
DescribeHandshake
View
Yes
Amazon Organizations
CreateOrganizationalUnit
Create
Yes
Amazon Organizations
AttachPolicy
Attach
Yes
Amazon Organizations
CreatePolicy
Create
Yes
Amazon Organizations
DisableAWSServiceAccess
Delete
Yes
Amazon Organizations
DescribeEffectivePolicy
View
Yes
Amazon Organizations
RemoveAccountFromOrganization
Delete
Yes
Amazon Organizations
ListAccountsForParent
View
Yes
Amazon Organizations
ListCreateAccountStatus
View
Yes
Amazon Organizations
ListChildren
View
Yes
Amazon Organizations
DeletePolicy
Delete
Yes
Amazon Organizations
AcceptHandshake
Approve
Yes
Amazon Organizations
CreateGovCloudAccount
Create
Yes
Amazon Organizations
UpdatePolicy
Edit
Yes
Amazon Organizations
DeleteOrganizationalUnit
Delete
Yes
Amazon Organizations
ListAWSServiceAccessForOrganization
View
Yes
Amazon Organizations
ListHandshakesForOrganization
View
Yes
Amazon Organizations
ListOrganizationalUnitsForParent
View
Yes
Amazon Organizations
ListPoliciesForTarget
View
Yes
Amazon Organizations
ListParents
View
Yes
Amazon Organizations
DescribeAccount
View
Yes
Amazon Organizations
ListHandshakesForAccount
View
Yes
Amazon Organizations
DescribeCreateAccountStatus
View
Yes
Amazon Organizations
ListTargetsForPolicy
View
Yes
Amazon Organizations
DescribeOrganization
View
Yes
Amazon Organizations
RegisterDelegatedAdministrator
Register
Yes
Amazon Organizations
LeaveOrganization
Create
Yes
Amazon Organizations
ListAccounts
View
Yes
Amazon Organizations
CreateOrganization
Create
Yes
Amazon Organizations
ListRoots
View
Yes
Amazon Organizations
DeleteOrganization
Delete
Yes
Amazon Organizations
EnableAllFeatures
Enable
Yes
Amazon Organizations
DetachPolicy
Delete
Yes
Amazon Organizations
DescribeOrganizationalUnit
View
Yes
Amazon Organizations
ListDelegatedServicesForAccount
View
Yes
Amazon Organizations
UpdateOrganizationalUnit
Edit
Yes
Amazon Organizations
ListPolicies
View
Yes
Amazon Organizations
MoveAccount
Move
Yes
Amazon Organizations
ListTagsForResource
View
Yes
Amazon Organizations
CancelHandshake
Delete
Yes
Amazon Organizations
CreateAccount
Create
Yes
Amazon Organizations
EnablePolicyType
Enable
Yes
Amazon Organizations
ListDelegatedAdministrators
View
Yes
Amazon Organizations
UntagResource
Delete
Yes
Amazon RDS
RebootDBInstance
Reboot
Yes
Amazon RDS
DescribeEngineDefaultClusterParameters
View
Yes
Amazon RDS
DeleteDBClusterParameterGroup
Delete
Yes
Amazon RDS
ListTagsForResource
View
Yes
Amazon RDS
ModifyOptionGroup
Edit
Yes
Amazon RDS
CopyDBClusterSnapshot
Copy
Yes
Amazon RDS
DescribeDBInstanceAutomatedBackups
View
Yes
Amazon RDS
CreateDBClusterSnapshot
Create
Yes
Amazon RDS
DescribeDBProxies
View
Yes
Amazon RDS
ModifyDBProxy
Edit
Yes
Amazon RDS
DeleteOptionGroup
Delete
Yes
Amazon RDS
DescribeDBClusterBacktracks
View
Yes
Amazon RDS
RestoreDBInstanceFromS
Create
Yes
Amazon RDS
CreateDBParameterGroup
Create
Yes
Amazon RDS
DeleteDBClusterSnapshot
Delete
Yes
Amazon RDS
DeleteGlobalCluster
Delete
Yes
Amazon RDS
AddRoleToDBCluster
Create
Yes
Amazon RDS
DeleteDBProxyEndpoint
Delete
Yes
Amazon RDS
StartDBCluster
Start
Yes
Amazon RDS
CreateDBSnapshot
Create
Yes
Amazon RDS
DescribeDBProxyTargets
View
Yes
Amazon RDS
StopActivityStream
Stop
Yes
Amazon RDS
RestoreDBInstanceToPointInTime
Create
Yes
Amazon RDS
CreateDBSubnetGroup
Create
Yes
Amazon RDS
CreateDBClusterEndpoint
Create
Yes
Amazon RDS
StartExportTask
Start
Yes
Amazon RDS
AuthorizeDBSecurityGroupIngress
Create
Yes
Amazon RDS
RemoveRoleFromDBInstance
Delete
Yes
Amazon RDS
StartDBInstanceAutomatedBackupsReplication
Start
Yes
Amazon RDS
ModifyDBSubnetGroup
Edit
Yes
Amazon RDS
AddSourceIdentifierToSubscription
Create
Yes
Amazon RDS
DescribeReservedDBInstances
View
Yes
Amazon RDS
CopyDBParameterGroup
Copy
Yes
Amazon RDS
DeleteCustomAvailabilityZone
Delete
Yes
Amazon RDS
DeleteDBCluster
Delete
Yes
Amazon RDS
DescribeDBSubnetGroups
View
Yes
Amazon RDS
DeleteDBSubnetGroup
Delete
Yes
Amazon RDS
DescribeDBClusters
View
Yes
Amazon RDS
DownloadDBLogFilePortion
Download
Yes
Amazon RDS
ApplyPendingMaintenanceAction
Edit
Yes
Amazon RDS
DescribeDBClusterParameters
View
Yes
Amazon RDS
ModifyDBInstance
Edit
Yes
Amazon RDS
DescribeDBSecurityGroups
View
Yes
Amazon RDS
DeleteEventSubscription
Delete
Yes
Amazon RDS
DescribeEventSubscriptions
View
Yes
Amazon RDS
PurchaseReservedDBInstancesOffering
Purchase
Yes
Amazon RDS
DescribeDBClusterEndpoints
View
Yes
Amazon RDS
DescribePendingMaintenanceActions
View
Yes
Amazon RDS
DeleteDBSecurityGroup
Delete
Yes
Amazon RDS
CreateDBProxyEndpoint
Create
Yes
Amazon RDS
ResetDBClusterParameterGroup
Edit
Yes
Amazon RDS
DescribeDBParameterGroups
View
Yes
Amazon RDS
StartDBInstance
Start
Yes
Amazon RDS
ImportInstallationMedia
Create
Yes
Amazon RDS
FailoverGlobalCluster
Create
Yes
Amazon RDS
DescribeAccountAttributes
View
Yes
Amazon RDS
DescribeDBEngineVersions
View
Yes
Amazon RDS
DescribeCertificates
View
Yes
Amazon RDS
FailoverDBCluster
Create
Yes
Amazon RDS
ModifyDBSnapshotAttribute
Edit
Yes
Amazon RDS
DescribeDBProxyEndpoints
View
Yes
Amazon RDS
CopyDBClusterParameterGroup
Copy
Yes
Amazon RDS
RevokeDBSecurityGroupIngress
Delete
Yes
Amazon RDS
RestoreDBInstanceFromDBSnapshot
Create
Yes
Amazon RDS
ModifyDBParameterGroup
Edit
Yes
Amazon RDS
DeleteDBSnapshot
Delete
Yes
Amazon RDS
DeleteDBParameterGroup
Delete
Yes
Amazon RDS
CreateDBInstance
Create
Yes
Amazon RDS
StopDBInstanceAutomatedBackupsReplication
Stop
Yes
Amazon RDS
RemoveFromGlobalCluster
Delete
Yes
Amazon RDS
StopDBInstance
Stop
Yes
Amazon RDS
DescribeDBParameters
View
Yes
Amazon RDS
DescribeDBSnapshots
View
Yes
Amazon RDS
RegisterDBProxyTargets
Register
Yes
Amazon RDS
CopyOptionGroup
Copy
Yes
Amazon RDS
DescribeValidDBInstanceModifications
View
Yes
Amazon RDS
DescribeDBSnapshotAttributes
View
Yes
Amazon RDS
RestoreDBClusterToPointInTime
Create
Yes
Amazon RDS
ModifyEventSubscription
Edit
Yes
Amazon RDS
RemoveRoleFromDBCluster
Delete
Yes
Amazon RDS
ModifyDBProxyEndpoint
Edit
Yes
Amazon RDS
DescribeDBLogFiles
View
Yes
Amazon RDS
DescribeGlobalClusters
View
Yes
Amazon RDS
DescribeEventCategories
View
Yes
Amazon RDS
DescribeDBProxyTargetGroups
View
Yes
Amazon RDS
ResetDBParameterGroup
Edit
Yes
Amazon RDS
DescribeExportTasks
View
Yes
Amazon RDS
CreateDBSecurityGroup
Create
Yes
Amazon RDS
DescribeDBClusterSnapshots
View
Yes
Amazon RDS
DescribeOptionGroups
View
Yes
Amazon RDS
ModifyDBClusterParameterGroup
Edit
Yes
Amazon RDS
CreateDBCluster
Create
Yes
Amazon RDS
ModifyDBSnapshot
Edit
Yes
Amazon RDS
StopDBCluster
Stop
Yes
Amazon RDS
DeleteInstallationMedia
Delete
Yes
Amazon RDS
RemoveSourceIdentifierFromSubscription
Delete
Yes
Amazon RDS
DeleteDBProxy
Delete
Yes
Amazon RDS
CreateEventSubscription
Create
Yes
Amazon RDS
DescribeDBClusterParameterGroups
View
Yes
Amazon RDS
PromoteReadReplicaDBCluster
Create
Yes
Amazon RDS
ModifyCertificates
Edit
Yes
Amazon RDS
DescribeSourceRegions
View
Yes
Amazon RDS
ModifyDBClusterSnapshotAttribute
Edit
Yes
Amazon RDS
PromoteReadReplica
Create
Yes
Amazon RDS
RemoveTagsFromResource
Delete
Yes
Amazon RDS
DeregisterDBProxyTargets
Deregister
Yes
Amazon RDS
CreateDBProxy
Create
Yes
Amazon RDS
DeleteDBInstance
Delete
Yes
Amazon RDS
DescribeInstallationMedia
View
Yes
Amazon RDS
ModifyDBClusterEndpoint
Edit
Yes
Amazon RDS
DescribeCustomAvailabilityZones
View
Yes
Amazon RDS
StartActivityStream
Start
Yes
Amazon RDS
DescribeEngineDefaultParameters
View
Yes
Amazon RDS
CancelExportTask
Delete
Yes
Amazon RDS
CreateGlobalCluster
Create
Yes
Amazon RDS
CreateDBClusterParameterGroup
Create
Yes
Amazon RDS
ModifyCurrentDBClusterCapacity
Edit
Yes
Amazon RDS
RestoreDBClusterFromSnapshot
Create
Yes
Amazon RDS
DescribeEvents
View
Yes
Amazon RDS
CreateCustomAvailabilityZone
Create
Yes
Amazon RDS
DescribeOptionGroupOptions
View
Yes
Amazon RDS
BacktrackDBCluster
Create
Yes
Amazon RDS
ModifyDBProxyTargetGroup
Edit
Yes
Amazon RDS
CreateDBInstanceReadReplica
Create
Yes
Amazon RDS
DescribeOrderableDBInstanceOptions
View
Yes
Amazon RDS
DeleteDBClusterEndpoint
Delete
Yes
Amazon RDS
DescribeDBInstances
View
Yes
Amazon RDS
DescribeDBClusterSnapshotAttributes
View
Yes
Amazon RDS
AddTagsToResource
Create
Yes
Amazon RDS
ModifyDBCluster
Edit
Yes
Amazon RDS
RestoreDBClusterFromS
Create
Yes
Amazon RDS
ModifyGlobalCluster
Edit
Yes
Amazon RDS
CopyDBSnapshot
Copy
Yes
Amazon RDS
DeleteDBInstanceAutomatedBackup
Delete
Yes
Amazon RDS
DescribeReservedDBInstancesOfferings
View
Yes
Amazon RDS
CreateOptionGroup
Create
Yes
Amazon RDS
AddRoleToDBInstance
Create
Yes
Amazon Redshift
DisableLogging
Delete
Yes
Amazon Redshift
ModifyClusterSnapshot
Edit
Yes
Amazon Redshift
ModifyClusterIamRoles
Edit
Yes
Amazon Redshift
ModifyClusterParameterGroup
Edit
Yes
Amazon Redshift
DescribeClusterSecurityGroups
View
Yes
Amazon Redshift
CreateSnapshotCopyGrant
Create
Yes
Amazon Redshift
CopyClusterSnapshot
Copy
Yes
Amazon Redshift
ModifyCluster
Edit
Yes
Amazon Redshift
DeleteClusterSnapshot
Delete
Yes
Amazon Redshift
DescribeHsmConfigurations
View
Yes
Amazon Redshift
DescribeClusterSubnetGroups
View
Yes
Amazon Redshift
DescribeScheduledActions
View
Yes
Amazon Redshift
AuthorizeSnapshotAccess
Create
Yes
Amazon Redshift
DeleteTags
Delete
Yes
Amazon Redshift
ResizeCluster
Edit
Yes
Amazon Redshift
RevokeClusterSecurityGroupIngress
Delete
Yes
Amazon Redshift
DescribeClusterTracks
View
Yes
Amazon Redshift
RebootCluster
Reboot
Yes
Amazon Redshift
CreateTags
Create
Yes
Amazon Redshift
CreateHsmClientCertificate
Create
Yes
Amazon Redshift
RestoreFromClusterSnapshot
Create
Yes
Amazon Redshift
ModifySnapshotSchedule
Edit
Yes
Amazon Redshift
DeleteCluster
Delete
Yes
Amazon Redshift
DescribeSnapshotCopyGrants
View
Yes
Amazon Redshift
DescribeDefaultClusterParameters
View
Yes
Amazon Redshift
ModifyClusterSnapshots
Edit
Yes
Amazon Redshift
CreateClusterSnapshot
Create
Yes
Amazon Redshift
CreateHsmConfiguration
Create
Yes
Amazon Redshift
ModifyClusterDbRevision
Edit
Yes
Amazon Redshift
CreateSnapshotSchedule
Create
Yes
Amazon Redshift
PauseCluster
Create
Yes
Amazon Redshift
CreateCluster
Create
Yes
Amazon Redshift
ModifyUsageLimit
Edit
Yes
Amazon Redshift
CreateUsageLimit
Create
Yes
Amazon Redshift
DeleteEventSubscription
Delete
Yes
Amazon Redshift
EnableSnapshotCopy
Enable
Yes
Amazon Redshift
AuthorizeEndpointAccess
Create
Yes
Amazon Redshift
DescribeEventSubscriptions
View
Yes
Amazon Redshift
CreateClusterSecurityGroup
Create
Yes
Amazon Redshift
ModifyScheduledAction
Edit
Yes
Amazon Redshift
DeleteHsmConfiguration
Delete
Yes
Amazon Redshift
GetReservedNodeExchangeOfferings
View
Yes
Amazon Redshift
RevokeEndpointAccess
Delete
Yes
Amazon Redshift
DescribeAccountAttributes
View
Yes
Amazon Redshift
CreateEndpointAccess
Create
Yes
Amazon Redshift
DescribeClusterParameters
View
Yes
Amazon Redshift
DeleteEndpointAccess
Delete
Yes
Amazon Redshift
DescribeClusterParameterGroups
View
Yes
Amazon Redshift
DescribeLoggingStatus
View
Yes
Amazon Redshift
DescribeOrderableClusterOptions
View
Yes
Amazon Redshift
AcceptReservedNodeExchange
Approve
Yes
Amazon Redshift
DeleteClusterSubnetGroup
Delete
Yes
Amazon Redshift
ResetClusterParameterGroup
Edit
Yes
Amazon Redshift
DescribeEndpointAccess
View
Yes
Amazon Redshift
RestoreTableFromClusterSnapshot
Create
Yes
Amazon Redshift
DescribeReservedNodeOfferings
View
Yes
Amazon Redshift
DescribeTags
View
Yes
Amazon Redshift
DescribeClusters
View
Yes
Amazon Redshift
DisableSnapshotCopy
Delete
Yes
Amazon Redshift
ModifyEventSubscription
Edit
Yes
Amazon Redshift
DescribeReservedNodes
View
Yes
Amazon Redshift
DeleteHsmClientCertificate
Delete
Yes
Amazon Redshift
PurchaseReservedNodeOffering
Purchase
Yes
Amazon Redshift
DescribeHsmClientCertificates
View
Yes
Amazon Redshift
CreateScheduledAction
Create
Yes
Amazon Redshift
DeleteUsageLimit
Delete
Yes
Amazon Redshift
DeleteClusterParameterGroup
Delete
Yes
Amazon Redshift
DescribeEventCategories
View
Yes
Amazon Redshift
DescribeNodeConfigurationOptions
View
Yes
Amazon Redshift
DescribeSnapshotSchedules
View
Yes
Amazon Redshift
DeleteSnapshotCopyGrant
Delete
Yes
Amazon Redshift
ResumeCluster
Create
Yes
Amazon Redshift
ModifyAquaConfiguration
Edit
Yes
Amazon Redshift
CreateClusterParameterGroup
Create
Yes
Amazon Redshift
CreateEventSubscription
Create
Yes
Amazon Redshift
DescribeClusterVersions
View
Yes
Amazon Redshift
RevokeSnapshotAccess
Delete
Yes
Amazon Redshift
DescribeClusterDbRevisions
View
Yes
Amazon Redshift
DescribeUsageLimits
View
Yes
Amazon Redshift
DescribeResize
View
Yes
Amazon Redshift
DescribeEndpointAuthorization
View
Yes
Amazon Redshift
DescribeTableRestoreStatus
View
Yes
Amazon Redshift
RotateEncryptionKey
Create
Yes
Amazon Redshift
CancelResize
Delete
Yes
Amazon Redshift
DescribeStorage
View
Yes
Amazon Redshift
DeleteClusterSecurityGroup
Delete
Yes
Amazon Redshift
EnableLogging
Enable
Yes
Amazon Redshift
ModifyClusterSubnetGroup
Edit
Yes
Amazon Redshift
GetClusterCredentials
View
Yes
Amazon Redshift
ModifySnapshotCopyRetentionPeriod
Edit
Yes
Amazon Redshift
DeleteSnapshotSchedule
Delete
Yes
Amazon Redshift
DescribeEvents
View
Yes
Amazon Redshift
AuthorizeClusterSecurityGroupIngress
Create
Yes
Amazon Redshift
ModifyClusterMaintenance
Edit
Yes
Amazon Redshift
CreateClusterSubnetGroup
Create
Yes
Amazon Redshift
DeleteScheduledAction
Delete
Yes
Amazon Redshift
ModifyClusterSnapshotSchedule
Edit
Yes
Amazon Redshift
DeleteClusterSnapshots
Delete
Yes
Amazon Redshift
DescribeClusterSnapshots
View
Yes
Amazon Redshift
ModifyEndpointAccess
Edit
Yes
Amazon Redshift Data API Service
ListSchemas
View
Yes
Amazon Redshift Data API Service
ListStatements
View
Yes
Amazon Redshift Data API Service
CancelStatement
Delete
Yes
Amazon Redshift Data API Service
DescribeTable
View
Yes
Amazon Redshift Data API Service
ListTables
View
Yes
Amazon Redshift Data API Service
ExecuteStatement
Create
Yes
Amazon Redshift Data API Service
DescribeStatement
View
Yes
Amazon Redshift Data API Service
GetStatementResult
View
Yes
Amazon Redshift Data API Service
ListDatabases
View
Yes
Amazon Resource Access Manager
EnableSharingWithAwsOrganization
Enable
Yes
Amazon Resource Access Manager
ListPrincipals
View
Yes
Amazon Resource Access Manager
ListResourceSharePermissions
View
Yes
Amazon Resource Access Manager
AssociateResourceShare
Create
Yes
Amazon Resource Access Manager
RejectResourceShareInvitation
Reject
Yes
Amazon Resource Access Manager
UpdateResourceShare
Edit
Yes
Amazon Resource Access Manager
DisassociateResourceSharePermission
Delete
Yes
Amazon Resource Access Manager
GetPermission
View
Yes
Amazon Resource Access Manager
PromoteResourceShareCreatedFromPolicy
Create
Yes
Amazon Resource Access Manager
ListPendingInvitationResources
View
Yes
Amazon Resource Access Manager
DisassociateResourceShare
Delete
Yes
Amazon Resource Access Manager
ListResourceTypes
View
Yes
Amazon Resource Access Manager
TagResource
Create
Yes
Amazon Resource Access Manager
GetResourceShares
View
Yes
Amazon Resource Access Manager
GetResourceShareAssociations
View
Yes
Amazon Resource Access Manager
GetResourceShareInvitations
View
Yes
Amazon Resource Access Manager
DeleteResourceShare
Delete
Yes
Amazon Resource Access Manager
ListResources
View
Yes
Amazon Resource Access Manager
AcceptResourceShareInvitation
Approve
Yes
Amazon Resource Access Manager
AssociateResourceSharePermission
Create
Yes
Amazon Resource Access Manager
GetResourcePolicies
View
Yes
Amazon Resource Access Manager
ListPermissions
View
Yes
Amazon Resource Access Manager
UntagResource
Delete
Yes
Amazon Resource Access Manager
CreateResourceShare
Create
Yes
Amazon Route 53
DisassociateVPCFromHostedZone
Delete
API Only
Amazon Route 53
DisableHostedZoneDNSSEC
Delete
API Only
Amazon Route 53
CreateHealthCheck
Create
API Only
Amazon Route 53
ListHealthChecks
View
API Only
Amazon Route 53
UpdateTrafficPolicyInstance
Edit
API Only
Amazon Route 53
GetTrafficPolicyInstance
View
API Only
Amazon Route 53
DeleteTrafficPolicyInstance
Delete
API Only
Amazon Route 53
ListHostedZonesByVPC
View
API Only
Amazon Route 53
ListTrafficPolicyVersions
View
API Only
Amazon Route 53
DeactivateKeySigningKey
Deactivate
API Only
Amazon Route 53
GetAccountLimit
View
API Only
Amazon Route 53
GetReusableDelegationSetLimit
View
API Only
Amazon Route 53
ListHostedZonesByName
View
API Only
Amazon Route 53
ListResourceRecordSets
View
API Only
Amazon Route 53
GetDNSSEC
View
API Only
Amazon Route 53
GetGeoLocation
View
API Only
Amazon Route 53
CreateKeySigningKey
Create
API Only
Amazon Route 53
UpdateHealthCheck
Edit
API Only
Amazon Route 53
GetHealthCheck
View
API Only
Amazon Route 53
DeleteHealthCheck
Delete
API Only
Amazon Route 53
ListTagsForResources
View
API Only
Amazon Route 53
UpdateHostedZoneComment
Edit
API Only
Amazon Route 53
GetHostedZone
View
API Only
Amazon Route 53
DeleteHostedZone
Delete
API Only
Amazon Route 53
ListGeoLocations
View
API Only
Amazon Route 53
GetHostedZoneCount
View
API Only
Amazon Route 53
UpdateTrafficPolicyComment
Edit
API Only
Amazon Route 53
GetTrafficPolicy
View
API Only
Amazon Route 53
DeleteTrafficPolicy
Delete
API Only
Amazon Route 53
ChangeTagsForResource
Create
API Only
Amazon Route 53
ListTagsForResource
View
API Only
Amazon Route 53
CreateQueryLoggingConfig
Create
API Only
Amazon Route 53
ListQueryLoggingConfigs
View
API Only
Amazon Route 53
CreateReusableDelegationSet
Create
API Only
Amazon Route 53
ListReusableDelegationSets
View
API Only
Amazon Route 53
GetTrafficPolicyInstanceCount
View
API Only
Amazon Route 53
TestDNSAnswer
View
API Only
Amazon Route 53
ActivateKeySigningKey
Activate
API Only
Amazon Route 53
GetCheckerIpRanges
View
API Only
Amazon Route 53
GetChange
View
API Only
Amazon Route 53
GetReusableDelegationSet
View
API Only
Amazon Route 53
DeleteReusableDelegationSet
Delete
API Only
Amazon Route 53
ListTrafficPolicyInstancesByPolicy
View
API Only
Amazon Route 53
ListTrafficPolicies
View
API Only
Amazon Route 53
GetHealthCheckCount
View
API Only
Amazon Route 53
CreateTrafficPolicy
Create
API Only
Amazon Route 53
GetHealthCheckStatus
View
API Only
Amazon Route 53
GetHostedZoneLimit
View
API Only
Amazon Route 53
AssociateVPCWithHostedZone
Create
API Only
Amazon Route 53
EnableHostedZoneDNSSEC
Enable
API Only
Amazon Route 53
ChangeResourceRecordSets
Create
API Only
Amazon Route 53
DeleteVPCAssociationAuthorization
Delete
API Only
Amazon Route 53
CreateVPCAssociationAuthorization
Create
API Only
Amazon Route 53
ListVPCAssociationAuthorizations
View
API Only
Amazon Route 53
DeleteKeySigningKey
Delete
API Only
Amazon Route 53
CreateHostedZone
Create
API Only
Amazon Route 53
ListHostedZones
View
API Only
Amazon Route 53
CreateTrafficPolicyVersion
Create
API Only
Amazon Route 53
GetQueryLoggingConfig
View
API Only
Amazon Route 53
DeleteQueryLoggingConfig
Delete
API Only
Amazon Route 53
CreateTrafficPolicyInstance
Create
API Only
Amazon Route 53
ListTrafficPolicyInstances
View
API Only
Amazon Route 53
GetHealthCheckLastFailureReason
View
API Only
Amazon Route 53
ListTrafficPolicyInstancesByHostedZone
View
API Only
Amazon S3
CreateBucket
Create
Yes
Amazon S3
HeadBucket
View
Yes
Amazon S3
ListObjects
View
Yes
Amazon S3
DeleteBucket
Delete
Yes
Amazon S3
ListObjectVersions
View
Yes
Amazon S3
PutBucketOwnershipControls
Edit
Yes
Amazon S3
GetBucketOwnershipControls
View
Yes
Amazon S3
DeleteBucketOwnershipControls
Delete
Yes
Amazon S3
PutBucketRequestPayment
Edit
Yes
Amazon S3
GetBucketRequestPayment
View
Yes
Amazon S3
ListBucketMetricsConfigurations
View
Yes
Amazon S3
PutObjectAcl
Edit
Yes
Amazon S3
GetObjectAcl
View
Yes
Amazon S3
PutBucketTagging
Edit
Yes
Amazon S3
GetBucketTagging
View
Yes
Amazon S3
DeleteBucketTagging
Delete
Yes
Amazon S3
DeleteObjects
Delete
Yes
Amazon S3
CompleteMultipartUpload
Create
Yes
Amazon S3
ListParts
View
Yes
Amazon S3
AbortMultipartUpload
Delete
Yes
Amazon S3
ListBuckets
View
Yes
Amazon S3
GetBucketLocation
View
Yes
Amazon S3
PutBucketIntelligentTieringConfiguration
Edit
Yes
Amazon S3
GetBucketIntelligentTieringConfiguration
View
Yes
Amazon S3
DeleteBucketIntelligentTieringConfiguration
Delete
Yes
Amazon S3
PutBucketEncryption
Edit
Yes
Amazon S3
GetBucketEncryption
View
Yes
Amazon S3
DeleteBucketEncryption
Delete
Yes
Amazon S3
ListBucketIntelligentTieringConfigurations
View
Yes
Amazon S3
GetBucketPolicyStatus
View
Yes
Amazon S3
PutBucketAnalyticsConfiguration
Edit
Yes
Amazon S3
GetBucketAnalyticsConfiguration
View
Yes
Amazon S3
DeleteBucketAnalyticsConfiguration
Delete
Yes
Amazon S3
PutBucketPolicy
Edit
Yes
Amazon S3
GetBucketPolicy
View
Yes
Amazon S3
DeleteBucketPolicy
Delete
Yes
Amazon S3
ListBucketInventoryConfigurations
View
Yes
Amazon S3
PutBucketVersioning
Edit
Yes
Amazon S3
GetBucketVersioning
View
Yes
Amazon S3
PutBucketNotification
Edit
Yes
Amazon S3
GetBucketNotification
View
Yes
Amazon S3
PutBucketReplication
Edit
Yes
Amazon S3
GetBucketReplication
View
Yes
Amazon S3
DeleteBucketReplication
Delete
Yes
Amazon S3
PutObjectLockConfiguration
Edit
Yes
Amazon S3
GetObjectLockConfiguration
View
Yes
Amazon S3
SelectObjectContent
Create
Yes
Amazon S3
CopyObject
Copy
Yes
Amazon S3
PutBucketMetricsConfiguration
Edit
Yes
Amazon S3
GetBucketMetricsConfiguration
View
Yes
Amazon S3
DeleteBucketMetricsConfiguration
Delete
Yes
Amazon S3
UploadPart
Upload
Yes
Amazon S3
UploadPartCopy
Upload
Yes
Amazon S3
PutObjectRetention
Edit
Yes
Amazon S3
GetObjectRetention
View
Yes
Amazon S3
ListObjectsV
View
Yes
Amazon S3
RestoreObject
Create
Yes
Amazon S3
PutBucketAcl
Edit
Yes
Amazon S3
GetBucketAcl
View
Yes
Amazon S3
PutBucketWebsite
Edit
Yes
Amazon S3
GetBucketWebsite
View
Yes
Amazon S3
DeleteBucketWebsite
Delete
Yes
Amazon S3
PutBucketAccelerateConfiguration
Edit
Yes
Amazon S3
GetBucketAccelerateConfiguration
View
Yes
Amazon S3
CreateMultipartUpload
Create
Yes
Amazon S3
ListBucketAnalyticsConfigurations
View
Yes
Amazon S3
PutObject
Edit
Yes
Amazon S3
HeadObject
View
Yes
Amazon S3
GetObject
View
Yes
Amazon S3
DeleteObject
Delete
Yes
Amazon S3
PutBucketLifecycle
Edit
Yes
Amazon S3
GetBucketLifecycle
View
Yes
Amazon S3
PutBucketInventoryConfiguration
Edit
Yes
Amazon S3
GetBucketInventoryConfiguration
View
Yes
Amazon S3
DeleteBucketInventoryConfiguration
Delete
Yes
Amazon S3
ListMultipartUploads
View
Yes
Amazon S3
PutBucketLifecycleConfiguration
Edit
Yes
Amazon S3
GetBucketLifecycleConfiguration
View
Yes
Amazon S3
DeleteBucketLifecycle
Delete
Yes
Amazon S3
WriteGetObjectResponse
Create
Yes
Amazon S3
PutPublicAccessBlock
Edit
Yes
Amazon S3
GetPublicAccessBlock
View
Yes
Amazon S3
DeletePublicAccessBlock
Delete
Yes
Amazon S3
PutBucketCors
Edit
Yes
Amazon S3
GetBucketCors
View
Yes
Amazon S3
DeleteBucketCors
Delete
Yes
Amazon S3
PutObjectLegalHold
Edit
Yes
Amazon S3
GetObjectLegalHold
View
Yes
Amazon S3
PutBucketLogging
Edit
Yes
Amazon S3
GetBucketLogging
View
Yes
Amazon S3
PutBucketNotificationConfiguration
Edit
Yes
Amazon S3
GetBucketNotificationConfiguration
View
Yes
Amazon S3
GetObjectTorrent
View
Yes
Amazon S3
PutObjectTagging
Edit
Yes
Amazon S3
GetObjectTagging
View
Yes
Amazon S3
DeleteObjectTagging
Delete
Yes
Amazon Secrets Manager
ReplicateSecretToRegions
Create
Yes
Amazon Secrets Manager
RotateSecret
Create
Yes
Amazon Secrets Manager
GetRandomPassword
View
Yes
Amazon Secrets Manager
PutSecretValue
Edit
Yes
Amazon Secrets Manager
UpdateSecretVersionStage
Edit
Yes
Amazon Secrets Manager
StopReplicationToReplica
Stop
Yes
Amazon Secrets Manager
DeleteResourcePolicy
Delete
Yes
Amazon Secrets Manager
ValidateResourcePolicy
Create
Yes
Amazon Secrets Manager
GetResourcePolicy
View
Yes
Amazon Secrets Manager
RestoreSecret
Create
Yes
Amazon Secrets Manager
RemoveRegionsFromReplication
Delete
Yes
Amazon Secrets Manager
DescribeSecret
View
Yes
Amazon Secrets Manager
TagResource
Create
Yes
Amazon Secrets Manager
UntagResource
Delete
Yes
Amazon Secrets Manager
CreateSecret
Create
Yes
Amazon Secrets Manager
DeleteSecret
Delete
Yes
Amazon Secrets Manager
GetSecretValue
View
Yes
Amazon Secrets Manager
UpdateSecret
Edit
Yes
Amazon Secrets Manager
CancelRotateSecret
Delete
Yes
Amazon Secrets Manager
PutResourcePolicy
Edit
Yes
Amazon Secrets Manager
ListSecretVersionIds
View
Yes
Amazon Secrets Manager
ListSecrets
View
Yes
Amazon SNS
CreatePlatformApplication
Create
Yes
Amazon SNS
SetEndpointAttributes
Create
Yes
Amazon SNS
ConfirmSubscription
Create
Yes
Amazon SNS
ListTopics
View
Yes
Amazon SNS
CreatePlatformEndpoint
Create
Yes
Amazon SNS
ListTagsForResource
View
Yes
Amazon SNS
SetPlatformApplicationAttributes
Create
Yes
Amazon SNS
DeleteTopic
Delete
Yes
Amazon SNS
GetSubscriptionAttributes
View
Yes
Amazon SNS
SetSMSAttributes
Create
Yes
Amazon SNS
SetSubscriptionAttributes
Create
Yes
Amazon SNS
GetTopicAttributes
View
Yes
Amazon SNS
Unsubscribe
Create
Yes
Amazon SNS
CreateTopic
Create
Yes
Amazon SNS
DeletePlatformApplication
Delete
Yes
Amazon SNS
GetSMSAttributes
View
Yes
Amazon SNS
CheckIfPhoneNumberIsOptedOut
Create
Yes
Amazon SNS
ListSubscriptionsByTopic
View
Yes
Amazon SNS
ListEndpointsByPlatformApplication
View
Yes
Amazon SNS
GetEndpointAttributes
View
Yes
Amazon SNS
UntagResource
Delete
Yes
Amazon SNS
ListPhoneNumbersOptedOut
View
Yes
Amazon SNS
ListSubscriptions
View
Yes
Amazon SNS
ListPlatformApplications
View
Yes
Amazon SNS
RemovePermission
Delete
Yes
Amazon SNS
AddPermission
Create
Yes
Amazon SNS
SetTopicAttributes
Create
Yes
Amazon SNS
Publish
Create
Yes
Amazon SNS
TagResource
Create
Yes
Amazon SNS
Subscribe
Create
Yes
Amazon SNS
DeleteEndpoint
Delete
Yes
Amazon SNS
OptInPhoneNumber
Create
Yes
Amazon SNS
GetPlatformApplicationAttributes
View
Yes
Amazon SQS
GetQueueUrl
View
Yes
Amazon SQS
SendMessage
Send
Yes
Amazon SQS
TagQueue
Create
Yes
Amazon SQS
DeleteMessage
Delete
Yes
Amazon SQS
GetQueueAttributes
View
Yes
Amazon SQS
ReceiveMessage
Create
Yes
Amazon SQS
CreateQueue
Create
Yes
Amazon SQS
ListQueues
View
Yes
Amazon SQS
UntagQueue
Delete
Yes
Amazon SQS
ListDeadLetterSourceQueues
View
Yes
Amazon SQS
DeleteQueue
Delete
Yes
Amazon SQS
RemovePermission
Delete
Yes
Amazon SQS
ChangeMessageVisibility
Create
Yes
Amazon SQS
AddPermission
Create
Yes
Amazon SQS
ListQueueTags
View
Yes
Amazon SQS
PurgeQueue
Create
Yes
Amazon SQS
SetQueueAttributes
Create
Yes
Amazon Systems Manager
Start
StartSession
Yes
Amazon Systems Manager
Delete
DeleteMaintenanceWindow
Yes
Amazon Systems Manager
Delete
DeleteParameter
Yes
Amazon Systems Manager
View
DescribeAvailablePatches
Yes
Amazon Systems Manager
Edit
UpdateDocumentMetadata
Yes
Amazon Systems Manager
View
DescribeAutomationExecutions
Yes
Amazon Systems Manager
Create
CreateAssociation
Yes
Amazon Systems Manager
View
DescribePatchProperties
Yes
Amazon Systems Manager
View
DescribeDocumentPermission
Yes
Amazon Systems Manager
View
GetOpsSummary
Yes
Amazon Systems Manager
View
ListCommandInvocations
Yes
Amazon Systems Manager
View
GetPatchBaseline
Yes
Amazon Systems Manager
View
ListAssociations
Yes
Amazon Systems Manager
View
GetOpsItem
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowSchedule
Yes
Amazon Systems Manager
Edit
UpdateMaintenanceWindow
Yes
Amazon Systems Manager
Edit
PutParameter
Yes
Amazon Systems Manager
Delete
DeleteInventory
Yes
Amazon Systems Manager
Create
UnlabelParameterVersion
Yes
Amazon Systems Manager
Edit
UpdateAssociationStatus
Yes
Amazon Systems Manager
Register
RegisterPatchBaselineForPatchGroup
Yes
Amazon Systems Manager
View
GetServiceSetting
Yes
Amazon Systems Manager
Delete
CancelCommand
Yes
Amazon Systems Manager
Edit
UpdateServiceSetting
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowExecutions
Yes
Amazon Systems Manager
Delete
CancelMaintenanceWindowExecution
Yes
Amazon Systems Manager
View
GetMaintenanceWindowExecutionTask
Yes
Amazon Systems Manager
View
DescribeEffectivePatchesForPatchBaseline
Yes
Amazon Systems Manager
Delete
DeleteOpsMetadata
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowExecutionTasks
Yes
Amazon Systems Manager
Create
CreateOpsItem
Yes
Amazon Systems Manager
View
DescribeDocument
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindows
Yes
Amazon Systems Manager
View
DescribePatchGroups
Yes
Amazon Systems Manager
Create
ResumeSession
Yes
Amazon Systems Manager
View
GetMaintenanceWindowExecutionTaskInvocation
Yes
Amazon Systems Manager
View
ListOpsMetadata
Yes
Amazon Systems Manager
Start
StartAutomationExecution
Yes
Amazon Systems Manager
View
GetPatchBaselineForPatchGroup
Yes
Amazon Systems Manager
View
DescribeAssociation
Yes
Amazon Systems Manager
Register
RegisterTaskWithMaintenanceWindow
Yes
Amazon Systems Manager
View
DescribeActivations
Yes
Amazon Systems Manager
Edit
UpdateAssociation
Yes
Amazon Systems Manager
Edit
ResetServiceSetting
Yes
Amazon Systems Manager
View
ListDocuments
Yes
Amazon Systems Manager
Deregister
DeregisterTaskFromMaintenanceWindow
Yes
Amazon Systems Manager
View
DescribeInventoryDeletions
Yes
Amazon Systems Manager
Create
CreateActivation
Yes
Amazon Systems Manager
Start
StartAssociationsOnce
Yes
Amazon Systems Manager
Create
CreateDocument
Yes
Amazon Systems Manager
View
DescribePatchBaselines
Yes
Amazon Systems Manager
View
GetDocument
Yes
Amazon Systems Manager
View
ListResourceComplianceSummaries
Yes
Amazon Systems Manager
View
GetParametersByPath
Yes
Amazon Systems Manager
Delete
DeleteParameters
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowsForTarget
Yes
Amazon Systems Manager
Delete
DeletePatchBaseline
Yes
Amazon Systems Manager
View
GetInventory
Yes
Amazon Systems Manager
View
DescribeAssociationExecutions
Yes
Amazon Systems Manager
View
GetParameter
Yes
Amazon Systems Manager
Edit
UpdateMaintenanceWindowTask
Yes
Amazon Systems Manager
View
DescribeAutomationStepExecutions
Yes
Amazon Systems Manager
Create
CreateMaintenanceWindow
Yes
Amazon Systems Manager
Edit
UpdateManagedInstanceRole
Yes
Amazon Systems Manager
Delete
DeleteAssociation
Yes
Amazon Systems Manager
Edit
UpdateDocumentDefaultVersion
Yes
Amazon Systems Manager
Delete
DeleteActivation
Yes
Amazon Systems Manager
Edit
UpdateResourceDataSync
Yes
Amazon Systems Manager
Edit
PutComplianceItems
Yes
Amazon Systems Manager
View
GetOpsMetadata
Yes
Amazon Systems Manager
View
GetParameterHistory
Yes
Amazon Systems Manager
Deregister
DeregisterTargetFromMaintenanceWindow
Yes
Amazon Systems Manager
View
ListDocumentVersions
Yes
Amazon Systems Manager
View
DescribeOpsItems
Yes
Amazon Systems Manager
View
DescribeInstanceAssociationsStatus
Yes
Amazon Systems Manager
Delete
RemoveTagsFromResource
Yes
Amazon Systems Manager
View
GetDeployablePatchSnapshotForInstance
Yes
Amazon Systems Manager
View
DescribeInstancePatchStates
Yes
Amazon Systems Manager
Create
CreatePatchBaseline
Yes
Amazon Systems Manager
Edit
UpdateOpsItem
Yes
Amazon Systems Manager
View
DescribeSessions
Yes
Amazon Systems Manager
View
ListOpsItemEvents
Yes
Amazon Systems Manager
Create
CreateAssociationBatch
Yes
Amazon Systems Manager
View
DescribeEffectiveInstanceAssociations
Yes
Amazon Systems Manager
View
ListComplianceItems
Yes
Amazon Systems Manager
Delete
DeleteResourceDataSync
Yes
Amazon Systems Manager
View
GetCalendarState
Yes
Amazon Systems Manager
Deregister
DeregisterManagedInstance
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowTasks
Yes
Amazon Systems Manager
Stop
StopAutomationExecution
Yes
Amazon Systems Manager
Edit
UpdateOpsMetadata
Yes
Amazon Systems Manager
Create
CreateOpsMetadata
Yes
Amazon Systems Manager
View
DescribeAssociationExecutionTargets
Yes
Amazon Systems Manager
Register
RegisterDefaultPatchBaseline
Yes
Amazon Systems Manager
View
GetMaintenanceWindowExecution
Yes
Amazon Systems Manager
Terminate
TerminateSession
Yes
Amazon Systems Manager
View
DescribeInstancePatchStatesForPatchGroup
Yes
Amazon Systems Manager
View
GetMaintenanceWindow
Yes
Amazon Systems Manager
Send
SendCommand
Yes
Amazon Systems Manager
View
ListInventoryEntries
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowTargets
Yes
Amazon Systems Manager
Edit
UpdatePatchBaseline
Yes
Amazon Systems Manager
Create
AddTagsToResource
Yes
Amazon Systems Manager
View
GetAutomationExecution
Yes
Amazon Systems Manager
View
DescribeInstancePatches
Yes
Amazon Systems Manager
View
DescribePatchGroupState
Yes
Amazon Systems Manager
Send
SendAutomationSignal
Yes
Amazon Systems Manager
View
ListResourceDataSync
Yes
Amazon Systems Manager
View
ListComplianceSummaries
Yes
Amazon Systems Manager
View
GetConnectionStatus
Yes
Amazon Systems Manager
View
DescribeInstanceInformation
Yes
Amazon Systems Manager
Create
LabelParameterVersion
Yes
Amazon Systems Manager
Register
RegisterTargetWithMaintenanceWindow
Yes
Amazon Systems Manager
Edit
ModifyDocumentPermission
Yes
Amazon Systems Manager
View
GetParameters
Yes
Amazon Systems Manager
View
GetDefaultPatchBaseline
Yes
Amazon Systems Manager
Edit
UpdateDocument
Yes
Amazon Systems Manager
View
ListDocumentMetadataHistory
Yes
Amazon Systems Manager
View
ListAssociationVersions
Yes
Amazon Systems Manager
View
GetMaintenanceWindowTask
Yes
Amazon Systems Manager
View
GetCommandInvocation
Yes
Amazon Systems Manager
View
ListCommands
Yes
Amazon Systems Manager
View
DescribeMaintenanceWindowExecutionTaskInvocations
Yes
Amazon Systems Manager
Edit
UpdateMaintenanceWindowTarget
Yes
Amazon Systems Manager
Edit
PutInventory
Yes
Amazon Systems Manager
Create
CreateResourceDataSync
Yes
Amazon Systems Manager
View
DescribeParameters
Yes
Amazon Systems Manager
View
GetInventorySchema
Yes
Amazon Systems Manager
Start
StartChangeRequestExecution
Yes
Amazon Systems Manager
Deregister
DeregisterPatchBaselineForPatchGroup
Yes
Amazon WAF
GetPermissionPolicy
View
Yes
Amazon WAF
UpdateRegexPatternSet
Edit
Yes
Amazon WAF
DeleteByteMatchSet
Delete
Yes
Amazon WAF
UpdateSizeConstraintSet
Edit
Yes
Amazon WAF
DeleteRuleGroup
Delete
Yes
Amazon WAF
GetXssMatchSet
View
Yes
Amazon WAF
UpdateRegexMatchSet
Edit
Yes
Amazon WAF
DeleteWebACL
Delete
Yes
Amazon WAF
ListSubscribedRuleGroups
View
Yes
Amazon WAF
UpdateSqlInjectionMatchSet
Edit
Yes
Amazon WAF
DeleteRegexPatternSet
Delete
Yes
Amazon WAF
CreateRule
Create
Yes
Amazon WAF
CreateSizeConstraintSet
Create
Yes
Amazon WAF
ListByteMatchSets
View
Yes
Amazon WAF
CreateWebACLMigrationStack
Create
Yes
Amazon WAF
UpdateRule
Edit
Yes
Amazon WAF
UpdateByteMatchSet
Edit
Yes
Amazon WAF
PutPermissionPolicy
Edit
Yes
Amazon WAF
GetGeoMatchSet
View
Yes
Amazon WAF
DeleteRateBasedRule
Delete
Yes
Amazon WAF
CreateRegexMatchSet
Create
Yes
Amazon WAF
DeleteSqlInjectionMatchSet
Delete
Yes
Amazon WAF
GetLoggingConfiguration
View
Yes
Amazon WAF
UpdateXssMatchSet
Edit
Yes
Amazon WAF
UpdateGeoMatchSet
Edit
Yes
Amazon WAF
CreateRuleGroup
Create
Yes
Amazon WAF
GetRegexPatternSet
View
Yes
Amazon WAF
ListRateBasedRules
View
Yes
Amazon WAF
GetRule
View
Yes
Amazon WAF
DeletePermissionPolicy
Delete
Yes
Amazon WAF
GetSampledRequests
View
Yes
Amazon WAF
DeleteSizeConstraintSet
Delete
Yes
Amazon WAF
DeleteGeoMatchSet
Delete
Yes
Amazon WAF
DeleteXssMatchSet
Delete
Yes
Amazon WAF
ListTagsForResource
View
Yes
Amazon WAF
GetWebACL
View
Yes
Amazon WAF
PutLoggingConfiguration
Edit
Yes
Amazon WAF
ListLoggingConfigurations
View
Yes
Amazon WAF
ListActivatedRulesInRuleGroup
View
Yes
Amazon WAF
UpdateIPSet
Edit
Yes
Amazon WAF
DeleteIPSet
Delete
Yes
Amazon WAF
ListRegexPatternSets
View
Yes
Amazon WAF
DeleteRule
Delete
Yes
Amazon WAF
UpdateRateBasedRule
Edit
Yes
Amazon WAF
GetRegexMatchSet
View
Yes
Amazon WAF
ListSizeConstraintSets
View
Yes
Amazon WAF
GetRateBasedRuleManagedKeys
View
Yes
Amazon WAF
ListRuleGroups
View
Yes
Amazon WAF
UntagResource
Delete
Yes
Amazon WAF
GetChangeTokenStatus
View
Yes
Amazon WAF
GetSizeConstraintSet
View
Yes
Amazon WAF
GetChangeToken
View
Yes
Amazon WAF
ListWebACLs
View
Yes
Amazon WAF
CreateXssMatchSet
Create
Yes
Amazon WAF
ListRules
View
Yes
Amazon WAF
CreateRateBasedRule
Create
Yes
Amazon WAF
GetSqlInjectionMatchSet
View
Yes
Amazon WAF
GetIPSet
View
Yes
Amazon WAF
UpdateWebACL
Edit
Yes
Amazon WAF
GetRuleGroup
View
Yes
Amazon WAF
ListIPSets
View
Yes
Amazon WAF
CreateByteMatchSet
Create
Yes
Amazon WAF
CreateRegexPatternSet
Create
Yes
Amazon WAF
GetRateBasedRule
View
Yes
Amazon WAF
ListXssMatchSets
View
Yes
Amazon WAF
ListRegexMatchSets
View
Yes
Amazon WAF
ListSqlInjectionMatchSets
View
Yes
Amazon WAF
DeleteRegexMatchSet
Delete
Yes
Amazon WAF
GetByteMatchSet
View
Yes
Amazon WAF
UpdateRuleGroup
Edit
Yes
Amazon WAF
CreateGeoMatchSet
Create
Yes
Amazon WAF
CreateSqlInjectionMatchSet
Create
Yes
Amazon WAF
CreateWebACL
Create
Yes
Amazon WAF
CreateIPSet
Create
Yes
Amazon WAF
TagResource
Create
Yes
Amazon WAF
ListGeoMatchSets
View
Yes
Amazon WAF
DeleteLoggingConfiguration
Delete
Yes
Amazon WAF Regional
GetIPSet
View
Yes
Amazon WAF Regional
GetGeoMatchSet
View
Yes
Amazon WAF Regional
DisassociateWebACL
Delete
Yes
Amazon WAF Regional
DeleteRule
Delete
Yes
Amazon WAF Regional
GetRegexPatternSet
View
Yes
Amazon WAF Regional
CreateIPSet
Create
Yes
Amazon WAF Regional
PutLoggingConfiguration
Edit
Yes
Amazon WAF Regional
DeleteXssMatchSet
Delete
Yes
Amazon WAF Regional
ListRateBasedRules
View
Yes
Amazon WAF Regional
UpdateSqlInjectionMatchSet
Edit
Yes
Amazon WAF Regional
CreateByteMatchSet
Create
Yes
Amazon WAF Regional
CreateRule
Create
Yes
Amazon WAF Regional
UpdateRateBasedRule
Edit
Yes
Amazon WAF Regional
GetPermissionPolicy
View
Yes
Amazon WAF Regional
ListIPSets
View
Yes
Amazon WAF Regional
DeleteLoggingConfiguration
Delete
Yes
Amazon WAF Regional
DeletePermissionPolicy
Delete
Yes
Amazon WAF Regional
ListRules
View
Yes
Amazon WAF Regional
ListActivatedRulesInRuleGroup
View
Yes
Amazon WAF Regional
GetWebACLForResource
View
Yes
Amazon WAF Regional
ListSqlInjectionMatchSets
View
Yes
Amazon WAF Regional
GetRateBasedRuleManagedKeys
View
Yes
Amazon WAF Regional
UpdateGeoMatchSet
Edit
Yes
Amazon WAF Regional
GetByteMatchSet
View
Yes
Amazon WAF Regional
TagResource
Create
Yes
Amazon WAF Regional
ListRuleGroups
View
Yes
Amazon WAF Regional
UpdateIPSet
Edit
Yes
Amazon WAF Regional
GetChangeTokenStatus
View
Yes
Amazon WAF Regional
GetSampledRequests
View
Yes
Amazon WAF Regional
ListRegexMatchSets
View
Yes
Amazon WAF Regional
ListWebACLs
View
Yes
Amazon WAF Regional
DeleteGeoMatchSet
Delete
Yes
Amazon WAF Regional
UpdateWebACL
Edit
Yes
Amazon WAF Regional
DeleteSizeConstraintSet
Delete
Yes
Amazon WAF Regional
CreateGeoMatchSet
Create
Yes
Amazon WAF Regional
PutPermissionPolicy
Edit
Yes
Amazon WAF Regional
CreateXssMatchSet
Create
Yes
Amazon WAF Regional
GetLoggingConfiguration
View
Yes
Amazon WAF Regional
GetRateBasedRule
View
Yes
Amazon WAF Regional
UpdateXssMatchSet
Edit
Yes
Amazon WAF Regional
DeleteIPSet
Delete
Yes
Amazon WAF Regional
DeleteSqlInjectionMatchSet
Delete
Yes
Amazon WAF Regional
CreateSqlInjectionMatchSet
Create
Yes
Amazon WAF Regional
DeleteWebACL
Delete
Yes
Amazon WAF Regional
ListXssMatchSets
View
Yes
Amazon WAF Regional
GetXssMatchSet
View
Yes
Amazon WAF Regional
ListResourcesForWebACL
View
Yes
Amazon WAF Regional
UpdateRegexMatchSet
Edit
Yes
Amazon WAF Regional
UpdateByteMatchSet
Edit
Yes
Amazon WAF Regional
ListByteMatchSets
View
Yes
Amazon WAF Regional
ListGeoMatchSets
View
Yes
Amazon WAF Regional
ListLoggingConfigurations
View
Yes
Amazon WAF Regional
UpdateSizeConstraintSet
Edit
Yes
Amazon WAF Regional
UpdateRule
Edit
Yes
Amazon WAF Regional
GetSizeConstraintSet
View
Yes
Amazon WAF Regional
UpdateRegexPatternSet
Edit
Yes
Amazon WAF Regional
CreateRateBasedRule
Create
Yes
Amazon WAF Regional
ListSizeConstraintSets
View
Yes
Amazon WAF Regional
CreateWebACL
Create
Yes
Amazon WAF Regional
DeleteRuleGroup
Delete
Yes
Amazon WAF Regional
ListTagsForResource
View
Yes
Amazon WAF Regional
ListRegexPatternSets
View
Yes
Amazon WAF Regional
CreateWebACLMigrationStack
Create
Yes
Amazon WAF Regional
GetRuleGroup
View
Yes
Amazon WAF Regional
DeleteRegexMatchSet
Delete
Yes
Amazon WAF Regional
GetWebACL
View
Yes
Amazon WAF Regional
GetRegexMatchSet
View
Yes
Amazon WAF Regional
GetSqlInjectionMatchSet
View
Yes
Amazon WAF Regional
CreateRegexMatchSet
Create
Yes
Amazon WAF Regional
DeleteByteMatchSet
Delete
Yes
Amazon WAF Regional
ListSubscribedRuleGroups
View
Yes
Amazon WAF Regional
AssociateWebACL
Create
Yes
Amazon WAF Regional
CreateRuleGroup
Create
Yes
Amazon WAF Regional
UntagResource
Delete
Yes
Amazon WAF Regional
DeleteRateBasedRule
Delete
Yes
Amazon WAF Regional
CreateSizeConstraintSet
Create
Yes
Amazon WAF Regional
DeleteRegexPatternSet
Delete
Yes
Amazon WAF Regional
UpdateRuleGroup
Edit
Yes
Amazon WAF Regional
CreateRegexPatternSet
Create
Yes
Amazon WAF Regional
GetChangeToken
View
Yes
Amazon WAF Regional
GetRule
View
Yes
Amazon WAFV2
ListResourcesForWebACL
View
Yes
Amazon WAFV2
DeleteIPSet
Delete
Yes
Amazon WAFV2
CreateWebACL
Create
Yes
Amazon WAFV2
UpdateRuleGroup
Edit
Yes
Amazon WAFV2
UpdateRegexPatternSet
Edit
Yes
Amazon WAFV2
ListRuleGroups
View
Yes
Amazon WAFV2
ListIPSets
View
Yes
Amazon WAFV2
DeleteLoggingConfiguration
Delete
Yes
Amazon WAFV2
CreateRegexPatternSet
Create
Yes
Amazon WAFV2
DeleteWebACL
Delete
Yes
Amazon WAFV2
DeleteRegexPatternSet
Delete
Yes
Amazon WAFV2
GetLoggingConfiguration
View
Yes
Amazon WAFV2
DescribeManagedRuleGroup
View
Yes
Amazon WAFV2
UpdateIPSet
Edit
Yes
Amazon WAFV2
UntagResource
Delete
Yes
Amazon WAFV2
GetWebACL
View
Yes
Amazon WAFV2
CreateIPSet
Create
Yes
Amazon WAFV2
CheckCapacity
Create
Yes
Amazon WAFV2
CreateRuleGroup
Create
Yes
Amazon WAFV2
GetRateBasedStatementManagedKeys
View
Yes
Amazon WAFV2
GetPermissionPolicy
View
Yes
Amazon WAFV2
PutLoggingConfiguration
Edit
Yes
Amazon WAFV2
ListAvailableManagedRuleGroups
View
Yes
Amazon WAFV2
GetSampledRequests
View
Yes
Amazon WAFV2
ListLoggingConfigurations
View
Yes
Amazon WAFV2
GetWebACLForResource
View
Yes
Amazon WAFV2
DeleteRuleGroup
Delete
Yes
Amazon WAFV2
GetRuleGroup
View
Yes
Amazon WAFV2
ListRegexPatternSets
View
Yes
Amazon WAFV2
GetIPSet
View
Yes
Amazon WAFV2
DisassociateWebACL
Delete
Yes
Amazon WAFV2
ListTagsForResource
View
Yes
Amazon WAFV2
UpdateWebACL
Edit
Yes
Amazon WAFV2
ListWebACLs
View
Yes
Amazon WAFV2
DeletePermissionPolicy
Delete
Yes
Amazon WAFV2
DeleteFirewallManagerRuleGroups
Delete
Yes
Amazon WAFV2
GetRegexPatternSet
View
Yes
Amazon WAFV2
TagResource
Create
Yes
Amazon WAFV2
AssociateWebACL
Create
Yes
Amazon WAFV2
PutPermissionPolicy
Edit
Yes
Amazon WorkDocs
CreateLabels
Create
Yes
Amazon WorkDocs
DeleteLabels
Delete
Yes
Amazon WorkDocs
RemoveResourcePermission
Delete
Yes
Amazon WorkDocs
GetCurrentUser
View
Yes
Amazon WorkDocs
CreateComment
Create
Yes
Amazon WorkDocs
UpdateDocumentVersion
Edit
Yes
Amazon WorkDocs
GetDocumentVersion
View
Yes
Amazon WorkDocs
AbortDocumentVersionUpload
Delete
Yes
Amazon WorkDocs
CreateNotificationSubscription
Create
Yes
Amazon WorkDocs
DescribeNotificationSubscriptions
View
Yes
Amazon WorkDocs
CreateCustomMetadata
Create
Yes
Amazon WorkDocs
DeleteCustomMetadata
Delete
Yes
Amazon WorkDocs
GetResources
View
Yes
Amazon WorkDocs
DescribeDocumentVersions
View
Yes
Amazon WorkDocs
ActivateUser
Activate
Yes
Amazon WorkDocs
DeactivateUser
Delete
Yes
Amazon WorkDocs
DescribeFolderContents
View
Yes
Amazon WorkDocs
DeleteFolderContents
Delete
Yes
Amazon WorkDocs
CreateFolder
Create
Yes
Amazon WorkDocs
InitiateDocumentVersionUpload
Create
Yes
Amazon WorkDocs
UpdateFolder
Edit
Yes
Amazon WorkDocs
GetFolder
View
Yes
Amazon WorkDocs
DeleteFolder
Delete
Yes
Amazon WorkDocs
GetFolderPath
View
Yes
Amazon WorkDocs
AddResourcePermissions
Create
Yes
Amazon WorkDocs
RemoveAllResourcePermissions
Delete
Yes
Amazon WorkDocs
DescribeResourcePermissions
View
Yes
Amazon WorkDocs
DescribeComments
View
Yes
Amazon WorkDocs
UpdateDocument
Edit
Yes
Amazon WorkDocs
GetDocument
View
Yes
Amazon WorkDocs
DeleteDocument
Delete
Yes
Amazon WorkDocs
DescribeActivities
View
Yes
Amazon WorkDocs
DeleteComment
Delete
Yes
Amazon WorkDocs
CreateUser
Create
Yes
Amazon WorkDocs
DescribeUsers
View
Yes
Amazon WorkDocs
DescribeRootFolders
View
Yes
Amazon WorkDocs
UpdateUser
Edit
Yes
Amazon WorkDocs
DeleteUser
Delete
Yes
Amazon WorkDocs
DescribeGroups
View
Yes
Amazon WorkDocs
DeleteNotificationSubscription
Delete
Yes
Amazon WorkDocs
GetDocumentPath
View
Yes
Amazon WorkSpaces
ModifyWorkspaceAccessProperties
Edit
API Only
Amazon WorkSpaces
ListAvailableManagementCidrRanges
View
API Only
Amazon WorkSpaces
AssociateIpGroups
Create
API Only
Amazon WorkSpaces
StopWorkspaces
Stop
API Only
Amazon WorkSpaces
ModifyWorkspaceCreationProperties
Edit
API Only
Amazon WorkSpaces
DescribeClientProperties
View
API Only
Amazon WorkSpaces
UpdateWorkspaceBundle
Edit
API Only
Amazon WorkSpaces
DisassociateIpGroups
Delete
API Only
Amazon WorkSpaces
DescribeWorkspaceImagePermissions
View
API Only
Amazon WorkSpaces
DescribeWorkspaceImages
View
API Only
Amazon WorkSpaces
CreateIpGroup
Create
API Only
Amazon WorkSpaces
AssociateConnectionAlias
Create
API Only
Amazon WorkSpaces
AuthorizeIpRules
Create
API Only
Amazon WorkSpaces
DisassociateConnectionAlias
Delete
API Only
Amazon WorkSpaces
MigrateWorkspace
Create
API Only
Amazon WorkSpaces
ModifySelfservicePermissions
Edit
API Only
Amazon WorkSpaces
CreateTags
Create
API Only
Amazon WorkSpaces
CreateWorkspaces
Create
API Only
Amazon WorkSpaces
DescribeWorkspaces
View
API Only
Amazon WorkSpaces
DeleteWorkspaceImage
Delete
API Only
Amazon WorkSpaces
DescribeIpGroups
View
API Only
Amazon WorkSpaces
UpdateRulesOfIpGroup
Edit
API Only
Amazon WorkSpaces
CreateWorkspaceBundle
Create
API Only
Amazon WorkSpaces
DeleteTags
Delete
API Only
Amazon WorkSpaces
DeleteConnectionAlias
Delete
API Only
Amazon WorkSpaces
CopyWorkspaceImage
Copy
API Only
Amazon WorkSpaces
DescribeWorkspaceSnapshots
View
API Only
Amazon WorkSpaces
RegisterWorkspaceDirectory
Register
API Only
Amazon WorkSpaces
RevokeIpRules
Delete
API Only
Amazon WorkSpaces
ModifyAccount
Edit
API Only
Amazon WorkSpaces
ModifyWorkspaceProperties
Edit
API Only
Amazon WorkSpaces
ModifyClientProperties
Edit
API Only
Amazon WorkSpaces
DescribeTags
View
API Only
Amazon WorkSpaces
StartWorkspaces
Start
API Only
Amazon WorkSpaces
DescribeWorkspaceDirectories
View
API Only
Amazon WorkSpaces
DeleteWorkspaceBundle
Delete
API Only
Amazon WorkSpaces
UpdateWorkspaceImagePermission
Edit
API Only
Amazon WorkSpaces
RebootWorkspaces
Reboot
API Only
Amazon WorkSpaces
TerminateWorkspaces
Terminate
API Only
Amazon WorkSpaces
ImportWorkspaceImage
Create
API Only
Amazon WorkSpaces
DeleteIpGroup
Delete
API Only
Amazon WorkSpaces
UpdateConnectionAliasPermission
Edit
API Only
Amazon WorkSpaces
RestoreWorkspace
Create
API Only
Amazon WorkSpaces
DescribeAccount
View
API Only
Amazon WorkSpaces
DescribeAccountModifications
View
API Only
Amazon WorkSpaces
ModifyWorkspaceState
Edit
API Only
Amazon WorkSpaces
DescribeWorkspaceBundles
View
API Only
Amazon WorkSpaces
DescribeConnectionAliases
View
API Only
Amazon WorkSpaces
DescribeConnectionAliasPermissions
View
API Only
Amazon WorkSpaces
DescribeWorkspacesConnectionStatus
View
API Only
Amazon WorkSpaces
RebuildWorkspaces
Create
API Only
Amazon WorkSpaces
CreateConnectionAlias
Create
API Only
Amazon WorkSpaces
DeregisterWorkspaceDirectory
Deregister
API Only
Amazon IoT SiteWise
AssociateAssets
Create
Yes
Amazon IoT SiteWise
AssociateProjectAssets
Create
Yes
Amazon IoT SiteWise
DisassociateProjectAssets
Delete
Yes
Amazon IoT SiteWise
PutAssetPropertyValue
Edit
Yes
Amazon IoT SiteWise
CreateAccessPolicy
Create
Yes
Amazon IoT SiteWise
ListAccessPolicies
View
Yes
Amazon IoT SiteWise
CreateAsset
Create
Yes
Amazon IoT SiteWise
ListAssets
View
Yes
Amazon IoT SiteWise
CreateAssetModel
Create
Yes
Amazon IoT SiteWise
ListAssetModels
View
Yes
Amazon IoT SiteWise
CreateDashboard
Create
Yes
Amazon IoT SiteWise
CreateGateway
Create
Yes
Amazon IoT SiteWise
ListGateways
View
Yes
Amazon IoT SiteWise
CreatePortal
Create
Yes
Amazon IoT SiteWise
ListPortals
View
Yes
Amazon IoT SiteWise
CreateProject
Create
Yes
Amazon IoT SiteWise
DeleteAccessPolicy
Delete
Yes
Amazon IoT SiteWise
DescribeAccessPolicy
View
Yes
Amazon IoT SiteWise
UpdateAccessPolicy
Edit
Yes
Amazon IoT SiteWise
DeleteAsset
Delete
Yes
Amazon IoT SiteWise
DescribeAsset
View
Yes
Amazon IoT SiteWise
UpdateAsset
Edit
Yes
Amazon IoT SiteWise
DeleteAssetModel
Delete
Yes
Amazon IoT SiteWise
DescribeAssetModel
View
Yes
Amazon IoT SiteWise
UpdateAssetModel
Edit
Yes
Amazon IoT SiteWise
DeleteDashboard
Delete
Yes
Amazon IoT SiteWise
DescribeDashboard
View
Yes
Amazon IoT SiteWise
UpdateDashboard
Edit
Yes
Amazon IoT SiteWise
DeleteGateway
Delete
Yes
Amazon IoT SiteWise
DescribeGateway
View
Yes
Amazon IoT SiteWise
UpdateGateway
Edit
Yes
Amazon IoT SiteWise
DeletePortal
Delete
Yes
Amazon IoT SiteWise
DescribePortal
View
Yes
Amazon IoT SiteWise
UpdatePortal
Edit
Yes
Amazon IoT SiteWise
DeleteProject
Delete
Yes
Amazon IoT SiteWise
DescribeProject
View
Yes
Amazon IoT SiteWise
UpdateProject
Edit
Yes
Amazon IoT SiteWise
DescribeAssetProperty
View
Yes
Amazon IoT SiteWise
UpdateAssetProperty
Edit
Yes
Amazon IoT SiteWise
DescribeDefaultEncryptionConfiguration
View
Yes
Amazon IoT SiteWise
PutDefaultEncryptionConfiguration
Edit
Yes
Amazon IoT SiteWise
DescribeGatewayCapabilityConfiguration
View
Yes
Amazon IoT SiteWise
DescribeLoggingOptions
View
Yes
Amazon IoT SiteWise
PutLoggingOptions
Edit
Yes
Amazon IoT SiteWise
DescribeStorageConfiguration
View
Yes
Amazon IoT SiteWise
PutStorageConfiguration
Edit
Yes
Amazon IoT SiteWise
DisassociateAssets
Delete
Yes
Amazon IoT SiteWise
GetAssetPropertyAggregates
View
Yes
Amazon IoT SiteWise
GetAssetPropertyValue
View
Yes
Amazon IoT SiteWise
GetAssetPropertyValueHistory
View
Yes
Amazon IoT SiteWise
GetInterpolatedAssetPropertyValues
View
Yes
Amazon IoT SiteWise
ListAssetRelationships
View
Yes
Amazon IoT SiteWise
ListAssociatedAssets
View
Yes
Amazon IoT SiteWise
ListDashboards
View
Yes
Amazon IoT SiteWise
ListProjectAssets
View
Yes
Amazon IoT SiteWise
ListProjects
View
Yes
Amazon IoT SiteWise
ListTagsForResource
View
Yes
Amazon IoT SiteWise
TagResource
Create
Yes
Amazon IoT SiteWise
UntagResource
Delete
Yes
Amazon IoT SiteWise
UpdateGatewayCapabilityConfiguration
Edit
Yes
Amazon Elemental MediaPackage
ConfigureLogs
Edit
Yes
Amazon Elemental MediaPackage
CreateChannel
Create
Yes
Amazon Elemental MediaPackage
ListChannels
View
Yes
Amazon Elemental MediaPackage
CreateHarvestJob
Create
Yes
Amazon Elemental MediaPackage
ListHarvestJobs
View
Yes
Amazon Elemental MediaPackage
CreateOriginEndpoint
Create
Yes
Amazon Elemental MediaPackage
ListOriginEndpoints
View
Yes
Amazon Elemental MediaPackage
DeleteChannel
Delete
Yes
Amazon Elemental MediaPackage
DescribeChannel
View
Yes
Amazon Elemental MediaPackage
UpdateChannel
Edit
Yes
Amazon Elemental MediaPackage
DeleteOriginEndpoint
Delete
Yes
Amazon Elemental MediaPackage
DescribeOriginEndpoint
View
Yes
Amazon Elemental MediaPackage
UpdateOriginEndpoint
Edit
Yes
Amazon Elemental MediaPackage
DescribeHarvestJob
View
Yes
Amazon Elemental MediaPackage
ListTagsForResource
View
Yes
Amazon Elemental MediaPackage
TagResource
Create
Yes
Amazon Elemental MediaPackage
RotateChannelCredentials
Edit
Yes
Amazon Elemental MediaPackage
RotateIngestEndpointCredentials
Edit
Yes
Amazon Elemental MediaPackage
UntagResource
Delete
Yes
Amazon Cognito Identity
CreateIdentityPool
Create
Yes
Amazon Cognito Identity
DeleteIdentities
Delete
Yes
Amazon Cognito Identity
DeleteIdentityPool
Delete
Yes
Amazon Cognito Identity
DescribeIdentity
View
Yes
Amazon Cognito Identity
DescribeIdentityPool
View
Yes
Amazon Cognito Identity
GetCredentialsForIdentity
View
Yes
Amazon Cognito Identity
GetId
View
Yes
Amazon Cognito Identity
GetIdentityPoolRoles
View
Yes
Amazon Cognito Identity
GetOpenIdToken
View
Yes
Amazon Cognito Identity
GetOpenIdTokenForDeveloperIdentity
View
Yes
Amazon Cognito Identity
GetPrincipalTagAttributeMap
View
Yes
Amazon Cognito Identity
ListIdentities
View
Yes
Amazon Cognito Identity
ListIdentityPools
View
Yes
Amazon Cognito Identity
ListTagsForResource
View
Yes
Amazon Cognito Identity
LookupDeveloperIdentity
Create
Yes
Amazon Cognito Identity
MergeDeveloperIdentities
Create
Yes
Amazon Cognito Identity
SetIdentityPoolRoles
Create
Yes
Amazon Cognito Identity
SetPrincipalTagAttributeMap
Create
Yes
Amazon Cognito Identity
TagResource
Create
Yes
Amazon Cognito Identity
UnlinkDeveloperIdentity
Create
Yes
Amazon Cognito Identity
UnlinkIdentity
Create
Yes
Amazon Cognito Identity
UntagResource
Delete
Yes
Amazon Cognito Identity
UpdateIdentityPool
Edit
Yes
Amazon Compute Optimizer
DescribeRecommendationExportJobs
View
Yes
Amazon Compute Optimizer
ExportAutoScalingGroupRecommendations
View
Yes
Amazon Compute Optimizer
ExportEBSVolumeRecommendations
View
Yes
Amazon Compute Optimizer
ExportECInstanceRecommendations
View
Yes
Amazon Compute Optimizer
ExportLambdaFunctionRecommendations
View
Yes
Amazon Compute Optimizer
GetAutoScalingGroupRecommendations
View
Yes
Amazon Compute Optimizer
GetEBSVolumeRecommendations
View
Yes
Amazon Compute Optimizer
GetECInstanceRecommendations
View
Yes
Amazon Compute Optimizer
GetECRecommendationProjectedMetrics
View
Yes
Amazon Compute Optimizer
GetEnrollmentStatus
View
Yes
Amazon Compute Optimizer
GetEnrollmentStatusesForOrganization
View
Yes
Amazon Compute Optimizer
GetLambdaFunctionRecommendations
View
Yes
Amazon Compute Optimizer
GetRecommendationSummaries
View
Yes
Amazon Compute Optimizer
UpdateEnrollmentStatus
Edit
Yes
Amazon SecurityHub
AcceptAdministratorInvitation
Approve
Yes
Amazon SecurityHub
GetAdministratorAccount
View
Yes
Amazon SecurityHub
AcceptInvitation
Approve
Yes
Amazon SecurityHub
GetMasterAccount
View
Yes
Amazon SecurityHub
DisableStandards
Edit
Yes
Amazon SecurityHub
EnableStandards
Enable
Yes
Amazon SecurityHub
ImportFindings
Create
Yes
Amazon SecurityHub
UpdateFindings
Edit
Yes
Amazon SecurityHub
CreateActionTarget
Create
Yes
Amazon SecurityHub
CreateInsight
Create
Yes
Amazon SecurityHub
CreateMembers
Create
Yes
Amazon SecurityHub
ListMembers
View
Yes
Amazon SecurityHub
DeclineInvitations
Create
Yes
Amazon SecurityHub
DeleteActionTarget
Delete
Yes
Amazon SecurityHub
UpdateActionTarget
Edit
Yes
Amazon SecurityHub
DeleteInsight
Delete
Yes
Amazon SecurityHub
UpdateInsight
Edit
Yes
Amazon SecurityHub
DeleteInvitations
Delete
Yes
Amazon SecurityHub
DeleteMembers
Delete
Yes
Amazon SecurityHub
DescribeActionTargets
View
Yes
Amazon SecurityHub
DescribeHub
View
Yes
Amazon SecurityHub
DisableSecurityHub
Delete
Yes
Amazon SecurityHub
EnableSecurityHub
Enable
Yes
Amazon SecurityHub
UpdateSecurityHubConfiguration
Edit
Yes
Amazon SecurityHub
DescribeOrganizationConfiguration
View
Yes
Amazon SecurityHub
UpdateOrganizationConfiguration
Edit
Yes
Amazon SecurityHub
DescribeProducts
View
Yes
Amazon SecurityHub
DescribeStandards
View
Yes
Amazon SecurityHub
DescribeStandardsControls
View
Yes
Amazon SecurityHub
DisableImportFindingsForProduct
Delete
Yes
Amazon SecurityHub
DisableOrganizationAdminAccount
Edit
Yes
Amazon SecurityHub
DisassociateFromAdministratorAccount
Delete
Yes
Amazon SecurityHub
DisassociateFromMasterAccount
Delete
Yes
Amazon SecurityHub
DisassociateMembers
Delete
Yes
Amazon SecurityHub
EnableImportFindingsForProduct
Enable
Yes
Amazon SecurityHub
ListEnabledProductsForImport
View
Yes
Amazon SecurityHub
EnableOrganizationAdminAccount
Enable
Yes
Amazon SecurityHub
GetEnabledStandards
View
Yes
Amazon SecurityHub
GetFindings
View
Yes
Amazon SecurityHub
GetInsightResults
View
Yes
Amazon SecurityHub
GetInsights
View
Yes
Amazon SecurityHub
GetInvitationsCount
View
Yes
Amazon SecurityHub
GetMembers
View
Yes
Amazon SecurityHub
InviteMembers
Create
Yes
Amazon SecurityHub
ListInvitations
View
Yes
Amazon SecurityHub
ListOrganizationAdminAccounts
View
Yes
Amazon SecurityHub
ListTagsForResource
View
Yes
Amazon SecurityHub
TagResource
Create
Yes
Amazon SecurityHub
UntagResource
Delete
Yes
Amazon SecurityHub
UpdateStandardsControl
Edit
Yes
Amazon Fraud Detector
CreateVariable
Create
Yes
Amazon Fraud Detector
GetVariable
View
Yes
Amazon Fraud Detector
CancelPredictionJob
Delete
Yes
Amazon Fraud Detector
CreatePredictionJob
Create
Yes
Amazon Fraud Detector
CreateDetectorVersion
Create
Yes
Amazon Fraud Detector
CreateModel
Create
Yes
Amazon Fraud Detector
CreateModelVersion
Create
Yes
Amazon Fraud Detector
CreateRule
Create
Yes
Amazon Fraud Detector
DeletePredictionJob
Delete
Yes
Amazon Fraud Detector
DeleteDetector
Delete
Yes
Amazon Fraud Detector
DeleteDetectorVersion
Delete
Yes
Amazon Fraud Detector
DeleteEntityType
Delete
Yes
Amazon Fraud Detector
DeleteEvent
Delete
Yes
Amazon Fraud Detector
DeleteEventType
Delete
Yes
Amazon Fraud Detector
DeleteExternalModel
Delete
Yes
Amazon Fraud Detector
DeleteLabel
Delete
Yes
Amazon Fraud Detector
DeleteModel
Delete
Yes
Amazon Fraud Detector
DeleteModelVersion
Delete
Yes
Amazon Fraud Detector
DeleteOutcome
Delete
Yes
Amazon Fraud Detector
DeleteRule
Delete
Yes
Amazon Fraud Detector
DeleteVariable
Delete
Yes
Amazon Fraud Detector
DescribeDetector
View
Yes
Amazon Fraud Detector
DescribeModelVersions
View
Yes
Amazon Fraud Detector
GetPredictionJobs
View
Yes
Amazon Fraud Detector
GetDetectorVersion
View
Yes
Amazon Fraud Detector
GetDetectors
View
Yes
Amazon Fraud Detector
GetEntityTypes
View
Yes
Amazon Fraud Detector
GetEventPrediction
View
Yes
Amazon Fraud Detector
GetEventTypes
View
Yes
Amazon Fraud Detector
GetExternalModels
View
Yes
Amazon Fraud Detector
GetKMSEncryptionKey
View
Yes
Amazon Fraud Detector
GetLabels
View
Yes
Amazon Fraud Detector
GetModelVersion
View
Yes
Amazon Fraud Detector
GetModels
View
Yes
Amazon Fraud Detector
GetOutcomes
View
Yes
Amazon Fraud Detector
GetRules
View
Yes
Amazon Fraud Detector
GetVariables
View
Yes
Amazon Fraud Detector
ListTagsForResource
View
Yes
Amazon Fraud Detector
PutDetector
Edit
Yes
Amazon Fraud Detector
PutEntityType
Edit
Yes
Amazon Fraud Detector
PutEventType
Edit
Yes
Amazon Fraud Detector
PutExternalModel
Edit
Yes
Amazon Fraud Detector
PutKMSEncryptionKey
Edit
Yes
Amazon Fraud Detector
PutLabel
Edit
Yes
Amazon Fraud Detector
PutOutcome
Edit
Yes
Amazon Fraud Detector
TagResource
Create
Yes
Amazon Fraud Detector
UntagResource
Delete
Yes
Amazon Fraud Detector
UpdateDetectorVersion
Edit
Yes
Amazon Fraud Detector
UpdateDetectorVersionMetadata
Edit
Yes
Amazon Fraud Detector
UpdateDetectorVersionStatus
Edit
Yes
Amazon Fraud Detector
UpdateModel
Edit
Yes
Amazon Fraud Detector
UpdateModelVersion
Edit
Yes
Amazon Fraud Detector
UpdateModelVersionStatus
Edit
Yes
Amazon Fraud Detector
UpdateRuleMetadata
Edit
Yes
Amazon Fraud Detector
UpdateRuleVersion
Edit
Yes
Amazon Fraud Detector
UpdateVariable
Edit
Yes
Amazon Application Migration Service
ChangeServerLifeCycleState
Create
Yes
Amazon Application Migration Service
CreateReplicationConfigurationTemplate
Create
Yes
Amazon Application Migration Service
DeleteJob
Delete
Yes
Amazon Application Migration Service
DeleteReplicationConfigurationTemplate
Delete
Yes
Amazon Application Migration Service
DeleteSourceServer
Delete
Yes
Amazon Application Migration Service
DescribeJobLogItems
View
Yes
Amazon Application Migration Service
DescribeJobs
View
Yes
Amazon Application Migration Service
DescribeReplicationConfigurationTemplates
View
Yes
Amazon Application Migration Service
DescribeSourceServers
View
Yes
Amazon Application Migration Service
DisconnectFromService
Create
Yes
Amazon Application Migration Service
FinalizeCutover
Create
Yes
Amazon Application Migration Service
GetLaunchConfiguration
View
Yes
Amazon Application Migration Service
GetReplicationConfiguration
View
Yes
Amazon Application Migration Service
InitializeService
Create
Yes
Amazon Application Migration Service
ListTagsForResource
View
Yes
Amazon Application Migration Service
TagResource
Create
Yes
Amazon Application Migration Service
MarkAsArchived
Create
Yes
Amazon Application Migration Service
RetryDataReplication
Create
Yes
Amazon Application Migration Service
StartCutover
Start
Yes
Amazon Application Migration Service
StartTest
Start
Yes
Amazon Application Migration Service
TerminateTargetInstances
Terminate
Yes
Amazon Application Migration Service
UntagResource
Delete
Yes
Amazon Application Migration Service
UpdateLaunchConfiguration
Edit
Yes
Amazon Application Migration Service
UpdateReplicationConfiguration
Edit
Yes
Amazon Application Migration Service
UpdateReplicationConfigurationTemplate
Edit
Yes
Amazon Snow Device Management
CancelTask
Delete
Yes
Amazon Snow Device Management
CreateTask
Create
Yes
Amazon Snow Device Management
DescribeDevice
View
Yes
Amazon Snow Device Management
DescribeDeviceEcInstances
View
Yes
Amazon Snow Device Management
DescribeExecution
View
Yes
Amazon Snow Device Management
DescribeTask
View
Yes
Amazon Snow Device Management
ListDeviceResources
View
Yes
Amazon Snow Device Management
ListDevices
View
Yes
Amazon Snow Device Management
ListExecutions
View
Yes
Amazon Snow Device Management
ListTagsForResource
View
Yes
Amazon Snow Device Management
TagResource
Create
Yes
Amazon Snow Device Management
ListTasks
View
Yes
Amazon Snow Device Management
UntagResource
Delete
Yes
Amazon IoT Things Graph
AssociateEntityToThing
Create
Yes
Amazon IoT Things Graph
CreateFlowTemplate
Create
Yes
Amazon IoT Things Graph
CreateSystemInstance
Create
Yes
Amazon IoT Things Graph
CreateSystemTemplate
Create
Yes
Amazon IoT Things Graph
DeleteFlowTemplate
Delete
Yes
Amazon IoT Things Graph
DeleteNamespace
Delete
Yes
Amazon IoT Things Graph
DeleteSystemInstance
Delete
Yes
Amazon IoT Things Graph
DeleteSystemTemplate
Delete
Yes
Amazon IoT Things Graph
DeploySystemInstance
Create
Yes
Amazon IoT Things Graph
DeprecateFlowTemplate
Delete
Yes
Amazon IoT Things Graph
DeprecateSystemTemplate
Delete
Yes
Amazon IoT Things Graph
DescribeNamespace
View
Yes
Amazon IoT Things Graph
DissociateEntityFromThing
Create
Yes
Amazon IoT Things Graph
GetEntities
View
Yes
Amazon IoT Things Graph
GetFlowTemplate
View
Yes
Amazon IoT Things Graph
GetFlowTemplateRevisions
View
Yes
Amazon IoT Things Graph
GetNamespaceDeletionStatus
View
Yes
Amazon IoT Things Graph
GetSystemInstance
View
Yes
Amazon IoT Things Graph
GetSystemTemplate
View
Yes
Amazon IoT Things Graph
GetSystemTemplateRevisions
View
Yes
Amazon IoT Things Graph
GetUploadStatus
View
Yes
Amazon IoT Things Graph
ListFlowExecutionMessages
View
Yes
Amazon IoT Things Graph
ListTagsForResource
View
Yes
Amazon IoT Things Graph
SearchEntities
Search
Yes
Amazon IoT Things Graph
SearchFlowExecutions
Search
Yes
Amazon IoT Things Graph
SearchFlowTemplates
Search
Yes
Amazon IoT Things Graph
SearchSystemInstances
Search
Yes
Amazon IoT Things Graph
SearchSystemTemplates
Search
Yes
Amazon IoT Things Graph
SearchThings
Search
Yes
Amazon IoT Things Graph
TagResource
Create
Yes
Amazon IoT Things Graph
UndeploySystemInstance
Create
Yes
Amazon IoT Things Graph
UntagResource
Delete
Yes
Amazon IoT Things Graph
UpdateFlowTemplate
Edit
Yes
Amazon IoT Things Graph
UpdateSystemTemplate
Edit
Yes
Amazon IoT Things Graph
UploadEntityDefinitions
Upload
Yes
Amazon Storage Gateway
ActivateGateway
Activate
Yes
Amazon Storage Gateway
AddCache
Create
Yes
Amazon Storage Gateway
AddTagsToResource
Create
Yes
Amazon Storage Gateway
AddUploadBuffer
Create
Yes
Amazon Storage Gateway
AddWorkingStorage
Create
Yes
Amazon Storage Gateway
AssignTapePool
Create
Yes
Amazon Storage Gateway
AssociateFileSystem
Create
Yes
Amazon Storage Gateway
AttachVolume
Attach
Yes
Amazon Storage Gateway
CancelArchival
Delete
Yes
Amazon Storage Gateway
CancelRetrieval
Delete
Yes
Amazon Storage Gateway
CreateCachediSCSIVolume
Create
Yes
Amazon Storage Gateway
CreateNFSFileShare
Create
Yes
Amazon Storage Gateway
CreateSMBFileShare
Create
Yes
Amazon Storage Gateway
CreateSnapshot
Create
Yes
Amazon Storage Gateway
CreateSnapshotFromVolumeRecoveryPoint
Create
Yes
Amazon Storage Gateway
CreateStorediSCSIVolume
Create
Yes
Amazon Storage Gateway
CreateTapePool
Create
Yes
Amazon Storage Gateway
CreateTapeWithBarcode
Create
Yes
Amazon Storage Gateway
CreateTapes
Create
Yes
Amazon Storage Gateway
DeleteAutomaticTapeCreationPolicy
Delete
Yes
Amazon Storage Gateway
DeleteBandwidthRateLimit
Delete
Yes
Amazon Storage Gateway
DeleteChapCredentials
Delete
Yes
Amazon Storage Gateway
DeleteFileShare
Delete
Yes
Amazon Storage Gateway
DeleteGateway
Delete
Yes
Amazon Storage Gateway
DeleteSnapshotSchedule
Delete
Yes
Amazon Storage Gateway
DeleteTape
Delete
Yes
Amazon Storage Gateway
DeleteTapeArchive
Delete
Yes
Amazon Storage Gateway
DeleteTapePool
Delete
Yes
Amazon Storage Gateway
DeleteVolume
Delete
Yes
Amazon Storage Gateway
DescribeAvailabilityMonitorTest
View
Yes
Amazon Storage Gateway
DescribeBandwidthRateLimit
View
Yes
Amazon Storage Gateway
DescribeBandwidthRateLimitSchedule
View
Yes
Amazon Storage Gateway
DescribeCache
View
Yes
Amazon Storage Gateway
DescribeCachediSCSIVolumes
View
Yes
Amazon Storage Gateway
DescribeChapCredentials
View
Yes
Amazon Storage Gateway
DescribeFileSystemAssociations
View
Yes
Amazon Storage Gateway
DescribeGatewayInformation
View
Yes
Amazon Storage Gateway
DescribeMaintenanceStartTime
View
Yes
Amazon Storage Gateway
DescribeNFSFileShares
View
Yes
Amazon Storage Gateway
DescribeSMBFileShares
View
Yes
Amazon Storage Gateway
DescribeSMBSettings
View
Yes
Amazon Storage Gateway
DescribeSnapshotSchedule
View
Yes
Amazon Storage Gateway
DescribeStorediSCSIVolumes
View
Yes
Amazon Storage Gateway
DescribeTapeArchives
View
Yes
Amazon Storage Gateway
DescribeTapeRecoveryPoints
View
Yes
Amazon Storage Gateway
DescribeTapes
View
Yes
Amazon Storage Gateway
DescribeUploadBuffer
View
Yes
Amazon Storage Gateway
DescribeVTLDevices
View
Yes
Amazon Storage Gateway
DescribeWorkingStorage
View
Yes
Amazon Storage Gateway
DetachVolume
Delete
Yes
Amazon Storage Gateway
DisableGateway
Edit
Yes
Amazon Storage Gateway
DisassociateFileSystem
Delete
Yes
Amazon Storage Gateway
JoinDomain
Create
Yes
Amazon Storage Gateway
ListAutomaticTapeCreationPolicies
View
Yes
Amazon Storage Gateway
ListFileShares
View
Yes
Amazon Storage Gateway
ListFileSystemAssociations
View
Yes
Amazon Storage Gateway
ListGateways
View
Yes
Amazon Storage Gateway
ListLocalDisks
View
Yes
Amazon Storage Gateway
ListTagsForResource
View
Yes
Amazon Storage Gateway
ListTapePools
View
Yes
Amazon Storage Gateway
ListTapes
View
Yes
Amazon Storage Gateway
ListVolumeInitiators
View
Yes
Amazon Storage Gateway
ListVolumeRecoveryPoints
View
Yes
Amazon Storage Gateway
ListVolumes
View
Yes
Amazon Storage Gateway
NotifyWhenUploaded
Create
Yes
Amazon Storage Gateway
RefreshCache
Create
Yes
Amazon Storage Gateway
RemoveTagsFromResource
Delete
Yes
Amazon Storage Gateway
ResetCache
Edit
Yes
Amazon Storage Gateway
RetrieveTapeArchive
View
Yes
Amazon Storage Gateway
RetrieveTapeRecoveryPoint
View
Yes
Amazon Storage Gateway
SetLocalConsolePassword
Create
Yes
Amazon Storage Gateway
SetSMBGuestPassword
Create
Yes
Amazon Storage Gateway
ShutdownGateway
Stop
Yes
Amazon Storage Gateway
StartAvailabilityMonitorTest
Start
Yes
Amazon Storage Gateway
StartGateway
Start
Yes
Amazon Storage Gateway
UpdateAutomaticTapeCreationPolicy
Edit
Yes
Amazon Storage Gateway
UpdateBandwidthRateLimit
Edit
Yes
Amazon Storage Gateway
UpdateBandwidthRateLimitSchedule
Edit
Yes
Amazon Storage Gateway
UpdateChapCredentials
Edit
Yes
Amazon Storage Gateway
UpdateFileSystemAssociation
Edit
Yes
Amazon Storage Gateway
UpdateGatewayInformation
Edit
Yes
Amazon Storage Gateway
UpdateGatewaySoftwareNow
Edit
Yes
Amazon Storage Gateway
UpdateMaintenanceStartTime
Edit
Yes
Amazon Storage Gateway
UpdateNFSFileShare
Edit
Yes
Amazon Storage Gateway
UpdateSMBFileShare
Edit
Yes
Amazon Storage Gateway
UpdateSMBFileShareVisibility
Edit
Yes
Amazon Storage Gateway
UpdateSMBSecurityStrategy
Edit
Yes
Amazon Storage Gateway
UpdateSnapshotSchedule
Edit
Yes
Amazon Storage Gateway
UpdateVTLDeviceType
Edit
Yes
Amazon Personalize Runtime
GetPersonalizedRanking
View
Yes
Amazon Personalize Runtime
GetRecommendations
View
Yes
Amazon Cloud9
CreateEnvironmentEC
Create
Yes
Amazon Cloud9
CreateEnvironmentMembership
Create
Yes
Amazon Cloud9
DeleteEnvironment
Delete
Yes
Amazon Cloud9
DeleteEnvironmentMembership
Delete
Yes
Amazon Cloud9
DescribeEnvironmentMemberships
View
Yes
Amazon Cloud9
DescribeEnvironmentStatus
View
Yes
Amazon Cloud9
DescribeEnvironments
View
Yes
Amazon Cloud9
ListEnvironments
View
Yes
Amazon Cloud9
ListTagsForResource
View
Yes
Amazon Cloud9
TagResource
Create
Yes
Amazon Cloud9
UntagResource
Delete
Yes
Amazon Cloud9
UpdateEnvironment
Edit
Yes
Amazon Cloud9
UpdateEnvironmentMembership
Edit
Yes
Amazon S3 Control
CreateAccessPoint
Create
Yes
Amazon S3 Control
DeleteAccessPoint
Delete
Yes
Amazon S3 Control
GetAccessPoint
View
Yes
Amazon S3 Control
CreateAccessPointForObjectLambda
Create
Yes
Amazon S3 Control
DeleteAccessPointForObjectLambda
Delete
Yes
Amazon S3 Control
GetAccessPointForObjectLambda
View
Yes
Amazon S3 Control
CreateBucket
Create
Yes
Amazon S3 Control
CreateJob
Create
Yes
Amazon S3 Control
ListJobs
View
Yes
Amazon S3 Control
CreateMultiRegionAccessPoint
Create
Yes
Amazon S3 Control
DeleteAccessPointPolicy
Delete
Yes
Amazon S3 Control
GetAccessPointPolicy
View
Yes
Amazon S3 Control
PutAccessPointPolicy
Edit
Yes
Amazon S3 Control
DeleteAccessPointPolicyForObjectLambda
Delete
Yes
Amazon S3 Control
GetAccessPointPolicyForObjectLambda
View
Yes
Amazon S3 Control
PutAccessPointPolicyForObjectLambda
Edit
Yes
Amazon S3 Control
DeleteBucket
Delete
Yes
Amazon S3 Control
GetBucket
View
Yes
Amazon S3 Control
DeleteBucketLifecycleConfiguration
Delete
Yes
Amazon S3 Control
GetBucketLifecycleConfiguration
View
Yes
Amazon S3 Control
PutBucketLifecycleConfiguration
Edit
Yes
Amazon S3 Control
DeleteBucketPolicy
Delete
Yes
Amazon S3 Control
GetBucketPolicy
View
Yes
Amazon S3 Control
PutBucketPolicy
Edit
Yes
Amazon S3 Control
DeleteBucketTagging
Delete
Yes
Amazon S3 Control
GetBucketTagging
View
Yes
Amazon S3 Control
PutBucketTagging
Edit
Yes
Amazon S3 Control
DeleteJobTagging
Delete
Yes
Amazon S3 Control
GetJobTagging
View
Yes
Amazon S3 Control
PutJobTagging
Edit
Yes
Amazon S3 Control
DeleteMultiRegionAccessPoint
Delete
Yes
Amazon S3 Control
DeletePublicAccessBlock
Delete
Yes
Amazon S3 Control
GetPublicAccessBlock
View
Yes
Amazon S3 Control
PutPublicAccessBlock
Edit
Yes
Amazon S3 Control
DeleteStorageLensConfiguration
Delete
Yes
Amazon S3 Control
GetStorageLensConfiguration
View
Yes
Amazon S3 Control
PutStorageLensConfiguration
Edit
Yes
Amazon S3 Control
DeleteStorageLensConfigurationTagging
Delete
Yes
Amazon S3 Control
GetStorageLensConfigurationTagging
View
Yes
Amazon S3 Control
PutStorageLensConfigurationTagging
Edit
Yes
Amazon S3 Control
DescribeJob
View
Yes
Amazon S3 Control
DescribeMultiRegionAccessPointOperation
View
Yes
Amazon S3 Control
GetAccessPointConfigurationForObjectLambda
View
Yes
Amazon S3 Control
PutAccessPointConfigurationForObjectLambda
Edit
Yes
Amazon S3 Control
GetAccessPointPolicyStatus
View
Yes
Amazon S3 Control
GetAccessPointPolicyStatusForObjectLambda
View
Yes
Amazon S3 Control
GetMultiRegionAccessPoint
View
Yes
Amazon S3 Control
GetMultiRegionAccessPointPolicy
View
Yes
Amazon S3 Control
GetMultiRegionAccessPointPolicyStatus
View
Yes
Amazon S3 Control
ListAccessPoints
View
Yes
Amazon S3 Control
ListAccessPointsForObjectLambda
View
Yes
Amazon S3 Control
ListMultiRegionAccessPoints
View
Yes
Amazon S3 Control
ListRegionalBuckets
View
Yes
Amazon S3 Control
ListStorageLensConfigurations
View
Yes
Amazon S3 Control
PutMultiRegionAccessPointPolicy
Edit
Yes
Amazon S3 Control
UpdateJobPriority
Edit
Yes
Amazon S3 Control
UpdateJobStatus
Edit
Yes
Amazon Well-Architected Tool
AssociateLenses
Create
Yes
Amazon Well-Architected Tool
CreateMilestone
Create
Yes
Amazon Well-Architected Tool
CreateWorkload
Create
Yes
Amazon Well-Architected Tool
CreateWorkloadShare
Create
Yes
Amazon Well-Architected Tool
ListWorkloadShares
View
Yes
Amazon Well-Architected Tool
DeleteWorkload
Delete
Yes
Amazon Well-Architected Tool
DeleteWorkloadShare
Delete
Yes
Amazon Well-Architected Tool
DisassociateLenses
Delete
Yes
Amazon Well-Architected Tool
GetAnswer
View
Yes
Amazon Well-Architected Tool
UpdateAnswer
Edit
Yes
Amazon Well-Architected Tool
GetLensReview
View
Yes
Amazon Well-Architected Tool
UpdateLensReview
Edit
Yes
Amazon Well-Architected Tool
GetLensReviewReport
View
Yes
Amazon Well-Architected Tool
GetLensVersionDifference
View
Yes
Amazon Well-Architected Tool
GetMilestone
View
Yes
Amazon Well-Architected Tool
GetWorkload
View
Yes
Amazon Well-Architected Tool
UpdateWorkload
Edit
Yes
Amazon Well-Architected Tool
ListAnswers
View
Yes
Amazon Well-Architected Tool
ListLensReviewImprovements
View
Yes
Amazon Well-Architected Tool
ListLensReviews
View
Yes
Amazon Well-Architected Tool
ListLenses
View
Yes
Amazon Well-Architected Tool
ListMilestones
View
Yes
Amazon Well-Architected Tool
ListNotifications
View
Yes
Amazon Well-Architected Tool
ListShareInvitations
View
Yes
Amazon Well-Architected Tool
ListTagsForResource
View
Yes
Amazon Well-Architected Tool
TagResource
Create
Yes
Amazon Well-Architected Tool
ListWorkloads
View
Yes
Amazon Well-Architected Tool
UntagResource
Delete
Yes
Amazon Well-Architected Tool
UpdateShareInvitation
Edit
Yes
Amazon Well-Architected Tool
UpdateWorkloadShare
Edit
Yes
Amazon Well-Architected Tool
UpgradeLensReview
Edit
Yes
Amazon Fault Injection Simulator
CreateExperimentTemplate
Create
Yes
Amazon Fault Injection Simulator
ListExperimentTemplates
View
Yes
Amazon Fault Injection Simulator
DeleteExperimentTemplate
Delete
Yes
Amazon Fault Injection Simulator
GetExperimentTemplate
View
Yes
Amazon Fault Injection Simulator
UpdateExperimentTemplate
Edit
Yes
Amazon Fault Injection Simulator
GetAction
View
Yes
Amazon Fault Injection Simulator
GetExperiment
View
Yes
Amazon Fault Injection Simulator
StopExperiment
Delete
Yes
Amazon Fault Injection Simulator
ListActions
View
Yes
Amazon Fault Injection Simulator
ListExperiments
View
Yes
Amazon Fault Injection Simulator
StartExperiment
Start
Yes
Amazon Fault Injection Simulator
ListTagsForResource
View
Yes
Amazon Fault Injection Simulator
TagResource
Create
Yes
Amazon Fault Injection Simulator
UntagResource
Delete
Yes
Amazon DevOps Guru
AddNotificationChannel
Create
Yes
Amazon DevOps Guru
ListNotificationChannels
View
Yes
Amazon DevOps Guru
DescribeAccountHealth
View
Yes
Amazon DevOps Guru
DescribeAccountOverview
View
Yes
Amazon DevOps Guru
DescribeAnomaly
View
Yes
Amazon DevOps Guru
DescribeFeedback
View
Yes
Amazon DevOps Guru
PutFeedback
Edit
Yes
Amazon DevOps Guru
DescribeInsight
View
Yes
Amazon DevOps Guru
DescribeResourceCollectionHealth
View
Yes
Amazon DevOps Guru
DescribeServiceIntegration
View
Yes
Amazon DevOps Guru
UpdateServiceIntegration
Edit
Yes
Amazon DevOps Guru
GetCostEstimation
View
Yes
Amazon DevOps Guru
StartCostEstimation
Start
Yes
Amazon DevOps Guru
GetResourceCollection
View
Yes
Amazon DevOps Guru
ListAnomaliesForInsight
View
Yes
Amazon DevOps Guru
ListEvents
View
Yes
Amazon DevOps Guru
ListInsights
View
Yes
Amazon DevOps Guru
ListRecommendations
View
Yes
Amazon DevOps Guru
RemoveNotificationChannel
Delete
Yes
Amazon DevOps Guru
SearchInsights
Search
Yes
Amazon DevOps Guru
UpdateResourceCollection
Edit
Yes
Amazon FinSpace Public API
CreateChangeset
Create
Yes
Amazon FinSpace Public API
GetProgrammaticAccessCredentials
View
Yes
Amazon FinSpace Public API
GetWorkingLocation
View
Yes
Amazon Macie
AssociateMemberAccount
Create
Yes
Amazon Macie
AssociateSResources
Create
Yes
Amazon Macie
DisassociateMemberAccount
Delete
Yes
Amazon Macie
DisassociateSResources
Delete
Yes
Amazon Macie
ListMemberAccounts
View
Yes
Amazon Macie
ListSResources
View
Yes
Amazon Macie
UpdateSResources
Edit
Yes
Amazon Lightsail
AllocateStaticIp
Create
Yes
Amazon Lightsail
AttachCertificateToDistribution
Attach
Yes
Amazon Lightsail
AttachDisk
Attach
Yes
Amazon Lightsail
AttachInstancesToLoadBalancer
Attach
Yes
Amazon Lightsail
AttachLoadBalancerTlsCertificate
Attach
Yes
Amazon Lightsail
AttachStaticIp
Attach
Yes
Amazon Lightsail
CloseInstancePublicPorts
Create
Yes
Amazon Lightsail
CopySnapshot
Copy
Yes
Amazon Lightsail
CreateBucket
Create
Yes
Amazon Lightsail
CreateBucketAccessKey
Create
Yes
Amazon Lightsail
CreateCertificate
Create
Yes
Amazon Lightsail
CreateCloudFormationStack
Create
Yes
Amazon Lightsail
CreateContactMethod
Create
Yes
Amazon Lightsail
CreateContainerService
Create
Yes
Amazon Lightsail
CreateContainerServiceDeployment
Create
Yes
Amazon Lightsail
CreateContainerServiceRegistryLogin
Create
Yes
Amazon Lightsail
CreateDisk
Create
Yes
Amazon Lightsail
CreateDiskFromSnapshot
Create
Yes
Amazon Lightsail
CreateDiskSnapshot
Create
Yes
Amazon Lightsail
CreateDistribution
Create
Yes
Amazon Lightsail
CreateDomain
Create
Yes
Amazon Lightsail
CreateDomainEntry
Create
Yes
Amazon Lightsail
CreateInstanceSnapshot
Create
Yes
Amazon Lightsail
CreateInstances
Create
Yes
Amazon Lightsail
CreateInstancesFromSnapshot
Create
Yes
Amazon Lightsail
CreateKeyPair
Create
Yes
Amazon Lightsail
CreateLoadBalancer
Create
Yes
Amazon Lightsail
CreateLoadBalancerTlsCertificate
Create
Yes
Amazon Lightsail
CreateRelationalDatabase
Create
Yes
Amazon Lightsail
CreateRelationalDatabaseFromSnapshot
Create
Yes
Amazon Lightsail
CreateRelationalDatabaseSnapshot
Create
Yes
Amazon Lightsail
DeleteAlarm
Delete
Yes
Amazon Lightsail
DeleteAutoSnapshot
Delete
Yes
Amazon Lightsail
DeleteBucket
Delete
Yes
Amazon Lightsail
DeleteBucketAccessKey
Delete
Yes
Amazon Lightsail
DeleteCertificate
Delete
Yes
Amazon Lightsail
DeleteContactMethod
Delete
Yes
Amazon Lightsail
DeleteContainerImage
Delete
Yes
Amazon Lightsail
DeleteContainerService
Delete
Yes
Amazon Lightsail
DeleteDisk
Delete
Yes
Amazon Lightsail
DeleteDiskSnapshot
Delete
Yes
Amazon Lightsail
DeleteDistribution
Delete
Yes
Amazon Lightsail
DeleteDomain
Delete
Yes
Amazon Lightsail
DeleteDomainEntry
Delete
Yes
Amazon Lightsail
DeleteInstance
Delete
Yes
Amazon Lightsail
DeleteInstanceSnapshot
Delete
Yes
Amazon Lightsail
DeleteKeyPair
Delete
Yes
Amazon Lightsail
DeleteKnownHostKeys
Delete
Yes
Amazon Lightsail
DeleteLoadBalancer
Delete
Yes
Amazon Lightsail
DeleteLoadBalancerTlsCertificate
Delete
Yes
Amazon Lightsail
DeleteRelationalDatabase
Delete
Yes
Amazon Lightsail
DeleteRelationalDatabaseSnapshot
Delete
Yes
Amazon Lightsail
DetachCertificateFromDistribution
Delete
Yes
Amazon Lightsail
DetachDisk
Delete
Yes
Amazon Lightsail
DetachInstancesFromLoadBalancer
Delete
Yes
Amazon Lightsail
DetachStaticIp
Delete
Yes
Amazon Lightsail
DisableAddOn
Edit
Yes
Amazon Lightsail
DownloadDefaultKeyPair
Download
Yes
Amazon Lightsail
EnableAddOn
Enable
Yes
Amazon Lightsail
ExportSnapshot
View
Yes
Amazon Lightsail
GetActiveNames
View
Yes
Amazon Lightsail
GetAlarms
View
Yes
Amazon Lightsail
GetAutoSnapshots
View
Yes
Amazon Lightsail
GetBlueprints
View
Yes
Amazon Lightsail
GetBucketAccessKeys
View
Yes
Amazon Lightsail
GetBucketBundles
View
Yes
Amazon Lightsail
GetBucketMetricData
View
Yes
Amazon Lightsail
GetBuckets
View
Yes
Amazon Lightsail
GetBundles
View
Yes
Amazon Lightsail
GetCertificates
View
Yes
Amazon Lightsail
GetCloudFormationStackRecords
View
Yes
Amazon Lightsail
GetContactMethods
View
Yes
Amazon Lightsail
GetContainerAPIMetadata
View
Yes
Amazon Lightsail
GetContainerImages
View
Yes
Amazon Lightsail
GetContainerLog
View
Yes
Amazon Lightsail
GetContainerServiceDeployments
View
Yes
Amazon Lightsail
GetContainerServiceMetricData
View
Yes
Amazon Lightsail
GetContainerServicePowers
View
Yes
Amazon Lightsail
GetContainerServices
View
Yes
Amazon Lightsail
GetDisk
View
Yes
Amazon Lightsail
GetDiskSnapshot
View
Yes
Amazon Lightsail
GetDiskSnapshots
View
Yes
Amazon Lightsail
GetDisks
View
Yes
Amazon Lightsail
GetDistributionBundles
View
Yes
Amazon Lightsail
GetDistributionLatestCacheReset
View
Yes
Amazon Lightsail
GetDistributionMetricData
View
Yes
Amazon Lightsail
GetDistributions
View
Yes
Amazon Lightsail
GetDomain
View
Yes
Amazon Lightsail
GetDomains
View
Yes
Amazon Lightsail
GetExportSnapshotRecords
View
Yes
Amazon Lightsail
GetInstance
View
Yes
Amazon Lightsail
GetInstanceAccessDetails
View
Yes
Amazon Lightsail
GetInstanceMetricData
View
Yes
Amazon Lightsail
GetInstancePortStates
View
Yes
Amazon Lightsail
GetInstanceSnapshot
View
Yes
Amazon Lightsail
GetInstanceSnapshots
View
Yes
Amazon Lightsail
GetInstanceState
View
Yes
Amazon Lightsail
GetInstances
View
Yes
Amazon Lightsail
GetKeyPair
View
Yes
Amazon Lightsail
GetKeyPairs
View
Yes
Amazon Lightsail
GetLoadBalancer
View
Yes
Amazon Lightsail
GetLoadBalancerMetricData
View
Yes
Amazon Lightsail
GetLoadBalancerTlsCertificates
View
Yes
Amazon Lightsail
GetLoadBalancers
View
Yes
Amazon Lightsail
GetOperation
View
Yes
Amazon Lightsail
GetOperations
View
Yes
Amazon Lightsail
GetOperationsForResource
View
Yes
Amazon Lightsail
GetRegions
View
Yes
Amazon Lightsail
GetRelationalDatabase
View
Yes
Amazon Lightsail
GetRelationalDatabaseBlueprints
View
Yes
Amazon Lightsail
GetRelationalDatabaseBundles
View
Yes
Amazon Lightsail
GetRelationalDatabaseEvents
View
Yes
Amazon Lightsail
GetRelationalDatabaseLogEvents
View
Yes
Amazon Lightsail
GetRelationalDatabaseLogStreams
View
Yes
Amazon Lightsail
GetRelationalDatabaseMasterUserPassword
View
Yes
Amazon Lightsail
GetRelationalDatabaseMetricData
View
Yes
Amazon Lightsail
GetRelationalDatabaseParameters
View
Yes
Amazon Lightsail
GetRelationalDatabaseSnapshot
View
Yes
Amazon Lightsail
GetRelationalDatabaseSnapshots
View
Yes
Amazon Lightsail
GetRelationalDatabases
View
Yes
Amazon Lightsail
GetStaticIp
View
Yes
Amazon Lightsail
GetStaticIps
View
Yes
Amazon Lightsail
ImportKeyPair
Create
Yes
Amazon Lightsail
IsVpcPeered
Create
Yes
Amazon Lightsail
OpenInstancePublicPorts
Create
Yes
Amazon Lightsail
PeerVpc
Create
Yes
Amazon Lightsail
PutAlarm
Edit
Yes
Amazon Lightsail
PutInstancePublicPorts
Edit
Yes
Amazon Lightsail
RebootInstance
Reboot
Yes
Amazon Lightsail
RebootRelationalDatabase
Reboot
Yes
Amazon Lightsail
RegisterContainerImage
Register
Yes
Amazon Lightsail
ReleaseStaticIp
Delete
Yes
Amazon Lightsail
ResetDistributionCache
Edit
Yes
Amazon Lightsail
SendContactMethodVerification
Send
Yes
Amazon Lightsail
SetIpAddressType
Create
Yes
Amazon Lightsail
SetResourceAccessForBucket
Create
Yes
Amazon Lightsail
StartInstance
Start
Yes
Amazon Lightsail
StartRelationalDatabase
Start
Yes
Amazon Lightsail
StopInstance
Stop
Yes
Amazon Lightsail
StopRelationalDatabase
Stop
Yes
Amazon Lightsail
TagResource
Create
Yes
Amazon Lightsail
TestAlarm
Create
Yes
Amazon Lightsail
UnpeerVpc
Create
Yes
Amazon Lightsail
UntagResource
Delete
Yes
Amazon Lightsail
UpdateBucket
Edit
Yes
Amazon Lightsail
UpdateBucketBundle
Edit
Yes
Amazon Lightsail
UpdateContainerService
Edit
Yes
Amazon Lightsail
UpdateDistribution
Edit
Yes
Amazon Lightsail
UpdateDistributionBundle
Edit
Yes
Amazon Lightsail
UpdateDomainEntry
Edit
Yes
Amazon Lightsail
UpdateLoadBalancerAttribute
Edit
Yes
Amazon Lightsail
UpdateRelationalDatabase
Edit
Yes
Amazon Lightsail
UpdateRelationalDatabaseParameters
Edit
Yes
Amazon Price List Service
DescribeServices
View
Yes
Amazon Price List Service
GetAttributeValues
View
Yes
Amazon Price List Service
GetProducts
View
Yes
Amazon Server Migration Service
CreateApp
Create
Yes
Amazon Server Migration Service
CreateReplicationJob
Create
Yes
Amazon Server Migration Service
DeleteApp
Delete
Yes
Amazon Server Migration Service
DeleteAppLaunchConfiguration
Delete
Yes
Amazon Server Migration Service
DeleteAppReplicationConfiguration
Delete
Yes
Amazon Server Migration Service
DeleteAppValidationConfiguration
Delete
Yes
Amazon Server Migration Service
DeleteReplicationJob
Delete
Yes
Amazon Server Migration Service
DeleteServerCatalog
Delete
Yes
Amazon Server Migration Service
DisassociateConnector
Delete
Yes
Amazon Server Migration Service
GenerateChangeSet
Create
Yes
Amazon Server Migration Service
GenerateTemplate
Create
Yes
Amazon Server Migration Service
GetApp
View
Yes
Amazon Server Migration Service
GetAppLaunchConfiguration
View
Yes
Amazon Server Migration Service
GetAppReplicationConfiguration
View
Yes
Amazon Server Migration Service
GetAppValidationConfiguration
View
Yes
Amazon Server Migration Service
GetAppValidationOutput
View
Yes
Amazon Server Migration Service
GetConnectors
View
Yes
Amazon Server Migration Service
GetReplicationJobs
View
Yes
Amazon Server Migration Service
GetReplicationRuns
View
Yes
Amazon Server Migration Service
GetServers
View
Yes
Amazon Server Migration Service
ImportAppCatalog
Create
Yes
Amazon Server Migration Service
ImportServerCatalog
Create
Yes
Amazon Server Migration Service
LaunchApp
Create
Yes
Amazon Server Migration Service
ListApps
View
Yes
Amazon Server Migration Service
NotifyAppValidationOutput
Create
Yes
Amazon Server Migration Service
PutAppLaunchConfiguration
Edit
Yes
Amazon Server Migration Service
PutAppReplicationConfiguration
Edit
Yes
Amazon Server Migration Service
PutAppValidationConfiguration
Edit
Yes
Amazon Server Migration Service
StartAppReplication
Start
Yes
Amazon Server Migration Service
StartOnDemandAppReplication
Start
Yes
Amazon Server Migration Service
StartOnDemandReplicationRun
Start
Yes
Amazon Server Migration Service
StopAppReplication
Stop
Yes
Amazon Server Migration Service
TerminateApp
Terminate
Yes
Amazon Server Migration Service
UpdateApp
Edit
Yes
Amazon Server Migration Service
UpdateReplicationJob
Edit
Yes
Amazon Performance Insights
DescribeDimensionKeys
View
Yes
Amazon Performance Insights
GetDimensionKeyDetails
View
Yes
Amazon Performance Insights
GetResourceMetrics
View
Yes
Amazon MediaTailor
CreateChannel
Create
Yes
Amazon MediaTailor
DeleteChannel
Delete
Yes
Amazon MediaTailor
DescribeChannel
View
Yes
Amazon MediaTailor
UpdateChannel
Edit
Yes
Amazon MediaTailor
CreateProgram
Create
Yes
Amazon MediaTailor
DeleteProgram
Delete
Yes
Amazon MediaTailor
DescribeProgram
View
Yes
Amazon MediaTailor
CreateSourceLocation
Create
Yes
Amazon MediaTailor
DeleteSourceLocation
Delete
Yes
Amazon MediaTailor
DescribeSourceLocation
View
Yes
Amazon MediaTailor
UpdateSourceLocation
Edit
Yes
Amazon MediaTailor
CreateVodSource
Create
Yes
Amazon MediaTailor
DeleteVodSource
Delete
Yes
Amazon MediaTailor
DescribeVodSource
View
Yes
Amazon MediaTailor
UpdateVodSource
Edit
Yes
Amazon MediaTailor
DeleteChannelPolicy
Delete
Yes
Amazon MediaTailor
GetChannelPolicy
View
Yes
Amazon MediaTailor
PutChannelPolicy
Edit
Yes
Amazon MediaTailor
DeletePlaybackConfiguration
Delete
Yes
Amazon MediaTailor
GetPlaybackConfiguration
View
Yes
Amazon MediaTailor
GetChannelSchedule
View
Yes
Amazon MediaTailor
ListAlerts
View
Yes
Amazon MediaTailor
ListChannels
View
Yes
Amazon MediaTailor
ListPlaybackConfigurations
View
Yes
Amazon MediaTailor
ListSourceLocations
View
Yes
Amazon MediaTailor
ListTagsForResource
View
Yes
Amazon MediaTailor
TagResource
Create
Yes
Amazon MediaTailor
ListVodSources
View
Yes
Amazon MediaTailor
PutPlaybackConfiguration
Edit
Yes
Amazon MediaTailor
StartChannel
Start
Yes
Amazon MediaTailor
StopChannel
Stop
Yes
Amazon MediaTailor
UntagResource
Delete
Yes
Amazon IoT Jobs Data Plane
DescribeJobExecution
View
Yes
Amazon IoT Jobs Data Plane
UpdateJobExecution
Edit
Yes
Amazon IoT Jobs Data Plane
GetPendingJobExecutions
View
Yes
Amazon IoT Jobs Data Plane
StartNextPendingJobExecution
Start
Yes
Amazon Import/Export Snowball
CancelCluster
Delete
Yes
Amazon Import/Export Snowball
CancelJob
Delete
Yes
Amazon Import/Export Snowball
CreateAddress
Create
Yes
Amazon Import/Export Snowball
CreateCluster
Create
Yes
Amazon Import/Export Snowball
CreateJob
Create
Yes
Amazon Import/Export Snowball
CreateLongTermPricing
Create
Yes
Amazon Import/Export Snowball
CreateReturnShippingLabel
Create
Yes
Amazon Import/Export Snowball
DescribeAddress
View
Yes
Amazon Import/Export Snowball
DescribeAddresses
View
Yes
Amazon Import/Export Snowball
DescribeCluster
View
Yes
Amazon Import/Export Snowball
DescribeJob
View
Yes
Amazon Import/Export Snowball
DescribeReturnShippingLabel
View
Yes
Amazon Import/Export Snowball
GetJobManifest
View
Yes
Amazon Import/Export Snowball
GetJobUnlockCode
View
Yes
Amazon Import/Export Snowball
GetSnowballUsage
View
Yes
Amazon Import/Export Snowball
GetSoftwareUpdates
View
Yes
Amazon Import/Export Snowball
ListClusterJobs
View
Yes
Amazon Import/Export Snowball
ListClusters
View
Yes
Amazon Import/Export Snowball
ListCompatibleImages
View
Yes
Amazon Import/Export Snowball
ListJobs
View
Yes
Amazon Import/Export Snowball
ListLongTermPricing
View
Yes
Amazon Import/Export Snowball
UpdateCluster
Edit
Yes
Amazon Import/Export Snowball
UpdateJob
Edit
Yes
Amazon Import/Export Snowball
UpdateJobShipmentState
Edit
Yes
Amazon Import/Export Snowball
UpdateLongTermPricing
Edit
Yes
Amazon Comprehend
DetectDominantLanguage
Create
Yes
Amazon Comprehend
DetectEntities
Create
Yes
Amazon Comprehend
DetectKeyPhrases
Create
Yes
Amazon Comprehend
DetectSentiment
Create
Yes
Amazon Comprehend
DetectSyntax
Create
Yes
Amazon Comprehend
ClassifyDocument
Create
Yes
Amazon Comprehend
ContainsPiiEntities
Create
Yes
Amazon Comprehend
CreateDocumentClassifier
Create
Yes
Amazon Comprehend
CreateEndpoint
Create
Yes
Amazon Comprehend
CreateEntityRecognizer
Create
Yes
Amazon Comprehend
DeleteDocumentClassifier
Delete
Yes
Amazon Comprehend
DeleteEndpoint
Delete
Yes
Amazon Comprehend
DeleteEntityRecognizer
Delete
Yes
Amazon Comprehend
DescribeDocumentClassificationJob
View
Yes
Amazon Comprehend
DescribeDocumentClassifier
View
Yes
Amazon Comprehend
DescribeDominantLanguageDetectionJob
View
Yes
Amazon Comprehend
DescribeEndpoint
View
Yes
Amazon Comprehend
DescribeEntitiesDetectionJob
View
Yes
Amazon Comprehend
DescribeEntityRecognizer
View
Yes
Amazon Comprehend
DescribeEventsDetectionJob
View
Yes
Amazon Comprehend
DescribeKeyPhrasesDetectionJob
View
Yes
Amazon Comprehend
DescribePiiEntitiesDetectionJob
View
Yes
Amazon Comprehend
DescribeSentimentDetectionJob
View
Yes
Amazon Comprehend
DescribeTopicsDetectionJob
View
Yes
Amazon Comprehend
DetectPiiEntities
Create
Yes
Amazon Comprehend
ListDocumentClassificationJobs
View
Yes
Amazon Comprehend
ListDocumentClassifiers
View
Yes
Amazon Comprehend
ListDominantLanguageDetectionJobs
View
Yes
Amazon Comprehend
ListEndpoints
View
Yes
Amazon Comprehend
ListEntitiesDetectionJobs
View
Yes
Amazon Comprehend
ListEntityRecognizers
View
Yes
Amazon Comprehend
ListEventsDetectionJobs
View
Yes
Amazon Comprehend
ListKeyPhrasesDetectionJobs
View
Yes
Amazon Comprehend
ListPiiEntitiesDetectionJobs
View
Yes
Amazon Comprehend
ListSentimentDetectionJobs
View
Yes
Amazon Comprehend
ListTagsForResource
View
Yes
Amazon Comprehend
ListTopicsDetectionJobs
View
Yes
Amazon Comprehend
StartDocumentClassificationJob
Start
Yes
Amazon Comprehend
StartDominantLanguageDetectionJob
Start
Yes
Amazon Comprehend
StartEntitiesDetectionJob
Start
Yes
Amazon Comprehend
StartEventsDetectionJob
Start
Yes
Amazon Comprehend
StartKeyPhrasesDetectionJob
Start
Yes
Amazon Comprehend
StartPiiEntitiesDetectionJob
Start
Yes
Amazon Comprehend
StartSentimentDetectionJob
Start
Yes
Amazon Comprehend
StartTopicsDetectionJob
Start
Yes
Amazon Comprehend
StopDominantLanguageDetectionJob
Stop
Yes
Amazon Comprehend
StopEntitiesDetectionJob
Stop
Yes
Amazon Comprehend
StopEventsDetectionJob
Stop
Yes
Amazon Comprehend
StopKeyPhrasesDetectionJob
Stop
Yes
Amazon Comprehend
StopPiiEntitiesDetectionJob
Stop
Yes
Amazon Comprehend
StopSentimentDetectionJob
Stop
Yes
Amazon Comprehend
StopTrainingDocumentClassifier
Stop
Yes
Amazon Comprehend
StopTrainingEntityRecognizer
Stop
Yes
Amazon Comprehend
TagResource
Create
Yes
Amazon Comprehend
UntagResource
Delete
Yes
Amazon Comprehend
UpdateEndpoint
Edit
Yes
Amazon Elastic Block Store
CompleteSnapshot
Create
Yes
Amazon Elastic Block Store
GetSnapshotBlock
View
Yes
Amazon Elastic Block Store
ListChangedBlocks
View
Yes
Amazon Elastic Block Store
ListSnapshotBlocks
View
Yes
Amazon Elastic Block Store
PutSnapshotBlock
Edit
Yes
Amazon Elastic Block Store
StartSnapshot
Start
Yes
Amazon Ground Station
CancelContact
Delete
Yes
Amazon Ground Station
DescribeContact
View
Yes
Amazon Ground Station
CreateConfig
Create
Yes
Amazon Ground Station
ListConfigs
View
Yes
Amazon Ground Station
CreateDataflowEndpointGroup
Create
Yes
Amazon Ground Station
ListDataflowEndpointGroups
View
Yes
Amazon Ground Station
CreateMissionProfile
Create
Yes
Amazon Ground Station
ListMissionProfiles
View
Yes
Amazon Ground Station
DeleteConfig
Delete
Yes
Amazon Ground Station
GetConfig
View
Yes
Amazon Ground Station
UpdateConfig
Edit
Yes
Amazon Ground Station
DeleteDataflowEndpointGroup
Delete
Yes
Amazon Ground Station
GetDataflowEndpointGroup
View
Yes
Amazon Ground Station
DeleteMissionProfile
Delete
Yes
Amazon Ground Station
GetMissionProfile
View
Yes
Amazon Ground Station
UpdateMissionProfile
Edit
Yes
Amazon Ground Station
GetMinuteUsage
View
Yes
Amazon Ground Station
GetSatellite
View
Yes
Amazon Ground Station
ListContacts
View
Yes
Amazon Ground Station
ListGroundStations
View
Yes
Amazon Ground Station
ListSatellites
View
Yes
Amazon Ground Station
ListTagsForResource
View
Yes
Amazon Ground Station
TagResource
Create
Yes
Amazon Ground Station
ReserveContact
Create
Yes
Amazon Ground Station
UntagResource
Delete
Yes
Amazon Firewall Management Service
AssociateAdminAccount
Create
Yes
Amazon Firewall Management Service
DeleteAppsList
Delete
Yes
Amazon Firewall Management Service
DeleteNotificationChannel
Delete
Yes
Amazon Firewall Management Service
DeletePolicy
Delete
Yes
Amazon Firewall Management Service
DeleteProtocolsList
Delete
Yes
Amazon Firewall Management Service
DisassociateAdminAccount
Delete
Yes
Amazon Firewall Management Service
GetAdminAccount
View
Yes
Amazon Firewall Management Service
GetAppsList
View
Yes
Amazon Firewall Management Service
GetComplianceDetail
View
Yes
Amazon Firewall Management Service
GetNotificationChannel
View
Yes
Amazon Firewall Management Service
GetPolicy
View
Yes
Amazon Firewall Management Service
GetProtectionStatus
View
Yes
Amazon Firewall Management Service
GetProtocolsList
View
Yes
Amazon Firewall Management Service
GetViolationDetails
View
Yes
Amazon Firewall Management Service
ListAppsLists
View
Yes
Amazon Firewall Management Service
ListComplianceStatus
View
Yes
Amazon Firewall Management Service
ListMemberAccounts
View
Yes
Amazon Firewall Management Service
ListPolicies
View
Yes
Amazon Firewall Management Service
ListProtocolsLists
View
Yes
Amazon Firewall Management Service
ListTagsForResource
View
Yes
Amazon Firewall Management Service
PutAppsList
Edit
Yes
Amazon Firewall Management Service
PutNotificationChannel
Edit
Yes
Amazon Firewall Management Service
PutPolicy
Edit
Yes
Amazon Firewall Management Service
PutProtocolsList
Edit
Yes
Amazon Firewall Management Service
TagResource
Create
Yes
Amazon Firewall Management Service
UntagResource
Delete
Yes
Amazon Backup
CreateBackupPlan
Create
Yes
Amazon Backup
ListBackupPlans
View
Yes
Amazon Backup
CreateBackupSelection
Create
Yes
Amazon Backup
ListBackupSelections
View
Yes
Amazon Backup
CreateBackupVault
Create
Yes
Amazon Backup
DeleteBackupVault
Delete
Yes
Amazon Backup
DescribeBackupVault
View
Yes
Amazon Backup
CreateFramework
Create
Yes
Amazon Backup
ListFrameworks
View
Yes
Amazon Backup
CreateReportPlan
Create
Yes
Amazon Backup
ListReportPlans
View
Yes
Amazon Backup
DeleteBackupPlan
Delete
Yes
Amazon Backup
UpdateBackupPlan
Edit
Yes
Amazon Backup
DeleteBackupSelection
Delete
Yes
Amazon Backup
GetBackupSelection
View
Yes
Amazon Backup
DeleteBackupVaultAccessPolicy
Delete
Yes
Amazon Backup
GetBackupVaultAccessPolicy
View
Yes
Amazon Backup
PutBackupVaultAccessPolicy
Edit
Yes
Amazon Backup
DeleteBackupVaultNotifications
Delete
Yes
Amazon Backup
GetBackupVaultNotifications
View
Yes
Amazon Backup
PutBackupVaultNotifications
Edit
Yes
Amazon Backup
DeleteFramework
Delete
Yes
Amazon Backup
DescribeFramework
View
Yes
Amazon Backup
UpdateFramework
Edit
Yes
Amazon Backup
DeleteRecoveryPoint
Delete
Yes
Amazon Backup
DescribeRecoveryPoint
View
Yes
Amazon Backup
UpdateRecoveryPointLifecycle
Edit
Yes
Amazon Backup
DeleteReportPlan
Delete
Yes
Amazon Backup
DescribeReportPlan
View
Yes
Amazon Backup
UpdateReportPlan
Edit
Yes
Amazon Backup
DescribeBackupJob
View
Yes
Amazon Backup
StopBackupJob
Stop
Yes
Amazon Backup
DescribeCopyJob
View
Yes
Amazon Backup
DescribeGlobalSettings
View
Yes
Amazon Backup
UpdateGlobalSettings
Edit
Yes
Amazon Backup
DescribeProtectedResource
View
Yes
Amazon Backup
DescribeRegionSettings
View
Yes
Amazon Backup
UpdateRegionSettings
Edit
Yes
Amazon Backup
DescribeReportJob
View
Yes
Amazon Backup
DescribeRestoreJob
View
Yes
Amazon Backup
DisassociateRecoveryPoint
Delete
Yes
Amazon Backup
ExportBackupPlanTemplate
View
Yes
Amazon Backup
GetBackupPlan
View
Yes
Amazon Backup
GetBackupPlanFromJSON
View
Yes
Amazon Backup
GetBackupPlanFromTemplate
View
Yes
Amazon Backup
GetRecoveryPointRestoreMetadata
View
Yes
Amazon Backup
GetSupportedResourceTypes
View
Yes
Amazon Backup
ListBackupJobs
View
Yes
Amazon Backup
ListBackupPlanTemplates
View
Yes
Amazon Backup
ListBackupPlanVersions
View
Yes
Amazon Backup
ListBackupVaults
View
Yes
Amazon Backup
ListCopyJobs
View
Yes
Amazon Backup
ListProtectedResources
View
Yes
Amazon Backup
ListRecoveryPointsByBackupVault
View
Yes
Amazon Backup
ListRecoveryPointsByResource
View
Yes
Amazon Backup
ListReportJobs
View
Yes
Amazon Backup
ListRestoreJobs
View
Yes
Amazon Backup
ListTags
View
Yes
Amazon Backup
StartBackupJob
Start
Yes
Amazon Backup
StartCopyJob
Start
Yes
Amazon Backup
StartReportJob
Start
Yes
Amazon Backup
StartRestoreJob
Start
Yes
Amazon Backup
TagResource
Create
Yes
Amazon Backup
UntagResource
Delete
Yes
Amazon Kendra
DeleteDocument
Delete
Yes
Amazon Kendra
GetDocumentStatus
View
Yes
Amazon Kendra
PutDocument
Edit
Yes
Amazon Kendra
ClearQuerySuggestions
Delete
Yes
Amazon Kendra
CreateDataSource
Create
Yes
Amazon Kendra
CreateFaq
Create
Yes
Amazon Kendra
CreateIndex
Create
Yes
Amazon Kendra
CreateQuerySuggestionsBlockList
Create
Yes
Amazon Kendra
CreateThesaurus
Create
Yes
Amazon Kendra
DeleteDataSource
Delete
Yes
Amazon Kendra
DeleteFaq
Delete
Yes
Amazon Kendra
DeleteIndex
Delete
Yes
Amazon Kendra
DeletePrincipalMapping
Delete
Yes
Amazon Kendra
DeleteQuerySuggestionsBlockList
Delete
Yes
Amazon Kendra
DeleteThesaurus
Delete
Yes
Amazon Kendra
DescribeDataSource
View
Yes
Amazon Kendra
DescribeFaq
View
Yes
Amazon Kendra
DescribeIndex
View
Yes
Amazon Kendra
DescribePrincipalMapping
View
Yes
Amazon Kendra
DescribeQuerySuggestionsBlockList
View
Yes
Amazon Kendra
DescribeQuerySuggestionsConfig
View
Yes
Amazon Kendra
DescribeThesaurus
View
Yes
Amazon Kendra
GetQuerySuggestions
View
Yes
Amazon Kendra
ListDataSourceSyncJobs
View
Yes
Amazon Kendra
ListDataSources
View
Yes
Amazon Kendra
ListFaqs
View
Yes
Amazon Kendra
ListGroupsOlderThanOrderingId
View
Yes
Amazon Kendra
ListIndices
View
Yes
Amazon Kendra
ListQuerySuggestionsBlockLists
View
Yes
Amazon Kendra
ListTagsForResource
View
Yes
Amazon Kendra
ListThesauri
View
Yes
Amazon Kendra
PutPrincipalMapping
Edit
Yes
Amazon Kendra
Query
Create
Yes
Amazon Kendra
StartDataSourceSyncJob
Start
Yes
Amazon Kendra
StopDataSourceSyncJob
Stop
Yes
Amazon Kendra
SubmitFeedback
Create
Yes
Amazon Kendra
TagResource
Create
Yes
Amazon Kendra
UntagResource
Delete
Yes
Amazon Kendra
UpdateDataSource
Edit
Yes
Amazon Kendra
UpdateIndex
Edit
Yes
Amazon Kendra
UpdateQuerySuggestionsBlockList
Edit
Yes
Amazon Kendra
UpdateQuerySuggestionsConfig
Edit
Yes
Amazon Kendra
UpdateThesaurus
Edit
Yes
Amazon Health APIs and Notifications
DescribeAffectedAccountsForOrganization
View
Yes
Amazon Health APIs and Notifications
DescribeAffectedEntities
View
Yes
Amazon Health APIs and Notifications
DescribeAffectedEntitiesForOrganization
View
Yes
Amazon Health APIs and Notifications
DescribeEntityAggregates
View
Yes
Amazon Health APIs and Notifications
DescribeEventAggregates
View
Yes
Amazon Health APIs and Notifications
DescribeEventDetails
View
Yes
Amazon Health APIs and Notifications
DescribeEventDetailsForOrganization
View
Yes
Amazon Health APIs and Notifications
DescribeEventTypes
View
Yes
Amazon Health APIs and Notifications
DescribeEvents
View
Yes
Amazon Health APIs and Notifications
DescribeEventsForOrganization
View
Yes
Amazon Health APIs and Notifications
DescribeHealthServiceStatusForOrganization
View
Yes
Amazon Health APIs and Notifications
DisableHealthServiceAccessForOrganization
Edit
Yes
Amazon Health APIs and Notifications
EnableHealthServiceAccessForOrganization
Enable
Yes
Amazon CodeGuru Reviewer
AssociateRepository
Create
Yes
Amazon CodeGuru Reviewer
ListRepositoryAssociations
View
Yes
Amazon CodeGuru Reviewer
CreateCodeReview
Create
Yes
Amazon CodeGuru Reviewer
DescribeCodeReview
View
Yes
Amazon CodeGuru Reviewer
DescribeRecommendationFeedback
View
Yes
Amazon CodeGuru Reviewer
DescribeRepositoryAssociation
View
Yes
Amazon CodeGuru Reviewer
DisassociateRepository
Delete
Yes
Amazon CodeGuru Reviewer
ListCodeReviews
View
Yes
Amazon CodeGuru Reviewer
ListRecommendationFeedback
View
Yes
Amazon CodeGuru Reviewer
ListRecommendations
View
Yes
Amazon CodeGuru Reviewer
ListTagsForResource
View
Yes
Amazon CodeGuru Reviewer
TagResource
Create
Yes
Amazon CodeGuru Reviewer
PutRecommendationFeedback
Edit
Yes
Amazon CodeGuru Reviewer
UntagResource
Delete
Yes
Amazon CodeDeploy
AddTagsToOnPremisesInstances
Create
Yes
Amazon CodeDeploy
GetApplicationRevisions
View
Yes
Amazon CodeDeploy
GetApplications
View
Yes
Amazon CodeDeploy
GetDeploymentGroups
View
Yes
Amazon CodeDeploy
GetDeploymentInstances
View
Yes
Amazon CodeDeploy
GetDeploymentTargets
View
Yes
Amazon CodeDeploy
GetDeployments
View
Yes
Amazon CodeDeploy
GetOnPremisesInstances
View
Yes
Amazon CodeDeploy
ContinueDeployment
Create
Yes
Amazon CodeDeploy
CreateApplication
Create
Yes
Amazon CodeDeploy
CreateDeployment
Create
Yes
Amazon CodeDeploy
CreateDeploymentConfig
Create
Yes
Amazon CodeDeploy
CreateDeploymentGroup
Create
Yes
Amazon CodeDeploy
DeleteApplication
Delete
Yes
Amazon CodeDeploy
DeleteDeploymentConfig
Delete
Yes
Amazon CodeDeploy
DeleteDeploymentGroup
Delete
Yes
Amazon CodeDeploy
DeleteGitHubAccountToken
Delete
Yes
Amazon CodeDeploy
DeleteResourcesByExternalId
Delete
Yes
Amazon CodeDeploy
DeregisterOnPremisesInstance
Deregister
Yes
Amazon CodeDeploy
GetApplication
View
Yes
Amazon CodeDeploy
GetApplicationRevision
View
Yes
Amazon CodeDeploy
GetDeployment
View
Yes
Amazon CodeDeploy
GetDeploymentConfig
View
Yes
Amazon CodeDeploy
GetDeploymentGroup
View
Yes
Amazon CodeDeploy
GetDeploymentInstance
View
Yes
Amazon CodeDeploy
GetDeploymentTarget
View
Yes
Amazon CodeDeploy
GetOnPremisesInstance
View
Yes
Amazon CodeDeploy
ListApplicationRevisions
View
Yes
Amazon CodeDeploy
ListApplications
View
Yes
Amazon CodeDeploy
ListDeploymentConfigs
View
Yes
Amazon CodeDeploy
ListDeploymentGroups
View
Yes
Amazon CodeDeploy
ListDeploymentInstances
View
Yes
Amazon CodeDeploy
ListDeploymentTargets
View
Yes
Amazon CodeDeploy
ListDeployments
View
Yes
Amazon CodeDeploy
ListGitHubAccountTokenNames
View
Yes
Amazon CodeDeploy
ListOnPremisesInstances
View
Yes
Amazon CodeDeploy
ListTagsForResource
View
Yes
Amazon CodeDeploy
PutLifecycleEventHookExecutionStatus
Edit
Yes
Amazon CodeDeploy
RegisterApplicationRevision
Register
Yes
Amazon CodeDeploy
RegisterOnPremisesInstance
Register
Yes
Amazon CodeDeploy
RemoveTagsFromOnPremisesInstances
Delete
Yes
Amazon CodeDeploy
SkipWaitTimeForInstanceTermination
Create
Yes
Amazon CodeDeploy
StopDeployment
Stop
Yes
Amazon CodeDeploy
TagResource
Create
Yes
Amazon CodeDeploy
UntagResource
Delete
Yes
Amazon CodeDeploy
UpdateApplication
Edit
Yes
Amazon CodeDeploy
UpdateDeploymentGroup
Edit
Yes
Amazon QLDB
CancelJournalKinesisStream
Delete
Yes
Amazon QLDB
DescribeJournalKinesisStream
View
Yes
Amazon QLDB
CreateLedger
Create
Yes
Amazon QLDB
ListLedgers
View
Yes
Amazon QLDB
DeleteLedger
Delete
Yes
Amazon QLDB
DescribeLedger
View
Yes
Amazon QLDB
UpdateLedger
Edit
Yes
Amazon QLDB
DescribeJournalSExport
View
Yes
Amazon QLDB
ExportJournalToS
View
Yes
Amazon QLDB
ListJournalSExportsForLedger
View
Yes
Amazon QLDB
GetBlock
View
Yes
Amazon QLDB
GetDigest
View
Yes
Amazon QLDB
GetRevision
View
Yes
Amazon QLDB
ListJournalKinesisStreamsForLedger
View
Yes
Amazon QLDB
StreamJournalToKinesis
Create
Yes
Amazon QLDB
ListJournalSExports
View
Yes
Amazon QLDB
ListTagsForResource
View
Yes
Amazon QLDB
TagResource
Create
Yes
Amazon QLDB
UntagResource
Delete
Yes
Amazon QLDB
UpdateLedgerPermissionsMode
Edit
Yes
Amazon Personalize
CreateInferenceJob
Create
Yes
Amazon Personalize
CreateCampaign
Create
Yes
Amazon Personalize
CreateDataset
Create
Yes
Amazon Personalize
CreateDatasetExportJob
Create
Yes
Amazon Personalize
CreateDatasetGroup
Create
Yes
Amazon Personalize
CreateDatasetImportJob
Create
Yes
Amazon Personalize
CreateEventTracker
Create
Yes
Amazon Personalize
CreateFilter
Create
Yes
Amazon Personalize
CreateSchema
Create
Yes
Amazon Personalize
CreateSolution
Create
Yes
Amazon Personalize
CreateSolutionVersion
Create
Yes
Amazon Personalize
DeleteCampaign
Delete
Yes
Amazon Personalize
DeleteDataset
Delete
Yes
Amazon Personalize
DeleteDatasetGroup
Delete
Yes
Amazon Personalize
DeleteEventTracker
Delete
Yes
Amazon Personalize
DeleteFilter
Delete
Yes
Amazon Personalize
DeleteSchema
Delete
Yes
Amazon Personalize
DeleteSolution
Delete
Yes
Amazon Personalize
DescribeAlgorithm
View
Yes
Amazon Personalize
DescribeInferenceJob
View
Yes
Amazon Personalize
DescribeCampaign
View
Yes
Amazon Personalize
DescribeDataset
View
Yes
Amazon Personalize
DescribeDatasetExportJob
View
Yes
Amazon Personalize
DescribeDatasetGroup
View
Yes
Amazon Personalize
DescribeDatasetImportJob
View
Yes
Amazon Personalize
DescribeEventTracker
View
Yes
Amazon Personalize
DescribeFeatureTransformation
View
Yes
Amazon Personalize
DescribeFilter
View
Yes
Amazon Personalize
DescribeRecipe
View
Yes
Amazon Personalize
DescribeSchema
View
Yes
Amazon Personalize
DescribeSolution
View
Yes
Amazon Personalize
DescribeSolutionVersion
View
Yes
Amazon Personalize
GetSolutionMetrics
View
Yes
Amazon Personalize
ListInferenceJobs
View
Yes
Amazon Personalize
ListCampaigns
View
Yes
Amazon Personalize
ListDatasetExportJobs
View
Yes
Amazon Personalize
ListDatasetGroups
View
Yes
Amazon Personalize
ListDatasetImportJobs
View
Yes
Amazon Personalize
ListDatasets
View
Yes
Amazon Personalize
ListEventTrackers
View
Yes
Amazon Personalize
ListFilters
View
Yes
Amazon Personalize
ListRecipes
View
Yes
Amazon Personalize
ListSchemas
View
Yes
Amazon Personalize
ListSolutionVersions
View
Yes
Amazon Personalize
ListSolutions
View
Yes
Amazon Personalize
StopSolutionVersionCreation
Stop
Yes
Amazon Personalize
UpdateCampaign
Edit
Yes
Amazon DataSync
CancelTaskExecution
Delete
Yes
Amazon DataSync
CreateAgent
Create
Yes
Amazon DataSync
CreateLocationEfs
Create
Yes
Amazon DataSync
CreateLocationFsxWindows
Create
Yes
Amazon DataSync
CreateLocationNfs
Create
Yes
Amazon DataSync
CreateLocationObjectStorage
Create
Yes
Amazon DataSync
CreateLocationS
Create
Yes
Amazon DataSync
CreateLocationSmb
Create
Yes
Amazon DataSync
CreateTask
Create
Yes
Amazon DataSync
DeleteAgent
Delete
Yes
Amazon DataSync
DeleteLocation
Delete
Yes
Amazon DataSync
DeleteTask
Delete
Yes
Amazon DataSync
DescribeAgent
View
Yes
Amazon DataSync
DescribeLocationEfs
View
Yes
Amazon DataSync
DescribeLocationFsxWindows
View
Yes
Amazon DataSync
DescribeLocationNfs
View
Yes
Amazon DataSync
DescribeLocationObjectStorage
View
Yes
Amazon DataSync
DescribeLocationS
View
Yes
Amazon DataSync
DescribeLocationSmb
View
Yes
Amazon DataSync
DescribeTask
View
Yes
Amazon DataSync
DescribeTaskExecution
View
Yes
Amazon DataSync
ListAgents
View
Yes
Amazon DataSync
ListLocations
View
Yes
Amazon DataSync
ListTagsForResource
View
Yes
Amazon DataSync
ListTaskExecutions
View
Yes
Amazon DataSync
ListTasks
View
Yes
Amazon DataSync
StartTaskExecution
Start
Yes
Amazon DataSync
TagResource
Create
Yes
Amazon DataSync
UntagResource
Delete
Yes
Amazon DataSync
UpdateAgent
Edit
Yes
Amazon DataSync
UpdateLocationNfs
Edit
Yes
Amazon DataSync
UpdateLocationObjectStorage
Edit
Yes
Amazon DataSync
UpdateLocationSmb
Edit
Yes
Amazon DataSync
UpdateTask
Edit
Yes
Amazon DataSync
UpdateTaskExecution
Edit
Yes
Amazon AppConfig
CreateApplication
Create
Yes
Amazon AppConfig
ListApplications
View
Yes
Amazon AppConfig
CreateConfigurationProfile
Create
Yes
Amazon AppConfig
ListConfigurationProfiles
View
Yes
Amazon AppConfig
CreateDeploymentStrategy
Create
Yes
Amazon AppConfig
ListDeploymentStrategies
View
Yes
Amazon AppConfig
CreateEnvironment
Create
Yes
Amazon AppConfig
ListEnvironments
View
Yes
Amazon AppConfig
CreateHostedConfigurationVersion
Create
Yes
Amazon AppConfig
DeleteApplication
Delete
Yes
Amazon AppConfig
GetApplication
View
Yes
Amazon AppConfig
UpdateApplication
Edit
Yes
Amazon AppConfig
DeleteConfigurationProfile
Delete
Yes
Amazon AppConfig
GetConfigurationProfile
View
Yes
Amazon AppConfig
UpdateConfigurationProfile
Edit
Yes
Amazon AppConfig
DeleteDeploymentStrategy
Delete
Yes
Amazon AppConfig
DeleteEnvironment
Delete
Yes
Amazon AppConfig
GetEnvironment
View
Yes
Amazon AppConfig
UpdateEnvironment
Edit
Yes
Amazon AppConfig
DeleteHostedConfigurationVersion
Delete
Yes
Amazon AppConfig
GetHostedConfigurationVersion
View
Yes
Amazon AppConfig
GetConfiguration
View
Yes
Amazon AppConfig
GetDeployment
View
Yes
Amazon AppConfig
StopDeployment
Delete
Yes
Amazon AppConfig
GetDeploymentStrategy
View
Yes
Amazon AppConfig
UpdateDeploymentStrategy
Edit
Yes
Amazon AppConfig
ListDeployments
View
Yes
Amazon AppConfig
StartDeployment
Start
Yes
Amazon AppConfig
ListHostedConfigurationVersions
View
Yes
Amazon AppConfig
ListTagsForResource
View
Yes
Amazon AppConfig
TagResource
Create
Yes
Amazon AppConfig
UntagResource
Delete
Yes
Amazon AppConfig
ValidateConfiguration
Create
Yes
Amazon Cognito Identity Provider
AddCustomAttributes
Create
Yes
Amazon Cognito Identity Provider
AdminAddUserToGroup
Create
Yes
Amazon Cognito Identity Provider
AdminConfirmSignUp
Create
Yes
Amazon Cognito Identity Provider
AdminCreateUser
Create
Yes
Amazon Cognito Identity Provider
AdminDeleteUser
Create
Yes
Amazon Cognito Identity Provider
AdminDeleteUserAttributes
Create
Yes
Amazon Cognito Identity Provider
AdminDisableProviderForUser
Create
Yes
Amazon Cognito Identity Provider
AdminDisableUser
Create
Yes
Amazon Cognito Identity Provider
AdminEnableUser
Create
Yes
Amazon Cognito Identity Provider
AdminForgetDevice
Create
Yes
Amazon Cognito Identity Provider
AdminGetDevice
Create
Yes
Amazon Cognito Identity Provider
AdminGetUser
Create
Yes
Amazon Cognito Identity Provider
AdminInitiateAuth
Create
Yes
Amazon Cognito Identity Provider
AdminLinkProviderForUser
Create
Yes
Amazon Cognito Identity Provider
AdminListDevices
Create
Yes
Amazon Cognito Identity Provider
AdminListGroupsForUser
Create
Yes
Amazon Cognito Identity Provider
AdminListUserAuthEvents
Create
Yes
Amazon Cognito Identity Provider
AdminRemoveUserFromGroup
Create
Yes
Amazon Cognito Identity Provider
AdminResetUserPassword
Create
Yes
Amazon Cognito Identity Provider
AdminRespondToAuthChallenge
Create
Yes
Amazon Cognito Identity Provider
AdminSetUserMFAPreference
Create
Yes
Amazon Cognito Identity Provider
AdminSetUserPassword
Create
Yes
Amazon Cognito Identity Provider
AdminSetUserSettings
Create
Yes
Amazon Cognito Identity Provider
AdminUpdateAuthEventFeedback
Create
Yes
Amazon Cognito Identity Provider
AdminUpdateDeviceStatus
Create
Yes
Amazon Cognito Identity Provider
AdminUpdateUserAttributes
Create
Yes
Amazon Cognito Identity Provider
AdminUserGlobalSignOut
Create
Yes
Amazon Cognito Identity Provider
AssociateSoftwareToken
Create
Yes
Amazon Cognito Identity Provider
ChangePassword
Create
Yes
Amazon Cognito Identity Provider
ConfirmDevice
Create
Yes
Amazon Cognito Identity Provider
ConfirmForgotPassword
Create
Yes
Amazon Cognito Identity Provider
ConfirmSignUp
Create
Yes
Amazon Cognito Identity Provider
CreateGroup
Create
Yes
Amazon Cognito Identity Provider
CreateIdentityProvider
Create
Yes
Amazon Cognito Identity Provider
CreateResourceServer
Create
Yes
Amazon Cognito Identity Provider
CreateUserImportJob
Create
Yes
Amazon Cognito Identity Provider
CreateUserPool
Create
Yes
Amazon Cognito Identity Provider
CreateUserPoolClient
Create
Yes
Amazon Cognito Identity Provider
CreateUserPoolDomain
Create
Yes
Amazon Cognito Identity Provider
DeleteGroup
Delete
Yes
Amazon Cognito Identity Provider
DeleteIdentityProvider
Delete
Yes
Amazon Cognito Identity Provider
DeleteResourceServer
Delete
Yes
Amazon Cognito Identity Provider
DeleteUser
Delete
Yes
Amazon Cognito Identity Provider
DeleteUserAttributes
Delete
Yes
Amazon Cognito Identity Provider
DeleteUserPool
Delete
Yes
Amazon Cognito Identity Provider
DeleteUserPoolClient
Delete
Yes
Amazon Cognito Identity Provider
DeleteUserPoolDomain
Delete
Yes
Amazon Cognito Identity Provider
DescribeIdentityProvider
View
Yes
Amazon Cognito Identity Provider
DescribeResourceServer
View
Yes
Amazon Cognito Identity Provider
DescribeRiskConfiguration
View
Yes
Amazon Cognito Identity Provider
DescribeUserImportJob
View
Yes
Amazon Cognito Identity Provider
DescribeUserPool
View
Yes
Amazon Cognito Identity Provider
DescribeUserPoolClient
View
Yes
Amazon Cognito Identity Provider
DescribeUserPoolDomain
View
Yes
Amazon Cognito Identity Provider
ForgetDevice
Create
Yes
Amazon Cognito Identity Provider
ForgotPassword
Create
Yes
Amazon Cognito Identity Provider
GetCSVHeader
View
Yes
Amazon Cognito Identity Provider
GetDevice
View
Yes
Amazon Cognito Identity Provider
GetGroup
View
Yes
Amazon Cognito Identity Provider
GetIdentityProviderByIdentifier
View
Yes
Amazon Cognito Identity Provider
GetSigningCertificate
View
Yes
Amazon Cognito Identity Provider
GetUICustomization
View
Yes
Amazon Cognito Identity Provider
GetUser
View
Yes
Amazon Cognito Identity Provider
GetUserAttributeVerificationCode
View
Yes
Amazon Cognito Identity Provider
GetUserPoolMfaConfig
View
Yes
Amazon Cognito Identity Provider
GlobalSignOut
Create
Yes
Amazon Cognito Identity Provider
InitiateAuth
Create
Yes
Amazon Cognito Identity Provider
ListDevices
View
Yes
Amazon Cognito Identity Provider
ListGroups
View
Yes
Amazon Cognito Identity Provider
ListIdentityProviders
View
Yes
Amazon Cognito Identity Provider
ListResourceServers
View
Yes
Amazon Cognito Identity Provider
ListTagsForResource
View
Yes
Amazon Cognito Identity Provider
ListUserImportJobs
View
Yes
Amazon Cognito Identity Provider
ListUserPoolClients
View
Yes
Amazon Cognito Identity Provider
ListUserPools
View
Yes
Amazon Cognito Identity Provider
ListUsers
View
Yes
Amazon Cognito Identity Provider
ListUsersInGroup
View
Yes
Amazon Cognito Identity Provider
ResendConfirmationCode
Create
Yes
Amazon Cognito Identity Provider
RespondToAuthChallenge
Create
Yes
Amazon Cognito Identity Provider
RevokeToken
Delete
Yes
Amazon Cognito Identity Provider
SetRiskConfiguration
Create
Yes
Amazon Cognito Identity Provider
SetUICustomization
Create
Yes
Amazon Cognito Identity Provider
SetUserMFAPreference
Create
Yes
Amazon Cognito Identity Provider
SetUserPoolMfaConfig
Create
Yes
Amazon Cognito Identity Provider
SetUserSettings
Create
Yes
Amazon Cognito Identity Provider
SignUp
Create
Yes
Amazon Cognito Identity Provider
StartUserImportJob
Start
Yes
Amazon Cognito Identity Provider
StopUserImportJob
Stop
Yes
Amazon Cognito Identity Provider
TagResource
Create
Yes
Amazon Cognito Identity Provider
UntagResource
Delete
Yes
Amazon Cognito Identity Provider
UpdateAuthEventFeedback
Edit
Yes
Amazon Cognito Identity Provider
UpdateDeviceStatus
Edit
Yes
Amazon Cognito Identity Provider
UpdateGroup
Edit
Yes
Amazon Cognito Identity Provider
UpdateIdentityProvider
Edit
Yes
Amazon Cognito Identity Provider
UpdateResourceServer
Edit
Yes
Amazon Cognito Identity Provider
UpdateUserAttributes
Edit
Yes
Amazon Cognito Identity Provider
UpdateUserPool
Edit
Yes
Amazon Cognito Identity Provider
UpdateUserPoolClient
Edit
Yes
Amazon Cognito Identity Provider
UpdateUserPoolDomain
Edit
Yes
Amazon Cognito Identity Provider
VerifySoftwareToken
Create
Yes
Amazon Cognito Identity Provider
VerifyUserAttribute
Create
Yes
Amazon Elemental MediaPackage VOD
ConfigureLogs
Edit
Yes
Amazon Elemental MediaPackage VOD
CreateAsset
Create
Yes
Amazon Elemental MediaPackage VOD
ListAssets
View
Yes
Amazon Elemental MediaPackage VOD
CreatePackagingConfiguration
Create
Yes
Amazon Elemental MediaPackage VOD
ListPackagingConfigurations
View
Yes
Amazon Elemental MediaPackage VOD
CreatePackagingGroup
Create
Yes
Amazon Elemental MediaPackage VOD
ListPackagingGroups
View
Yes
Amazon Elemental MediaPackage VOD
DeleteAsset
Delete
Yes
Amazon Elemental MediaPackage VOD
DescribeAsset
View
Yes
Amazon Elemental MediaPackage VOD
DeletePackagingConfiguration
Delete
Yes
Amazon Elemental MediaPackage VOD
DescribePackagingConfiguration
View
Yes
Amazon Elemental MediaPackage VOD
DeletePackagingGroup
Delete
Yes
Amazon Elemental MediaPackage VOD
DescribePackagingGroup
View
Yes
Amazon Elemental MediaPackage VOD
UpdatePackagingGroup
Edit
Yes
Amazon Elemental MediaPackage VOD
ListTagsForResource
View
Yes
Amazon Elemental MediaPackage VOD
TagResource
Create
Yes
Amazon Elemental MediaPackage VOD
UntagResource
Delete
Yes
Amazon Augmented AI Runtime
DeleteHumanLoop
Delete
Yes
Amazon Augmented AI Runtime
DescribeHumanLoop
View
Yes
Amazon Augmented AI Runtime
ListHumanLoops
View
Yes
Amazon Augmented AI Runtime
StartHumanLoop
Start
Yes
Amazon Augmented AI Runtime
StopHumanLoop
Stop
Yes
Amazon Timestream Query
CancelQuery
Delete
Yes
Amazon Timestream Query
DescribeEndpoints
View
Yes
Amazon Timestream Query
Query
Create
Yes
Amazon RoboMaker
DeleteWorlds
Delete
Yes
Amazon RoboMaker
DescribeSimulationJob
View
Yes
Amazon RoboMaker
CancelDeploymentJob
Delete
Yes
Amazon RoboMaker
CancelSimulationJob
Delete
Yes
Amazon RoboMaker
CancelWorldExportJob
Delete
Yes
Amazon RoboMaker
CancelWorldGenerationJob
Delete
Yes
Amazon RoboMaker
CreateDeploymentJob
Create
Yes
Amazon RoboMaker
CreateFleet
Create
Yes
Amazon RoboMaker
CreateRobot
Create
Yes
Amazon RoboMaker
CreateRobotApplication
Create
Yes
Amazon RoboMaker
CreateRobotApplicationVersion
Create
Yes
Amazon RoboMaker
CreateSimulationApplication
Create
Yes
Amazon RoboMaker
CreateSimulationApplicationVersion
Create
Yes
Amazon RoboMaker
CreateSimulationJob
Create
Yes
Amazon RoboMaker
CreateWorldExportJob
Create
Yes
Amazon RoboMaker
CreateWorldGenerationJob
Create
Yes
Amazon RoboMaker
CreateWorldTemplate
Create
Yes
Amazon RoboMaker
DeleteFleet
Delete
Yes
Amazon RoboMaker
DeleteRobot
Delete
Yes
Amazon RoboMaker
DeleteRobotApplication
Delete
Yes
Amazon RoboMaker
DeleteSimulationApplication
Delete
Yes
Amazon RoboMaker
DeleteWorldTemplate
Delete
Yes
Amazon RoboMaker
DeregisterRobot
Deregister
Yes
Amazon RoboMaker
DescribeDeploymentJob
View
Yes
Amazon RoboMaker
DescribeFleet
View
Yes
Amazon RoboMaker
DescribeRobot
View
Yes
Amazon RoboMaker
DescribeRobotApplication
View
Yes
Amazon RoboMaker
DescribeSimulationApplication
View
Yes
Amazon RoboMaker
DescribeWorld
View
Yes
Amazon RoboMaker
DescribeWorldExportJob
View
Yes
Amazon RoboMaker
DescribeWorldGenerationJob
View
Yes
Amazon RoboMaker
DescribeWorldTemplate
View
Yes
Amazon RoboMaker
GetWorldTemplateBody
View
Yes
Amazon RoboMaker
ListDeploymentJobs
View
Yes
Amazon RoboMaker
ListFleets
View
Yes
Amazon RoboMaker
ListRobotApplications
View
Yes
Amazon RoboMaker
ListRobots
View
Yes
Amazon RoboMaker
ListSimulationApplications
View
Yes
Amazon RoboMaker
ListSimulationJobes
View
Yes
Amazon RoboMaker
ListSimulationJobs
View
Yes
Amazon RoboMaker
ListTagsForResource
View
Yes
Amazon RoboMaker
TagResource
Create
Yes
Amazon RoboMaker
ListWorldExportJobs
View
Yes
Amazon RoboMaker
ListWorldGenerationJobs
View
Yes
Amazon RoboMaker
ListWorldTemplates
View
Yes
Amazon RoboMaker
ListWorlds
View
Yes
Amazon RoboMaker
RegisterRobot
Register
Yes
Amazon RoboMaker
RestartSimulationJob
Reboot
Yes
Amazon RoboMaker
StartSimulationJob
Start
Yes
Amazon RoboMaker
SyncDeploymentJob
Create
Yes
Amazon RoboMaker
UntagResource
Delete
Yes
Amazon RoboMaker
UpdateRobotApplication
Edit
Yes
Amazon RoboMaker
UpdateSimulationApplication
Edit
Yes
Amazon RoboMaker
UpdateWorldTemplate
Edit
Yes
Amazon Mechanical Turk
AcceptQualificationRequest
Approve
Yes
Amazon Mechanical Turk
ApproveAssignment
Approve
Yes
Amazon Mechanical Turk
AssociateQualificationWithWorker
Create
Yes
Amazon Mechanical Turk
CreateAdditionalAssignmentsForHIT
Create
Yes
Amazon Mechanical Turk
CreateHIT
Create
Yes
Amazon Mechanical Turk
CreateHITType
Create
Yes
Amazon Mechanical Turk
CreateHITWithHITType
Create
Yes
Amazon Mechanical Turk
CreateQualificationType
Create
Yes
Amazon Mechanical Turk
CreateWorkerBlock
Create
Yes
Amazon Mechanical Turk
DeleteHIT
Delete
Yes
Amazon Mechanical Turk
DeleteQualificationType
Delete
Yes
Amazon Mechanical Turk
DeleteWorkerBlock
Delete
Yes
Amazon Mechanical Turk
DisassociateQualificationFromWorker
Delete
Yes
Amazon Mechanical Turk
GetAccountBalance
View
Yes
Amazon Mechanical Turk
GetAssignment
View
Yes
Amazon Mechanical Turk
GetFileUploadURL
View
Yes
Amazon Mechanical Turk
GetHIT
View
Yes
Amazon Mechanical Turk
GetQualificationScore
View
Yes
Amazon Mechanical Turk
GetQualificationType
View
Yes
Amazon Mechanical Turk
ListAssignmentsForHIT
View
Yes
Amazon Mechanical Turk
ListBonusPayments
View
Yes
Amazon Mechanical Turk
ListHITs
View
Yes
Amazon Mechanical Turk
ListHITsForQualificationType
View
Yes
Amazon Mechanical Turk
ListQualificationRequests
View
Yes
Amazon Mechanical Turk
ListQualificationTypes
View
Yes
Amazon Mechanical Turk
ListReviewPolicyResultsForHIT
View
Yes
Amazon Mechanical Turk
ListReviewableHITs
View
Yes
Amazon Mechanical Turk
ListWorkerBlocks
View
Yes
Amazon Mechanical Turk
ListWorkersWithQualificationType
View
Yes
Amazon Mechanical Turk
NotifyWorkers
Create
Yes
Amazon Mechanical Turk
RejectAssignment
Reject
Yes
Amazon Mechanical Turk
RejectQualificationRequest
Reject
Yes
Amazon Mechanical Turk
SendBonus
Send
Yes
Amazon Mechanical Turk
SendTestEventNotification
Send
Yes
Amazon Mechanical Turk
UpdateExpirationForHIT
Edit
Yes
Amazon Mechanical Turk
UpdateHITReviewStatus
Edit
Yes
Amazon Mechanical Turk
UpdateHITTypeOfHIT
Edit
Yes
Amazon Mechanical Turk
UpdateNotificationSettings
Edit
Yes
Amazon Mechanical Turk
UpdateQualificationType
Edit
Yes
Amazon MediaConnect
AddFlowMediaStreams
Create
Yes
Amazon MediaConnect
AddFlowOutputs
Create
Yes
Amazon MediaConnect
AddFlowSources
Create
Yes
Amazon MediaConnect
AddFlowVpcInterfaces
Create
Yes
Amazon MediaConnect
CreateFlow
Create
Yes
Amazon MediaConnect
ListFlows
View
Yes
Amazon MediaConnect
DeleteFlow
Delete
Yes
Amazon MediaConnect
DescribeFlow
View
Yes
Amazon MediaConnect
UpdateFlow
Edit
Yes
Amazon MediaConnect
DescribeOffering
View
Yes
Amazon MediaConnect
PurchaseOffering
Purchase
Yes
Amazon MediaConnect
DescribeReservation
View
Yes
Amazon MediaConnect
GrantFlowEntitlements
Create
Yes
Amazon MediaConnect
ListEntitlements
View
Yes
Amazon MediaConnect
ListOfferings
View
Yes
Amazon MediaConnect
ListReservations
View
Yes
Amazon MediaConnect
ListTagsForResource
View
Yes
Amazon MediaConnect
TagResource
Create
Yes
Amazon MediaConnect
RemoveFlowMediaStream
Delete
Yes
Amazon MediaConnect
UpdateFlowMediaStream
Edit
Yes
Amazon MediaConnect
RemoveFlowOutput
Delete
Yes
Amazon MediaConnect
UpdateFlowOutput
Edit
Yes
Amazon MediaConnect
RemoveFlowSource
Delete
Yes
Amazon MediaConnect
UpdateFlowSource
Edit
Yes
Amazon MediaConnect
RemoveFlowVpcInterface
Delete
Yes
Amazon MediaConnect
RevokeFlowEntitlement
Delete
Yes
Amazon MediaConnect
UpdateFlowEntitlement
Edit
Yes
Amazon MediaConnect
StartFlow
Start
Yes
Amazon MediaConnect
StopFlow
Stop
Yes
Amazon MediaConnect
UntagResource
Delete
Yes
Amazon Kinesis Analytics
AddApplicationCloudWatchLoggingOption
Create
Yes
Amazon Kinesis Analytics
AddApplicationInput
Create
Yes
Amazon Kinesis Analytics
AddApplicationInputProcessingConfiguration
Create
Yes
Amazon Kinesis Analytics
AddApplicationOutput
Create
Yes
Amazon Kinesis Analytics
AddApplicationReferenceDataSource
Create
Yes
Amazon Kinesis Analytics
AddApplicationVpcConfiguration
Create
Yes
Amazon Kinesis Analytics
CreateApplication
Create
Yes
Amazon Kinesis Analytics
CreateApplicationPresignedUrl
Create
Yes
Amazon Kinesis Analytics
CreateApplicationSnapshot
Create
Yes
Amazon Kinesis Analytics
DeleteApplication
Delete
Yes
Amazon Kinesis Analytics
DeleteApplicationCloudWatchLoggingOption
Delete
Yes
Amazon Kinesis Analytics
DeleteApplicationInputProcessingConfiguration
Delete
Yes
Amazon Kinesis Analytics
DeleteApplicationOutput
Delete
Yes
Amazon Kinesis Analytics
DeleteApplicationReferenceDataSource
Delete
Yes
Amazon Kinesis Analytics
DeleteApplicationSnapshot
Delete
Yes
Amazon Kinesis Analytics
DeleteApplicationVpcConfiguration
Delete
Yes
Amazon Kinesis Analytics
DescribeApplication
View
Yes
Amazon Kinesis Analytics
DescribeApplicationSnapshot
View
Yes
Amazon Kinesis Analytics
DescribeApplicationVersion
View
Yes
Amazon Kinesis Analytics
DiscoverInputSchema
Create
Yes
Amazon Kinesis Analytics
ListApplicationSnapshots
View
Yes
Amazon Kinesis Analytics
ListApplicationVersions
View
Yes
Amazon Kinesis Analytics
ListApplications
View
Yes
Amazon Kinesis Analytics
ListTagsForResource
View
Yes
Amazon Kinesis Analytics
RollbackApplication
Create
Yes
Amazon Kinesis Analytics
StartApplication
Start
Yes
Amazon Kinesis Analytics
StopApplication
Stop
Yes
Amazon Kinesis Analytics
TagResource
Create
Yes
Amazon Kinesis Analytics
UntagResource
Delete
Yes
Amazon Kinesis Analytics
UpdateApplication
Edit
Yes
Amazon Kinesis Analytics
UpdateApplicationMaintenanceConfiguration
Edit
Yes
Amazon Data Lifecycle Manager
CreateLifecyclePolicy
Create
Yes
Amazon Data Lifecycle Manager
GetLifecyclePolicies
View
Yes
Amazon Data Lifecycle Manager
DeleteLifecyclePolicy
Delete
Yes
Amazon Data Lifecycle Manager
GetLifecyclePolicy
View
Yes
Amazon Data Lifecycle Manager
ListTagsForResource
View
Yes
Amazon Data Lifecycle Manager
TagResource
Create
Yes
Amazon Data Lifecycle Manager
UntagResource
Delete
Yes
Amazon Data Lifecycle Manager
UpdateLifecyclePolicy
Edit
Yes
Amazon CodeCommit
AssociateApprovalRuleTemplateWithRepository
Create
Yes
Amazon CodeCommit
AssociateApprovalRuleTemplateWithRepositories
Create
Yes
Amazon CodeCommit
DescribeMergeConflicts
View
Yes
Amazon CodeCommit
DisassociateApprovalRuleTemplateFromRepositories
Delete
Yes
Amazon CodeCommit
GetCommits
View
Yes
Amazon CodeCommit
GetRepositories
View
Yes
Amazon CodeCommit
CreateApprovalRuleTemplate
Create
Yes
Amazon CodeCommit
CreateBranch
Create
Yes
Amazon CodeCommit
CreateCommit
Create
Yes
Amazon CodeCommit
CreatePullRequest
Create
Yes
Amazon CodeCommit
CreatePullRequestApprovalRule
Create
Yes
Amazon CodeCommit
CreateRepository
Create
Yes
Amazon CodeCommit
CreateUnreferencedMergeCommit
Create
Yes
Amazon CodeCommit
DeleteApprovalRuleTemplate
Delete
Yes
Amazon CodeCommit
DeleteBranch
Delete
Yes
Amazon CodeCommit
DeleteCommentContent
Delete
Yes
Amazon CodeCommit
DeleteFile
Delete
Yes
Amazon CodeCommit
DeletePullRequestApprovalRule
Delete
Yes
Amazon CodeCommit
DeleteRepository
Delete
Yes
Amazon CodeCommit
DescribePullRequestEvents
View
Yes
Amazon CodeCommit
DisassociateApprovalRuleTemplateFromRepository
Delete
Yes
Amazon CodeCommit
EvaluatePullRequestApprovalRules
Create
Yes
Amazon CodeCommit
GetApprovalRuleTemplate
View
Yes
Amazon CodeCommit
GetBlob
View
Yes
Amazon CodeCommit
GetBranch
View
Yes
Amazon CodeCommit
GetComment
View
Yes
Amazon CodeCommit
GetCommentReactions
View
Yes
Amazon CodeCommit
GetCommentsForComparedCommit
View
Yes
Amazon CodeCommit
GetCommentsForPullRequest
View
Yes
Amazon CodeCommit
GetCommit
View
Yes
Amazon CodeCommit
GetDifferences
View
Yes
Amazon CodeCommit
GetFile
View
Yes
Amazon CodeCommit
GetFolder
View
Yes
Amazon CodeCommit
GetMergeCommit
View
Yes
Amazon CodeCommit
GetMergeConflicts
View
Yes
Amazon CodeCommit
GetMergeOptions
View
Yes
Amazon CodeCommit
GetPullRequest
View
Yes
Amazon CodeCommit
GetPullRequestApprovalStates
View
Yes
Amazon CodeCommit
GetPullRequestOverrideState
View
Yes
Amazon CodeCommit
GetRepository
View
Yes
Amazon CodeCommit
GetRepositoryTriggers
View
Yes
Amazon CodeCommit
ListApprovalRuleTemplates
View
Yes
Amazon CodeCommit
ListAssociatedApprovalRuleTemplatesForRepository
View
Yes
Amazon CodeCommit
ListBranches
View
Yes
Amazon CodeCommit
ListPullRequests
View
Yes
Amazon CodeCommit
ListRepositories
View
Yes
Amazon CodeCommit
ListRepositoriesForApprovalRuleTemplate
View
Yes
Amazon CodeCommit
ListTagsForResource
View
Yes
Amazon CodeCommit
MergeBranchesByFastForward
Create
Yes
Amazon CodeCommit
MergeBranchesBySquash
Create
Yes
Amazon CodeCommit
MergeBranchesByThreeWay
Create
Yes
Amazon CodeCommit
MergePullRequestByFastForward
Create
Yes
Amazon CodeCommit
MergePullRequestBySquash
Create
Yes
Amazon CodeCommit
MergePullRequestByThreeWay
Create
Yes
Amazon CodeCommit
OverridePullRequestApprovalRules
Create
Yes
Amazon CodeCommit
PostCommentForComparedCommit
Create
Yes
Amazon CodeCommit
PostCommentForPullRequest
Create
Yes
Amazon CodeCommit
PostCommentReply
Create
Yes
Amazon CodeCommit
PutCommentReaction
Edit
Yes
Amazon CodeCommit
PutFile
Edit
Yes
Amazon CodeCommit
PutRepositoryTriggers
Edit
Yes
Amazon CodeCommit
TagResource
Create
Yes
Amazon CodeCommit
TestRepositoryTriggers
Create
Yes
Amazon CodeCommit
UntagResource
Delete
Yes
Amazon CodeCommit
UpdateApprovalRuleTemplateContent
Edit
Yes
Amazon CodeCommit
UpdateApprovalRuleTemplateDescription
Edit
Yes
Amazon CodeCommit
UpdateApprovalRuleTemplateName
Edit
Yes
Amazon CodeCommit
UpdateComment
Edit
Yes
Amazon CodeCommit
UpdateDefaultBranch
Edit
Yes
Amazon CodeCommit
UpdatePullRequestApprovalRuleContent
Edit
Yes
Amazon CodeCommit
UpdatePullRequestApprovalState
Edit
Yes
Amazon CodeCommit
UpdatePullRequestDescription
Edit
Yes
Amazon CodeCommit
UpdatePullRequestStatus
Edit
Yes
Amazon CodeCommit
UpdatePullRequestTitle
Edit
Yes
Amazon CodeCommit
UpdateRepositoryDescription
Edit
Yes
Amazon CodeCommit
UpdateRepositoryName
Edit
Yes
Amazon CodeArtifact
AssociateExternalConnection
Create
Yes
Amazon CodeArtifact
DisassociateExternalConnection
Delete
Yes
Amazon CodeArtifact
CopyPackageVersions
Copy
Yes
Amazon CodeArtifact
CreateDomain
Create
Yes
Amazon CodeArtifact
DeleteDomain
Delete
Yes
Amazon CodeArtifact
DescribeDomain
View
Yes
Amazon CodeArtifact
CreateRepository
Create
Yes
Amazon CodeArtifact
DeleteRepository
Delete
Yes
Amazon CodeArtifact
DescribeRepository
View
Yes
Amazon CodeArtifact
UpdateRepository
Edit
Yes
Amazon CodeArtifact
DeleteDomainPermissionsPolicy
Delete
Yes
Amazon CodeArtifact
GetDomainPermissionsPolicy
View
Yes
Amazon CodeArtifact
DeletePackageVersions
Delete
Yes
Amazon CodeArtifact
DeleteRepositoryPermissionsPolicy
Delete
Yes
Amazon CodeArtifact
DescribePackageVersion
View
Yes
Amazon CodeArtifact
DisposePackageVersions
Create
Yes
Amazon CodeArtifact
GetAuthorizationToken
View
Yes
Amazon CodeArtifact
GetPackageVersionAsset
View
Yes
Amazon CodeArtifact
GetPackageVersionReadme
View
Yes
Amazon CodeArtifact
GetRepositoryEndpoint
View
Yes
Amazon CodeArtifact
GetRepositoryPermissionsPolicy
View
Yes
Amazon CodeArtifact
PutRepositoryPermissionsPolicy
Edit
Yes
Amazon CodeArtifact
ListDomains
View
Yes
Amazon CodeArtifact
ListPackageVersionAssets
View
Yes
Amazon CodeArtifact
ListPackageVersionDependencies
View
Yes
Amazon CodeArtifact
ListPackageVersions
View
Yes
Amazon CodeArtifact
ListPackages
View
Yes
Amazon CodeArtifact
ListRepositories
View
Yes
Amazon CodeArtifact
ListRepositoriesInDomain
View
Yes
Amazon CodeArtifact
ListTagsForResource
View
Yes
Amazon CodeArtifact
PutDomainPermissionsPolicy
Edit
Yes
Amazon CodeArtifact
TagResource
Create
Yes
Amazon CodeArtifact
UntagResource
Delete
Yes
Amazon CodeArtifact
UpdatePackageVersionsStatus
Edit
Yes
Amazon EC2 Instance Connect
SendSSHPublicKey
Send
Yes
Amazon EC2 Instance Connect
SendSerialConsoleSSHPublicKey
Send
Yes
Amazon IoT Events
CreateAlarmModel
Create
Yes
Amazon IoT Events
ListAlarmModels
View
Yes
Amazon IoT Events
CreateDetectorModel
Create
Yes
Amazon IoT Events
ListDetectorModels
View
Yes
Amazon IoT Events
CreateInput
Create
Yes
Amazon IoT Events
ListInputs
View
Yes
Amazon IoT Events
DeleteAlarmModel
Delete
Yes
Amazon IoT Events
DescribeAlarmModel
View
Yes
Amazon IoT Events
UpdateAlarmModel
Edit
Yes
Amazon IoT Events
DeleteDetectorModel
Delete
Yes
Amazon IoT Events
DescribeDetectorModel
View
Yes
Amazon IoT Events
UpdateDetectorModel
Edit
Yes
Amazon IoT Events
DeleteInput
Delete
Yes
Amazon IoT Events
DescribeInput
View
Yes
Amazon IoT Events
UpdateInput
Edit
Yes
Amazon IoT Events
DescribeDetectorModelAnalysis
View
Yes
Amazon IoT Events
DescribeLoggingOptions
View
Yes
Amazon IoT Events
PutLoggingOptions
Edit
Yes
Amazon IoT Events
GetDetectorModelAnalysisResults
View
Yes
Amazon IoT Events
ListAlarmModelVersions
View
Yes
Amazon IoT Events
ListDetectorModelVersions
View
Yes
Amazon IoT Events
ListInputRoutings
View
Yes
Amazon IoT Events
ListTagsForResource
View
Yes
Amazon IoT Events
TagResource
Create
Yes
Amazon IoT Events
StartDetectorModelAnalysis
Start
Yes
Amazon IoT Events
UntagResource
Delete
Yes
Amazon IoT Analytics
PutMessage
Edit
Yes
Amazon IoT Analytics
CancelPipelineReprocessing
Delete
Yes
Amazon IoT Analytics
CreateChannel
Create
Yes
Amazon IoT Analytics
ListChannels
View
Yes
Amazon IoT Analytics
CreateDataset
Create
Yes
Amazon IoT Analytics
ListDatasets
View
Yes
Amazon IoT Analytics
CreateDatasetContent
Create
Yes
Amazon IoT Analytics
DeleteDatasetContent
Delete
Yes
Amazon IoT Analytics
GetDatasetContent
View
Yes
Amazon IoT Analytics
CreateDatastore
Create
Yes
Amazon IoT Analytics
ListDatastores
View
Yes
Amazon IoT Analytics
CreatePipeline
Create
Yes
Amazon IoT Analytics
ListPipelines
View
Yes
Amazon IoT Analytics
DeleteChannel
Delete
Yes
Amazon IoT Analytics
DescribeChannel
View
Yes
Amazon IoT Analytics
UpdateChannel
Edit
Yes
Amazon IoT Analytics
DeleteDataset
Delete
Yes
Amazon IoT Analytics
DescribeDataset
View
Yes
Amazon IoT Analytics
UpdateDataset
Edit
Yes
Amazon IoT Analytics
DeleteDatastore
Delete
Yes
Amazon IoT Analytics
DescribeDatastore
View
Yes
Amazon IoT Analytics
UpdateDatastore
Edit
Yes
Amazon IoT Analytics
DeletePipeline
Delete
Yes
Amazon IoT Analytics
DescribePipeline
View
Yes
Amazon IoT Analytics
UpdatePipeline
Edit
Yes
Amazon IoT Analytics
DescribeLoggingOptions
View
Yes
Amazon IoT Analytics
PutLoggingOptions
Edit
Yes
Amazon IoT Analytics
ListDatasetContents
View
Yes
Amazon IoT Analytics
ListTagsForResource
View
Yes
Amazon IoT Analytics
TagResource
Create
Yes
Amazon IoT Analytics
RunPipelineActivity
Create
Yes
Amazon IoT Analytics
SampleChannelData
View
Yes
Amazon IoT Analytics
StartPipelineReprocessing
Start
Yes
Amazon IoT Analytics
UntagResource
Delete
Yes
Amazon EC2 Image Builder
CancelImageCreation
Delete
Yes
Amazon EC2 Image Builder
CreateComponent
Create
Yes
Amazon EC2 Image Builder
CreateContainerRecipe
Create
Yes
Amazon EC2 Image Builder
CreateDistributionConfiguration
Create
Yes
Amazon EC2 Image Builder
CreateImage
Create
Yes
Amazon EC2 Image Builder
CreateImagePipeline
Create
Yes
Amazon EC2 Image Builder
CreateImageRecipe
Create
Yes
Amazon EC2 Image Builder
CreateInfrastructureConfiguration
Create
Yes
Amazon EC2 Image Builder
DeleteComponent
Delete
Yes
Amazon EC2 Image Builder
DeleteContainerRecipe
Delete
Yes
Amazon EC2 Image Builder
DeleteDistributionConfiguration
Delete
Yes
Amazon EC2 Image Builder
DeleteImage
Delete
Yes
Amazon EC2 Image Builder
DeleteImagePipeline
Delete
Yes
Amazon EC2 Image Builder
DeleteImageRecipe
Delete
Yes
Amazon EC2 Image Builder
DeleteInfrastructureConfiguration
Delete
Yes
Amazon EC2 Image Builder
GetComponent
View
Yes
Amazon EC2 Image Builder
GetComponentPolicy
View
Yes
Amazon EC2 Image Builder
GetContainerRecipe
View
Yes
Amazon EC2 Image Builder
GetContainerRecipePolicy
View
Yes
Amazon EC2 Image Builder
GetDistributionConfiguration
View
Yes
Amazon EC2 Image Builder
GetImage
View
Yes
Amazon EC2 Image Builder
GetImagePipeline
View
Yes
Amazon EC2 Image Builder
GetImagePolicy
View
Yes
Amazon EC2 Image Builder
GetImageRecipe
View
Yes
Amazon EC2 Image Builder
GetImageRecipePolicy
View
Yes
Amazon EC2 Image Builder
GetInfrastructureConfiguration
View
Yes
Amazon EC2 Image Builder
ImportComponent
Create
Yes
Amazon EC2 Image Builder
ListComponentBuildVersions
View
Yes
Amazon EC2 Image Builder
ListComponents
View
Yes
Amazon EC2 Image Builder
ListContainerRecipes
View
Yes
Amazon EC2 Image Builder
ListDistributionConfigurations
View
Yes
Amazon EC2 Image Builder
ListImageBuildVersions
View
Yes
Amazon EC2 Image Builder
ListImagePackages
View
Yes
Amazon EC2 Image Builder
ListImagePipelineImages
View
Yes
Amazon EC2 Image Builder
ListImagePipelines
View
Yes
Amazon EC2 Image Builder
ListImageRecipes
View
Yes
Amazon EC2 Image Builder
ListImages
View
Yes
Amazon EC2 Image Builder
ListInfrastructureConfigurations
View
Yes
Amazon EC2 Image Builder
ListTagsForResource
View
Yes
Amazon EC2 Image Builder
TagResource
Create
Yes
Amazon EC2 Image Builder
PutComponentPolicy
Edit
Yes
Amazon EC2 Image Builder
PutContainerRecipePolicy
Edit
Yes
Amazon EC2 Image Builder
PutImagePolicy
Edit
Yes
Amazon EC2 Image Builder
PutImageRecipePolicy
Edit
Yes
Amazon EC2 Image Builder
StartImagePipelineExecution
Start
Yes
Amazon EC2 Image Builder
UntagResource
Delete
Yes
Amazon EC2 Image Builder
UpdateDistributionConfiguration
Edit
Yes
Amazon EC2 Image Builder
UpdateImagePipeline
Edit
Yes
Amazon EC2 Image Builder
UpdateInfrastructureConfiguration
Edit
Yes
Amazon Step Functions
CreateActivity
Create
Yes
Amazon Step Functions
CreateStateMachine
Create
Yes
Amazon Step Functions
DeleteActivity
Delete
Yes
Amazon Step Functions
DeleteStateMachine
Delete
Yes
Amazon Step Functions
DescribeActivity
View
Yes
Amazon Step Functions
DescribeExecution
View
Yes
Amazon Step Functions
DescribeStateMachine
View
Yes
Amazon Step Functions
DescribeStateMachineForExecution
View
Yes
Amazon Step Functions
GetActivityTask
View
Yes
Amazon Step Functions
GetExecutionHistory
View
Yes
Amazon Step Functions
ListActivities
View
Yes
Amazon Step Functions
ListExecutions
View
Yes
Amazon Step Functions
ListStateMachines
View
Yes
Amazon Step Functions
ListTagsForResource
View
Yes
Amazon Step Functions
SendTaskFailure
Send
Yes
Amazon Step Functions
SendTaskHeartbeat
Send
Yes
Amazon Step Functions
SendTaskSuccess
Send
Yes
Amazon Step Functions
StartExecution
Start
Yes
Amazon Step Functions
StartSyncExecution
Start
Yes
Amazon Step Functions
StopExecution
Stop
Yes
Amazon Step Functions
TagResource
Create
Yes
Amazon Step Functions
UntagResource
Delete
Yes
Amazon Step Functions
UpdateStateMachine
Edit
Yes
Amazon Connect Contact Lens
ListRealtimeContactAnalysisSegments
View
Yes
Amazon Nimble Studio
AcceptEulas
Approve
Yes
Amazon Nimble Studio
ListEulaAcceptances
View
Yes
Amazon Nimble Studio
CreateLaunchProfile
Create
Yes
Amazon Nimble Studio
ListLaunchProfiles
View
Yes
Amazon Nimble Studio
CreateStreamingImage
Create
Yes
Amazon Nimble Studio
ListStreamingImages
View
Yes
Amazon Nimble Studio
CreateStreamingSession
Create
Yes
Amazon Nimble Studio
ListStreamingSessions
View
Yes
Amazon Nimble Studio
CreateStreamingSessionStream
Create
Yes
Amazon Nimble Studio
CreateStudio
Create
Yes
Amazon Nimble Studio
ListStudios
View
Yes
Amazon Nimble Studio
CreateStudioComponent
Create
Yes
Amazon Nimble Studio
ListStudioComponents
View
Yes
Amazon Nimble Studio
DeleteLaunchProfile
Delete
Yes
Amazon Nimble Studio
GetLaunchProfile
View
Yes
Amazon Nimble Studio
UpdateLaunchProfile
Edit
Yes
Amazon Nimble Studio
DeleteLaunchProfileMember
Delete
Yes
Amazon Nimble Studio
GetLaunchProfileMember
View
Yes
Amazon Nimble Studio
UpdateLaunchProfileMember
Edit
Yes
Amazon Nimble Studio
DeleteStreamingImage
Delete
Yes
Amazon Nimble Studio
GetStreamingImage
View
Yes
Amazon Nimble Studio
UpdateStreamingImage
Edit
Yes
Amazon Nimble Studio
DeleteStreamingSession
Delete
Yes
Amazon Nimble Studio
GetStreamingSession
View
Yes
Amazon Nimble Studio
DeleteStudio
Delete
Yes
Amazon Nimble Studio
GetStudio
View
Yes
Amazon Nimble Studio
UpdateStudio
Edit
Yes
Amazon Nimble Studio
DeleteStudioComponent
Delete
Yes
Amazon Nimble Studio
GetStudioComponent
View
Yes
Amazon Nimble Studio
UpdateStudioComponent
Edit
Yes
Amazon Nimble Studio
DeleteStudioMember
Delete
Yes
Amazon Nimble Studio
GetStudioMember
View
Yes
Amazon Nimble Studio
GetEula
View
Yes
Amazon Nimble Studio
GetLaunchProfileDetails
View
Yes
Amazon Nimble Studio
GetLaunchProfileInitialization
View
Yes
Amazon Nimble Studio
GetStreamingSessionStream
View
Yes
Amazon Nimble Studio
ListEulas
View
Yes
Amazon Nimble Studio
ListLaunchProfileMembers
View
Yes
Amazon Nimble Studio
PutLaunchProfileMembers
Edit
Yes
Amazon Nimble Studio
ListStudioMembers
View
Yes
Amazon Nimble Studio
PutStudioMembers
Edit
Yes
Amazon Nimble Studio
ListTagsForResource
View
Yes
Amazon Nimble Studio
TagResource
Create
Yes
Amazon Nimble Studio
StartStudioSSOConfigurationRepair
Start
Yes
Amazon Nimble Studio
UntagResource
Delete
Yes
Amazon AppSync
CreateApiCache
Create
Yes
Amazon AppSync
DeleteApiCache
Delete
Yes
Amazon AppSync
GetApiCache
View
Yes
Amazon AppSync
CreateApiKey
Create
Yes
Amazon AppSync
ListApiKeys
View
Yes
Amazon AppSync
CreateDataSource
Create
Yes
Amazon AppSync
ListDataSources
View
Yes
Amazon AppSync
CreateFunction
Create
Yes
Amazon AppSync
ListFunctions
View
Yes
Amazon AppSync
CreateGraphqlApi
Create
Yes
Amazon AppSync
ListGraphqlApis
View
Yes
Amazon AppSync
CreateResolver
Create
Yes
Amazon AppSync
ListResolvers
View
Yes
Amazon AppSync
CreateType
Create
Yes
Amazon AppSync
DeleteApiKey
Delete
Yes
Amazon AppSync
UpdateApiKey
Edit
Yes
Amazon AppSync
DeleteDataSource
Delete
Yes
Amazon AppSync
GetDataSource
View
Yes
Amazon AppSync
UpdateDataSource
Edit
Yes
Amazon AppSync
DeleteFunction
Delete
Yes
Amazon AppSync
GetFunction
View
Yes
Amazon AppSync
UpdateFunction
Edit
Yes
Amazon AppSync
DeleteGraphqlApi
Delete
Yes
Amazon AppSync
GetGraphqlApi
View
Yes
Amazon AppSync
UpdateGraphqlApi
Edit
Yes
Amazon AppSync
DeleteResolver
Delete
Yes
Amazon AppSync
GetResolver
View
Yes
Amazon AppSync
UpdateResolver
Edit
Yes
Amazon AppSync
DeleteType
Delete
Yes
Amazon AppSync
UpdateType
Edit
Yes
Amazon AppSync
FlushApiCache
Delete
Yes
Amazon AppSync
GetIntrospectionSchema
View
Yes
Amazon AppSync
GetSchemaCreationStatus
View
Yes
Amazon AppSync
StartSchemaCreation
Start
Yes
Amazon AppSync
GetType
View
Yes
Amazon AppSync
ListResolversByFunction
View
Yes
Amazon AppSync
ListTagsForResource
View
Yes
Amazon AppSync
TagResource
Create
Yes
Amazon AppSync
ListTypes
View
Yes
Amazon AppSync
UntagResource
Delete
Yes
Amazon AppSync
UpdateApiCache
Edit
Yes
Amazon X-Ray
GetTraces
View
Yes
Amazon X-Ray
CreateGroup
Create
Yes
Amazon X-Ray
CreateSamplingRule
Create
Yes
Amazon X-Ray
DeleteGroup
Delete
Yes
Amazon X-Ray
DeleteSamplingRule
Delete
Yes
Amazon X-Ray
GetEncryptionConfig
View
Yes
Amazon X-Ray
GetGroup
View
Yes
Amazon X-Ray
GetGroups
View
Yes
Amazon X-Ray
GetInsight
View
Yes
Amazon X-Ray
GetInsightEvents
View
Yes
Amazon X-Ray
GetInsightImpactGraph
View
Yes
Amazon X-Ray
GetInsightSummaries
View
Yes
Amazon X-Ray
GetSamplingRules
View
Yes
Amazon X-Ray
GetSamplingStatisticSummaries
View
Yes
Amazon X-Ray
GetSamplingTargets
View
Yes
Amazon X-Ray
GetServiceGraph
View
Yes
Amazon X-Ray
GetTimeSeriesServiceStatistics
View
Yes
Amazon X-Ray
GetTraceGraph
View
Yes
Amazon X-Ray
GetTraceSummaries
View
Yes
Amazon X-Ray
ListTagsForResource
View
Yes
Amazon X-Ray
PutEncryptionConfig
Edit
Yes
Amazon X-Ray
PutTelemetryRecords
Edit
Yes
Amazon X-Ray
PutTraceSegments
Edit
Yes
Amazon X-Ray
TagResource
Create
Yes
Amazon X-Ray
UntagResource
Delete
Yes
Amazon X-Ray
UpdateGroup
Edit
Yes
Amazon X-Ray
UpdateSamplingRule
Edit
Yes
Amazon Pinpoint Email Service
CreateConfigurationSet
Create
Yes
Amazon Pinpoint Email Service
ListConfigurationSets
View
Yes
Amazon Pinpoint Email Service
CreateConfigurationSetEventDestination
Create
Yes
Amazon Pinpoint Email Service
GetConfigurationSetEventDestinations
View
Yes
Amazon Pinpoint Email Service
CreateDedicatedIpPool
Create
Yes
Amazon Pinpoint Email Service
ListDedicatedIpPools
View
Yes
Amazon Pinpoint Email Service
CreateDeliverabilityTestReport
Create
Yes
Amazon Pinpoint Email Service
CreateEmailIdentity
Create
Yes
Amazon Pinpoint Email Service
ListEmailIdentities
View
Yes
Amazon Pinpoint Email Service
DeleteConfigurationSet
Delete
Yes
Amazon Pinpoint Email Service
GetConfigurationSet
View
Yes
Amazon Pinpoint Email Service
DeleteConfigurationSetEventDestination
Delete
Yes
Amazon Pinpoint Email Service
UpdateConfigurationSetEventDestination
Edit
Yes
Amazon Pinpoint Email Service
DeleteDedicatedIpPool
Delete
Yes
Amazon Pinpoint Email Service
DeleteEmailIdentity
Delete
Yes
Amazon Pinpoint Email Service
GetEmailIdentity
View
Yes
Amazon Pinpoint Email Service
GetAccount
View
Yes
Amazon Pinpoint Email Service
GetBlacklistReports
View
Yes
Amazon Pinpoint Email Service
GetDedicatedIp
View
Yes
Amazon Pinpoint Email Service
GetDedicatedIps
View
Yes
Amazon Pinpoint Email Service
GetDeliverabilityDashboardOptions
View
Yes
Amazon Pinpoint Email Service
PutDeliverabilityDashboardOption
Edit
Yes
Amazon Pinpoint Email Service
GetDeliverabilityTestReport
View
Yes
Amazon Pinpoint Email Service
GetDomainDeliverabilityCampaign
View
Yes
Amazon Pinpoint Email Service
GetDomainStatisticsReport
View
Yes
Amazon Pinpoint Email Service
ListDeliverabilityTestReports
View
Yes
Amazon Pinpoint Email Service
ListDomainDeliverabilityCampaigns
View
Yes
Amazon Pinpoint Email Service
ListTagsForResource
View
Yes
Amazon Pinpoint Email Service
PutAccountDedicatedIpWarmupAttributes
Edit
Yes
Amazon Pinpoint Email Service
PutAccountSendingAttributes
Edit
Yes
Amazon Pinpoint Email Service
PutConfigurationSetDeliveryOptions
Edit
Yes
Amazon Pinpoint Email Service
PutConfigurationSetReputationOptions
Edit
Yes
Amazon Pinpoint Email Service
PutConfigurationSetSendingOptions
Edit
Yes
Amazon Pinpoint Email Service
PutConfigurationSetTrackingOptions
Edit
Yes
Amazon Pinpoint Email Service
PutDedicatedIpInPool
Edit
Yes
Amazon Pinpoint Email Service
PutDedicatedIpWarmupAttributes
Edit
Yes
Amazon Pinpoint Email Service
PutEmailIdentityDkimAttributes
Edit
Yes
Amazon Pinpoint Email Service
PutEmailIdentityFeedbackAttributes
Edit
Yes
Amazon Pinpoint Email Service
PutEmailIdentityMailFromAttributes
Edit
Yes
Amazon Pinpoint Email Service
SendEmail
Send
Yes
Amazon Pinpoint Email Service
TagResource
Create
Yes
Amazon Pinpoint Email Service
UntagResource
Delete
Yes
Amazon CloudHSM
AddTagsToResource
Create
Yes
Amazon CloudHSM
CreateHapg
Create
Yes
Amazon CloudHSM
CreateHsm
Create
Yes
Amazon CloudHSM
CreateLunaClient
Create
Yes
Amazon CloudHSM
DeleteHapg
Delete
Yes
Amazon CloudHSM
DeleteHsm
Delete
Yes
Amazon CloudHSM
DeleteLunaClient
Delete
Yes
Amazon CloudHSM
DescribeHapg
View
Yes
Amazon CloudHSM
DescribeHsm
View
Yes
Amazon CloudHSM
DescribeLunaClient
View
Yes
Amazon CloudHSM
GetConfig
View
Yes
Amazon CloudHSM
ListAvailableZones
View
Yes
Amazon CloudHSM
ListHapgs
View
Yes
Amazon CloudHSM
ListHsms
View
Yes
Amazon CloudHSM
ListLunaClients
View
Yes
Amazon CloudHSM
ListTagsForResource
View
Yes
Amazon CloudHSM
ModifyHapg
Edit
Yes
Amazon CloudHSM
ModifyHsm
Edit
Yes
Amazon CloudHSM
ModifyLunaClient
Edit
Yes
Amazon CloudHSM
RemoveTagsFromResource
Delete
Yes
Amazon CloudDirectory
AddFacetToObject
Create
Yes
Amazon CloudDirectory
ApplySchema
Edit
Yes
Amazon CloudDirectory
AttachObject
Attach
Yes
Amazon CloudDirectory
AttachPolicy
Attach
Yes
Amazon CloudDirectory
AttachToIndex
Attach
Yes
Amazon CloudDirectory
AttachTypedLink
Attach
Yes
Amazon CloudDirectory
Read
Create
Yes
Amazon CloudDirectory
Write
Edit
Yes
Amazon CloudDirectory
CreateDirectory
Create
Yes
Amazon CloudDirectory
CreateFacet
Create
Yes
Amazon CloudDirectory
CreateIndex
Create
Yes
Amazon CloudDirectory
CreateObject
Create
Yes
Amazon CloudDirectory
CreateSchema
Create
Yes
Amazon CloudDirectory
CreateTypedLinkFacet
Create
Yes
Amazon CloudDirectory
DeleteDirectory
Delete
Yes
Amazon CloudDirectory
DeleteFacet
Delete
Yes
Amazon CloudDirectory
DeleteObject
Delete
Yes
Amazon CloudDirectory
DeleteSchema
Delete
Yes
Amazon CloudDirectory
DeleteTypedLinkFacet
Delete
Yes
Amazon CloudDirectory
DetachFromIndex
Delete
Yes
Amazon CloudDirectory
DetachObject
Delete
Yes
Amazon CloudDirectory
DetachPolicy
Delete
Yes
Amazon CloudDirectory
DetachTypedLink
Delete
Yes
Amazon CloudDirectory
DisableDirectory
Edit
Yes
Amazon CloudDirectory
EnableDirectory
Enable
Yes
Amazon CloudDirectory
GetAppliedSchemaVersion
View
Yes
Amazon CloudDirectory
GetDirectory
View
Yes
Amazon CloudDirectory
GetFacet
View
Yes
Amazon CloudDirectory
UpdateFacet
Edit
Yes
Amazon CloudDirectory
GetLinkAttributes
View
Yes
Amazon CloudDirectory
GetObjectAttributes
View
Yes
Amazon CloudDirectory
GetObjectInformation
View
Yes
Amazon CloudDirectory
GetSchemaAsJson
View
Yes
Amazon CloudDirectory
PutSchemaFromJson
Edit
Yes
Amazon CloudDirectory
GetTypedLinkFacetInformation
View
Yes
Amazon CloudDirectory
ListAppliedSchemaArns
View
Yes
Amazon CloudDirectory
ListAttachedIndices
View
Yes
Amazon CloudDirectory
ListDevelopmentSchemaArns
View
Yes
Amazon CloudDirectory
ListDirectories
View
Yes
Amazon CloudDirectory
ListFacetAttributes
View
Yes
Amazon CloudDirectory
ListFacetNames
View
Yes
Amazon CloudDirectory
ListIncomingTypedLinks
View
Yes
Amazon CloudDirectory
ListIndex
View
Yes
Amazon CloudDirectory
ListManagedSchemaArns
View
Yes
Amazon CloudDirectory
ListObjectAttributes
View
Yes
Amazon CloudDirectory
ListObjectChildren
View
Yes
Amazon CloudDirectory
ListObjectParentPaths
View
Yes
Amazon CloudDirectory
ListObjectParents
View
Yes
Amazon CloudDirectory
ListObjectPolicies
View
Yes
Amazon CloudDirectory
ListOutgoingTypedLinks
View
Yes
Amazon CloudDirectory
ListPolicyAttachments
View
Yes
Amazon CloudDirectory
ListPublishedSchemaArns
View
Yes
Amazon CloudDirectory
ListTagsForResource
View
Yes
Amazon CloudDirectory
ListTypedLinkFacetAttributes
View
Yes
Amazon CloudDirectory
ListTypedLinkFacetNames
View
Yes
Amazon CloudDirectory
LookupPolicy
Create
Yes
Amazon CloudDirectory
PublishSchema
Edit
Yes
Amazon CloudDirectory
RemoveFacetFromObject
Delete
Yes
Amazon CloudDirectory
TagResource
Create
Yes
Amazon CloudDirectory
UntagResource
Delete
Yes
Amazon CloudDirectory
UpdateLinkAttributes
Edit
Yes
Amazon CloudDirectory
UpdateObjectAttributes
Edit
Yes
Amazon CloudDirectory
UpdateSchema
Edit
Yes
Amazon CloudDirectory
UpdateTypedLinkFacet
Edit
Yes
Amazon CloudDirectory
UpgradeAppliedSchema
Edit
Yes
Amazon CloudDirectory
UpgradePublishedSchema
Edit
Yes
Amazon CodeGuru Profiler
AddNotificationChannels
Create
Yes
Amazon CodeGuru Profiler
GetNotificationConfiguration
View
Yes
Amazon CodeGuru Profiler
GetFrameMetricData
View
Yes
Amazon CodeGuru Profiler
ConfigureAgent
Create
Yes
Amazon CodeGuru Profiler
CreateProfilingGroup
Create
Yes
Amazon CodeGuru Profiler
DeleteProfilingGroup
Delete
Yes
Amazon CodeGuru Profiler
DescribeProfilingGroup
View
Yes
Amazon CodeGuru Profiler
UpdateProfilingGroup
Edit
Yes
Amazon CodeGuru Profiler
GetFindingsReportAccountSummary
View
Yes
Amazon CodeGuru Profiler
GetPolicy
View
Yes
Amazon CodeGuru Profiler
GetProfile
View
Yes
Amazon CodeGuru Profiler
GetRecommendations
View
Yes
Amazon CodeGuru Profiler
ListFindingsReports
View
Yes
Amazon CodeGuru Profiler
ListProfileTimes
View
Yes
Amazon CodeGuru Profiler
ListProfilingGroups
View
Yes
Amazon CodeGuru Profiler
ListTagsForResource
View
Yes
Amazon CodeGuru Profiler
TagResource
Create
Yes
Amazon CodeGuru Profiler
PostAgentProfile
Create
Yes
Amazon CodeGuru Profiler
PutPermission
Edit
Yes
Amazon CodeGuru Profiler
RemoveNotificationChannel
Delete
Yes
Amazon CodeGuru Profiler
RemovePermission
Delete
Yes
Amazon CodeGuru Profiler
SubmitFeedback
Create
Yes
Amazon CodeGuru Profiler
UntagResource
Delete
Yes
Amazon Migration Hub Config
CreateHomeRegionControl
Create
Yes
Amazon Migration Hub Config
DescribeHomeRegionControls
View
Yes
Amazon Migration Hub Config
GetHomeRegion
View
Yes
Amazon Elemental MediaStore
CreateContainer
Create
Yes
Amazon Elemental MediaStore
DeleteContainer
Delete
Yes
Amazon Elemental MediaStore
DeleteContainerPolicy
Delete
Yes
Amazon Elemental MediaStore
DeleteCorsPolicy
Delete
Yes
Amazon Elemental MediaStore
DeleteLifecyclePolicy
Delete
Yes
Amazon Elemental MediaStore
DeleteMetricPolicy
Delete
Yes
Amazon Elemental MediaStore
DescribeContainer
View
Yes
Amazon Elemental MediaStore
GetContainerPolicy
View
Yes
Amazon Elemental MediaStore
GetCorsPolicy
View
Yes
Amazon Elemental MediaStore
GetLifecyclePolicy
View
Yes
Amazon Elemental MediaStore
GetMetricPolicy
View
Yes
Amazon Elemental MediaStore
ListContainers
View
Yes
Amazon Elemental MediaStore
ListTagsForResource
View
Yes
Amazon Elemental MediaStore
PutContainerPolicy
Edit
Yes
Amazon Elemental MediaStore
PutCorsPolicy
Edit
Yes
Amazon Elemental MediaStore
PutLifecyclePolicy
Edit
Yes
Amazon Elemental MediaStore
PutMetricPolicy
Edit
Yes
Amazon Elemental MediaStore
StartAccessLogging
Start
Yes
Amazon Elemental MediaStore
StopAccessLogging
Stop
Yes
Amazon Elemental MediaStore
TagResource
Create
Yes
Amazon Elemental MediaStore
UntagResource
Delete
Yes
Amazon Elastic Container Registry Public
CheckLayerAvailability
Create
Yes
Amazon Elastic Container Registry Public
DeleteImage
Delete
Yes
Amazon Elastic Container Registry Public
CompleteLayerUpload
Create
Yes
Amazon Elastic Container Registry Public
CreateRepository
Create
Yes
Amazon Elastic Container Registry Public
DeleteRepository
Delete
Yes
Amazon Elastic Container Registry Public
DeleteRepositoryPolicy
Delete
Yes
Amazon Elastic Container Registry Public
DescribeImageTags
View
Yes
Amazon Elastic Container Registry Public
DescribeImages
View
Yes
Amazon Elastic Container Registry Public
DescribeRegistries
View
Yes
Amazon Elastic Container Registry Public
DescribeRepositories
View
Yes
Amazon Elastic Container Registry Public
GetAuthorizationToken
View
Yes
Amazon Elastic Container Registry Public
GetRegistryCatalogData
View
Yes
Amazon Elastic Container Registry Public
GetRepositoryCatalogData
View
Yes
Amazon Elastic Container Registry Public
GetRepositoryPolicy
View
Yes
Amazon Elastic Container Registry Public
InitiateLayerUpload
Create
Yes
Amazon Elastic Container Registry Public
ListTagsForResource
View
Yes
Amazon Elastic Container Registry Public
PutImage
Edit
Yes
Amazon Elastic Container Registry Public
PutRegistryCatalogData
Edit
Yes
Amazon Elastic Container Registry Public
PutRepositoryCatalogData
Edit
Yes
Amazon Elastic Container Registry Public
SetRepositoryPolicy
Create
Yes
Amazon Elastic Container Registry Public
TagResource
Create
Yes
Amazon Elastic Container Registry Public
UntagResource
Delete
Yes
Amazon Elastic Container Registry Public
UploadLayerPart
Upload
Yes
Amazon Service Catalog App Registry
AssociateAttributeGroup
Create
Yes
Amazon Service Catalog App Registry
DisassociateAttributeGroup
Delete
Yes
Amazon Service Catalog App Registry
AssociateResource
Create
Yes
Amazon Service Catalog App Registry
DisassociateResource
Delete
Yes
Amazon Service Catalog App Registry
GetAssociatedResource
View
Yes
Amazon Service Catalog App Registry
CreateApplication
Create
Yes
Amazon Service Catalog App Registry
ListApplications
View
Yes
Amazon Service Catalog App Registry
CreateAttributeGroup
Create
Yes
Amazon Service Catalog App Registry
ListAttributeGroups
View
Yes
Amazon Service Catalog App Registry
DeleteApplication
Delete
Yes
Amazon Service Catalog App Registry
GetApplication
View
Yes
Amazon Service Catalog App Registry
UpdateApplication
Edit
Yes
Amazon Service Catalog App Registry
DeleteAttributeGroup
Delete
Yes
Amazon Service Catalog App Registry
GetAttributeGroup
View
Yes
Amazon Service Catalog App Registry
UpdateAttributeGroup
Edit
Yes
Amazon Service Catalog App Registry
ListAssociatedAttributeGroups
View
Yes
Amazon Service Catalog App Registry
ListAssociatedResources
View
Yes
Amazon Service Catalog App Registry
ListTagsForResource
View
Yes
Amazon Service Catalog App Registry
TagResource
Create
Yes
Amazon Service Catalog App Registry
SyncResource
Create
Yes
Amazon Service Catalog App Registry
UntagResource
Delete
Yes
Amazon SSO OIDC
CreateToken
Create
Yes
Amazon SSO OIDC
RegisterClient
Register
Yes
Amazon SSO OIDC
StartDeviceAuthorization
Start
Yes
Amazon Access Analyzer
ApplyArchiveRule
Edit
Yes
Amazon Access Analyzer
CancelPolicyGeneration
Delete
Yes
Amazon Access Analyzer
GetGeneratedPolicy
View
Yes
Amazon Access Analyzer
CreateAccessPreview
Create
Yes
Amazon Access Analyzer
CreateAnalyzer
Create
Yes
Amazon Access Analyzer
ListAnalyzers
View
Yes
Amazon Access Analyzer
CreateArchiveRule
Create
Yes
Amazon Access Analyzer
ListArchiveRules
View
Yes
Amazon Access Analyzer
DeleteAnalyzer
Delete
Yes
Amazon Access Analyzer
GetAnalyzer
View
Yes
Amazon Access Analyzer
DeleteArchiveRule
Delete
Yes
Amazon Access Analyzer
GetArchiveRule
View
Yes
Amazon Access Analyzer
UpdateArchiveRule
Edit
Yes
Amazon Access Analyzer
GetAccessPreview
View
Yes
Amazon Access Analyzer
GetAnalyzedResource
View
Yes
Amazon Access Analyzer
GetFinding
View
Yes
Amazon Access Analyzer
ListAccessPreviewFindings
View
Yes
Amazon Access Analyzer
ListAccessPreviews
View
Yes
Amazon Access Analyzer
ListAnalyzedResources
View
Yes
Amazon Access Analyzer
ListFindings
View
Yes
Amazon Access Analyzer
UpdateFindings
Edit
Yes
Amazon Access Analyzer
ListPolicyGenerations
View
Yes
Amazon Access Analyzer
StartPolicyGeneration
Start
Yes
Amazon Access Analyzer
ListTagsForResource
View
Yes
Amazon Access Analyzer
TagResource
Create
Yes
Amazon Access Analyzer
StartResourceScan
Start
Yes
Amazon Access Analyzer
UntagResource
Delete
Yes
Amazon Access Analyzer
ValidatePolicy
Create
Yes
Amazon SageMaker Feature Store Runtime
GetRecord
View
Yes
Amazon SageMaker Feature Store Runtime
DeleteRecord
Delete
Yes
Amazon SageMaker Feature Store Runtime
PutRecord
Edit
Yes
Amazon IoT Secure Tunneling
CloseTunnel
Create
Yes
Amazon IoT Secure Tunneling
DescribeTunnel
View
Yes
Amazon IoT Secure Tunneling
ListTagsForResource
View
Yes
Amazon IoT Secure Tunneling
ListTunnels
View
Yes
Amazon IoT Secure Tunneling
OpenTunnel
Create
Yes
Amazon IoT Secure Tunneling
TagResource
Create
Yes
Amazon IoT Secure Tunneling
UntagResource
Delete
Yes
Amazon Comprehend Medical
DescribeEntitiesDetectionVJob
View
Yes
Amazon Comprehend Medical
DescribeICDCMInferenceJob
View
Yes
Amazon Comprehend Medical
DescribePHIDetectionJob
View
Yes
Amazon Comprehend Medical
DescribeRxNormInferenceJob
View
Yes
Amazon Comprehend Medical
DetectEntities
Create
Yes
Amazon Comprehend Medical
DetectEntitiesV
Create
Yes
Amazon Comprehend Medical
DetectPHI
Create
Yes
Amazon Comprehend Medical
InferICDCM
Create
Yes
Amazon Comprehend Medical
InferRxNorm
Create
Yes
Amazon Comprehend Medical
ListEntitiesDetectionVJobs
View
Yes
Amazon Comprehend Medical
ListICDCMInferenceJobs
View
Yes
Amazon Comprehend Medical
ListPHIDetectionJobs
View
Yes
Amazon Comprehend Medical
ListRxNormInferenceJobs
View
Yes
Amazon Comprehend Medical
StartEntitiesDetectionVJob
Start
Yes
Amazon Comprehend Medical
StartICDCMInferenceJob
Start
Yes
Amazon Comprehend Medical
StartPHIDetectionJob
Start
Yes
Amazon Comprehend Medical
StartRxNormInferenceJob
Start
Yes
Amazon Comprehend Medical
StopEntitiesDetectionVJob
Stop
Yes
Amazon Comprehend Medical
StopICDCMInferenceJob
Stop
Yes
Amazon Comprehend Medical
StopPHIDetectionJob
Stop
Yes
Amazon Comprehend Medical
StopRxNormInferenceJob
Stop
Yes
Amazon Managed Streaming for Kafka
AssociateScramSecret
Create
Yes
Amazon Managed Streaming for Kafka
DisassociateScramSecret
Delete
Yes
Amazon Managed Streaming for Kafka
ListScramSecrets
View
Yes
Amazon Managed Streaming for Kafka
CreateCluster
Create
Yes
Amazon Managed Streaming for Kafka
ListClusters
View
Yes
Amazon Managed Streaming for Kafka
CreateConfiguration
Create
Yes
Amazon Managed Streaming for Kafka
ListConfigurations
View
Yes
Amazon Managed Streaming for Kafka
DeleteCluster
Delete
Yes
Amazon Managed Streaming for Kafka
DescribeCluster
View
Yes
Amazon Managed Streaming for Kafka
DeleteConfiguration
Delete
Yes
Amazon Managed Streaming for Kafka
DescribeConfiguration
View
Yes
Amazon Managed Streaming for Kafka
UpdateConfiguration
Edit
Yes
Amazon Managed Streaming for Kafka
DescribeClusterOperation
View
Yes
Amazon Managed Streaming for Kafka
DescribeConfigurationRevision
View
Yes
Amazon Managed Streaming for Kafka
GetBootstrapBrokers
View
Yes
Amazon Managed Streaming for Kafka
GetCompatibleKafkaVersions
View
Yes
Amazon Managed Streaming for Kafka
ListClusterOperations
View
Yes
Amazon Managed Streaming for Kafka
ListConfigurationRevisions
View
Yes
Amazon Managed Streaming for Kafka
ListKafkaVersions
View
Yes
Amazon Managed Streaming for Kafka
ListNodes
View
Yes
Amazon Managed Streaming for Kafka
ListTagsForResource
View
Yes
Amazon Managed Streaming for Kafka
TagResource
Create
Yes
Amazon Managed Streaming for Kafka
RebootBroker
Reboot
Yes
Amazon Managed Streaming for Kafka
UntagResource
Delete
Yes
Amazon Managed Streaming for Kafka
UpdateBrokerCount
Edit
Yes
Amazon Managed Streaming for Kafka
UpdateBrokerType
Edit
Yes
Amazon Managed Streaming for Kafka
UpdateBrokerStorage
Edit
Yes
Amazon Managed Streaming for Kafka
UpdateClusterConfiguration
Edit
Yes
Amazon Managed Streaming for Kafka
UpdateClusterKafkaVersion
Edit
Yes
Amazon Managed Streaming for Kafka
UpdateMonitoring
Edit
Yes
Amazon Managed Streaming for Kafka
UpdateSecurity
Edit
Yes
Amazon Elemental MediaStore Data Plane
DeleteObject
Delete
Yes
Amazon Elemental MediaStore Data Plane
DescribeObject
View
Yes
Amazon Elemental MediaStore Data Plane
GetObject
View
Yes
Amazon Elemental MediaStore Data Plane
PutObject
Edit
Yes
Amazon Elemental MediaStore Data Plane
ListItems
View
Yes
Amazon Kinesis Firehose
CreateDeliveryStream
Create
Yes
Amazon Kinesis Firehose
DeleteDeliveryStream
Delete
Yes
Amazon Kinesis Firehose
DescribeDeliveryStream
View
Yes
Amazon Kinesis Firehose
ListDeliveryStreams
View
Yes
Amazon Kinesis Firehose
ListTagsForDeliveryStream
View
Yes
Amazon Kinesis Firehose
PutRecord
Edit
Yes
Amazon Kinesis Firehose
StartDeliveryStreamEncryption
Start
Yes
Amazon Kinesis Firehose
StopDeliveryStreamEncryption
Stop
Yes
Amazon Kinesis Firehose
TagDeliveryStream
Create
Yes
Amazon Kinesis Firehose
UntagDeliveryStream
Delete
Yes
Amazon Kinesis Firehose
UpdateDestination
Edit
Yes
Amazon Cost and Usage Report Service
DeleteReportDefinition
Delete
Yes
Amazon Cost and Usage Report Service
DescribeReportDefinitions
View
Yes
Amazon Cost and Usage Report Service
ModifyReportDefinition
Edit
Yes
Amazon Cost and Usage Report Service
PutReportDefinition
Edit
Yes
Amazon SageMaker Runtime
InvokeEndpoint
Create
Yes
Amazon SageMaker Runtime
InvokeEndpointAsync
Create
Yes
Amazon Global Accelerator
AddCustomRoutingEndpoints
Create
Yes
Amazon Global Accelerator
AdvertiseByoipCidr
View
Yes
Amazon Global Accelerator
AllowCustomRoutingTraffic
Create
Yes
Amazon Global Accelerator
CreateAccelerator
Create
Yes
Amazon Global Accelerator
CreateCustomRoutingAccelerator
Create
Yes
Amazon Global Accelerator
CreateCustomRoutingEndpointGroup
Create
Yes
Amazon Global Accelerator
CreateCustomRoutingListener
Create
Yes
Amazon Global Accelerator
CreateEndpointGroup
Create
Yes
Amazon Global Accelerator
CreateListener
Create
Yes
Amazon Global Accelerator
DeleteAccelerator
Delete
Yes
Amazon Global Accelerator
DeleteCustomRoutingAccelerator
Delete
Yes
Amazon Global Accelerator
DeleteCustomRoutingEndpointGroup
Delete
Yes
Amazon Global Accelerator
DeleteCustomRoutingListener
Delete
Yes
Amazon Global Accelerator
DeleteEndpointGroup
Delete
Yes
Amazon Global Accelerator
DeleteListener
Delete
Yes
Amazon Global Accelerator
DenyCustomRoutingTraffic
Create
Yes
Amazon Global Accelerator
DeprovisionByoipCidr
Delete
Yes
Amazon Global Accelerator
DescribeAccelerator
View
Yes
Amazon Global Accelerator
DescribeAcceleratorAttributes
View
Yes
Amazon Global Accelerator
DescribeCustomRoutingAccelerator
View
Yes
Amazon Global Accelerator
DescribeCustomRoutingAcceleratorAttributes
View
Yes
Amazon Global Accelerator
DescribeCustomRoutingEndpointGroup
View
Yes
Amazon Global Accelerator
DescribeCustomRoutingListener
View
Yes
Amazon Global Accelerator
DescribeEndpointGroup
View
Yes
Amazon Global Accelerator
DescribeListener
View
Yes
Amazon Global Accelerator
ListAccelerators
View
Yes
Amazon Global Accelerator
ListByoipCidrs
View
Yes
Amazon Global Accelerator
ListCustomRoutingAccelerators
View
Yes
Amazon Global Accelerator
ListCustomRoutingEndpointGroups
View
Yes
Amazon Global Accelerator
ListCustomRoutingListeners
View
Yes
Amazon Global Accelerator
ListCustomRoutingPortMappings
View
Yes
Amazon Global Accelerator
ListCustomRoutingPortMappingsByDestination
View
Yes
Amazon Global Accelerator
ListEndpointGroups
View
Yes
Amazon Global Accelerator
ListListeners
View
Yes
Amazon Global Accelerator
ListTagsForResource
View
Yes
Amazon Global Accelerator
ProvisionByoipCidr
Create
Yes
Amazon Global Accelerator
RemoveCustomRoutingEndpoints
Delete
Yes
Amazon Global Accelerator
TagResource
Create
Yes
Amazon Global Accelerator
UntagResource
Delete
Yes
Amazon Global Accelerator
UpdateAccelerator
Edit
Yes
Amazon Global Accelerator
UpdateAcceleratorAttributes
Edit
Yes
Amazon Global Accelerator
UpdateCustomRoutingAccelerator
Edit
Yes
Amazon Global Accelerator
UpdateCustomRoutingAcceleratorAttributes
Edit
Yes
Amazon Global Accelerator
UpdateCustomRoutingListener
Edit
Yes
Amazon Global Accelerator
UpdateEndpointGroup
Edit
Yes
Amazon Global Accelerator
UpdateListener
Edit
Yes
Amazon Global Accelerator
WithdrawByoipCidr
Delete
Yes
Amazon S3 on Outposts
CreateEndpoint
Create
Yes
Amazon S3 on Outposts
DeleteEndpoint
Delete
Yes
Amazon S3 on Outposts
ListEndpoints
View
Yes
Amazon Simple Email Service
CloneReceiptRuleSet
View
Yes
Amazon Simple Email Service
CloneReceiptRuleSet
Create
Yes
Amazon Simple Email Service
CreateConfigurationSet
Create
Yes
Amazon Simple Email Service
CreateConfigurationSetEventDestination
Create
Yes
Amazon Simple Email Service
CreateConfigurationSetTrackingOptions
Create
Yes
Amazon Simple Email Service
CreateCustomVerificationEmailTemplate
Create
Yes
Amazon Simple Email Service
CreateReceiptFilter
Create
Yes
Amazon Simple Email Service
CreateReceiptRule
Create
Yes
Amazon Simple Email Service
CreateReceiptRuleSet
Create
Yes
Amazon Simple Email Service
CreateTemplate
Create
Yes
Amazon Simple Email Service
DeleteConfigurationSet
Delete
Yes
Amazon Simple Email Service
DeleteConfigurationSetEventDestination
Delete
Yes
Amazon Simple Email Service
DeleteConfigurationSetTrackingOptions
Delete
Yes
Amazon Simple Email Service
DeleteCustomVerificationEmailTemplate
Delete
Yes
Amazon Simple Email Service
DeleteIdentity
Delete
Yes
Amazon Simple Email Service
DeleteIdentityPolicy
Delete
Yes
Amazon Simple Email Service
DeleteReceiptFilter
Delete
Yes
Amazon Simple Email Service
DeleteReceiptRule
Delete
Yes
Amazon Simple Email Service
DeleteReceiptRuleSet
Delete
Yes
Amazon Simple Email Service
DeleteTemplate
Delete
Yes
Amazon Simple Email Service
DeleteVerifiedEmailAddress
Delete
Yes
Amazon Simple Email Service
DescribeActiveReceiptRuleSet
View
Yes
Amazon Simple Email Service
DescribeConfigurationSet
View
Yes
Amazon Simple Email Service
DescribeReceiptRule
View
Yes
Amazon Simple Email Service
DescribeReceiptRuleSet
View
Yes
Amazon Simple Email Service
GetAccountSendingEnabled
View
Yes
Amazon Simple Email Service
GetCustomVerificationEmailTemplate
View
Yes
Amazon Simple Email Service
GetIdentityDkimAttributes
View
Yes
Amazon Simple Email Service
GetIdentityMailFromDomainAttributes
View
Yes
Amazon Simple Email Service
GetIdentityNotificationAttributes
View
Yes
Amazon Simple Email Service
GetIdentityPolicies
View
Yes
Amazon Simple Email Service
GetIdentityVerificationAttributes
View
Yes
Amazon Simple Email Service
GetSendQuota
View
Yes
Amazon Simple Email Service
GetSendStatistics
View
Yes
Amazon Simple Email Service
GetTemplate
View
Yes
Amazon Simple Email Service
ListConfigurationSets
View
Yes
Amazon Simple Email Service
ListCustomVerificationEmailTemplates
View
Yes
Amazon Simple Email Service
ListIdentities
View
Yes
Amazon Simple Email Service
ListIdentityPolicies
View
Yes
Amazon Simple Email Service
ListReceiptFilters
View
Yes
Amazon Simple Email Service
ListReceiptRuleSets
View
Yes
Amazon Simple Email Service
ListTemplates
View
Yes
Amazon Simple Email Service
ListVerifiedEmailAddresses
View
Yes
Amazon Simple Email Service
PutConfigurationSetDeliveryOptions
Edit
Yes
Amazon Simple Email Service
PutIdentityPolicy
Edit
Yes
Amazon Simple Email Service
ReorderReceiptRuleSet
View
Yes
Amazon Simple Email Service
ReorderReceiptRuleSet
Create
Yes
Amazon Simple Email Service
SendBounce
Send
Yes
Amazon Simple Email Service
SendBulkTemplatedEmail
Send
Yes
Amazon Simple Email Service
SendCustomVerificationEmail
Send
Yes
Amazon Simple Email Service
SendEmail
Send
Yes
Amazon Simple Email Service
SendRawEmail
Send
Yes
Amazon Simple Email Service
SendTemplatedEmail
Send
Yes
Amazon Simple Email Service
SetActiveReceiptRuleSet
Create
Yes
Amazon Simple Email Service
SetIdentityDkimEnabled
Create
Yes
Amazon Simple Email Service
SetIdentityFeedbackForwardingEnabled
Create
Yes
Amazon Simple Email Service
SetIdentityHeadersInNotificationsEnabled
Create
Yes
Amazon Simple Email Service
SetIdentityMailFromDomain
Create
Yes
Amazon Simple Email Service
SetIdentityNotificationTopic
Create
Yes
Amazon Simple Email Service
SetReceiptRulePosition
Create
Yes
Amazon Simple Email Service
TestRenderTemplate
View
Yes
Amazon Simple Email Service
TestRenderTemplate
Create
Yes
Amazon Simple Email Service
UpdateAccountSendingEnabled
Edit
Yes
Amazon Simple Email Service
UpdateConfigurationSetEventDestination
Edit
Yes
Amazon Simple Email Service
UpdateConfigurationSetReputationMetricsEnabled
Edit
Yes
Amazon Simple Email Service
UpdateConfigurationSetSendingEnabled
Edit
Yes
Amazon Simple Email Service
UpdateConfigurationSetTrackingOptions
Edit
Yes
Amazon Simple Email Service
UpdateCustomVerificationEmailTemplate
Edit
Yes
Amazon Simple Email Service
UpdateReceiptRule
Edit
Yes
Amazon Simple Email Service
UpdateTemplate
Edit
Yes
Amazon Simple Email Service
VerifyDomainDkim
View
Yes
Amazon Simple Email Service
VerifyDomainDkim
Create
Yes
Amazon Simple Email Service
VerifyDomainIdentity
View
Yes
Amazon Simple Email Service
VerifyDomainIdentity
Create
Yes
Amazon Simple Email Service
VerifyEmailAddress
View
Yes
Amazon Simple Email Service
VerifyEmailAddress
Create
Yes
Amazon Simple Email Service
VerifyEmailIdentity
View
Yes
Amazon Simple Email Service
VerifyEmailIdentity
Create
Yes
Amazon Shield
AssociateDRTLogBucket
Create
Yes
Amazon Shield
AssociateDRTRole
Create
Yes
Amazon Shield
AssociateHealthCheck
Create
Yes
Amazon Shield
AssociateProactiveEngagementDetails
Create
Yes
Amazon Shield
CreateProtection
Create
Yes
Amazon Shield
CreateProtectionGroup
Create
Yes
Amazon Shield
CreateSubscription
Create
Yes
Amazon Shield
DeleteProtection
Delete
Yes
Amazon Shield
DeleteProtectionGroup
Delete
Yes
Amazon Shield
DeleteSubscription
Delete
Yes
Amazon Shield
DescribeAttack
View
Yes
Amazon Shield
DescribeAttackStatistics
View
Yes
Amazon Shield
DescribeDRTAccess
View
Yes
Amazon Shield
DescribeEmergencyContactSettings
View
Yes
Amazon Shield
DescribeProtection
View
Yes
Amazon Shield
DescribeProtectionGroup
View
Yes
Amazon Shield
DescribeSubscription
View
Yes
Amazon Shield
DisableProactiveEngagement
Edit
Yes
Amazon Shield
DisassociateDRTLogBucket
Delete
Yes
Amazon Shield
DisassociateDRTRole
Delete
Yes
Amazon Shield
DisassociateHealthCheck
Delete
Yes
Amazon Shield
EnableProactiveEngagement
Enable
Yes
Amazon Shield
GetSubscriptionState
View
Yes
Amazon Shield
ListAttacks
View
Yes
Amazon Shield
ListProtectionGroups
View
Yes
Amazon Shield
ListProtections
View
Yes
Amazon Shield
ListResourcesInProtectionGroup
View
Yes
Amazon Shield
ListTagsForResource
View
Yes
Amazon Shield
TagResource
Create
Yes
Amazon Shield
UntagResource
Delete
Yes
Amazon Shield
UpdateEmergencyContactSettings
Edit
Yes
Amazon Shield
UpdateProtectionGroup
Edit
Yes
Amazon Shield
UpdateSubscription
Edit
Yes
Amazon GameLift
AcceptMatch
Approve
Yes
Amazon GameLift
ClaimGameServer
Create
Yes
Amazon GameLift
CreateAlias
Create
Yes
Amazon GameLift
CreateBuild
Create
Yes
Amazon GameLift
CreateFleet
Create
Yes
Amazon GameLift
CreateFleetLocations
Create
Yes
Amazon GameLift
CreateGameServerGroup
Create
Yes
Amazon GameLift
CreateGameSession
Create
Yes
Amazon GameLift
CreateGameSessionQueue
Create
Yes
Amazon GameLift
CreateMatchmakingConfiguration
Create
Yes
Amazon GameLift
CreateMatchmakingRuleSet
Create
Yes
Amazon GameLift
CreatePlayerSession
Create
Yes
Amazon GameLift
CreatePlayerSessions
Create
Yes
Amazon GameLift
CreateScript
Create
Yes
Amazon GameLift
CreateVpcPeeringAuthorization
Create
Yes
Amazon GameLift
CreateVpcPeeringConnection
Create
Yes
Amazon GameLift
DeleteAlias
Delete
Yes
Amazon GameLift
DeleteBuild
Delete
Yes
Amazon GameLift
DeleteFleet
Delete
Yes
Amazon GameLift
DeleteFleetLocations
Delete
Yes
Amazon GameLift
DeleteGameServerGroup
Delete
Yes
Amazon GameLift
DeleteGameSessionQueue
Delete
Yes
Amazon GameLift
DeleteMatchmakingConfiguration
Delete
Yes
Amazon GameLift
DeleteMatchmakingRuleSet
Delete
Yes
Amazon GameLift
DeleteScalingPolicy
Delete
Yes
Amazon GameLift
DeleteScript
Delete
Yes
Amazon GameLift
DeleteVpcPeeringAuthorization
Delete
Yes
Amazon GameLift
DeleteVpcPeeringConnection
Delete
Yes
Amazon GameLift
DeregisterGameServer
Deregister
Yes
Amazon GameLift
DescribeAlias
View
Yes
Amazon GameLift
DescribeBuild
View
Yes
Amazon GameLift
DescribeECInstanceLimits
View
Yes
Amazon GameLift
DescribeFleetAttributes
View
Yes
Amazon GameLift
DescribeFleetCapacity
View
Yes
Amazon GameLift
DescribeFleetEvents
View
Yes
Amazon GameLift
DescribeFleetLocationAttributes
View
Yes
Amazon GameLift
DescribeFleetLocationCapacity
View
Yes
Amazon GameLift
DescribeFleetLocationUtilization
View
Yes
Amazon GameLift
DescribeFleetPortSettings
View
Yes
Amazon GameLift
DescribeFleetUtilization
View
Yes
Amazon GameLift
DescribeGameServer
View
Yes
Amazon GameLift
DescribeGameServerGroup
View
Yes
Amazon GameLift
DescribeGameServerInstances
View
Yes
Amazon GameLift
DescribeGameSessionDetails
View
Yes
Amazon GameLift
DescribeGameSessionPlacement
View
Yes
Amazon GameLift
DescribeGameSessionQueues
View
Yes
Amazon GameLift
DescribeGameSessions
View
Yes
Amazon GameLift
DescribeInstances
View
Yes
Amazon GameLift
DescribeMatchmaking
View
Yes
Amazon GameLift
DescribeMatchmakingConfigurations
View
Yes
Amazon GameLift
DescribeMatchmakingRuleSets
View
Yes
Amazon GameLift
DescribePlayerSessions
View
Yes
Amazon GameLift
DescribeRuntimeConfiguration
View
Yes
Amazon GameLift
DescribeScalingPolicies
View
Yes
Amazon GameLift
DescribeScript
View
Yes
Amazon GameLift
DescribeVpcPeeringAuthorizations
View
Yes
Amazon GameLift
DescribeVpcPeeringConnections
View
Yes
Amazon GameLift
GetGameSessionLogUrl
View
Yes
Amazon GameLift
GetInstanceAccess
View
Yes
Amazon GameLift
ListAliases
View
Yes
Amazon GameLift
ListBuilds
View
Yes
Amazon GameLift
ListFleets
View
Yes
Amazon GameLift
ListGameServerGroups
View
Yes
Amazon GameLift
ListGameServers
View
Yes
Amazon GameLift
ListScripts
View
Yes
Amazon GameLift
ListTagsForResource
View
Yes
Amazon GameLift
PutScalingPolicy
Edit
Yes
Amazon GameLift
RegisterGameServer
Register
Yes
Amazon GameLift
RequestUploadCredentials
Create
Yes
Amazon GameLift
ResolveAlias
Create
Yes
Amazon GameLift
ResumeGameServerGroup
Start
Yes
Amazon GameLift
SearchGameSessions
Search
Yes
Amazon GameLift
StartFleetActions
Start
Yes
Amazon GameLift
StartGameSessionPlacement
Start
Yes
Amazon GameLift
StartMatchBackfill
Start
Yes
Amazon GameLift
StartMatchmaking
Start
Yes
Amazon GameLift
StopFleetActions
Stop
Yes
Amazon GameLift
StopGameSessionPlacement
Stop
Yes
Amazon GameLift
StopMatchmaking
Stop
Yes
Amazon GameLift
SuspendGameServerGroup
Delete
Yes
Amazon GameLift
TagResource
Create
Yes
Amazon GameLift
UntagResource
Delete
Yes
Amazon GameLift
UpdateAlias
Edit
Yes
Amazon GameLift
UpdateBuild
Edit
Yes
Amazon GameLift
UpdateFleetAttributes
Edit
Yes
Amazon GameLift
UpdateFleetCapacity
Edit
Yes
Amazon GameLift
UpdateFleetPortSettings
Edit
Yes
Amazon GameLift
UpdateGameServer
Edit
Yes
Amazon GameLift
UpdateGameServerGroup
Edit
Yes
Amazon GameLift
UpdateGameSession
Edit
Yes
Amazon GameLift
UpdateGameSessionQueue
Edit
Yes
Amazon GameLift
UpdateMatchmakingConfiguration
Edit
Yes
Amazon GameLift
UpdateRuntimeConfiguration
Edit
Yes
Amazon GameLift
UpdateScript
Edit
Yes
Amazon GameLift
ValidateMatchmakingRuleSet
Create
Yes
Amazon Kinesis
AddTagsToStream
Create
Yes
Amazon Kinesis
CreateStream
Create
Yes
Amazon Kinesis
DecreaseStreamRetentionPeriod
Edit
Yes
Amazon Kinesis
DeleteStream
Delete
Yes
Amazon Kinesis
DeregisterStreamConsumer
Deregister
Yes
Amazon Kinesis
DescribeLimits
View
Yes
Amazon Kinesis
DescribeStream
View
Yes
Amazon Kinesis
DescribeStreamConsumer
View
Yes
Amazon Kinesis
DescribeStreamSummary
View
Yes
Amazon Kinesis
DisableEnhancedMonitoring
Edit
Yes
Amazon Kinesis
EnableEnhancedMonitoring
Enable
Yes
Amazon Kinesis
GetRecords
View
Yes
Amazon Kinesis
GetShardIterator
View
Yes
Amazon Kinesis
IncreaseStreamRetentionPeriod
Edit
Yes
Amazon Kinesis
ListShards
View
Yes
Amazon Kinesis
ListStreamConsumers
View
Yes
Amazon Kinesis
ListStreams
View
Yes
Amazon Kinesis
ListTagsForStream
View
Yes
Amazon Kinesis
MergeShards
Create
Yes
Amazon Kinesis
PutRecord
Edit
Yes
Amazon Kinesis
PutRecords
Edit
Yes
Amazon Kinesis
RegisterStreamConsumer
Register
Yes
Amazon Kinesis
RemoveTagsFromStream
Delete
Yes
Amazon Kinesis
SplitShard
Create
Yes
Amazon Kinesis
StartStreamEncryption
Start
Yes
Amazon Kinesis
StopStreamEncryption
Stop
Yes
Amazon Kinesis
UpdateShardCount
Edit
Yes
Amazon Pinpoint SMS and Voice Service
CreateConfigurationSet
Create
Yes
Amazon Pinpoint SMS and Voice Service
ListConfigurationSets
View
Yes
Amazon Pinpoint SMS and Voice Service
CreateConfigurationSetEventDestination
Create
Yes
Amazon Pinpoint SMS and Voice Service
GetConfigurationSetEventDestinations
View
Yes
Amazon Pinpoint SMS and Voice Service
DeleteConfigurationSet
Delete
Yes
Amazon Pinpoint SMS and Voice Service
DeleteConfigurationSetEventDestination
Delete
Yes
Amazon Pinpoint SMS and Voice Service
UpdateConfigurationSetEventDestination
Edit
Yes
Amazon Pinpoint SMS and Voice Service
SendVoiceMessage
Send
Yes
Amazon MemoryDB
UpdateCluster
Edit
Yes
Amazon MemoryDB
CopySnapshot
Copy
Yes
Amazon MemoryDB
CreateACL
Create
Yes
Amazon MemoryDB
CreateCluster
Create
Yes
Amazon MemoryDB
CreateParameterGroup
Create
Yes
Amazon MemoryDB
CreateSnapshot
Create
Yes
Amazon MemoryDB
CreateSubnetGroup
Create
Yes
Amazon MemoryDB
CreateUser
Create
Yes
Amazon MemoryDB
DeleteACL
Delete
Yes
Amazon MemoryDB
DeleteCluster
Delete
Yes
Amazon MemoryDB
DeleteParameterGroup
Delete
Yes
Amazon MemoryDB
DeleteSnapshot
Delete
Yes
Amazon MemoryDB
DeleteSubnetGroup
Delete
Yes
Amazon MemoryDB
DeleteUser
Delete
Yes
Amazon MemoryDB
DescribeACLs
View
Yes
Amazon MemoryDB
DescribeClusters
View
Yes
Amazon MemoryDB
DescribeEngineVersions
View
Yes
Amazon MemoryDB
DescribeEvents
View
Yes
Amazon MemoryDB
DescribeParameterGroups
View
Yes
Amazon MemoryDB
DescribeParameters
View
Yes
Amazon MemoryDB
DescribeServiceUpdates
View
Yes
Amazon MemoryDB
DescribeSnapshots
View
Yes
Amazon MemoryDB
DescribeSubnetGroups
View
Yes
Amazon MemoryDB
DescribeUsers
View
Yes
Amazon MemoryDB
FailoverShard
Create
Yes
Amazon MemoryDB
ListAllowedNodeTypeUpdates
View
Yes
Amazon MemoryDB
ListTags
View
Yes
Amazon MemoryDB
ResetParameterGroup
Edit
Yes
Amazon MemoryDB
TagResource
Create
Yes
Amazon MemoryDB
UntagResource
Delete
Yes
Amazon MemoryDB
UpdateACL
Edit
Yes
Amazon MemoryDB
UpdateParameterGroup
Edit
Yes
Amazon MemoryDB
UpdateSubnetGroup
Edit
Yes
Amazon MemoryDB
UpdateUser
Edit
Yes
Amazon FinSpace User Environment Management service
CreateEnvironment
Create
Yes
Amazon FinSpace User Environment Management service
ListEnvironments
View
Yes
Amazon FinSpace User Environment Management service
DeleteEnvironment
Delete
Yes
Amazon FinSpace User Environment Management service
GetEnvironment
View
Yes
Amazon FinSpace User Environment Management service
UpdateEnvironment
Edit
Yes
Amazon FinSpace User Environment Management service
ListTagsForResource
View
Yes
Amazon FinSpace User Environment Management service
TagResource
Create
Yes
Amazon FinSpace User Environment Management service
UntagResource
Delete
Yes
Amazon Transcribe Service
CreateCallAnalyticsCategory
Create
Yes
Amazon Transcribe Service
CreateLanguageModel
Create
Yes
Amazon Transcribe Service
CreateMedicalVocabulary
Create
Yes
Amazon Transcribe Service
CreateVocabulary
Create
Yes
Amazon Transcribe Service
CreateVocabularyFilter
Create
Yes
Amazon Transcribe Service
DeleteCallAnalyticsCategory
Delete
Yes
Amazon Transcribe Service
DeleteCallAnalyticsJob
Delete
Yes
Amazon Transcribe Service
DeleteLanguageModel
Delete
Yes
Amazon Transcribe Service
DeleteMedicalTranscriptionJob
Delete
Yes
Amazon Transcribe Service
DeleteMedicalVocabulary
Delete
Yes
Amazon Transcribe Service
DeleteTranscriptionJob
Delete
Yes
Amazon Transcribe Service
DeleteVocabulary
Delete
Yes
Amazon Transcribe Service
DeleteVocabularyFilter
Delete
Yes
Amazon Transcribe Service
DescribeLanguageModel
View
Yes
Amazon Transcribe Service
GetCallAnalyticsCategory
View
Yes
Amazon Transcribe Service
GetCallAnalyticsJob
View
Yes
Amazon Transcribe Service
GetMedicalTranscriptionJob
View
Yes
Amazon Transcribe Service
GetMedicalVocabulary
View
Yes
Amazon Transcribe Service
GetTranscriptionJob
View
Yes
Amazon Transcribe Service
GetVocabulary
View
Yes
Amazon Transcribe Service
GetVocabularyFilter
View
Yes
Amazon Transcribe Service
ListCallAnalyticsCategories
View
Yes
Amazon Transcribe Service
ListCallAnalyticsJobs
View
Yes
Amazon Transcribe Service
ListLanguageModels
View
Yes
Amazon Transcribe Service
ListMedicalTranscriptionJobs
View
Yes
Amazon Transcribe Service
ListMedicalVocabularies
View
Yes
Amazon Transcribe Service
ListTagsForResource
View
Yes
Amazon Transcribe Service
ListTranscriptionJobs
View
Yes
Amazon Transcribe Service
ListVocabularies
View
Yes
Amazon Transcribe Service
ListVocabularyFilters
View
Yes
Amazon Transcribe Service
StartCallAnalyticsJob
Start
Yes
Amazon Transcribe Service
StartMedicalTranscriptionJob
Start
Yes
Amazon Transcribe Service
StartTranscriptionJob
Start
Yes
Amazon Transcribe Service
TagResource
Create
Yes
Amazon Transcribe Service
UntagResource
Delete
Yes
Amazon Transcribe Service
UpdateCallAnalyticsCategory
Edit
Yes
Amazon Transcribe Service
UpdateMedicalVocabulary
Edit
Yes
Amazon Transcribe Service
UpdateVocabulary
Edit
Yes
Amazon Transcribe Service
UpdateVocabularyFilter
Edit
Yes
Amazon AmplifyBackend
CloneBackend
Create
Yes
Amazon AmplifyBackend
CreateBackend
Create
Yes
Amazon AmplifyBackend
CreateBackendAPI
Create
Yes
Amazon AmplifyBackend
CreateBackendAuth
Create
Yes
Amazon AmplifyBackend
CreateBackendConfig
Create
Yes
Amazon AmplifyBackend
CreateToken
Create
Yes
Amazon AmplifyBackend
DeleteBackend
Delete
Yes
Amazon AmplifyBackend
DeleteBackendAPI
Delete
Yes
Amazon AmplifyBackend
DeleteBackendAuth
Delete
Yes
Amazon AmplifyBackend
DeleteToken
Delete
Yes
Amazon AmplifyBackend
GenerateBackendAPIModels
Create
Yes
Amazon AmplifyBackend
GetBackend
View
Yes
Amazon AmplifyBackend
GetBackendAPI
View
Yes
Amazon AmplifyBackend
GetBackendAPIModels
View
Yes
Amazon AmplifyBackend
GetBackendAuth
View
Yes
Amazon AmplifyBackend
GetBackendJob
View
Yes
Amazon AmplifyBackend
UpdateBackendJob
Edit
Yes
Amazon AmplifyBackend
GetToken
View
Yes
Amazon AmplifyBackend
ImportBackendAuth
Create
Yes
Amazon AmplifyBackend
ListBackendJobs
View
Yes
Amazon AmplifyBackend
RemoveAllBackends
Delete
Yes
Amazon AmplifyBackend
RemoveBackendConfig
Delete
Yes
Amazon AmplifyBackend
UpdateBackendAPI
Edit
Yes
Amazon AmplifyBackend
UpdateBackendAuth
Edit
Yes
Amazon AmplifyBackend
UpdateBackendConfig
Edit
Yes
Amazon Schemas
CreateDiscoverer
Create
Yes
Amazon Schemas
ListDiscoverers
View
Yes
Amazon Schemas
CreateRegistry
Create
Yes
Amazon Schemas
DeleteRegistry
Delete
Yes
Amazon Schemas
DescribeRegistry
View
Yes
Amazon Schemas
UpdateRegistry
Edit
Yes
Amazon Schemas
CreateSchema
Create
Yes
Amazon Schemas
DeleteSchema
Delete
Yes
Amazon Schemas
DescribeSchema
View
Yes
Amazon Schemas
UpdateSchema
Edit
Yes
Amazon Schemas
DeleteDiscoverer
Delete
Yes
Amazon Schemas
DescribeDiscoverer
View
Yes
Amazon Schemas
UpdateDiscoverer
Edit
Yes
Amazon Schemas
DeleteResourcePolicy
Delete
Yes
Amazon Schemas
GetResourcePolicy
View
Yes
Amazon Schemas
PutResourcePolicy
Edit
Yes
Amazon Schemas
DeleteSchemaVersion
Delete
Yes
Amazon Schemas
DescribeCodeBinding
View
Yes
Amazon Schemas
PutCodeBinding
Edit
Yes
Amazon Schemas
ExportSchema
View
Yes
Amazon Schemas
GetCodeBindingSource
View
Yes
Amazon Schemas
GetDiscoveredSchema
View
Yes
Amazon Schemas
ListRegistries
View
Yes
Amazon Schemas
ListSchemaVersions
View
Yes
Amazon Schemas
ListSchemas
View
Yes
Amazon Schemas
ListTagsForResource
View
Yes
Amazon Schemas
TagResource
Create
Yes
Amazon Schemas
SearchSchemas
Search
Yes
Amazon Schemas
StartDiscoverer
Start
Yes
Amazon Schemas
StopDiscoverer
Stop
Yes
Amazon Schemas
UntagResource
Delete
Yes
Amazon Application Auto Scaling
DeleteScalingPolicy
Delete
Yes
Amazon Application Auto Scaling
DeleteScheduledAction
Delete
Yes
Amazon Application Auto Scaling
DeregisterScalableTarget
Deregister
Yes
Amazon Application Auto Scaling
DescribeScalableTargets
View
Yes
Amazon Application Auto Scaling
DescribeScalingActivities
View
Yes
Amazon Application Auto Scaling
DescribeScalingPolicies
View
Yes
Amazon Application Auto Scaling
DescribeScheduledActions
View
Yes
Amazon Application Auto Scaling
PutScalingPolicy
Edit
Yes
Amazon Application Auto Scaling
PutScheduledAction
Edit
Yes
Amazon Application Auto Scaling
RegisterScalableTarget
Register
Yes
Amazon IoT Events Data
AcknowledgeAlarm
Create
Yes
Amazon IoT Events Data
DisableAlarm
Edit
Yes
Amazon IoT Events Data
EnableAlarm
Enable
Yes
Amazon IoT Events Data
PutMessage
Edit
Yes
Amazon IoT Events Data
ResetAlarm
Edit
Yes
Amazon IoT Events Data
SnoozeAlarm
Create
Yes
Amazon IoT Events Data
UpdateDetector
Edit
Yes
Amazon IoT Events Data
DescribeAlarm
View
Yes
Amazon IoT Events Data
DescribeDetector
View
Yes
Amazon IoT Events Data
ListAlarms
View
Yes
Amazon IoT Events Data
ListDetectors
View
Yes
Amazon Prometheus Service
CreateWorkspace
Create
Yes
Amazon Prometheus Service
ListWorkspaces
View
Yes
Amazon Prometheus Service
DeleteWorkspace
Delete
Yes
Amazon Prometheus Service
DescribeWorkspace
View
Yes
Amazon Prometheus Service
ListTagsForResource
View
Yes
Amazon Prometheus Service
TagResource
Create
Yes
Amazon Prometheus Service
UntagResource
Delete
Yes
Amazon Prometheus Service
UpdateWorkspaceAlias
Edit
Yes
Amazon WorkMail
AssociateDelegateToResource
Create
Yes
Amazon WorkMail
AssociateMemberToGroup
Create
Yes
Amazon WorkMail
CancelMailboxExportJob
Delete
Yes
Amazon WorkMail
CreateAlias
Create
Yes
Amazon WorkMail
CreateGroup
Create
Yes
Amazon WorkMail
CreateMobileDeviceAccessRule
Create
Yes
Amazon WorkMail
CreateOrganization
Create
Yes
Amazon WorkMail
CreateResource
Create
Yes
Amazon WorkMail
CreateUser
Create
Yes
Amazon WorkMail
DeleteAccessControlRule
Delete
Yes
Amazon WorkMail
DeleteAlias
Delete
Yes
Amazon WorkMail
DeleteGroup
Delete
Yes
Amazon WorkMail
DeleteMailboxPermissions
Delete
Yes
Amazon WorkMail
DeleteMobileDeviceAccessRule
Delete
Yes
Amazon WorkMail
DeleteOrganization
Delete
Yes
Amazon WorkMail
DeleteResource
Delete
Yes
Amazon WorkMail
DeleteRetentionPolicy
Delete
Yes
Amazon WorkMail
DeleteUser
Delete
Yes
Amazon WorkMail
DeregisterFromWorkMail
Deregister
Yes
Amazon WorkMail
DescribeGroup
View
Yes
Amazon WorkMail
DescribeMailboxExportJob
View
Yes
Amazon WorkMail
DescribeOrganization
View
Yes
Amazon WorkMail
DescribeResource
View
Yes
Amazon WorkMail
DescribeUser
View
Yes
Amazon WorkMail
DisassociateDelegateFromResource
Delete
Yes
Amazon WorkMail
DisassociateMemberFromGroup
Delete
Yes
Amazon WorkMail
GetAccessControlEffect
View
Yes
Amazon WorkMail
GetDefaultRetentionPolicy
View
Yes
Amazon WorkMail
GetMailboxDetails
View
Yes
Amazon WorkMail
GetMobileDeviceAccessEffect
View
Yes
Amazon WorkMail
ListAccessControlRules
View
Yes
Amazon WorkMail
ListAliases
View
Yes
Amazon WorkMail
ListGroupMembers
View
Yes
Amazon WorkMail
ListGroups
View
Yes
Amazon WorkMail
ListMailboxExportJobs
View
Yes
Amazon WorkMail
ListMailboxPermissions
View
Yes
Amazon WorkMail
ListMobileDeviceAccessRules
View
Yes
Amazon WorkMail
ListOrganizations
View
Yes
Amazon WorkMail
ListResourceDelegates
View
Yes
Amazon WorkMail
ListResources
View
Yes
Amazon WorkMail
ListTagsForResource
View
Yes
Amazon WorkMail
ListUsers
View
Yes
Amazon WorkMail
PutAccessControlRule
Edit
Yes
Amazon WorkMail
PutMailboxPermissions
Edit
Yes
Amazon WorkMail
PutRetentionPolicy
Edit
Yes
Amazon WorkMail
RegisterToWorkMail
Register
Yes
Amazon WorkMail
ResetPassword
Edit
Yes
Amazon WorkMail
StartMailboxExportJob
Start
Yes
Amazon WorkMail
TagResource
Create
Yes
Amazon WorkMail
UntagResource
Delete
Yes
Amazon WorkMail
UpdateMailboxQuota
Edit
Yes
Amazon WorkMail
UpdateMobileDeviceAccessRule
Edit
Yes
Amazon WorkMail
UpdatePrimaryEmailAddress
Edit
Yes
Amazon WorkMail
UpdateResource
Edit
Yes
Amazon Forecast Service
CreateDataset
Create
Yes
Amazon Forecast Service
CreateDatasetGroup
Create
Yes
Amazon Forecast Service
CreateDatasetImportJob
Create
Yes
Amazon Forecast Service
CreateForecast
Create
Yes
Amazon Forecast Service
CreateForecastExportJob
Create
Yes
Amazon Forecast Service
CreatePredictor
Create
Yes
Amazon Forecast Service
CreatePredictorBacktestExportJob
Create
Yes
Amazon Forecast Service
DeleteDataset
Delete
Yes
Amazon Forecast Service
DeleteDatasetGroup
Delete
Yes
Amazon Forecast Service
DeleteDatasetImportJob
Delete
Yes
Amazon Forecast Service
DeleteForecast
Delete
Yes
Amazon Forecast Service
DeleteForecastExportJob
Delete
Yes
Amazon Forecast Service
DeletePredictor
Delete
Yes
Amazon Forecast Service
DeletePredictorBacktestExportJob
Delete
Yes
Amazon Forecast Service
DeleteResourceTree
Delete
Yes
Amazon Forecast Service
DescribeDataset
View
Yes
Amazon Forecast Service
DescribeDatasetGroup
View
Yes
Amazon Forecast Service
DescribeDatasetImportJob
View
Yes
Amazon Forecast Service
DescribeForecast
View
Yes
Amazon Forecast Service
DescribeForecastExportJob
View
Yes
Amazon Forecast Service
DescribePredictor
View
Yes
Amazon Forecast Service
DescribePredictorBacktestExportJob
View
Yes
Amazon Forecast Service
GetAccuracyMetrics
View
Yes
Amazon Forecast Service
ListDatasetGroups
View
Yes
Amazon Forecast Service
ListDatasetImportJobs
View
Yes
Amazon Forecast Service
ListDatasets
View
Yes
Amazon Forecast Service
ListForecastExportJobs
View
Yes
Amazon Forecast Service
ListForecasts
View
Yes
Amazon Forecast Service
ListPredictorBacktestExportJobs
View
Yes
Amazon Forecast Service
ListPredictors
View
Yes
Amazon Forecast Service
ListTagsForResource
View
Yes
Amazon Forecast Service
StopResource
Stop
Yes
Amazon Forecast Service
TagResource
Create
Yes
Amazon Forecast Service
UntagResource
Delete
Yes
Amazon Forecast Service
UpdateDatasetGroup
Edit
Yes
Amazon Security Token Service
AssumeRole
View
Yes
Amazon Security Token Service
AssumeRole
Create
Yes
Amazon Security Token Service
AssumeRoleWithSAML
View
Yes
Amazon Security Token Service
AssumeRoleWithSAML
Create
Yes
Amazon Security Token Service
AssumeRoleWithWebIdentity
View
Yes
Amazon Security Token Service
AssumeRoleWithWebIdentity
Create
Yes
Amazon Security Token Service
DecodeAuthorizationMessage
View
Yes
Amazon Security Token Service
DecodeAuthorizationMessage
Create
Yes
Amazon Security Token Service
GetAccessKeyInfo
View
Yes
Amazon Security Token Service
GetCallerIdentity
View
Yes
Amazon Security Token Service
GetFederationToken
View
Yes
Amazon Security Token Service
GetSessionToken
View
Yes
Amazon Inspector
AddAttributesToFindings
Create
Yes
Amazon Inspector
CreateAssessmentTarget
Create
Yes
Amazon Inspector
CreateAssessmentTemplate
Create
Yes
Amazon Inspector
CreateExclusionsPreview
Create
Yes
Amazon Inspector
CreateResourceGroup
Create
Yes
Amazon Inspector
DeleteAssessmentRun
Delete
Yes
Amazon Inspector
DeleteAssessmentTarget
Delete
Yes
Amazon Inspector
DeleteAssessmentTemplate
Delete
Yes
Amazon Inspector
DescribeAssessmentRuns
View
Yes
Amazon Inspector
DescribeAssessmentTargets
View
Yes
Amazon Inspector
DescribeAssessmentTemplates
View
Yes
Amazon Inspector
DescribeCrossAccountAccessRole
View
Yes
Amazon Inspector
DescribeExclusions
View
Yes
Amazon Inspector
DescribeFindings
View
Yes
Amazon Inspector
DescribeResourceGroups
View
Yes
Amazon Inspector
DescribeRulesPackages
View
Yes
Amazon Inspector
GetAssessmentReport
View
Yes
Amazon Inspector
GetExclusionsPreview
View
Yes
Amazon Inspector
GetTelemetryMetadata
View
Yes
Amazon Inspector
ListAssessmentRunAgents
View
Yes
Amazon Inspector
ListAssessmentRuns
View
Yes
Amazon Inspector
ListAssessmentTargets
View
Yes
Amazon Inspector
ListAssessmentTemplates
View
Yes
Amazon Inspector
ListEventSubscriptions
View
Yes
Amazon Inspector
ListExclusions
View
Yes
Amazon Inspector
ListFindings
View
Yes
Amazon Inspector
ListRulesPackages
View
Yes
Amazon Inspector
ListTagsForResource
View
Yes
Amazon Inspector
PreviewAgents
Create
Yes
Amazon Inspector
RegisterCrossAccountAccessRole
Register
Yes
Amazon Inspector
RemoveAttributesFromFindings
Delete
Yes
Amazon Inspector
SetTagsForResource
Create
Yes
Amazon Inspector
StartAssessmentRun
Start
Yes
Amazon Inspector
StopAssessmentRun
Stop
Yes
Amazon Inspector
SubscribeToEvent
Create
Yes
Amazon Inspector
UnsubscribeFromEvent
Create
Yes
Amazon Inspector
UpdateAssessmentTarget
Edit
Yes
Amazon Cognito Sync
BulkPublish
Create
Yes
Amazon Cognito Sync
DeleteDataset
Delete
Yes
Amazon Cognito Sync
DescribeDataset
View
Yes
Amazon Cognito Sync
UpdateRecords
Edit
Yes
Amazon Cognito Sync
DescribeIdentityPoolUsage
View
Yes
Amazon Cognito Sync
DescribeIdentityUsage
View
Yes
Amazon Cognito Sync
GetBulkPublishDetails
View
Yes
Amazon Cognito Sync
GetCognitoEvents
View
Yes
Amazon Cognito Sync
SetCognitoEvents
Create
Yes
Amazon Cognito Sync
GetIdentityPoolConfiguration
View
Yes
Amazon Cognito Sync
SetIdentityPoolConfiguration
Create
Yes
Amazon Cognito Sync
ListDatasets
View
Yes
Amazon Cognito Sync
ListIdentityPoolUsage
View
Yes
Amazon Cognito Sync
ListRecords
View
Yes
Amazon Cognito Sync
RegisterDevice
Register
Yes
Amazon Cognito Sync
SubscribeToDataset
Create
Yes
Amazon Cognito Sync
UnsubscribeFromDataset
Delete
Yes
Amazon AppStream
AssociateFleet
Create
Yes
Amazon AppStream
AssociateUserStack
Create
Yes
Amazon AppStream
DisassociateUserStack
Delete
Yes
Amazon AppStream
CopyImage
Copy
Yes
Amazon AppStream
CreateDirectoryConfig
Create
Yes
Amazon AppStream
CreateFleet
Create
Yes
Amazon AppStream
CreateImageBuilder
Create
Yes
Amazon AppStream
CreateImageBuilderStreamingURL
Create
Yes
Amazon AppStream
CreateStack
Create
Yes
Amazon AppStream
CreateStreamingURL
Create
Yes
Amazon AppStream
CreateUpdatedImage
Create
Yes
Amazon AppStream
CreateUsageReportSubscription
Create
Yes
Amazon AppStream
CreateUser
Create
Yes
Amazon AppStream
DeleteDirectoryConfig
Delete
Yes
Amazon AppStream
DeleteFleet
Delete
Yes
Amazon AppStream
DeleteImage
Delete
Yes
Amazon AppStream
DeleteImageBuilder
Delete
Yes
Amazon AppStream
DeleteImagePermissions
Delete
Yes
Amazon AppStream
DeleteStack
Delete
Yes
Amazon AppStream
DeleteUsageReportSubscription
Delete
Yes
Amazon AppStream
DeleteUser
Delete
Yes
Amazon AppStream
DescribeDirectoryConfigs
View
Yes
Amazon AppStream
DescribeFleets
View
Yes
Amazon AppStream
DescribeImageBuilders
View
Yes
Amazon AppStream
DescribeImagePermissions
View
Yes
Amazon AppStream
DescribeImages
View
Yes
Amazon AppStream
DescribeSessions
View
Yes
Amazon AppStream
DescribeStacks
View
Yes
Amazon AppStream
DescribeUsageReportSubscriptions
View
Yes
Amazon AppStream
DescribeUserStackAssociations
View
Yes
Amazon AppStream
DescribeUsers
View
Yes
Amazon AppStream
DisableUser
Edit
Yes
Amazon AppStream
DisassociateFleet
Delete
Yes
Amazon AppStream
EnableUser
Enable
Yes
Amazon AppStream
ExpireSession
Create
Yes
Amazon AppStream
ListAssociatedFleets
View
Yes
Amazon AppStream
ListAssociatedStacks
View
Yes
Amazon AppStream
ListTagsForResource
View
Yes
Amazon AppStream
StartFleet
Start
Yes
Amazon AppStream
StartImageBuilder
Start
Yes
Amazon AppStream
StopFleet
Stop
Yes
Amazon AppStream
StopImageBuilder
Stop
Yes
Amazon AppStream
TagResource
Create
Yes
Amazon AppStream
UntagResource
Delete
Yes
Amazon AppStream
UpdateDirectoryConfig
Edit
Yes
Amazon AppStream
UpdateFleet
Edit
Yes
Amazon AppStream
UpdateImagePermissions
Edit
Yes
Amazon AppStream
UpdateStack
Edit
Yes
Amazon Route53 Recovery Cluster
GetRoutingControlState
View
Yes
Amazon Route53 Recovery Cluster
UpdateRoutingControlState
Edit
Yes
Amazon Route53 Recovery Cluster
UpdateRoutingControlStates
Edit
Yes
Amazon Honeycode
CreateTableRows
Create
Yes
Amazon Honeycode
DeleteTableRows
Delete
Yes
Amazon Honeycode
UpdateTableRows
Edit
Yes
Amazon Honeycode
UpsertTableRows
Create
Yes
Amazon Honeycode
DescribeTableDataImportJob
View
Yes
Amazon Honeycode
GetScreenData
View
Yes
Amazon Honeycode
InvokeScreenAutomation
Create
Yes
Amazon Honeycode
ListTableColumns
View
Yes
Amazon Honeycode
ListTableRows
View
Yes
Amazon Honeycode
ListTables
View
Yes
Amazon Honeycode
QueryTableRows
Create
Yes
Amazon Honeycode
StartTableDataImportJob
Start
Yes
Amazon Outposts
CreateOrder
Create
Yes
Amazon Outposts
CreateOutpost
Create
Yes
Amazon Outposts
ListOutposts
View
Yes
Amazon Outposts
DeleteOutpost
Delete
Yes
Amazon Outposts
GetOutpost
View
Yes
Amazon Outposts
DeleteSite
Delete
Yes
Amazon Outposts
GetOutpostInstanceTypes
View
Yes
Amazon Outposts
ListSites
View
Yes
Amazon Outposts
ListTagsForResource
View
Yes
Amazon Outposts
TagResource
Create
Yes
Amazon Outposts
UntagResource
Delete
Yes
Amazon EMR Containers
CancelJobRun
Delete
Yes
Amazon EMR Containers
DescribeJobRun
View
Yes
Amazon EMR Containers
CreateManagedEndpoint
Create
Yes
Amazon EMR Containers
ListManagedEndpoints
View
Yes
Amazon EMR Containers
CreateVirtualCluster
Create
Yes
Amazon EMR Containers
ListVirtualClusters
View
Yes
Amazon EMR Containers
DeleteManagedEndpoint
Delete
Yes
Amazon EMR Containers
DescribeManagedEndpoint
View
Yes
Amazon EMR Containers
DeleteVirtualCluster
Delete
Yes
Amazon EMR Containers
DescribeVirtualCluster
View
Yes
Amazon EMR Containers
ListJobRuns
View
Yes
Amazon EMR Containers
StartJobRun
Start
Yes
Amazon EMR Containers
ListTagsForResource
View
Yes
Amazon EMR Containers
TagResource
Create
Yes
Amazon EMR Containers
UntagResource
Delete
Yes
Amazon IoT 1-Click Projects Service
AssociateDeviceWithPlacement
Create
Yes
Amazon IoT 1-Click Projects Service
DisassociateDeviceFromPlacement
Delete
Yes
Amazon IoT 1-Click Projects Service
CreatePlacement
Create
Yes
Amazon IoT 1-Click Projects Service
ListPlacements
View
Yes
Amazon IoT 1-Click Projects Service
CreateProject
Create
Yes
Amazon IoT 1-Click Projects Service
ListProjects
View
Yes
Amazon IoT 1-Click Projects Service
DeletePlacement
Delete
Yes
Amazon IoT 1-Click Projects Service
DescribePlacement
View
Yes
Amazon IoT 1-Click Projects Service
UpdatePlacement
Edit
Yes
Amazon IoT 1-Click Projects Service
DeleteProject
Delete
Yes
Amazon IoT 1-Click Projects Service
DescribeProject
View
Yes
Amazon IoT 1-Click Projects Service
UpdateProject
Edit
Yes
Amazon IoT 1-Click Projects Service
GetDevicesInPlacement
View
Yes
Amazon IoT 1-Click Projects Service
ListTagsForResource
View
Yes
Amazon IoT 1-Click Projects Service
TagResource
Create
Yes
Amazon IoT 1-Click Projects Service
UntagResource
Delete
Yes
Amazon IoT Fleet Hub
CreateApplication
Create
Yes
Amazon IoT Fleet Hub
ListApplications
View
Yes
Amazon IoT Fleet Hub
DeleteApplication
Delete
Yes
Amazon IoT Fleet Hub
DescribeApplication
View
Yes
Amazon IoT Fleet Hub
UpdateApplication
Edit
Yes
Amazon IoT Fleet Hub
ListTagsForResource
View
Yes
Amazon IoT Fleet Hub
TagResource
Create
Yes
Amazon IoT Fleet Hub
UntagResource
Delete
Yes
Amazon Managed Blockchain
CreateMember
Create
Yes
Amazon Managed Blockchain
ListMembers
View
Yes
Amazon Managed Blockchain
CreateNetwork
Create
Yes
Amazon Managed Blockchain
ListNetworks
View
Yes
Amazon Managed Blockchain
CreateNode
Create
Yes
Amazon Managed Blockchain
ListNodes
View
Yes
Amazon Managed Blockchain
CreateProposal
Create
Yes
Amazon Managed Blockchain
ListProposals
View
Yes
Amazon Managed Blockchain
DeleteMember
Delete
Yes
Amazon Managed Blockchain
GetMember
View
Yes
Amazon Managed Blockchain
UpdateMember
Edit
Yes
Amazon Managed Blockchain
DeleteNode
Delete
Yes
Amazon Managed Blockchain
GetNode
View
Yes
Amazon Managed Blockchain
UpdateNode
Edit
Yes
Amazon Managed Blockchain
GetNetwork
View
Yes
Amazon Managed Blockchain
GetProposal
View
Yes
Amazon Managed Blockchain
ListInvitations
View
Yes
Amazon Managed Blockchain
ListProposalVotes
View
Yes
Amazon Managed Blockchain
VoteOnProposal
Create
Yes
Amazon Managed Blockchain
ListTagsForResource
View
Yes
Amazon Managed Blockchain
TagResource
Create
Yes
Amazon Managed Blockchain
RejectInvitation
Delete
Yes
Amazon Managed Blockchain
UntagResource
Delete
Yes
Amazon License Manager
AcceptGrant
Approve
Yes
Amazon License Manager
CheckInLicense
Create
Yes
Amazon License Manager
CheckoutBorrowLicense
Create
Yes
Amazon License Manager
CheckoutLicense
Create
Yes
Amazon License Manager
CreateGrant
Create
Yes
Amazon License Manager
CreateGrantVersion
Create
Yes
Amazon License Manager
CreateLicense
Create
Yes
Amazon License Manager
CreateLicenseConfiguration
Create
Yes
Amazon License Manager
CreateLicenseManagerReportGenerator
Create
Yes
Amazon License Manager
CreateLicenseVersion
Create
Yes
Amazon License Manager
CreateToken
Create
Yes
Amazon License Manager
DeleteGrant
Delete
Yes
Amazon License Manager
DeleteLicense
Delete
Yes
Amazon License Manager
DeleteLicenseConfiguration
Delete
Yes
Amazon License Manager
DeleteLicenseManagerReportGenerator
Delete
Yes
Amazon License Manager
DeleteToken
Delete
Yes
Amazon License Manager
ExtendLicenseConsumption
Create
Yes
Amazon License Manager
GetAccessToken
View
Yes
Amazon License Manager
GetGrant
View
Yes
Amazon License Manager
GetLicense
View
Yes
Amazon License Manager
GetLicenseConfiguration
View
Yes
Amazon License Manager
GetLicenseManagerReportGenerator
View
Yes
Amazon License Manager
GetLicenseUsage
View
Yes
Amazon License Manager
GetServiceSettings
View
Yes
Amazon License Manager
ListAssociationsForLicenseConfiguration
View
Yes
Amazon License Manager
ListDistributedGrants
View
Yes
Amazon License Manager
ListFailuresForLicenseConfigurationOperations
View
Yes
Amazon License Manager
ListLicenseConfigurations
View
Yes
Amazon License Manager
ListLicenseManagerReportGenerators
View
Yes
Amazon License Manager
ListLicenseSpecificationsForResource
View
Yes
Amazon License Manager
ListLicenseVersions
View
Yes
Amazon License Manager
ListLicenses
View
Yes
Amazon License Manager
ListReceivedGrants
View
Yes
Amazon License Manager
ListReceivedLicenses
View
Yes
Amazon License Manager
ListResourceInventory
View
Yes
Amazon License Manager
ListTagsForResource
View
Yes
Amazon License Manager
ListTokens
View
Yes
Amazon License Manager
ListUsageForLicenseConfiguration
View
Yes
Amazon License Manager
RejectGrant
Reject
Yes
Amazon License Manager
TagResource
Create
Yes
Amazon License Manager
UntagResource
Delete
Yes
Amazon License Manager
UpdateLicenseConfiguration
Edit
Yes
Amazon License Manager
UpdateLicenseManagerReportGenerator
Edit
Yes
Amazon License Manager
UpdateLicenseSpecificationsForResource
Edit
Yes
Amazon License Manager
UpdateServiceSettings
Edit
Yes
Amazon Lookout for Vision
CreateDataset
Create
Yes
Amazon Lookout for Vision
CreateModel
Create
Yes
Amazon Lookout for Vision
ListModels
View
Yes
Amazon Lookout for Vision
CreateProject
Create
Yes
Amazon Lookout for Vision
ListProjects
View
Yes
Amazon Lookout for Vision
DeleteDataset
Delete
Yes
Amazon Lookout for Vision
DescribeDataset
View
Yes
Amazon Lookout for Vision
DeleteModel
Delete
Yes
Amazon Lookout for Vision
DescribeModel
View
Yes
Amazon Lookout for Vision
DeleteProject
Delete
Yes
Amazon Lookout for Vision
DescribeProject
View
Yes
Amazon Lookout for Vision
DetectAnomalies
Create
Yes
Amazon Lookout for Vision
ListDatasetEntries
View
Yes
Amazon Lookout for Vision
UpdateDatasetEntries
Edit
Yes
Amazon Lookout for Vision
ListTagsForResource
View
Yes
Amazon Lookout for Vision
TagResource
Create
Yes
Amazon Lookout for Vision
StartModel
Start
Yes
Amazon Lookout for Vision
StopModel
Stop
Yes
Amazon Lookout for Vision
UntagResource
Delete
Yes
Amazon Network Manager
AssociateCustomerGateway
Create
Yes
Amazon Network Manager
GetCustomerGatewayAssociations
View
Yes
Amazon Network Manager
AssociateLink
Create
Yes
Amazon Network Manager
GetLinkAssociations
View
Yes
Amazon Network Manager
AssociateTransitGatewayConnectPeer
Create
Yes
Amazon Network Manager
GetTransitGatewayConnectPeerAssociations
View
Yes
Amazon Network Manager
CreateConnection
Create
Yes
Amazon Network Manager
GetConnections
View
Yes
Amazon Network Manager
CreateDevice
Create
Yes
Amazon Network Manager
GetDevices
View
Yes
Amazon Network Manager
CreateGlobalNetwork
Create
Yes
Amazon Network Manager
DescribeGlobalNetworks
View
Yes
Amazon Network Manager
CreateLink
Create
Yes
Amazon Network Manager
GetLinks
View
Yes
Amazon Network Manager
CreateSite
Create
Yes
Amazon Network Manager
GetSites
View
Yes
Amazon Network Manager
DeleteConnection
Delete
Yes
Amazon Network Manager
UpdateConnection
Edit
Yes
Amazon Network Manager
DeleteDevice
Delete
Yes
Amazon Network Manager
UpdateDevice
Edit
Yes
Amazon Network Manager
DeleteGlobalNetwork
Delete
Yes
Amazon Network Manager
UpdateGlobalNetwork
Edit
Yes
Amazon Network Manager
DeleteLink
Delete
Yes
Amazon Network Manager
UpdateLink
Edit
Yes
Amazon Network Manager
DeleteSite
Delete
Yes
Amazon Network Manager
UpdateSite
Edit
Yes
Amazon Network Manager
DeregisterTransitGateway
Delete
Yes
Amazon Network Manager
DisassociateCustomerGateway
Delete
Yes
Amazon Network Manager
DisassociateLink
Delete
Yes
Amazon Network Manager
DisassociateTransitGatewayConnectPeer
Delete
Yes
Amazon Network Manager
GetTransitGatewayRegistrations
View
Yes
Amazon Network Manager
RegisterTransitGateway
Register
Yes
Amazon Network Manager
ListTagsForResource
View
Yes
Amazon Network Manager
TagResource
Create
Yes
Amazon Network Manager
UntagResource
Delete
Yes
Amazon Audit Manager
AssociateAssessmentReportEvidenceFolder
Create
Yes
Amazon Audit Manager
AssociateAssessmentReportEvidence
Create
Yes
Amazon Audit Manager
CreateDelegationByAssessment
Create
Yes
Amazon Audit Manager
DeleteDelegationByAssessment
Delete
Yes
Amazon Audit Manager
DisassociateAssessmentReportEvidence
Delete
Yes
Amazon Audit Manager
ImportEvidenceToAssessmentControl
Create
Yes
Amazon Audit Manager
CreateAssessment
Create
Yes
Amazon Audit Manager
ListAssessments
View
Yes
Amazon Audit Manager
CreateAssessmentFramework
Create
Yes
Amazon Audit Manager
CreateAssessmentReport
Create
Yes
Amazon Audit Manager
CreateControl
Create
Yes
Amazon Audit Manager
DeleteAssessment
Delete
Yes
Amazon Audit Manager
GetAssessment
View
Yes
Amazon Audit Manager
UpdateAssessment
Edit
Yes
Amazon Audit Manager
DeleteAssessmentFramework
Delete
Yes
Amazon Audit Manager
GetAssessmentFramework
View
Yes
Amazon Audit Manager
UpdateAssessmentFramework
Edit
Yes
Amazon Audit Manager
DeleteAssessmentReport
Delete
Yes
Amazon Audit Manager
DeleteControl
Delete
Yes
Amazon Audit Manager
GetControl
View
Yes
Amazon Audit Manager
UpdateControl
Edit
Yes
Amazon Audit Manager
DeregisterAccount
Deregister
Yes
Amazon Audit Manager
DeregisterOrganizationAdminAccount
Deregister
Yes
Amazon Audit Manager
DisassociateAssessmentReportEvidenceFolder
Delete
Yes
Amazon Audit Manager
GetAccountStatus
View
Yes
Amazon Audit Manager
GetAssessmentReportUrl
View
Yes
Amazon Audit Manager
GetChangeLogs
View
Yes
Amazon Audit Manager
GetDelegations
View
Yes
Amazon Audit Manager
GetEvidence
View
Yes
Amazon Audit Manager
GetEvidenceByEvidenceFolder
View
Yes
Amazon Audit Manager
GetEvidenceFolder
View
Yes
Amazon Audit Manager
GetEvidenceFoldersByAssessment
View
Yes
Amazon Audit Manager
GetEvidenceFoldersByAssessmentControl
View
Yes
Amazon Audit Manager
GetOrganizationAdminAccount
View
Yes
Amazon Audit Manager
GetServicesInScope
View
Yes
Amazon Audit Manager
GetSettings
View
Yes
Amazon Audit Manager
ListAssessmentFrameworks
View
Yes
Amazon Audit Manager
ListAssessmentReports
View
Yes
Amazon Audit Manager
ListControls
View
Yes
Amazon Audit Manager
ListKeywordsForDataSource
View
Yes
Amazon Audit Manager
ListNotifications
View
Yes
Amazon Audit Manager
ListTagsForResource
View
Yes
Amazon Audit Manager
TagResource
Create
Yes
Amazon Audit Manager
RegisterAccount
Register
Yes
Amazon Audit Manager
RegisterOrganizationAdminAccount
Register
Yes
Amazon Audit Manager
UntagResource
Delete
Yes
Amazon Audit Manager
UpdateAssessmentControl
Edit
Yes
Amazon Audit Manager
UpdateAssessmentControlSetStatus
Edit
Yes
Amazon Audit Manager
UpdateAssessmentStatus
Edit
Yes
Amazon Audit Manager
UpdateSettings
Edit
Yes
Amazon Audit Manager
ValidateAssessmentReportIntegrity
Create
Yes
Amazon Amplify
CreateApp
Create
Yes
Amazon Amplify
ListApps
View
Yes
Amazon Amplify
CreateBackendEnvironment
Create
Yes
Amazon Amplify
ListBackendEnvironments
View
Yes
Amazon Amplify
CreateBranch
Create
Yes
Amazon Amplify
ListBranches
View
Yes
Amazon Amplify
CreateDeployment
Create
Yes
Amazon Amplify
CreateDomainAssociation
Create
Yes
Amazon Amplify
ListDomainAssociations
View
Yes
Amazon Amplify
CreateWebhook
Create
Yes
Amazon Amplify
ListWebhooks
View
Yes
Amazon Amplify
DeleteApp
Delete
Yes
Amazon Amplify
GetApp
View
Yes
Amazon Amplify
UpdateApp
Edit
Yes
Amazon Amplify
DeleteBackendEnvironment
Delete
Yes
Amazon Amplify
GetBackendEnvironment
View
Yes
Amazon Amplify
DeleteBranch
Delete
Yes
Amazon Amplify
GetBranch
View
Yes
Amazon Amplify
UpdateBranch
Edit
Yes
Amazon Amplify
DeleteDomainAssociation
Delete
Yes
Amazon Amplify
GetDomainAssociation
View
Yes
Amazon Amplify
UpdateDomainAssociation
Edit
Yes
Amazon Amplify
DeleteJob
Delete
Yes
Amazon Amplify
GetJob
View
Yes
Amazon Amplify
DeleteWebhook
Delete
Yes
Amazon Amplify
GetWebhook
View
Yes
Amazon Amplify
UpdateWebhook
Edit
Yes
Amazon Amplify
GenerateAccessLogs
Create
Yes
Amazon Amplify
GetArtifactUrl
View
Yes
Amazon Amplify
ListArtifacts
View
Yes
Amazon Amplify
ListJobs
View
Yes
Amazon Amplify
StartJob
Start
Yes
Amazon Amplify
ListTagsForResource
View
Yes
Amazon Amplify
TagResource
Create
Yes
Amazon Amplify
StartDeployment
Start
Yes
Amazon Amplify
StopJob
Delete
Yes
Amazon Amplify
UntagResource
Delete
Yes
Amazon Import/Export
CancelJob
Delete
Yes
Amazon Import/Export
CreateJob
Create
Yes
Amazon Import/Export
GetShippingLabel
View
Yes
Amazon Import/Export
GetStatus
View
Yes
Amazon Import/Export
ListJobs
View
Yes
Amazon Import/Export
UpdateJob
Edit
Yes
Amazon CloudHSM V2
CopyBackupToRegion
Copy
Yes
Amazon CloudHSM V2
CreateCluster
Create
Yes
Amazon CloudHSM V2
CreateHsm
Create
Yes
Amazon CloudHSM V2
DeleteBackup
Delete
Yes
Amazon CloudHSM V2
DeleteCluster
Delete
Yes
Amazon CloudHSM V2
DeleteHsm
Delete
Yes
Amazon CloudHSM V2
DescribeBackups
View
Yes
Amazon CloudHSM V2
DescribeClusters
View
Yes
Amazon CloudHSM V2
InitializeCluster
Create
Yes
Amazon CloudHSM V2
ListTags
View
Yes
Amazon CloudHSM V2
ModifyBackupAttributes
Edit
Yes
Amazon CloudHSM V2
ModifyCluster
Edit
Yes
Amazon CloudHSM V2
RestoreBackup
Create
Yes
Amazon CloudHSM V2
TagResource
Create
Yes
Amazon CloudHSM V2
UntagResource
Delete
Yes
Amazon Textract
AnalyzeDocument
Create
Yes
Amazon Textract
AnalyzeExpense
Create
Yes
Amazon Textract
DetectDocumentText
Create
Yes
Amazon Textract
GetDocumentAnalysis
View
Yes
Amazon Textract
GetDocumentTextDetection
View
Yes
Amazon Textract
StartDocumentAnalysis
Start
Yes
Amazon Textract
StartDocumentTextDetection
Start
Yes
Amazon QLDB Session
SendCommand
Send
Yes
Amazon Systems Manager Incident Manager Contacts
AcceptPage
Approve
Yes
Amazon Systems Manager Incident Manager Contacts
ActivateContactChannel
Activate
Yes
Amazon Systems Manager Incident Manager Contacts
CreateContact
Create
Yes
Amazon Systems Manager Incident Manager Contacts
CreateContactChannel
Create
Yes
Amazon Systems Manager Incident Manager Contacts
DeactivateContactChannel
Deactivate
Yes
Amazon Systems Manager Incident Manager Contacts
DeleteContact
Delete
Yes
Amazon Systems Manager Incident Manager Contacts
DeleteContactChannel
Delete
Yes
Amazon Systems Manager Incident Manager Contacts
DescribeEngagement
View
Yes
Amazon Systems Manager Incident Manager Contacts
DescribePage
View
Yes
Amazon Systems Manager Incident Manager Contacts
GetContact
View
Yes
Amazon Systems Manager Incident Manager Contacts
GetContactChannel
View
Yes
Amazon Systems Manager Incident Manager Contacts
GetContactPolicy
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListContactChannels
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListContacts
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListEngagements
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListPageReceipts
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListPagesByContact
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListPagesByEngagement
View
Yes
Amazon Systems Manager Incident Manager Contacts
ListTagsForResource
View
Yes
Amazon Systems Manager Incident Manager Contacts
PutContactPolicy
Edit
Yes
Amazon Systems Manager Incident Manager Contacts
SendActivationCode
Send
Yes
Amazon Systems Manager Incident Manager Contacts
StartEngagement
Start
Yes
Amazon Systems Manager Incident Manager Contacts
StopEngagement
Stop
Yes
Amazon Systems Manager Incident Manager Contacts
TagResource
Create
Yes
Amazon Systems Manager Incident Manager Contacts
UntagResource
Delete
Yes
Amazon Systems Manager Incident Manager Contacts
UpdateContact
Edit
Yes
Amazon Systems Manager Incident Manager Contacts
UpdateContactChannel
Edit
Yes
Amazon CloudSearch Domain
Search
Search
Yes
Amazon CloudSearch Domain
Suggest
View
Yes
Amazon CloudSearch Domain
UploadDocuments
Upload
Yes
Amazon App Mesh
CreateGatewayRoute
Create
Yes
Amazon App Mesh
ListGatewayRoutes
View
Yes
Amazon App Mesh
CreateMesh
Create
Yes
Amazon App Mesh
ListMeshes
View
Yes
Amazon App Mesh
CreateRoute
Create
Yes
Amazon App Mesh
ListRoutes
View
Yes
Amazon App Mesh
CreateVirtualGateway
Create
Yes
Amazon App Mesh
ListVirtualGateways
View
Yes
Amazon App Mesh
CreateVirtualNode
Create
Yes
Amazon App Mesh
ListVirtualNodes
View
Yes
Amazon App Mesh
CreateVirtualRouter
Create
Yes
Amazon App Mesh
ListVirtualRouters
View
Yes
Amazon App Mesh
CreateVirtualService
Create
Yes
Amazon App Mesh
ListVirtualServices
View
Yes
Amazon App Mesh
DeleteGatewayRoute
Delete
Yes
Amazon App Mesh
DescribeGatewayRoute
View
Yes
Amazon App Mesh
UpdateGatewayRoute
Edit
Yes
Amazon App Mesh
DeleteMesh
Delete
Yes
Amazon App Mesh
DescribeMesh
View
Yes
Amazon App Mesh
UpdateMesh
Edit
Yes
Amazon App Mesh
DeleteRoute
Delete
Yes
Amazon App Mesh
DescribeRoute
View
Yes
Amazon App Mesh
UpdateRoute
Edit
Yes
Amazon App Mesh
DeleteVirtualGateway
Delete
Yes
Amazon App Mesh
DescribeVirtualGateway
View
Yes
Amazon App Mesh
UpdateVirtualGateway
Edit
Yes
Amazon App Mesh
DeleteVirtualNode
Delete
Yes
Amazon App Mesh
DescribeVirtualNode
View
Yes
Amazon App Mesh
UpdateVirtualNode
Edit
Yes
Amazon App Mesh
DeleteVirtualRouter
Delete
Yes
Amazon App Mesh
DescribeVirtualRouter
View
Yes
Amazon App Mesh
UpdateVirtualRouter
Edit
Yes
Amazon App Mesh
DeleteVirtualService
Delete
Yes
Amazon App Mesh
DescribeVirtualService
View
Yes
Amazon App Mesh
UpdateVirtualService
Edit
Yes
Amazon App Mesh
ListTagsForResource
View
Yes
Amazon App Mesh
TagResource
Create
Yes
Amazon App Mesh
UntagResource
Delete
Yes
Amazon IoT Core Device Advisor
CreateSuiteDefinition
Create
Yes
Amazon IoT Core Device Advisor
ListSuiteDefinitions
View
Yes
Amazon IoT Core Device Advisor
DeleteSuiteDefinition
Delete
Yes
Amazon IoT Core Device Advisor
GetSuiteDefinition
View
Yes
Amazon IoT Core Device Advisor
UpdateSuiteDefinition
Edit
Yes
Amazon IoT Core Device Advisor
GetSuiteRun
View
Yes
Amazon IoT Core Device Advisor
GetSuiteRunReport
View
Yes
Amazon IoT Core Device Advisor
ListSuiteRuns
View
Yes
Amazon IoT Core Device Advisor
ListTagsForResource
View
Yes
Amazon IoT Core Device Advisor
TagResource
Create
Yes
Amazon IoT Core Device Advisor
StartSuiteRun
Start
Yes
Amazon IoT Core Device Advisor
StopSuiteRun
Stop
Yes
Amazon IoT Core Device Advisor
UntagResource
Delete
Yes
Amazon WorkMail Message Flow
GetRawMessageContent
View
Yes
Amazon WorkMail Message Flow
PutRawMessageContent
Edit
Yes
Amazon Synthetics
CreateCanary
Create
Yes
Amazon Synthetics
DeleteCanary
Delete
Yes
Amazon Synthetics
GetCanary
View
Yes
Amazon Synthetics
UpdateCanary
Edit
Yes
Amazon Synthetics
DescribeCanaries
View
Yes
Amazon Synthetics
DescribeCanariesLastRun
View
Yes
Amazon Synthetics
DescribeRuntimeVersions
View
Yes
Amazon Synthetics
GetCanaryRuns
View
Yes
Amazon Synthetics
ListTagsForResource
View
Yes
Amazon Synthetics
TagResource
Create
Yes
Amazon Synthetics
StartCanary
Start
Yes
Amazon Synthetics
StopCanary
Stop
Yes
Amazon Synthetics
UntagResource
Delete
Yes
Amazon Kinesis Video Streams
CreateSignalingChannel
Create
Yes
Amazon Kinesis Video Streams
CreateStream
Create
Yes
Amazon Kinesis Video Streams
DeleteSignalingChannel
Delete
Yes
Amazon Kinesis Video Streams
DeleteStream
Delete
Yes
Amazon Kinesis Video Streams
DescribeSignalingChannel
View
Yes
Amazon Kinesis Video Streams
DescribeStream
View
Yes
Amazon Kinesis Video Streams
GetDataEndpoint
View
Yes
Amazon Kinesis Video Streams
GetSignalingChannelEndpoint
View
Yes
Amazon Kinesis Video Streams
ListSignalingChannels
View
Yes
Amazon Kinesis Video Streams
ListStreams
View
Yes
Amazon Kinesis Video Streams
ListTagsForResource
View
Yes
Amazon Kinesis Video Streams
ListTagsForStream
View
Yes
Amazon Kinesis Video Streams
TagResource
Create
Yes
Amazon Kinesis Video Streams
TagStream
Create
Yes
Amazon Kinesis Video Streams
UntagResource
Delete
Yes
Amazon Kinesis Video Streams
UntagStream
Delete
Yes
Amazon Kinesis Video Streams
UpdateDataRetention
Edit
Yes
Amazon Kinesis Video Streams
UpdateSignalingChannel
Edit
Yes
Amazon Kinesis Video Streams
UpdateStream
Edit
Yes
Amazon Elastic Transcoder
CancelJob
Delete
Yes
Amazon Elastic Transcoder
ReadJob
View
Yes
Amazon Elastic Transcoder
CreateJob
Create
Yes
Amazon Elastic Transcoder
CreatePipeline
Create
Yes
Amazon Elastic Transcoder
ListPipelines
View
Yes
Amazon Elastic Transcoder
CreatePreset
Create
Yes
Amazon Elastic Transcoder
ListPresets
View
Yes
Amazon Elastic Transcoder
DeletePipeline
Delete
Yes
Amazon Elastic Transcoder
ReadPipeline
View
Yes
Amazon Elastic Transcoder
UpdatePipeline
Edit
Yes
Amazon Elastic Transcoder
DeletePreset
Delete
Yes
Amazon Elastic Transcoder
ReadPreset
View
Yes
Amazon Elastic Transcoder
ListJobsByPipeline
View
Yes
Amazon Elastic Transcoder
ListJobsByStatus
View
Yes
Amazon Elastic Transcoder
TestRole
Create
Yes
Amazon Elastic Transcoder
UpdatePipelineNotifications
Edit
Yes
Amazon Elastic Transcoder
UpdatePipelineStatus
Edit
Yes
Amazon Resource Groups
CreateGroup
Create
Yes
Amazon Resource Groups
DeleteGroup
Delete
Yes
Amazon Resource Groups
GetGroup
View
Yes
Amazon Resource Groups
GetGroupConfiguration
View
Yes
Amazon Resource Groups
GetGroupQuery
View
Yes
Amazon Resource Groups
GetTags
View
Yes
Amazon Resource Groups
Tag
Create
Yes
Amazon Resource Groups
Untag
Delete
Yes
Amazon Resource Groups
GroupResources
Create
Yes
Amazon Resource Groups
ListGroupResources
View
Yes
Amazon Resource Groups
ListGroups
View
Yes
Amazon Resource Groups
PutGroupConfiguration
Edit
Yes
Amazon Resource Groups
SearchResources
Search
Yes
Amazon Resource Groups
UngroupResources
Create
Yes
Amazon Resource Groups
UpdateGroup
Edit
Yes
Amazon Resource Groups
UpdateGroupQuery
Edit
Yes
Amazon WorkLink
AssociateDomain
Create
Yes
Amazon WorkLink
AssociateWebsiteAuthorizationProvider
Create
Yes
Amazon WorkLink
AssociateWebsiteCertificateAuthority
Create
Yes
Amazon WorkLink
CreateFleet
Create
Yes
Amazon WorkLink
DeleteFleet
Delete
Yes
Amazon WorkLink
DescribeAuditStreamConfiguration
View
Yes
Amazon WorkLink
DescribeCompanyNetworkConfiguration
View
Yes
Amazon WorkLink
DescribeDevice
View
Yes
Amazon WorkLink
DescribeDevicePolicyConfiguration
View
Yes
Amazon WorkLink
DescribeDomain
View
Yes
Amazon WorkLink
DescribeFleetMetadata
View
Yes
Amazon WorkLink
DescribeIdentityProviderConfiguration
View
Yes
Amazon WorkLink
DescribeWebsiteCertificateAuthority
View
Yes
Amazon WorkLink
DisassociateDomain
Delete
Yes
Amazon WorkLink
DisassociateWebsiteAuthorizationProvider
Delete
Yes
Amazon WorkLink
DisassociateWebsiteCertificateAuthority
Delete
Yes
Amazon WorkLink
ListDevices
View
Yes
Amazon WorkLink
ListDomains
View
Yes
Amazon WorkLink
ListFleets
View
Yes
Amazon WorkLink
ListTagsForResource
View
Yes
Amazon WorkLink
TagResource
Create
Yes
Amazon WorkLink
ListWebsiteAuthorizationProviders
View
Yes
Amazon WorkLink
ListWebsiteCertificateAuthorities
View
Yes
Amazon WorkLink
RestoreDomainAccess
Create
Yes
Amazon WorkLink
RevokeDomainAccess
Delete
Yes
Amazon WorkLink
SignOutUser
Create
Yes
Amazon WorkLink
UntagResource
Delete
Yes
Amazon WorkLink
UpdateAuditStreamConfiguration
Edit
Yes
Amazon WorkLink
UpdateCompanyNetworkConfiguration
Edit
Yes
Amazon WorkLink
UpdateDevicePolicyConfiguration
Edit
Yes
Amazon WorkLink
UpdateDomainMetadata
Edit
Yes
Amazon WorkLink
UpdateFleetMetadata
Edit
Yes
Amazon WorkLink
UpdateIdentityProviderConfiguration
Edit
Yes
Amazon Glue
CreatePartition
Create
Yes
Amazon Glue
DeleteConnection
Delete
Yes
Amazon Glue
DeletePartition
Delete
Yes
Amazon Glue
DeleteTable
Delete
Yes
Amazon Glue
DeleteTableVersion
Delete
Yes
Amazon Glue
GetBlueprints
View
Yes
Amazon Glue
GetCrawlers
View
Yes
Amazon Glue
GetDevEndpoints
View
Yes
Amazon Glue
GetJobs
View
Yes
Amazon Glue
GetPartition
View
Yes
Amazon Glue
GetTriggers
View
Yes
Amazon Glue
GetWorkflows
View
Yes
Amazon Glue
StopJobRun
Stop
Yes
Amazon Glue
UpdatePartition
Edit
Yes
Amazon Glue
CancelMLTaskRun
Delete
Yes
Amazon Glue
CheckSchemaVersionValidity
Create
Yes
Amazon Glue
CreateBlueprint
Create
Yes
Amazon Glue
CreateClassifier
Create
Yes
Amazon Glue
CreateConnection
Create
Yes
Amazon Glue
CreateCrawler
Create
Yes
Amazon Glue
CreateDatabase
Create
Yes
Amazon Glue
CreateDevEndpoint
Create
Yes
Amazon Glue
CreateJob
Create
Yes
Amazon Glue
CreateMLTransform
Create
Yes
Amazon Glue
CreatePartitionIndex
Create
Yes
Amazon Glue
CreateRegistry
Create
Yes
Amazon Glue
CreateSchema
Create
Yes
Amazon Glue
CreateScript
Create
Yes
Amazon Glue
CreateSecurityConfiguration
Create
Yes
Amazon Glue
CreateTable
Create
Yes
Amazon Glue
CreateTrigger
Create
Yes
Amazon Glue
CreateUserDefinedFunction
Create
Yes
Amazon Glue
CreateWorkflow
Create
Yes
Amazon Glue
DeleteBlueprint
Delete
Yes
Amazon Glue
DeleteClassifier
Delete
Yes
Amazon Glue
DeleteColumnStatisticsForPartition
Delete
Yes
Amazon Glue
DeleteColumnStatisticsForTable
Delete
Yes
Amazon Glue
DeleteCrawler
Delete
Yes
Amazon Glue
DeleteDatabase
Delete
Yes
Amazon Glue
DeleteDevEndpoint
Delete
Yes
Amazon Glue
DeleteJob
Delete
Yes
Amazon Glue
DeleteMLTransform
Delete
Yes
Amazon Glue
DeletePartitionIndex
Delete
Yes
Amazon Glue
DeleteRegistry
Delete
Yes
Amazon Glue
DeleteResourcePolicy
Delete
Yes
Amazon Glue
DeleteSchema
Delete
Yes
Amazon Glue
DeleteSchemaVersions
Delete
Yes
Amazon Glue
DeleteSecurityConfiguration
Delete
Yes
Amazon Glue
DeleteTrigger
Delete
Yes
Amazon Glue
DeleteUserDefinedFunction
Delete
Yes
Amazon Glue
DeleteWorkflow
Delete
Yes
Amazon Glue
GetBlueprint
View
Yes
Amazon Glue
GetBlueprintRun
View
Yes
Amazon Glue
GetBlueprintRuns
View
Yes
Amazon Glue
GetCatalogImportStatus
View
Yes
Amazon Glue
GetClassifier
View
Yes
Amazon Glue
GetClassifiers
View
Yes
Amazon Glue
GetColumnStatisticsForPartition
View
Yes
Amazon Glue
GetColumnStatisticsForTable
View
Yes
Amazon Glue
GetConnection
View
Yes
Amazon Glue
GetConnections
View
Yes
Amazon Glue
GetCrawler
View
Yes
Amazon Glue
GetCrawlerMetrics
View
Yes
Amazon Glue
GetDataCatalogEncryptionSettings
View
Yes
Amazon Glue
GetDatabase
View
Yes
Amazon Glue
GetDatabases
View
Yes
Amazon Glue
GetDataflowGraph
View
Yes
Amazon Glue
GetDevEndpoint
View
Yes
Amazon Glue
GetJob
View
Yes
Amazon Glue
GetJobBookmark
View
Yes
Amazon Glue
GetJobRun
View
Yes
Amazon Glue
GetJobRuns
View
Yes
Amazon Glue
GetMLTaskRun
View
Yes
Amazon Glue
GetMLTaskRuns
View
Yes
Amazon Glue
GetMLTransform
View
Yes
Amazon Glue
GetMLTransforms
View
Yes
Amazon Glue
GetMapping
View
Yes
Amazon Glue
GetPartitionIndexes
View
Yes
Amazon Glue
GetPartitions
View
Yes
Amazon Glue
GetPlan
View
Yes
Amazon Glue
GetRegistry
View
Yes
Amazon Glue
GetResourcePolicies
View
Yes
Amazon Glue
GetResourcePolicy
View
Yes
Amazon Glue
GetSchema
View
Yes
Amazon Glue
GetSchemaByDefinition
View
Yes
Amazon Glue
GetSchemaVersion
View
Yes
Amazon Glue
GetSchemaVersionsDiff
View
Yes
Amazon Glue
GetSecurityConfiguration
View
Yes
Amazon Glue
GetSecurityConfigurations
View
Yes
Amazon Glue
GetTable
View
Yes
Amazon Glue
GetTableVersion
View
Yes
Amazon Glue
GetTableVersions
View
Yes
Amazon Glue
GetTables
View
Yes
Amazon Glue
GetTags
View
Yes
Amazon Glue
GetTrigger
View
Yes
Amazon Glue
GetUserDefinedFunction
View
Yes
Amazon Glue
GetUserDefinedFunctions
View
Yes
Amazon Glue
GetWorkflow
View
Yes
Amazon Glue
GetWorkflowRun
View
Yes
Amazon Glue
GetWorkflowRunProperties
View
Yes
Amazon Glue
GetWorkflowRuns
View
Yes
Amazon Glue
ImportCatalogToGlue
Create
Yes
Amazon Glue
ListBlueprints
View
Yes
Amazon Glue
ListCrawlers
View
Yes
Amazon Glue
ListDevEndpoints
View
Yes
Amazon Glue
ListJobs
View
Yes
Amazon Glue
ListMLTransforms
View
Yes
Amazon Glue
ListRegistries
View
Yes
Amazon Glue
ListSchemaVersions
View
Yes
Amazon Glue
ListSchemas
View
Yes
Amazon Glue
ListTriggers
View
Yes
Amazon Glue
ListWorkflows
View
Yes
Amazon Glue
PutDataCatalogEncryptionSettings
Edit
Yes
Amazon Glue
PutResourcePolicy
Edit
Yes
Amazon Glue
PutSchemaVersionMetadata
Edit
Yes
Amazon Glue
PutWorkflowRunProperties
Edit
Yes
Amazon Glue
QuerySchemaVersionMetadata
Create
Yes
Amazon Glue
RegisterSchemaVersion
Register
Yes
Amazon Glue
RemoveSchemaVersionMetadata
Delete
Yes
Amazon Glue
ResetJobBookmark
Edit
Yes
Amazon Glue
ResumeWorkflowRun
Start
Yes
Amazon Glue
SearchTables
Search
Yes
Amazon Glue
StartBlueprintRun
Start
Yes
Amazon Glue
StartCrawler
Start
Yes
Amazon Glue
StartCrawlerSchedule
Start
Yes
Amazon Glue
StartExportLabelsTaskRun
Start
Yes
Amazon Glue
StartImportLabelsTaskRun
Start
Yes
Amazon Glue
StartJobRun
Start
Yes
Amazon Glue
StartMLEvaluationTaskRun
Start
Yes
Amazon Glue
StartMLLabelingSetGenerationTaskRun
Start
Yes
Amazon Glue
StartTrigger
Start
Yes
Amazon Glue
StartWorkflowRun
Start
Yes
Amazon Glue
StopCrawler
Stop
Yes
Amazon Glue
StopCrawlerSchedule
Stop
Yes
Amazon Glue
StopTrigger
Stop
Yes
Amazon Glue
StopWorkflowRun
Stop
Yes
Amazon Glue
TagResource
Create
Yes
Amazon Glue
UntagResource
Delete
Yes
Amazon Glue
UpdateBlueprint
Edit
Yes
Amazon Glue
UpdateClassifier
Edit
Yes
Amazon Glue
UpdateColumnStatisticsForPartition
Edit
Yes
Amazon Glue
UpdateColumnStatisticsForTable
Edit
Yes
Amazon Glue
UpdateConnection
Edit
Yes
Amazon Glue
UpdateCrawler
Edit
Yes
Amazon Glue
UpdateCrawlerSchedule
Edit
Yes
Amazon Glue
UpdateDatabase
Edit
Yes
Amazon Glue
UpdateDevEndpoint
Edit
Yes
Amazon Glue
UpdateJob
Edit
Yes
Amazon Glue
UpdateMLTransform
Edit
Yes
Amazon Glue
UpdateRegistry
Edit
Yes
Amazon Glue
UpdateSchema
Edit
Yes
Amazon Glue
UpdateTable
Edit
Yes
Amazon Glue
UpdateTrigger
Edit
Yes
Amazon Glue
UpdateUserDefinedFunction
Edit
Yes
Amazon Glue
UpdateWorkflow
Edit
Yes
Amazon SageMaker Service
AddAssociation
Create
Yes
Amazon SageMaker Service
AddTags
Create
Yes
Amazon SageMaker Service
AssociateTrialComponent
Create
Yes
Amazon SageMaker Service
CreateAction
Create
Yes
Amazon SageMaker Service
CreateAlgorithm
Create
Yes
Amazon SageMaker Service
CreateApp
Create
Yes
Amazon SageMaker Service
CreateAppImageConfig
Create
Yes
Amazon SageMaker Service
CreateArtifact
Create
Yes
Amazon SageMaker Service
CreateAutoMLJob
Create
Yes
Amazon SageMaker Service
CreateCodeRepository
Create
Yes
Amazon SageMaker Service
CreateCompilationJob
Create
Yes
Amazon SageMaker Service
CreateContext
Create
Yes
Amazon SageMaker Service
CreateDataQualityJobDefinition
Create
Yes
Amazon SageMaker Service
CreateDeviceFleet
Create
Yes
Amazon SageMaker Service
CreateDomain
Create
Yes
Amazon SageMaker Service
CreateEdgePackagingJob
Create
Yes
Amazon SageMaker Service
CreateEndpoint
Create
Yes
Amazon SageMaker Service
CreateEndpointConfig
Create
Yes
Amazon SageMaker Service
CreateExperiment
Create
Yes
Amazon SageMaker Service
CreateFeatureGroup
Create
Yes
Amazon SageMaker Service
CreateFlowDefinition
Create
Yes
Amazon SageMaker Service
CreateHumanTaskUi
Create
Yes
Amazon SageMaker Service
CreateHyperParameterTuningJob
Create
Yes
Amazon SageMaker Service
CreateImage
Create
Yes
Amazon SageMaker Service
CreateImageVersion
Create
Yes
Amazon SageMaker Service
CreateLabelingJob
Create
Yes
Amazon SageMaker Service
CreateModel
Create
Yes
Amazon SageMaker Service
CreateModelBiasJobDefinition
Create
Yes
Amazon SageMaker Service
CreateModelExplainabilityJobDefinition
Create
Yes
Amazon SageMaker Service
CreateModelPackage
Create
Yes
Amazon SageMaker Service
CreateModelPackageGroup
Create
Yes
Amazon SageMaker Service
CreateModelQualityJobDefinition
Create
Yes
Amazon SageMaker Service
CreateMonitoringSchedule
Create
Yes
Amazon SageMaker Service
CreateNotebookInstance
Create
Yes
Amazon SageMaker Service
CreateNotebookInstanceLifecycleConfig
Create
Yes
Amazon SageMaker Service
CreatePipeline
Create
Yes
Amazon SageMaker Service
CreatePresignedDomainUrl
Create
Yes
Amazon SageMaker Service
CreatePresignedNotebookInstanceUrl
Create
Yes
Amazon SageMaker Service
CreateProcessingJob
Create
Yes
Amazon SageMaker Service
CreateProject
Create
Yes
Amazon SageMaker Service
CreateStudioLifecycleConfig
Create
Yes
Amazon SageMaker Service
CreateTrainingJob
Create
Yes
Amazon SageMaker Service
CreateTransformJob
Create
Yes
Amazon SageMaker Service
CreateTrial
Create
Yes
Amazon SageMaker Service
CreateTrialComponent
Create
Yes
Amazon SageMaker Service
CreateUserProfile
Create
Yes
Amazon SageMaker Service
CreateWorkforce
Create
Yes
Amazon SageMaker Service
CreateWorkteam
Create
Yes
Amazon SageMaker Service
DeleteAction
Delete
Yes
Amazon SageMaker Service
DeleteAlgorithm
Delete
Yes
Amazon SageMaker Service
DeleteApp
Delete
Yes
Amazon SageMaker Service
DeleteAppImageConfig
Delete
Yes
Amazon SageMaker Service
DeleteArtifact
Delete
Yes
Amazon SageMaker Service
DeleteAssociation
Delete
Yes
Amazon SageMaker Service
DeleteCodeRepository
Delete
Yes
Amazon SageMaker Service
DeleteContext
Delete
Yes
Amazon SageMaker Service
DeleteDataQualityJobDefinition
Delete
Yes
Amazon SageMaker Service
DeleteDeviceFleet
Delete
Yes
Amazon SageMaker Service
DeleteDomain
Delete
Yes
Amazon SageMaker Service
DeleteEndpoint
Delete
Yes
Amazon SageMaker Service
DeleteEndpointConfig
Delete
Yes
Amazon SageMaker Service
DeleteExperiment
Delete
Yes
Amazon SageMaker Service
DeleteFeatureGroup
Delete
Yes
Amazon SageMaker Service
DeleteFlowDefinition
Delete
Yes
Amazon SageMaker Service
DeleteHumanTaskUi
Delete
Yes
Amazon SageMaker Service
DeleteImage
Delete
Yes
Amazon SageMaker Service
DeleteImageVersion
Delete
Yes
Amazon SageMaker Service
DeleteModel
Delete
Yes
Amazon SageMaker Service
DeleteModelBiasJobDefinition
Delete
Yes
Amazon SageMaker Service
DeleteModelExplainabilityJobDefinition
Delete
Yes
Amazon SageMaker Service
DeleteModelPackage
Delete
Yes
Amazon SageMaker Service
DeleteModelPackageGroup
Delete
Yes
Amazon SageMaker Service
DeleteModelPackageGroupPolicy
Delete
Yes
Amazon SageMaker Service
DeleteModelQualityJobDefinition
Delete
Yes
Amazon SageMaker Service
DeleteMonitoringSchedule
Delete
Yes
Amazon SageMaker Service
DeleteNotebookInstance
Delete
Yes
Amazon SageMaker Service
DeleteNotebookInstanceLifecycleConfig
Delete
Yes
Amazon SageMaker Service
DeletePipeline
Delete
Yes
Amazon SageMaker Service
DeleteProject
Delete
Yes
Amazon SageMaker Service
DeleteStudioLifecycleConfig
Delete
Yes
Amazon SageMaker Service
DeleteTags
Delete
Yes
Amazon SageMaker Service
DeleteTrial
Delete
Yes
Amazon SageMaker Service
DeleteTrialComponent
Delete
Yes
Amazon SageMaker Service
DeleteUserProfile
Delete
Yes
Amazon SageMaker Service
DeleteWorkforce
Delete
Yes
Amazon SageMaker Service
DeleteWorkteam
Delete
Yes
Amazon SageMaker Service
DeregisterDevices
Deregister
Yes
Amazon SageMaker Service
DescribeAction
View
Yes
Amazon SageMaker Service
DescribeAlgorithm
View
Yes
Amazon SageMaker Service
DescribeApp
View
Yes
Amazon SageMaker Service
DescribeAppImageConfig
View
Yes
Amazon SageMaker Service
DescribeArtifact
View
Yes
Amazon SageMaker Service
DescribeAutoMLJob
View
Yes
Amazon SageMaker Service
DescribeCodeRepository
View
Yes
Amazon SageMaker Service
DescribeCompilationJob
View
Yes
Amazon SageMaker Service
DescribeContext
View
Yes
Amazon SageMaker Service
DescribeDataQualityJobDefinition
View
Yes
Amazon SageMaker Service
DescribeDevice
View
Yes
Amazon SageMaker Service
DescribeDeviceFleet
View
Yes
Amazon SageMaker Service
DescribeDomain
View
Yes
Amazon SageMaker Service
DescribeEdgePackagingJob
View
Yes
Amazon SageMaker Service
DescribeEndpoint
View
Yes
Amazon SageMaker Service
DescribeEndpointConfig
View
Yes
Amazon SageMaker Service
DescribeExperiment
View
Yes
Amazon SageMaker Service
DescribeFeatureGroup
View
Yes
Amazon SageMaker Service
DescribeFlowDefinition
View
Yes
Amazon SageMaker Service
DescribeHumanTaskUi
View
Yes
Amazon SageMaker Service
DescribeHyperParameterTuningJob
View
Yes
Amazon SageMaker Service
DescribeImage
View
Yes
Amazon SageMaker Service
DescribeImageVersion
View
Yes
Amazon SageMaker Service
DescribeLabelingJob
View
Yes
Amazon SageMaker Service
DescribeModel
View
Yes
Amazon SageMaker Service
DescribeModelBiasJobDefinition
View
Yes
Amazon SageMaker Service
DescribeModelExplainabilityJobDefinition
View
Yes
Amazon SageMaker Service
DescribeModelPackage
View
Yes
Amazon SageMaker Service
DescribeModelPackageGroup
View
Yes
Amazon SageMaker Service
DescribeModelQualityJobDefinition
View
Yes
Amazon SageMaker Service
DescribeMonitoringSchedule
View
Yes
Amazon SageMaker Service
DescribeNotebookInstance
View
Yes
Amazon SageMaker Service
DescribeNotebookInstanceLifecycleConfig
View
Yes
Amazon SageMaker Service
DescribePipeline
View
Yes
Amazon SageMaker Service
DescribePipelineDefinitionForExecution
View
Yes
Amazon SageMaker Service
DescribePipelineExecution
View
Yes
Amazon SageMaker Service
DescribeProcessingJob
View
Yes
Amazon SageMaker Service
DescribeProject
View
Yes
Amazon SageMaker Service
DescribeStudioLifecycleConfig
View
Yes
Amazon SageMaker Service
DescribeSubscribedWorkteam
View
Yes
Amazon SageMaker Service
DescribeTrainingJob
View
Yes
Amazon SageMaker Service
DescribeTransformJob
View
Yes
Amazon SageMaker Service
DescribeTrial
View
Yes
Amazon SageMaker Service
DescribeTrialComponent
View
Yes
Amazon SageMaker Service
DescribeUserProfile
View
Yes
Amazon SageMaker Service
DescribeWorkforce
View
Yes
Amazon SageMaker Service
DescribeWorkteam
View
Yes
Amazon SageMaker Service
DisableSagemakerServicecatalogPortfolio
Edit
Yes
Amazon SageMaker Service
DisassociateTrialComponent
Delete
Yes
Amazon SageMaker Service
EnableSagemakerServicecatalogPortfolio
Enable
Yes
Amazon SageMaker Service
GetDeviceFleetReport
View
Yes
Amazon SageMaker Service
GetModelPackageGroupPolicy
View
Yes
Amazon SageMaker Service
GetSagemakerServicecatalogPortfolioStatus
View
Yes
Amazon SageMaker Service
GetSearchSuggestions
View
Yes
Amazon SageMaker Service
ListActions
View
Yes
Amazon SageMaker Service
ListAlgorithms
View
Yes
Amazon SageMaker Service
ListAppImageConfigs
View
Yes
Amazon SageMaker Service
ListApps
View
Yes
Amazon SageMaker Service
ListArtifacts
View
Yes
Amazon SageMaker Service
ListAssociations
View
Yes
Amazon SageMaker Service
ListAutoMLJobs
View
Yes
Amazon SageMaker Service
ListCandidatesForAutoMLJob
View
Yes
Amazon SageMaker Service
ListCodeRepositories
View
Yes
Amazon SageMaker Service
ListCompilationJobs
View
Yes
Amazon SageMaker Service
ListContexts
View
Yes
Amazon SageMaker Service
ListDataQualityJobDefinitions
View
Yes
Amazon SageMaker Service
ListDeviceFleets
View
Yes
Amazon SageMaker Service
ListDevices
View
Yes
Amazon SageMaker Service
ListDomains
View
Yes
Amazon SageMaker Service
ListEdgePackagingJobs
View
Yes
Amazon SageMaker Service
ListEndpointConfigs
View
Yes
Amazon SageMaker Service
ListEndpoints
View
Yes
Amazon SageMaker Service
ListExperiments
View
Yes
Amazon SageMaker Service
ListFeatureGroups
View
Yes
Amazon SageMaker Service
ListFlowDefinitions
View
Yes
Amazon SageMaker Service
ListHumanTaskUis
View
Yes
Amazon SageMaker Service
ListHyperParameterTuningJobs
View
Yes
Amazon SageMaker Service
ListImageVersions
View
Yes
Amazon SageMaker Service
ListImages
View
Yes
Amazon SageMaker Service
ListLabelingJobs
View
Yes
Amazon SageMaker Service
ListLabelingJobsForWorkteam
View
Yes
Amazon SageMaker Service
ListModelBiasJobDefinitions
View
Yes
Amazon SageMaker Service
ListModelExplainabilityJobDefinitions
View
Yes
Amazon SageMaker Service
ListModelPackageGroups
View
Yes
Amazon SageMaker Service
ListModelPackages
View
Yes
Amazon SageMaker Service
ListModelQualityJobDefinitions
View
Yes
Amazon SageMaker Service
ListModels
View
Yes
Amazon SageMaker Service
ListMonitoringExecutions
View
Yes
Amazon SageMaker Service
ListMonitoringSchedules
View
Yes
Amazon SageMaker Service
ListNotebookInstanceLifecycleConfigs
View
Yes
Amazon SageMaker Service
ListNotebookInstances
View
Yes
Amazon SageMaker Service
ListPipelineExecutionSteps
View
Yes
Amazon SageMaker Service
ListPipelineExecutions
View
Yes
Amazon SageMaker Service
ListPipelineParametersForExecution
View
Yes
Amazon SageMaker Service
ListPipelines
View
Yes
Amazon SageMaker Service
ListProcessingJobs
View
Yes
Amazon SageMaker Service
ListProjects
View
Yes
Amazon SageMaker Service
ListStudioLifecycleConfigs
View
Yes
Amazon SageMaker Service
ListSubscribedWorkteams
View
Yes
Amazon SageMaker Service
ListTags
View
Yes
Amazon SageMaker Service
ListTrainingJobs
View
Yes
Amazon SageMaker Service
ListTrainingJobsForHyperParameterTuningJob
View
Yes
Amazon SageMaker Service
ListTransformJobs
View
Yes
Amazon SageMaker Service
ListTrialComponents
View
Yes
Amazon SageMaker Service
ListTrials
View
Yes
Amazon SageMaker Service
ListUserProfiles
View
Yes
Amazon SageMaker Service
ListWorkforces
View
Yes
Amazon SageMaker Service
ListWorkteams
View
Yes
Amazon SageMaker Service
PutModelPackageGroupPolicy
Edit
Yes
Amazon SageMaker Service
RegisterDevices
Register
Yes
Amazon SageMaker Service
RenderUiTemplate
Create
Yes
Amazon SageMaker Service
RetryPipelineExecution
Create
Yes
Amazon SageMaker Service
Search
Search
Yes
Amazon SageMaker Service
SendPipelineExecutionStepFailure
Send
Yes
Amazon SageMaker Service
SendPipelineExecutionStepSuccess
Send
Yes
Amazon SageMaker Service
StartMonitoringSchedule
Start
Yes
Amazon SageMaker Service
StartNotebookInstance
Start
Yes
Amazon SageMaker Service
StartPipelineExecution
Start
Yes
Amazon SageMaker Service
StopAutoMLJob
Stop
Yes
Amazon SageMaker Service
StopCompilationJob
Stop
Yes
Amazon SageMaker Service
StopEdgePackagingJob
Stop
Yes
Amazon SageMaker Service
StopHyperParameterTuningJob
Stop
Yes
Amazon SageMaker Service
StopLabelingJob
Stop
Yes
Amazon SageMaker Service
StopMonitoringSchedule
Stop
Yes
Amazon SageMaker Service
StopNotebookInstance
Stop
Yes
Amazon SageMaker Service
StopPipelineExecution
Stop
Yes
Amazon SageMaker Service
StopProcessingJob
Stop
Yes
Amazon SageMaker Service
StopTrainingJob
Stop
Yes
Amazon SageMaker Service
StopTransformJob
Stop
Yes
Amazon SageMaker Service
UpdateAction
Edit
Yes
Amazon SageMaker Service
UpdateAppImageConfig
Edit
Yes
Amazon SageMaker Service
UpdateArtifact
Edit
Yes
Amazon SageMaker Service
UpdateCodeRepository
Edit
Yes
Amazon SageMaker Service
UpdateContext
Edit
Yes
Amazon SageMaker Service
UpdateDeviceFleet
Edit
Yes
Amazon SageMaker Service
UpdateDevices
Edit
Yes
Amazon SageMaker Service
UpdateDomain
Edit
Yes
Amazon SageMaker Service
UpdateEndpoint
Edit
Yes
Amazon SageMaker Service
UpdateEndpointWeightsAndCapacities
Edit
Yes
Amazon SageMaker Service
UpdateExperiment
Edit
Yes
Amazon SageMaker Service
UpdateImage
Edit
Yes
Amazon SageMaker Service
UpdateModelPackage
Edit
Yes
Amazon SageMaker Service
UpdateMonitoringSchedule
Edit
Yes
Amazon SageMaker Service
UpdateNotebookInstance
Edit
Yes
Amazon SageMaker Service
UpdateNotebookInstanceLifecycleConfig
Edit
Yes
Amazon SageMaker Service
UpdatePipeline
Edit
Yes
Amazon SageMaker Service
UpdatePipelineExecution
Edit
Yes
Amazon SageMaker Service
UpdateTrainingJob
Edit
Yes
Amazon SageMaker Service
UpdateTrial
Edit
Yes
Amazon SageMaker Service
UpdateTrialComponent
Edit
Yes
Amazon SageMaker Service
UpdateUserProfile
Edit
Yes
Amazon SageMaker Service
UpdateWorkforce
Edit
Yes
Amazon SageMaker Service
UpdateWorkteam
Edit
Yes
Amazon Managed Streaming for Kafka Connect
CreateConnector
Create
Yes
Amazon Managed Streaming for Kafka Connect
ListConnectors
View
Yes
Amazon Managed Streaming for Kafka Connect
CreateCustomPlugin
Create
Yes
Amazon Managed Streaming for Kafka Connect
ListCustomPlugins
View
Yes
Amazon Managed Streaming for Kafka Connect
CreateWorkerConfiguration
Create
Yes
Amazon Managed Streaming for Kafka Connect
ListWorkerConfigurations
View
Yes
Amazon Managed Streaming for Kafka Connect
DeleteConnector
Delete
Yes
Amazon Managed Streaming for Kafka Connect
DescribeConnector
View
Yes
Amazon Managed Streaming for Kafka Connect
DescribeCustomPlugin
View
Yes
Amazon Managed Streaming for Kafka Connect
DescribeWorkerConfiguration
View
Yes
Amazon Managed Streaming for Kafka Connect
UpdateConnector
Edit
Yes
Amazon Translate
CreateParallelData
Create
Yes
Amazon Translate
DeleteParallelData
Delete
Yes
Amazon Translate
DeleteTerminology
Delete
Yes
Amazon Translate
DescribeTextTranslationJob
View
Yes
Amazon Translate
GetParallelData
View
Yes
Amazon Translate
GetTerminology
View
Yes
Amazon Translate
ImportTerminology
Create
Yes
Amazon Translate
ListParallelData
View
Yes
Amazon Translate
ListTerminologies
View
Yes
Amazon Translate
ListTextTranslationJobs
View
Yes
Amazon Translate
StartTextTranslationJob
Start
Yes
Amazon Translate
StopTextTranslationJob
Stop
Yes
Amazon Translate
TranslateText
Create
Yes
Amazon Translate
UpdateParallelData
Edit
Yes
Amazon App Runner
AssociateCustomDomain
Create
Yes
Amazon App Runner
CreateAutoScalingConfiguration
Create
Yes
Amazon App Runner
CreateConnection
Create
Yes
Amazon App Runner
CreateService
Create
Yes
Amazon App Runner
DeleteAutoScalingConfiguration
Delete
Yes
Amazon App Runner
DeleteConnection
Delete
Yes
Amazon App Runner
DeleteService
Delete
Yes
Amazon App Runner
DescribeAutoScalingConfiguration
View
Yes
Amazon App Runner
DescribeCustomDomains
View
Yes
Amazon App Runner
DescribeService
View
Yes
Amazon App Runner
DisassociateCustomDomain
Delete
Yes
Amazon App Runner
ListAutoScalingConfigurations
View
Yes
Amazon App Runner
ListConnections
View
Yes
Amazon App Runner
ListOperations
View
Yes
Amazon App Runner
ListServices
View
Yes
Amazon App Runner
ListTagsForResource
View
Yes
Amazon App Runner
PauseService
Create
Yes
Amazon App Runner
ResumeService
Start
Yes
Amazon App Runner
StartDeployment
Start
Yes
Amazon App Runner
TagResource
Create
Yes
Amazon App Runner
UntagResource
Delete
Yes
Amazon App Runner
UpdateService
Edit
Yes
Amazon Cost Explorer Service
CreateAnomalyMonitor
Create
Yes
Amazon Cost Explorer Service
CreateAnomalySubscription
Create
Yes
Amazon Cost Explorer Service
CreateCostCategoryDefinition
Create
Yes
Amazon Cost Explorer Service
DeleteAnomalyMonitor
Delete
Yes
Amazon Cost Explorer Service
DeleteAnomalySubscription
Delete
Yes
Amazon Cost Explorer Service
DeleteCostCategoryDefinition
Delete
Yes
Amazon Cost Explorer Service
DescribeCostCategoryDefinition
View
Yes
Amazon Cost Explorer Service
GetAnomalies
View
Yes
Amazon Cost Explorer Service
GetAnomalyMonitors
View
Yes
Amazon Cost Explorer Service
GetAnomalySubscriptions
View
Yes
Amazon Cost Explorer Service
GetCostAndUsage
View
Yes
Amazon Cost Explorer Service
GetCostAndUsageWithResources
View
Yes
Amazon Cost Explorer Service
GetCostCategories
View
Yes
Amazon Cost Explorer Service
GetCostForecast
View
Yes
Amazon Cost Explorer Service
GetDimensionValues
View
Yes
Amazon Cost Explorer Service
GetReservationCoverage
View
Yes
Amazon Cost Explorer Service
GetReservationPurchaseRecommendation
View
Yes
Amazon Cost Explorer Service
GetReservationUtilization
View
Yes
Amazon Cost Explorer Service
GetRightsizingRecommendation
View
Yes
Amazon Cost Explorer Service
GetSavingsPlansCoverage
View
Yes
Amazon Cost Explorer Service
GetSavingsPlansPurchaseRecommendation
View
Yes
Amazon Cost Explorer Service
GetSavingsPlansUtilization
View
Yes
Amazon Cost Explorer Service
GetSavingsPlansUtilizationDetails
View
Yes
Amazon Cost Explorer Service
GetTags
View
Yes
Amazon Cost Explorer Service
GetUsageForecast
View
Yes
Amazon Cost Explorer Service
ListCostCategoryDefinitions
View
Yes
Amazon Cost Explorer Service
ProvideAnomalyFeedback
Create
Yes
Amazon Cost Explorer Service
UpdateAnomalyMonitor
Edit
Yes
Amazon Cost Explorer Service
UpdateAnomalySubscription
Edit
Yes
Amazon Cost Explorer Service
UpdateCostCategoryDefinition
Edit
Yes
Amazon Elastic MapReduce
AddInstanceFleet
Create
Yes
Amazon Elastic MapReduce
AddInstanceGroups
Create
Yes
Amazon Elastic MapReduce
AddJobFlowSteps
Create
Yes
Amazon Elastic MapReduce
AddTags
Create
Yes
Amazon Elastic MapReduce
CancelSteps
Delete
Yes
Amazon Elastic MapReduce
CreateSecurityConfiguration
Create
Yes
Amazon Elastic MapReduce
CreateStudio
Create
Yes
Amazon Elastic MapReduce
CreateStudioSessionMapping
Create
Yes
Amazon Elastic MapReduce
DeleteSecurityConfiguration
Delete
Yes
Amazon Elastic MapReduce
DeleteStudio
Delete
Yes
Amazon Elastic MapReduce
DeleteStudioSessionMapping
Delete
Yes
Amazon Elastic MapReduce
DescribeCluster
View
Yes
Amazon Elastic MapReduce
DescribeJobFlows
View
Yes
Amazon Elastic MapReduce
DescribeNotebookExecution
View
Yes
Amazon Elastic MapReduce
DescribeReleaseLabel
View
Yes
Amazon Elastic MapReduce
DescribeSecurityConfiguration
View
Yes
Amazon Elastic MapReduce
DescribeStep
View
Yes
Amazon Elastic MapReduce
DescribeStudio
View
Yes
Amazon Elastic MapReduce
GetAutoTerminationPolicy
View
Yes
Amazon Elastic MapReduce
GetBlockPublicAccessConfiguration
View
Yes
Amazon Elastic MapReduce
GetManagedScalingPolicy
View
Yes
Amazon Elastic MapReduce
GetStudioSessionMapping
View
Yes
Amazon Elastic MapReduce
ListBootstrapActions
View
Yes
Amazon Elastic MapReduce
ListClusters
View
Yes
Amazon Elastic MapReduce
ListInstanceFleets
View
Yes
Amazon Elastic MapReduce
ListInstanceGroups
View
Yes
Amazon Elastic MapReduce
ListInstances
View
Yes
Amazon Elastic MapReduce
ListNotebookExecutions
View
Yes
Amazon Elastic MapReduce
ListReleaseLabels
View
Yes
Amazon Elastic MapReduce
ListSecurityConfigurations
View
Yes
Amazon Elastic MapReduce
ListSteps
View
Yes
Amazon Elastic MapReduce
ListStudioSessionMappings
View
Yes
Amazon Elastic MapReduce
ListStudios
View
Yes
Amazon Elastic MapReduce
ModifyCluster
Edit
Yes
Amazon Elastic MapReduce
ModifyInstanceFleet
Edit
Yes
Amazon Elastic MapReduce
ModifyInstanceGroups
Edit
Yes
Amazon Elastic MapReduce
PutAutoScalingPolicy
Edit
Yes
Amazon Elastic MapReduce
PutAutoTerminationPolicy
Edit
Yes
Amazon Elastic MapReduce
PutBlockPublicAccessConfiguration
Edit
Yes
Amazon Elastic MapReduce
PutManagedScalingPolicy
Edit
Yes
Amazon Elastic MapReduce
RemoveAutoScalingPolicy
Delete
Yes
Amazon Elastic MapReduce
RemoveAutoTerminationPolicy
Delete
Yes
Amazon Elastic MapReduce
RemoveManagedScalingPolicy
Delete
Yes
Amazon Elastic MapReduce
RemoveTags
Delete
Yes
Amazon Elastic MapReduce
RunJobFlow
Create
Yes
Amazon Elastic MapReduce
SetTerminationProtection
Create
Yes
Amazon Elastic MapReduce
SetVisibleToAllUsers
Create
Yes
Amazon Elastic MapReduce
StartNotebookExecution
Start
Yes
Amazon Elastic MapReduce
StopNotebookExecution
Stop
Yes
Amazon Elastic MapReduce
TerminateJobFlows
Terminate
Yes
Amazon Elastic MapReduce
UpdateStudio
Edit
Yes
Amazon Elastic MapReduce
UpdateStudioSessionMapping
Edit
Yes
Amazon Auto Scaling Plans
CreateScalingPlan
Create
Yes
Amazon Auto Scaling Plans
DeleteScalingPlan
Delete
Yes
Amazon Auto Scaling Plans
DescribeScalingPlanResources
View
Yes
Amazon Auto Scaling Plans
DescribeScalingPlans
View
Yes
Amazon Auto Scaling Plans
GetScalingPlanResourceForecastData
View
Yes
Amazon Auto Scaling Plans
UpdateScalingPlan
Edit
Yes
Amazon CodeStar Notifications
CreateNotificationRule
Create
Yes
Amazon CodeStar Notifications
DeleteNotificationRule
Delete
Yes
Amazon CodeStar Notifications
DeleteTarget
Delete
Yes
Amazon CodeStar Notifications
DescribeNotificationRule
View
Yes
Amazon CodeStar Notifications
ListEventTypes
View
Yes
Amazon CodeStar Notifications
ListNotificationRules
View
Yes
Amazon CodeStar Notifications
ListTagsForResource
View
Yes
Amazon CodeStar Notifications
ListTargets
View
Yes
Amazon CodeStar Notifications
Subscribe
Create
Yes
Amazon CodeStar Notifications
TagResource
Create
Yes
Amazon CodeStar Notifications
Unsubscribe
Create
Yes
Amazon CodeStar Notifications
UntagResource
Delete
Yes
Amazon CodeStar Notifications
UpdateNotificationRule
Edit
Yes
Amazon Chime SDK Messaging
CreateChannelMembership
Create
Yes
Amazon Chime SDK Messaging
CreateChannel
Create
Yes
Amazon Chime SDK Messaging
CreateChannelBan
Create
Yes
Amazon Chime SDK Messaging
ListChannelBans
View
Yes
Amazon Chime SDK Messaging
ListChannelMemberships
View
Yes
Amazon Chime SDK Messaging
CreateChannelModerator
Create
Yes
Amazon Chime SDK Messaging
ListChannelModerators
View
Yes
Amazon Chime SDK Messaging
DeleteChannel
Delete
Yes
Amazon Chime SDK Messaging
DescribeChannel
View
Yes
Amazon Chime SDK Messaging
UpdateChannel
Edit
Yes
Amazon Chime SDK Messaging
DeleteChannelBan
Delete
Yes
Amazon Chime SDK Messaging
DescribeChannelBan
View
Yes
Amazon Chime SDK Messaging
DeleteChannelMembership
Delete
Yes
Amazon Chime SDK Messaging
DescribeChannelMembership
View
Yes
Amazon Chime SDK Messaging
DeleteChannelMessage
Delete
Yes
Amazon Chime SDK Messaging
GetChannelMessage
View
Yes
Amazon Chime SDK Messaging
UpdateChannelMessage
Edit
Yes
Amazon Chime SDK Messaging
DeleteChannelModerator
Delete
Yes
Amazon Chime SDK Messaging
DescribeChannelModerator
View
Yes
Amazon Chime SDK Messaging
DescribeChannelMembershipForAppInstanceUser
View
Yes
Amazon Chime SDK Messaging
DescribeChannelModeratedByAppInstanceUser
View
Yes
Amazon Chime SDK Messaging
GetMessagingSessionEndpoint
View
Yes
Amazon Chime SDK Messaging
ListChannelMembershipsForAppInstanceUser
View
Yes
Amazon Chime SDK Messaging
ListChannelMessages
View
Yes
Amazon Chime SDK Messaging
SendChannelMessage
Send
Yes
Amazon Chime SDK Messaging
ListChannels
View
Yes
Amazon Chime SDK Messaging
ListChannelsModeratedByAppInstanceUser
View
Yes
Amazon Chime SDK Messaging
RedactChannelMessage
Create
Yes
Amazon Chime SDK Messaging
UpdateChannelReadMarker
Edit
Yes
Amazon OpenSearch Service
AcceptInboundConnection
Approve
Yes
Amazon OpenSearch Service
AddTags
Create
Yes
Amazon OpenSearch Service
AssociatePackage
Create
Yes
Amazon OpenSearch Service
CancelServiceSoftwareUpdate
Delete
Yes
Amazon OpenSearch Service
CreateDomain
Create
Yes
Amazon OpenSearch Service
CreateOutboundConnection
Create
Yes
Amazon OpenSearch Service
CreatePackage
Create
Yes
Amazon OpenSearch Service
DeleteDomain
Delete
Yes
Amazon OpenSearch Service
DescribeDomain
View
Yes
Amazon OpenSearch Service
DeleteInboundConnection
Delete
Yes
Amazon OpenSearch Service
DeleteOutboundConnection
Delete
Yes
Amazon OpenSearch Service
DeletePackage
Delete
Yes
Amazon OpenSearch Service
DescribeDomainAutoTunes
View
Yes
Amazon OpenSearch Service
DescribeDomainConfig
View
Yes
Amazon OpenSearch Service
UpdateDomainConfig
Edit
Yes
Amazon OpenSearch Service
DescribeDomains
View
Yes
Amazon OpenSearch Service
DescribeInboundConnections
View
Yes
Amazon OpenSearch Service
DescribeInstanceTypeLimits
View
Yes
Amazon OpenSearch Service
DescribeOutboundConnections
View
Yes
Amazon OpenSearch Service
DescribePackages
View
Yes
Amazon OpenSearch Service
DescribeReservedInstanceOfferings
View
Yes
Amazon OpenSearch Service
DescribeReservedInstances
View
Yes
Amazon OpenSearch Service
DissociatePackage
Create
Yes
Amazon OpenSearch Service
GetCompatibleVersions
View
Yes
Amazon OpenSearch Service
GetPackageVersionHistory
View
Yes
Amazon OpenSearch Service
GetUpgradeHistory
View
Yes
Amazon OpenSearch Service
GetUpgradeStatus
View
Yes
Amazon OpenSearch Service
ListDomainNames
View
Yes
Amazon OpenSearch Service
ListDomainsForPackage
View
Yes
Amazon OpenSearch Service
ListInstanceTypeDetails
View
Yes
Amazon OpenSearch Service
ListPackagesForDomain
View
Yes
Amazon OpenSearch Service
ListTags
View
Yes
Amazon OpenSearch Service
ListVersions
View
Yes
Amazon OpenSearch Service
PurchaseReservedInstanceOffering
Purchase
Yes
Amazon OpenSearch Service
RejectInboundConnection
Reject
Yes
Amazon OpenSearch Service
RemoveTags
Delete
Yes
Amazon OpenSearch Service
StartServiceSoftwareUpdate
Start
Yes
Amazon OpenSearch Service
UpdatePackage
Edit
Yes
Amazon OpenSearch Service
UpgradeDomain
Create
Yes
Amazon IoT Wireless
AssociateAwsAccountWithPartnerAccount
Create
Yes
Amazon IoT Wireless
ListPartnerAccounts
View
Yes
Amazon IoT Wireless
AssociateWirelessDeviceWithThing
Create
Yes
Amazon IoT Wireless
DisassociateWirelessDeviceFromThing
Delete
Yes
Amazon IoT Wireless
AssociateWirelessGatewayWithCertificate
Create
Yes
Amazon IoT Wireless
DisassociateWirelessGatewayFromCertificate
Delete
Yes
Amazon IoT Wireless
GetWirelessGatewayCertificate
View
Yes
Amazon IoT Wireless
AssociateWirelessGatewayWithThing
Create
Yes
Amazon IoT Wireless
DisassociateWirelessGatewayFromThing
Delete
Yes
Amazon IoT Wireless
CreateDestination
Create
Yes
Amazon IoT Wireless
ListDestinations
View
Yes
Amazon IoT Wireless
CreateDeviceProfile
Create
Yes
Amazon IoT Wireless
ListDeviceProfiles
View
Yes
Amazon IoT Wireless
CreateServiceProfile
Create
Yes
Amazon IoT Wireless
ListServiceProfiles
View
Yes
Amazon IoT Wireless
CreateWirelessDevice
Create
Yes
Amazon IoT Wireless
ListWirelessDevices
View
Yes
Amazon IoT Wireless
CreateWirelessGateway
Create
Yes
Amazon IoT Wireless
ListWirelessGateways
View
Yes
Amazon IoT Wireless
CreateWirelessGatewayTask
Create
Yes
Amazon IoT Wireless
DeleteWirelessGatewayTask
Delete
Yes
Amazon IoT Wireless
GetWirelessGatewayTask
View
Yes
Amazon IoT Wireless
CreateWirelessGatewayTaskDefinition
Create
Yes
Amazon IoT Wireless
ListWirelessGatewayTaskDefinitions
View
Yes
Amazon IoT Wireless
DeleteDestination
Delete
Yes
Amazon IoT Wireless
GetDestination
View
Yes
Amazon IoT Wireless
UpdateDestination
Edit
Yes
Amazon IoT Wireless
DeleteDeviceProfile
Delete
Yes
Amazon IoT Wireless
GetDeviceProfile
View
Yes
Amazon IoT Wireless
DeleteServiceProfile
Delete
Yes
Amazon IoT Wireless
GetServiceProfile
View
Yes
Amazon IoT Wireless
DeleteWirelessDevice
Delete
Yes
Amazon IoT Wireless
UpdateWirelessDevice
Edit
Yes
Amazon IoT Wireless
DeleteWirelessGateway
Delete
Yes
Amazon IoT Wireless
UpdateWirelessGateway
Edit
Yes
Amazon IoT Wireless
DeleteWirelessGatewayTaskDefinition
Delete
Yes
Amazon IoT Wireless
GetWirelessGatewayTaskDefinition
View
Yes
Amazon IoT Wireless
DisassociateAwsAccountFromPartnerAccount
Delete
Yes
Amazon IoT Wireless
GetPartnerAccount
View
Yes
Amazon IoT Wireless
UpdatePartnerAccount
Edit
Yes
Amazon IoT Wireless
GetLogLevelsByResourceTypes
View
Yes
Amazon IoT Wireless
ResetAllResourceLogLevels
Delete
Yes
Amazon IoT Wireless
UpdateLogLevelsByResourceTypes
Edit
Yes
Amazon IoT Wireless
GetResourceLogLevel
View
Yes
Amazon IoT Wireless
PutResourceLogLevel
Edit
Yes
Amazon IoT Wireless
ResetResourceLogLevel
Delete
Yes
Amazon IoT Wireless
GetServiceEndpoint
View
Yes
Amazon IoT Wireless
GetWirelessDevice
View
Yes
Amazon IoT Wireless
GetWirelessDeviceStatistics
View
Yes
Amazon IoT Wireless
GetWirelessGateway
View
Yes
Amazon IoT Wireless
GetWirelessGatewayFirmwareInformation
View
Yes
Amazon IoT Wireless
GetWirelessGatewayStatistics
View
Yes
Amazon IoT Wireless
ListTagsForResource
View
Yes
Amazon IoT Wireless
TagResource
Create
Yes
Amazon IoT Wireless
SendDataToWirelessDevice
Send
Yes
Amazon IoT Wireless
TestWirelessDevice
Create
Yes
Amazon IoT Wireless
UntagResource
Delete
Yes
Amazon Lake Formation
AddLFTagsToResource
Create
Yes
Amazon Lake Formation
GrantPermissions
Create
Yes
Amazon Lake Formation
RevokePermissions
Delete
Yes
Amazon Lake Formation
CreateLFTag
Create
Yes
Amazon Lake Formation
DeleteLFTag
Delete
Yes
Amazon Lake Formation
DeregisterResource
Deregister
Yes
Amazon Lake Formation
DescribeResource
View
Yes
Amazon Lake Formation
GetDataLakeSettings
View
Yes
Amazon Lake Formation
GetEffectivePermissionsForPath
View
Yes
Amazon Lake Formation
GetLFTag
View
Yes
Amazon Lake Formation
GetResourceLFTags
View
Yes
Amazon Lake Formation
ListLFTags
View
Yes
Amazon Lake Formation
ListPermissions
View
Yes
Amazon Lake Formation
ListResources
View
Yes
Amazon Lake Formation
PutDataLakeSettings
Edit
Yes
Amazon Lake Formation
RegisterResource
Register
Yes
Amazon Lake Formation
RemoveLFTagsFromResource
Delete
Yes
Amazon Lake Formation
SearchDatabasesByLFTags
Search
Yes
Amazon Lake Formation
SearchTablesByLFTags
Search
Yes
Amazon Lake Formation
UpdateLFTag
Edit
Yes
Amazon Lake Formation
UpdateResource
Edit
Yes
Amazon Support
AddAttachmentsToSet
Create
Yes
Amazon Support
AddCommunicationToCase
Create
Yes
Amazon Support
CreateCase
Create
Yes
Amazon Support
DescribeAttachment
View
Yes
Amazon Support
DescribeCases
View
Yes
Amazon Support
DescribeCommunications
View
Yes
Amazon Support
DescribeServices
View
Yes
Amazon Support
DescribeSeverityLevels
View
Yes
Amazon Support
DescribeTrustedAdvisorCheckRefreshStatuses
View
Yes
Amazon Support
DescribeTrustedAdvisorCheckResult
View
Yes
Amazon Support
DescribeTrustedAdvisorCheckSummaries
View
Yes
Amazon Support
DescribeTrustedAdvisorChecks
View
Yes
Amazon Support
RefreshTrustedAdvisorCheck
Create
Yes
Amazon Support
ResolveCase
Create
Yes
Amazon HealthLake
CreateFHIRDatastore
Create
Yes
Amazon HealthLake
DeleteFHIRDatastore
Delete
Yes
Amazon HealthLake
DescribeFHIRDatastore
View
Yes
Amazon HealthLake
DescribeFHIRExportJob
View
Yes
Amazon HealthLake
DescribeFHIRImportJob
View
Yes
Amazon HealthLake
ListFHIRDatastores
View
Yes
Amazon HealthLake
ListFHIRExportJobs
View
Yes
Amazon HealthLake
ListFHIRImportJobs
View
Yes
Amazon HealthLake
ListTagsForResource
View
Yes
Amazon HealthLake
StartFHIRExportJob
Start
Yes
Amazon HealthLake
StartFHIRImportJob
Start
Yes
Amazon HealthLake
TagResource
Create
Yes
Amazon HealthLake
UntagResource
Delete
Yes
Amazon Elemental MediaConvert
AssociateCertificate
Create
Yes
Amazon Elemental MediaConvert
CancelJob
Delete
Yes
Amazon Elemental MediaConvert
GetJob
View
Yes
Amazon Elemental MediaConvert
CreateJob
Create
Yes
Amazon Elemental MediaConvert
ListJobs
View
Yes
Amazon Elemental MediaConvert
CreateJobTemplate
Create
Yes
Amazon Elemental MediaConvert
ListJobTemplates
View
Yes
Amazon Elemental MediaConvert
CreatePreset
Create
Yes
Amazon Elemental MediaConvert
ListPresets
View
Yes
Amazon Elemental MediaConvert
CreateQueue
Create
Yes
Amazon Elemental MediaConvert
ListQueues
View
Yes
Amazon Elemental MediaConvert
DeleteJobTemplate
Delete
Yes
Amazon Elemental MediaConvert
GetJobTemplate
View
Yes
Amazon Elemental MediaConvert
UpdateJobTemplate
Edit
Yes
Amazon Elemental MediaConvert
DeletePreset
Delete
Yes
Amazon Elemental MediaConvert
GetPreset
View
Yes
Amazon Elemental MediaConvert
UpdatePreset
Edit
Yes
Amazon Elemental MediaConvert
DeleteQueue
Delete
Yes
Amazon Elemental MediaConvert
GetQueue
View
Yes
Amazon Elemental MediaConvert
UpdateQueue
Edit
Yes
Amazon Elemental MediaConvert
DescribeEndpoints
View
Yes
Amazon Elemental MediaConvert
DisassociateCertificate
Delete
Yes
Amazon Elemental MediaConvert
ListTagsForResource
View
Yes
Amazon Elemental MediaConvert
UntagResource
Delete
Yes
Amazon Elemental MediaConvert
TagResource
Create
Yes
Amazon Config
GetAggregateResourceConfig
View
Yes
Amazon Config
GetResourceConfig
View
Yes
Amazon Config
DeleteAggregationAuthorization
Delete
Yes
Amazon Config
DeleteConfigRule
Delete
Yes
Amazon Config
DeleteConfigurationAggregator
Delete
Yes
Amazon Config
DeleteConfigurationRecorder
Delete
Yes
Amazon Config
DeleteConformancePack
Delete
Yes
Amazon Config
DeleteDeliveryChannel
Delete
Yes
Amazon Config
DeleteEvaluationResults
Delete
Yes
Amazon Config
DeleteOrganizationConfigRule
Delete
Yes
Amazon Config
DeleteOrganizationConformancePack
Delete
Yes
Amazon Config
DeletePendingAggregationRequest
Delete
Yes
Amazon Config
DeleteRemediationConfiguration
Delete
Yes
Amazon Config
DeleteRemediationExceptions
Delete
Yes
Amazon Config
DeleteResourceConfig
Delete
Yes
Amazon Config
DeleteRetentionConfiguration
Delete
Yes
Amazon Config
DeleteStoredQuery
Delete
Yes
Amazon Config
DeliverConfigSnapshot
Create
Yes
Amazon Config
DescribeAggregateComplianceByConfigRules
View
Yes
Amazon Config
DescribeAggregateComplianceByConformancePacks
View
Yes
Amazon Config
DescribeAggregationAuthorizations
View
Yes
Amazon Config
DescribeComplianceByConfigRule
View
Yes
Amazon Config
DescribeComplianceByResource
View
Yes
Amazon Config
DescribeConfigRuleEvaluationStatus
View
Yes
Amazon Config
DescribeConfigRules
View
Yes
Amazon Config
DescribeConfigurationAggregatorSourcesStatus
View
Yes
Amazon Config
DescribeConfigurationAggregators
View
Yes
Amazon Config
DescribeConfigurationRecorderStatus
View
Yes
Amazon Config
DescribeConfigurationRecorders
View
Yes
Amazon Config
DescribeConformancePackCompliance
View
Yes
Amazon Config
DescribeConformancePackStatus
View
Yes
Amazon Config
DescribeConformancePacks
View
Yes
Amazon Config
DescribeDeliveryChannelStatus
View
Yes
Amazon Config
DescribeDeliveryChannels
View
Yes
Amazon Config
DescribeOrganizationConfigRuleStatuses
View
Yes
Amazon Config
DescribeOrganizationConfigRules
View
Yes
Amazon Config
DescribeOrganizationConformancePackStatuses
View
Yes
Amazon Config
DescribeOrganizationConformancePacks
View
Yes
Amazon Config
DescribePendingAggregationRequests
View
Yes
Amazon Config
DescribeRemediationConfigurations
View
Yes
Amazon Config
DescribeRemediationExceptions
View
Yes
Amazon Config
DescribeRemediationExecutionStatus
View
Yes
Amazon Config
DescribeRetentionConfigurations
View
Yes
Amazon Config
GetAggregateComplianceDetailsByConfigRule
View
Yes
Amazon Config
GetAggregateConfigRuleComplianceSummary
View
Yes
Amazon Config
GetAggregateConformancePackComplianceSummary
View
Yes
Amazon Config
GetAggregateDiscoveredResourceCounts
View
Yes
Amazon Config
GetComplianceDetailsByConfigRule
View
Yes
Amazon Config
GetComplianceDetailsByResource
View
Yes
Amazon Config
GetComplianceSummaryByConfigRule
View
Yes
Amazon Config
GetComplianceSummaryByResourceType
View
Yes
Amazon Config
GetConformancePackComplianceDetails
View
Yes
Amazon Config
GetConformancePackComplianceSummary
View
Yes
Amazon Config
GetDiscoveredResourceCounts
View
Yes
Amazon Config
GetOrganizationConfigRuleDetailedStatus
View
Yes
Amazon Config
GetOrganizationConformancePackDetailedStatus
View
Yes
Amazon Config
GetResourceConfigHistory
View
Yes
Amazon Config
GetStoredQuery
View
Yes
Amazon Config
ListAggregateDiscoveredResources
View
Yes
Amazon Config
ListDiscoveredResources
View
Yes
Amazon Config
ListStoredQueries
View
Yes
Amazon Config
ListTagsForResource
View
Yes
Amazon Config
PutAggregationAuthorization
Edit
Yes
Amazon Config
PutConfigRule
Edit
Yes
Amazon Config
PutConfigurationAggregator
Edit
Yes
Amazon Config
PutConfigurationRecorder
Edit
Yes
Amazon Config
PutConformancePack
Edit
Yes
Amazon Config
PutDeliveryChannel
Edit
Yes
Amazon Config
PutEvaluations
Edit
Yes
Amazon Config
PutExternalEvaluation
Edit
Yes
Amazon Config
PutOrganizationConfigRule
Edit
Yes
Amazon Config
PutOrganizationConformancePack
Edit
Yes
Amazon Config
PutRemediationConfigurations
Edit
Yes
Amazon Config
PutRemediationExceptions
Edit
Yes
Amazon Config
PutResourceConfig
Edit
Yes
Amazon Config
PutRetentionConfiguration
Edit
Yes
Amazon Config
PutStoredQuery
Edit
Yes
Amazon Config
SelectAggregateResourceConfig
Create
Yes
Amazon Config
SelectResourceConfig
Create
Yes
Amazon Config
StartConfigRulesEvaluation
Start
Yes
Amazon Config
StartConfigurationRecorder
Start
Yes
Amazon Config
StartRemediationExecution
Start
Yes
Amazon Config
StopConfigurationRecorder
Stop
Yes
Amazon Config
TagResource
Create
Yes
Amazon Config
UntagResource
Delete
Yes
Amazon CodeBuild
DeleteBuilds
Delete
Yes
Amazon CodeBuild
GetBuildes
View
Yes
Amazon CodeBuild
GetBuilds
View
Yes
Amazon CodeBuild
GetProjects
View
Yes
Amazon CodeBuild
GetReportGroups
View
Yes
Amazon CodeBuild
GetReports
View
Yes
Amazon CodeBuild
CreateProject
Create
Yes
Amazon CodeBuild
CreateReportGroup
Create
Yes
Amazon CodeBuild
CreateWebhook
Create
Yes
Amazon CodeBuild
DeleteBuild
Delete
Yes
Amazon CodeBuild
DeleteProject
Delete
Yes
Amazon CodeBuild
DeleteReport
Delete
Yes
Amazon CodeBuild
DeleteReportGroup
Delete
Yes
Amazon CodeBuild
DeleteResourcePolicy
Delete
Yes
Amazon CodeBuild
DeleteSourceCredentials
Delete
Yes
Amazon CodeBuild
DeleteWebhook
Delete
Yes
Amazon CodeBuild
DescribeCodeCoverages
View
Yes
Amazon CodeBuild
DescribeTestCases
View
Yes
Amazon CodeBuild
GetReportGroupTrend
View
Yes
Amazon CodeBuild
GetResourcePolicy
View
Yes
Amazon CodeBuild
ImportSourceCredentials
Create
Yes
Amazon CodeBuild
InvalidateProjectCache
Create
Yes
Amazon CodeBuild
ListBuildes
View
Yes
Amazon CodeBuild
ListBuildesForProject
View
Yes
Amazon CodeBuild
ListBuilds
View
Yes
Amazon CodeBuild
ListBuildsForProject
View
Yes
Amazon CodeBuild
ListCuratedEnvironmentImages
View
Yes
Amazon CodeBuild
ListProjects
View
Yes
Amazon CodeBuild
ListReportGroups
View
Yes
Amazon CodeBuild
ListReports
View
Yes
Amazon CodeBuild
ListReportsForReportGroup
View
Yes
Amazon CodeBuild
ListSharedProjects
View
Yes
Amazon CodeBuild
ListSharedReportGroups
View
Yes
Amazon CodeBuild
ListSourceCredentials
View
Yes
Amazon CodeBuild
PutResourcePolicy
Edit
Yes
Amazon CodeBuild
RetryBuild
Create
Yes
Amazon CodeBuild
StartBuild
Start
Yes
Amazon CodeBuild
StopBuild
Stop
Yes
Amazon CodeBuild
UpdateProject
Edit
Yes
Amazon CodeBuild
UpdateProjectVisibility
Edit
Yes
Amazon CodeBuild
UpdateReportGroup
Edit
Yes
Amazon CodeBuild
UpdateWebhook
Edit
Yes
Amazon OpsWorks
AssignInstance
Create
Yes
Amazon OpsWorks
AssignVolume
Create
Yes
Amazon OpsWorks
AssociateElasticIp
Create
Yes
Amazon OpsWorks
AttachElasticLoadBalancer
Attach
Yes
Amazon OpsWorks
CloneStack
Create
Yes
Amazon OpsWorks
CreateApp
Create
Yes
Amazon OpsWorks
CreateDeployment
Create
Yes
Amazon OpsWorks
CreateInstance
Create
Yes
Amazon OpsWorks
CreateLayer
Create
Yes
Amazon OpsWorks
CreateStack
Create
Yes
Amazon OpsWorks
CreateUserProfile
Create
Yes
Amazon OpsWorks
DeleteApp
Delete
Yes
Amazon OpsWorks
DeleteInstance
Delete
Yes
Amazon OpsWorks
DeleteLayer
Delete
Yes
Amazon OpsWorks
DeleteStack
Delete
Yes
Amazon OpsWorks
DeleteUserProfile
Delete
Yes
Amazon OpsWorks
DeregisterEcsCluster
Deregister
Yes
Amazon OpsWorks
DeregisterElasticIp
Deregister
Yes
Amazon OpsWorks
DeregisterInstance
Deregister
Yes
Amazon OpsWorks
DeregisterRdsDbInstance
Deregister
Yes
Amazon OpsWorks
DeregisterVolume
Deregister
Yes
Amazon OpsWorks
DescribeAgentVersions
View
Yes
Amazon OpsWorks
DescribeApps
View
Yes
Amazon OpsWorks
DescribeCommands
View
Yes
Amazon OpsWorks
DescribeDeployments
View
Yes
Amazon OpsWorks
DescribeEcsClusters
View
Yes
Amazon OpsWorks
DescribeElasticIps
View
Yes
Amazon OpsWorks
DescribeElasticLoadBalancers
View
Yes
Amazon OpsWorks
DescribeInstances
View
Yes
Amazon OpsWorks
DescribeLayers
View
Yes
Amazon OpsWorks
DescribeLoadBasedAutoScaling
View
Yes
Amazon OpsWorks
DescribeMyUserProfile
View
Yes
Amazon OpsWorks
DescribeOperatingSystems
View
Yes
Amazon OpsWorks
DescribePermissions
View
Yes
Amazon OpsWorks
DescribeRaidArrays
View
Yes
Amazon OpsWorks
DescribeRdsDbInstances
View
Yes
Amazon OpsWorks
DescribeServiceErrors
View
Yes
Amazon OpsWorks
DescribeStackProvisioningParameters
View
Yes
Amazon OpsWorks
DescribeStackSummary
View
Yes
Amazon OpsWorks
DescribeStacks
View
Yes
Amazon OpsWorks
DescribeTimeBasedAutoScaling
View
Yes
Amazon OpsWorks
DescribeUserProfiles
View
Yes
Amazon OpsWorks
DescribeVolumes
View
Yes
Amazon OpsWorks
DetachElasticLoadBalancer
Delete
Yes
Amazon OpsWorks
DisassociateElasticIp
Delete
Yes
Amazon OpsWorks
GetHostnameSuggestion
View
Yes
Amazon OpsWorks
GrantAccess
Create
Yes
Amazon OpsWorks
ListTags
View
Yes
Amazon OpsWorks
RebootInstance
Reboot
Yes
Amazon OpsWorks
RegisterEcsCluster
Register
Yes
Amazon OpsWorks
RegisterElasticIp
Register
Yes
Amazon OpsWorks
RegisterInstance
Register
Yes
Amazon OpsWorks
RegisterRdsDbInstance
Register
Yes
Amazon OpsWorks
RegisterVolume
Register
Yes
Amazon OpsWorks
SetLoadBasedAutoScaling
Create
Yes
Amazon OpsWorks
SetPermission
Create
Yes
Amazon OpsWorks
SetTimeBasedAutoScaling
Create
Yes
Amazon OpsWorks
StartInstance
Start
Yes
Amazon OpsWorks
StartStack
Start
Yes
Amazon OpsWorks
StopInstance
Stop
Yes
Amazon OpsWorks
StopStack
Stop
Yes
Amazon OpsWorks
TagResource
Create
Yes
Amazon OpsWorks
UnassignInstance
Delete
Yes
Amazon OpsWorks
UnassignVolume
Delete
Yes
Amazon OpsWorks
UntagResource
Delete
Yes
Amazon OpsWorks
UpdateApp
Edit
Yes
Amazon OpsWorks
UpdateElasticIp
Edit
Yes
Amazon OpsWorks
UpdateInstance
Edit
Yes
Amazon OpsWorks
UpdateLayer
Edit
Yes
Amazon OpsWorks
UpdateMyUserProfile
Edit
Yes
Amazon OpsWorks
UpdateRdsDbInstance
Edit
Yes
Amazon OpsWorks
UpdateStack
Edit
Yes
Amazon OpsWorks
UpdateUserProfile
Edit
Yes
Amazon OpsWorks
UpdateVolume
Edit
Yes
Amazon Route53 Recovery Readiness
CreateCell
Create
Yes
Amazon Route53 Recovery Readiness
ListCells
View
Yes
Amazon Route53 Recovery Readiness
CreateCrossAccountAuthorization
Create
Yes
Amazon Route53 Recovery Readiness
ListCrossAccountAuthorizations
View
Yes
Amazon Route53 Recovery Readiness
CreateReadinessCheck
Create
Yes
Amazon Route53 Recovery Readiness
ListReadinessChecks
View
Yes
Amazon Route53 Recovery Readiness
CreateRecoveryGroup
Create
Yes
Amazon Route53 Recovery Readiness
ListRecoveryGroups
View
Yes
Amazon Route53 Recovery Readiness
CreateResourceSet
Create
Yes
Amazon Route53 Recovery Readiness
ListResourceSets
View
Yes
Amazon Route53 Recovery Readiness
DeleteCell
Delete
Yes
Amazon Route53 Recovery Readiness
GetCell
View
Yes
Amazon Route53 Recovery Readiness
UpdateCell
Edit
Yes
Amazon Route53 Recovery Readiness
DeleteCrossAccountAuthorization
Delete
Yes
Amazon Route53 Recovery Readiness
DeleteReadinessCheck
Delete
Yes
Amazon Route53 Recovery Readiness
GetReadinessCheck
View
Yes
Amazon Route53 Recovery Readiness
UpdateReadinessCheck
Edit
Yes
Amazon Route53 Recovery Readiness
DeleteRecoveryGroup
Delete
Yes
Amazon Route53 Recovery Readiness
GetRecoveryGroup
View
Yes
Amazon Route53 Recovery Readiness
UpdateRecoveryGroup
Edit
Yes
Amazon Route53 Recovery Readiness
DeleteResourceSet
Delete
Yes
Amazon Route53 Recovery Readiness
GetResourceSet
View
Yes
Amazon Route53 Recovery Readiness
UpdateResourceSet
Edit
Yes
Amazon Route53 Recovery Readiness
GetArchitectureRecommendations
View
Yes
Amazon Route53 Recovery Readiness
GetCellReadinessSummary
View
Yes
Amazon Route53 Recovery Readiness
GetReadinessCheckResourceStatus
View
Yes
Amazon Route53 Recovery Readiness
GetReadinessCheckStatus
View
Yes
Amazon Route53 Recovery Readiness
GetRecoveryGroupReadinessSummary
View
Yes
Amazon Route53 Recovery Readiness
ListRules
View
Yes
Amazon Route53 Recovery Readiness
ListTagsForResources
View
Yes
Amazon Route53 Recovery Readiness
TagResource
Create
Yes
Amazon Route53 Recovery Readiness
UntagResource
Delete
Yes
Amazon Budgets
CreateBudget
Create
Yes
Amazon Budgets
CreateBudgetAction
Create
Yes
Amazon Budgets
CreateNotification
Create
Yes
Amazon Budgets
CreateSubscriber
Create
Yes
Amazon Budgets
DeleteBudget
Delete
Yes
Amazon Budgets
DeleteBudgetAction
Delete
Yes
Amazon Budgets
DeleteNotification
Delete
Yes
Amazon Budgets
DeleteSubscriber
Delete
Yes
Amazon Budgets
DescribeBudget
View
Yes
Amazon Budgets
DescribeBudgetAction
View
Yes
Amazon Budgets
DescribeBudgetActionHistories
View
Yes
Amazon Budgets
DescribeBudgetActionsForAccount
View
Yes
Amazon Budgets
DescribeBudgetActionsForBudget
View
Yes
Amazon Budgets
DescribeBudgetPerformanceHistory
View
Yes
Amazon Budgets
DescribeBudgets
View
Yes
Amazon Budgets
DescribeNotificationsForBudget
View
Yes
Amazon Budgets
DescribeSubscribersForNotification
View
Yes
Amazon Budgets
ExecuteBudgetAction
Create
Yes
Amazon Budgets
UpdateBudget
Edit
Yes
Amazon Budgets
UpdateBudgetAction
Edit
Yes
Amazon Budgets
UpdateNotification
Edit
Yes
Amazon Budgets
UpdateSubscriber
Edit
Yes
Amazon CodeStar
AssociateTeamMember
Create
Yes
Amazon CodeStar
CreateProject
Create
Yes
Amazon CodeStar
CreateUserProfile
Create
Yes
Amazon CodeStar
DeleteProject
Delete
Yes
Amazon CodeStar
DeleteUserProfile
Delete
Yes
Amazon CodeStar
DescribeProject
View
Yes
Amazon CodeStar
DescribeUserProfile
View
Yes
Amazon CodeStar
DisassociateTeamMember
Delete
Yes
Amazon CodeStar
ListProjects
View
Yes
Amazon CodeStar
ListResources
View
Yes
Amazon CodeStar
ListTagsForProject
View
Yes
Amazon CodeStar
ListTeamMembers
View
Yes
Amazon CodeStar
ListUserProfiles
View
Yes
Amazon CodeStar
TagProject
Create
Yes
Amazon CodeStar
UntagProject
Delete
Yes
Amazon CodeStar
UpdateProject
Edit
Yes
Amazon CodeStar
UpdateTeamMember
Edit
Yes
Amazon CodeStar
UpdateUserProfile
Edit
Yes
Amazon Polly
DeleteLexicon
Delete
Yes
Amazon Polly
GetLexicon
View
Yes
Amazon Polly
PutLexicon
Edit
Yes
Amazon Polly
DescribeVoices
View
Yes
Amazon Polly
GetSpeechSynthesisTask
View
Yes
Amazon Polly
ListLexicons
View
Yes
Amazon Polly
ListSpeechSynthesisTasks
View
Yes
Amazon Polly
StartSpeechSynthesisTask
Start
Yes
Amazon Polly
SynthesizeSpeech
Create
Yes
Amazon Application Discovery Service
AssociateConfigurationItemsToApplication
Create
Yes
Amazon Application Discovery Service
DeleteImportData
Delete
Yes
Amazon Application Discovery Service
CreateApplication
Create
Yes
Amazon Application Discovery Service
CreateTags
Create
Yes
Amazon Application Discovery Service
DeleteApplications
Delete
Yes
Amazon Application Discovery Service
DeleteTags
Delete
Yes
Amazon Application Discovery Service
DescribeAgents
View
Yes
Amazon Application Discovery Service
DescribeConfigurations
View
Yes
Amazon Application Discovery Service
DescribeContinuousExports
View
Yes
Amazon Application Discovery Service
DescribeExportConfigurations
View
Yes
Amazon Application Discovery Service
DescribeExportTasks
View
Yes
Amazon Application Discovery Service
DescribeImportTasks
View
Yes
Amazon Application Discovery Service
DescribeTags
View
Yes
Amazon Application Discovery Service
DisassociateConfigurationItemsFromApplication
Delete
Yes
Amazon Application Discovery Service
ExportConfigurations
View
Yes
Amazon Application Discovery Service
GetDiscoverySummary
View
Yes
Amazon Application Discovery Service
ListConfigurations
View
Yes
Amazon Application Discovery Service
ListServerNeighbors
View
Yes
Amazon Application Discovery Service
StartContinuousExport
Start
Yes
Amazon Application Discovery Service
StartDataCollectionByAgentIds
Start
Yes
Amazon Application Discovery Service
StartExportTask
Start
Yes
Amazon Application Discovery Service
StartImportTask
Start
Yes
Amazon Application Discovery Service
StopContinuousExport
Stop
Yes
Amazon Application Discovery Service
StopDataCollectionByAgentIds
Stop
Yes
Amazon Application Discovery Service
UpdateApplication
Edit
Yes
Amazon Timestream Write
CreateDatabase
Create
Yes
Amazon Timestream Write
CreateTable
Create
Yes
Amazon Timestream Write
DeleteDatabase
Delete
Yes
Amazon Timestream Write
DeleteTable
Delete
Yes
Amazon Timestream Write
DescribeDatabase
View
Yes
Amazon Timestream Write
DescribeEndpoints
View
Yes
Amazon Timestream Write
DescribeTable
View
Yes
Amazon Timestream Write
ListDatabases
View
Yes
Amazon Timestream Write
ListTables
View
Yes
Amazon Timestream Write
ListTagsForResource
View
Yes
Amazon Timestream Write
TagResource
Create
Yes
Amazon Timestream Write
UntagResource
Delete
Yes
Amazon Timestream Write
UpdateDatabase
Edit
Yes
Amazon Timestream Write
UpdateTable
Edit
Yes
Amazon Timestream Write
WriteRecords
Create
Yes
Amazon Elemental MediaLive
AcceptInputDeviceTransfer
Approve
Yes
Amazon Elemental MediaLive
Delete
Delete
Yes
Amazon Elemental MediaLive
Start
Start
Yes
Amazon Elemental MediaLive
Stop
Stop
Yes
Amazon Elemental MediaLive
UpdateSchedule
Edit
Yes
Amazon Elemental MediaLive
DeleteSchedule
Delete
Yes
Amazon Elemental MediaLive
DescribeSchedule
View
Yes
Amazon Elemental MediaLive
CancelInputDeviceTransfer
Delete
Yes
Amazon Elemental MediaLive
CreateChannel
Create
Yes
Amazon Elemental MediaLive
ListChannels
View
Yes
Amazon Elemental MediaLive
CreateInput
Create
Yes
Amazon Elemental MediaLive
ListInputs
View
Yes
Amazon Elemental MediaLive
CreateInputSecurityGroup
Create
Yes
Amazon Elemental MediaLive
ListInputSecurityGroups
View
Yes
Amazon Elemental MediaLive
CreateMultiplex
Create
Yes
Amazon Elemental MediaLive
ListMultiplexes
View
Yes
Amazon Elemental MediaLive
CreateMultiplexProgram
Create
Yes
Amazon Elemental MediaLive
ListMultiplexPrograms
View
Yes
Amazon Elemental MediaLive
CreatePartnerInput
Create
Yes
Amazon Elemental MediaLive
CreateTags
Create
Yes
Amazon Elemental MediaLive
ListTagsForResource
View
Yes
Amazon Elemental MediaLive
DeleteChannel
Delete
Yes
Amazon Elemental MediaLive
DescribeChannel
View
Yes
Amazon Elemental MediaLive
UpdateChannel
Edit
Yes
Amazon Elemental MediaLive
DeleteInput
Delete
Yes
Amazon Elemental MediaLive
DescribeInput
View
Yes
Amazon Elemental MediaLive
UpdateInput
Edit
Yes
Amazon Elemental MediaLive
DeleteInputSecurityGroup
Delete
Yes
Amazon Elemental MediaLive
DescribeInputSecurityGroup
View
Yes
Amazon Elemental MediaLive
UpdateInputSecurityGroup
Edit
Yes
Amazon Elemental MediaLive
DeleteMultiplex
Delete
Yes
Amazon Elemental MediaLive
DescribeMultiplex
View
Yes
Amazon Elemental MediaLive
UpdateMultiplex
Edit
Yes
Amazon Elemental MediaLive
DeleteMultiplexProgram
Delete
Yes
Amazon Elemental MediaLive
DescribeMultiplexProgram
View
Yes
Amazon Elemental MediaLive
UpdateMultiplexProgram
Edit
Yes
Amazon Elemental MediaLive
DeleteReservation
Delete
Yes
Amazon Elemental MediaLive
DescribeReservation
View
Yes
Amazon Elemental MediaLive
UpdateReservation
Edit
Yes
Amazon Elemental MediaLive
DeleteTags
Delete
Yes
Amazon Elemental MediaLive
DescribeInputDevice
View
Yes
Amazon Elemental MediaLive
UpdateInputDevice
Edit
Yes
Amazon Elemental MediaLive
DescribeInputDeviceThumbnail
View
Yes
Amazon Elemental MediaLive
DescribeOffering
View
Yes
Amazon Elemental MediaLive
ListInputDeviceTransfers
View
Yes
Amazon Elemental MediaLive
ListInputDevices
View
Yes
Amazon Elemental MediaLive
ListOfferings
View
Yes
Amazon Elemental MediaLive
ListReservations
View
Yes
Amazon Elemental MediaLive
PurchaseOffering
Purchase
Yes
Amazon Elemental MediaLive
RejectInputDeviceTransfer
Reject
Yes
Amazon Elemental MediaLive
StartChannel
Start
Yes
Amazon Elemental MediaLive
StartMultiplex
Start
Yes
Amazon Elemental MediaLive
StopChannel
Stop
Yes
Amazon Elemental MediaLive
StopMultiplex
Stop
Yes
Amazon Elemental MediaLive
TransferInputDevice
Create
Yes
Amazon Elemental MediaLive
UpdateChannelClass
Edit
Yes
Amazon Macie 2
AcceptInvitation
Approve
Yes
Amazon Macie 2
GetCustomDataIdentifiers
View
Yes
Amazon Macie 2
CreateClassificationJob
Create
Yes
Amazon Macie 2
CreateCustomDataIdentifier
Create
Yes
Amazon Macie 2
CreateFindingsFilter
Create
Yes
Amazon Macie 2
ListFindingsFilters
View
Yes
Amazon Macie 2
CreateInvitations
Create
Yes
Amazon Macie 2
ListInvitations
View
Yes
Amazon Macie 2
CreateMember
Create
Yes
Amazon Macie 2
ListMembers
View
Yes
Amazon Macie 2
CreateSampleFindings
Create
Yes
Amazon Macie 2
DeclineInvitations
Create
Yes
Amazon Macie 2
DeleteCustomDataIdentifier
Delete
Yes
Amazon Macie 2
GetCustomDataIdentifier
View
Yes
Amazon Macie 2
DeleteFindingsFilter
Delete
Yes
Amazon Macie 2
GetFindingsFilter
View
Yes
Amazon Macie 2
UpdateFindingsFilter
Edit
Yes
Amazon Macie 2
DeleteInvitations
Delete
Yes
Amazon Macie 2
DeleteMember
Delete
Yes
Amazon Macie 2
GetMember
View
Yes
Amazon Macie 2
DescribeBuckets
View
Yes
Amazon Macie 2
DescribeClassificationJob
View
Yes
Amazon Macie 2
UpdateClassificationJob
Edit
Yes
Amazon Macie 2
DescribeOrganizationConfiguration
View
Yes
Amazon Macie 2
UpdateOrganizationConfiguration
Edit
Yes
Amazon Macie 2
DisableMacie
Delete
Yes
Amazon Macie 2
EnableMacie
Enable
Yes
Amazon Macie 2
GetMacieSession
View
Yes
Amazon Macie 2
UpdateMacieSession
Edit
Yes
Amazon Macie 2
DisableOrganizationAdminAccount
Delete
Yes
Amazon Macie 2
DisassociateFromAdministratorAccount
Delete
Yes
Amazon Macie 2
DisassociateFromMasterAccount
Delete
Yes
Amazon Macie 2
DisassociateMember
Delete
Yes
Amazon Macie 2
EnableOrganizationAdminAccount
Enable
Yes
Amazon Macie 2
ListOrganizationAdminAccounts
View
Yes
Amazon Macie 2
GetAdministratorAccount
View
Yes
Amazon Macie 2
GetBucketStatistics
View
Yes
Amazon Macie 2
GetClassificationExportConfiguration
View
Yes
Amazon Macie 2
PutClassificationExportConfiguration
Edit
Yes
Amazon Macie 2
GetFindingStatistics
View
Yes
Amazon Macie 2
GetFindings
View
Yes
Amazon Macie 2
GetFindingsPublicationConfiguration
View
Yes
Amazon Macie 2
PutFindingsPublicationConfiguration
Edit
Yes
Amazon Macie 2
GetInvitationsCount
View
Yes
Amazon Macie 2
GetMasterAccount
View
Yes
Amazon Macie 2
GetUsageStatistics
View
Yes
Amazon Macie 2
GetUsageTotals
View
Yes
Amazon Macie 2
ListClassificationJobs
View
Yes
Amazon Macie 2
ListCustomDataIdentifiers
View
Yes
Amazon Macie 2
ListFindings
View
Yes
Amazon Macie 2
ListManagedDataIdentifiers
View
Yes
Amazon Macie 2
ListTagsForResource
View
Yes
Amazon Macie 2
TagResource
Create
Yes
Amazon Macie 2
SearchResources
Search
Yes
Amazon Macie 2
TestCustomDataIdentifier
Create
Yes
Amazon Macie 2
UntagResource
Delete
Yes
Amazon Macie 2
UpdateMemberSession
Edit
Yes
Amazon CodeStar connections
CreateConnection
Create
Yes
Amazon CodeStar connections
CreateHost
Create
Yes
Amazon CodeStar connections
DeleteConnection
Delete
Yes
Amazon CodeStar connections
DeleteHost
Delete
Yes
Amazon CodeStar connections
GetConnection
View
Yes
Amazon CodeStar connections
GetHost
View
Yes
Amazon CodeStar connections
ListConnections
View
Yes
Amazon CodeStar connections
ListHosts
View
Yes
Amazon CodeStar connections
ListTagsForResource
View
Yes
Amazon CodeStar connections
TagResource
Create
Yes
Amazon CodeStar connections
UntagResource
Delete
Yes
Amazon CodeStar connections
UpdateHost
Edit
Yes
Amazon Location Service
AssociateTrackerConsumer
Create
Yes
Amazon Location Service
DeleteDevicePositionHistory
Delete
Yes
Amazon Location Service
DeleteGeofence
Delete
Yes
Amazon Location Service
EvaluateGeofences
Create
Yes
Amazon Location Service
GetDevicePosition
View
Yes
Amazon Location Service
PutGeofence
Edit
Yes
Amazon Location Service
UpdateDevicePosition
Edit
Yes
Amazon Location Service
CalculateRoute
Create
Yes
Amazon Location Service
CreateGeofenceCollection
Create
Yes
Amazon Location Service
CreateMap
Create
Yes
Amazon Location Service
CreatePlaceIndex
Create
Yes
Amazon Location Service
CreateRouteCalculator
Create
Yes
Amazon Location Service
CreateTracker
Create
Yes
Amazon Location Service
DeleteGeofenceCollection
Delete
Yes
Amazon Location Service
DescribeGeofenceCollection
View
Yes
Amazon Location Service
UpdateGeofenceCollection
Edit
Yes
Amazon Location Service
DeleteMap
Delete
Yes
Amazon Location Service
DescribeMap
View
Yes
Amazon Location Service
UpdateMap
Edit
Yes
Amazon Location Service
DeletePlaceIndex
Delete
Yes
Amazon Location Service
DescribePlaceIndex
View
Yes
Amazon Location Service
UpdatePlaceIndex
Edit
Yes
Amazon Location Service
DeleteRouteCalculator
Delete
Yes
Amazon Location Service
DescribeRouteCalculator
View
Yes
Amazon Location Service
UpdateRouteCalculator
Edit
Yes
Amazon Location Service
DeleteTracker
Delete
Yes
Amazon Location Service
DescribeTracker
View
Yes
Amazon Location Service
UpdateTracker
Edit
Yes
Amazon Location Service
DisassociateTrackerConsumer
Delete
Yes
Amazon Location Service
GetDevicePositionHistory
View
Yes
Amazon Location Service
GetGeofence
View
Yes
Amazon Location Service
GetMapGlyphs
View
Yes
Amazon Location Service
GetMapSprites
View
Yes
Amazon Location Service
GetMapStyleDescriptor
View
Yes
Amazon Location Service
GetMapTile
View
Yes
Amazon Location Service
ListDevicePositions
View
Yes
Amazon Location Service
ListGeofenceCollections
View
Yes
Amazon Location Service
ListGeofences
View
Yes
Amazon Location Service
ListMaps
View
Yes
Amazon Location Service
ListPlaceIndexes
View
Yes
Amazon Location Service
ListRouteCalculators
View
Yes
Amazon Location Service
ListTagsForResource
View
Yes
Amazon Location Service
TagResource
Create
Yes
Amazon Location Service
ListTrackerConsumers
View
Yes
Amazon Location Service
ListTrackers
View
Yes
Amazon Location Service
SearchPlaceIndexForPosition
Search
Yes
Amazon Location Service
SearchPlaceIndexForText
Search
Yes
Amazon Location Service
UntagResource
Delete
Yes
Amazon CodePipeline
AcknowledgeJob
Create
Yes
Amazon CodePipeline
AcknowledgeThirdPartyJob
Create
Yes
Amazon CodePipeline
CreateCustomActionType
Create
Yes
Amazon CodePipeline
CreatePipeline
Create
Yes
Amazon CodePipeline
DeleteCustomActionType
Delete
Yes
Amazon CodePipeline
DeletePipeline
Delete
Yes
Amazon CodePipeline
DeleteWebhook
Delete
Yes
Amazon CodePipeline
DeregisterWebhookWithThirdParty
Deregister
Yes
Amazon CodePipeline
DisableStageTransition
Edit
Yes
Amazon CodePipeline
EnableStageTransition
Enable
Yes
Amazon CodePipeline
GetActionType
View
Yes
Amazon CodePipeline
GetJobDetails
View
Yes
Amazon CodePipeline
GetPipeline
View
Yes
Amazon CodePipeline
GetPipelineExecution
View
Yes
Amazon CodePipeline
GetPipelineState
View
Yes
Amazon CodePipeline
GetThirdPartyJobDetails
View
Yes
Amazon CodePipeline
ListActionExecutions
View
Yes
Amazon CodePipeline
ListActionTypes
View
Yes
Amazon CodePipeline
ListPipelineExecutions
View
Yes
Amazon CodePipeline
ListPipelines
View
Yes
Amazon CodePipeline
ListTagsForResource
View
Yes
Amazon CodePipeline
ListWebhooks
View
Yes
Amazon CodePipeline
PollForJobs
Create
Yes
Amazon CodePipeline
PollForThirdPartyJobs
Create
Yes
Amazon CodePipeline
PutActionRevision
Edit
Yes
Amazon CodePipeline
PutApprovalResult
Edit
Yes
Amazon CodePipeline
PutJobFailureResult
Edit
Yes
Amazon CodePipeline
PutJobSuccessResult
Edit
Yes
Amazon CodePipeline
PutThirdPartyJobFailureResult
Edit
Yes
Amazon CodePipeline
PutThirdPartyJobSuccessResult
Edit
Yes
Amazon CodePipeline
PutWebhook
Edit
Yes
Amazon CodePipeline
RegisterWebhookWithThirdParty
Register
Yes
Amazon CodePipeline
RetryStageExecution
Create
Yes
Amazon CodePipeline
StartPipelineExecution
Start
Yes
Amazon CodePipeline
StopPipelineExecution
Stop
Yes
Amazon CodePipeline
TagResource
Create
Yes
Amazon CodePipeline
UntagResource
Delete
Yes
Amazon CodePipeline
UpdateActionType
Edit
Yes
Amazon CodePipeline
UpdatePipeline
Edit
Yes
Amazon Lex Runtime V2
DeleteSession
Delete
Yes
Amazon Lex Runtime V2
GetSession
View
Yes
Amazon Lex Runtime V2
PutSession
Edit
Yes
Amazon Lex Runtime V2
RecognizeText
Create
Yes
Amazon Lex Runtime V2
RecognizeUtterance
Create
Yes
Amazon Connect Participant Service
CompleteAttachmentUpload
Create
Yes
Amazon Connect Participant Service
CreateParticipantConnection
Create
Yes
Amazon Connect Participant Service
DisconnectParticipant
Create
Yes
Amazon Connect Participant Service
GetAttachment
View
Yes
Amazon Connect Participant Service
GetTranscript
View
Yes
Amazon Connect Participant Service
SendEvent
Send
Yes
Amazon Connect Participant Service
SendMessage
Send
Yes
Amazon Connect Participant Service
StartAttachmentUpload
Start
Yes
Amazon Marketplace Commerce Analytics
GenerateDataSet
Create
Yes
Amazon Marketplace Commerce Analytics
StartSupportDataExport
Start
Yes
Amazon IoT Greengrass V2
AssociateClientDeviceWithCoreDevice
Create
Yes
Amazon IoT Greengrass V2
DisassociateClientDeviceFromCoreDevice
Delete
Yes
Amazon IoT Greengrass V2
CancelDeployment
Delete
Yes
Amazon IoT Greengrass V2
CreateComponentVersion
Create
Yes
Amazon IoT Greengrass V2
CreateDeployment
Create
Yes
Amazon IoT Greengrass V2
ListDeployments
View
Yes
Amazon IoT Greengrass V2
DeleteComponent
Delete
Yes
Amazon IoT Greengrass V2
GetComponent
View
Yes
Amazon IoT Greengrass V2
DeleteCoreDevice
Delete
Yes
Amazon IoT Greengrass V2
GetCoreDevice
View
Yes
Amazon IoT Greengrass V2
DescribeComponent
View
Yes
Amazon IoT Greengrass V2
GetComponentVersionArtifact
View
Yes
Amazon IoT Greengrass V2
GetDeployment
View
Yes
Amazon IoT Greengrass V2
ListClientDevicesAssociatedWithCoreDevice
View
Yes
Amazon IoT Greengrass V2
ListComponentVersions
View
Yes
Amazon IoT Greengrass V2
ListComponents
View
Yes
Amazon IoT Greengrass V2
ListCoreDevices
View
Yes
Amazon IoT Greengrass V2
ListEffectiveDeployments
View
Yes
Amazon IoT Greengrass V2
ListInstalledComponents
View
Yes
Amazon IoT Greengrass V2
ListTagsForResource
View
Yes
Amazon IoT Greengrass V2
TagResource
Create
Yes
Amazon IoT Greengrass V2
ResolveComponentCandidates
Create
Yes
Amazon IoT Greengrass V2
UntagResource
Delete
Yes
Amazon Proton
AcceptEnvironmentAccountConnection
Approve
Yes
Amazon Proton
CancelEnvironmentDeployment
Delete
Yes
Amazon Proton
CancelServiceInstanceDeployment
Delete
Yes
Amazon Proton
CancelServicePipelineDeployment
Delete
Yes
Amazon Proton
CreateEnvironment
Create
Yes
Amazon Proton
CreateEnvironmentAccountConnection
Create
Yes
Amazon Proton
CreateEnvironmentTemplate
Create
Yes
Amazon Proton
CreateEnvironmentTemplateVersion
Create
Yes
Amazon Proton
CreateService
Create
Yes
Amazon Proton
CreateServiceTemplate
Create
Yes
Amazon Proton
CreateServiceTemplateVersion
Create
Yes
Amazon Proton
DeleteEnvironment
Delete
Yes
Amazon Proton
DeleteEnvironmentAccountConnection
Delete
Yes
Amazon Proton
DeleteEnvironmentTemplate
Delete
Yes
Amazon Proton
DeleteEnvironmentTemplateVersion
Delete
Yes
Amazon Proton
DeleteService
Delete
Yes
Amazon Proton
DeleteServiceTemplate
Delete
Yes
Amazon Proton
DeleteServiceTemplateVersion
Delete
Yes
Amazon Proton
GetAccountSettings
View
Yes
Amazon Proton
GetEnvironment
View
Yes
Amazon Proton
GetEnvironmentAccountConnection
View
Yes
Amazon Proton
GetEnvironmentTemplate
View
Yes
Amazon Proton
GetEnvironmentTemplateVersion
View
Yes
Amazon Proton
GetService
View
Yes
Amazon Proton
GetServiceInstance
View
Yes
Amazon Proton
GetServiceTemplate
View
Yes
Amazon Proton
GetServiceTemplateVersion
View
Yes
Amazon Proton
ListEnvironmentAccountConnections
View
Yes
Amazon Proton
ListEnvironmentTemplateVersions
View
Yes
Amazon Proton
ListEnvironmentTemplates
View
Yes
Amazon Proton
ListEnvironments
View
Yes
Amazon Proton
ListServiceInstances
View
Yes
Amazon Proton
ListServiceTemplateVersions
View
Yes
Amazon Proton
ListServiceTemplates
View
Yes
Amazon Proton
ListServices
View
Yes
Amazon Proton
ListTagsForResource
View
Yes
Amazon Proton
RejectEnvironmentAccountConnection
Reject
Yes
Amazon Proton
TagResource
Create
Yes
Amazon Proton
UntagResource
Delete
Yes
Amazon Proton
UpdateAccountSettings
Edit
Yes
Amazon Proton
UpdateEnvironment
Edit
Yes
Amazon Proton
UpdateEnvironmentAccountConnection
Edit
Yes
Amazon Proton
UpdateEnvironmentTemplate
Edit
Yes
Amazon Proton
UpdateEnvironmentTemplateVersion
Edit
Yes
Amazon Proton
UpdateService
Edit
Yes
Amazon Proton
UpdateServiceInstance
Edit
Yes
Amazon Proton
UpdateServicePipeline
Edit
Yes
Amazon Proton
UpdateServiceTemplate
Edit
Yes
Amazon Proton
UpdateServiceTemplateVersion
Edit
Yes
Amazon Cloud Map
CreateHttpNamespace
Create
Yes
Amazon Cloud Map
CreatePrivateDnsNamespace
Create
Yes
Amazon Cloud Map
CreatePublicDnsNamespace
Create
Yes
Amazon Cloud Map
CreateService
Create
Yes
Amazon Cloud Map
DeleteNamespace
Delete
Yes
Amazon Cloud Map
DeleteService
Delete
Yes
Amazon Cloud Map
DeregisterInstance
Deregister
Yes
Amazon Cloud Map
DiscoverInstances
Create
Yes
Amazon Cloud Map
GetInstance
View
Yes
Amazon Cloud Map
GetInstancesHealthStatus
View
Yes
Amazon Cloud Map
GetNamespace
View
Yes
Amazon Cloud Map
GetOperation
View
Yes
Amazon Cloud Map
GetService
View
Yes
Amazon Cloud Map
ListInstances
View
Yes
Amazon Cloud Map
ListNamespaces
View
Yes
Amazon Cloud Map
ListOperations
View
Yes
Amazon Cloud Map
ListServices
View
Yes
Amazon Cloud Map
ListTagsForResource
View
Yes
Amazon Cloud Map
RegisterInstance
Register
Yes
Amazon Cloud Map
TagResource
Create
Yes
Amazon Cloud Map
UntagResource
Delete
Yes
Amazon Cloud Map
UpdateHttpNamespace
Edit
Yes
Amazon Cloud Map
UpdateInstanceCustomHealthStatus
Edit
Yes
Amazon Cloud Map
UpdatePrivateDnsNamespace
Edit
Yes
Amazon Cloud Map
UpdatePublicDnsNamespace
Edit
Yes
Amazon Cloud Map
UpdateService
Edit
Yes
Amazon Elastic Inference
DescribeAcceleratorOfferings
View
Yes
Amazon Elastic Inference
DescribeAcceleratorTypes
View
Yes
Amazon Elastic Inference
DescribeAccelerators
View
Yes
Amazon Elastic Inference
ListTagsForResource
View
Yes
Amazon Elastic Inference
TagResource
Create
Yes
Amazon Elastic Inference
UntagResource
Delete
Yes
Amazon Greengrass
AssociateRoleToGroup
Create
Yes
Amazon Greengrass
DisassociateRoleFromGroup
Delete
Yes
Amazon Greengrass
GetAssociatedRole
View
Yes
Amazon Greengrass
AssociateServiceRoleToAccount
Create
Yes
Amazon Greengrass
DisassociateServiceRoleFromAccount
Delete
Yes
Amazon Greengrass
GetServiceRoleForAccount
View
Yes
Amazon Greengrass
CreateConnectorDefinition
Create
Yes
Amazon Greengrass
ListConnectorDefinitions
View
Yes
Amazon Greengrass
CreateConnectorDefinitionVersion
Create
Yes
Amazon Greengrass
ListConnectorDefinitionVersions
View
Yes
Amazon Greengrass
CreateCoreDefinition
Create
Yes
Amazon Greengrass
ListCoreDefinitions
View
Yes
Amazon Greengrass
CreateCoreDefinitionVersion
Create
Yes
Amazon Greengrass
ListCoreDefinitionVersions
View
Yes
Amazon Greengrass
CreateDeployment
Create
Yes
Amazon Greengrass
ListDeployments
View
Yes
Amazon Greengrass
CreateDeviceDefinition
Create
Yes
Amazon Greengrass
ListDeviceDefinitions
View
Yes
Amazon Greengrass
CreateDeviceDefinitionVersion
Create
Yes
Amazon Greengrass
ListDeviceDefinitionVersions
View
Yes
Amazon Greengrass
CreateFunctionDefinition
Create
Yes
Amazon Greengrass
ListFunctionDefinitions
View
Yes
Amazon Greengrass
CreateFunctionDefinitionVersion
Create
Yes
Amazon Greengrass
ListFunctionDefinitionVersions
View
Yes
Amazon Greengrass
CreateGroup
Create
Yes
Amazon Greengrass
ListGroups
View
Yes
Amazon Greengrass
CreateGroupCertificateAuthority
Create
Yes
Amazon Greengrass
ListGroupCertificateAuthorities
View
Yes
Amazon Greengrass
CreateGroupVersion
Create
Yes
Amazon Greengrass
ListGroupVersions
View
Yes
Amazon Greengrass
CreateLoggerDefinition
Create
Yes
Amazon Greengrass
ListLoggerDefinitions
View
Yes
Amazon Greengrass
CreateLoggerDefinitionVersion
Create
Yes
Amazon Greengrass
ListLoggerDefinitionVersions
View
Yes
Amazon Greengrass
CreateResourceDefinition
Create
Yes
Amazon Greengrass
ListResourceDefinitions
View
Yes
Amazon Greengrass
CreateResourceDefinitionVersion
Create
Yes
Amazon Greengrass
ListResourceDefinitionVersions
View
Yes
Amazon Greengrass
CreateSoftwareUpdateJob
Create
Yes
Amazon Greengrass
CreateSubscriptionDefinition
Create
Yes
Amazon Greengrass
ListSubscriptionDefinitions
View
Yes
Amazon Greengrass
CreateSubscriptionDefinitionVersion
Create
Yes
Amazon Greengrass
ListSubscriptionDefinitionVersions
View
Yes
Amazon Greengrass
DeleteConnectorDefinition
Delete
Yes
Amazon Greengrass
GetConnectorDefinition
View
Yes
Amazon Greengrass
UpdateConnectorDefinition
Edit
Yes
Amazon Greengrass
DeleteCoreDefinition
Delete
Yes
Amazon Greengrass
GetCoreDefinition
View
Yes
Amazon Greengrass
UpdateCoreDefinition
Edit
Yes
Amazon Greengrass
DeleteDeviceDefinition
Delete
Yes
Amazon Greengrass
GetDeviceDefinition
View
Yes
Amazon Greengrass
UpdateDeviceDefinition
Edit
Yes
Amazon Greengrass
DeleteFunctionDefinition
Delete
Yes
Amazon Greengrass
GetFunctionDefinition
View
Yes
Amazon Greengrass
UpdateFunctionDefinition
Edit
Yes
Amazon Greengrass
DeleteGroup
Delete
Yes
Amazon Greengrass
GetGroup
View
Yes
Amazon Greengrass
UpdateGroup
Edit
Yes
Amazon Greengrass
DeleteLoggerDefinition
Delete
Yes
Amazon Greengrass
GetLoggerDefinition
View
Yes
Amazon Greengrass
UpdateLoggerDefinition
Edit
Yes
Amazon Greengrass
DeleteResourceDefinition
Delete
Yes
Amazon Greengrass
GetResourceDefinition
View
Yes
Amazon Greengrass
UpdateResourceDefinition
Edit
Yes
Amazon Greengrass
DeleteSubscriptionDefinition
Delete
Yes
Amazon Greengrass
GetSubscriptionDefinition
View
Yes
Amazon Greengrass
UpdateSubscriptionDefinition
Edit
Yes
Amazon Greengrass
GetBulkDeploymentStatus
View
Yes
Amazon Greengrass
GetConnectivityInfo
View
Yes
Amazon Greengrass
UpdateConnectivityInfo
Edit
Yes
Amazon Greengrass
GetConnectorDefinitionVersion
View
Yes
Amazon Greengrass
GetCoreDefinitionVersion
View
Yes
Amazon Greengrass
GetDeploymentStatus
View
Yes
Amazon Greengrass
GetDeviceDefinitionVersion
View
Yes
Amazon Greengrass
GetFunctionDefinitionVersion
View
Yes
Amazon Greengrass
GetGroupCertificateAuthority
View
Yes
Amazon Greengrass
GetGroupCertificateConfiguration
View
Yes
Amazon Greengrass
UpdateGroupCertificateConfiguration
Edit
Yes
Amazon Greengrass
GetGroupVersion
View
Yes
Amazon Greengrass
GetLoggerDefinitionVersion
View
Yes
Amazon Greengrass
GetResourceDefinitionVersion
View
Yes
Amazon Greengrass
GetSubscriptionDefinitionVersion
View
Yes
Amazon Greengrass
GetThingRuntimeConfiguration
View
Yes
Amazon Greengrass
UpdateThingRuntimeConfiguration
Edit
Yes
Amazon Greengrass
ListBulkDeploymentDetailedReports
View
Yes
Amazon Greengrass
ListBulkDeployments
View
Yes
Amazon Greengrass
StartBulkDeployment
Start
Yes
Amazon Greengrass
ListTagsForResource
View
Yes
Amazon Greengrass
TagResource
Create
Yes
Amazon Greengrass
ResetDeployments
Edit
Yes
Amazon Greengrass
StopBulkDeployment
Stop
Yes
Amazon Greengrass
UntagResource
Delete
Yes
Amazon Simple Email Service V2
CreateConfigurationSet
Create
Yes
Amazon Simple Email Service V2
ListConfigurationSets
View
Yes
Amazon Simple Email Service V2
CreateConfigurationSetEventDestination
Create
Yes
Amazon Simple Email Service V2
GetConfigurationSetEventDestinations
View
Yes
Amazon Simple Email Service V2
CreateContact
Create
Yes
Amazon Simple Email Service V2
ListContacts
View
Yes
Amazon Simple Email Service V2
CreateContactList
Create
Yes
Amazon Simple Email Service V2
ListContactLists
View
Yes
Amazon Simple Email Service V2
CreateCustomVerificationEmailTemplate
Create
Yes
Amazon Simple Email Service V2
ListCustomVerificationEmailTemplates
View
Yes
Amazon Simple Email Service V2
CreateDedicatedIpPool
Create
Yes
Amazon Simple Email Service V2
ListDedicatedIpPools
View
Yes
Amazon Simple Email Service V2
CreateDeliverabilityTestReport
Create
Yes
Amazon Simple Email Service V2
CreateEmailIdentity
Create
Yes
Amazon Simple Email Service V2
ListEmailIdentities
View
Yes
Amazon Simple Email Service V2
CreateEmailIdentityPolicy
Create
Yes
Amazon Simple Email Service V2
DeleteEmailIdentityPolicy
Delete
Yes
Amazon Simple Email Service V2
UpdateEmailIdentityPolicy
Edit
Yes
Amazon Simple Email Service V2
CreateEmailTemplate
Create
Yes
Amazon Simple Email Service V2
ListEmailTemplates
View
Yes
Amazon Simple Email Service V2
CreateImportJob
Create
Yes
Amazon Simple Email Service V2
ListImportJobs
View
Yes
Amazon Simple Email Service V2
DeleteConfigurationSet
Delete
Yes
Amazon Simple Email Service V2
GetConfigurationSet
View
Yes
Amazon Simple Email Service V2
DeleteConfigurationSetEventDestination
Delete
Yes
Amazon Simple Email Service V2
UpdateConfigurationSetEventDestination
Edit
Yes
Amazon Simple Email Service V2
DeleteContact
Delete
Yes
Amazon Simple Email Service V2
GetContact
View
Yes
Amazon Simple Email Service V2
UpdateContact
Edit
Yes
Amazon Simple Email Service V2
DeleteContactList
Delete
Yes
Amazon Simple Email Service V2
GetContactList
View
Yes
Amazon Simple Email Service V2
UpdateContactList
Edit
Yes
Amazon Simple Email Service V2
DeleteCustomVerificationEmailTemplate
Delete
Yes
Amazon Simple Email Service V2
GetCustomVerificationEmailTemplate
View
Yes
Amazon Simple Email Service V2
UpdateCustomVerificationEmailTemplate
Edit
Yes
Amazon Simple Email Service V2
DeleteDedicatedIpPool
Delete
Yes
Amazon Simple Email Service V2
DeleteEmailIdentity
Delete
Yes
Amazon Simple Email Service V2
GetEmailIdentity
View
Yes
Amazon Simple Email Service V2
DeleteEmailTemplate
Delete
Yes
Amazon Simple Email Service V2
GetEmailTemplate
View
Yes
Amazon Simple Email Service V2
UpdateEmailTemplate
Edit
Yes
Amazon Simple Email Service V2
DeleteSuppressedDestination
Delete
Yes
Amazon Simple Email Service V2
GetSuppressedDestination
View
Yes
Amazon Simple Email Service V2
GetAccount
View
Yes
Amazon Simple Email Service V2
GetBlacklistReports
View
Yes
Amazon Simple Email Service V2
GetDedicatedIp
View
Yes
Amazon Simple Email Service V2
GetDedicatedIps
View
Yes
Amazon Simple Email Service V2
GetDeliverabilityDashboardOptions
View
Yes
Amazon Simple Email Service V2
PutDeliverabilityDashboardOption
Edit
Yes
Amazon Simple Email Service V2
GetDeliverabilityTestReport
View
Yes
Amazon Simple Email Service V2
GetDomainDeliverabilityCampaign
View
Yes
Amazon Simple Email Service V2
GetDomainStatisticsReport
View
Yes
Amazon Simple Email Service V2
GetEmailIdentityPolicies
View
Yes
Amazon Simple Email Service V2
GetImportJob
View
Yes
Amazon Simple Email Service V2
ListDeliverabilityTestReports
View
Yes
Amazon Simple Email Service V2
ListDomainDeliverabilityCampaigns
View
Yes
Amazon Simple Email Service V2
ListSuppressedDestinations
View
Yes
Amazon Simple Email Service V2
PutSuppressedDestination
Edit
Yes
Amazon Simple Email Service V2
ListTagsForResource
View
Yes
Amazon Simple Email Service V2
PutAccountDedicatedIpWarmupAttributes
Edit
Yes
Amazon Simple Email Service V2
PutAccountDetails
Edit
Yes
Amazon Simple Email Service V2
PutAccountSendingAttributes
Edit
Yes
Amazon Simple Email Service V2
PutAccountSuppressionAttributes
Edit
Yes
Amazon Simple Email Service V2
PutConfigurationSetDeliveryOptions
Edit
Yes
Amazon Simple Email Service V2
PutConfigurationSetReputationOptions
Edit
Yes
Amazon Simple Email Service V2
PutConfigurationSetSendingOptions
Edit
Yes
Amazon Simple Email Service V2
PutConfigurationSetSuppressionOptions
Edit
Yes
Amazon Simple Email Service V2
PutConfigurationSetTrackingOptions
Edit
Yes
Amazon Simple Email Service V2
PutDedicatedIpInPool
Edit
Yes
Amazon Simple Email Service V2
PutDedicatedIpWarmupAttributes
Edit
Yes
Amazon Simple Email Service V2
PutEmailIdentityConfigurationSetAttributes
Edit
Yes
Amazon Simple Email Service V2
PutEmailIdentityDkimAttributes
Edit
Yes
Amazon Simple Email Service V2
PutEmailIdentityDkimSigningAttributes
Edit
Yes
Amazon Simple Email Service V2
PutEmailIdentityFeedbackAttributes
Edit
Yes
Amazon Simple Email Service V2
PutEmailIdentityMailFromAttributes
Edit
Yes
Amazon Simple Email Service V2
SendBulkEmail
Send
Yes
Amazon Simple Email Service V2
SendCustomVerificationEmail
Send
Yes
Amazon Simple Email Service V2
SendEmail
Send
Yes
Amazon Simple Email Service V2
TagResource
Create
Yes
Amazon Simple Email Service V2
TestRenderEmailTemplate
Create
Yes
Amazon Simple Email Service V2
UntagResource
Delete
Yes
Amazon Connect Customer Profiles
AddProfileKey
Create
Yes
Amazon Connect Customer Profiles
CreateDomain
Create
Yes
Amazon Connect Customer Profiles
DeleteDomain
Delete
Yes
Amazon Connect Customer Profiles
GetDomain
View
Yes
Amazon Connect Customer Profiles
UpdateDomain
Edit
Yes
Amazon Connect Customer Profiles
CreateProfile
Create
Yes
Amazon Connect Customer Profiles
UpdateProfile
Edit
Yes
Amazon Connect Customer Profiles
DeleteIntegration
Delete
Yes
Amazon Connect Customer Profiles
DeleteProfile
Delete
Yes
Amazon Connect Customer Profiles
DeleteProfileKey
Delete
Yes
Amazon Connect Customer Profiles
DeleteProfileObject
Delete
Yes
Amazon Connect Customer Profiles
DeleteProfileObjectType
Delete
Yes
Amazon Connect Customer Profiles
GetProfileObjectType
View
Yes
Amazon Connect Customer Profiles
PutProfileObjectType
Edit
Yes
Amazon Connect Customer Profiles
GetIntegration
View
Yes
Amazon Connect Customer Profiles
ListIntegrations
View
Yes
Amazon Connect Customer Profiles
PutIntegration
Edit
Yes
Amazon Connect Customer Profiles
GetMatches
View
Yes
Amazon Connect Customer Profiles
GetProfileObjectTypeTemplate
View
Yes
Amazon Connect Customer Profiles
ListAccountIntegrations
View
Yes
Amazon Connect Customer Profiles
ListDomains
View
Yes
Amazon Connect Customer Profiles
ListProfileObjectTypeTemplates
View
Yes
Amazon Connect Customer Profiles
ListProfileObjectTypes
View
Yes
Amazon Connect Customer Profiles
ListProfileObjects
View
Yes
Amazon Connect Customer Profiles
PutProfileObject
Edit
Yes
Amazon Connect Customer Profiles
ListTagsForResource
View
Yes
Amazon Connect Customer Profiles
TagResource
Create
Yes
Amazon Connect Customer Profiles
MergeProfiles
Create
Yes
Amazon Connect Customer Profiles
SearchProfiles
Search
Yes
Amazon Connect Customer Profiles
UntagResource
Delete
Yes
Amazon OpsWorks CM
AssociateNode
Create
Yes
Amazon OpsWorks CM
CreateBackup
Create
Yes
Amazon OpsWorks CM
CreateServer
Create
Yes
Amazon OpsWorks CM
DeleteBackup
Delete
Yes
Amazon OpsWorks CM
DeleteServer
Delete
Yes
Amazon OpsWorks CM
DescribeAccountAttributes
View
Yes
Amazon OpsWorks CM
DescribeBackups
View
Yes
Amazon OpsWorks CM
DescribeEvents
View
Yes
Amazon OpsWorks CM
DescribeNodeAssociationStatus
View
Yes
Amazon OpsWorks CM
DescribeServers
View
Yes
Amazon OpsWorks CM
DisassociateNode
Delete
Yes
Amazon OpsWorks CM
ExportServerEngineAttribute
View
Yes
Amazon OpsWorks CM
ListTagsForResource
View
Yes
Amazon OpsWorks CM
RestoreServer
Create
Yes
Amazon OpsWorks CM
StartMaintenance
Start
Yes
Amazon OpsWorks CM
TagResource
Create
Yes
Amazon OpsWorks CM
UntagResource
Delete
Yes
Amazon OpsWorks CM
UpdateServer
Edit
Yes
Amazon OpsWorks CM
UpdateServerEngineAttributes
Edit
Yes
Amazon SimpleDB
DeleteAttributes
Delete
Yes
Amazon SimpleDB
PutAttributes
Edit
Yes
Amazon SimpleDB
CreateDomain
Create
Yes
Amazon SimpleDB
DeleteDomain
Delete
Yes
Amazon SimpleDB
DomainMetadata
View
Yes
Amazon SimpleDB
DomainMetadata
Create
Yes
Amazon SimpleDB
GetAttributes
View
Yes
Amazon SimpleDB
ListDomains
View
Yes
Amazon SimpleDB
Select
View
Yes
Amazon SimpleDB
Select
Create
Yes
Amazon Network Firewall
AssociateFirewallPolicy
Create
Yes
Amazon Network Firewall
AssociateSubnets
Create
Yes
Amazon Network Firewall
CreateFirewall
Create
Yes
Amazon Network Firewall
CreateFirewallPolicy
Create
Yes
Amazon Network Firewall
CreateRuleGroup
Create
Yes
Amazon Network Firewall
DeleteFirewall
Delete
Yes
Amazon Network Firewall
DeleteFirewallPolicy
Delete
Yes
Amazon Network Firewall
DeleteResourcePolicy
Delete
Yes
Amazon Network Firewall
DeleteRuleGroup
Delete
Yes
Amazon Network Firewall
DescribeFirewall
View
Yes
Amazon Network Firewall
DescribeFirewallPolicy
View
Yes
Amazon Network Firewall
DescribeLoggingConfiguration
View
Yes
Amazon Network Firewall
DescribeResourcePolicy
View
Yes
Amazon Network Firewall
DescribeRuleGroup
View
Yes
Amazon Network Firewall
DisassociateSubnets
Delete
Yes
Amazon Network Firewall
ListFirewallPolicies
View
Yes
Amazon Network Firewall
ListFirewalls
View
Yes
Amazon Network Firewall
ListRuleGroups
View
Yes
Amazon Network Firewall
ListTagsForResource
View
Yes
Amazon Network Firewall
PutResourcePolicy
Edit
Yes
Amazon Network Firewall
TagResource
Create
Yes
Amazon Network Firewall
UntagResource
Delete
Yes
Amazon Network Firewall
UpdateFirewallDeleteProtection
Edit
Yes
Amazon Network Firewall
UpdateFirewallDescription
Edit
Yes
Amazon Network Firewall
UpdateFirewallPolicy
Edit
Yes
Amazon Network Firewall
UpdateFirewallPolicyChangeProtection
Edit
Yes
Amazon Network Firewall
UpdateLoggingConfiguration
Edit
Yes
Amazon Network Firewall
UpdateRuleGroup
Edit
Yes
Amazon Network Firewall
UpdateSubnetChangeProtection
Edit
Yes
Amazon Interactive Video Service
GetChannel
View
Yes
Amazon Interactive Video Service
GetStreamKey
View
Yes
Amazon Interactive Video Service
CreateChannel
Create
Yes
Amazon Interactive Video Service
CreateRecordingConfiguration
Create
Yes
Amazon Interactive Video Service
CreateStreamKey
Create
Yes
Amazon Interactive Video Service
DeleteChannel
Delete
Yes
Amazon Interactive Video Service
DeletePlaybackKeyPair
Delete
Yes
Amazon Interactive Video Service
DeleteRecordingConfiguration
Delete
Yes
Amazon Interactive Video Service
DeleteStreamKey
Delete
Yes
Amazon Interactive Video Service
GetPlaybackKeyPair
View
Yes
Amazon Interactive Video Service
GetRecordingConfiguration
View
Yes
Amazon Interactive Video Service
GetStream
View
Yes
Amazon Interactive Video Service
ImportPlaybackKeyPair
Create
Yes
Amazon Interactive Video Service
ListChannels
View
Yes
Amazon Interactive Video Service
ListPlaybackKeyPairs
View
Yes
Amazon Interactive Video Service
ListRecordingConfigurations
View
Yes
Amazon Interactive Video Service
ListStreamKeys
View
Yes
Amazon Interactive Video Service
ListStreams
View
Yes
Amazon Interactive Video Service
ListTagsForResource
View
Yes
Amazon Interactive Video Service
TagResource
Create
Yes
Amazon Interactive Video Service
PutMetadata
Edit
Yes
Amazon Interactive Video Service
StopStream
Stop
Yes
Amazon Interactive Video Service
UntagResource
Delete
Yes
Amazon Interactive Video Service
UpdateChannel
Edit
Yes
Amazon Machine Learning
AddTags
Create
Yes
Amazon Machine Learning
CreatePrediction
Create
Yes
Amazon Machine Learning
CreateDataSourceFromRDS
Create
Yes
Amazon Machine Learning
CreateDataSourceFromRedshift
Create
Yes
Amazon Machine Learning
CreateDataSourceFromS
Create
Yes
Amazon Machine Learning
CreateEvaluation
Create
Yes
Amazon Machine Learning
CreateMLModel
Create
Yes
Amazon Machine Learning
CreateRealtimeEndpoint
Create
Yes
Amazon Machine Learning
DeletePrediction
Delete
Yes
Amazon Machine Learning
DeleteDataSource
Delete
Yes
Amazon Machine Learning
DeleteEvaluation
Delete
Yes
Amazon Machine Learning
DeleteMLModel
Delete
Yes
Amazon Machine Learning
DeleteRealtimeEndpoint
Delete
Yes
Amazon Machine Learning
DeleteTags
Delete
Yes
Amazon Machine Learning
DescribePredictions
View
Yes
Amazon Machine Learning
DescribeDataSources
View
Yes
Amazon Machine Learning
DescribeEvaluations
View
Yes
Amazon Machine Learning
DescribeMLModels
View
Yes
Amazon Machine Learning
DescribeTags
View
Yes
Amazon Machine Learning
GetPrediction
View
Yes
Amazon Machine Learning
GetDataSource
View
Yes
Amazon Machine Learning
GetEvaluation
View
Yes
Amazon Machine Learning
GetMLModel
View
Yes
Amazon Machine Learning
Predict
Create
Yes
Amazon Machine Learning
UpdatePrediction
Edit
Yes
Amazon Machine Learning
UpdateDataSource
Edit
Yes
Amazon Machine Learning
UpdateEvaluation
Edit
Yes
Amazon Machine Learning
UpdateMLModel
Edit
Yes
Amazon Batch
CancelJob
Delete
Yes
Amazon Batch
CreateComputeEnvironment
Create
Yes
Amazon Batch
CreateJobQueue
Create
Yes
Amazon Batch
DeleteComputeEnvironment
Delete
Yes
Amazon Batch
DeleteJobQueue
Delete
Yes
Amazon Batch
DeregisterJobDefinition
Deregister
Yes
Amazon Batch
DescribeComputeEnvironments
View
Yes
Amazon Batch
DescribeJobDefinitions
View
Yes
Amazon Batch
DescribeJobQueues
View
Yes
Amazon Batch
DescribeJobs
View
Yes
Amazon Batch
ListJobs
View
Yes
Amazon Batch
ListTagsForResource
View
Yes
Amazon Batch
TagResource
Create
Yes
Amazon Batch
RegisterJobDefinition
Register
Yes
Amazon Batch
SubmitJob
Create
Yes
Amazon Batch
TerminateJob
Terminate
Yes
Amazon Batch
UntagResource
Delete
Yes
Amazon Batch
UpdateComputeEnvironment
Edit
Yes
Amazon Batch
UpdateJobQueue
Edit
Yes
Amazon Savings Plans
CreateSavingsPlan
Create
Yes
Amazon Savings Plans
DeleteQueuedSavingsPlan
Delete
Yes
Amazon Savings Plans
DescribeSavingsPlanRates
View
Yes
Amazon Savings Plans
DescribeSavingsPlans
View
Yes
Amazon Savings Plans
DescribeSavingsPlansOfferingRates
View
Yes
Amazon Savings Plans
DescribeSavingsPlansOfferings
View
Yes
Amazon Savings Plans
ListTagsForResource
View
Yes
Amazon Savings Plans
TagResource
Create
Yes
Amazon Savings Plans
UntagResource
Delete
Yes
Amazon Sagemaker Edge Manager
GetDeviceRegistration
View
Yes
Amazon Sagemaker Edge Manager
SendHeartbeat
Send
Yes
Amazon Application Cost Profiler
DeleteReportDefinition
Delete
Yes
Amazon Application Cost Profiler
GetReportDefinition
View
Yes
Amazon Application Cost Profiler
UpdateReportDefinition
Edit
Yes
Amazon Application Cost Profiler
ImportApplicationUsage
Create
Yes
Amazon Application Cost Profiler
ListReportDefinitions
View
Yes
Amazon Application Cost Profiler
PutReportDefinition
Edit
Yes
Amazon Detective
AcceptInvitation
Approve
Yes
Amazon Detective
CreateGraph
Create
Yes
Amazon Detective
CreateMembers
Create
Yes
Amazon Detective
DeleteGraph
Delete
Yes
Amazon Detective
DeleteMembers
Delete
Yes
Amazon Detective
DisassociateMembership
Delete
Yes
Amazon Detective
GetMembers
View
Yes
Amazon Detective
ListGraphs
View
Yes
Amazon Detective
ListInvitations
View
Yes
Amazon Detective
ListMembers
View
Yes
Amazon Detective
ListTagsForResource
View
Yes
Amazon Detective
TagResource
Create
Yes
Amazon Detective
RejectInvitation
Reject
Yes
Amazon Detective
StartMonitoringMember
Start
Yes
Amazon Detective
UntagResource
Delete
Yes
Amazon Marketplace Metering
MeterUsage
Create
Yes
Amazon Marketplace Metering
RegisterUsage
Register
Yes
Amazon Marketplace Metering
ResolveCustomer
Create
Yes
Amazon Serverless Application Repository
CreateApplication
Create
Yes
Amazon Serverless Application Repository
ListApplications
View
Yes
Amazon Serverless Application Repository
CreateApplicationVersion
Create
Yes
Amazon Serverless Application Repository
CreateCloudFormationChangeSet
Create
Yes
Amazon Serverless Application Repository
CreateCloudFormationTemplate
Create
Yes
Amazon Serverless Application Repository
DeleteApplication
Delete
Yes
Amazon Serverless Application Repository
GetApplication
View
Yes
Amazon Serverless Application Repository
UpdateApplication
Edit
Yes
Amazon Serverless Application Repository
GetApplicationPolicy
View
Yes
Amazon Serverless Application Repository
PutApplicationPolicy
Edit
Yes
Amazon Serverless Application Repository
GetCloudFormationTemplate
View
Yes
Amazon Serverless Application Repository
ListApplicationDependencies
View
Yes
Amazon Serverless Application Repository
ListApplicationVersions
View
Yes
Amazon Serverless Application Repository
UnshareApplication
Create
Yes
Amazon Lex Runtime Service
DeleteSession
Delete
Yes
Amazon Lex Runtime Service
PutSession
Edit
Yes
Amazon Lex Runtime Service
GetSession
View
Yes
Amazon Lex Runtime Service
PostContent
Create
Yes
Amazon Lex Runtime Service
PostText
Create
Yes
Amazon Transfer Family
CreateAccess
Create
Yes
Amazon Transfer Family
CreateServer
Create
Yes
Amazon Transfer Family
CreateUser
Create
Yes
Amazon Transfer Family
CreateWorkflow
Create
Yes
Amazon Transfer Family
DeleteAccess
Delete
Yes
Amazon Transfer Family
DeleteServer
Delete
Yes
Amazon Transfer Family
DeleteSshPublicKey
Delete
Yes
Amazon Transfer Family
DeleteUser
Delete
Yes
Amazon Transfer Family
DeleteWorkflow
Delete
Yes
Amazon Transfer Family
DescribeAccess
View
Yes
Amazon Transfer Family
DescribeExecution
View
Yes
Amazon Transfer Family
DescribeSecurityPolicy
View
Yes
Amazon Transfer Family
DescribeServer
View
Yes
Amazon Transfer Family
DescribeUser
View
Yes
Amazon Transfer Family
DescribeWorkflow
View
Yes
Amazon Transfer Family
ImportSshPublicKey
Create
Yes
Amazon Transfer Family
ListAccesses
View
Yes
Amazon Transfer Family
ListExecutions
View
Yes
Amazon Transfer Family
ListSecurityPolicies
View
Yes
Amazon Transfer Family
ListServers
View
Yes
Amazon Transfer Family
ListTagsForResource
View
Yes
Amazon Transfer Family
ListUsers
View
Yes
Amazon Transfer Family
ListWorkflows
View
Yes
Amazon Transfer Family
SendWorkflowStepState
Send
Yes
Amazon Transfer Family
StartServer
Start
Yes
Amazon Transfer Family
StopServer
Stop
Yes
Amazon Transfer Family
TagResource
Create
Yes
Amazon Transfer Family
TestIdentityProvider
Create
Yes
Amazon Transfer Family
UntagResource
Delete
Yes
Amazon Transfer Family
UpdateAccess
Edit
Yes
Amazon Transfer Family
UpdateServer
Edit
Yes
Amazon Transfer Family
UpdateUser
Edit
Yes
Amazon Appflow
CreateConnectorProfile
Create
Yes
Amazon Appflow
CreateFlow
Create
Yes
Amazon Appflow
DeleteConnectorProfile
Delete
Yes
Amazon Appflow
DeleteFlow
Delete
Yes
Amazon Appflow
DescribeConnectorEntity
View
Yes
Amazon Appflow
DescribeConnectorProfiles
View
Yes
Amazon Appflow
DescribeConnectors
View
Yes
Amazon Appflow
DescribeFlow
View
Yes
Amazon Appflow
DescribeFlowExecutionRecords
View
Yes
Amazon Appflow
ListConnectorEntities
View
Yes
Amazon Appflow
ListFlows
View
Yes
Amazon Appflow
ListTagsForResource
View
Yes
Amazon Appflow
TagResource
Create
Yes
Amazon Appflow
StartFlow
Start
Yes
Amazon Appflow
StopFlow
Stop
Yes
Amazon Appflow
UntagResource
Delete
Yes
Amazon Appflow
UpdateConnectorProfile
Edit
Yes
Amazon Appflow
UpdateFlow
Edit
Yes
Amazon Systems Manager Incident Manager
CreateReplicationSet
Create
Yes
Amazon Systems Manager Incident Manager
CreateResponsePlan
Create
Yes
Amazon Systems Manager Incident Manager
CreateTimelineEvent
Create
Yes
Amazon Systems Manager Incident Manager
DeleteIncidentRecord
Delete
Yes
Amazon Systems Manager Incident Manager
DeleteReplicationSet
Delete
Yes
Amazon Systems Manager Incident Manager
DeleteResourcePolicy
Delete
Yes
Amazon Systems Manager Incident Manager
DeleteResponsePlan
Delete
Yes
Amazon Systems Manager Incident Manager
DeleteTimelineEvent
Delete
Yes
Amazon Systems Manager Incident Manager
GetIncidentRecord
View
Yes
Amazon Systems Manager Incident Manager
GetReplicationSet
View
Yes
Amazon Systems Manager Incident Manager
GetResourcePolicies
View
Yes
Amazon Systems Manager Incident Manager
GetResponsePlan
View
Yes
Amazon Systems Manager Incident Manager
GetTimelineEvent
View
Yes
Amazon Systems Manager Incident Manager
ListIncidentRecords
View
Yes
Amazon Systems Manager Incident Manager
ListRelatedItems
View
Yes
Amazon Systems Manager Incident Manager
ListReplicationSets
View
Yes
Amazon Systems Manager Incident Manager
ListResponsePlans
View
Yes
Amazon Systems Manager Incident Manager
ListTagsForResource
View
Yes
Amazon Systems Manager Incident Manager
TagResource
Create
Yes
Amazon Systems Manager Incident Manager
ListTimelineEvents
View
Yes
Amazon Systems Manager Incident Manager
PutResourcePolicy
Edit
Yes
Amazon Systems Manager Incident Manager
StartIncident
Start
Yes
Amazon Systems Manager Incident Manager
UntagResource
Delete
Yes
Amazon Systems Manager Incident Manager
UpdateDeletionProtection
Edit
Yes
Amazon Systems Manager Incident Manager
UpdateIncidentRecord
Edit
Yes
Amazon Systems Manager Incident Manager
UpdateRelatedItems
Edit
Yes
Amazon Systems Manager Incident Manager
UpdateReplicationSet
Edit
Yes
Amazon Systems Manager Incident Manager
UpdateResponsePlan
Edit
Yes
Amazon Systems Manager Incident Manager
UpdateTimelineEvent
Edit
Yes
Amazon MWAA
CreateCliToken
Create
Yes
Amazon MWAA
CreateEnvironment
Create
Yes
Amazon MWAA
DeleteEnvironment
Delete
Yes
Amazon MWAA
GetEnvironment
View
Yes
Amazon MWAA
UpdateEnvironment
Edit
Yes
Amazon MWAA
CreateWebLoginToken
Create
Yes
Amazon MWAA
ListEnvironments
View
Yes
Amazon MWAA
ListTagsForResource
View
Yes
Amazon MWAA
TagResource
Create
Yes
Amazon MWAA
PublishMetrics
Create
Yes
Amazon MWAA
UntagResource
Delete
Yes
Amazon Device Farm
CreateDevicePool
Create
Yes
Amazon Device Farm
CreateInstanceProfile
Create
Yes
Amazon Device Farm
CreateNetworkProfile
Create
Yes
Amazon Device Farm
CreateProject
Create
Yes
Amazon Device Farm
CreateRemoteAccessSession
Create
Yes
Amazon Device Farm
CreateTestGridProject
Create
Yes
Amazon Device Farm
CreateTestGridUrl
Create
Yes
Amazon Device Farm
CreateUpload
Create
Yes
Amazon Device Farm
CreateVPCEConfiguration
Create
Yes
Amazon Device Farm
DeleteDevicePool
Delete
Yes
Amazon Device Farm
DeleteInstanceProfile
Delete
Yes
Amazon Device Farm
DeleteNetworkProfile
Delete
Yes
Amazon Device Farm
DeleteProject
Delete
Yes
Amazon Device Farm
DeleteRemoteAccessSession
Delete
Yes
Amazon Device Farm
DeleteRun
Delete
Yes
Amazon Device Farm
DeleteTestGridProject
Delete
Yes
Amazon Device Farm
DeleteUpload
Delete
Yes
Amazon Device Farm
DeleteVPCEConfiguration
Delete
Yes
Amazon Device Farm
GetAccountSettings
View
Yes
Amazon Device Farm
GetDevice
View
Yes
Amazon Device Farm
GetDeviceInstance
View
Yes
Amazon Device Farm
GetDevicePool
View
Yes
Amazon Device Farm
GetDevicePoolCompatibility
View
Yes
Amazon Device Farm
GetInstanceProfile
View
Yes
Amazon Device Farm
GetJob
View
Yes
Amazon Device Farm
GetNetworkProfile
View
Yes
Amazon Device Farm
GetOfferingStatus
View
Yes
Amazon Device Farm
GetProject
View
Yes
Amazon Device Farm
GetRemoteAccessSession
View
Yes
Amazon Device Farm
GetRun
View
Yes
Amazon Device Farm
GetSuite
View
Yes
Amazon Device Farm
GetTest
View
Yes
Amazon Device Farm
GetTestGridProject
View
Yes
Amazon Device Farm
GetTestGridSession
View
Yes
Amazon Device Farm
GetUpload
View
Yes
Amazon Device Farm
GetVPCEConfiguration
View
Yes
Amazon Device Farm
InstallToRemoteAccessSession
Create
Yes
Amazon Device Farm
ListArtifacts
View
Yes
Amazon Device Farm
ListDeviceInstances
View
Yes
Amazon Device Farm
ListDevicePools
View
Yes
Amazon Device Farm
ListDevices
View
Yes
Amazon Device Farm
ListInstanceProfiles
View
Yes
Amazon Device Farm
ListJobs
View
Yes
Amazon Device Farm
ListNetworkProfiles
View
Yes
Amazon Device Farm
ListOfferingPromotions
View
Yes
Amazon Device Farm
ListOfferingTransactions
View
Yes
Amazon Device Farm
ListOfferings
View
Yes
Amazon Device Farm
ListProjects
View
Yes
Amazon Device Farm
ListRemoteAccessSessions
View
Yes
Amazon Device Farm
ListRuns
View
Yes
Amazon Device Farm
ListSamples
View
Yes
Amazon Device Farm
ListSuites
View
Yes
Amazon Device Farm
ListTagsForResource
View
Yes
Amazon Device Farm
ListTestGridProjects
View
Yes
Amazon Device Farm
ListTestGridSessionActions
View
Yes
Amazon Device Farm
ListTestGridSessionArtifacts
View
Yes
Amazon Device Farm
ListTestGridSessions
View
Yes
Amazon Device Farm
ListTests
View
Yes
Amazon Device Farm
ListUniqueProblems
View
Yes
Amazon Device Farm
ListUploads
View
Yes
Amazon Device Farm
ListVPCEConfigurations
View
Yes
Amazon Device Farm
PurchaseOffering
Purchase
Yes
Amazon Device Farm
RenewOffering
Create
Yes
Amazon Device Farm
ScheduleRun
Create
Yes
Amazon Device Farm
StopJob
Stop
Yes
Amazon Device Farm
StopRemoteAccessSession
Stop
Yes
Amazon Device Farm
StopRun
Stop
Yes
Amazon Device Farm
TagResource
Create
Yes
Amazon Device Farm
UntagResource
Delete
Yes
Amazon Device Farm
UpdateDeviceInstance
Edit
Yes
Amazon Device Farm
UpdateDevicePool
Edit
Yes
Amazon Device Farm
UpdateInstanceProfile
Edit
Yes
Amazon Device Farm
UpdateNetworkProfile
Edit
Yes
Amazon Device Farm
UpdateProject
Edit
Yes
Amazon Device Farm
UpdateTestGridProject
Edit
Yes
Amazon Device Farm
UpdateUpload
Edit
Yes
Amazon Device Farm
UpdateVPCEConfiguration
Edit
Yes
Amazon Single Sign-On
GetRoleCredentials
View
Yes
Amazon Single Sign-On
ListAccountRoles
View
Yes
Amazon Single Sign-On
ListAccounts
View
Yes
Amazon Single Sign-On
Logout
Create
Yes
Amazon Pinpoint
CreateApp
Create
Yes
Amazon Pinpoint
GetApps
View
Yes
Amazon Pinpoint
CreateCampaign
Create
Yes
Amazon Pinpoint
GetCampaigns
View
Yes
Amazon Pinpoint
CreateEmailTemplate
Create
Yes
Amazon Pinpoint
DeleteEmailTemplate
Delete
Yes
Amazon Pinpoint
GetEmailTemplate
View
Yes
Amazon Pinpoint
UpdateEmailTemplate
Edit
Yes
Amazon Pinpoint
CreateExportJob
Create
Yes
Amazon Pinpoint
GetExportJobs
View
Yes
Amazon Pinpoint
CreateImportJob
Create
Yes
Amazon Pinpoint
GetImportJobs
View
Yes
Amazon Pinpoint
CreateInAppTemplate
Create
Yes
Amazon Pinpoint
DeleteInAppTemplate
Delete
Yes
Amazon Pinpoint
GetInAppTemplate
View
Yes
Amazon Pinpoint
UpdateInAppTemplate
Edit
Yes
Amazon Pinpoint
CreateJourney
Create
Yes
Amazon Pinpoint
ListJourneys
View
Yes
Amazon Pinpoint
CreatePushTemplate
Create
Yes
Amazon Pinpoint
DeletePushTemplate
Delete
Yes
Amazon Pinpoint
GetPushTemplate
View
Yes
Amazon Pinpoint
UpdatePushTemplate
Edit
Yes
Amazon Pinpoint
CreateRecommenderConfiguration
Create
Yes
Amazon Pinpoint
GetRecommenderConfigurations
View
Yes
Amazon Pinpoint
CreateSegment
Create
Yes
Amazon Pinpoint
GetSegments
View
Yes
Amazon Pinpoint
CreateSmsTemplate
Create
Yes
Amazon Pinpoint
DeleteSmsTemplate
Delete
Yes
Amazon Pinpoint
GetSmsTemplate
View
Yes
Amazon Pinpoint
UpdateSmsTemplate
Edit
Yes
Amazon Pinpoint
CreateVoiceTemplate
Create
Yes
Amazon Pinpoint
DeleteVoiceTemplate
Delete
Yes
Amazon Pinpoint
GetVoiceTemplate
View
Yes
Amazon Pinpoint
UpdateVoiceTemplate
Edit
Yes
Amazon Pinpoint
DeleteAdmChannel
Delete
Yes
Amazon Pinpoint
GetAdmChannel
View
Yes
Amazon Pinpoint
UpdateAdmChannel
Edit
Yes
Amazon Pinpoint
DeleteApnsChannel
Delete
Yes
Amazon Pinpoint
GetApnsChannel
View
Yes
Amazon Pinpoint
UpdateApnsChannel
Edit
Yes
Amazon Pinpoint
DeleteApnsSandboxChannel
Delete
Yes
Amazon Pinpoint
GetApnsSandboxChannel
View
Yes
Amazon Pinpoint
UpdateApnsSandboxChannel
Edit
Yes
Amazon Pinpoint
DeleteApnsVoipChannel
Delete
Yes
Amazon Pinpoint
GetApnsVoipChannel
View
Yes
Amazon Pinpoint
UpdateApnsVoipChannel
Edit
Yes
Amazon Pinpoint
DeleteApnsVoipSandboxChannel
Delete
Yes
Amazon Pinpoint
GetApnsVoipSandboxChannel
View
Yes
Amazon Pinpoint
UpdateApnsVoipSandboxChannel
Edit
Yes
Amazon Pinpoint
DeleteApp
Delete
Yes
Amazon Pinpoint
GetApp
View
Yes
Amazon Pinpoint
DeleteBaiduChannel
Delete
Yes
Amazon Pinpoint
GetBaiduChannel
View
Yes
Amazon Pinpoint
UpdateBaiduChannel
Edit
Yes
Amazon Pinpoint
DeleteCampaign
Delete
Yes
Amazon Pinpoint
GetCampaign
View
Yes
Amazon Pinpoint
UpdateCampaign
Edit
Yes
Amazon Pinpoint
DeleteEmailChannel
Delete
Yes
Amazon Pinpoint
GetEmailChannel
View
Yes
Amazon Pinpoint
UpdateEmailChannel
Edit
Yes
Amazon Pinpoint
DeleteEndpoint
Delete
Yes
Amazon Pinpoint
GetEndpoint
View
Yes
Amazon Pinpoint
UpdateEndpoint
Edit
Yes
Amazon Pinpoint
DeleteEventStream
Delete
Yes
Amazon Pinpoint
GetEventStream
View
Yes
Amazon Pinpoint
PutEventStream
Edit
Yes
Amazon Pinpoint
DeleteGcmChannel
Delete
Yes
Amazon Pinpoint
GetGcmChannel
View
Yes
Amazon Pinpoint
UpdateGcmChannel
Edit
Yes
Amazon Pinpoint
DeleteJourney
Delete
Yes
Amazon Pinpoint
GetJourney
View
Yes
Amazon Pinpoint
UpdateJourney
Edit
Yes
Amazon Pinpoint
DeleteRecommenderConfiguration
Delete
Yes
Amazon Pinpoint
GetRecommenderConfiguration
View
Yes
Amazon Pinpoint
UpdateRecommenderConfiguration
Edit
Yes
Amazon Pinpoint
DeleteSegment
Delete
Yes
Amazon Pinpoint
GetSegment
View
Yes
Amazon Pinpoint
UpdateSegment
Edit
Yes
Amazon Pinpoint
DeleteSmsChannel
Delete
Yes
Amazon Pinpoint
GetSmsChannel
View
Yes
Amazon Pinpoint
UpdateSmsChannel
Edit
Yes
Amazon Pinpoint
DeleteUserEndpoints
Delete
Yes
Amazon Pinpoint
GetUserEndpoints
View
Yes
Amazon Pinpoint
DeleteVoiceChannel
Delete
Yes
Amazon Pinpoint
GetVoiceChannel
View
Yes
Amazon Pinpoint
UpdateVoiceChannel
Edit
Yes
Amazon Pinpoint
GetApplicationDateRangeKpi
View
Yes
Amazon Pinpoint
GetApplicationSettings
View
Yes
Amazon Pinpoint
UpdateApplicationSettings
Edit
Yes
Amazon Pinpoint
GetCampaignActivities
View
Yes
Amazon Pinpoint
GetCampaignDateRangeKpi
View
Yes
Amazon Pinpoint
GetCampaignVersion
View
Yes
Amazon Pinpoint
GetCampaignVersions
View
Yes
Amazon Pinpoint
GetChannels
View
Yes
Amazon Pinpoint
GetExportJob
View
Yes
Amazon Pinpoint
GetImportJob
View
Yes
Amazon Pinpoint
GetInAppMessages
View
Yes
Amazon Pinpoint
GetJourneyDateRangeKpi
View
Yes
Amazon Pinpoint
GetJourneyExecutionActivityMetrics
View
Yes
Amazon Pinpoint
GetJourneyExecutionMetrics
View
Yes
Amazon Pinpoint
GetSegmentExportJobs
View
Yes
Amazon Pinpoint
GetSegmentImportJobs
View
Yes
Amazon Pinpoint
GetSegmentVersion
View
Yes
Amazon Pinpoint
GetSegmentVersions
View
Yes
Amazon Pinpoint
ListTagsForResource
View
Yes
Amazon Pinpoint
TagResource
Create
Yes
Amazon Pinpoint
ListTemplateVersions
View
Yes
Amazon Pinpoint
ListTemplates
View
Yes
Amazon Pinpoint
PhoneNumberValidate
Create
Yes
Amazon Pinpoint
PutEvents
Edit
Yes
Amazon Pinpoint
RemoveAttributes
Delete
Yes
Amazon Pinpoint
SendMessages
Send
Yes
Amazon Pinpoint
SendUsersMessages
Send
Yes
Amazon Pinpoint
UntagResource
Delete
Yes
Amazon Pinpoint
UpdateEndpoints
Edit
Yes
Amazon Pinpoint
UpdateJourneyState
Edit
Yes
Amazon Pinpoint
UpdateTemplateActiveVersion
Edit
Yes
Amazon Marketplace Catalog Service
CancelChangeSet
Delete
Yes
Amazon Marketplace Catalog Service
DescribeChangeSet
View
Yes
Amazon Marketplace Catalog Service
DescribeEntity
View
Yes
Amazon Marketplace Catalog Service
ListChangeSets
View
Yes
Amazon Marketplace Catalog Service
ListEntities
View
Yes
Amazon Marketplace Catalog Service
StartChangeSet
Start
Yes
Amazon Signer
AddProfilePermission
Create
Yes
Amazon Signer
ListProfilePermissions
View
Yes
Amazon Signer
CancelSigningProfile
Delete
Yes
Amazon Signer
GetSigningProfile
View
Yes
Amazon Signer
PutSigningProfile
Edit
Yes
Amazon Signer
DescribeSigningJob
View
Yes
Amazon Signer
GetSigningPlatform
View
Yes
Amazon Signer
ListSigningJobs
View
Yes
Amazon Signer
StartSigningJob
Start
Yes
Amazon Signer
ListSigningPlatforms
View
Yes
Amazon Signer
ListSigningProfiles
View
Yes
Amazon Signer
ListTagsForResource
View
Yes
Amazon Signer
TagResource
Create
Yes
Amazon Signer
RemoveProfilePermission
Delete
Yes
Amazon Signer
RevokeSignature
Delete
Yes
Amazon Signer
RevokeSigningProfile
Delete
Yes
Amazon Signer
UntagResource
Delete
Yes
Amazon Chime
AssociatePhoneNumberWithUser
Create
Yes
Amazon Chime
AssociatePhoneNumbersWithVoiceConnector
Create
Yes
Amazon Chime
AssociatePhoneNumbersWithVoiceConnectorGroup
Create
Yes
Amazon Chime
AssociateSigninDelegateGroupsWithAccount
Create
Yes
Amazon Chime
CreateAttendee
Create
Yes
Amazon Chime
CreateChannelMembership
Create
Yes
Amazon Chime
CreateRoomMembership
Create
Yes
Amazon Chime
DeletePhoneNumber
Delete
Yes
Amazon Chime
SuspendUser
Delete
Yes
Amazon Chime
UnsuspendUser
Create
Yes
Amazon Chime
UpdatePhoneNumber
Edit
Yes
Amazon Chime
UpdateUser
Edit
Yes
Amazon Chime
ListUsers
View
Yes
Amazon Chime
CreateAccount
Create
Yes
Amazon Chime
ListAccounts
View
Yes
Amazon Chime
CreateAppInstance
Create
Yes
Amazon Chime
ListAppInstances
View
Yes
Amazon Chime
CreateAppInstanceAdmin
Create
Yes
Amazon Chime
ListAppInstanceAdmins
View
Yes
Amazon Chime
CreateAppInstanceUser
Create
Yes
Amazon Chime
ListAttendees
View
Yes
Amazon Chime
CreateBot
Create
Yes
Amazon Chime
ListBots
View
Yes
Amazon Chime
CreateChannel
Create
Yes
Amazon Chime
CreateChannelBan
Create
Yes
Amazon Chime
ListChannelBans
View
Yes
Amazon Chime
ListChannelMemberships
View
Yes
Amazon Chime
CreateChannelModerator
Create
Yes
Amazon Chime
ListChannelModerators
View
Yes
Amazon Chime
CreateMediaCapturePipeline
Create
Yes
Amazon Chime
ListMediaCapturePipelines
View
Yes
Amazon Chime
CreateMeeting
Create
Yes
Amazon Chime
ListMeetings
View
Yes
Amazon Chime
CreateMeetingDialOut
Create
Yes
Amazon Chime
CreateMeetingWithAttendees
Create
Yes
Amazon Chime
CreatePhoneNumberOrder
Create
Yes
Amazon Chime
ListPhoneNumberOrders
View
Yes
Amazon Chime
CreateProxySession
Create
Yes
Amazon Chime
ListProxySessions
View
Yes
Amazon Chime
CreateRoom
Create
Yes
Amazon Chime
ListRooms
View
Yes
Amazon Chime
ListRoomMemberships
View
Yes
Amazon Chime
CreateSipMediaApplication
Create
Yes
Amazon Chime
ListSipMediaApplications
View
Yes
Amazon Chime
CreateSipMediaApplicationCall
Create
Yes
Amazon Chime
CreateSipRule
Create
Yes
Amazon Chime
ListSipRules
View
Yes
Amazon Chime
CreateUser
Create
Yes
Amazon Chime
CreateVoiceConnector
Create
Yes
Amazon Chime
ListVoiceConnectors
View
Yes
Amazon Chime
CreateVoiceConnectorGroup
Create
Yes
Amazon Chime
ListVoiceConnectorGroups
View
Yes
Amazon Chime
DeleteAccount
Delete
Yes
Amazon Chime
GetAccount
View
Yes
Amazon Chime
UpdateAccount
Edit
Yes
Amazon Chime
DeleteAppInstance
Delete
Yes
Amazon Chime
DescribeAppInstance
View
Yes
Amazon Chime
UpdateAppInstance
Edit
Yes
Amazon Chime
DeleteAppInstanceAdmin
Delete
Yes
Amazon Chime
DescribeAppInstanceAdmin
View
Yes
Amazon Chime
DeleteAppInstanceStreamingConfigurations
Delete
Yes
Amazon Chime
GetAppInstanceStreamingConfigurations
View
Yes
Amazon Chime
PutAppInstanceStreamingConfigurations
Edit
Yes
Amazon Chime
DeleteAppInstanceUser
Delete
Yes
Amazon Chime
DescribeAppInstanceUser
View
Yes
Amazon Chime
UpdateAppInstanceUser
Edit
Yes
Amazon Chime
DeleteAttendee
Delete
Yes
Amazon Chime
GetAttendee
View
Yes
Amazon Chime
DeleteChannel
Delete
Yes
Amazon Chime
DescribeChannel
View
Yes
Amazon Chime
UpdateChannel
Edit
Yes
Amazon Chime
DeleteChannelBan
Delete
Yes
Amazon Chime
DescribeChannelBan
View
Yes
Amazon Chime
DeleteChannelMembership
Delete
Yes
Amazon Chime
DescribeChannelMembership
View
Yes
Amazon Chime
DeleteChannelMessage
Delete
Yes
Amazon Chime
GetChannelMessage
View
Yes
Amazon Chime
UpdateChannelMessage
Edit
Yes
Amazon Chime
DeleteChannelModerator
Delete
Yes
Amazon Chime
DescribeChannelModerator
View
Yes
Amazon Chime
DeleteEventsConfiguration
Delete
Yes
Amazon Chime
GetEventsConfiguration
View
Yes
Amazon Chime
PutEventsConfiguration
Edit
Yes
Amazon Chime
DeleteMediaCapturePipeline
Delete
Yes
Amazon Chime
GetMediaCapturePipeline
View
Yes
Amazon Chime
DeleteMeeting
Delete
Yes
Amazon Chime
GetMeeting
View
Yes
Amazon Chime
GetPhoneNumber
View
Yes
Amazon Chime
DeleteProxySession
Delete
Yes
Amazon Chime
GetProxySession
View
Yes
Amazon Chime
UpdateProxySession
Edit
Yes
Amazon Chime
DeleteRoom
Delete
Yes
Amazon Chime
GetRoom
View
Yes
Amazon Chime
UpdateRoom
Edit
Yes
Amazon Chime
DeleteRoomMembership
Delete
Yes
Amazon Chime
UpdateRoomMembership
Edit
Yes
Amazon Chime
DeleteSipMediaApplication
Delete
Yes
Amazon Chime
GetSipMediaApplication
View
Yes
Amazon Chime
UpdateSipMediaApplication
Edit
Yes
Amazon Chime
DeleteSipRule
Delete
Yes
Amazon Chime
GetSipRule
View
Yes
Amazon Chime
UpdateSipRule
Edit
Yes
Amazon Chime
DeleteVoiceConnector
Delete
Yes
Amazon Chime
GetVoiceConnector
View
Yes
Amazon Chime
UpdateVoiceConnector
Edit
Yes
Amazon Chime
DeleteVoiceConnectorEmergencyCallingConfiguration
Delete
Yes
Amazon Chime
GetVoiceConnectorEmergencyCallingConfiguration
View
Yes
Amazon Chime
PutVoiceConnectorEmergencyCallingConfiguration
Edit
Yes
Amazon Chime
DeleteVoiceConnectorGroup
Delete
Yes
Amazon Chime
GetVoiceConnectorGroup
View
Yes
Amazon Chime
UpdateVoiceConnectorGroup
Edit
Yes
Amazon Chime
DeleteVoiceConnectorOrigination
Delete
Yes
Amazon Chime
GetVoiceConnectorOrigination
View
Yes
Amazon Chime
PutVoiceConnectorOrigination
Edit
Yes
Amazon Chime
DeleteVoiceConnectorProxy
Delete
Yes
Amazon Chime
GetVoiceConnectorProxy
View
Yes
Amazon Chime
PutVoiceConnectorProxy
Edit
Yes
Amazon Chime
DeleteVoiceConnectorStreamingConfiguration
Delete
Yes
Amazon Chime
GetVoiceConnectorStreamingConfiguration
View
Yes
Amazon Chime
PutVoiceConnectorStreamingConfiguration
Edit
Yes
Amazon Chime
DeleteVoiceConnectorTermination
Delete
Yes
Amazon Chime
GetVoiceConnectorTermination
View
Yes
Amazon Chime
PutVoiceConnectorTermination
Edit
Yes
Amazon Chime
DeleteVoiceConnectorTerminationCredentials
Delete
Yes
Amazon Chime
DescribeChannelMembershipForAppInstanceUser
View
Yes
Amazon Chime
DescribeChannelModeratedByAppInstanceUser
View
Yes
Amazon Chime
DisassociatePhoneNumberFromUser
Delete
Yes
Amazon Chime
DisassociatePhoneNumbersFromVoiceConnector
Delete
Yes
Amazon Chime
DisassociatePhoneNumbersFromVoiceConnectorGroup
Delete
Yes
Amazon Chime
DisassociateSigninDelegateGroupsFromAccount
Delete
Yes
Amazon Chime
GetAccountSettings
View
Yes
Amazon Chime
UpdateAccountSettings
Edit
Yes
Amazon Chime
GetAppInstanceRetentionSettings
View
Yes
Amazon Chime
PutAppInstanceRetentionSettings
Edit
Yes
Amazon Chime
GetBot
View
Yes
Amazon Chime
UpdateBot
Edit
Yes
Amazon Chime
GetGlobalSettings
View
Yes
Amazon Chime
UpdateGlobalSettings
Edit
Yes
Amazon Chime
GetMessagingSessionEndpoint
View
Yes
Amazon Chime
GetPhoneNumberOrder
View
Yes
Amazon Chime
GetPhoneNumberSettings
View
Yes
Amazon Chime
UpdatePhoneNumberSettings
Edit
Yes
Amazon Chime
GetRetentionSettings
View
Yes
Amazon Chime
PutRetentionSettings
Edit
Yes
Amazon Chime
GetSipMediaApplicationLoggingConfiguration
View
Yes
Amazon Chime
PutSipMediaApplicationLoggingConfiguration
Edit
Yes
Amazon Chime
GetUser
View
Yes
Amazon Chime
GetUserSettings
View
Yes
Amazon Chime
UpdateUserSettings
Edit
Yes
Amazon Chime
GetVoiceConnectorLoggingConfiguration
View
Yes
Amazon Chime
PutVoiceConnectorLoggingConfiguration
Edit
Yes
Amazon Chime
GetVoiceConnectorTerminationHealth
View
Yes
Amazon Chime
InviteUsers
Create
Yes
Amazon Chime
ListAppInstanceUsers
View
Yes
Amazon Chime
ListAttendeeTags
View
Yes
Amazon Chime
ListChannelMembershipsForAppInstanceUser
View
Yes
Amazon Chime
ListChannelMessages
View
Yes
Amazon Chime
SendChannelMessage
Send
Yes
Amazon Chime
ListChannels
View
Yes
Amazon Chime
ListChannelsModeratedByAppInstanceUser
View
Yes
Amazon Chime
ListMeetingTags
View
Yes
Amazon Chime
ListPhoneNumbers
View
Yes
Amazon Chime
ListSupportedPhoneNumberCountries
View
Yes
Amazon Chime
ListTagsForResource
View
Yes
Amazon Chime
ListVoiceConnectorTerminationCredentials
View
Yes
Amazon Chime
LogoutUser
Create
Yes
Amazon Chime
PutVoiceConnectorTerminationCredentials
Edit
Yes
Amazon Chime
RedactChannelMessage
Create
Yes
Amazon Chime
RedactConversationMessage
Create
Yes
Amazon Chime
RedactRoomMessage
Create
Yes
Amazon Chime
RegenerateSecurityToken
Create
Yes
Amazon Chime
ResetPersonalPIN
Edit
Yes
Amazon Chime
RestorePhoneNumber
Create
Yes
Amazon Chime
SearchAvailablePhoneNumbers
Search
Yes
Amazon Chime
StartMeetingTranscription
Start
Yes
Amazon Chime
StopMeetingTranscription
Stop
Yes
Amazon Chime
TagAttendee
Create
Yes
Amazon Chime
TagMeeting
Create
Yes
Amazon Chime
TagResource
Create
Yes
Amazon Chime
UntagAttendee
Delete
Yes
Amazon Chime
UntagMeeting
Delete
Yes
Amazon Chime
UntagResource
Delete
Yes
Amazon Chime
UpdateChannelReadMarker
Edit
Yes
Amazon Chime
UpdateSipMediaApplicationCall
Edit
Yes
Amazon Glue DataBrew
DeleteRecipeVersion
Delete
Yes
Amazon Glue DataBrew
CreateDataset
Create
Yes
Amazon Glue DataBrew
ListDatasets
View
Yes
Amazon Glue DataBrew
CreateProfileJob
Create
Yes
Amazon Glue DataBrew
CreateProject
Create
Yes
Amazon Glue DataBrew
ListProjects
View
Yes
Amazon Glue DataBrew
CreateRecipe
Create
Yes
Amazon Glue DataBrew
ListRecipes
View
Yes
Amazon Glue DataBrew
CreateRecipeJob
Create
Yes
Amazon Glue DataBrew
CreateSchedule
Create
Yes
Amazon Glue DataBrew
ListSchedules
View
Yes
Amazon Glue DataBrew
DeleteDataset
Delete
Yes
Amazon Glue DataBrew
DescribeDataset
View
Yes
Amazon Glue DataBrew
UpdateDataset
Edit
Yes
Amazon Glue DataBrew
DeleteJob
Delete
Yes
Amazon Glue DataBrew
DescribeJob
View
Yes
Amazon Glue DataBrew
DeleteProject
Delete
Yes
Amazon Glue DataBrew
DescribeProject
View
Yes
Amazon Glue DataBrew
UpdateProject
Edit
Yes
Amazon Glue DataBrew
DeleteSchedule
Delete
Yes
Amazon Glue DataBrew
DescribeSchedule
View
Yes
Amazon Glue DataBrew
UpdateSchedule
Edit
Yes
Amazon Glue DataBrew
DescribeJobRun
View
Yes
Amazon Glue DataBrew
DescribeRecipe
View
Yes
Amazon Glue DataBrew
UpdateRecipe
Edit
Yes
Amazon Glue DataBrew
ListJobRuns
View
Yes
Amazon Glue DataBrew
ListJobs
View
Yes
Amazon Glue DataBrew
ListRecipeVersions
View
Yes
Amazon Glue DataBrew
ListTagsForResource
View
Yes
Amazon Glue DataBrew
TagResource
Create
Yes
Amazon Glue DataBrew
PublishRecipe
Create
Yes
Amazon Glue DataBrew
SendProjectSessionAction
Send
Yes
Amazon Glue DataBrew
StartJobRun
Start
Yes
Amazon Glue DataBrew
StartProjectSession
Start
Yes
Amazon Glue DataBrew
StopJobRun
Stop
Yes
Amazon Glue DataBrew
UntagResource
Delete
Yes
Amazon Glue DataBrew
UpdateProfileJob
Edit
Yes
Amazon Glue DataBrew
UpdateRecipeJob
Edit
Yes
Amazon Rekognition
CompareFaces
Create
Yes
Amazon Rekognition
CreateCollection
Create
Yes
Amazon Rekognition
CreateProject
Create
Yes
Amazon Rekognition
CreateProjectVersion
Create
Yes
Amazon Rekognition
CreateStreamProcessor
Create
Yes
Amazon Rekognition
DeleteCollection
Delete
Yes
Amazon Rekognition
DeleteFaces
Delete
Yes
Amazon Rekognition
DeleteProject
Delete
Yes
Amazon Rekognition
DeleteProjectVersion
Delete
Yes
Amazon Rekognition
DeleteStreamProcessor
Delete
Yes
Amazon Rekognition
DescribeCollection
View
Yes
Amazon Rekognition
DescribeProjectVersions
View
Yes
Amazon Rekognition
DescribeProjects
View
Yes
Amazon Rekognition
DescribeStreamProcessor
View
Yes
Amazon Rekognition
DetectCustomLabels
Create
Yes
Amazon Rekognition
DetectFaces
Create
Yes
Amazon Rekognition
DetectLabels
Create
Yes
Amazon Rekognition
DetectModerationLabels
Create
Yes
Amazon Rekognition
DetectProtectiveEquipment
Create
Yes
Amazon Rekognition
DetectText
Create
Yes
Amazon Rekognition
GetCelebrityInfo
View
Yes
Amazon Rekognition
GetCelebrityRecognition
View
Yes
Amazon Rekognition
GetContentModeration
View
Yes
Amazon Rekognition
GetFaceDetection
View
Yes
Amazon Rekognition
GetFaceSearch
View
Yes
Amazon Rekognition
GetLabelDetection
View
Yes
Amazon Rekognition
GetPersonTracking
View
Yes
Amazon Rekognition
GetSegmentDetection
View
Yes
Amazon Rekognition
GetTextDetection
View
Yes
Amazon Rekognition
IndexFaces
Create
Yes
Amazon Rekognition
ListCollections
View
Yes
Amazon Rekognition
ListFaces
View
Yes
Amazon Rekognition
ListStreamProcessors
View
Yes
Amazon Rekognition
ListTagsForResource
View
Yes
Amazon Rekognition
RecognizeCelebrities
Create
Yes
Amazon Rekognition
SearchFaces
Search
Yes
Amazon Rekognition
SearchFacesByImage
Search
Yes
Amazon Rekognition
StartCelebrityRecognition
Start
Yes
Amazon Rekognition
StartContentModeration
Start
Yes
Amazon Rekognition
StartFaceDetection
Start
Yes
Amazon Rekognition
StartFaceSearch
Start
Yes
Amazon Rekognition
StartLabelDetection
Start
Yes
Amazon Rekognition
StartPersonTracking
Start
Yes
Amazon Rekognition
StartProjectVersion
Start
Yes
Amazon Rekognition
StartSegmentDetection
Start
Yes
Amazon Rekognition
StartStreamProcessor
Start
Yes
Amazon Rekognition
StartTextDetection
Start
Yes
Amazon Rekognition
StopProjectVersion
Stop
Yes
Amazon Rekognition
StopStreamProcessor
Stop
Yes
Amazon Rekognition
TagResource
Create
Yes
Amazon Rekognition
UntagResource
Delete
Yes
Amazon Migration Hub
AssociateCreatedArtifact
Create
Yes
Amazon Migration Hub
AssociateDiscoveredResource
Create
Yes
Amazon Migration Hub
CreateProgressUpdateStream
Create
Yes
Amazon Migration Hub
DeleteProgressUpdateStream
Delete
Yes
Amazon Migration Hub
DescribeApplicationState
View
Yes
Amazon Migration Hub
DescribeMigrationTask
View
Yes
Amazon Migration Hub
DisassociateCreatedArtifact
Delete
Yes
Amazon Migration Hub
DisassociateDiscoveredResource
Delete
Yes
Amazon Migration Hub
ImportMigrationTask
Create
Yes
Amazon Migration Hub
ListApplicationStates
View
Yes
Amazon Migration Hub
ListCreatedArtifacts
View
Yes
Amazon Migration Hub
ListDiscoveredResources
View
Yes
Amazon Migration Hub
ListMigrationTasks
View
Yes
Amazon Migration Hub
ListProgressUpdateStreams
View
Yes
Amazon Migration Hub
NotifyApplicationState
Create
Yes
Amazon Migration Hub
NotifyMigrationTaskState
Create
Yes
Amazon Migration Hub
PutResourceAttributes
Edit
Yes
Amazon Braket
CancelQuantumTask
Delete
Yes
Amazon Braket
CreateQuantumTask
Create
Yes
Amazon Braket
GetDevice
View
Yes
Amazon Braket
GetQuantumTask
View
Yes
Amazon Braket
ListTagsForResource
View
Yes
Amazon Braket
TagResource
Create
Yes
Amazon Braket
SearchDevices
Search
Yes
Amazon Braket
SearchQuantumTasks
Search
Yes
Amazon Braket
UntagResource
Delete
Yes
Amazon Lex Model Building Service
CreateBotVersion
Create
Yes
Amazon Lex Model Building Service
CreateIntentVersion
Create
Yes
Amazon Lex Model Building Service
CreateSlotTypeVersion
Create
Yes
Amazon Lex Model Building Service
DeleteBot
Delete
Yes
Amazon Lex Model Building Service
DeleteBotAlias
Delete
Yes
Amazon Lex Model Building Service
GetBotAlias
View
Yes
Amazon Lex Model Building Service
PutBotAlias
Edit
Yes
Amazon Lex Model Building Service
DeleteBotChannelAssociation
Delete
Yes
Amazon Lex Model Building Service
GetBotChannelAssociation
View
Yes
Amazon Lex Model Building Service
DeleteBotVersion
Delete
Yes
Amazon Lex Model Building Service
DeleteIntent
Delete
Yes
Amazon Lex Model Building Service
DeleteIntentVersion
Delete
Yes
Amazon Lex Model Building Service
GetIntent
View
Yes
Amazon Lex Model Building Service
DeleteSlotType
Delete
Yes
Amazon Lex Model Building Service
DeleteSlotTypeVersion
Delete
Yes
Amazon Lex Model Building Service
DeleteUtterances
Delete
Yes
Amazon Lex Model Building Service
GetBot
View
Yes
Amazon Lex Model Building Service
GetBotAliases
View
Yes
Amazon Lex Model Building Service
GetBotChannelAssociations
View
Yes
Amazon Lex Model Building Service
GetBotVersions
View
Yes
Amazon Lex Model Building Service
GetBots
View
Yes
Amazon Lex Model Building Service
GetBuiltinIntent
View
Yes
Amazon Lex Model Building Service
GetBuiltinIntents
View
Yes
Amazon Lex Model Building Service
GetBuiltinSlotTypes
View
Yes
Amazon Lex Model Building Service
GetExport
View
Yes
Amazon Lex Model Building Service
GetImport
View
Yes
Amazon Lex Model Building Service
GetIntentVersions
View
Yes
Amazon Lex Model Building Service
GetIntents
View
Yes
Amazon Lex Model Building Service
GetMigration
View
Yes
Amazon Lex Model Building Service
GetMigrations
View
Yes
Amazon Lex Model Building Service
StartMigration
Start
Yes
Amazon Lex Model Building Service
GetSlotType
View
Yes
Amazon Lex Model Building Service
GetSlotTypeVersions
View
Yes
Amazon Lex Model Building Service
GetSlotTypes
View
Yes
Amazon Lex Model Building Service
GetUtterancesView
View
Yes
Amazon Lex Model Building Service
ListTagsForResource
View
Yes
Amazon Lex Model Building Service
TagResource
Create
Yes
Amazon Lex Model Building Service
PutBot
Edit
Yes
Amazon Lex Model Building Service
PutIntent
Edit
Yes
Amazon Lex Model Building Service
PutSlotType
Edit
Yes
Amazon Lex Model Building Service
StartImport
Start
Yes
Amazon Lex Model Building Service
UntagResource
Delete
Yes
Amazon FSx
AssociateFileSystemAliases
Create
Yes
Amazon FSx
CancelDataRepositoryTask
Delete
Yes
Amazon FSx
CopyBackup
Copy
Yes
Amazon FSx
CreateBackup
Create
Yes
Amazon FSx
CreateDataRepositoryTask
Create
Yes
Amazon FSx
CreateFileSystem
Create
Yes
Amazon FSx
CreateFileSystemFromBackup
Create
Yes
Amazon FSx
CreateStorageVirtualMachine
Create
Yes
Amazon FSx
CreateVolume
Create
Yes
Amazon FSx
CreateVolumeFromBackup
Create
Yes
Amazon FSx
DeleteBackup
Delete
Yes
Amazon FSx
DeleteFileSystem
Delete
Yes
Amazon FSx
DeleteStorageVirtualMachine
Delete
Yes
Amazon FSx
DeleteVolume
Delete
Yes
Amazon FSx
DescribeBackups
View
Yes
Amazon FSx
DescribeDataRepositoryTasks
View
Yes
Amazon FSx
DescribeFileSystemAliases
View
Yes
Amazon FSx
DescribeFileSystems
View
Yes
Amazon FSx
DescribeStorageVirtualMachines
View
Yes
Amazon FSx
DescribeVolumes
View
Yes
Amazon FSx
DisassociateFileSystemAliases
Delete
Yes
Amazon FSx
ListTagsForResource
View
Yes
Amazon FSx
TagResource
Create
Yes
Amazon FSx
UntagResource
Delete
Yes
Amazon FSx
UpdateFileSystem
Edit
Yes
Amazon FSx
UpdateStorageVirtualMachine
Edit
Yes
Amazon FSx
UpdateVolume
Edit
Yes
Amazon IoT
AcceptCertificateTransfer
Approve
Yes
Amazon IoT
AddThingToBillingGroup
Create
Yes
Amazon IoT
AddThingToThingGroup
Create
Yes
Amazon IoT
AssociateTargetsWithJob
Create
Yes
Amazon IoT
AttachPolicy
Attach
Yes
Amazon IoT
DetachPolicy
Delete
Yes
Amazon IoT
AttachPrincipalPolicy
Attach
Yes
Amazon IoT
DetachPrincipalPolicy
Delete
Yes
Amazon IoT
AttachSecurityProfile
Attach
Yes
Amazon IoT
DetachSecurityProfile
Delete
Yes
Amazon IoT
AttachThingPrincipal
Attach
Yes
Amazon IoT
DetachThingPrincipal
Delete
Yes
Amazon IoT
CancelAuditMitigationActionsTask
Delete
Yes
Amazon IoT
CancelAuditTask
Delete
Yes
Amazon IoT
CancelCertificateTransfer
Delete
Yes
Amazon IoT
CancelDetectMitigationActionsTask
Delete
Yes
Amazon IoT
CancelJob
Delete
Yes
Amazon IoT
CancelJobExecution
Delete
Yes
Amazon IoT
ClearDefaultAuthorizer
Delete
Yes
Amazon IoT
DescribeDefaultAuthorizer
View
Yes
Amazon IoT
SetDefaultAuthorizer
Create
Yes
Amazon IoT
ConfirmTopicRuleDestination
View
Yes
Amazon IoT
CreateAuditSuppression
Create
Yes
Amazon IoT
CreateAuthorizer
Create
Yes
Amazon IoT
DeleteAuthorizer
Delete
Yes
Amazon IoT
DescribeAuthorizer
View
Yes
Amazon IoT
UpdateAuthorizer
Edit
Yes
Amazon IoT
CreateBillingGroup
Create
Yes
Amazon IoT
DeleteBillingGroup
Delete
Yes
Amazon IoT
DescribeBillingGroup
View
Yes
Amazon IoT
UpdateBillingGroup
Edit
Yes
Amazon IoT
CreateCertificateFromCsr
Create
Yes
Amazon IoT
ListCertificates
View
Yes
Amazon IoT
CreateCustomMetric
Create
Yes
Amazon IoT
DeleteCustomMetric
Delete
Yes
Amazon IoT
DescribeCustomMetric
View
Yes
Amazon IoT
UpdateCustomMetric
Edit
Yes
Amazon IoT
CreateDimension
Create
Yes
Amazon IoT
DeleteDimension
Delete
Yes
Amazon IoT
DescribeDimension
View
Yes
Amazon IoT
UpdateDimension
Edit
Yes
Amazon IoT
CreateDomainConfiguration
Create
Yes
Amazon IoT
DeleteDomainConfiguration
Delete
Yes
Amazon IoT
DescribeDomainConfiguration
View
Yes
Amazon IoT
UpdateDomainConfiguration
Edit
Yes
Amazon IoT
CreateDynamicThingGroup
Create
Yes
Amazon IoT
DeleteDynamicThingGroup
Delete
Yes
Amazon IoT
UpdateDynamicThingGroup
Edit
Yes
Amazon IoT
CreateFleetMetric
Create
Yes
Amazon IoT
DeleteFleetMetric
Delete
Yes
Amazon IoT
DescribeFleetMetric
View
Yes
Amazon IoT
UpdateFleetMetric
Edit
Yes
Amazon IoT
CreateJob
Create
Yes
Amazon IoT
DeleteJob
Delete
Yes
Amazon IoT
DescribeJob
View
Yes
Amazon IoT
UpdateJob
Edit
Yes
Amazon IoT
CreateJobTemplate
Create
Yes
Amazon IoT
DeleteJobTemplate
Delete
Yes
Amazon IoT
DescribeJobTemplate
View
Yes
Amazon IoT
CreateKeysAndCertificate
Create
Yes
Amazon IoT
CreateMitigationAction
Create
Yes
Amazon IoT
DeleteMitigationAction
Delete
Yes
Amazon IoT
DescribeMitigationAction
View
Yes
Amazon IoT
UpdateMitigationAction
Edit
Yes
Amazon IoT
CreateOTAUpdate
Create
Yes
Amazon IoT
DeleteOTAUpdate
Delete
Yes
Amazon IoT
GetOTAUpdate
View
Yes
Amazon IoT
CreatePolicy
Create
Yes
Amazon IoT
DeletePolicy
Delete
Yes
Amazon IoT
GetPolicy
View
Yes
Amazon IoT
CreatePolicyVersion
Create
Yes
Amazon IoT
ListPolicyVersions
View
Yes
Amazon IoT
CreateProvisioningClaim
Create
Yes
Amazon IoT
CreateProvisioningTemplate
Create
Yes
Amazon IoT
ListProvisioningTemplates
View
Yes
Amazon IoT
CreateProvisioningTemplateVersion
Create
Yes
Amazon IoT
ListProvisioningTemplateVersions
View
Yes
Amazon IoT
CreateRoleAlias
Create
Yes
Amazon IoT
DeleteRoleAlias
Delete
Yes
Amazon IoT
DescribeRoleAlias
View
Yes
Amazon IoT
UpdateRoleAlias
Edit
Yes
Amazon IoT
CreateScheduledAudit
Create
Yes
Amazon IoT
DeleteScheduledAudit
Delete
Yes
Amazon IoT
DescribeScheduledAudit
View
Yes
Amazon IoT
UpdateScheduledAudit
Edit
Yes
Amazon IoT
CreateSecurityProfile
Create
Yes
Amazon IoT
DeleteSecurityProfile
Delete
Yes
Amazon IoT
DescribeSecurityProfile
View
Yes
Amazon IoT
UpdateSecurityProfile
Edit
Yes
Amazon IoT
CreateStream
Create
Yes
Amazon IoT
DeleteStream
Delete
Yes
Amazon IoT
DescribeStream
View
Yes
Amazon IoT
UpdateStream
Edit
Yes
Amazon IoT
CreateThing
Create
Yes
Amazon IoT
DeleteThing
Delete
Yes
Amazon IoT
DescribeThing
View
Yes
Amazon IoT
UpdateThing
Edit
Yes
Amazon IoT
CreateThingGroup
Create
Yes
Amazon IoT
DeleteThingGroup
Delete
Yes
Amazon IoT
DescribeThingGroup
View
Yes
Amazon IoT
UpdateThingGroup
Edit
Yes
Amazon IoT
CreateThingType
Create
Yes
Amazon IoT
DeleteThingType
Delete
Yes
Amazon IoT
DescribeThingType
View
Yes
Amazon IoT
CreateTopicRule
Create
Yes
Amazon IoT
DeleteTopicRule
Delete
Yes
Amazon IoT
GetTopicRule
View
Yes
Amazon IoT
ReplaceTopicRule
Create
Yes
Amazon IoT
CreateTopicRuleDestination
Create
Yes
Amazon IoT
ListTopicRuleDestinations
View
Yes
Amazon IoT
UpdateTopicRuleDestination
Edit
Yes
Amazon IoT
DeleteAccountAuditConfiguration
Delete
Yes
Amazon IoT
DescribeAccountAuditConfiguration
View
Yes
Amazon IoT
UpdateAccountAuditConfiguration
Edit
Yes
Amazon IoT
DeleteAuditSuppression
Delete
Yes
Amazon IoT
DeleteCACertificate
Delete
Yes
Amazon IoT
DescribeCACertificate
View
Yes
Amazon IoT
UpdateCACertificate
Edit
Yes
Amazon IoT
DeleteCertificate
Delete
Yes
Amazon IoT
DescribeCertificate
View
Yes
Amazon IoT
DeleteJobExecution
Delete
Yes
Amazon IoT
DeletePolicyVersion
Delete
Yes
Amazon IoT
GetPolicyVersion
View
Yes
Amazon IoT
SetDefaultPolicyVersion
Create
Yes
Amazon IoT
DeleteProvisioningTemplate
Delete
Yes
Amazon IoT
DescribeProvisioningTemplate
View
Yes
Amazon IoT
UpdateProvisioningTemplate
Edit
Yes
Amazon IoT
DeleteProvisioningTemplateVersion
Delete
Yes
Amazon IoT
DescribeProvisioningTemplateVersion
View
Yes
Amazon IoT
DeleteRegistrationCode
Delete
Yes
Amazon IoT
GetRegistrationCode
View
Yes
Amazon IoT
DeleteTopicRuleDestination
Delete
Yes
Amazon IoT
GetTopicRuleDestination
View
Yes
Amazon IoT
DeleteVLoggingLevel
Delete
Yes
Amazon IoT
DeprecateThingType
Delete
Yes
Amazon IoT
DescribeAuditFinding
View
Yes
Amazon IoT
DescribeAuditMitigationActionsTask
View
Yes
Amazon IoT
StartAuditMitigationActionsTask
Start
Yes
Amazon IoT
DescribeAuditSuppression
View
Yes
Amazon IoT
DescribeAuditTask
View
Yes
Amazon IoT
DescribeDetectMitigationActionsTask
View
Yes
Amazon IoT
StartDetectMitigationActionsTask
Start
Yes
Amazon IoT
DescribeEndpoint
View
Yes
Amazon IoT
DescribeEventConfigurations
View
Yes
Amazon IoT
UpdateEventConfigurations
Edit
Yes
Amazon IoT
DescribeIndex
View
Yes
Amazon IoT
DescribeJobExecution
View
Yes
Amazon IoT
DescribeThingRegistrationTask
View
Yes
Amazon IoT
DisableTopicRule
Edit
Yes
Amazon IoT
EnableTopicRule
Enable
Yes
Amazon IoT
GetBehaviorModelTrainingSummaries
View
Yes
Amazon IoT
GetBucketsAggregation
View
Yes
Amazon IoT
GetCardinality
View
Yes
Amazon IoT
GetEffectivePolicies
View
Yes
Amazon IoT
GetIndexingConfiguration
View
Yes
Amazon IoT
UpdateIndexingConfiguration
Edit
Yes
Amazon IoT
GetJobDocument
View
Yes
Amazon IoT
GetLoggingOptions
View
Yes
Amazon IoT
SetLoggingOptions
Create
Yes
Amazon IoT
GetPercentiles
View
Yes
Amazon IoT
GetStatistics
View
Yes
Amazon IoT
GetVLoggingOptions
View
Yes
Amazon IoT
SetVLoggingOptions
Create
Yes
Amazon IoT
ListActiveViolations
View
Yes
Amazon IoT
ListAttachedPolicies
View
Yes
Amazon IoT
ListAuditFindings
View
Yes
Amazon IoT
ListAuditMitigationActionsExecutions
View
Yes
Amazon IoT
ListAuditMitigationActionsTasks
View
Yes
Amazon IoT
ListAuditSuppressions
View
Yes
Amazon IoT
ListAuditTasks
View
Yes
Amazon IoT
ListAuthorizers
View
Yes
Amazon IoT
ListBillingGroups
View
Yes
Amazon IoT
ListCACertificates
View
Yes
Amazon IoT
ListCertificatesByCA
View
Yes
Amazon IoT
ListCustomMetrics
View
Yes
Amazon IoT
ListDetectMitigationActionsExecutions
View
Yes
Amazon IoT
ListDetectMitigationActionsTasks
View
Yes
Amazon IoT
ListDimensions
View
Yes
Amazon IoT
ListDomainConfigurations
View
Yes
Amazon IoT
ListFleetMetrics
View
Yes
Amazon IoT
ListIndices
View
Yes
Amazon IoT
ListJobExecutionsForJob
View
Yes
Amazon IoT
ListJobExecutionsForThing
View
Yes
Amazon IoT
ListJobTemplates
View
Yes
Amazon IoT
ListJobs
View
Yes
Amazon IoT
ListMitigationActions
View
Yes
Amazon IoT
ListOTAUpdates
View
Yes
Amazon IoT
ListOutgoingCertificates
View
Yes
Amazon IoT
ListPolicies
View
Yes
Amazon IoT
ListPolicyPrincipals
View
Yes
Amazon IoT
ListPrincipalPolicies
View
Yes
Amazon IoT
ListPrincipalThings
View
Yes
Amazon IoT
ListRoleAliases
View
Yes
Amazon IoT
ListScheduledAudits
View
Yes
Amazon IoT
ListSecurityProfiles
View
Yes
Amazon IoT
ListSecurityProfilesForTarget
View
Yes
Amazon IoT
ListStreams
View
Yes
Amazon IoT
ListTagsForResource
View
Yes
Amazon IoT
ListTargetsForPolicy
View
Yes
Amazon IoT
ListTargetsForSecurityProfile
View
Yes
Amazon IoT
ListThingGroups
View
Yes
Amazon IoT
ListThingGroupsForThing
View
Yes
Amazon IoT
ListThingPrincipals
View
Yes
Amazon IoT
ListThingRegistrationTaskReports
View
Yes
Amazon IoT
ListThingRegistrationTasks
View
Yes
Amazon IoT
StartThingRegistrationTask
Start
Yes
Amazon IoT
ListThingTypes
View
Yes
Amazon IoT
ListThings
View
Yes
Amazon IoT
RegisterThing
Register
Yes
Amazon IoT
ListThingsInBillingGroup
View
Yes
Amazon IoT
ListThingsInThingGroup
View
Yes
Amazon IoT
ListTopicRules
View
Yes
Amazon IoT
ListVLoggingLevels
View
Yes
Amazon IoT
SetVLoggingLevel
Create
Yes
Amazon IoT
ListViolationEvents
View
Yes
Amazon IoT
RegisterCACertificate
Register
Yes
Amazon IoT
RegisterCertificate
Register
Yes
Amazon IoT
RegisterCertificateWithoutCA
Register
Yes
Amazon IoT
RejectCertificateTransfer
Reject
Yes
Amazon IoT
RemoveThingFromBillingGroup
Delete
Yes
Amazon IoT
RemoveThingFromThingGroup
Delete
Yes
Amazon IoT
SearchIndex
Search
Yes
Amazon IoT
StartOnDemandAuditTask
Start
Yes
Amazon IoT
StopThingRegistrationTask
Stop
Yes
Amazon IoT
TagResource
Create
Yes
Amazon IoT
TestAuthorization
Create
Yes
Amazon IoT
TestInvokeAuthorizer
Create
Yes
Amazon IoT
TransferCertificate
Edit
Yes
Amazon IoT
UntagResource
Delete
Yes
Amazon IoT
UpdateAuditSuppression
Edit
Yes
Amazon IoT
UpdateCertificate
Edit
Yes
Amazon IoT
UpdateThingGroupsForThing
Edit
Yes
Amazon IoT
ValidateSecurityProfileBehaviors
Create
Yes
Amazon Mobile Analytics
PutEvents
Edit
Yes
Amazon RDS DataService
ExecuteStatement
Create
Yes
Amazon RDS DataService
BeginTransaction
Create
Yes
Amazon RDS DataService
CommitTransaction
Create
Yes
Amazon RDS DataService
ExecuteSql
Create
Yes
Amazon RDS DataService
RollbackTransaction
Create
Yes
Amazon Certificate Manager Private Certificate Authority
CreateCertificateAuthority
Create
Yes
Amazon Certificate Manager Private Certificate Authority
CreateCertificateAuthorityAuditReport
Create
Yes
Amazon Certificate Manager Private Certificate Authority
CreatePermission
Create
Yes
Amazon Certificate Manager Private Certificate Authority
DeleteCertificateAuthority
Delete
Yes
Amazon Certificate Manager Private Certificate Authority
DeletePermission
Delete
Yes
Amazon Certificate Manager Private Certificate Authority
DeletePolicy
Delete
Yes
Amazon Certificate Manager Private Certificate Authority
DescribeCertificateAuthority
View
Yes
Amazon Certificate Manager Private Certificate Authority
DescribeCertificateAuthorityAuditReport
View
Yes
Amazon Certificate Manager Private Certificate Authority
GetCertificate
View
Yes
Amazon Certificate Manager Private Certificate Authority
GetCertificateAuthorityCertificate
View
Yes
Amazon Certificate Manager Private Certificate Authority
GetCertificateAuthorityCsr
View
Yes
Amazon Certificate Manager Private Certificate Authority
GetPolicy
View
Yes
Amazon Certificate Manager Private Certificate Authority
ImportCertificateAuthorityCertificate
Create
Yes
Amazon Certificate Manager Private Certificate Authority
IssueCertificate
Create
Yes
Amazon Certificate Manager Private Certificate Authority
ListCertificateAuthorities
View
Yes
Amazon Certificate Manager Private Certificate Authority
ListPermissions
View
Yes
Amazon Certificate Manager Private Certificate Authority
ListTags
View
Yes
Amazon Certificate Manager Private Certificate Authority
PutPolicy
Edit
Yes
Amazon Certificate Manager Private Certificate Authority
RestoreCertificateAuthority
Create
Yes
Amazon Certificate Manager Private Certificate Authority
RevokeCertificate
Delete
Yes
Amazon Certificate Manager Private Certificate Authority
TagCertificateAuthority
Create
Yes
Amazon Certificate Manager Private Certificate Authority
UntagCertificateAuthority
Delete
Yes
Amazon Certificate Manager Private Certificate Authority
UpdateCertificateAuthority
Edit
Yes
Amazon Alexa For Business
ApproveSkill
Approve
Yes
Amazon Alexa For Business
AssociateContactWithAddressBook
Create
Yes
Amazon Alexa For Business
AssociateDeviceWithNetworkProfile
Create
Yes
Amazon Alexa For Business
AssociateDeviceWithRoom
Create
Yes
Amazon Alexa For Business
AssociateSkillGroupWithRoom
Create
Yes
Amazon Alexa For Business
AssociateSkillWithSkillGroup
Create
Yes
Amazon Alexa For Business
AssociateSkillWithUsers
Create
Yes
Amazon Alexa For Business
CreateAddressBook
Create
Yes
Amazon Alexa For Business
CreateBusinessReportSchedule
Create
Yes
Amazon Alexa For Business
CreateConferenceProvider
Create
Yes
Amazon Alexa For Business
CreateContact
Create
Yes
Amazon Alexa For Business
CreateGatewayGroup
Create
Yes
Amazon Alexa For Business
CreateNetworkProfile
Create
Yes
Amazon Alexa For Business
CreateProfile
Create
Yes
Amazon Alexa For Business
CreateRoom
Create
Yes
Amazon Alexa For Business
CreateSkillGroup
Create
Yes
Amazon Alexa For Business
CreateUser
Create
Yes
Amazon Alexa For Business
DeleteAddressBook
Delete
Yes
Amazon Alexa For Business
DeleteBusinessReportSchedule
Delete
Yes
Amazon Alexa For Business
DeleteConferenceProvider
Delete
Yes
Amazon Alexa For Business
DeleteContact
Delete
Yes
Amazon Alexa For Business
DeleteDevice
Delete
Yes
Amazon Alexa For Business
DeleteDeviceUsageData
Delete
Yes
Amazon Alexa For Business
DeleteGatewayGroup
Delete
Yes
Amazon Alexa For Business
DeleteNetworkProfile
Delete
Yes
Amazon Alexa For Business
DeleteProfile
Delete
Yes
Amazon Alexa For Business
DeleteRoom
Delete
Yes
Amazon Alexa For Business
DeleteRoomSkillParameter
Delete
Yes
Amazon Alexa For Business
DeleteSkillAuthorization
Delete
Yes
Amazon Alexa For Business
DeleteSkillGroup
Delete
Yes
Amazon Alexa For Business
DeleteUser
Delete
Yes
Amazon Alexa For Business
DisassociateContactFromAddressBook
Delete
Yes
Amazon Alexa For Business
DisassociateDeviceFromRoom
Delete
Yes
Amazon Alexa For Business
DisassociateSkillFromSkillGroup
Delete
Yes
Amazon Alexa For Business
DisassociateSkillFromUsers
Delete
Yes
Amazon Alexa For Business
DisassociateSkillGroupFromRoom
Delete
Yes
Amazon Alexa For Business
ForgetSmartHomeAppliances
Create
Yes
Amazon Alexa For Business
GetAddressBook
View
Yes
Amazon Alexa For Business
GetConferencePreference
View
Yes
Amazon Alexa For Business
GetConferenceProvider
View
Yes
Amazon Alexa For Business
GetContact
View
Yes
Amazon Alexa For Business
GetDevice
View
Yes
Amazon Alexa For Business
GetGateway
View
Yes
Amazon Alexa For Business
GetGatewayGroup
View
Yes
Amazon Alexa For Business
GetInvitationConfiguration
View
Yes
Amazon Alexa For Business
GetNetworkProfile
View
Yes
Amazon Alexa For Business
GetProfile
View
Yes
Amazon Alexa For Business
GetRoom
View
Yes
Amazon Alexa For Business
GetRoomSkillParameter
View
Yes
Amazon Alexa For Business
GetSkillGroup
View
Yes
Amazon Alexa For Business
ListBusinessReportSchedules
View
Yes
Amazon Alexa For Business
ListConferenceProviders
View
Yes
Amazon Alexa For Business
ListDeviceEvents
View
Yes
Amazon Alexa For Business
ListGatewayGroups
View
Yes
Amazon Alexa For Business
ListGateways
View
Yes
Amazon Alexa For Business
ListSkills
View
Yes
Amazon Alexa For Business
ListSkillsStoreCategories
View
Yes
Amazon Alexa For Business
ListSkillsStoreSkillsByCategory
View
Yes
Amazon Alexa For Business
ListSmartHomeAppliances
View
Yes
Amazon Alexa For Business
ListTags
View
Yes
Amazon Alexa For Business
PutConferencePreference
Edit
Yes
Amazon Alexa For Business
PutInvitationConfiguration
Edit
Yes
Amazon Alexa For Business
PutRoomSkillParameter
Edit
Yes
Amazon Alexa For Business
PutSkillAuthorization
Edit
Yes
Amazon Alexa For Business
RegisterAVSDevice
Register
Yes
Amazon Alexa For Business
RejectSkill
Reject
Yes
Amazon Alexa For Business
ResolveRoom
Create
Yes
Amazon Alexa For Business
RevokeInvitation
Delete
Yes
Amazon Alexa For Business
SearchAddressBooks
Search
Yes
Amazon Alexa For Business
SearchContacts
Search
Yes
Amazon Alexa For Business
SearchDevices
Search
Yes
Amazon Alexa For Business
SearchNetworkProfiles
Search
Yes
Amazon Alexa For Business
SearchProfiles
Search
Yes
Amazon Alexa For Business
SearchRooms
Search
Yes
Amazon Alexa For Business
SearchSkillGroups
Search
Yes
Amazon Alexa For Business
SearchUsers
Search
Yes
Amazon Alexa For Business
SendAnnouncement
Send
Yes
Amazon Alexa For Business
SendInvitation
Send
Yes
Amazon Alexa For Business
StartDeviceSync
Start
Yes
Amazon Alexa For Business
StartSmartHomeApplianceDiscovery
Start
Yes
Amazon Alexa For Business
TagResource
Create
Yes
Amazon Alexa For Business
UntagResource
Delete
Yes
Amazon Alexa For Business
UpdateAddressBook
Edit
Yes
Amazon Alexa For Business
UpdateBusinessReportSchedule
Edit
Yes
Amazon Alexa For Business
UpdateConferenceProvider
Edit
Yes
Amazon Alexa For Business
UpdateContact
Edit
Yes
Amazon Alexa For Business
UpdateDevice
Edit
Yes
Amazon Alexa For Business
UpdateGateway
Edit
Yes
Amazon Alexa For Business
UpdateGatewayGroup
Edit
Yes
Amazon Alexa For Business
UpdateNetworkProfile
Edit
Yes
Amazon Alexa For Business
UpdateProfile
Edit
Yes
Amazon Alexa For Business
UpdateRoom
Edit
Yes
Amazon Alexa For Business
UpdateSkillGroup
Edit
Yes
Amazon AppIntegrations Service
CreateEventIntegration
Create
Yes
Amazon AppIntegrations Service
ListEventIntegrations
View
Yes
Amazon AppIntegrations Service
DeleteEventIntegration
Delete
Yes
Amazon AppIntegrations Service
GetEventIntegration
View
Yes
Amazon AppIntegrations Service
UpdateEventIntegration
Edit
Yes
Amazon AppIntegrations Service
ListEventIntegrationAssociations
View
Yes
Amazon AppIntegrations Service
ListTagsForResource
View
Yes
Amazon AppIntegrations Service
TagResource
Create
Yes
Amazon AppIntegrations Service
UntagResource
Delete
Yes
Amazon Athena
GetNamedQuery
View
Yes
Amazon Athena
GetQueryExecution
View
Yes
Amazon Athena
CreateDataCatalog
Create
Yes
Amazon Athena
CreateNamedQuery
Create
Yes
Amazon Athena
CreatePreparedStatement
Create
Yes
Amazon Athena
CreateWorkGroup
Create
Yes
Amazon Athena
DeleteDataCatalog
Delete
Yes
Amazon Athena
DeleteNamedQuery
Delete
Yes
Amazon Athena
DeletePreparedStatement
Delete
Yes
Amazon Athena
DeleteWorkGroup
Delete
Yes
Amazon Athena
GetDataCatalog
View
Yes
Amazon Athena
GetDatabase
View
Yes
Amazon Athena
GetPreparedStatement
View
Yes
Amazon Athena
GetQueryResults
View
Yes
Amazon Athena
GetTableMetadata
View
Yes
Amazon Athena
GetWorkGroup
View
Yes
Amazon Athena
ListDataCatalogs
View
Yes
Amazon Athena
ListDatabases
View
Yes
Amazon Athena
ListEngineVersions
View
Yes
Amazon Athena
ListNamedQueries
View
Yes
Amazon Athena
ListPreparedStatements
View
Yes
Amazon Athena
ListQueryExecutions
View
Yes
Amazon Athena
ListTableMetadata
View
Yes
Amazon Athena
ListTagsForResource
View
Yes
Amazon Athena
ListWorkGroups
View
Yes
Amazon Athena
StartQueryExecution
Start
Yes
Amazon Athena
StopQueryExecution
Stop
Yes
Amazon Athena
TagResource
Create
Yes
Amazon Athena
UntagResource
Delete
Yes
Amazon Athena
UpdateDataCatalog
Edit
Yes
Amazon Athena
UpdatePreparedStatement
Edit
Yes
Amazon Athena
UpdateWorkGroup
Edit
Yes
Amazon Data Exchange
CancelJob
Delete
Yes
Amazon Data Exchange
GetJob
View
Yes
Amazon Data Exchange
StartJob
Start
Yes
Amazon Data Exchange
CreateDataSet
Create
Yes
Amazon Data Exchange
ListDataSets
View
Yes
Amazon Data Exchange
CreateJob
Create
Yes
Amazon Data Exchange
ListJobs
View
Yes
Amazon Data Exchange
CreateRevision
Create
Yes
Amazon Data Exchange
ListDataSetRevisions
View
Yes
Amazon Data Exchange
DeleteAsset
Delete
Yes
Amazon Data Exchange
GetAsset
View
Yes
Amazon Data Exchange
UpdateAsset
Edit
Yes
Amazon Data Exchange
DeleteDataSet
Delete
Yes
Amazon Data Exchange
GetDataSet
View
Yes
Amazon Data Exchange
UpdateDataSet
Edit
Yes
Amazon Data Exchange
DeleteRevision
Delete
Yes
Amazon Data Exchange
GetRevision
View
Yes
Amazon Data Exchange
UpdateRevision
Edit
Yes
Amazon Data Exchange
ListRevisionAssets
View
Yes
Amazon Data Exchange
ListTagsForResource
View
Yes
Amazon Data Exchange
TagResource
Create
Yes
Amazon Data Exchange
UntagResource
Delete
Yes
Amazon Single Sign-On Admin
AttachManagedPolicyToPermissionSet
Attach
Yes
Amazon Single Sign-On Admin
CreateAccountAssignment
Create
Yes
Amazon Single Sign-On Admin
CreateInstanceAccessControlAttributeConfiguration
Create
Yes
Amazon Single Sign-On Admin
CreatePermissionSet
Create
Yes
Amazon Single Sign-On Admin
DeleteAccountAssignment
Delete
Yes
Amazon Single Sign-On Admin
DeleteInlinePolicyFromPermissionSet
Delete
Yes
Amazon Single Sign-On Admin
DeleteInstanceAccessControlAttributeConfiguration
Delete
Yes
Amazon Single Sign-On Admin
DeletePermissionSet
Delete
Yes
Amazon Single Sign-On Admin
DescribeAccountAssignmentCreationStatus
View
Yes
Amazon Single Sign-On Admin
DescribeAccountAssignmentDeletionStatus
View
Yes
Amazon Single Sign-On Admin
DescribeInstanceAccessControlAttributeConfiguration
View
Yes
Amazon Single Sign-On Admin
DescribePermissionSet
View
Yes
Amazon Single Sign-On Admin
DescribePermissionSetProvisioningStatus
View
Yes
Amazon Single Sign-On Admin
DetachManagedPolicyFromPermissionSet
Delete
Yes
Amazon Single Sign-On Admin
GetInlinePolicyForPermissionSet
View
Yes
Amazon Single Sign-On Admin
ListAccountAssignmentCreationStatus
View
Yes
Amazon Single Sign-On Admin
ListAccountAssignmentDeletionStatus
View
Yes
Amazon Single Sign-On Admin
ListAccountAssignments
View
Yes
Amazon Single Sign-On Admin
ListAccountsForProvisionedPermissionSet
View
Yes
Amazon Single Sign-On Admin
ListInstances
View
Yes
Amazon Single Sign-On Admin
ListManagedPoliciesInPermissionSet
View
Yes
Amazon Single Sign-On Admin
ListPermissionSetProvisioningStatus
View
Yes
Amazon Single Sign-On Admin
ListPermissionSets
View
Yes
Amazon Single Sign-On Admin
ListPermissionSetsProvisionedToAccount
View
Yes
Amazon Single Sign-On Admin
ListTagsForResource
View
Yes
Amazon Single Sign-On Admin
ProvisionPermissionSet
Create
Yes
Amazon Single Sign-On Admin
PutInlinePolicyToPermissionSet
Edit
Yes
Amazon Single Sign-On Admin
TagResource
Create
Yes
Amazon Single Sign-On Admin
UntagResource
Delete
Yes
Amazon Single Sign-On Admin
UpdateInstanceAccessControlAttributeConfiguration
Edit
Yes
Amazon Single Sign-On Admin
UpdatePermissionSet
Edit
Yes
Amazon Simple Workflow Service
CountClosedWorkflowExecutions
Create
Yes
Amazon Simple Workflow Service
CountOpenWorkflowExecutions
Create
Yes
Amazon Simple Workflow Service
CountPendingActivityTasks
Create
Yes
Amazon Simple Workflow Service
CountPendingDecisionTasks
Create
Yes
Amazon Simple Workflow Service
DeprecateActivityType
Delete
Yes
Amazon Simple Workflow Service
DeprecateDomain
Delete
Yes
Amazon Simple Workflow Service
DeprecateWorkflowType
Delete
Yes
Amazon Simple Workflow Service
DescribeActivityType
View
Yes
Amazon Simple Workflow Service
DescribeDomain
View
Yes
Amazon Simple Workflow Service
DescribeWorkflowExecution
View
Yes
Amazon Simple Workflow Service
DescribeWorkflowType
View
Yes
Amazon Simple Workflow Service
GetWorkflowExecutionHistory
View
Yes
Amazon Simple Workflow Service
ListActivityTypes
View
Yes
Amazon Simple Workflow Service
ListClosedWorkflowExecutions
View
Yes
Amazon Simple Workflow Service
ListDomains
View
Yes
Amazon Simple Workflow Service
ListOpenWorkflowExecutions
View
Yes
Amazon Simple Workflow Service
ListTagsForResource
View
Yes
Amazon Simple Workflow Service
ListWorkflowTypes
View
Yes
Amazon Simple Workflow Service
PollForActivityTask
Create
Yes
Amazon Simple Workflow Service
PollForDecisionTask
Create
Yes
Amazon Simple Workflow Service
RecordActivityTaskHeartbeat
Create
Yes
Amazon Simple Workflow Service
RegisterActivityType
Register
Yes
Amazon Simple Workflow Service
RegisterDomain
Register
Yes
Amazon Simple Workflow Service
RegisterWorkflowType
Register
Yes
Amazon Simple Workflow Service
RequestCancelWorkflowExecution
Create
Yes
Amazon Simple Workflow Service
RespondActivityTaskCanceled
Create
Yes
Amazon Simple Workflow Service
RespondActivityTaskCompleted
Create
Yes
Amazon Simple Workflow Service
RespondActivityTaskFailed
Create
Yes
Amazon Simple Workflow Service
RespondDecisionTaskCompleted
Create
Yes
Amazon Simple Workflow Service
SignalWorkflowExecution
Create
Yes
Amazon Simple Workflow Service
StartWorkflowExecution
Start
Yes
Amazon Simple Workflow Service
TagResource
Create
Yes
Amazon Simple Workflow Service
TerminateWorkflowExecution
Terminate
Yes
Amazon Simple Workflow Service
UndeprecateActivityType
Create
Yes
Amazon Simple Workflow Service
UndeprecateDomain
Create
Yes
Amazon Simple Workflow Service
UndeprecateWorkflowType
Create
Yes
Amazon Simple Workflow Service
UntagResource
Delete
Yes
Amazon Chime SDK Identity
CreateAppInstance
Create
Yes
Amazon Chime SDK Identity
ListAppInstances
View
Yes
Amazon Chime SDK Identity
CreateAppInstanceAdmin
Create
Yes
Amazon Chime SDK Identity
ListAppInstanceAdmins
View
Yes
Amazon Chime SDK Identity
CreateAppInstanceUser
Create
Yes
Amazon Chime SDK Identity
DeleteAppInstance
Delete
Yes
Amazon Chime SDK Identity
DescribeAppInstance
View
Yes
Amazon Chime SDK Identity
UpdateAppInstance
Edit
Yes
Amazon Chime SDK Identity
DeleteAppInstanceAdmin
Delete
Yes
Amazon Chime SDK Identity
DescribeAppInstanceAdmin
View
Yes
Amazon Chime SDK Identity
DeleteAppInstanceUser
Delete
Yes
Amazon Chime SDK Identity
DescribeAppInstanceUser
View
Yes
Amazon Chime SDK Identity
UpdateAppInstanceUser
Edit
Yes
Amazon Chime SDK Identity
GetAppInstanceRetentionSettings
View
Yes
Amazon Chime SDK Identity
PutAppInstanceRetentionSettings
Edit
Yes
Amazon Chime SDK Identity
ListAppInstanceUsers
View
Yes
Amazon Lookout for Equipment
CreateDataset
Create
Yes
Amazon Lookout for Equipment
CreateInferenceScheduler
Create
Yes
Amazon Lookout for Equipment
CreateModel
Create
Yes
Amazon Lookout for Equipment
DeleteDataset
Delete
Yes
Amazon Lookout for Equipment
DeleteInferenceScheduler
Delete
Yes
Amazon Lookout for Equipment
DeleteModel
Delete
Yes
Amazon Lookout for Equipment
DescribeDataIngestionJob
View
Yes
Amazon Lookout for Equipment
DescribeDataset
View
Yes
Amazon Lookout for Equipment
DescribeInferenceScheduler
View
Yes
Amazon Lookout for Equipment
DescribeModel
View
Yes
Amazon Lookout for Equipment
ListDataIngestionJobs
View
Yes
Amazon Lookout for Equipment
ListDatasets
View
Yes
Amazon Lookout for Equipment
ListInferenceExecutions
View
Yes
Amazon Lookout for Equipment
ListInferenceSchedulers
View
Yes
Amazon Lookout for Equipment
ListModels
View
Yes
Amazon Lookout for Equipment
ListTagsForResource
View
Yes
Amazon Lookout for Equipment
StartDataIngestionJob
Start
Yes
Amazon Lookout for Equipment
StartInferenceScheduler
Start
Yes
Amazon Lookout for Equipment
StopInferenceScheduler
Stop
Yes
Amazon Lookout for Equipment
TagResource
Create
Yes
Amazon Lookout for Equipment
UntagResource
Delete
Yes
Amazon Lookout for Equipment
UpdateInferenceScheduler
Edit
Yes
Amazon IoT Data Plane
DeleteThingShadow
Delete
Yes
Amazon IoT Data Plane
GetThingShadow
View
Yes
Amazon IoT Data Plane
UpdateThingShadow
Edit
Yes
Amazon IoT Data Plane
GetRetainedMessage
View
Yes
Amazon IoT Data Plane
ListNamedShadowsForThing
View
Yes
Amazon IoT Data Plane
ListRetainedMessages
View
Yes
Amazon IoT Data Plane
Publish
Create
Yes
Amazon QuickSight
CancelIngestion
Delete
Yes
Amazon QuickSight
CreateIngestion
Create
Yes
Amazon QuickSight
DescribeIngestion
View
Yes
Amazon QuickSight
CreateAccountCustomization
Create
Yes
Amazon QuickSight
DeleteAccountCustomization
Delete
Yes
Amazon QuickSight
DescribeAccountCustomization
View
Yes
Amazon QuickSight
UpdateAccountCustomization
Edit
Yes
Amazon QuickSight
CreateAnalysis
Create
Yes
Amazon QuickSight
DeleteAnalysis
Delete
Yes
Amazon QuickSight
DescribeAnalysis
View
Yes
Amazon QuickSight
UpdateAnalysis
Edit
Yes
Amazon QuickSight
CreateDashboard
Create
Yes
Amazon QuickSight
DeleteDashboard
Delete
Yes
Amazon QuickSight
DescribeDashboard
View
Yes
Amazon QuickSight
UpdateDashboard
Edit
Yes
Amazon QuickSight
CreateDataSet
Create
Yes
Amazon QuickSight
ListDataSets
View
Yes
Amazon QuickSight
CreateDataSource
Create
Yes
Amazon QuickSight
ListDataSources
View
Yes
Amazon QuickSight
CreateFolder
Create
Yes
Amazon QuickSight
DeleteFolder
Delete
Yes
Amazon QuickSight
DescribeFolder
View
Yes
Amazon QuickSight
UpdateFolder
Edit
Yes
Amazon QuickSight
CreateFolderMembership
Create
Yes
Amazon QuickSight
DeleteFolderMembership
Delete
Yes
Amazon QuickSight
CreateGroup
Create
Yes
Amazon QuickSight
ListGroups
View
Yes
Amazon QuickSight
CreateGroupMembership
Create
Yes
Amazon QuickSight
DeleteGroupMembership
Delete
Yes
Amazon QuickSight
CreateIAMPolicyAssignment
Create
Yes
Amazon QuickSight
CreateNamespace
Create
Yes
Amazon QuickSight
CreateTemplate
Create
Yes
Amazon QuickSight
DeleteTemplate
Delete
Yes
Amazon QuickSight
DescribeTemplate
View
Yes
Amazon QuickSight
UpdateTemplate
Edit
Yes
Amazon QuickSight
CreateTemplateAlias
Create
Yes
Amazon QuickSight
DeleteTemplateAlias
Delete
Yes
Amazon QuickSight
DescribeTemplateAlias
View
Yes
Amazon QuickSight
UpdateTemplateAlias
Edit
Yes
Amazon QuickSight
CreateTheme
Create
Yes
Amazon QuickSight
DeleteTheme
Delete
Yes
Amazon QuickSight
DescribeTheme
View
Yes
Amazon QuickSight
UpdateTheme
Edit
Yes
Amazon QuickSight
CreateThemeAlias
Create
Yes
Amazon QuickSight
DeleteThemeAlias
Delete
Yes
Amazon QuickSight
DescribeThemeAlias
View
Yes
Amazon QuickSight
UpdateThemeAlias
Edit
Yes
Amazon QuickSight
DeleteDataSet
Delete
Yes
Amazon QuickSight
DescribeDataSet
View
Yes
Amazon QuickSight
UpdateDataSet
Edit
Yes
Amazon QuickSight
DeleteDataSource
Delete
Yes
Amazon QuickSight
DescribeDataSource
View
Yes
Amazon QuickSight
UpdateDataSource
Edit
Yes
Amazon QuickSight
DeleteGroup
Delete
Yes
Amazon QuickSight
DescribeGroup
View
Yes
Amazon QuickSight
UpdateGroup
Edit
Yes
Amazon QuickSight
DeleteIAMPolicyAssignment
Delete
Yes
Amazon QuickSight
DeleteNamespace
Delete
Yes
Amazon QuickSight
DescribeNamespace
View
Yes
Amazon QuickSight
DeleteUser
Delete
Yes
Amazon QuickSight
DescribeUser
View
Yes
Amazon QuickSight
UpdateUser
Edit
Yes
Amazon QuickSight
DeleteUserByPrincipalId
Delete
Yes
Amazon QuickSight
DescribeAccountSettings
View
Yes
Amazon QuickSight
UpdateAccountSettings
Edit
Yes
Amazon QuickSight
DescribeAnalysisPermissions
View
Yes
Amazon QuickSight
UpdateAnalysisPermissions
Edit
Yes
Amazon QuickSight
DescribeDashboardPermissions
View
Yes
Amazon QuickSight
UpdateDashboardPermissions
Edit
Yes
Amazon QuickSight
DescribeDataSetPermissions
View
Yes
Amazon QuickSight
UpdateDataSetPermissions
Edit
Yes
Amazon QuickSight
DescribeDataSourcePermissions
View
Yes
Amazon QuickSight
UpdateDataSourcePermissions
Edit
Yes
Amazon QuickSight
DescribeFolderPermissions
View
Yes
Amazon QuickSight
UpdateFolderPermissions
Edit
Yes
Amazon QuickSight
DescribeFolderResolvedPermissions
View
Yes
Amazon QuickSight
DescribeIAMPolicyAssignment
View
Yes
Amazon QuickSight
UpdateIAMPolicyAssignment
Edit
Yes
Amazon QuickSight
DescribeTemplatePermissions
View
Yes
Amazon QuickSight
UpdateTemplatePermissions
Edit
Yes
Amazon QuickSight
DescribeThemePermissions
View
Yes
Amazon QuickSight
UpdateThemePermissions
Edit
Yes
Amazon QuickSight
GenerateEmbedUrlForAnonymousUser
Create
Yes
Amazon QuickSight
GenerateEmbedUrlForRegisteredUser
Create
Yes
Amazon QuickSight
GetDashboardEmbedUrl
View
Yes
Amazon QuickSight
GetSessionEmbedUrl
View
Yes
Amazon QuickSight
ListAnalyses
View
Yes
Amazon QuickSight
ListDashboardVersions
View
Yes
Amazon QuickSight
ListDashboards
View
Yes
Amazon QuickSight
ListFolderMembers
View
Yes
Amazon QuickSight
ListFolders
View
Yes
Amazon QuickSight
ListGroupMemberships
View
Yes
Amazon QuickSight
ListIAMPolicyAssignments
View
Yes
Amazon QuickSight
ListIAMPolicyAssignmentsForUser
View
Yes
Amazon QuickSight
ListIngestions
View
Yes
Amazon QuickSight
ListNamespaces
View
Yes
Amazon QuickSight
ListTagsForResource
View
Yes
Amazon QuickSight
TagResource
Create
Yes
Amazon QuickSight
ListTemplateAliases
View
Yes
Amazon QuickSight
ListTemplateVersions
View
Yes
Amazon QuickSight
ListTemplates
View
Yes
Amazon QuickSight
ListThemeAliases
View
Yes
Amazon QuickSight
ListThemeVersions
View
Yes
Amazon QuickSight
ListThemes
View
Yes
Amazon QuickSight
ListUserGroups
View
Yes
Amazon QuickSight
ListUsers
View
Yes
Amazon QuickSight
RegisterUser
Register
Yes
Amazon QuickSight
RestoreAnalysis
Create
Yes
Amazon QuickSight
SearchAnalyses
Search
Yes
Amazon QuickSight
SearchDashboards
Search
Yes
Amazon QuickSight
SearchFolders
Search
Yes
Amazon QuickSight
UntagResource
Delete
Yes
Amazon QuickSight
UpdateDashboardPublishedVersion
Edit
Yes
Amazon Service Catalog
AcceptPortfolioShare
Approve
Yes
Amazon Service Catalog
AssociateBudgetWithResource
Create
Yes
Amazon Service Catalog
AssociatePrincipalWithPortfolio
Create
Yes
Amazon Service Catalog
AssociateProductWithPortfolio
Create
Yes
Amazon Service Catalog
AssociateServiceActionWithProvisioningArtifact
Create
Yes
Amazon Service Catalog
AssociateTagOptionWithResource
Create
Yes
Amazon Service Catalog
DisassociateServiceActionFromProvisioningArtifact
Delete
Yes
Amazon Service Catalog
CopyProduct
Copy
Yes
Amazon Service Catalog
CreateConstraint
Create
Yes
Amazon Service Catalog
CreatePortfolio
Create
Yes
Amazon Service Catalog
CreatePortfolioShare
Create
Yes
Amazon Service Catalog
CreateProduct
Create
Yes
Amazon Service Catalog
CreateProvisionedProductPlan
Create
Yes
Amazon Service Catalog
CreateProvisioningArtifact
Create
Yes
Amazon Service Catalog
CreateServiceAction
Create
Yes
Amazon Service Catalog
CreateTagOption
Create
Yes
Amazon Service Catalog
DeleteConstraint
Delete
Yes
Amazon Service Catalog
DeletePortfolio
Delete
Yes
Amazon Service Catalog
DeletePortfolioShare
Delete
Yes
Amazon Service Catalog
DeleteProduct
Delete
Yes
Amazon Service Catalog
DeleteProvisionedProductPlan
Delete
Yes
Amazon Service Catalog
DeleteProvisioningArtifact
Delete
Yes
Amazon Service Catalog
DeleteServiceAction
Delete
Yes
Amazon Service Catalog
DeleteTagOption
Delete
Yes
Amazon Service Catalog
DescribeConstraint
View
Yes
Amazon Service Catalog
DescribeCopyProductStatus
View
Yes
Amazon Service Catalog
DescribePortfolio
View
Yes
Amazon Service Catalog
DescribePortfolioShareStatus
View
Yes
Amazon Service Catalog
DescribePortfolioShares
View
Yes
Amazon Service Catalog
DescribeProduct
View
Yes
Amazon Service Catalog
DescribeProductAsAdmin
View
Yes
Amazon Service Catalog
DescribeProductView
View
Yes
Amazon Service Catalog
DescribeProvisionedProduct
View
Yes
Amazon Service Catalog
DescribeProvisionedProductPlan
View
Yes
Amazon Service Catalog
DescribeProvisioningArtifact
View
Yes
Amazon Service Catalog
DescribeProvisioningParameters
View
Yes
Amazon Service Catalog
DescribeRecord
View
Yes
Amazon Service Catalog
DescribeServiceAction
View
Yes
Amazon Service Catalog
DescribeServiceActionExecutionParameters
View
Yes
Amazon Service Catalog
DescribeTagOption
View
Yes
Amazon Service Catalog
DisableAWSOrganizationsAccess
Edit
Yes
Amazon Service Catalog
DisassociateBudgetFromResource
Delete
Yes
Amazon Service Catalog
DisassociatePrincipalFromPortfolio
Delete
Yes
Amazon Service Catalog
DisassociateProductFromPortfolio
Delete
Yes
Amazon Service Catalog
DisassociateTagOptionFromResource
Delete
Yes
Amazon Service Catalog
EnableAWSOrganizationsAccess
Enable
Yes
Amazon Service Catalog
ExecuteProvisionedProductPlan
Create
Yes
Amazon Service Catalog
ExecuteProvisionedProductServiceAction
Create
Yes
Amazon Service Catalog
GetAWSOrganizationsAccessStatus
View
Yes
Amazon Service Catalog
GetProvisionedProductOutputs
View
Yes
Amazon Service Catalog
ImportAsProvisionedProduct
Create
Yes
Amazon Service Catalog
ListAcceptedPortfolioShares
View
Yes
Amazon Service Catalog
ListBudgetsForResource
View
Yes
Amazon Service Catalog
ListConstraintsForPortfolio
View
Yes
Amazon Service Catalog
ListLaunchPaths
View
Yes
Amazon Service Catalog
ListOrganizationPortfolioAccess
View
Yes
Amazon Service Catalog
ListPortfolioAccess
View
Yes
Amazon Service Catalog
ListPortfolios
View
Yes
Amazon Service Catalog
ListPortfoliosForProduct
View
Yes
Amazon Service Catalog
ListPrincipalsForPortfolio
View
Yes
Amazon Service Catalog
ListProvisionedProductPlans
View
Yes
Amazon Service Catalog
ListProvisioningArtifacts
View
Yes
Amazon Service Catalog
ListProvisioningArtifactsForServiceAction
View
Yes
Amazon Service Catalog
ListRecordHistory
View
Yes
Amazon Service Catalog
ListResourcesForTagOption
View
Yes
Amazon Service Catalog
ListServiceActions
View
Yes
Amazon Service Catalog
ListServiceActionsForProvisioningArtifact
View
Yes
Amazon Service Catalog
ListStackInstancesForProvisionedProduct
View
Yes
Amazon Service Catalog
ListTagOptions
View
Yes
Amazon Service Catalog
ProvisionProduct
Create
Yes
Amazon Service Catalog
RejectPortfolioShare
Reject
Yes
Amazon Service Catalog
ScanProvisionedProducts
Create
Yes
Amazon Service Catalog
SearchProducts
Search
Yes
Amazon Service Catalog
SearchProductsAsAdmin
Search
Yes
Amazon Service Catalog
SearchProvisionedProducts
Search
Yes
Amazon Service Catalog
TerminateProvisionedProduct
Terminate
Yes
Amazon Service Catalog
UpdateConstraint
Edit
Yes
Amazon Service Catalog
UpdatePortfolio
Edit
Yes
Amazon Service Catalog
UpdatePortfolioShare
Edit
Yes
Amazon Service Catalog
UpdateProduct
Edit
Yes
Amazon Service Catalog
UpdateProvisionedProduct
Edit
Yes
Amazon Service Catalog
UpdateProvisionedProductProperties
Edit
Yes
Amazon Service Catalog
UpdateProvisioningArtifact
Edit
Yes
Amazon Service Catalog
UpdateServiceAction
Edit
Yes
Amazon Service Catalog
UpdateTagOption
Edit
Yes
Amazon Lookout for Metrics
ActivateAnomalyDetector
Activate
Yes
Amazon Lookout for Metrics
BackTestAnomalyDetector
Create
Yes
Amazon Lookout for Metrics
CreateAlert
Create
Yes
Amazon Lookout for Metrics
CreateAnomalyDetector
Create
Yes
Amazon Lookout for Metrics
CreateMetricSet
Create
Yes
Amazon Lookout for Metrics
DeleteAlert
Delete
Yes
Amazon Lookout for Metrics
DeleteAnomalyDetector
Delete
Yes
Amazon Lookout for Metrics
DescribeAlert
View
Yes
Amazon Lookout for Metrics
DescribeAnomalyDetectionExecutions
View
Yes
Amazon Lookout for Metrics
DescribeAnomalyDetector
View
Yes
Amazon Lookout for Metrics
DescribeMetricSet
View
Yes
Amazon Lookout for Metrics
GetAnomalyGroup
View
Yes
Amazon Lookout for Metrics
GetFeedback
View
Yes
Amazon Lookout for Metrics
GetSampleData
View
Yes
Amazon Lookout for Metrics
ListAlerts
View
Yes
Amazon Lookout for Metrics
ListAnomalyDetectors
View
Yes
Amazon Lookout for Metrics
ListAnomalyGroupSummaries
View
Yes
Amazon Lookout for Metrics
ListAnomalyGroupTimeSeries
View
Yes
Amazon Lookout for Metrics
ListMetricSets
View
Yes
Amazon Lookout for Metrics
ListTagsForResource
View
Yes
Amazon Lookout for Metrics
TagResource
Create
Yes
Amazon Lookout for Metrics
PutFeedback
Edit
Yes
Amazon Lookout for Metrics
UntagResource
Delete
Yes
Amazon Lookout for Metrics
UpdateAnomalyDetector
Edit
Yes
Amazon Lookout for Metrics
UpdateMetricSet
Edit
Yes
Amazon Marketplace Entitlement Service
GetEntitlements
View
Yes
Amazon Personalize Events
PutEvents
Edit
Yes
Amazon Personalize Events
PutItems
Edit
Yes
Amazon Personalize Events
PutUsers
Edit
Yes
Amazon IoT 1-Click Devices Service
ClaimDevicesByClaimCode
Edit
Yes
Amazon IoT 1-Click Devices Service
DescribeDevice
View
Yes
Amazon IoT 1-Click Devices Service
FinalizeDeviceClaim
Edit
Yes
Amazon IoT 1-Click Devices Service
GetDeviceMethods
View
Yes
Amazon IoT 1-Click Devices Service
InvokeDeviceMethod
Create
Yes
Amazon IoT 1-Click Devices Service
InitiateDeviceClaim
Edit
Yes
Amazon IoT 1-Click Devices Service
ListDeviceEvents
View
Yes
Amazon IoT 1-Click Devices Service
ListDevices
View
Yes
Amazon IoT 1-Click Devices Service
ListTagsForResource
View
Yes
Amazon IoT 1-Click Devices Service
TagResource
Create
Yes
Amazon IoT 1-Click Devices Service
UnclaimDevice
Delete
Yes
Amazon IoT 1-Click Devices Service
UntagResource
Delete
Yes
Amazon IoT 1-Click Devices Service
UpdateDeviceState
Edit
Yes
Amazon Forecast Query Service
QueryForecast
Create
Yes
Amazon Data Pipeline
ActivatePipeline
Activate
Yes
Amazon Data Pipeline
AddTags
Create
Yes
Amazon Data Pipeline
CreatePipeline
Create
Yes
Amazon Data Pipeline
DeactivatePipeline
Deactivate
Yes
Amazon Data Pipeline
DeletePipeline
Delete
Yes
Amazon Data Pipeline
DescribeObjects
View
Yes
Amazon Data Pipeline
DescribePipelines
View
Yes
Amazon Data Pipeline
EvaluateExpression
Create
Yes
Amazon Data Pipeline
GetPipelineDefinition
View
Yes
Amazon Data Pipeline
ListPipelines
View
Yes
Amazon Data Pipeline
PollForTask
Create
Yes
Amazon Data Pipeline
PutPipelineDefinition
Edit
Yes
Amazon Data Pipeline
QueryObjects
Create
Yes
Amazon Data Pipeline
RemoveTags
Delete
Yes
Amazon Data Pipeline
ReportTaskProgress
Create
Yes
Amazon Data Pipeline
ReportTaskRunnerHeartbeat
Create
Yes
Amazon Data Pipeline
SetStatus
Create
Yes
Amazon Data Pipeline
SetTaskStatus
Create
Yes
Amazon Data Pipeline
ValidatePipelineDefinition
Create
Yes
Amazon SSO Identity Store
DescribeGroup
View
Yes
Amazon SSO Identity Store
DescribeUser
View
Yes
Amazon SSO Identity Store
ListGroups
View
Yes
Amazon SSO Identity Store
ListUsers
View
Yes
Amazon Route53 Recovery Control Config
CreateCluster
Create
Yes
Amazon Route53 Recovery Control Config
ListClusters
View
Yes
Amazon Route53 Recovery Control Config
CreateControlPanel
Create
Yes
Amazon Route53 Recovery Control Config
UpdateControlPanel
Edit
Yes
Amazon Route53 Recovery Control Config
CreateRoutingControl
Create
Yes
Amazon Route53 Recovery Control Config
UpdateRoutingControl
Edit
Yes
Amazon Route53 Recovery Control Config
CreateSafetyRule
Create
Yes
Amazon Route53 Recovery Control Config
UpdateSafetyRule
Edit
Yes
Amazon Route53 Recovery Control Config
DeleteCluster
Delete
Yes
Amazon Route53 Recovery Control Config
DescribeCluster
View
Yes
Amazon Route53 Recovery Control Config
DeleteControlPanel
Delete
Yes
Amazon Route53 Recovery Control Config
DescribeControlPanel
View
Yes
Amazon Route53 Recovery Control Config
DeleteRoutingControl
Delete
Yes
Amazon Route53 Recovery Control Config
DescribeRoutingControl
View
Yes
Amazon Route53 Recovery Control Config
DeleteSafetyRule
Delete
Yes
Amazon Route53 Recovery Control Config
DescribeSafetyRule
View
Yes
Amazon Route53 Recovery Control Config
ListAssociatedRouteHealthChecks
View
Yes
Amazon Route53 Recovery Control Config
ListControlPanels
View
Yes
Amazon Route53 Recovery Control Config
ListRoutingControls
View
Yes
Amazon Route53 Recovery Control Config
ListSafetyRules
View
Yes
Amazon Service Quotas
AssociateServiceQuotaTemplate
Create
Yes
Amazon Service Quotas
DeleteServiceQuotaIncreaseRequestFromTemplate
Delete
Yes
Amazon Service Quotas
DisassociateServiceQuotaTemplate
Delete
Yes
Amazon Service Quotas
GetAWSDefaultServiceQuota
View
Yes
Amazon Service Quotas
GetAssociationForServiceQuotaTemplate
View
Yes
Amazon Service Quotas
GetRequestedServiceQuotaChange
View
Yes
Amazon Service Quotas
GetServiceQuota
View
Yes
Amazon Service Quotas
GetServiceQuotaIncreaseRequestFromTemplate
View
Yes
Amazon Service Quotas
ListAWSDefaultServiceQuotas
View
Yes
Amazon Service Quotas
ListRequestedServiceQuotaChangeHistory
View
Yes
Amazon Service Quotas
ListRequestedServiceQuotaChangeHistoryByQuota
View
Yes
Amazon Service Quotas
ListServiceQuotaIncreaseRequestsInTemplate
View
Yes
Amazon Service Quotas
ListServiceQuotas
View
Yes
Amazon Service Quotas
ListServices
View
Yes
Amazon Service Quotas
ListTagsForResource
View
Yes
Amazon Service Quotas
PutServiceQuotaIncreaseRequestIntoTemplate
Edit
Yes
Amazon Service Quotas
RequestServiceQuotaIncrease
Create
Yes
Amazon Service Quotas
TagResource
Create
Yes
Amazon Service Quotas
UntagResource
Delete
Yes
Amazon Connect Service
AssociateApprovedOrigin
Create
Yes
Amazon Connect Service
AssociateBot
Create
Yes
Amazon Connect Service
DisassociateBot
Delete
Yes
Amazon Connect Service
AssociateInstanceStorageConfig
Create
Yes
Amazon Connect Service
AssociateLambdaFunction
Create
Yes
Amazon Connect Service
AssociateLexBot
Create
Yes
Amazon Connect Service
AssociateQueueQuickConnects
Create
Yes
Amazon Connect Service
AssociateRoutingProfileQueues
Create
Yes
Amazon Connect Service
AssociateSecurityKey
Create
Yes
Amazon Connect Service
CreateAgentStatus
Create
Yes
Amazon Connect Service
ListAgentStatuses
View
Yes
Amazon Connect Service
CreateContactFlow
Create
Yes
Amazon Connect Service
CreateHoursOfOperation
Create
Yes
Amazon Connect Service
CreateInstance
Create
Yes
Amazon Connect Service
ListInstances
View
Yes
Amazon Connect Service
CreateIntegrationAssociation
Create
Yes
Amazon Connect Service
ListIntegrationAssociations
View
Yes
Amazon Connect Service
CreateQueue
Create
Yes
Amazon Connect Service
CreateQuickConnect
Create
Yes
Amazon Connect Service
ListQuickConnects
View
Yes
Amazon Connect Service
CreateRoutingProfile
Create
Yes
Amazon Connect Service
CreateUseCase
Create
Yes
Amazon Connect Service
ListUseCases
View
Yes
Amazon Connect Service
CreateUser
Create
Yes
Amazon Connect Service
CreateUserHierarchyGroup
Create
Yes
Amazon Connect Service
DeleteHoursOfOperation
Delete
Yes
Amazon Connect Service
DescribeHoursOfOperation
View
Yes
Amazon Connect Service
UpdateHoursOfOperation
Edit
Yes
Amazon Connect Service
DeleteInstance
Delete
Yes
Amazon Connect Service
DescribeInstance
View
Yes
Amazon Connect Service
DeleteIntegrationAssociation
Delete
Yes
Amazon Connect Service
DeleteQuickConnect
Delete
Yes
Amazon Connect Service
DescribeQuickConnect
View
Yes
Amazon Connect Service
DeleteUseCase
Delete
Yes
Amazon Connect Service
DeleteUser
Delete
Yes
Amazon Connect Service
DescribeUser
View
Yes
Amazon Connect Service
DeleteUserHierarchyGroup
Delete
Yes
Amazon Connect Service
DescribeUserHierarchyGroup
View
Yes
Amazon Connect Service
DescribeAgentStatus
View
Yes
Amazon Connect Service
UpdateAgentStatus
Edit
Yes
Amazon Connect Service
DescribeContactFlow
View
Yes
Amazon Connect Service
DescribeInstanceAttribute
View
Yes
Amazon Connect Service
UpdateInstanceAttribute
Edit
Yes
Amazon Connect Service
DescribeInstanceStorageConfig
View
Yes
Amazon Connect Service
DisassociateInstanceStorageConfig
Delete
Yes
Amazon Connect Service
UpdateInstanceStorageConfig
Edit
Yes
Amazon Connect Service
DescribeQueue
View
Yes
Amazon Connect Service
DescribeRoutingProfile
View
Yes
Amazon Connect Service
DescribeUserHierarchyStructure
View
Yes
Amazon Connect Service
UpdateUserHierarchyStructure
Edit
Yes
Amazon Connect Service
DisassociateApprovedOrigin
Delete
Yes
Amazon Connect Service
DisassociateLambdaFunction
Delete
Yes
Amazon Connect Service
DisassociateLexBot
Delete
Yes
Amazon Connect Service
DisassociateQueueQuickConnects
Delete
Yes
Amazon Connect Service
DisassociateRoutingProfileQueues
Delete
Yes
Amazon Connect Service
DisassociateSecurityKey
Delete
Yes
Amazon Connect Service
GetContactAttributes
View
Yes
Amazon Connect Service
GetCurrentMetricData
View
Yes
Amazon Connect Service
GetFederationToken
View
Yes
Amazon Connect Service
GetMetricData
View
Yes
Amazon Connect Service
ListApprovedOrigins
View
Yes
Amazon Connect Service
ListBots
View
Yes
Amazon Connect Service
ListContactFlows
View
Yes
Amazon Connect Service
ListHoursOfOperations
View
Yes
Amazon Connect Service
ListInstanceAttributes
View
Yes
Amazon Connect Service
ListInstanceStorageConfigs
View
Yes
Amazon Connect Service
ListLambdaFunctions
View
Yes
Amazon Connect Service
ListLexBots
View
Yes
Amazon Connect Service
ListPhoneNumbers
View
Yes
Amazon Connect Service
ListPrompts
View
Yes
Amazon Connect Service
ListQueueQuickConnects
View
Yes
Amazon Connect Service
ListQueues
View
Yes
Amazon Connect Service
ListRoutingProfileQueues
View
Yes
Amazon Connect Service
UpdateRoutingProfileQueues
Edit
Yes
Amazon Connect Service
ListRoutingProfiles
View
Yes
Amazon Connect Service
ListSecurityKeys
View
Yes
Amazon Connect Service
ListSecurityProfiles
View
Yes
Amazon Connect Service
ListTagsForResource
View
Yes
Amazon Connect Service
TagResource
Create
Yes
Amazon Connect Service
ListUserHierarchyGroups
View
Yes
Amazon Connect Service
ListUsers
View
Yes
Amazon Connect Service
ResumeContactRecording
Start
Yes
Amazon Connect Service
StartChatContact
Start
Yes
Amazon Connect Service
StartContactRecording
Start
Yes
Amazon Connect Service
StartOutboundVoiceContact
Start
Yes
Amazon Connect Service
StartTaskContact
Start
Yes
Amazon Connect Service
StopContact
Stop
Yes
Amazon Connect Service
StopContactRecording
Stop
Yes
Amazon Connect Service
SuspendContactRecording
Delete
Yes
Amazon Connect Service
UntagResource
Delete
Yes
Amazon Connect Service
UpdateContactAttributes
Edit
Yes
Amazon Connect Service
UpdateContactFlowContent
Edit
Yes
Amazon Connect Service
UpdateContactFlowName
Edit
Yes
Amazon Connect Service
UpdateQueueHoursOfOperation
Edit
Yes
Amazon Connect Service
UpdateQueueMaxContacts
Edit
Yes
Amazon Connect Service
UpdateQueueName
Edit
Yes
Amazon Connect Service
UpdateQueueOutboundCallerConfig
Edit
Yes
Amazon Connect Service
UpdateQueueStatus
Edit
Yes
Amazon Connect Service
UpdateQuickConnectConfig
Edit
Yes
Amazon Connect Service
UpdateQuickConnectName
Edit
Yes
Amazon Connect Service
UpdateRoutingProfileConcurrency
Edit
Yes
Amazon Connect Service
UpdateRoutingProfileDefaultOutboundQueue
Edit
Yes
Amazon Connect Service
UpdateRoutingProfileName
Edit
Yes
Amazon Connect Service
UpdateUserHierarchy
Edit
Yes
Amazon Connect Service
UpdateUserHierarchyGroupName
Edit
Yes
Amazon Connect Service
UpdateUserIdentityInfo
Edit
Yes
Amazon Connect Service
UpdateUserPhoneConfig
Edit
Yes
Amazon Connect Service
UpdateUserRoutingProfile
Edit
Yes
Amazon Connect Service
UpdateUserSecurityProfiles
Edit
Yes
Amazon Mobile
CreateProject
Create
Yes
Amazon Mobile
ListProjects
View
Yes
Amazon Mobile
DeleteProject
Delete
Yes
Amazon Mobile
DescribeBundle
View
Yes
Amazon Mobile
ExportBundle
View
Yes
Amazon Mobile
DescribeProject
View
Yes
Amazon Mobile
ExportProject
View
Yes
Amazon Mobile
ListBundles
View
Yes
Amazon Mobile
UpdateProject
Edit
Yes
Amazon Resource Groups Tagging API
DescribeReportCreation
View
Yes
Amazon Resource Groups Tagging API
GetComplianceSummary
View
Yes
Amazon Resource Groups Tagging API
GetResources
View
Yes
Amazon Resource Groups Tagging API
GetTagKeys
View
Yes
Amazon Resource Groups Tagging API
GetTagValues
View
Yes
Amazon Resource Groups Tagging API
StartReportCreation
Start
Yes
Amazon Resource Groups Tagging API
TagResources
Create
Yes
Amazon Resource Groups Tagging API
UntagResources
Delete
Yes
Amazon Lex Model Building V2
BuildBotLocale
Create
Yes
Amazon Lex Model Building V2
DeleteBotLocale
Delete
Yes
Amazon Lex Model Building V2
DescribeBotLocale
View
Yes
Amazon Lex Model Building V2
UpdateBotLocale
Edit
Yes
Amazon Lex Model Building V2
CreateBot
Create
Yes
Amazon Lex Model Building V2
ListBots
View
Yes
Amazon Lex Model Building V2
CreateBotAlias
Create
Yes
Amazon Lex Model Building V2
ListBotAliases
View
Yes
Amazon Lex Model Building V2
CreateBotLocale
Create
Yes
Amazon Lex Model Building V2
ListBotLocales
View
Yes
Amazon Lex Model Building V2
CreateBotVersion
Create
Yes
Amazon Lex Model Building V2
ListBotVersions
View
Yes
Amazon Lex Model Building V2
CreateExport
Create
Yes
Amazon Lex Model Building V2
ListExports
View
Yes
Amazon Lex Model Building V2
CreateIntent
Create
Yes
Amazon Lex Model Building V2
ListIntents
View
Yes
Amazon Lex Model Building V2
CreateResourcePolicy
Create
Yes
Amazon Lex Model Building V2
DeleteResourcePolicy
Delete
Yes
Amazon Lex Model Building V2
DescribeResourcePolicy
View
Yes
Amazon Lex Model Building V2
UpdateResourcePolicy
Edit
Yes
Amazon Lex Model Building V2
CreateResourcePolicyStatement
Create
Yes
Amazon Lex Model Building V2
CreateSlot
Create
Yes
Amazon Lex Model Building V2
ListSlots
View
Yes
Amazon Lex Model Building V2
CreateSlotType
Create
Yes
Amazon Lex Model Building V2
ListSlotTypes
View
Yes
Amazon Lex Model Building V2
CreateUploadUrl
Create
Yes
Amazon Lex Model Building V2
DeleteBot
Delete
Yes
Amazon Lex Model Building V2
DescribeBot
View
Yes
Amazon Lex Model Building V2
UpdateBot
Edit
Yes
Amazon Lex Model Building V2
DeleteBotAlias
Delete
Yes
Amazon Lex Model Building V2
DescribeBotAlias
View
Yes
Amazon Lex Model Building V2
UpdateBotAlias
Edit
Yes
Amazon Lex Model Building V2
DeleteBotVersion
Delete
Yes
Amazon Lex Model Building V2
DescribeBotVersion
View
Yes
Amazon Lex Model Building V2
DeleteExport
Delete
Yes
Amazon Lex Model Building V2
DescribeExport
View
Yes
Amazon Lex Model Building V2
UpdateExport
Edit
Yes
Amazon Lex Model Building V2
DeleteImport
Delete
Yes
Amazon Lex Model Building V2
DescribeImport
View
Yes
Amazon Lex Model Building V2
DeleteIntent
Delete
Yes
Amazon Lex Model Building V2
DescribeIntent
View
Yes
Amazon Lex Model Building V2
UpdateIntent
Edit
Yes
Amazon Lex Model Building V2
DeleteResourcePolicyStatement
Delete
Yes
Amazon Lex Model Building V2
DeleteSlot
Delete
Yes
Amazon Lex Model Building V2
DescribeSlot
View
Yes
Amazon Lex Model Building V2
UpdateSlot
Edit
Yes
Amazon Lex Model Building V2
DeleteSlotType
Delete
Yes
Amazon Lex Model Building V2
DescribeSlotType
View
Yes
Amazon Lex Model Building V2
UpdateSlotType
Edit
Yes
Amazon Lex Model Building V2
ListBuiltInIntents
View
Yes
Amazon Lex Model Building V2
ListBuiltInSlotTypes
View
Yes
Amazon Lex Model Building V2
ListImports
View
Yes
Amazon Lex Model Building V2
StartImport
Start
Yes
Amazon Lex Model Building V2
ListTagsForResource
View
Yes
Amazon Lex Model Building V2
TagResource
Create
Yes
Amazon Lex Model Building V2
UntagResource
Delete
Yes
In this Topic
Supported AWS Entities for Real-time Protection
Supported AWS Entities for Real-time Protection - Netskope Knowledge Portal

---
## Configure Real-time Protection Policies for Email Outbound
**URL:** https://docs.netskope.com/en/configure-real-time-protection-policies-for-email-outbound/
**Last Modified:** 2025-08-31T01:55:55+00:00
**Scraped:** 2026-06-25T09:11:10.121818+00:00

Configure Real-time Protection Policies for Email Outbound
Real-time Protection policies enable Netskope to scan outgoing emails for DLP violations. This protection is done as emails are received from Microsoft Exchange or Gmail and processed by the SMTP Proxy which allows data to be examined and protected in real time.
In the Netskope UI, navigate to
Policies > Real-time Protection
.
In the Real-time Protection page, click
New Policy > Email Outbound
.
In the Real-time Protection Policy page, select the Users, User Groups, and Organizational Units under Source. Outgoing emails from the selected users, groups, and organizations will be scanned by DLP.
Under Destination, select
Email Outbound App
and then select
Microsoft Office 365 Exchange
and
Google Gmail
as the Email Outbound.
In the Destinations section, click
Edit
under Activities & Constraints and select
Send
. Additionally, you can specify user constraints on the right side of the Select Activities & Constraints dialog box. Click
Save
.
Under Profile and Action, select the various DLP profiles from the list.
Select an action to define the enforcement action to be performed when a DLP profile matches the content in the email.
When you select
Allow,
the action is allowed when it meets the profile.
When you select
Alert
, the action type is applied globally to all the selected DLP profiles and alerts are generated when any of the profiles match the email content.
When you select
Add SMTP Header
, Netskope SMTP Proxy adds the specified custom header to the email when the email content matches the policy definition.
As of R128, you can select
Remove Recipients
. For more information, see below.
Alternatively, you can set the type of action for each profile by clicking
Set action for each profile
.
In the Profile and Action section, click
Add Traffic Action
to specify additional actions to be taken if none of the selected profiles match the criteria for violation.
Under Set Policy, provide a name for the policy and a policy description.
In the Set Policy section, click
Email Notification
. In the Email Notification window, specify the notification frequency and who should receive the notifications. Optionally, you can also specify the From Email. Click
Done
.
Click
Save
and in the Real-time Protection page click
Apply Changes
.
Removing Recipients through SMTP Proxy
This feature is in Beta. For more information, please contact your account executive or support@netskope.com
The Netskope SMTP Proxy has the ability to remove specific recipients from an email while still allowing the email to go through to the rest of the recipients, so that the emails are delivered only to the allow-listed recipients. This ensures compliance while maintaining communication flow for permitted recipients.
Use Case:
Consider a situation where
Alice
<alice@example.com>
sends an email to Bob
<bob@example.com>
and
Carol
<
carol@example.com
> with
Bob
and
Carol
as the recipients in the
To:
header. If a
Constraint Profile
has been set up to only allow emails to
Carol
, then
Bob
will not receive an email and the email will only go to
Carol
.
Alice
will also receive a notification stating her email failed to reach
Bob
as it was blocked by the SMTP Proxy.
Carol
will also see that
Bob
was an intended recipient.
If there are no recipients left after deleting the restricted recipients, the SMTP Proxy will return an SMTP error with code 558. The reply message depends on the email provider:
In case of Gmail, where there is always only one recipient in an email, the message will be as follows:
558 User is restricted and has been deleted from the recipient list due to policy
.
In case of Microsoft Exchange, where there can be multiple recipients in the email, the message will be as follows:
558 Message rejected: No recipients remaining after deleting restricted users due to policy
Configuration:
Requirements:
This will only work with an
Email Outbound App
.
You must select a DLP under
Profile & Action
section.
You must set
To User
: in the
Activity Constraints
section.
When all three requirements are fulfilled,
Remove Recipients
will appear.
The notification must be configured to inform the sender that users have been removed as recipients.
SMTP Removed Recipients
has been added to the Email Notification template in order to inform the user that their email has been modified by the SMTP Proxy.
In this Topic
Configure Real-time Protection Policies for Email Outbound

---
## Create a Real-time Protection Policy for Threat Exchange File Hashes
**URL:** https://docs.netskope.com/en/create-a-real-time-protection-policy-for-threat-exchange-file-hashes/
**Last Modified:** 2026-03-21T02:26:06+00:00
**Scraped:** 2026-06-25T09:11:27.238956+00:00

Create a Real-time Protection Policy for Threat Exchange File Hashes - Netskope Knowledge Portal
Create a Real-time Protection Policy for Threat Exchange File Hashes
Go to
Policies > Real-time Protection
.
Select the
Source
and
Destination
options as needed.
Under
Profile & Action
, select
Threat Protection Profile
.
Select the profile that you created.
Add severity actions.
Enter a Policy name and click
Save
.
Your Netskope tenant is now ready to react to file hashes uploaded from Cloud Threat Exchange.
In this Topic
Create a Real-time Protection Policy for Threat Exchange File Hashes

---
## Supported GCP Entities for Real-time Protection
**URL:** https://docs.netskope.com/en/supported-gcp-entities-for-real-time-protection/
**Last Modified:** 2025-08-31T01:50:21+00:00
**Scraped:** 2026-06-25T09:20:41.981381+00:00

Supported GCP Entities for Real-time Protection - Netskope Knowledge Portal
Supported GCP Entities for Real-time Protection
Netskope for IaaS Real-time Protection provides robust real-time activity monitoring and enforcement for GCP services across API and CLI traffic. For GCP, Browser traffic is also covered. The following table provides the list of GCP services that are supported for Real-time Protection.
When looking up browser activity coverage for an App, ignore the “API Activity” column.
App Name
API Action
Connector Activity
Browser and API Traffic
Instance ID
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.predictionApiKeyRegistrations.delete
Delete
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.operations.get
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.catalogItems.patch
Edit
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.operations.list
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.placements.predict
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.catalogItems.list
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.catalogItems.create
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.catalogItems.import
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.list
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.predictionApiKeyRegistrations.list
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.predictionApiKeyRegistrations.create
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.userEvents.list
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.userEvents.collect
View
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.userEvents.import
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.userEvents.purge
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.userEvents.rejoin
Create
API Only
GCP Recommendations
recommendationengine.projects.locations.catalogs.eventStores.userEvents.write
Create
API Only
GCP Billing
cloudbilling.billingAccounts.list
View
API Only
GCP Billing
cloudbilling.billingAccounts.create
Create
API Only
GCP Billing
cloudbilling.services.list
View
API Only
GCP Billing
cloudbilling.billingAccounts.get
View
API Only
GCP Billing
cloudbilling.billingAccounts.patch
Edit
API Only
GCP Billing
cloudbilling.projects.getBillingInfo
View
API Only
GCP Billing
cloudbilling.projects.updateBillingInfo
Edit
API Only
GCP Billing
cloudbilling.billingAccounts.projects.list
View
API Only
GCP Billing
cloudbilling.services.skus.list
View
API Only
GCP Billing
cloudbilling.billingAccounts.getIamPolicy
View
API Only
GCP Billing
cloudbilling.billingAccounts.setIamPolicy
Create
API Only
GCP Billing
cloudbilling.billingAccounts.testIamPermissions
Create
API Only
GCP Speech-to-Text
speech.operations.list
View
API Only
GCP Speech-to-Text
speech.operations.get
View
API Only
GCP Speech-to-Text
speech.speech.longrunningrecognize
Create
API Only
GCP Speech-to-Text
speech.speech.recognize
Create
API Only
GCP Speech-to-Text
speech.projects.locations.phraseSets.delete
Delete
API Only
GCP Speech-to-Text
speech.projects.locations.phraseSets.get
View
API Only
GCP Speech-to-Text
speech.projects.locations.phraseSets.patch
Edit
API Only
GCP Speech-to-Text
speech.projects.locations.customClasses.list
View
API Only
GCP Speech-to-Text
speech.projects.locations.customClasses.create
Create
API Only
GCP Speech-to-Text
speech.projects.locations.phraseSets.list
View
API Only
GCP Speech-to-Text
speech.projects.locations.phraseSets.create
Create
API Only
GCP IDS
ids.projects.locations.operations.delete
Delete
API Only
GCP IDS
ids.projects.locations.operations.get
View
API Only
GCP IDS
ids.projects.locations.endpoints.patch
Edit
API Only
GCP IDS
ids.projects.locations.list
View
API Only
GCP IDS
ids.projects.locations.operations.list
View
API Only
GCP IDS
ids.projects.locations.operations.cancel
Delete
API Only
GCP IDS
ids.projects.locations.endpoints.list
View
API Only
GCP IDS
ids.projects.locations.endpoints.create
Create
API Only
GCP IDS
ids.projects.locations.endpoints.getIamPolicy
View
API Only
GCP IDS
ids.projects.locations.endpoints.setIamPolicy
Create
API Only
GCP IDS
ids.projects.locations.endpoints.testIamPermissions
Create
API Only
GCP Policy Analyzer
policyanalyzer.projects.locations.activityTypes.activities.query
View
API Only
GCP IAM Service Account Credentials
iamcredentials.projects.serviceAccounts.generateAccessToken
Create
API Only
GCP IAM Service Account Credentials
iamcredentials.projects.serviceAccounts.generateIdToken
Create
API Only
GCP IAM Service Account Credentials
iamcredentials.projects.serviceAccounts.signBlob
Create
API Only
GCP IAM Service Account Credentials
iamcredentials.projects.serviceAccounts.signJwt
Create
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.delete
Delete
API Only
GCP Service Consumer Management
serviceconsumermanagement.operations.list
View
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.applyProjectConfig
Edit
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.attachProject
Attach
API Only
GCP Service Consumer Management
serviceconsumermanagement.operations.cancel
Delete
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.deleteProject
Delete
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.removeProject
Delete
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.undeleteProject
Create
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.list
View
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.create
Create
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.tenancyUnits.addProject
Create
API Only
GCP Service Consumer Management
serviceconsumermanagement.services.search
Search
API Only
GCP Datastore
datastore.projects.indexes.list
View
API Only
GCP Datastore
datastore.projects.indexes.create
Create
API Only
GCP Datastore
datastore.projects.indexes.delete
Delete
API Only
GCP Datastore
datastore.projects.indexes.get
View
API Only
GCP Datastore
datastore.projects.allocateIds
Create
API Only
GCP Datastore
datastore.projects.beginTransaction
Create
API Only
GCP Datastore
datastore.projects.commit
Create
API Only
GCP Datastore
datastore.projects.export
View
API Only
GCP Datastore
datastore.projects.import
Create
API Only
GCP Datastore
datastore.projects.lookup
Create
API Only
GCP Datastore
datastore.projects.reserveIds
Create
API Only
GCP Datastore
datastore.projects.rollback
Create
API Only
GCP Datastore
datastore.projects.runAggregationQuery
Create
API Only
GCP Datastore
datastore.projects.runQuery
Create
API Only
GCP Datastore
datastore.projects.operations.delete
Delete
API Only
GCP Datastore
datastore.projects.operations.get
View
API Only
GCP Datastore
datastore.projects.operations.list
View
API Only
GCP Datastore
datastore.projects.operations.cancel
Delete
API Only
GCP Policy Troubleshooter
policytroubleshooter.iam.troubleshoot
Create
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.delete
Delete
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.get
View
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.patch
Edit
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.configVersions.list
View
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.states.list
View
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.modifyCloudToDeviceConfig
Edit
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.sendCommandToDevice
Send
API Only
GCP IoT
cloudiot.projects.locations.registries.groups.devices.list
View
API Only
GCP IoT
cloudiot.projects.locations.registries.devices.create
Create
API Only
GCP IoT
cloudiot.projects.locations.registries.list
View
API Only
GCP IoT
cloudiot.projects.locations.registries.create
Create
API Only
GCP IoT
cloudiot.projects.locations.registries.bindDeviceToGateway
Create
API Only
GCP IoT
cloudiot.projects.locations.registries.unbindDeviceFromGateway
Create
API Only
GCP IoT
cloudiot.projects.locations.registries.groups.getIamPolicy
View
API Only
GCP IoT
cloudiot.projects.locations.registries.groups.setIamPolicy
Create
API Only
GCP IoT
cloudiot.projects.locations.registries.groups.testIamPermissions
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.tasks.delete
Delete
API Only
GCP Tasks
cloudtasks.projects.locations.queues.tasks.get
View
API Only
GCP Tasks
cloudtasks.projects.locations.queues.patch
Edit
API Only
GCP Tasks
cloudtasks.projects.locations.list
View
API Only
GCP Tasks
cloudtasks.projects.locations.queues.pause
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.purge
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.resume
Start
API Only
GCP Tasks
cloudtasks.projects.locations.queues.tasks.run
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.list
View
API Only
GCP Tasks
cloudtasks.projects.locations.queues.create
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.tasks.list
View
API Only
GCP Tasks
cloudtasks.projects.locations.queues.tasks.create
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.getIamPolicy
View
API Only
GCP Tasks
cloudtasks.projects.locations.queues.setIamPolicy
Create
API Only
GCP Tasks
cloudtasks.projects.locations.queues.testIamPermissions
Create
API Only
GCP Build
cloudbuild.githubDotComWebhook.receive
Create
API Only
GCP Build
cloudbuild.projects.builds.list
View
API Only
GCP Build
cloudbuild.projects.builds.create
Create
API Only
GCP Build
cloudbuild.projects.builds.get
View
API Only
GCP Build
cloudbuild.projects.builds.cancel
Delete
API Only
GCP Build
cloudbuild.projects.builds.retry
Create
API Only
GCP Build
cloudbuild.projects.triggers.list
View
API Only
GCP Build
cloudbuild.projects.triggers.create
Create
API Only
GCP Build
cloudbuild.projects.triggers.delete
Delete
API Only
GCP Build
cloudbuild.projects.triggers.get
View
API Only
GCP Build
cloudbuild.projects.triggers.patch
Edit
API Only
GCP Build
cloudbuild.projects.triggers.run
Create
API Only
GCP Build
cloudbuild.projects.triggers.webhook
Create
API Only
GCP Build
cloudbuild.webhook
Create
API Only
GCP Build
cloudbuild.projects.locations.bitbucketServerConfigs.removeBitbucketServerConnectedRepository
Delete
API Only
GCP Build
cloudbuild.projects.locations.gitLabConfigs.removeGitLabConnectedRepository
Delete
API Only
GCP Build
cloudbuild.locations.regionalWebhook
Create
API Only
GCP Build
cloudbuild.projects.locations.workerPools.delete
Delete
API Only
GCP Build
cloudbuild.projects.locations.workerPools.get
View
API Only
GCP Build
cloudbuild.projects.locations.workerPools.patch
Edit
API Only
GCP Build
cloudbuild.projects.locations.builds.approve
Approve
API Only
GCP Build
cloudbuild.projects.locations.operations.cancel
Delete
API Only
GCP Build
cloudbuild.projects.locations.builds.retry
Create
API Only
GCP Build
cloudbuild.projects.locations.triggers.run
Create
API Only
GCP Build
cloudbuild.projects.locations.triggers.webhook
Create
API Only
GCP Build
cloudbuild.projects.locations.bitbucketServerConfigs.list
View
API Only
GCP Build
cloudbuild.projects.locations.bitbucketServerConfigs.create
Create
API Only
GCP Build
cloudbuild.projects.locations.builds.list
View
API Only
GCP Build
cloudbuild.projects.locations.builds.create
Create
API Only
GCP Build
cloudbuild.projects.locations.gitLabConfigs.connectedRepositories.Create
Create
API Only
GCP Build
cloudbuild.projects.locations.gitLabConfigs.list
View
API Only
GCP Build
cloudbuild.projects.locations.gitLabConfigs.create
Create
API Only
GCP Build
cloudbuild.projects.locations.githubEnterpriseConfigs.list
View
API Only
GCP Build
cloudbuild.projects.locations.githubEnterpriseConfigs.create
Create
API Only
GCP Build
cloudbuild.projects.locations.gitLabConfigs.repos.list
View
API Only
GCP Build
cloudbuild.projects.locations.triggers.list
View
API Only
GCP Build
cloudbuild.projects.locations.triggers.create
Create
API Only
GCP Build
cloudbuild.projects.locations.workerPools.list
View
API Only
GCP Build
cloudbuild.projects.locations.workerPools.create
Create
API Only
GCP Build
cloudbuild.projects.locations.triggers.patch
Edit
API Only
GCP Runtime Configuration
runtimeconfig.operations.delete
Delete
API Only
GCP Runtime Configuration
runtimeconfig.operations.list
View
API Only
GCP Runtime Configuration
runtimeconfig.operations.cancel
Delete
API Only
GCP Firestore
firestore.projects.databases.documents.Get
View
API Only
GCP Firestore
firestore.projects.databases.documents.Write
Create
API Only
GCP Firestore
firestore.projects.databases.documents.beginTransaction
Create
API Only
GCP Firestore
firestore.projects.databases.documents.commit
Create
API Only
GCP Firestore
firestore.projects.databases.documents.listen
View
API Only
GCP Firestore
firestore.projects.databases.documents.rollback
Create
API Only
GCP Firestore
firestore.projects.databases.documents.write
Create
API Only
GCP Firestore
firestore.projects.locations.backups.delete
Delete
API Only
GCP Firestore
firestore.projects.locations.backups.get
View
API Only
GCP Firestore
firestore.projects.databases.documents.patch
Edit
API Only
GCP Firestore
firestore.projects.locations.list
View
API Only
GCP Firestore
firestore.projects.databases.operations.list
View
API Only
GCP Firestore
firestore.projects.databases.operations.cancel
Delete
API Only
GCP Firestore
firestore.projects.databases.exportDocuments
View
API Only
GCP Firestore
firestore.projects.databases.importDocuments
Create
API Only
GCP Firestore
firestore.projects.databases.backupSchedules.list
View
API Only
GCP Firestore
firestore.projects.databases.backupSchedules.create
Create
API Only
GCP Firestore
firestore.projects.locations.backups.list
View
API Only
GCP Firestore
firestore.projects.databases.list
View
API Only
GCP Firestore
firestore.projects.databases.create
Create
API Only
GCP Firestore
firestore.projects.databases.restore
Create
API Only
GCP Firestore
firestore.projects.databases.collectionGroups.fields.list
View
API Only
GCP Firestore
firestore.projects.databases.collectionGroups.indexes.list
View
API Only
GCP Firestore
firestore.projects.databases.collectionGroups.indexes.create
Create
API Only
GCP Firestore
firestore.projects.databases.documents.listDocuments
View
API Only
GCP Firestore
firestore.projects.databases.documents.createDocument
Create
API Only
GCP Firestore
firestore.projects.databases.documents.listCollectionIds
View
API Only
GCP Firestore
firestore.projects.databases.documents.partitionQuery
Create
API Only
GCP Firestore
firestore.projects.databases.documents.runAggregationQuery
Create
API Only
GCP Firestore
firestore.projects.databases.documents.runQuery
Create
API Only
GCP SQL Admin
sql.flags.list
View
API Only
GCP SQL Admin
sql.instances.list
View
API Only
GCP SQL Admin
sql.instances.insert
Create
API Only
GCP SQL Admin
sql.instances.delete
Delete
API Only
GCP SQL Admin
sql.instances.get
View
API Only
GCP SQL Admin
sql.instances.patch
Edit
API Only
GCP SQL Admin
sql.instances.update
Edit
API Only
GCP SQL Admin
sql.instances.addServerCa
Create
API Only
GCP SQL Admin
sql.backupRuns.list
View
API Only
GCP SQL Admin
sql.backupRuns.insert
Create
API Only
GCP SQL Admin
sql.backupRuns.delete
Delete
API Only
GCP SQL Admin
sql.backupRuns.get
View
API Only
GCP SQL Admin
sql.instances.clone
Create
API Only
GCP SQL Admin
sql.connect.get
View
API Only
GCP SQL Admin
sql.sslCerts.createEphemeral
Create
API Only
GCP SQL Admin
sql.databases.list
View
API Only
GCP SQL Admin
sql.databases.insert
Create
API Only
GCP SQL Admin
sql.databases.delete
Delete
API Only
GCP SQL Admin
sql.databases.get
View
API Only
GCP SQL Admin
sql.databases.patch
Edit
API Only
GCP SQL Admin
sql.databases.update
Edit
API Only
GCP SQL Admin
sql.instances.demoteMaster
Create
API Only
GCP SQL Admin
sql.instances.export
View
API Only
GCP SQL Admin
sql.instances.failover
Create
API Only
GCP SQL Admin
sql.projects.instances.getDiskShrinkConfig
View
API Only
GCP SQL Admin
sql.instances.import
Create
API Only
GCP SQL Admin
sql.instances.listServerCas
View
API Only
GCP SQL Admin
sql.projects.instances.performDiskShrink
Create
API Only
GCP SQL Admin
sql.instances.promoteReplica
Create
API Only
GCP SQL Admin
sql.instances.reencrypt
Create
API Only
GCP SQL Admin
sql.projects.instances.rescheduleMaintenance
Create
API Only
GCP SQL Admin
sql.projects.instances.resetReplicaSize
Edit
API Only
GCP SQL Admin
sql.instances.resetSslConfig
Edit
API Only
GCP SQL Admin
sql.instances.restart
Reboot
API Only
GCP SQL Admin
sql.instances.restoreBackup
Create
API Only
GCP SQL Admin
sql.instances.rotateServerCa
Create
API Only
GCP SQL Admin
sql.sslCerts.list
View
API Only
GCP SQL Admin
sql.sslCerts.insert
Create
API Only
GCP SQL Admin
sql.sslCerts.delete
Delete
API Only
GCP SQL Admin
sql.sslCerts.get
View
API Only
GCP SQL Admin
sql.projects.instances.startExternalSync
Start
API Only
GCP SQL Admin
sql.instances.startReplica
Start
API Only
GCP SQL Admin
sql.instances.stopReplica
Stop
API Only
GCP SQL Admin
sql.instances.truncateLog
Create
API Only
GCP SQL Admin
sql.users.delete
Delete
API Only
GCP SQL Admin
sql.users.list
View
API Only
GCP SQL Admin
sql.users.insert
Create
API Only
GCP SQL Admin
sql.users.update
Edit
API Only
GCP SQL Admin
sql.users.get
View
API Only
GCP SQL Admin
sql.projects.instances.verifyExternalSyncSettings
Create
API Only
GCP SQL Admin
sql.connect.generateEphemeral
Create
API Only
GCP SQL Admin
sql.operations.list
View
API Only
GCP SQL Admin
sql.operations.get
View
API Only
GCP SQL Admin
sql.operations.cancel
Delete
API Only
GCP SQL Admin
sql.tiers.list
View
API Only
GCP BigQuery
bigquery.projects.list
View
API Only
GCP BigQuery
bigquery.datasets.list
View
API Only
GCP BigQuery
bigquery.datasets.insert
Create
API Only
GCP BigQuery
bigquery.datasets.delete
Delete
API Only
GCP BigQuery
bigquery.datasets.get
View
API Only
GCP BigQuery
bigquery.datasets.patch
Edit
API Only
GCP BigQuery
bigquery.datasets.update
Edit
API Only
GCP BigQuery
bigquery.models.list
View
API Only
GCP BigQuery
bigquery.models.delete
Delete
API Only
GCP BigQuery
bigquery.models.get
View
API Only
GCP BigQuery
bigquery.models.patch
Edit
API Only
GCP BigQuery
bigquery.routines.list
View
API Only
GCP BigQuery
bigquery.routines.insert
Create
API Only
GCP BigQuery
bigquery.routines.delete
Delete
API Only
GCP BigQuery
bigquery.routines.get
View
API Only
GCP BigQuery
bigquery.routines.update
Edit
API Only
GCP BigQuery
bigquery.tables.list
View
API Only
GCP BigQuery
bigquery.tables.insert
Create
API Only
GCP BigQuery
bigquery.tables.delete
Delete
API Only
GCP BigQuery
bigquery.tables.get
View
API Only
GCP BigQuery
bigquery.tables.patch
Edit
API Only
GCP BigQuery
bigquery.tables.update
Edit
API Only
GCP BigQuery
bigquery.tabledata.list
View
API Only
GCP BigQuery
bigquery.tabledata.insertAll
Create
API Only
GCP BigQuery
bigquery.rowAccessPolicies.list
View
API Only
GCP BigQuery
bigquery.jobs.list
View
API Only
GCP BigQuery
bigquery.jobs.insert
Create
API Only
GCP BigQuery
bigquery.jobs.get
View
API Only
GCP BigQuery
bigquery.jobs.cancel
Delete
API Only
GCP BigQuery
bigquery.jobs.delete
Delete
API Only
GCP BigQuery
bigquery.jobs.query
Create
API Only
GCP BigQuery
bigquery.jobs.getQueryResults
View
API Only
GCP BigQuery
bigquery.projects.getServiceAccount
View
API Only
GCP BigQuery
bigquery.tables.getIamPolicy
View
API Only
GCP BigQuery
bigquery.tables.setIamPolicy
Create
API Only
GCP BigQuery
bigquery.tables.testIamPermissions
Create
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.delete
Delete
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.get
View
API Only
GCP GKE Hub
gkehub.projects.locations.memberships.bindings.patch
Edit
API Only
GCP GKE Hub
gkehub.projects.locations.list
View
API Only
GCP GKE Hub
gkehub.projects.locations.operations.list
View
API Only
GCP GKE Hub
gkehub.projects.locations.operations.cancel
Delete
API Only
GCP GKE Hub
gkehub.projects.locations.memberships.generateConnectManifest
Create
API Only
GCP GKE Hub
gkehub.projects.locations.memberships.bindings.list
View
API Only
GCP GKE Hub
gkehub.projects.locations.memberships.bindings.create
Create
API Only
GCP GKE Hub
gkehub.projects.locations.features.list
View
API Only
GCP GKE Hub
gkehub.projects.locations.features.create
Create
API Only
GCP GKE Hub
gkehub.projects.locations.memberships.list
View
API Only
GCP GKE Hub
gkehub.projects.locations.memberships.create
Create
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.list
View
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.create
Create
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.getIamPolicy
View
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.setIamPolicy
Create
API Only
GCP GKE Hub
gkehub.projects.locations.scopes.testIamPermissions
Create
API Only
GCP Spanner
spanner.projects.instances.databases.dropDatabase
Delete
API Only
GCP Spanner
spanner.projects.instances.databases.getDdl
View
API Only
GCP Spanner
spanner.projects.instances.databases.updateDdl
Edit
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.list
View
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.create
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.Create
Create
API Only
GCP Spanner
spanner.projects.instances.operations.delete
Delete
API Only
GCP Spanner
spanner.projects.instances.operations.list
View
API Only
GCP Spanner
spanner.projects.instances.databases.patch
Edit
API Only
GCP Spanner
spanner.projects.instances.databases.getScans
View
API Only
GCP Spanner
spanner.projects.instances.operations.cancel
Delete
API Only
GCP Spanner
spanner.scans.list
View
API Only
GCP Spanner
spanner.projects.instances.backupOperations.list
View
API Only
GCP Spanner
spanner.projects.instances.backups.list
View
API Only
GCP Spanner
spanner.projects.instances.backups.create
Create
API Only
GCP Spanner
spanner.projects.instances.backups.copy
Copy
API Only
GCP Spanner
spanner.projects.instances.databaseOperations.list
View
API Only
GCP Spanner
spanner.projects.instances.databases.databaseRoles.list
View
API Only
GCP Spanner
spanner.projects.instances.databases.list
View
API Only
GCP Spanner
spanner.projects.instances.databases.create
Create
API Only
GCP Spanner
spanner.projects.instances.databases.restore
Create
API Only
GCP Spanner
spanner.projects.instanceConfigOperations.list
View
API Only
GCP Spanner
spanner.projects.instanceConfigs.list
View
API Only
GCP Spanner
spanner.projects.instanceConfigs.create
Create
API Only
GCP Spanner
spanner.projects.instances.list
View
API Only
GCP Spanner
spanner.projects.instances.create
Create
API Only
GCP Spanner
spanner.projects.instances.databases.getIamPolicy
View
API Only
GCP Spanner
spanner.projects.instances.databases.setIamPolicy
Create
API Only
GCP Spanner
spanner.projects.instances.databases.databaseRoles.testIamPermissions
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.beginTransaction
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.commit
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.executeDml
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.executeSql
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.executeStreamingSql
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.partitionQuery
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.partitionRead
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.read
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.rollback
Create
API Only
GCP Spanner
spanner.projects.instances.databases.sessions.streamingRead
Create
API Only
GCP Cloud Data Catalog
datacatalog.catalog.search
Search
API Only
GCP Cloud Data Catalog
datacatalog.entries.lookup
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.delete
Delete
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.get
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.patch
Edit
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.operations.list
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.operations.cancel
Delete
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.modifyEntryContacts
Edit
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.modifyEntryOverview
Edit
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.tagTemplates.fields.enumValues.rename
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.replace
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.star
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.unstar
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.list
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.import
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.list
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.tagTemplates.fields.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.list
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.tagTemplates.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.tags.list
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.tags.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.entryGroups.entries.tags.reconcile
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.list
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.create
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.export
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.import
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.getIamPolicy
View
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.setIamPolicy
Create
API Only
GCP Cloud Data Catalog
datacatalog.projects.locations.taxonomies.policyTags.testIamPermissions
Create
API Only
GCP Security Token Service
sts.introspect
Create
API Only
GCP Security Token Service
sts.oauthtoken
Create
API Only
GCP Security Token Service
sts.token
Create
API Only
GCP Digital Asset Links
digitalassetlinks.assetlinks.bulkCheck
Create
API Only
GCP Digital Asset Links
digitalassetlinks.assetlinks.check
View
API Only
GCP Digital Asset Links
digitalassetlinks.statements.list
View
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.assignments.delete
Delete
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.get
View
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.assignments.patch
Edit
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.assignments.move
Move
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.capacityCommitments.split
Create
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.assignments.list
View
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.assignments.create
Create
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.capacityCommitments.list
View
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.capacityCommitments.create
Create
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.capacityCommitments.merge
Create
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.list
View
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.reservations.create
Create
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.searchAllAssignments
Search
API Only
GCP BigQuery Reservation
bigqueryreservation.projects.locations.searchAssignments
Search
API Only
GCP Dataplex
dataplex.projects.locations.operations.delete
Delete
API Only
GCP Dataplex
dataplex.projects.locations.operations.get
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.patch
Edit
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.entities.update
Edit
API Only
GCP Dataplex
dataplex.projects.locations.list
View
API Only
GCP Dataplex
dataplex.projects.locations.operations.list
View
API Only
GCP Dataplex
dataplex.projects.locations.operations.cancel
Delete
API Only
GCP Dataplex
dataplex.projects.locations.lakes.tasks.run
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.actions.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.dataTaxonomies.attributes.list
View
API Only
GCP Dataplex
dataplex.projects.locations.dataTaxonomies.attributes.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.content.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.content.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.contentitems.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.contentitems.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.dataAttributeBindings.list
View
API Only
GCP Dataplex
dataplex.projects.locations.dataAttributeBindings.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.dataScans.list
View
API Only
GCP Dataplex
dataplex.projects.locations.dataScans.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.dataTaxonomies.list
View
API Only
GCP Dataplex
dataplex.projects.locations.dataTaxonomies.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.entities.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.entities.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.environments.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.environments.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.tasks.jobs.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.entities.partitions.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.entities.partitions.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.environments.sessions.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.tasks.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.tasks.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.list
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.create
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.getIamPolicy
View
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.setIamPolicy
Create
API Only
GCP Dataplex
dataplex.projects.locations.lakes.zones.assets.testIamPermissions
Create
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.delete
Delete
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.get
View
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.patch
Edit
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.subscribe
Create
API Only
GCP Analytics Hub
analyticshub.organizations.locations.dataExchanges.list
View
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.list
View
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.create
Create
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.list
View
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.create
Create
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.getIamPolicy
View
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.setIamPolicy
Create
API Only
GCP Analytics Hub
analyticshub.projects.locations.dataExchanges.listings.testIamPermissions
Create
API Only
GCP Network Services
networkservices.projects.locations.tlsRoutes.delete
Delete
API Only
GCP Network Services
networkservices.projects.locations.tlsRoutes.get
View
API Only
GCP Network Services
networkservices.projects.locations.tlsRoutes.patch
Edit
API Only
GCP Network Services
networkservices.projects.locations.list
View
API Only
GCP Network Services
networkservices.projects.locations.operations.list
View
API Only
GCP Network Services
networkservices.projects.locations.operations.cancel
Delete
API Only
GCP Network Services
networkservices.projects.locations.endpointPolicies.list
View
API Only
GCP Network Services
networkservices.projects.locations.endpointPolicies.create
Create
API Only
GCP Network Services
networkservices.projects.locations.gateways.list
View
API Only
GCP Network Services
networkservices.projects.locations.gateways.create
Create
API Only
GCP Network Services
networkservices.projects.locations.grpcRoutes.list
View
API Only
GCP Network Services
networkservices.projects.locations.grpcRoutes.create
Create
API Only
GCP Network Services
networkservices.projects.locations.httpRoutes.list
View
API Only
GCP Network Services
networkservices.projects.locations.httpRoutes.create
Create
API Only
GCP Network Services
networkservices.projects.locations.meshes.list
View
API Only
GCP Network Services
networkservices.projects.locations.meshes.create
Create
API Only
GCP Network Services
networkservices.projects.locations.serviceBindings.list
View
API Only
GCP Network Services
networkservices.projects.locations.serviceBindings.create
Create
API Only
GCP Network Services
networkservices.projects.locations.tcpRoutes.list
View
API Only
GCP Network Services
networkservices.projects.locations.tcpRoutes.create
Create
API Only
GCP Network Services
networkservices.projects.locations.tlsRoutes.list
View
API Only
GCP Network Services
networkservices.projects.locations.tlsRoutes.create
Create
API Only
GCP Network Services
networkservices.projects.locations.serviceBindings.getIamPolicy
View
API Only
GCP Network Services
networkservices.projects.locations.serviceBindings.setIamPolicy
Create
API Only
GCP Network Services
networkservices.projects.locations.serviceBindings.testIamPermissions
Create
API Only
GCP Private Catalog
cloudprivatecatalog.organizations.catalogs.search
Search
API Only
GCP Private Catalog
cloudprivatecatalog.organizations.products.search
Search
API Only
GCP Private Catalog
cloudprivatecatalog.organizations.versions.search
Search
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.list
View
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.create
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.delete
Delete
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.get
View
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.update
Edit
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.addons
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.legacyAbac
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.locations
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.logging
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.master
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.monitoring
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.list
View
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.create
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.delete
Delete
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.get
View
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.autoscaling
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.setManagement
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.setSize
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.update
Edit
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.nodePools.rollback
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.resourceLabels
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.completeIpRotation
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.setMaintenancePolicy
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.setMasterAuth
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.setNetworkPolicy
Create
API Only
GCP Kubernetes Engine
container.projects.zones.clusters.startIpRotation
Start
API Only
GCP Kubernetes Engine
container.projects.zones.operations.list
View
API Only
GCP Kubernetes Engine
container.projects.zones.operations.get
View
API Only
GCP Kubernetes Engine
container.projects.zones.operations.cancel
Delete
API Only
GCP Kubernetes Engine
container.projects.zones.getServerconfig
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.delete
Delete
API Only
GCP Kubernetes Engine
container.projects.locations.operations.get
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.update
Edit
API Only
GCP Kubernetes Engine
container.projects.locations.getServerConfig
View
API Only
GCP Kubernetes Engine
container.projects.locations.operations.cancel
Delete
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.checkAutopilotCompatibility
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.completeIpRotation
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.completeUpgrade
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.rollback
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setAddons
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.setAutoscaling
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setLegacyAbac
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setLocations
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setLogging
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setMaintenancePolicy
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.setManagement
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setMasterAuth
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setMonitoring
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setNetworkPolicy
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.setResourceLabels
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.setSize
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.startIpRotation
Start
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.updateMaster
Edit
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.well_known.getOpenid_configuration
View
API Only
GCP Kubernetes Engine
container.projects.aggregated.usableSubnetworks.list
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.list
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.create
Create
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.getJwks
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.list
View
API Only
GCP Kubernetes Engine
container.projects.locations.clusters.nodePools.create
Create
API Only
GCP Kubernetes Engine
container.projects.locations.operations.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.trustConfigs.delete
Delete
API Only
GCP Certificate Manager
certificatemanager.projects.locations.trustConfigs.get
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.trustConfigs.patch
Edit
API Only
GCP Certificate Manager
certificatemanager.projects.locations.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.operations.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.operations.cancel
Delete
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificateIssuanceConfigs.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificateIssuanceConfigs.create
Create
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificateMaps.certificateMapEntries.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificateMaps.certificateMapEntries.create
Create
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificateMaps.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificateMaps.create
Create
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificates.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.certificates.create
Create
API Only
GCP Certificate Manager
certificatemanager.projects.locations.dnsAuthorizations.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.dnsAuthorizations.create
Create
API Only
GCP Certificate Manager
certificatemanager.projects.locations.trustConfigs.list
View
API Only
GCP Certificate Manager
certificatemanager.projects.locations.trustConfigs.create
Create
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.delete
Delete
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.get
View
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.patch
Edit
API Only
GCP Scheduler
cloudscheduler.projects.locations.list
View
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.pause
Create
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.resume
Start
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.run
Create
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.list
View
API Only
GCP Scheduler
cloudscheduler.projects.locations.jobs.create
Create
API Only
GCP Identity and Access Management (IAM)
iam.policies.delete
Delete
API Only
GCP Identity and Access Management (IAM)
iam.policies.operations.get
View
API Only
GCP Identity and Access Management (IAM)
iam.policies.update
Edit
API Only
GCP Identity and Access Management (IAM)
iam.policies.listPolicies
View
API Only
GCP Identity and Access Management (IAM)
iam.policies.createPolicy
Create
API Only
GCP Natural Language
language.documents.analyzeEntities
Create
API Only
GCP Natural Language
language.documents.analyzeEntitySentiment
Create
API Only
GCP Natural Language
language.documents.analyzeSentiment
Create
API Only
GCP Natural Language
language.documents.analyzeSyntax
Create
API Only
GCP Natural Language
language.documents.annotateText
Create
API Only
GCP Natural Language
language.documents.classifyText
Create
API Only
GCP Natural Language
language.documents.moderateText
Create
API Only
GCP Service Usage
serviceusage.operations.list
View
API Only
GCP Service Usage
serviceusage.operations.delete
Delete
API Only
GCP Service Usage
serviceusage.services.get
View
API Only
GCP Service Usage
serviceusage.operations.cancel
Delete
API Only
GCP Service Usage
serviceusage.services.disable
Edit
API Only
GCP Service Usage
serviceusage.services.enable
Enable
API Only
GCP Service Usage
serviceusage.services.list
View
API Only
GCP Service Usage
serviceusage.services.Enable
Enable
API Only
GCP Service Usage
serviceusage.services.Get
View
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.list
View
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.insert
Create
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.delete
Delete
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.get
View
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.patch
Edit
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.update
Edit
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.cancelPreview
Delete
API Only
GCP Deployment Manager V2
deploymentmanager.manifests.list
View
API Only
GCP Deployment Manager V2
deploymentmanager.manifests.get
View
API Only
GCP Deployment Manager V2
deploymentmanager.resources.list
View
API Only
GCP Deployment Manager V2
deploymentmanager.resources.get
View
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.stop
Stop
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.getIamPolicy
View
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.setIamPolicy
Create
API Only
GCP Deployment Manager V2
deploymentmanager.deployments.testIamPermissions
Create
API Only
GCP Deployment Manager V2
deploymentmanager.operations.list
View
API Only
GCP Deployment Manager V2
deploymentmanager.operations.get
View
API Only
GCP Deployment Manager V2
deploymentmanager.types.list
View
API Only
GCP API Gateway
apigateway.projects.locations.operations.delete
Delete
API Only
GCP API Gateway
apigateway.projects.locations.operations.get
View
API Only
GCP API Gateway
apigateway.projects.locations.gateways.patch
Edit
API Only
GCP API Gateway
apigateway.projects.locations.list
View
API Only
GCP API Gateway
apigateway.projects.locations.operations.list
View
API Only
GCP API Gateway
apigateway.projects.locations.operations.cancel
Delete
API Only
GCP API Gateway
apigateway.projects.locations.apis.list
View
API Only
GCP API Gateway
apigateway.projects.locations.apis.create
Create
API Only
GCP API Gateway
apigateway.projects.locations.apis.configs.list
View
API Only
GCP API Gateway
apigateway.projects.locations.apis.configs.create
Create
API Only
GCP API Gateway
apigateway.projects.locations.gateways.list
View
API Only
GCP API Gateway
apigateway.projects.locations.gateways.create
Create
API Only
GCP API Gateway
apigateway.projects.locations.gateways.getIamPolicy
View
API Only
GCP API Gateway
apigateway.projects.locations.gateways.setIamPolicy
Create
API Only
GCP API Gateway
apigateway.projects.locations.gateways.testIamPermissions
Create
API Only
GCP TPU
tpu.projects.locations.operations.delete
Delete
API Only
GCP TPU
tpu.projects.locations.runtimeVersions.get
View
API Only
GCP TPU
tpu.projects.locations.nodes.patch
Edit
API Only
GCP TPU
tpu.projects.locations.list
View
API Only
GCP TPU
tpu.projects.locations.operations.list
View
API Only
GCP TPU
tpu.projects.locations.operations.cancel
Delete
API Only
GCP TPU
tpu.projects.locations.nodes.getGuestAttributes
View
API Only
GCP TPU
tpu.projects.locations.nodes.start
Start
API Only
GCP TPU
tpu.projects.locations.nodes.stop
Stop
API Only
GCP TPU
tpu.projects.locations.acceleratorTypes.list
View
API Only
GCP TPU
tpu.projects.locations.nodes.list
View
API Only
GCP TPU
tpu.projects.locations.nodes.create
Create
API Only
GCP TPU
tpu.projects.locations.runtimeVersions.list
View
API Only
GCP TPU
tpu.projects.locations.generateServiceIdentity
Create
API Only
GCP Access Approval
accessapproval.projects.deleteAccessApprovalSettings
Delete
API Only
GCP Access Approval
accessapproval.projects.approvalRequests.get
View
API Only
GCP Access Approval
accessapproval.projects.updateAccessApprovalSettings
Edit
API Only
GCP Access Approval
accessapproval.projects.approvalRequests.approve
Approve
API Only
GCP Access Approval
accessapproval.projects.approvalRequests.dismiss
Create
API Only
GCP Access Approval
accessapproval.projects.approvalRequests.invalidate
Create
API Only
GCP Access Approval
accessapproval.projects.approvalRequests.list
View
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.delete
Delete
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.get
View
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.patch
Edit
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.getNotes
View
API Only
GCP Container Analysis
containeranalysis.projects.notes.occurrences.list
View
API Only
GCP Container Analysis
containeranalysis.projects.notes.list
View
API Only
GCP Container Analysis
containeranalysis.projects.notes.create
Create
API Only
GCP Container Analysis
containeranalysis.projects.notes.Create
Create
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.list
View
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.create
Create
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.Create
Create
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.getVulnerabilitySummary
View
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.getIamPolicy
View
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.setIamPolicy
Create
API Only
GCP Container Analysis
containeranalysis.projects.occurrences.testIamPermissions
Create
API Only
GCP Firebase Hosting
firebasehosting.operations.delete
Delete
API Only
GCP Firebase Hosting
firebasehosting.operations.list
View
API Only
GCP Firebase Hosting
firebasehosting.operations.cancel
Delete
API Only
GCP Firebase ML
firebaseml.operations.delete
Delete
API Only
GCP Firebase ML
firebaseml.operations.list
View
API Only
GCP Firebase ML
firebaseml.operations.cancel
Delete
API Only
GCP Secret Manager
secretmanager.projects.secrets.delete
Delete
API Only
GCP Secret Manager
secretmanager.projects.secrets.versions.get
View
API Only
GCP Secret Manager
secretmanager.projects.secrets.patch
Edit
API Only
GCP Secret Manager
secretmanager.projects.locations.list
View
API Only
GCP Secret Manager
secretmanager.projects.secrets.versions.access
View
API Only
GCP Secret Manager
secretmanager.projects.secrets.versions.destroy
Delete
API Only
GCP Secret Manager
secretmanager.projects.secrets.versions.disable
Edit
API Only
GCP Secret Manager
secretmanager.projects.secrets.versions.enable
Enable
API Only
GCP Secret Manager
secretmanager.projects.secrets.list
View
API Only
GCP Secret Manager
secretmanager.projects.secrets.create
Create
API Only
GCP Secret Manager
secretmanager.projects.secrets.versions.list
View
API Only
GCP Secret Manager
secretmanager.projects.secrets.addVersion
Create
API Only
GCP Secret Manager
secretmanager.projects.secrets.getIamPolicy
View
API Only
GCP Secret Manager
secretmanager.projects.secrets.setIamPolicy
Create
API Only
GCP Secret Manager
secretmanager.projects.secrets.testIamPermissions
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.models.versions.delete
Delete
API Only
GCP AI Platform Training and Prediction
ml.projects.operations.get
View
API Only
GCP AI Platform Training and Prediction
ml.projects.models.versions.patch
Edit
API Only
GCP AI Platform Training and Prediction
ml.projects.operations.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.addMeasurement
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.operations.cancel
Delete
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.checkEarlyStoppingState
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.complete
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.explain
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.getConfig
View
API Only
GCP AI Platform Training and Prediction
ml.projects.predict
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.models.versions.setDefault
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.stop
Stop
API Only
GCP AI Platform Training and Prediction
ml.projects.jobs.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.jobs.create
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.models.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.models.create
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.create
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.create
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.listOptimalTrials
View
API Only
GCP AI Platform Training and Prediction
ml.projects.locations.studies.trials.suggest
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.models.versions.list
View
API Only
GCP AI Platform Training and Prediction
ml.projects.models.versions.create
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.models.getIamPolicy
View
API Only
GCP AI Platform Training and Prediction
ml.projects.models.setIamPolicy
Create
API Only
GCP AI Platform Training and Prediction
ml.projects.models.testIamPermissions
Create
API Only
GCP Resource Settings
resourcesettings.projects.settings.get
View
API Only
GCP Resource Settings
resourcesettings.projects.settings.patch
Edit
API Only
GCP Resource Settings
resourcesettings.projects.settings.list
View
API Only
GCP Service Control
servicecontrol.services.check
Create
API Only
GCP Service Control
servicecontrol.services.report
Create
API Only
GCP Identity
cloudidentity.devices.list
View
API Only
GCP Identity
cloudidentity.devices.create
Create
API Only
GCP Identity
cloudidentity.groups.list
View
API Only
GCP Identity
cloudidentity.groups.create
Create
API Only
GCP Identity
cloudidentity.groups.lookup
View
API Only
GCP Identity
cloudidentity.groups.search
Search
API Only
GCP Identity
cloudidentity.inboundSamlSsoProfiles.list
View
API Only
GCP Identity
cloudidentity.inboundSamlSsoProfiles.create
Create
API Only
GCP Identity
cloudidentity.inboundSsoAssignments.list
View
API Only
GCP Identity
cloudidentity.inboundSsoAssignments.create
Create
API Only
GCP Identity
cloudidentity.inboundSsoAssignments.delete
Delete
API Only
GCP Identity
cloudidentity.inboundSsoAssignments.get
View
API Only
GCP Identity
cloudidentity.inboundSsoAssignments.patch
Edit
API Only
GCP Identity
cloudidentity.devices.deviceUsers.approve
Approve
API Only
GCP Identity
cloudidentity.devices.deviceUsers.block
Create
API Only
GCP Identity
cloudidentity.customers.userinvitations.cancel
Delete
API Only
GCP Identity
cloudidentity.devices.deviceUsers.cancelWipe
Delete
API Only
GCP Identity
cloudidentity.customers.userinvitations.isInvitableUser
View
API Only
GCP Identity
cloudidentity.groups.memberships.modifyMembershipRoles
Edit
API Only
GCP Identity
cloudidentity.customers.userinvitations.send
Send
API Only
GCP Identity
cloudidentity.devices.deviceUsers.wipe
Create
API Only
GCP Identity
cloudidentity.devices.deviceUsers.clientStates.list
View
API Only
GCP Identity
cloudidentity.devices.deviceUsers.list
View
API Only
GCP Identity
cloudidentity.inboundSamlSsoProfiles.idpCredentials.list
View
API Only
GCP Identity
cloudidentity.inboundSamlSsoProfiles.idpCredentials.add
Create
API Only
GCP Identity
cloudidentity.groups.memberships.list
View
API Only
GCP Identity
cloudidentity.groups.memberships.create
Create
API Only
GCP Identity
cloudidentity.groups.memberships.checkTransitiveMembership
View
API Only
GCP Identity
cloudidentity.groups.memberships.getMembershipGraph
View
API Only
GCP Identity
cloudidentity.groups.memberships.lookup
View
API Only
GCP Identity
cloudidentity.groups.memberships.searchDirectGroups
Search
API Only
GCP Identity
cloudidentity.groups.memberships.searchTransitiveGroups
Search
API Only
GCP Identity
cloudidentity.groups.memberships.searchTransitiveMemberships
Search
API Only
GCP Identity
cloudidentity.customers.userinvitations.list
View
API Only
GCP Identity
cloudidentity.devices.deviceUsers.lookup
View
API Only
GCP Eventarc
eventarc.projects.locations.triggers.delete
Delete
API Only
GCP Eventarc
eventarc.projects.locations.triggers.get
View
API Only
GCP Eventarc
eventarc.projects.locations.triggers.patch
Edit
API Only
GCP Eventarc
eventarc.projects.locations.list
View
API Only
GCP Eventarc
eventarc.projects.locations.operations.list
View
API Only
GCP Eventarc
eventarc.projects.locations.operations.cancel
Delete
API Only
GCP Eventarc
eventarc.projects.locations.channelConnections.list
View
API Only
GCP Eventarc
eventarc.projects.locations.channelConnections.create
Create
API Only
GCP Eventarc
eventarc.projects.locations.channels.list
View
API Only
GCP Eventarc
eventarc.projects.locations.channels.create
Create
API Only
GCP Eventarc
eventarc.projects.locations.providers.list
View
API Only
GCP Eventarc
eventarc.projects.locations.triggers.list
View
API Only
GCP Eventarc
eventarc.projects.locations.triggers.create
Create
API Only
GCP Eventarc
eventarc.projects.locations.triggers.getIamPolicy
View
API Only
GCP Eventarc
eventarc.projects.locations.triggers.setIamPolicy
Create
API Only
GCP Eventarc
eventarc.projects.locations.triggers.testIamPermissions
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.list
View
API Only
GCP Dataproc
dataproc.projects.regions.clusters.create
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.delete
Delete
API Only
GCP Dataproc
dataproc.projects.regions.clusters.get
View
API Only
GCP Dataproc
dataproc.projects.regions.clusters.patch
Edit
API Only
GCP Dataproc
dataproc.projects.regions.clusters.diagnose
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.repair
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.start
Start
API Only
GCP Dataproc
dataproc.projects.regions.clusters.stop
Stop
API Only
GCP Dataproc
dataproc.projects.regions.jobs.list
View
API Only
GCP Dataproc
dataproc.projects.regions.jobs.delete
Delete
API Only
GCP Dataproc
dataproc.projects.regions.jobs.get
View
API Only
GCP Dataproc
dataproc.projects.regions.jobs.patch
Edit
API Only
GCP Dataproc
dataproc.projects.regions.jobs.cancel
Delete
API Only
GCP Dataproc
dataproc.projects.regions.jobs.submit
Create
API Only
GCP Dataproc
dataproc.projects.regions.jobs.submitAsOperation
Create
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.delete
Delete
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.get
View
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.update
Edit
API Only
GCP Dataproc
dataproc.projects.regions.operations.cancel
Delete
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.instantiate
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.nodeGroups.resize
Edit
API Only
GCP Dataproc
dataproc.projects.regions.autoscalingPolicies.list
View
API Only
GCP Dataproc
dataproc.projects.regions.autoscalingPolicies.create
Create
API Only
GCP Dataproc
dataproc.projects.locations.es.list
View
API Only
GCP Dataproc
dataproc.projects.locations.es.create
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.nodeGroups.create
Create
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.list
View
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.create
Create
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.instantiateInline
Create
API Only
GCP Dataproc
dataproc.projects.regions.clusters.injectCredentials
Create
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.getIamPolicy
View
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.setIamPolicy
Create
API Only
GCP Dataproc
dataproc.projects.regions.workflowTemplates.testIamPermissions
Create
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.describeConversionWorkspaceRevisions
View
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.describeDatabaseEntities
View
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.searchBackgroundJobs
Search
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.generateSshScript
Create
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.delete
Delete
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.get
View
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.patch
Edit
API Only
GCP Database Migration
datamigration.projects.locations.list
View
API Only
GCP Database Migration
datamigration.projects.locations.operations.list
View
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.apply
Edit
API Only
GCP Database Migration
datamigration.projects.locations.operations.cancel
Delete
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.commit
Create
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.convert
Create
API Only
GCP Database Migration
datamigration.projects.locations.fetchStaticIps
View
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.promote
Create
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.restart
Reboot
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.resume
Start
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.rollback
Create
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.seed
Create
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.start
Start
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.stop
Stop
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.verify
Create
API Only
GCP Database Migration
datamigration.projects.locations.connectionProfiles.list
View
API Only
GCP Database Migration
datamigration.projects.locations.connectionProfiles.create
Create
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.list
View
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.create
Create
API Only
GCP Database Migration
datamigration.projects.locations.conversionWorkspaces.mappingRules.import
Create
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.list
View
API Only
GCP Database Migration
datamigration.projects.locations.migrationJobs.create
Create
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.list
View
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.create
Create
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.getIamPolicy
View
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.setIamPolicy
Create
API Only
GCP Database Migration
datamigration.projects.locations.privateConnections.testIamPermissions
Create
API Only
GCP Network Security
networksecurity.projects.locations.addressGroups.addItems
Create
API Only
GCP Network Security
networksecurity.projects.locations.addressGroups.cloneItems
Create
API Only
GCP Network Security
networksecurity.projects.locations.addressGroups.listReferences
View
API Only
GCP Network Security
networksecurity.projects.locations.addressGroups.removeItems
Delete
API Only
GCP Network Security
networksecurity.projects.locations.urlLists.delete
Delete
API Only
GCP Network Security
networksecurity.projects.locations.urlLists.get
View
API Only
GCP Network Security
networksecurity.projects.locations.urlLists.patch
Edit
API Only
GCP Network Security
networksecurity.projects.locations.list
View
API Only
GCP Network Security
networksecurity.projects.locations.operations.list
View
API Only
GCP Network Security
networksecurity.projects.locations.operations.cancel
Delete
API Only
GCP Network Security
networksecurity.projects.locations.addressGroups.list
View
API Only
GCP Network Security
networksecurity.projects.locations.addressGroups.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.authorizationPolicies.list
View
API Only
GCP Network Security
networksecurity.projects.locations.authorizationPolicies.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.clientTlsPolicies.list
View
API Only
GCP Network Security
networksecurity.projects.locations.clientTlsPolicies.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.gatewaySecurityPolicies.list
View
API Only
GCP Network Security
networksecurity.projects.locations.gatewaySecurityPolicies.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.gatewaySecurityPolicies.rules.list
View
API Only
GCP Network Security
networksecurity.projects.locations.gatewaySecurityPolicies.rules.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.serverTlsPolicies.list
View
API Only
GCP Network Security
networksecurity.projects.locations.serverTlsPolicies.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.tlsInspectionPolicies.list
View
API Only
GCP Network Security
networksecurity.projects.locations.tlsInspectionPolicies.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.urlLists.list
View
API Only
GCP Network Security
networksecurity.projects.locations.urlLists.create
Create
API Only
GCP Network Security
networksecurity.projects.locations.serverTlsPolicies.getIamPolicy
View
API Only
GCP Network Security
networksecurity.projects.locations.serverTlsPolicies.setIamPolicy
Create
API Only
GCP Network Security
networksecurity.projects.locations.serverTlsPolicies.testIamPermissions
Create
API Only
GCP Security Command Center
securitycenter.projects.securityHealthAnalyticsSettings.customModules.delete
Delete
API Only
GCP Security Command Center
securitycenter.projects.securityHealthAnalyticsSettings.effectiveCustomModules.get
View
API Only
GCP Security Command Center
securitycenter.projects.sources.findings.externalSystems.patch
Edit
API Only
GCP Security Command Center
securitycenter.organizations.operations.cancel
Delete
API Only
GCP Security Command Center
securitycenter.projects.sources.findings.setMute
Create
API Only
GCP Security Command Center
securitycenter.projects.sources.findings.setState
Create
API Only
GCP Security Command Center
securitycenter.projects.assets.list
View
API Only
GCP Security Command Center
securitycenter.projects.assets.group
Create
API Only
GCP Security Command Center
securitycenter.organizations.assets.runDiscovery
Create
API Only
GCP Security Command Center
securitycenter.projects.bigQueryExports.list
View
API Only
GCP Security Command Center
securitycenter.projects.bigQueryExports.create
Create
API Only
GCP Security Command Center
securitycenter.projects.securityHealthAnalyticsSettings.customModules.list
View
API Only
GCP Security Command Center
securitycenter.projects.securityHealthAnalyticsSettings.customModules.create
Create
API Only
GCP Security Command Center
securitycenter.projects.securityHealthAnalyticsSettings.customModules.listDescendant
View
API Only
GCP Security Command Center
securitycenter.projects.securityHealthAnalyticsSettings.effectiveCustomModules.list
View
API Only
GCP Security Command Center
securitycenter.projects.sources.findings.list
View
API Only
GCP Security Command Center
securitycenter.organizations.sources.findings.create
Create
API Only
GCP Security Command Center
securitycenter.projects.findings.bulkMute
Create
API Only
GCP Security Command Center
securitycenter.projects.sources.findings.group
Create
API Only
GCP Security Command Center
securitycenter.projects.muteConfigs.list
View
API Only
GCP Security Command Center
securitycenter.projects.muteConfigs.create
Create
API Only
GCP Security Command Center
securitycenter.projects.notificationConfigs.list
View
API Only
GCP Security Command Center
securitycenter.projects.notificationConfigs.create
Create
API Only
GCP Security Command Center
securitycenter.projects.sources.list
View
API Only
GCP Security Command Center
securitycenter.organizations.sources.create
Create
API Only
GCP Security Command Center
securitycenter.organizations.sources.getIamPolicy
View
API Only
GCP Security Command Center
securitycenter.organizations.sources.setIamPolicy
Create
API Only
GCP Security Command Center
securitycenter.organizations.sources.testIamPermissions
Create
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.delete
Delete
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.get
View
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.patch
Edit
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.list
View
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.create
Create
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.compute
View
API Only
GCP Essential Contacts
essentialcontacts.projects.contacts.sendTestMessage
Send
API Only
GCP Policy Simulator
policysimulator.projects.locations.replays.operations.list
View
API Only
GCP Policy Simulator
policysimulator.projects.locations.replays.create
Create
API Only
GCP Policy Simulator
policysimulator.projects.locations.replays.results.list
View
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.list
View
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.create
Create
API Only
GCP Access Context Manager
accesscontextmanager.organizations.gcpUserAccessBindings.delete
Delete
API Only
GCP Access Context Manager
accesscontextmanager.organizations.gcpUserAccessBindings.get
View
API Only
GCP Access Context Manager
accesscontextmanager.organizations.gcpUserAccessBindings.patch
Edit
API Only
GCP Access Context Manager
accesscontextmanager.operations.cancel
Delete
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.accessLevels.list
View
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.accessLevels.create
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.accessLevels.replaceAll
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.authorizedOrgsDescs.list
View
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.authorizedOrgsDescs.create
Create
API Only
GCP Access Context Manager
accesscontextmanager.organizations.gcpUserAccessBindings.list
View
API Only
GCP Access Context Manager
accesscontextmanager.organizations.gcpUserAccessBindings.create
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.servicePerimeters.list
View
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.servicePerimeters.create
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.servicePerimeters.commit
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.servicePerimeters.replaceAll
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.getIamPolicy
View
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.setIamPolicy
Create
API Only
GCP Access Context Manager
accesscontextmanager.accessPolicies.servicePerimeters.testIamPermissions
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.list
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.create
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.operations.list
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.versions.delete
Delete
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.versions.get
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.versions.patch
Edit
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.operations.cancel
Delete
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.copy
Copy
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.undelete
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.associations.list
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.associations.create
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.list
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.create
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.versions.list
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.versions.create
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.products.icons.upload
Upload
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.getIamPolicy
View
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.setIamPolicy
Create
API Only
GCP Private Catalog Producer
cloudprivatecatalogproducer.catalogs.testIamPermissions
Create
API Only
GCP Memorystore for Memcached
memcache.projects.locations.instances.rescheduleMaintenance
Create
API Only
GCP Memorystore for Memcached
memcache.projects.locations.operations.delete
Delete
API Only
GCP Memorystore for Memcached
memcache.projects.locations.operations.get
View
API Only
GCP Memorystore for Memcached
memcache.projects.locations.instances.patch
Edit
API Only
GCP Memorystore for Memcached
memcache.projects.locations.list
View
API Only
GCP Memorystore for Memcached
memcache.projects.locations.operations.list
View
API Only
GCP Memorystore for Memcached
memcache.projects.locations.instances.applyParameters
Edit
API Only
GCP Memorystore for Memcached
memcache.projects.locations.operations.cancel
Delete
API Only
GCP Memorystore for Memcached
memcache.projects.locations.instances.updateParameters
Edit
API Only
GCP Memorystore for Memcached
memcache.projects.locations.instances.list
View
API Only
GCP Memorystore for Memcached
memcache.projects.locations.instances.create
Create
API Only
GCP Transcoder
transcoder.projects.locations.jobTemplates.delete
Delete
API Only
GCP Transcoder
transcoder.projects.locations.jobTemplates.get
View
API Only
GCP Transcoder
transcoder.projects.locations.jobTemplates.list
View
API Only
GCP Transcoder
transcoder.projects.locations.jobTemplates.create
Create
API Only
GCP Transcoder
transcoder.projects.locations.jobs.list
View
API Only
GCP Transcoder
transcoder.projects.locations.jobs.create
Create
API Only
GCP Storage Transfer
storagetransfer.googleServiceAccounts.get
View
API Only
GCP Storage Transfer
storagetransfer.projects.agentPools.list
View
API Only
GCP Storage Transfer
storagetransfer.projects.agentPools.create
Create
API Only
GCP Storage Transfer
storagetransfer.transferJobs.list
View
API Only
GCP Storage Transfer
storagetransfer.transferJobs.create
Create
API Only
GCP Storage Transfer
storagetransfer.transferJobs.delete
Delete
API Only
GCP Storage Transfer
storagetransfer.transferJobs.get
View
API Only
GCP Storage Transfer
storagetransfer.transferJobs.patch
Edit
API Only
GCP Storage Transfer
storagetransfer.transferJobs.run
Create
API Only
GCP Storage Transfer
storagetransfer.projects.agentPools.delete
Delete
API Only
GCP Storage Transfer
storagetransfer.transferOperations.list
View
API Only
GCP Storage Transfer
storagetransfer.projects.agentPools.patch
Edit
API Only
GCP Storage Transfer
storagetransfer.transferOperations.cancel
Delete
API Only
GCP Storage Transfer
storagetransfer.transferOperations.pause
Create
API Only
GCP Storage Transfer
storagetransfer.transferOperations.resume
Start
API Only
GCP Identity-Aware Proxy
iap.projects.iap_tunnel.locations.destGroups.delete
Delete
API Only
GCP Identity-Aware Proxy
iap.projects.iap_tunnel.locations.destGroups.get
View
API Only
GCP Identity-Aware Proxy
iap.projects.iap_tunnel.locations.destGroups.patch
Edit
API Only
GCP Identity-Aware Proxy
iap.getIapSettings
View
API Only
GCP Identity-Aware Proxy
iap.updateIapSettings
Edit
API Only
GCP Identity-Aware Proxy
iap.projects.brands.identityAwareProxyClients.resetSecret
Edit
API Only
GCP Identity-Aware Proxy
iap.validateAttributeExpression
Create
API Only
GCP Identity-Aware Proxy
iap.projects.brands.list
View
API Only
GCP Identity-Aware Proxy
iap.projects.brands.create
Create
API Only
GCP Identity-Aware Proxy
iap.projects.iap_tunnel.locations.destGroups.list
View
API Only
GCP Identity-Aware Proxy
iap.projects.iap_tunnel.locations.destGroups.create
Create
API Only
GCP Identity-Aware Proxy
iap.projects.brands.identityAwareProxyClients.list
View
API Only
GCP Identity-Aware Proxy
iap.projects.brands.identityAwareProxyClients.create
Create
API Only
GCP Identity-Aware Proxy
iap.getIamPolicy
View
API Only
GCP Identity-Aware Proxy
iap.setIamPolicy
Create
API Only
GCP Identity-Aware Proxy
iap.testIamPermissions
Create
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.fetchCaCerts
View
API Only
GCP Certificate Authority
privateca.projects.locations.operations.delete
Delete
API Only
GCP Certificate Authority
privateca.projects.locations.operations.get
View
API Only
GCP Certificate Authority
privateca.projects.locations.certificateTemplates.patch
Edit
API Only
GCP Certificate Authority
privateca.projects.locations.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.operations.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.activate
Activate
API Only
GCP Certificate Authority
privateca.projects.locations.operations.cancel
Delete
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.disable
Edit
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.enable
Enable
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.fetch
View
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificates.revoke
Delete
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.undelete
Create
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.create
Create
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.create
Create
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificateAuthorities.certificateRevocationLists.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.certificateTemplates.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.certificateTemplates.create
Create
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificates.list
View
API Only
GCP Certificate Authority
privateca.projects.locations.caPools.certificates.create
Create
API Only
GCP Certificate Authority
privateca.projects.locations.certificateTemplates.getIamPolicy
View
API Only
GCP Certificate Authority
privateca.projects.locations.certificateTemplates.setIamPolicy
Create
API Only
GCP Certificate Authority
privateca.projects.locations.certificateTemplates.testIamPermissions
Create
API Only
GCP Life Sciences
lifesciences.projects.locations.operations.get
View
API Only
GCP Life Sciences
lifesciences.projects.locations.list
View
API Only
GCP Life Sciences
lifesciences.projects.locations.operations.list
View
API Only
GCP Life Sciences
lifesciences.projects.locations.operations.cancel
Delete
API Only
GCP Life Sciences
lifesciences.projects.locations.pipelines.run
Create
API Only
GCP Tool Results
toolresults.projects.histories.list
View
API Only
GCP Tool Results
toolresults.projects.histories.create
Create
API Only
GCP Tool Results
toolresults.projects.histories.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.create
Create
API Only
GCP Tool Results
toolresults.projects.histories.executions.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.patch
Edit
API Only
GCP Tool Results
toolresults.projects.histories.executions.clusters.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.clusters.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.environments.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.environments.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.create
Create
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.patch
Edit
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.getPerfMetricsSummary
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.perfMetricsSummary.create
Create
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.perfSampleSeries.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.perfSampleSeries.create
Create
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.perfSampleSeries.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.perfSampleSeries.samples.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.perfSampleSeries.samples.Create
Create
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.testCases.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.testCases.get
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.thumbnails.list
View
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.publishXunitXmlFiles
Create
API Only
GCP Tool Results
toolresults.projects.getSettings
View
API Only
GCP Tool Results
toolresults.projects.initializeSettings
Create
API Only
GCP Tool Results
toolresults.projects.histories.executions.steps.accessibilityClusters
View
API Only
GCP API Keys
apikeys.keys.lookupKey
View
API Only
GCP API Keys
apikeys.projects.locations.keys.delete
Delete
API Only
GCP API Keys
apikeys.projects.locations.keys.get
View
API Only
GCP API Keys
apikeys.projects.locations.keys.patch
Edit
API Only
GCP API Keys
apikeys.projects.locations.keys.getKeyString
View
API Only
GCP API Keys
apikeys.projects.locations.keys.undelete
Create
API Only
GCP API Keys
apikeys.projects.locations.keys.list
View
API Only
GCP API Keys
apikeys.projects.locations.keys.create
Create
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnectors.reportStatus
Create
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnectors.resolveInstanceConfig
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.operations.delete
Delete
API Only
GCP BeyondCorp
beyondcorp.projects.locations.operations.get
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnectors.patch
Edit
API Only
GCP BeyondCorp
beyondcorp.projects.locations.list
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.operations.list
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.operations.cancel
Delete
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnections.list
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnections.create
Create
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnections.resolve
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnectors.list
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appConnectors.create
Create
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appGateways.list
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.appGateways.create
Create
API Only
GCP BeyondCorp
beyondcorp.projects.locations.clientGateways.getIamPolicy
View
API Only
GCP BeyondCorp
beyondcorp.projects.locations.clientGateways.setIamPolicy
Create
API Only
GCP BeyondCorp
beyondcorp.projects.locations.clientGateways.testIamPermissions
Create
API Only
GCP Firebase Rules
firebaserules.projects.rulesets.delete
Delete
API Only
GCP Firebase Rules
firebaserules.projects.rulesets.get
View
API Only
GCP Firebase Rules
firebaserules.projects.releases.patch
Edit
API Only
GCP Firebase Rules
firebaserules.projects.releases.list
View
API Only
GCP Firebase Rules
firebaserules.projects.releases.create
Create
API Only
GCP Firebase Rules
firebaserules.projects.rulesets.list
View
API Only
GCP Firebase Rules
firebaserules.projects.rulesets.create
Create
API Only
GCP Firebase Rules
firebaserules.projects.releases.getExecutable
View
API Only
GCP Firebase Rules
firebaserules.projects.test
Create
API Only
GCP Dataflow
dataflow.projects.workerMessages
Create
API Only
GCP Dataflow
dataflow.projects.jobs.list
View
API Only
GCP Dataflow
dataflow.projects.jobs.create
Create
API Only
GCP Dataflow
dataflow.projects.jobs.get
View
API Only
GCP Dataflow
dataflow.projects.jobs.update
Edit
API Only
GCP Dataflow
dataflow.projects.jobs.debug.getConfig
View
API Only
GCP Dataflow
dataflow.projects.jobs.debug.sendCapture
Send
API Only
GCP Dataflow
dataflow.projects.jobs.messages.list
View
API Only
GCP Dataflow
dataflow.projects.jobs.getMetrics
View
API Only
GCP Dataflow
dataflow.projects.jobs.workItems.lease
Create
API Only
GCP Dataflow
dataflow.projects.jobs.workItems.reportStatus
Create
API Only
GCP Dataflow
dataflow.projects.jobs.snapshot
Create
API Only
GCP Dataflow
dataflow.projects.jobs.aggregated
View
API Only
GCP Dataflow
dataflow.projects.locations.workerMessages
Create
API Only
GCP Dataflow
dataflow.projects.locations.flexTemplates.launch
Create
API Only
GCP Dataflow
dataflow.projects.locations.jobs.list
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.create
Create
API Only
GCP Dataflow
dataflow.projects.locations.jobs.get
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.update
Edit
API Only
GCP Dataflow
dataflow.projects.locations.jobs.debug.getConfig
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.debug.sendCapture
Send
API Only
GCP Dataflow
dataflow.projects.locations.jobs.getExecutionDetails
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.messages.list
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.getMetrics
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.snapshots.list
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.stages.getExecutionDetails
View
API Only
GCP Dataflow
dataflow.projects.locations.jobs.workItems.lease
Create
API Only
GCP Dataflow
dataflow.projects.locations.jobs.workItems.reportStatus
Create
API Only
GCP Dataflow
dataflow.projects.locations.jobs.snapshot
Create
API Only
GCP Dataflow
dataflow.projects.locations.snapshots.list
View
API Only
GCP Dataflow
dataflow.projects.locations.snapshots.delete
Delete
API Only
GCP Dataflow
dataflow.projects.locations.snapshots.get
View
API Only
GCP Dataflow
dataflow.projects.locations.templates.create
Create
API Only
GCP Dataflow
dataflow.projects.locations.templates.get
View
API Only
GCP Dataflow
dataflow.projects.locations.templates.launch
Create
API Only
GCP Dataflow
dataflow.projects.deleteSnapshots
Delete
API Only
GCP Dataflow
dataflow.projects.snapshots.list
View
API Only
GCP Dataflow
dataflow.projects.snapshots.get
View
API Only
GCP Dataflow
dataflow.projects.templates.create
Create
API Only
GCP Dataflow
dataflow.projects.templates.get
View
API Only
GCP Dataflow
dataflow.projects.templates.launch
Create
API Only
GCP Testing
testing.applicationDetailService.getApkDetails
View
API Only
GCP Testing
testing.projects.testMatrices.create
Create
API Only
GCP Testing
testing.projects.testMatrices.get
View
API Only
GCP Testing
testing.projects.testMatrices.cancel
Delete
API Only
GCP Testing
testing.testEnvironmentCatalog.get
View
API Only
GCP Video Intelligence
videointelligence.operations.projects.locations.operations.delete
Delete
API Only
GCP Video Intelligence
videointelligence.operations.projects.locations.operations.get
View
API Only
GCP Video Intelligence
videointelligence.operations.projects.locations.operations.cancel
Delete
API Only
GCP Video Intelligence
videointelligence.videos.annotate
Create
API Only
GCP Video Intelligence
videointelligence.projects.locations.operations.delete
Delete
API Only
GCP Video Intelligence
videointelligence.projects.locations.operations.get
View
API Only
GCP Video Intelligence
videointelligence.projects.locations.operations.list
View
API Only
GCP Video Intelligence
videointelligence.projects.locations.operations.cancel
Delete
API Only
GCP Service Management
servicemanagement.operations.list
View
API Only
GCP Service Management
servicemanagement.services.list
View
API Only
GCP Service Management
servicemanagement.services.create
Create
API Only
GCP Service Management
servicemanagement.services.delete
Delete
API Only
GCP Service Management
servicemanagement.services.get
View
API Only
GCP Service Management
servicemanagement.services.getConfig
View
API Only
GCP Service Management
servicemanagement.services.configs.list
View
API Only
GCP Service Management
servicemanagement.services.configs.create
Create
API Only
GCP Service Management
servicemanagement.services.configs.get
View
API Only
GCP Service Management
servicemanagement.services.configs.submit
Create
API Only
GCP Service Management
servicemanagement.services.rollouts.list
View
API Only
GCP Service Management
servicemanagement.services.rollouts.create
Create
API Only
GCP Service Management
servicemanagement.services.rollouts.get
View
API Only
GCP Service Management
servicemanagement.services.undelete
Create
API Only
GCP Service Management
servicemanagement.services.generateConfigReport
Create
API Only
GCP Service Management
servicemanagement.operations.get
View
API Only
GCP Service Management
servicemanagement.services.consumers.getIamPolicy
View
API Only
GCP Service Management
servicemanagement.services.consumers.setIamPolicy
Create
API Only
GCP Service Management
servicemanagement.services.consumers.testIamPermissions
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.delete
Delete
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.get
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.patch
Edit
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.operations.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.operations.cancel
Delete
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.global.hubs.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.global.hubs.create
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.internalRanges.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.internalRanges.create
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceClasses.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceConnectionMaps.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceConnectionMaps.create
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceConnectionPolicies.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceConnectionPolicies.create
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceConnectionTokens.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.serviceConnectionTokens.create
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.list
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.create
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.getIamPolicy
View
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.setIamPolicy
Create
API Only
GCP Network Connectivity
networkconnectivity.projects.locations.spokes.testIamPermissions
Create
API Only
GCP Domains
domains.projects.locations.registrations.retrieveImportableDomains
View
API Only
GCP Domains
domains.projects.locations.registrations.retrieveRegisterParameters
View
API Only
GCP Domains
domains.projects.locations.registrations.retrieveTransferParameters
View
API Only
GCP Domains
domains.projects.locations.registrations.searchDomains
Search
API Only
GCP Domains
domains.projects.locations.registrations.delete
Delete
API Only
GCP Domains
domains.projects.locations.registrations.get
View
API Only
GCP Domains
domains.projects.locations.registrations.patch
Edit
API Only
GCP Domains
domains.projects.locations.list
View
API Only
GCP Domains
domains.projects.locations.operations.list
View
API Only
GCP Domains
domains.projects.locations.registrations.export
View
API Only
GCP Domains
domains.projects.locations.registrations.list
View
API Only
GCP Domains
domains.projects.locations.registrations.import
Create
API Only
GCP Domains
domains.projects.locations.registrations.register
Register
API Only
GCP Domains
domains.projects.locations.registrations.transfer
Create
API Only
GCP Domains
domains.projects.locations.registrations.configureContactSettings
Create
API Only
GCP Domains
domains.projects.locations.registrations.configureDnsSettings
Create
API Only
GCP Domains
domains.projects.locations.registrations.configureManagementSettings
Create
API Only
GCP Domains
domains.projects.locations.registrations.resetAuthorizationCode
Edit
API Only
GCP Domains
domains.projects.locations.registrations.retrieveAuthorizationCode
View
API Only
GCP Domains
domains.projects.locations.registrations.getIamPolicy
View
API Only
GCP Domains
domains.projects.locations.registrations.setIamPolicy
Create
API Only
GCP Domains
domains.projects.locations.registrations.testIamPermissions
Create
API Only
GCP Pub/Sub
pubsub.projects.schemas.delete
Delete
API Only
GCP Pub/Sub
pubsub.projects.schemas.get
View
API Only
GCP Pub/Sub
pubsub.projects.topics.patch
Edit
API Only
GCP Pub/Sub
pubsub.projects.topics.create
Create
API Only
GCP Pub/Sub
pubsub.projects.schemas.commit
Create
API Only
GCP Pub/Sub
pubsub.projects.schemas.deleteRevision
Delete
API Only
GCP Pub/Sub
pubsub.projects.schemas.listRevisions
View
API Only
GCP Pub/Sub
pubsub.projects.schemas.rollback
Create
API Only
GCP Pub/Sub
pubsub.projects.schemas.list
View
API Only
GCP Pub/Sub
pubsub.projects.schemas.create
Create
API Only
GCP Pub/Sub
pubsub.projects.schemas.validate
Create
API Only
GCP Pub/Sub
pubsub.projects.schemas.validateMessage
Create
API Only
GCP Pub/Sub
pubsub.projects.snapshots.list
View
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.list
View
API Only
GCP Pub/Sub
pubsub.projects.topics.list
View
API Only
GCP Pub/Sub
pubsub.projects.topics.getIamPolicy
View
API Only
GCP Pub/Sub
pubsub.projects.topics.setIamPolicy
Create
API Only
GCP Pub/Sub
pubsub.projects.topics.testIamPermissions
Create
API Only
GCP Pub/Sub
pubsub.projects.snapshots.delete
Delete
API Only
GCP Pub/Sub
pubsub.projects.snapshots.get
View
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.delete
Delete
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.get
View
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.acknowledge
Create
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.detach
Delete
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.modifyAckDeadline
Edit
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.modifyPushConfig
Edit
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.pull
Create
API Only
GCP Pub/Sub
pubsub.projects.subscriptions.seek
Create
API Only
GCP Pub/Sub
pubsub.projects.topics.delete
Delete
API Only
GCP Pub/Sub
pubsub.projects.topics.get
View
API Only
GCP Pub/Sub
pubsub.projects.topics.snapshots.list
View
API Only
GCP Pub/Sub
pubsub.projects.topics.subscriptions.list
View
API Only
GCP Pub/Sub
pubsub.projects.topics.publish
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.generateRandomBytes
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.importJobs.get
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.patch
Edit
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.list
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.getPublicKey
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.asymmetricDecrypt
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.asymmetricSign
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.decrypt
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.destroy
Delete
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.encrypt
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.macSign
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.macVerify
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.restore
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.updatePrimaryVersion
Edit
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.ekmConnections.verifyConnectivity
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.list
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.create
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.import
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.list
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.cryptoKeys.create
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.ekmConnections.list
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.ekmConnections.create
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.importJobs.list
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.importJobs.create
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.list
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.create
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.importJobs.getIamPolicy
View
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.importJobs.setIamPolicy
Create
API Only
GCP Key Management Service (KMS)
cloudkms.projects.locations.keyRings.importJobs.testIamPermissions
Create
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.endpoints.delete
Delete
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.endpoints.get
View
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.endpoints.patch
Edit
API Only
GCP Service Directory
servicedirectory.projects.locations.list
View
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.resolve
Create
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.endpoints.list
View
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.endpoints.create
Create
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.list
View
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.create
Create
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.list
View
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.create
Create
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.getIamPolicy
View
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.setIamPolicy
Create
API Only
GCP Service Directory
servicedirectory.projects.locations.namespaces.services.testIamPermissions
Create
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.delete
Delete
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.volumeRestores.get
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.patch
Edit
API Only
GCP Backup for GKE
gkebackup.projects.locations.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.deleteOperations
Delete
API Only
GCP Backup for GKE
gkebackup.projects.locations.operations.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.operations.cancel
Delete
API Only
GCP Backup for GKE
gkebackup.projects.locations.backupPlans.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.backupPlans.create
Create
API Only
GCP Backup for GKE
gkebackup.projects.locations.backupPlans.backups.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.backupPlans.backups.create
Create
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.create
Create
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.create
Create
API Only
GCP Backup for GKE
gkebackup.projects.locations.backupPlans.backups.volumeBackups.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.volumeRestores.list
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.volumeRestores.getIamPolicy
View
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.volumeRestores.setIamPolicy
Create
API Only
GCP Backup for GKE
gkebackup.projects.locations.restorePlans.restores.volumeRestores.testIamPermissions
Create
API Only
GCP Text-to-Speech
texttospeech.text.synthesize
Create
API Only
GCP Text-to-Speech
texttospeech.voices.list
View
API Only
GCP Text-to-Speech
texttospeech.operations.delete
Delete
API Only
GCP Text-to-Speech
texttospeech.projects.locations.operations.get
View
API Only
GCP Text-to-Speech
texttospeech.projects.locations.operations.list
View
API Only
GCP Text-to-Speech
texttospeech.operations.cancel
Delete
API Only
GCP Text-to-Speech
texttospeech.projects.locations.synthesizeLongAudio
Create
API Only
GCP Shell
cloudshell.users.environments.addPublicKey
Create
API Only
GCP Shell
cloudshell.users.environments.removePublicKey
Delete
API Only
GCP Shell
cloudshell.operations.delete
Delete
API Only
GCP Shell
cloudshell.users.environments.get
View
API Only
GCP Shell
cloudshell.users.environments.authorize
Create
API Only
GCP Shell
cloudshell.operations.cancel
Delete
API Only
GCP Shell
cloudshell.users.environments.start
Start
API Only
GCP Apigee
apigee.organizations.create
Create
API Only
GCP Apigee
apigee.organizations.instances.reportStatus
Create
API Only
GCP Apigee
apigee.organizations.sites.apicategories.delete
Delete
API Only
GCP Apigee
apigee.organizations.sites.apicategories.get
View
API Only
GCP Apigee
apigee.organizations.sites.apicategories.patch
Edit
API Only
GCP Apigee
apigee.organizations.sharedflows.revisions.updateSharedFlowRevision
Edit
API Only
GCP Apigee
apigee.organizations.reports.update
Edit
API Only
GCP Apigee
apigee.organizations.developers.apps.attributes
Create
API Only
GCP Apigee
apigee.organizations.environments.keystores.aliases.getCertificate
View
API Only
GCP Apigee
apigee.organizations.environments.keystores.aliases.csr
View
API Only
GCP Apigee
apigee.organizations.environments.apis.revisions.debugsessions.deleteData
Delete
API Only
GCP Apigee
apigee.organizations.environments.sharedflows.revisions.undeploy
Delete
API Only
GCP Apigee
apigee.organizations.environments.sharedflows.revisions.getDeployments
View
API Only
GCP Apigee
apigee.organizations.environments.sharedflows.revisions.deploy
Create
API Only
GCP Apigee
apigee.organizations.environments.apis.revisions.deployments.generateDeployChangeReport
Create
API Only
GCP Apigee
apigee.organizations.environments.apis.revisions.deployments.generateUndeployChangeReport
Create
API Only
GCP Apigee
apigee.organizations.operations.list
View
API Only
GCP Apigee
apigee.organizations.instances.natAddresses.activate
Activate
API Only
GCP Apigee
apigee.organizations.developers.balance.adjust
Create
API Only
GCP Apigee
apigee.organizations.developers.balance.credit
Create
API Only
GCP Apigee
apigee.organizations.developers.subscriptions.expire
Create
API Only
GCP Apigee
apigee.organizations.environments.archiveDeployments.generateDownloadUrl
Create
API Only
GCP Apigee
apigee.organizations.getProjectMapping
View
API Only
GCP Apigee
apigee.organizations.getSyncAuthorization
View
API Only
GCP Apigee
apigee.organizations.securityProfiles.listRevisions
View
API Only
GCP Apigee
apigee.organizations.setSyncAuthorization
Create
API Only
GCP Apigee
apigee.organizations.environments.securityStats.queryTabularStats
Create
API Only
GCP Apigee
apigee.organizations.environments.securityStats.queryTimeSeriesStats
Create
API Only
GCP Apigee
apigee.organizations.setAddons
Create
API Only
GCP Apigee
apigee.organizations.list
View
API Only
GCP Apigee
apigee.organizations.environments.keystores.aliases.create
Create
API Only
GCP Apigee
apigee.organizations.analytics.datastores.list
View
API Only
GCP Apigee
apigee.organizations.analytics.datastores.create
Create
API Only
GCP Apigee
apigee.organizations.analytics.datastores.test
Create
API Only
GCP Apigee
apigee.organizations.environments.analytics.exports.list
View
API Only
GCP Apigee
apigee.organizations.environments.analytics.exports.create
Create
API Only
GCP Apigee
apigee.organizations.sites.apicategories.list
View
API Only
GCP Apigee
apigee.organizations.sites.apicategories.create
Create
API Only
GCP Apigee
apigee.organizations.apiproducts.list
View
API Only
GCP Apigee
apigee.organizations.apiproducts.create
Create
API Only
GCP Apigee
apigee.organizations.apis.list
View
API Only
GCP Apigee
apigee.organizations.apis.create
Create
API Only
GCP Apigee
apigee.organizations.developers.apps.list
View
API Only
GCP Apigee
apigee.organizations.developers.apps.create
Create
API Only
GCP Apigee
apigee.organizations.environments.archiveDeployments.list
View
API Only
GCP Apigee
apigee.organizations.environments.archiveDeployments.create
Create
API Only
GCP Apigee
apigee.organizations.environments.archiveDeployments.generateUploadUrl
Create
API Only
GCP Apigee
apigee.organizations.instances.attachments.list
View
API Only
GCP Apigee
apigee.organizations.instances.attachments.create
Create
API Only
GCP Apigee
apigee.organizations.developers.attributes.list
View
API Only
GCP Apigee
apigee.organizations.developers.attributes
Create
API Only
GCP Apigee
apigee.organizations.instances.canaryevaluations.create
Create
API Only
GCP Apigee
apigee.organizations.datacollectors.list
View
API Only
GCP Apigee
apigee.organizations.datacollectors.create
Create
API Only
GCP Apigee
apigee.organizations.environments.apis.revisions.debugsessions.list
View
API Only
GCP Apigee
apigee.organizations.environments.apis.revisions.debugsessions.create
Create
API Only
GCP Apigee
apigee.organizations.sharedflows.revisions.deployments.list
View
API Only
GCP Apigee
apigee.organizations.developers.list
View
API Only
GCP Apigee
apigee.organizations.developers.create
Create
API Only
GCP Apigee
apigee.organizations.endpointAttachments.list
View
API Only
GCP Apigee
apigee.organizations.endpointAttachments.create
Create
API Only
GCP Apigee
apigee.organizations.keyvaluemaps.entries.list
View
API Only
GCP Apigee
apigee.organizations.keyvaluemaps.entries.create
Create
API Only
GCP Apigee
apigee.organizations.envgroups.list
View
API Only
GCP Apigee
apigee.organizations.envgroups.create
Create
API Only
GCP Apigee
apigee.organizations.securityProfiles.environments.create
Create
API Only
GCP Apigee
apigee.organizations.hostQueries.list
View
API Only
GCP Apigee
apigee.organizations.hostQueries.create
Create
API Only
GCP Apigee
apigee.organizations.hostSecurityReports.list
View
API Only
GCP Apigee
apigee.organizations.hostSecurityReports.create
Create
API Only
GCP Apigee
apigee.organizations.instances.list
View
API Only
GCP Apigee
apigee.organizations.instances.create
Create
API Only
GCP Apigee
apigee.organizations.developers.apps.keys.create
Create
API Only
GCP Apigee
apigee.organizations.developers.apps.keys.create.create
Create
API Only
GCP Apigee
apigee.organizations.environments.keystores.create
Create
API Only
GCP Apigee
apigee.organizations.keyvaluemaps.create
Create
API Only
GCP Apigee
apigee.organizations.instances.natAddresses.list
View
API Only
GCP Apigee
apigee.organizations.instances.natAddresses.create
Create
API Only
GCP Apigee
apigee.organizations.environments.traceConfig.overrides.list
View
API Only
GCP Apigee
apigee.organizations.environments.traceConfig.overrides.create
Create
API Only
GCP Apigee
apigee.organizations.environments.queries.list
View
API Only
GCP Apigee
apigee.organizations.environments.queries.create
Create
API Only
GCP Apigee
apigee.organizations.apiproducts.rateplans.list
View
API Only
GCP Apigee
apigee.organizations.apiproducts.rateplans.create
Create
API Only
GCP Apigee
apigee.organizations.environments.references.create
Create
API Only
GCP Apigee
apigee.organizations.reports.list
View
API Only
GCP Apigee
apigee.organizations.reports.create
Create
API Only
GCP Apigee
apigee.organizations.environments.resourcefiles.list
View
API Only
GCP Apigee
apigee.organizations.environments.resourcefiles.create
Create
API Only
GCP Apigee
apigee.organizations.environments.resourcefiles.listEnvironmentResources
View
API Only
GCP Apigee
apigee.organizations.environments.resourcefiles.delete
Delete
API Only
GCP Apigee
apigee.organizations.environments.resourcefiles.get
View
API Only
GCP Apigee
apigee.organizations.environments.resourcefiles.update
Edit
API Only
GCP Apigee
apigee.organizations.environments.securityIncidents.list
View
API Only
GCP Apigee
apigee.organizations.securityProfiles.list
View
API Only
GCP Apigee
apigee.organizations.environments.securityReports.list
View
API Only
GCP Apigee
apigee.organizations.environments.securityReports.create
Create
API Only
GCP Apigee
apigee.organizations.sharedflows.list
View
API Only
GCP Apigee
apigee.organizations.sharedflows.create
Create
API Only
GCP Apigee
apigee.organizations.developers.subscriptions.list
View
API Only
GCP Apigee
apigee.organizations.developers.subscriptions.create
Create
API Only
GCP Apigee
apigee.organizations.environments.targetservers.create
Create
API Only
GCP Apigee
apigee.organizations.environments.subscribe
Create
API Only
GCP Apigee
apigee.organizations.environments.unsubscribe
Create
API Only
GCP Apigee
apigee.organizations.securityProfiles.environments.computeEnvironmentScores
Create
API Only
GCP Apigee
apigee.projects.provisionOrganization
Create
API Only
GCP Apigee
apigee.organizations.environments.getIamPolicy
View
API Only
GCP Apigee
apigee.organizations.environments.setIamPolicy
Create
API Only
GCP Apigee
apigee.organizations.environments.testIamPermissions
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeAppAttestAssertion
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeAppAttestAttestation
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeCustomToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeDebugToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeDeviceCheckToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangePlayIntegrityToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeRecaptchaEnterpriseToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeRecaptchaVToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.exchangeSafetyNetToken
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.generateAppAttestChallenge
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.generatePlayIntegrityChallenge
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.debugTokens.delete
Delete
API Only
GCP Firebase App Check
firebaseappcheck.projects.services.get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.services.patch
Edit
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.appAttestConfig.Get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.deviceCheckConfig.Get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.playIntegrityConfig.Get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.recaptchaEnterpriseConfig.Get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.recaptchaVConfig.Get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.safetyNetConfig.Get
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.debugTokens.list
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.apps.debugTokens.create
Create
API Only
GCP Firebase App Check
firebaseappcheck.projects.services.list
View
API Only
GCP Firebase App Check
firebaseappcheck.projects.services.Update
Edit
API Only
GCP Firebase Management
firebase.availableProjects.list
View
API Only
GCP Firebase Management
firebase.projects.list
View
API Only
GCP Firebase Management
firebase.projects.androidApps.sha.delete
Delete
API Only
GCP Firebase Management
firebase.projects.webApps.getConfig
View
API Only
GCP Firebase Management
firebase.projects.webApps.patch
Edit
API Only
GCP Firebase Management
firebase.projects.webApps.remove
Delete
API Only
GCP Firebase Management
firebase.projects.webApps.undelete
Create
API Only
GCP Firebase Management
firebase.projects.androidApps.list
View
API Only
GCP Firebase Management
firebase.projects.androidApps.create
Create
API Only
GCP Firebase Management
firebase.projects.availableLocations.list
View
API Only
GCP Firebase Management
firebase.projects.defaultLocation.finalize
Create
API Only
GCP Firebase Management
firebase.projects.iosApps.list
View
API Only
GCP Firebase Management
firebase.projects.iosApps.create
Create
API Only
GCP Firebase Management
firebase.projects.androidApps.sha.list
View
API Only
GCP Firebase Management
firebase.projects.androidApps.sha.create
Create
API Only
GCP Firebase Management
firebase.projects.webApps.list
View
API Only
GCP Firebase Management
firebase.projects.webApps.create
Create
API Only
GCP Firebase Management
firebase.projects.addGoogleAnalytics
Create
API Only
GCP Firebase Management
firebase.projects.removeAnalytics
Delete
API Only
GCP Firebase Management
firebase.projects.searchApps
Search
API Only
GCP Firebase Management
firebase.projects.addFirebase
Create
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.runs.delete
Delete
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.runs.get
View
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.patch
Edit
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.locations.list
View
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.locations.dataSources.checkValidCreds
Create
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.locations.enrollDataSources
Create
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.locations.dataSources.list
View
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.runs.list
View
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.list
View
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.create
Create
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.runs.transferLogs.list
View
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.scheduleRuns
Create
API Only
GCP BigQuery Data Transfer
bigquerydatatransfer.projects.transferConfigs.startManualRuns
Start
API Only
GCP Logging
logging.entries.copy
Copy
API Only
GCP Logging
logging.entries.list
View
API Only
GCP Logging
logging.entries.tail
Create
API Only
GCP Logging
logging.entries.write
Create
API Only
GCP Logging
logging.monitoredResourceDescriptors.list
View
API Only
GCP Logging
logging.projects.logs.delete
Delete
API Only
GCP Logging
logging.projects.metrics.delete
Delete
API Only
GCP Logging
logging.projects.metrics.get
View
API Only
GCP Logging
logging.projects.metrics.update
Edit
API Only
GCP Logging
logging.projects.locations.buckets.views.delete
Delete
API Only
GCP Logging
logging.projects.locations.operations.get
View
API Only
GCP Logging
logging.projects.locations.buckets.views.patch
Edit
API Only
GCP Logging
logging.getCmekSettings
View
API Only
GCP Logging
logging.updateCmekSettings
Edit
API Only
GCP Logging
logging.projects.locations.list
View
API Only
GCP Logging
logging.projects.locations.operations.list
View
API Only
GCP Logging
logging.getSettings
View
API Only
GCP Logging
logging.updateSettings
Edit
API Only
GCP Logging
logging.projects.locations.operations.cancel
Delete
API Only
GCP Logging
logging.projects.locations.buckets.undelete
Create
API Only
GCP Logging
logging.projects.locations.buckets.updateAsync
Edit
API Only
GCP Logging
logging.projects.locations.buckets.list
View
API Only
GCP Logging
logging.projects.locations.buckets.create
Create
API Only
GCP Logging
logging.projects.locations.buckets.createAsync
Create
API Only
GCP Logging
logging.projects.exclusions.list
View
API Only
GCP Logging
logging.projects.exclusions.create
Create
API Only
GCP Logging
logging.projects.locations.buckets.links.list
View
API Only
GCP Logging
logging.projects.locations.buckets.links.create
Create
API Only
GCP Logging
logging.projects.logs.list
View
API Only
GCP Logging
logging.projects.metrics.list
View
API Only
GCP Logging
logging.projects.metrics.create
Create
API Only
GCP Logging
logging.sinks.list
View
API Only
GCP Logging
logging.sinks.create
Create
API Only
GCP Logging
logging.projects.locations.buckets.views.list
View
API Only
GCP Logging
logging.projects.locations.buckets.views.create
Create
API Only
GCP Logging
logging.sinks.delete
Delete
API Only
GCP Logging
logging.sinks.get
View
API Only
GCP Logging
logging.projects.sinks.patch
Edit
API Only
GCP Logging
logging.sinks.update
Edit
API Only
GCP Debugger
clouddebugger.controller.debuggees.register
Register
API Only
GCP Debugger
clouddebugger.controller.debuggees.breakpoints.list
View
API Only
GCP Debugger
clouddebugger.controller.debuggees.breakpoints.update
Edit
API Only
GCP Debugger
clouddebugger.debugger.debuggees.list
View
API Only
GCP Debugger
clouddebugger.debugger.debuggees.breakpoints.list
View
API Only
GCP Debugger
clouddebugger.debugger.debuggees.breakpoints.set
Create
API Only
GCP Debugger
clouddebugger.debugger.debuggees.breakpoints.delete
Delete
API Only
GCP Debugger
clouddebugger.debugger.debuggees.breakpoints.get
View
API Only
GCP Batch API
batch.projects.locations.operations.delete
Delete
API Only
GCP Batch API
batch.projects.locations.operations.get
View
API Only
GCP Batch API
batch.projects.locations.list
View
API Only
GCP Batch API
batch.projects.locations.operations.list
View
API Only
GCP Batch API
batch.projects.locations.operations.cancel
Delete
API Only
GCP Batch API
batch.projects.locations.jobs.list
View
API Only
GCP Batch API
batch.projects.locations.jobs.create
Create
API Only
GCP Batch API
batch.projects.locations.state.report
Create
API Only
GCP Batch API
batch.projects.locations.jobs.taskGroups.tasks.list
View
API Only
GCP Data Labelling
datalabeling.projects.operations.delete
Delete
API Only
GCP Data Labelling
datalabeling.projects.operations.get
View
API Only
GCP Data Labelling
datalabeling.projects.evaluationJobs.patch
Edit
API Only
GCP Data Labelling
datalabeling.projects.operations.list
View
API Only
GCP Data Labelling
datalabeling.projects.operations.cancel
Delete
API Only
GCP Data Labelling
datalabeling.projects.datasets.exportData
View
API Only
GCP Data Labelling
datalabeling.projects.datasets.importData
Create
API Only
GCP Data Labelling
datalabeling.projects.evaluationJobs.pause
Create
API Only
GCP Data Labelling
datalabeling.projects.evaluationJobs.resume
Start
API Only
GCP Data Labelling
datalabeling.projects.datasets.annotatedDatasets.list
View
API Only
GCP Data Labelling
datalabeling.projects.annotationSpecSets.list
View
API Only
GCP Data Labelling
datalabeling.projects.annotationSpecSets.create
Create
API Only
GCP Data Labelling
datalabeling.projects.datasets.dataItems.list
View
API Only
GCP Data Labelling
datalabeling.projects.datasets.list
View
API Only
GCP Data Labelling
datalabeling.projects.datasets.create
Create
API Only
GCP Data Labelling
datalabeling.projects.evaluationJobs.list
View
API Only
GCP Data Labelling
datalabeling.projects.evaluationJobs.create
Create
API Only
GCP Data Labelling
datalabeling.projects.evaluations.search
Search
API Only
GCP Data Labelling
datalabeling.projects.datasets.evaluations.exampleComparisons.search
Search
API Only
GCP Data Labelling
datalabeling.projects.datasets.annotatedDatasets.examples.list
View
API Only
GCP Data Labelling
datalabeling.projects.datasets.annotatedDatasets.feedbackThreads.feedbackMessages.list
View
API Only
GCP Data Labelling
datalabeling.projects.datasets.annotatedDatasets.feedbackThreads.feedbackMessages.create
Create
API Only
GCP Data Labelling
datalabeling.projects.datasets.annotatedDatasets.feedbackThreads.list
View
API Only
GCP Data Labelling
datalabeling.projects.datasets.image.label
Create
API Only
GCP Data Labelling
datalabeling.projects.instructions.list
View
API Only
GCP Data Labelling
datalabeling.projects.instructions.create
Create
API Only
GCP Data Labelling
datalabeling.projects.datasets.text.label
Create
API Only
GCP Data Labelling
datalabeling.projects.datasets.video.label
Create
API Only
GCP Organization Policy
orgpolicy.projects.policies.delete
Delete
API Only
GCP Organization Policy
orgpolicy.projects.policies.get
View
API Only
GCP Organization Policy
orgpolicy.projects.policies.patch
Edit
API Only
GCP Organization Policy
orgpolicy.projects.policies.getEffectivePolicy
View
API Only
GCP Organization Policy
orgpolicy.projects.constraints.list
View
API Only
GCP Organization Policy
orgpolicy.organizations.customConstraints.list
View
API Only
GCP Organization Policy
orgpolicy.organizations.customConstraints.create
Create
API Only
GCP Organization Policy
orgpolicy.projects.policies.list
View
API Only
GCP Organization Policy
orgpolicy.projects.policies.create
Create
API Only
GCP Notebooks
notebooks.projects.locations.operations.delete
Delete
API Only
GCP Notebooks
notebooks.projects.locations.operations.get
View
API Only
GCP Notebooks
notebooks.projects.locations.list
View
API Only
GCP Notebooks
notebooks.projects.locations.operations.list
View
API Only
GCP Notebooks
notebooks.projects.locations.operations.cancel
Delete
API Only
GCP Notebooks
notebooks.projects.locations.instances.getIamPolicy
View
API Only
GCP Notebooks
notebooks.projects.locations.instances.setIamPolicy
Create
API Only
GCP Notebooks
notebooks.projects.locations.instances.testIamPermissions
Create
API Only
GCP Firebase Cloud Messaging
fcm.projects.messages.send
Send
API Only
GCP Service Networking
servicenetworking.services.projects.global.networks.peeredDnsDomains.delete
Delete
API Only
GCP Service Networking
servicenetworking.services.projects.global.networks.get
View
API Only
GCP Service Networking
servicenetworking.services.connections.patch
Edit
API Only
GCP Service Networking
servicenetworking.services.connections.deleteConnection
Delete
API Only
GCP Service Networking
servicenetworking.operations.cancel
Delete
API Only
GCP Service Networking
servicenetworking.services.connections.list
View
API Only
GCP Service Networking
servicenetworking.services.connections.create
Create
API Only
GCP Service Networking
servicenetworking.services.dnsRecordSets.add
Create
API Only
GCP Service Networking
servicenetworking.services.dnsRecordSets.remove
Delete
API Only
GCP Service Networking
servicenetworking.services.dnsRecordSets.update
Edit
API Only
GCP Service Networking
servicenetworking.services.dnsZones.add
Create
API Only
GCP Service Networking
servicenetworking.services.dnsZones.remove
Delete
API Only
GCP Service Networking
servicenetworking.services.projects.global.networks.peeredDnsDomains.list
View
API Only
GCP Service Networking
servicenetworking.services.projects.global.networks.peeredDnsDomains.create
Create
API Only
GCP Service Networking
servicenetworking.services.roles.add
Create
API Only
GCP Service Networking
servicenetworking.services.addSubnetwork
Create
API Only
GCP Service Networking
servicenetworking.services.disableVpcServiceControls
Edit
API Only
GCP Service Networking
servicenetworking.services.enableVpcServiceControls
Enable
API Only
GCP Service Networking
servicenetworking.services.searchRange
Search
API Only
GCP Service Networking
servicenetworking.services.projects.global.networks.updateConsumerConfig
Edit
API Only
GCP Service Networking
servicenetworking.services.validate
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.datacenterConnectors.upgradeAppliance
Create
API Only
GCP VM Migration
vmmigration.projects.locations.groups.addGroupMigration
Create
API Only
GCP VM Migration
vmmigration.projects.locations.groups.removeGroupMigration
Delete
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.finalizeMigration
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.pauseMigration
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.resumeMigration
Start
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.startMigration
Start
API Only
GCP VM Migration
vmmigration.projects.locations.targetProjects.delete
Delete
API Only
GCP VM Migration
vmmigration.projects.locations.targetProjects.get
View
API Only
GCP VM Migration
vmmigration.projects.locations.targetProjects.patch
Edit
API Only
GCP VM Migration
vmmigration.projects.locations.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.operations.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.cutoverJobs.cancel
Delete
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.cloneJobs.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.cloneJobs.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.cutoverJobs.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.cutoverJobs.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.datacenterConnectors.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.datacenterConnectors.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.groups.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.groups.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.migratingVms.replicationCycles.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.targetProjects.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.targetProjects.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.utilizationReports.list
View
API Only
GCP VM Migration
vmmigration.projects.locations.sources.utilizationReports.create
Create
API Only
GCP VM Migration
vmmigration.projects.locations.sources.fetchInventory
View
API Only
GCP Monitoring
monitoring.uptimeCheckIps.list
View
API Only
GCP Monitoring
monitoring.services.serviceLevelObjectives.delete
Delete
API Only
GCP Monitoring
monitoring.services.serviceLevelObjectives.get
View
API Only
GCP Monitoring
monitoring.services.serviceLevelObjectives.patch
Edit
API Only
GCP Monitoring
monitoring.projects.groups.update
Edit
API Only
GCP Monitoring
monitoring.projects.alertPolicies.list
View
API Only
GCP Monitoring
monitoring.projects.alertPolicies.create
Create
API Only
GCP Monitoring
monitoring.projects.collectdTimeSeries.create
Create
API Only
GCP Monitoring
monitoring.projects.groups.list
View
API Only
GCP Monitoring
monitoring.projects.groups.create
Create
API Only
GCP Monitoring
monitoring.projects.groups.members.list
View
API Only
GCP Monitoring
monitoring.projects.metricDescriptors.list
View
API Only
GCP Monitoring
monitoring.projects.metricDescriptors.create
Create
API Only
GCP Monitoring
monitoring.projects.monitoredResourceDescriptors.list
View
API Only
GCP Monitoring
monitoring.projects.notificationChannelDescriptors.list
View
API Only
GCP Monitoring
monitoring.projects.notificationChannels.list
View
API Only
GCP Monitoring
monitoring.projects.notificationChannels.create
Create
API Only
GCP Monitoring
monitoring.projects.timeSeries.list
View
API Only
GCP Monitoring
monitoring.projects.timeSeries.create
Create
API Only
GCP Monitoring
monitoring.projects.timeSeries.createService
Create
API Only
GCP Monitoring
monitoring.projects.timeSeries.query
Create
API Only
GCP Monitoring
monitoring.projects.notificationChannels.getVerificationCode
View
API Only
GCP Monitoring
monitoring.projects.notificationChannels.sendVerificationCode
Send
API Only
GCP Monitoring
monitoring.projects.notificationChannels.verify
Create
API Only
GCP Monitoring
monitoring.services.serviceLevelObjectives.list
View
API Only
GCP Monitoring
monitoring.services.serviceLevelObjectives.create
Create
API Only
GCP Monitoring
monitoring.services.list
View
API Only
GCP Monitoring
monitoring.services.create
Create
API Only
GCP Monitoring
monitoring.projects.snoozes.list
View
API Only
GCP Monitoring
monitoring.projects.snoozes.create
Create
API Only
GCP Monitoring
monitoring.projects.uptimeCheckConfigs.list
View
API Only
GCP Monitoring
monitoring.projects.uptimeCheckConfigs.create
Create
API Only
GCP AutoML
automl.projects.locations.operations.delete
Delete
API Only
GCP AutoML
automl.projects.locations.operations.get
View
API Only
GCP AutoML
automl.projects.locations.datasets.tableSpecs.columnSpecs.patch
Edit
API Only
GCP AutoML
automl.projects.locations.list
View
API Only
GCP AutoML
automl.projects.locations.operations.list
View
API Only
GCP AutoML
automl.projects.locations.models.Predict
Create
API Only
GCP AutoML
automl.projects.locations.operations.cancel
Delete
API Only
GCP AutoML
automl.projects.locations.models.deploy
Create
API Only
GCP AutoML
automl.projects.locations.models.export
View
API Only
GCP AutoML
automl.projects.locations.datasets.exportData
View
API Only
GCP AutoML
automl.projects.locations.models.exportEvaluatedExamples
View
API Only
GCP AutoML
automl.projects.locations.datasets.importData
Create
API Only
GCP AutoML
automl.projects.locations.models.predict
Create
API Only
GCP AutoML
automl.projects.locations.models.undeploy
Create
API Only
GCP AutoML
automl.projects.locations.operations.wait
Create
API Only
GCP AutoML
automl.projects.locations.datasets.tableSpecs.columnSpecs.list
View
API Only
GCP AutoML
automl.projects.locations.datasets.list
View
API Only
GCP AutoML
automl.projects.locations.datasets.create
Create
API Only
GCP AutoML
automl.projects.locations.models.modelEvaluations.list
View
API Only
GCP AutoML
automl.projects.locations.models.list
View
API Only
GCP AutoML
automl.projects.locations.models.create
Create
API Only
GCP AutoML
automl.projects.locations.datasets.tableSpecs.list
View
API Only
GCP AutoML
automl.projects.locations.models.getIamPolicy
View
API Only
GCP AutoML
automl.projects.locations.models.setIamPolicy
Create
API Only
GCP AutoML
automl.projects.locations.testIamPermissions
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.operations.delete
Delete
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.operations.get
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.patch
Edit
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.artifacts.replaceArtifact
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.operations.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.operations.cancel
Delete
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.deleteRevision
Delete
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.artifacts.getContents
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.listRevisions
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.rollback
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.tagRevision
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.create
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.artifacts.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.artifacts.create
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.deployments.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.deployments.create
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.instances.create
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.specs.create
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.list
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.apis.versions.create
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.runtime.getIamPolicy
View
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.runtime.setIamPolicy
Create
API Only
GCP Apigee Registry
apigeeregistry.projects.locations.runtime.testIamPermissions
Create
API Only
GCP Network Management
networkmanagement.projects.locations.global.operations.delete
Delete
API Only
GCP Network Management
networkmanagement.projects.locations.global.operations.get
View
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.patch
Edit
API Only
GCP Network Management
networkmanagement.projects.locations.list
View
API Only
GCP Network Management
networkmanagement.projects.locations.global.operations.list
View
API Only
GCP Network Management
networkmanagement.projects.locations.global.operations.cancel
Delete
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.rerun
Create
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.list
View
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.create
Create
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.getIamPolicy
View
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.setIamPolicy
Create
API Only
GCP Network Management
networkmanagement.projects.locations.global.connectivityTests.testIamPermissions
Create
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.delete
Delete
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.get
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.patch
Edit
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.operations.list
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.getPartitions
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.subscriptions.list
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.reservations.topics.list
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.operations.cancel
Delete
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.subscriptions.seek
Create
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.reservations.list
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.reservations.create
Create
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.subscriptions.list
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.subscriptions.create
Create
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.list
View
API Only
GCP Pub/Sub Lite
pubsublite.admin.projects.locations.topics.create
Create
API Only
GCP Pub/Sub Lite
pubsublite.cursor.projects.locations.subscriptions.cursors.list
View
API Only
GCP Pub/Sub Lite
pubsublite.cursor.projects.locations.subscriptions.commitCursor
Create
API Only
GCP Pub/Sub Lite
pubsublite.topicStats.projects.locations.topics.computeHeadCursor
Create
API Only
GCP Pub/Sub Lite
pubsublite.topicStats.projects.locations.topics.computeMessageStats
Create
API Only
GCP Pub/Sub Lite
pubsublite.topicStats.projects.locations.topics.computeTimeCursor
Create
API Only
GCP Channel
cloudchannel.products.list
View
API Only
GCP Channel
cloudchannel.accounts.listSubscribers
View
API Only
GCP Channel
cloudchannel.accounts.register
Register
API Only
GCP Channel
cloudchannel.accounts.unregister
Delete
API Only
GCP Channel
cloudchannel.accounts.customers.listPurchasableOffers
View
API Only
GCP Channel
cloudchannel.accounts.customers.listPurchasableSkus
View
API Only
GCP Channel
cloudchannel.accounts.customers.provisionCloudIdentity
Create
API Only
GCP Channel
cloudchannel.accounts.customers.queryEligibleBillingAccounts
View
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.lookupOffer
View
API Only
GCP Channel
cloudchannel.operations.delete
Delete
API Only
GCP Channel
cloudchannel.operations.list
View
API Only
GCP Channel
cloudchannel.accounts.customers.customerRepricingConfigs.patch
Edit
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.activate
Activate
API Only
GCP Channel
cloudchannel.operations.cancel
Delete
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.changeOffer
Create
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.changeParameters
Create
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.changeRenewalSettings
Create
API Only
GCP Channel
cloudchannel.accounts.reports.run
Create
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.startPaidService
Start
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.suspend
Delete
API Only
GCP Channel
cloudchannel.accounts.skuGroups.billableSkus.list
View
API Only
GCP Channel
cloudchannel.accounts.channelPartnerLinks.list
View
API Only
GCP Channel
cloudchannel.accounts.channelPartnerLinks.create
Create
API Only
GCP Channel
cloudchannel.accounts.channelPartnerLinks.channelPartnerRepricingConfigs.list
View
API Only
GCP Channel
cloudchannel.accounts.channelPartnerLinks.channelPartnerRepricingConfigs.create
Create
API Only
GCP Channel
cloudchannel.accounts.customers.customerRepricingConfigs.list
View
API Only
GCP Channel
cloudchannel.accounts.customers.customerRepricingConfigs.create
Create
API Only
GCP Channel
cloudchannel.accounts.customers.list
View
API Only
GCP Channel
cloudchannel.accounts.customers.create
Create
API Only
GCP Channel
cloudchannel.accounts.customers.import
Create
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.list
View
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.create
Create
API Only
GCP Channel
cloudchannel.accounts.offers.list
View
API Only
GCP Channel
cloudchannel.accounts.reports.list
View
API Only
GCP Channel
cloudchannel.accounts.skuGroups.list
View
API Only
GCP Channel
cloudchannel.products.skus.list
View
API Only
GCP Channel
cloudchannel.accounts.checkCloudIdentityAccountsExist
Create
API Only
GCP Channel
cloudchannel.accounts.customers.entitlements.listEntitlementChanges
View
API Only
GCP Channel
cloudchannel.accounts.listTransferableOffers
View
API Only
GCP Channel
cloudchannel.accounts.listTransferableSkus
View
API Only
GCP Channel
cloudchannel.accounts.customers.transferEntitlements
Create
API Only
GCP Channel
cloudchannel.accounts.customers.transferEntitlementsToGoogle
Create
API Only
GCP Channel
cloudchannel.accounts.reportJobs.fetchReportResults
View
API Only
GCP Storage for Firebase
firebasestorage.projects.buckets.addFirebase
Create
API Only
GCP Storage for Firebase
firebasestorage.projects.buckets.removeFirebase
Delete
API Only
GCP Storage for Firebase
firebasestorage.projects.buckets.get
View
API Only
GCP Storage for Firebase
firebasestorage.projects.buckets.list
View
API Only
GCP Functions
cloudfunctions.projects.locations.functions.delete
Delete
API Only
GCP Functions
cloudfunctions.projects.locations.operations.get
View
API Only
GCP Functions
cloudfunctions.projects.locations.functions.patch
Edit
API Only
GCP Functions
cloudfunctions.projects.locations.list
View
API Only
GCP Functions
cloudfunctions.projects.locations.operations.list
View
API Only
GCP Functions
cloudfunctions.projects.locations.functions.generateDownloadUrl
Create
API Only
GCP Functions
cloudfunctions.projects.locations.functions.list
View
API Only
GCP Functions
cloudfunctions.projects.locations.functions.create
Create
API Only
GCP Functions
cloudfunctions.projects.locations.functions.generateUploadUrl
Create
API Only
GCP Functions
cloudfunctions.projects.locations.runtimes.list
View
API Only
GCP Functions
cloudfunctions.projects.locations.functions.getIamPolicy
View
API Only
GCP Functions
cloudfunctions.projects.locations.functions.setIamPolicy
Create
API Only
GCP Functions
cloudfunctions.projects.locations.functions.testIamPermissions
Create
API Only
GCP Tag Manager
tagmanager.accounts.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.lookup
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.built_in_variables.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.built_in_variables.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.clients.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.clients.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.destinations.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.destinations.link
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.environments.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.environments.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.folders.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.folders.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.gtag_config.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.gtag_config.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.tags.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.tags.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.templates.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.templates.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.transformations.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.transformations.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.triggers.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.triggers.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.user_permissions.list
View
API Only
GCP Tag Manager
tagmanager.accounts.user_permissions.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.variables.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.variables.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.version_headers.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.version_headers.latest
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.versions.live
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.zones.list
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.zones.create
Create
API Only
GCP Tag Manager
tagmanager.accounts.user_permissions.delete
Delete
API Only
GCP Tag Manager
tagmanager.accounts.user_permissions.get
View
API Only
GCP Tag Manager
tagmanager.accounts.user_permissions.update
Edit
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.built_in_variables.revert
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.getStatus
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.combine
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.create_version
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.folders.entities
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.folders.move_entities_to_folder
Move
API Only
GCP Tag Manager
tagmanager.accounts.containers.move_tag_id
Move
API Only
GCP Tag Manager
tagmanager.accounts.containers.versions.publish
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.quick_preview
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.environments.reauthorize
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.resolve_conflict
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.zones.revert
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.versions.set_latest
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.snippet
View
API Only
GCP Tag Manager
tagmanager.accounts.containers.workspaces.sync
Create
API Only
GCP Tag Manager
tagmanager.accounts.containers.versions.undelete
Create
API Only
GCP Source Repositories
sourcerepo.projects.repos.delete
Delete
API Only
GCP Source Repositories
sourcerepo.projects.repos.get
View
API Only
GCP Source Repositories
sourcerepo.projects.repos.patch
Edit
API Only
GCP Source Repositories
sourcerepo.projects.getConfig
View
API Only
GCP Source Repositories
sourcerepo.projects.updateConfig
Edit
API Only
GCP Source Repositories
sourcerepo.projects.repos.list
View
API Only
GCP Source Repositories
sourcerepo.projects.repos.sync
Create
API Only
GCP Source Repositories
sourcerepo.projects.repos.create
Create
API Only
GCP Source Repositories
sourcerepo.projects.repos.getIamPolicy
View
API Only
GCP Source Repositories
sourcerepo.projects.repos.setIamPolicy
Create
API Only
GCP Source Repositories
sourcerepo.projects.repos.testIamPermissions
Create
API Only
GCP Game
gameservices.projects.locations.operations.delete
Delete
API Only
GCP Game
gameservices.projects.locations.operations.get
View
API Only
GCP Game
gameservices.projects.locations.list
View
API Only
GCP Game
gameservices.projects.locations.operations.list
View
API Only
GCP Game
gameservices.projects.locations.operations.cancel
Delete
API Only
GCP Game
gameservices.projects.locations.gameServerDeployments.getIamPolicy
View
API Only
GCP Game
gameservices.projects.locations.gameServerDeployments.setIamPolicy
Create
API Only
GCP Game
gameservices.projects.locations.gameServerDeployments.testIamPermissions
Create
API Only
GCP Composer
composer.projects.locations.environments.databaseFailover
Create
API Only
GCP Composer
composer.projects.locations.environments.executeAirflowCommand
Create
API Only
GCP Composer
composer.projects.locations.environments.fetchDatabaseProperties
View
API Only
GCP Composer
composer.projects.locations.environments.loadSnapshot
Create
API Only
GCP Composer
composer.projects.locations.environments.pollAirflowCommand
Create
API Only
GCP Composer
composer.projects.locations.environments.saveSnapshot
Create
API Only
GCP Composer
composer.projects.locations.environments.stopAirflowCommand
Stop
API Only
GCP Composer
composer.projects.locations.operations.delete
Delete
API Only
GCP Composer
composer.projects.locations.operations.get
View
API Only
GCP Composer
composer.projects.locations.environments.patch
Edit
API Only
GCP Composer
composer.projects.locations.operations.list
View
API Only
GCP Composer
composer.projects.locations.environments.list
View
API Only
GCP Composer
composer.projects.locations.environments.create
Create
API Only
GCP Composer
composer.projects.locations.imageVersions.list
View
API Only
GCP Traffic Director
trafficdirector.discovery.client_status
Create
API Only
GCP OS Login
oslogin.users.sshPublicKeys.delete
Delete
API Only
GCP OS Login
oslogin.users.sshPublicKeys.get
View
API Only
GCP OS Login
oslogin.users.sshPublicKeys.patch
Edit
API Only
GCP OS Login
oslogin.users.getLoginProfile
View
API Only
GCP OS Login
oslogin.users.sshPublicKeys.create
Create
API Only
GCP OS Login
oslogin.users.importSshPublicKey
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.delete
Delete
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.get
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.patch
Edit
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.operations.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.abandon
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.advance
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.approve
Approve
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.operations.cancel
Delete
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.jobRuns.terminate
Terminate
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.create
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.jobRuns.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.create
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.create
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.list
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.create
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.getIamPolicy
View
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.setIamPolicy
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.targets.testIamPermissions
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.ignoreJob
Create
API Only
GCP Cloud Deploy
clouddeploy.projects.locations.deliveryPipelines.releases.rollouts.retryJob
Create
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.operations.delete
Delete
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.operations.get
View
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.contactCenters.patch
Edit
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.list
View
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.operations.list
View
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.operations.cancel
Delete
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.contactCenters.list
View
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.contactCenters.create
Create
API Only
GCP Contact Center AI Platform
contactcenteraiplatform.projects.locations.queryContactCenterQuota
View
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.delete
Delete
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.violations.get
View
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.patch
Edit
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.operations.list
View
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.violations.acknowledge
Create
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.mutatePartnerPermissions
Edit
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.restrictAllowedResources
Create
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.violations.list
View
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.list
View
API Only
GCP Assured Workloads
assuredworkloads.organizations.locations.workloads.create
Create
API Only
GCP Genomics
genomics.pipelines.run
Create
API Only
GCP Genomics
genomics.workers.checkIn
Create
API Only
GCP Genomics
genomics.projects.workers.checkIn
Create
API Only
GCP Genomics
genomics.projects.operations.list
View
API Only
GCP Genomics
genomics.projects.operations.cancel
Delete
API Only
GCP Trace
cloudtrace.projects.traces.spans.createSpan
Create
API Only
GCP Trace
cloudtrace.projects.traces.Write
Create
API Only
GCP Engine Admin
appengine.apps.create
Create
API Only
GCP Engine Admin
appengine.apps.get
View
API Only
GCP Engine Admin
appengine.apps.patch
Edit
API Only
GCP Engine Admin
appengine.apps.authorizedCertificates.list
View
API Only
GCP Engine Admin
appengine.apps.authorizedCertificates.create
Create
API Only
GCP Engine Admin
appengine.apps.authorizedCertificates.delete
Delete
API Only
GCP Engine Admin
appengine.apps.authorizedCertificates.get
View
API Only
GCP Engine Admin
appengine.apps.authorizedCertificates.patch
Edit
API Only
GCP Engine Admin
appengine.apps.authorizedDomains.list
View
API Only
GCP Engine Admin
appengine.apps.domainMappings.list
View
API Only
GCP Engine Admin
appengine.apps.domainMappings.create
Create
API Only
GCP Engine Admin
appengine.apps.domainMappings.delete
Delete
API Only
GCP Engine Admin
appengine.apps.domainMappings.get
View
API Only
GCP Engine Admin
appengine.apps.domainMappings.patch
Edit
API Only
GCP Engine Admin
appengine.apps.firewall.ingressRules.list
View
API Only
GCP Engine Admin
appengine.apps.firewall.ingressRules.create
Create
API Only
GCP Engine Admin
appengine.apps.firewall.ingressRules.delete
Delete
API Only
GCP Engine Admin
appengine.apps.firewall.ingressRules.get
View
API Only
GCP Engine Admin
appengine.apps.firewall.ingressRules.patch
Edit
API Only
GCP Engine Admin
appengine.apps.firewall.ingressRules.Update
Edit
API Only
GCP Engine Admin
appengine.apps.locations.list
View
API Only
GCP Engine Admin
appengine.apps.locations.get
View
API Only
GCP Engine Admin
appengine.apps.operations.list
View
API Only
GCP Engine Admin
appengine.apps.operations.get
View
API Only
GCP Engine Admin
appengine.apps.services.list
View
API Only
GCP Engine Admin
appengine.apps.services.delete
Delete
API Only
GCP Engine Admin
appengine.apps.services.get
View
API Only
GCP Engine Admin
appengine.apps.services.patch
Edit
API Only
GCP Engine Admin
appengine.apps.services.versions.list
View
API Only
GCP Engine Admin
appengine.apps.services.versions.create
Create
API Only
GCP Engine Admin
appengine.apps.services.versions.delete
Delete
API Only
GCP Engine Admin
appengine.apps.services.versions.get
View
API Only
GCP Engine Admin
appengine.apps.services.versions.patch
Edit
API Only
GCP Engine Admin
appengine.apps.services.versions.instances.list
View
API Only
GCP Engine Admin
appengine.apps.services.versions.instances.delete
Delete
API Only
GCP Engine Admin
appengine.apps.services.versions.instances.get
View
API Only
GCP Engine Admin
appengine.apps.services.versions.instances.debug
Create
API Only
GCP Engine Admin
appengine.apps.repair
Create
API Only
GCP Engine Admin
appengine.projects.locations.applications.create
Create
API Only
GCP Engine Admin
appengine.projects.locations.applications.get
View
API Only
GCP Engine Admin
appengine.projects.locations.applications.services.list
View
API Only
GCP Engine Admin
appengine.projects.locations.applications.services.get
View
API Only
GCP Engine Admin
appengine.projects.locations.applications.repair
Create
API Only
GCP Compute Engine
compute.firewallPolicies.list
View
API Only
GCP Compute Engine
compute.firewallPolicies.insert
Create
API Only
GCP Compute Engine
compute.firewallPolicies.listAssociations
View
API Only
GCP Compute Engine
compute.firewallPolicies.delete
Delete
API Only
GCP Compute Engine
compute.firewallPolicies.get
View
API Only
GCP Compute Engine
compute.firewallPolicies.patch
Edit
API Only
GCP Compute Engine
compute.firewallPolicies.addAssociation
Create
API Only
GCP Compute Engine
compute.firewallPolicies.addRule
Create
API Only
GCP Compute Engine
compute.firewallPolicies.cloneRules
Create
API Only
GCP Compute Engine
compute.firewallPolicies.getAssociation
View
API Only
GCP Compute Engine
compute.firewallPolicies.getRule
View
API Only
GCP Compute Engine
compute.firewallPolicies.move
Move
API Only
GCP Compute Engine
compute.firewallPolicies.patchRule
Create
API Only
GCP Compute Engine
compute.firewallPolicies.removeAssociation
Delete
API Only
GCP Compute Engine
compute.firewallPolicies.removeRule
Delete
API Only
GCP Compute Engine
compute.firewallPolicies.getIamPolicy
View
API Only
GCP Compute Engine
compute.firewallPolicies.setIamPolicy
Create
API Only
GCP Compute Engine
compute.firewallPolicies.testIamPermissions
Create
API Only
GCP Compute Engine
compute.globalOrganizationOperations.list
View
API Only
GCP Compute Engine
compute.globalOrganizationOperations.delete
Delete
API Only
GCP Compute Engine
compute.globalOrganizationOperations.get
View
API Only
GCP Compute Engine
compute.projects.get
View
API Only
GCP Compute Engine
compute.acceleratorTypes.aggregatedList
View
API Only
GCP Compute Engine
compute.addresses.aggregatedList
View
API Only
GCP Compute Engine
compute.autoscalers.aggregatedList
View
API Only
GCP Compute Engine
compute.backendServices.aggregatedList
View
API Only
GCP Compute Engine
compute.regionCommitments.aggregatedList
View
API Only
GCP Compute Engine
compute.diskTypes.aggregatedList
View
API Only
GCP Compute Engine
compute.disks.aggregatedList
View
API Only
GCP Compute Engine
compute.forwardingRules.aggregatedList
View
API Only
GCP Compute Engine
compute.healthChecks.aggregatedList
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.aggregatedList
View
API Only
GCP Compute Engine
compute.instanceGroups.aggregatedList
View
API Only
GCP Compute Engine
compute.instanceTemplates.aggregatedList
View
API Only
GCP Compute Engine
compute.instances.aggregatedList
View
API Only
GCP Compute Engine
compute.interconnectAttachments.aggregatedList
View
API Only
GCP Compute Engine
compute.machineTypes.aggregatedList
View
API Only
GCP Compute Engine
compute.networkAttachments.aggregatedList
View
API Only
GCP Compute Engine
compute.networkEdgeSecurityServices.aggregatedList
View
API Only
GCP Compute Engine
compute.networkEndpointGroups.aggregatedList
View
API Only
GCP Compute Engine
compute.nodeGroups.aggregatedList
View
API Only
GCP Compute Engine
compute.nodeTemplates.aggregatedList
View
API Only
GCP Compute Engine
compute.nodeTypes.aggregatedList
View
API Only
GCP Compute Engine
compute.globalOperations.aggregatedList
View
API Only
GCP Compute Engine
compute.packetMirrorings.aggregatedList
View
API Only
GCP Compute Engine
compute.publicDelegatedPrefixes.aggregatedList
View
API Only
GCP Compute Engine
compute.reservations.aggregatedList
View
API Only
GCP Compute Engine
compute.resourcePolicies.aggregatedList
View
API Only
GCP Compute Engine
compute.routers.aggregatedList
View
API Only
GCP Compute Engine
compute.securityPolicies.aggregatedList
View
API Only
GCP Compute Engine
compute.serviceAttachments.aggregatedList
View
API Only
GCP Compute Engine
compute.sslCertificates.aggregatedList
View
API Only
GCP Compute Engine
compute.sslPolicies.aggregatedList
View
API Only
GCP Compute Engine
compute.subnetworks.aggregatedList
View
API Only
GCP Compute Engine
compute.subnetworks.listUsable
View
API Only
GCP Compute Engine
compute.targetHttpProxies.aggregatedList
View
API Only
GCP Compute Engine
compute.targetHttpsProxies.aggregatedList
View
API Only
GCP Compute Engine
compute.targetInstances.aggregatedList
View
API Only
GCP Compute Engine
compute.targetPools.aggregatedList
View
API Only
GCP Compute Engine
compute.targetTcpProxies.aggregatedList
View
API Only
GCP Compute Engine
compute.targetVpnGateways.aggregatedList
View
API Only
GCP Compute Engine
compute.urlMaps.aggregatedList
View
API Only
GCP Compute Engine
compute.vpnGateways.aggregatedList
View
API Only
GCP Compute Engine
compute.vpnTunnels.aggregatedList
View
API Only
GCP Compute Engine
compute.projects.disableXpnHost
Edit
API Only
GCP Compute Engine
compute.projects.disableXpnResource
Edit
API Only
GCP Compute Engine
compute.projects.enableXpnHost
Enable
API Only
GCP Compute Engine
compute.projects.enableXpnResource
Enable
API Only
GCP Compute Engine
compute.projects.getXpnHost
View
API Only
GCP Compute Engine
compute.projects.getXpnResources
View
API Only
GCP Compute Engine
compute.globalAddresses.list
View
API Only
GCP Compute Engine
compute.globalAddresses.insert
Create
API Only
GCP Compute Engine
compute.globalAddresses.delete
Delete
API Only
GCP Compute Engine
compute.globalAddresses.get
View
API Only
GCP Compute Engine
compute.globalAddresses.move
Move
API Only
GCP Compute Engine
compute.globalAddresses.setLabels
Create
API Only
GCP Compute Engine
compute.backendBuckets.list
View
API Only
GCP Compute Engine
compute.backendBuckets.insert
Create
API Only
GCP Compute Engine
compute.backendBuckets.delete
Delete
API Only
GCP Compute Engine
compute.backendBuckets.get
View
API Only
GCP Compute Engine
compute.backendBuckets.patch
Edit
API Only
GCP Compute Engine
compute.backendBuckets.update
Edit
API Only
GCP Compute Engine
compute.backendBuckets.addSignedUrlKey
Create
API Only
GCP Compute Engine
compute.backendBuckets.deleteSignedUrlKey
Delete
API Only
GCP Compute Engine
compute.backendBuckets.setEdgeSecurityPolicy
Create
API Only
GCP Compute Engine
compute.backendServices.list
View
API Only
GCP Compute Engine
compute.backendServices.insert
Create
API Only
GCP Compute Engine
compute.backendServices.delete
Delete
API Only
GCP Compute Engine
compute.backendServices.get
View
API Only
GCP Compute Engine
compute.backendServices.patch
Edit
API Only
GCP Compute Engine
compute.backendServices.update
Edit
API Only
GCP Compute Engine
compute.backendServices.addSignedUrlKey
Create
API Only
GCP Compute Engine
compute.backendServices.deleteSignedUrlKey
Delete
API Only
GCP Compute Engine
compute.backendServices.getHealth
View
API Only
GCP Compute Engine
compute.backendServices.setEdgeSecurityPolicy
Create
API Only
GCP Compute Engine
compute.backendServices.setSecurityPolicy
Create
API Only
GCP Compute Engine
compute.backendServices.getIamPolicy
View
API Only
GCP Compute Engine
compute.backendServices.setIamPolicy
Create
API Only
GCP Compute Engine
compute.externalVpnGateways.list
View
API Only
GCP Compute Engine
compute.externalVpnGateways.insert
Create
API Only
GCP Compute Engine
compute.externalVpnGateways.delete
Delete
API Only
GCP Compute Engine
compute.externalVpnGateways.get
View
API Only
GCP Compute Engine
compute.externalVpnGateways.setLabels
Create
API Only
GCP Compute Engine
compute.externalVpnGateways.testIamPermissions
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.list
View
API Only
GCP Compute Engine
compute.networkFirewallPolicies.insert
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.delete
Delete
API Only
GCP Compute Engine
compute.networkFirewallPolicies.get
View
API Only
GCP Compute Engine
compute.networkFirewallPolicies.patch
Edit
API Only
GCP Compute Engine
compute.networkFirewallPolicies.addAssociation
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.addRule
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.cloneRules
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.getAssociation
View
API Only
GCP Compute Engine
compute.networkFirewallPolicies.getRule
View
API Only
GCP Compute Engine
compute.networkFirewallPolicies.patchRule
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.removeAssociation
Delete
API Only
GCP Compute Engine
compute.networkFirewallPolicies.removeRule
Delete
API Only
GCP Compute Engine
compute.networkFirewallPolicies.getIamPolicy
View
API Only
GCP Compute Engine
compute.networkFirewallPolicies.setIamPolicy
Create
API Only
GCP Compute Engine
compute.networkFirewallPolicies.testIamPermissions
Create
API Only
GCP Compute Engine
compute.firewalls.list
View
API Only
GCP Compute Engine
compute.firewalls.insert
Create
API Only
GCP Compute Engine
compute.firewalls.delete
Delete
API Only
GCP Compute Engine
compute.firewalls.get
View
API Only
GCP Compute Engine
compute.firewalls.patch
Edit
API Only
GCP Compute Engine
compute.firewalls.update
Edit
API Only
GCP Compute Engine
compute.globalForwardingRules.list
View
API Only
GCP Compute Engine
compute.globalForwardingRules.insert
Create
API Only
GCP Compute Engine
compute.globalForwardingRules.delete
Delete
API Only
GCP Compute Engine
compute.globalForwardingRules.get
View
API Only
GCP Compute Engine
compute.globalForwardingRules.patch
Edit
API Only
GCP Compute Engine
compute.globalForwardingRules.setTarget
Create
API Only
GCP Compute Engine
compute.globalForwardingRules.setLabels
Create
API Only
GCP Compute Engine
compute.healthChecks.list
View
API Only
GCP Compute Engine
compute.healthChecks.insert
Create
API Only
GCP Compute Engine
compute.healthChecks.delete
Delete
API Only
GCP Compute Engine
compute.healthChecks.get
View
API Only
GCP Compute Engine
compute.healthChecks.patch
Edit
API Only
GCP Compute Engine
compute.healthChecks.update
Edit
API Only
GCP Compute Engine
compute.httpHealthChecks.list
View
API Only
GCP Compute Engine
compute.httpHealthChecks.insert
Create
API Only
GCP Compute Engine
compute.httpHealthChecks.delete
Delete
API Only
GCP Compute Engine
compute.httpHealthChecks.get
View
API Only
GCP Compute Engine
compute.httpHealthChecks.patch
Edit
API Only
GCP Compute Engine
compute.httpHealthChecks.update
Edit
API Only
GCP Compute Engine
compute.httpsHealthChecks.list
View
API Only
GCP Compute Engine
compute.httpsHealthChecks.insert
Create
API Only
GCP Compute Engine
compute.httpsHealthChecks.delete
Delete
API Only
GCP Compute Engine
compute.httpsHealthChecks.get
View
API Only
GCP Compute Engine
compute.httpsHealthChecks.patch
Edit
API Only
GCP Compute Engine
compute.httpsHealthChecks.update
Edit
API Only
GCP Compute Engine
compute.images.list
View
API Only
GCP Compute Engine
compute.images.insert
Create
API Only
GCP Compute Engine
compute.images.getFromFamily
View
API Only
GCP Compute Engine
compute.images.delete
Delete
API Only
GCP Compute Engine
compute.images.get
View
API Only
GCP Compute Engine
compute.images.patch
Edit
API Only
GCP Compute Engine
compute.images.deprecate
Delete
API Only
GCP Compute Engine
compute.images.getIamPolicy
View
API Only
GCP Compute Engine
compute.images.setIamPolicy
Create
API Only
GCP Compute Engine
compute.images.setLabels
Create
API Only
GCP Compute Engine
compute.images.testIamPermissions
Create
API Only
GCP Compute Engine
compute.instanceTemplates.list
View
API Only
GCP Compute Engine
compute.instanceTemplates.insert
Create
API Only
GCP Compute Engine
compute.instanceTemplates.delete
Delete
API Only
GCP Compute Engine
compute.instanceTemplates.get
View
API Only
GCP Compute Engine
compute.instanceTemplates.getIamPolicy
View
API Only
GCP Compute Engine
compute.instanceTemplates.setIamPolicy
Create
API Only
GCP Compute Engine
compute.instanceTemplates.testIamPermissions
Create
API Only
GCP Compute Engine
compute.interconnectLocations.list
View
API Only
GCP Compute Engine
compute.interconnectLocations.get
View
API Only
GCP Compute Engine
compute.interconnectRemoteLocations.list
View
API Only
GCP Compute Engine
compute.interconnectRemoteLocations.get
View
API Only
GCP Compute Engine
compute.interconnects.list
View
API Only
GCP Compute Engine
compute.interconnects.insert
Create
API Only
GCP Compute Engine
compute.interconnects.delete
Delete
API Only
GCP Compute Engine
compute.interconnects.get
View
API Only
GCP Compute Engine
compute.interconnects.patch
Edit
API Only
GCP Compute Engine
compute.interconnects.getDiagnostics
View
API Only
GCP Compute Engine
compute.interconnects.setLabels
Create
API Only
GCP Compute Engine
compute.licenseCodes.get
View
API Only
GCP Compute Engine
compute.licenseCodes.testIamPermissions
Create
API Only
GCP Compute Engine
compute.licenses.list
View
API Only
GCP Compute Engine
compute.licenses.insert
Create
API Only
GCP Compute Engine
compute.licenses.delete
Delete
API Only
GCP Compute Engine
compute.licenses.get
View
API Only
GCP Compute Engine
compute.licenses.getIamPolicy
View
API Only
GCP Compute Engine
compute.licenses.setIamPolicy
Create
API Only
GCP Compute Engine
compute.licenses.testIamPermissions
Create
API Only
GCP Compute Engine
compute.machineImages.list
View
API Only
GCP Compute Engine
compute.machineImages.insert
Create
API Only
GCP Compute Engine
compute.machineImages.delete
Delete
API Only
GCP Compute Engine
compute.machineImages.get
View
API Only
GCP Compute Engine
compute.machineImages.getIamPolicy
View
API Only
GCP Compute Engine
compute.machineImages.setIamPolicy
Create
API Only
GCP Compute Engine
compute.machineImages.testIamPermissions
Create
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.list
View
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.insert
Create
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.delete
Delete
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.get
View
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.attachNetworkEndpoints
Attach
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.detachNetworkEndpoints
Delete
API Only
GCP Compute Engine
compute.globalNetworkEndpointGroups.listNetworkEndpoints
View
API Only
GCP Compute Engine
compute.networks.list
View
API Only
GCP Compute Engine
compute.networks.insert
Create
API Only
GCP Compute Engine
compute.networks.delete
Delete
API Only
GCP Compute Engine
compute.networks.get
View
API Only
GCP Compute Engine
compute.networks.patch
Edit
API Only
GCP Compute Engine
compute.networks.addPeering
Create
API Only
GCP Compute Engine
compute.networks.getEffectiveFirewalls
View
API Only
GCP Compute Engine
compute.networks.listPeeringRoutes
View
API Only
GCP Compute Engine
compute.networks.removePeering
Delete
API Only
GCP Compute Engine
compute.networks.switchToCustomMode
Create
API Only
GCP Compute Engine
compute.networks.updatePeering
Edit
API Only
GCP Compute Engine
compute.globalOperations.list
View
API Only
GCP Compute Engine
compute.globalOperations.delete
Delete
API Only
GCP Compute Engine
compute.globalOperations.get
View
API Only
GCP Compute Engine
compute.globalOperations.wait
Create
API Only
GCP Compute Engine
compute.publicAdvertisedPrefixes.list
View
API Only
GCP Compute Engine
compute.publicAdvertisedPrefixes.insert
Create
API Only
GCP Compute Engine
compute.publicAdvertisedPrefixes.delete
Delete
API Only
GCP Compute Engine
compute.publicAdvertisedPrefixes.get
View
API Only
GCP Compute Engine
compute.publicAdvertisedPrefixes.patch
Edit
API Only
GCP Compute Engine
compute.globalPublicDelegatedPrefixes.list
View
API Only
GCP Compute Engine
compute.globalPublicDelegatedPrefixes.insert
Create
API Only
GCP Compute Engine
compute.globalPublicDelegatedPrefixes.delete
Delete
API Only
GCP Compute Engine
compute.globalPublicDelegatedPrefixes.get
View
API Only
GCP Compute Engine
compute.globalPublicDelegatedPrefixes.patch
Edit
API Only
GCP Compute Engine
compute.routes.list
View
API Only
GCP Compute Engine
compute.routes.insert
Create
API Only
GCP Compute Engine
compute.routes.delete
Delete
API Only
GCP Compute Engine
compute.routes.get
View
API Only
GCP Compute Engine
compute.securityPolicies.list
View
API Only
GCP Compute Engine
compute.securityPolicies.insert
Create
API Only
GCP Compute Engine
compute.securityPolicies.listPreconfiguredExpressionSets
View
API Only
GCP Compute Engine
compute.securityPolicies.setLabels
Create
API Only
GCP Compute Engine
compute.securityPolicies.delete
Delete
API Only
GCP Compute Engine
compute.securityPolicies.get
View
API Only
GCP Compute Engine
compute.securityPolicies.patch
Edit
API Only
GCP Compute Engine
compute.securityPolicies.addRule
Create
API Only
GCP Compute Engine
compute.securityPolicies.getRule
View
API Only
GCP Compute Engine
compute.securityPolicies.patchRule
Create
API Only
GCP Compute Engine
compute.securityPolicies.removeRule
Delete
API Only
GCP Compute Engine
compute.snapshots.list
View
API Only
GCP Compute Engine
compute.snapshots.insert
Create
API Only
GCP Compute Engine
compute.snapshots.getIamPolicy
View
API Only
GCP Compute Engine
compute.snapshots.setIamPolicy
Create
API Only
GCP Compute Engine
compute.snapshots.setLabels
Create
API Only
GCP Compute Engine
compute.snapshots.testIamPermissions
Create
API Only
GCP Compute Engine
compute.snapshots.delete
Delete
API Only
GCP Compute Engine
compute.snapshots.get
View
API Only
GCP Compute Engine
compute.sslCertificates.list
View
API Only
GCP Compute Engine
compute.sslCertificates.insert
Create
API Only
GCP Compute Engine
compute.sslCertificates.delete
Delete
API Only
GCP Compute Engine
compute.sslCertificates.get
View
API Only
GCP Compute Engine
compute.sslPolicies.list
View
API Only
GCP Compute Engine
compute.sslPolicies.insert
Create
API Only
GCP Compute Engine
compute.sslPolicies.listAvailableFeatures
View
API Only
GCP Compute Engine
compute.sslPolicies.delete
Delete
API Only
GCP Compute Engine
compute.sslPolicies.get
View
API Only
GCP Compute Engine
compute.sslPolicies.patch
Edit
API Only
GCP Compute Engine
compute.targetGrpcProxies.list
View
API Only
GCP Compute Engine
compute.targetGrpcProxies.insert
Create
API Only
GCP Compute Engine
compute.targetGrpcProxies.delete
Delete
API Only
GCP Compute Engine
compute.targetGrpcProxies.get
View
API Only
GCP Compute Engine
compute.targetGrpcProxies.patch
Edit
API Only
GCP Compute Engine
compute.targetHttpProxies.list
View
API Only
GCP Compute Engine
compute.targetHttpProxies.insert
Create
API Only
GCP Compute Engine
compute.targetHttpProxies.delete
Delete
API Only
GCP Compute Engine
compute.targetHttpProxies.get
View
API Only
GCP Compute Engine
compute.targetHttpProxies.patch
Edit
API Only
GCP Compute Engine
compute.targetHttpsProxies.list
View
API Only
GCP Compute Engine
compute.targetHttpsProxies.insert
Create
API Only
GCP Compute Engine
compute.targetHttpsProxies.delete
Delete
API Only
GCP Compute Engine
compute.targetHttpsProxies.get
View
API Only
GCP Compute Engine
compute.targetHttpsProxies.patch
Edit
API Only
GCP Compute Engine
compute.targetHttpsProxies.setCertificateMap
Create
API Only
GCP Compute Engine
compute.targetHttpsProxies.setQuicOverride
Create
API Only
GCP Compute Engine
compute.targetHttpsProxies.setSslPolicy
Create
API Only
GCP Compute Engine
compute.targetSslProxies.list
View
API Only
GCP Compute Engine
compute.targetSslProxies.insert
Create
API Only
GCP Compute Engine
compute.targetSslProxies.delete
Delete
API Only
GCP Compute Engine
compute.targetSslProxies.get
View
API Only
GCP Compute Engine
compute.targetSslProxies.setBackendService
Create
API Only
GCP Compute Engine
compute.targetSslProxies.setCertificateMap
Create
API Only
GCP Compute Engine
compute.targetSslProxies.setProxyHeader
Create
API Only
GCP Compute Engine
compute.targetSslProxies.setSslCertificates
Create
API Only
GCP Compute Engine
compute.targetSslProxies.setSslPolicy
Create
API Only
GCP Compute Engine
compute.targetTcpProxies.list
View
API Only
GCP Compute Engine
compute.targetTcpProxies.insert
Create
API Only
GCP Compute Engine
compute.targetTcpProxies.delete
Delete
API Only
GCP Compute Engine
compute.targetTcpProxies.get
View
API Only
GCP Compute Engine
compute.targetTcpProxies.setBackendService
Create
API Only
GCP Compute Engine
compute.targetTcpProxies.setProxyHeader
Create
API Only
GCP Compute Engine
compute.urlMaps.list
View
API Only
GCP Compute Engine
compute.urlMaps.insert
Create
API Only
GCP Compute Engine
compute.urlMaps.delete
Delete
API Only
GCP Compute Engine
compute.urlMaps.get
View
API Only
GCP Compute Engine
compute.urlMaps.patch
Edit
API Only
GCP Compute Engine
compute.urlMaps.update
Edit
API Only
GCP Compute Engine
compute.urlMaps.invalidateCache
Create
API Only
GCP Compute Engine
compute.urlMaps.validate
Create
API Only
GCP Compute Engine
compute.projects.listXpnHosts
View
API Only
GCP Compute Engine
compute.projects.moveDisk
Move
API Only
GCP Compute Engine
compute.projects.moveInstance
Move
API Only
GCP Compute Engine
compute.regions.list
View
API Only
GCP Compute Engine
compute.regions.get
View
API Only
GCP Compute Engine
compute.addresses.list
View
API Only
GCP Compute Engine
compute.addresses.insert
Create
API Only
GCP Compute Engine
compute.addresses.delete
Delete
API Only
GCP Compute Engine
compute.addresses.get
View
API Only
GCP Compute Engine
compute.addresses.move
Move
API Only
GCP Compute Engine
compute.addresses.setLabels
Create
API Only
GCP Compute Engine
compute.regionAutoscalers.list
View
API Only
GCP Compute Engine
compute.regionAutoscalers.patch
Edit
API Only
GCP Compute Engine
compute.regionAutoscalers.insert
Create
API Only
GCP Compute Engine
compute.regionAutoscalers.update
Edit
API Only
GCP Compute Engine
compute.regionAutoscalers.delete
Delete
API Only
GCP Compute Engine
compute.regionAutoscalers.get
View
API Only
GCP Compute Engine
compute.regionBackendServices.list
View
API Only
GCP Compute Engine
compute.regionBackendServices.insert
Create
API Only
GCP Compute Engine
compute.regionBackendServices.delete
Delete
API Only
GCP Compute Engine
compute.regionBackendServices.get
View
API Only
GCP Compute Engine
compute.regionBackendServices.patch
Edit
API Only
GCP Compute Engine
compute.regionBackendServices.update
Edit
API Only
GCP Compute Engine
compute.regionBackendServices.getHealth
View
API Only
GCP Compute Engine
compute.regionBackendServices.getIamPolicy
View
API Only
GCP Compute Engine
compute.regionBackendServices.setIamPolicy
Create
API Only
GCP Compute Engine
compute.regionCommitments.list
View
API Only
GCP Compute Engine
compute.regionCommitments.insert
Create
API Only
GCP Compute Engine
compute.regionCommitments.get
View
API Only
GCP Compute Engine
compute.regionCommitments.update
Edit
API Only
GCP Compute Engine
compute.regionDiskTypes.list
View
API Only
GCP Compute Engine
compute.regionDiskTypes.get
View
API Only
GCP Compute Engine
compute.regionDisks.list
View
API Only
GCP Compute Engine
compute.regionDisks.insert
Create
API Only
GCP Compute Engine
compute.regionDisks.bulkInsert
Create
API Only
GCP Compute Engine
compute.regionDisks.stopGroupAsyncReplication
Stop
API Only
GCP Compute Engine
compute.regionDisks.delete
Delete
API Only
GCP Compute Engine
compute.regionDisks.get
View
API Only
GCP Compute Engine
compute.regionDisks.update
Edit
API Only
GCP Compute Engine
compute.regionDisks.addResourcePolicies
Create
API Only
GCP Compute Engine
compute.regionDisks.createSnapshot
Create
API Only
GCP Compute Engine
compute.regionDisks.removeResourcePolicies
Delete
API Only
GCP Compute Engine
compute.regionDisks.resize
Edit
API Only
GCP Compute Engine
compute.regionDisks.startAsyncReplication
Start
API Only
GCP Compute Engine
compute.regionDisks.stopAsyncReplication
Stop
API Only
GCP Compute Engine
compute.regionDisks.getIamPolicy
View
API Only
GCP Compute Engine
compute.regionDisks.setIamPolicy
Create
API Only
GCP Compute Engine
compute.regionDisks.setLabels
Create
API Only
GCP Compute Engine
compute.regionDisks.testIamPermissions
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.list
View
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.insert
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.getEffectiveFirewalls
View
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.delete
Delete
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.get
View
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.patch
Edit
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.addAssociation
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.addRule
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.cloneRules
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.getAssociation
View
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.getRule
View
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.patchRule
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.removeAssociation
Delete
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.removeRule
Delete
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.getIamPolicy
View
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.setIamPolicy
Create
API Only
GCP Compute Engine
compute.regionNetworkFirewallPolicies.testIamPermissions
Create
API Only
GCP Compute Engine
compute.forwardingRules.list
View
API Only
GCP Compute Engine
compute.forwardingRules.insert
Create
API Only
GCP Compute Engine
compute.forwardingRules.delete
Delete
API Only
GCP Compute Engine
compute.forwardingRules.get
View
API Only
GCP Compute Engine
compute.forwardingRules.patch
Edit
API Only
GCP Compute Engine
compute.forwardingRules.setTarget
Create
API Only
GCP Compute Engine
compute.forwardingRules.setLabels
Create
API Only
GCP Compute Engine
compute.regionHealthCheckServices.list
View
API Only
GCP Compute Engine
compute.regionHealthCheckServices.insert
Create
API Only
GCP Compute Engine
compute.regionHealthCheckServices.delete
Delete
API Only
GCP Compute Engine
compute.regionHealthCheckServices.get
View
API Only
GCP Compute Engine
compute.regionHealthCheckServices.patch
Edit
API Only
GCP Compute Engine
compute.regionHealthChecks.list
View
API Only
GCP Compute Engine
compute.regionHealthChecks.insert
Create
API Only
GCP Compute Engine
compute.regionHealthChecks.delete
Delete
API Only
GCP Compute Engine
compute.regionHealthChecks.get
View
API Only
GCP Compute Engine
compute.regionHealthChecks.patch
Edit
API Only
GCP Compute Engine
compute.regionHealthChecks.update
Edit
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.list
View
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.insert
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.delete
Delete
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.get
View
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.patch
Edit
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.abandonInstances
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.applyUpdatesToInstances
Edit
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.createInstances
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.deleteInstances
Delete
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.deletePerInstanceConfigs
Delete
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.listErrors
View
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.listManagedInstances
View
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.listPerInstanceConfigs
View
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.patchPerInstanceConfigs
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.recreateInstances
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.resize
Edit
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.setInstanceTemplate
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.setTargetPools
Create
API Only
GCP Compute Engine
compute.regionInstanceGroupManagers.updatePerInstanceConfigs
Edit
API Only
GCP Compute Engine
compute.regionInstanceGroups.list
View
API Only
GCP Compute Engine
compute.regionInstanceGroups.get
View
API Only
GCP Compute Engine
compute.regionInstanceGroups.listInstances
View
API Only
GCP Compute Engine
compute.regionInstanceGroups.setNamedPorts
Create
API Only
GCP Compute Engine
compute.regionInstanceTemplates.list
View
API Only
GCP Compute Engine
compute.regionInstanceTemplates.insert
Create
API Only
GCP Compute Engine
compute.regionInstanceTemplates.delete
Delete
API Only
GCP Compute Engine
compute.regionInstanceTemplates.get
View
API Only
GCP Compute Engine
compute.regionInstances.bulkInsert
Create
API Only
GCP Compute Engine
compute.interconnectAttachments.list
View
API Only
GCP Compute Engine
compute.interconnectAttachments.insert
Create
API Only
GCP Compute Engine
compute.interconnectAttachments.delete
Delete
API Only
GCP Compute Engine
compute.interconnectAttachments.get
View
API Only
GCP Compute Engine
compute.interconnectAttachments.patch
Edit
API Only
GCP Compute Engine
compute.interconnectAttachments.setLabels
Create
API Only
GCP Compute Engine
compute.networkAttachments.list
View
API Only
GCP Compute Engine
compute.networkAttachments.insert
Create
API Only
GCP Compute Engine
compute.networkAttachments.delete
Delete
API Only
GCP Compute Engine
compute.networkAttachments.get
View
API Only
GCP Compute Engine
compute.networkAttachments.getIamPolicy
View
API Only
GCP Compute Engine
compute.networkAttachments.setIamPolicy
Create
API Only
GCP Compute Engine
compute.networkAttachments.testIamPermissions
Create
API Only
GCP Compute Engine
compute.networkEdgeSecurityServices.insert
Create
API Only
GCP Compute Engine
compute.networkEdgeSecurityServices.delete
Delete
API Only
GCP Compute Engine
compute.networkEdgeSecurityServices.get
View
API Only
GCP Compute Engine
compute.networkEdgeSecurityServices.patch
Edit
API Only
GCP Compute Engine
compute.regionNetworkEndpointGroups.list
View
API Only
GCP Compute Engine
compute.regionNetworkEndpointGroups.insert
Create
API Only
GCP Compute Engine
compute.regionNetworkEndpointGroups.delete
Delete
API Only
GCP Compute Engine
compute.regionNetworkEndpointGroups.get
View
API Only
GCP Compute Engine
compute.nodeTemplates.list
View
API Only
GCP Compute Engine
compute.nodeTemplates.insert
Create
API Only
GCP Compute Engine
compute.nodeTemplates.delete
Delete
API Only
GCP Compute Engine
compute.nodeTemplates.get
View
API Only
GCP Compute Engine
compute.nodeTemplates.getIamPolicy
View
API Only
GCP Compute Engine
compute.nodeTemplates.setIamPolicy
Create
API Only
GCP Compute Engine
compute.nodeTemplates.testIamPermissions
Create
API Only
GCP Compute Engine
compute.regionNotificationEndpoints.list
View
API Only
GCP Compute Engine
compute.regionNotificationEndpoints.insert
Create
API Only
GCP Compute Engine
compute.regionNotificationEndpoints.delete
Delete
API Only
GCP Compute Engine
compute.regionNotificationEndpoints.get
View
API Only
GCP Compute Engine
compute.regionOperations.list
View
API Only
GCP Compute Engine
compute.regionOperations.delete
Delete
API Only
GCP Compute Engine
compute.regionOperations.get
View
API Only
GCP Compute Engine
compute.regionOperations.wait
Create
API Only
GCP Compute Engine
compute.packetMirrorings.list
View
API Only
GCP Compute Engine
compute.packetMirrorings.insert
Create
API Only
GCP Compute Engine
compute.packetMirrorings.delete
Delete
API Only
GCP Compute Engine
compute.packetMirrorings.get
View
API Only
GCP Compute Engine
compute.packetMirrorings.patch
Edit
API Only
GCP Compute Engine
compute.packetMirrorings.testIamPermissions
Create
API Only
GCP Compute Engine
compute.publicDelegatedPrefixes.list
View
API Only
GCP Compute Engine
compute.publicDelegatedPrefixes.insert
Create
API Only
GCP Compute Engine
compute.publicDelegatedPrefixes.delete
Delete
API Only
GCP Compute Engine
compute.publicDelegatedPrefixes.get
View
API Only
GCP Compute Engine
compute.publicDelegatedPrefixes.patch
Edit
API Only
GCP Compute Engine
compute.resourcePolicies.list
View
API Only
GCP Compute Engine
compute.resourcePolicies.insert
Create
API Only
GCP Compute Engine
compute.resourcePolicies.delete
Delete
API Only
GCP Compute Engine
compute.resourcePolicies.get
View
API Only
GCP Compute Engine
compute.resourcePolicies.getIamPolicy
View
API Only
GCP Compute Engine
compute.resourcePolicies.setIamPolicy
Create
API Only
GCP Compute Engine
compute.resourcePolicies.testIamPermissions
Create
API Only
GCP Compute Engine
compute.routers.list
View
API Only
GCP Compute Engine
compute.routers.insert
Create
API Only
GCP Compute Engine
compute.routers.delete
Delete
API Only
GCP Compute Engine
compute.routers.get
View
API Only
GCP Compute Engine
compute.routers.patch
Edit
API Only
GCP Compute Engine
compute.routers.update
Edit
API Only
GCP Compute Engine
compute.routers.getNatMappingInfo
View
API Only
GCP Compute Engine
compute.routers.getRouterStatus
View
API Only
GCP Compute Engine
compute.routers.preview
Create
API Only
GCP Compute Engine
compute.regionSecurityPolicies.list
View
API Only
GCP Compute Engine
compute.regionSecurityPolicies.insert
Create
API Only
GCP Compute Engine
compute.regionSecurityPolicies.delete
Delete
API Only
GCP Compute Engine
compute.regionSecurityPolicies.get
View
API Only
GCP Compute Engine
compute.regionSecurityPolicies.patch
Edit
API Only
GCP Compute Engine
compute.serviceAttachments.list
View
API Only
GCP Compute Engine
compute.serviceAttachments.insert
Create
API Only
GCP Compute Engine
compute.serviceAttachments.getIamPolicy
View
API Only
GCP Compute Engine
compute.serviceAttachments.setIamPolicy
Create
API Only
GCP Compute Engine
compute.serviceAttachments.testIamPermissions
Create
API Only
GCP Compute Engine
compute.serviceAttachments.delete
Delete
API Only
GCP Compute Engine
compute.serviceAttachments.get
View
API Only
GCP Compute Engine
compute.serviceAttachments.patch
Edit
API Only
GCP Compute Engine
compute.regionSslCertificates.list
View
API Only
GCP Compute Engine
compute.regionSslCertificates.insert
Create
API Only
GCP Compute Engine
compute.regionSslCertificates.delete
Delete
API Only
GCP Compute Engine
compute.regionSslCertificates.get
View
API Only
GCP Compute Engine
compute.regionSslPolicies.list
View
API Only
GCP Compute Engine
compute.regionSslPolicies.insert
Create
API Only
GCP Compute Engine
compute.regionSslPolicies.listAvailableFeatures
View
API Only
GCP Compute Engine
compute.regionSslPolicies.delete
Delete
API Only
GCP Compute Engine
compute.regionSslPolicies.get
View
API Only
GCP Compute Engine
compute.regionSslPolicies.patch
Edit
API Only
GCP Compute Engine
compute.subnetworks.list
View
API Only
GCP Compute Engine
compute.subnetworks.insert
Create
API Only
GCP Compute Engine
compute.subnetworks.getIamPolicy
View
API Only
GCP Compute Engine
compute.subnetworks.setIamPolicy
Create
API Only
GCP Compute Engine
compute.subnetworks.testIamPermissions
Create
API Only
GCP Compute Engine
compute.subnetworks.delete
Delete
API Only
GCP Compute Engine
compute.subnetworks.get
View
API Only
GCP Compute Engine
compute.subnetworks.patch
Edit
API Only
GCP Compute Engine
compute.subnetworks.expandIpCidrRange
Create
API Only
GCP Compute Engine
compute.subnetworks.setPrivateIpGoogleAccess
Create
API Only
GCP Compute Engine
compute.regionTargetHttpProxies.list
View
API Only
GCP Compute Engine
compute.regionTargetHttpProxies.insert
Create
API Only
GCP Compute Engine
compute.regionTargetHttpProxies.delete
Delete
API Only
GCP Compute Engine
compute.regionTargetHttpProxies.get
View
API Only
GCP Compute Engine
compute.regionTargetHttpProxies.setUrlMap
Create
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.list
View
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.insert
Create
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.delete
Delete
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.get
View
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.patch
Edit
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.setSslCertificates
Create
API Only
GCP Compute Engine
compute.regionTargetHttpsProxies.setUrlMap
Create
API Only
GCP Compute Engine
compute.targetPools.list
View
API Only
GCP Compute Engine
compute.targetPools.insert
Create
API Only
GCP Compute Engine
compute.targetPools.delete
Delete
API Only
GCP Compute Engine
compute.targetPools.get
View
API Only
GCP Compute Engine
compute.targetPools.addHealthCheck
Create
API Only
GCP Compute Engine
compute.targetPools.addInstance
Create
API Only
GCP Compute Engine
compute.targetPools.getHealth
View
API Only
GCP Compute Engine
compute.targetPools.removeHealthCheck
Delete
API Only
GCP Compute Engine
compute.targetPools.removeInstance
Delete
API Only
GCP Compute Engine
compute.targetPools.setBackup
Create
API Only
GCP Compute Engine
compute.regionTargetTcpProxies.list
View
API Only
GCP Compute Engine
compute.regionTargetTcpProxies.insert
Create
API Only
GCP Compute Engine
compute.regionTargetTcpProxies.delete
Delete
API Only
GCP Compute Engine
compute.regionTargetTcpProxies.get
View
API Only
GCP Compute Engine
compute.targetVpnGateways.list
View
API Only
GCP Compute Engine
compute.targetVpnGateways.insert
Create
API Only
GCP Compute Engine
compute.targetVpnGateways.setLabels
Create
API Only
GCP Compute Engine
compute.targetVpnGateways.delete
Delete
API Only
GCP Compute Engine
compute.targetVpnGateways.get
View
API Only
GCP Compute Engine
compute.regionUrlMaps.list
View
API Only
GCP Compute Engine
compute.regionUrlMaps.insert
Create
API Only
GCP Compute Engine
compute.regionUrlMaps.delete
Delete
API Only
GCP Compute Engine
compute.regionUrlMaps.get
View
API Only
GCP Compute Engine
compute.regionUrlMaps.patch
Edit
API Only
GCP Compute Engine
compute.regionUrlMaps.update
Edit
API Only
GCP Compute Engine
compute.regionUrlMaps.validate
Create
API Only
GCP Compute Engine
compute.vpnGateways.list
View
API Only
GCP Compute Engine
compute.vpnGateways.insert
Create
API Only
GCP Compute Engine
compute.vpnGateways.setLabels
Create
API Only
GCP Compute Engine
compute.vpnGateways.testIamPermissions
Create
API Only
GCP Compute Engine
compute.vpnGateways.delete
Delete
API Only
GCP Compute Engine
compute.vpnGateways.get
View
API Only
GCP Compute Engine
compute.vpnGateways.getStatus
View
API Only
GCP Compute Engine
compute.vpnTunnels.list
View
API Only
GCP Compute Engine
compute.vpnTunnels.insert
Create
API Only
GCP Compute Engine
compute.vpnTunnels.setLabels
Create
API Only
GCP Compute Engine
compute.vpnTunnels.delete
Delete
API Only
GCP Compute Engine
compute.vpnTunnels.get
View
API Only
GCP Compute Engine
compute.projects.setCommonInstanceMetadata
Create
API Only
GCP Compute Engine
compute.projects.setDefaultNetworkTier
Create
API Only
GCP Compute Engine
compute.projects.setUsageExportBucket
Create
API Only
GCP Compute Engine
compute.targetHttpProxies.setUrlMap
Create
API Only
GCP Compute Engine
compute.targetHttpsProxies.setSslCertificates
Create
API Only
GCP Compute Engine
compute.targetHttpsProxies.setUrlMap
Create
API Only
GCP Compute Engine
compute.zones.list
View
API Only
GCP Compute Engine
compute.zones.get
View
API Only
GCP Compute Engine
compute.acceleratorTypes.list
View
API Only
GCP Compute Engine
compute.acceleratorTypes.get
View
API Only
GCP Compute Engine
compute.autoscalers.list
View
API Only
GCP Compute Engine
compute.autoscalers.patch
Edit
API Only
GCP Compute Engine
compute.autoscalers.insert
Create
API Only
GCP Compute Engine
compute.autoscalers.update
Edit
API Only
GCP Compute Engine
compute.autoscalers.delete
Delete
API Only
GCP Compute Engine
compute.autoscalers.get
View
API Only
GCP Compute Engine
compute.diskTypes.list
View
API Only
GCP Compute Engine
compute.diskTypes.get
View
API Only
GCP Compute Engine
compute.disks.list
View
API Only
GCP Compute Engine
compute.disks.insert
Create
API Only
GCP Compute Engine
compute.disks.bulkInsert
Create
API Only
GCP Compute Engine
compute.disks.stopGroupAsyncReplication
Stop
API Only
GCP Compute Engine
compute.disks.delete
Delete
API Only
GCP Compute Engine
compute.disks.get
View
API Only
GCP Compute Engine
compute.disks.update
Edit
API Only
GCP Compute Engine
compute.disks.addResourcePolicies
Create
API Only
GCP Compute Engine
compute.disks.createSnapshot
Create
API Only
GCP Compute Engine
compute.disks.removeResourcePolicies
Delete
API Only
GCP Compute Engine
compute.disks.resize
Edit
API Only
GCP Compute Engine
compute.disks.startAsyncReplication
Start
API Only
GCP Compute Engine
compute.disks.stopAsyncReplication
Stop
API Only
GCP Compute Engine
compute.disks.getIamPolicy
View
API Only
GCP Compute Engine
compute.disks.setIamPolicy
Create
API Only
GCP Compute Engine
compute.disks.setLabels
Create
API Only
GCP Compute Engine
compute.disks.testIamPermissions
Create
API Only
GCP Compute Engine
compute.imageFamilyViews.get
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.list
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.insert
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.delete
Delete
API Only
GCP Compute Engine
compute.instanceGroupManagers.get
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.patch
Edit
API Only
GCP Compute Engine
compute.instanceGroupManagers.abandonInstances
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.applyUpdatesToInstances
Edit
API Only
GCP Compute Engine
compute.instanceGroupManagers.createInstances
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.deleteInstances
Delete
API Only
GCP Compute Engine
compute.instanceGroupManagers.deletePerInstanceConfigs
Delete
API Only
GCP Compute Engine
compute.instanceGroupManagers.listErrors
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.listManagedInstances
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.listPerInstanceConfigs
View
API Only
GCP Compute Engine
compute.instanceGroupManagers.patchPerInstanceConfigs
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.recreateInstances
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.resize
Edit
API Only
GCP Compute Engine
compute.instanceGroupManagers.setInstanceTemplate
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.setTargetPools
Create
API Only
GCP Compute Engine
compute.instanceGroupManagers.updatePerInstanceConfigs
Edit
API Only
GCP Compute Engine
compute.instanceGroups.list
View
API Only
GCP Compute Engine
compute.instanceGroups.insert
Create
API Only
GCP Compute Engine
compute.instanceGroups.delete
Delete
API Only
GCP Compute Engine
compute.instanceGroups.get
View
API Only
GCP Compute Engine
compute.instanceGroups.addInstances
Create
API Only
GCP Compute Engine
compute.instanceGroups.listInstances
View
API Only
GCP Compute Engine
compute.instanceGroups.removeInstances
Delete
API Only
GCP Compute Engine
compute.instanceGroups.setNamedPorts
Create
API Only
GCP Compute Engine
compute.instances.list
View
API Only
GCP Compute Engine
compute.instances.insert
Create
API Only
GCP Compute Engine
compute.instances.bulkInsert
Create
API Only
GCP Compute Engine
compute.instances.delete
Delete
API Only
GCP Compute Engine
compute.instances.get
View
API Only
GCP Compute Engine
compute.instances.update
Edit
API Only
GCP Compute Engine
compute.instances.addAccessConfig
Create
API Only
GCP Compute Engine
compute.instances.addResourcePolicies
Create
API Only
GCP Compute Engine
compute.instances.attachDisk
Attach
API Only
GCP Compute Engine
compute.instances.deleteAccessConfig
Delete
API Only
GCP Compute Engine
compute.instances.detachDisk
Delete
API Only
GCP Compute Engine
compute.instances.getEffectiveFirewalls
View
API Only
GCP Compute Engine
compute.instances.getGuestAttributes
View
API Only
GCP Compute Engine
compute.instances.getShieldedInstanceIdentity
View
API Only
GCP Compute Engine
compute.instances.listReferrers
View
API Only
GCP Compute Engine
compute.instances.removeResourcePolicies
Delete
API Only
GCP Compute Engine
compute.instances.reset
Edit
API Only
GCP Compute Engine
compute.instances.resume
Start
API Only
GCP Compute Engine
compute.instances.getScreenshot
View
API Only
GCP Compute Engine
compute.instances.sendDiagnosticInterrupt
Send
API Only
GCP Compute Engine
compute.instances.getSerialPortOutput
View
API Only
GCP Compute Engine
compute.instances.setDiskAutoDelete
Create
API Only
GCP Compute Engine
compute.instances.setLabels
Create
API Only
GCP Compute Engine
compute.instances.setMachineResources
Create
API Only
GCP Compute Engine
compute.instances.setMachineType
Create
API Only
GCP Compute Engine
compute.instances.setMetadata
Create
API Only
GCP Compute Engine
compute.instances.setMinCpuPlatform
Create
API Only
GCP Compute Engine
compute.instances.setName
Create
API Only
GCP Compute Engine
compute.instances.setScheduling
Create
API Only
GCP Compute Engine
compute.instances.setServiceAccount
Create
API Only
GCP Compute Engine
compute.instances.setShieldedInstanceIntegrityPolicy
Create
API Only
GCP Compute Engine
compute.instances.setTags
Create
API Only
GCP Compute Engine
compute.instances.simulateMaintenanceEvent
Create
API Only
GCP Compute Engine
compute.instances.start
Start
API Only
GCP Compute Engine
compute.instances.startWithEncryptionKey
Start
API Only
GCP Compute Engine
compute.instances.stop
Stop
API Only
GCP Compute Engine
compute.instances.suspend
Delete
API Only
GCP Compute Engine
compute.instances.updateAccessConfig
Edit
API Only
GCP Compute Engine
compute.instances.updateDisplayDevice
Edit
API Only
GCP Compute Engine
compute.instances.updateNetworkInterface
Edit
API Only
GCP Compute Engine
compute.instances.updateShieldedInstanceConfig
Edit
API Only
GCP Compute Engine
compute.instances.getIamPolicy
View
API Only
GCP Compute Engine
compute.instances.setDeletionProtection
Create
API Only
GCP Compute Engine
compute.instances.setIamPolicy
Create
API Only
GCP Compute Engine
compute.instances.testIamPermissions
Create
API Only
GCP Compute Engine
compute.machineTypes.list
View
API Only
GCP Compute Engine
compute.machineTypes.get
View
API Only
GCP Compute Engine
compute.networkEndpointGroups.list
View
API Only
GCP Compute Engine
compute.networkEndpointGroups.insert
Create
API Only
GCP Compute Engine
compute.networkEndpointGroups.delete
Delete
API Only
GCP Compute Engine
compute.networkEndpointGroups.get
View
API Only
GCP Compute Engine
compute.networkEndpointGroups.attachNetworkEndpoints
Attach
API Only
GCP Compute Engine
compute.networkEndpointGroups.detachNetworkEndpoints
Delete
API Only
GCP Compute Engine
compute.networkEndpointGroups.listNetworkEndpoints
View
API Only
GCP Compute Engine
compute.networkEndpointGroups.testIamPermissions
Create
API Only
GCP Compute Engine
compute.nodeGroups.list
View
API Only
GCP Compute Engine
compute.nodeGroups.insert
Create
API Only
GCP Compute Engine
compute.nodeGroups.delete
Delete
API Only
GCP Compute Engine
compute.nodeGroups.get
View
API Only
GCP Compute Engine
compute.nodeGroups.patch
Edit
API Only
GCP Compute Engine
compute.nodeGroups.addNodes
Create
API Only
GCP Compute Engine
compute.nodeGroups.deleteNodes
Delete
API Only
GCP Compute Engine
compute.nodeGroups.listNodes
View
API Only
GCP Compute Engine
compute.nodeGroups.setNodeTemplate
Create
API Only
GCP Compute Engine
compute.nodeGroups.simulateMaintenanceEvent
Create
API Only
GCP Compute Engine
compute.nodeGroups.getIamPolicy
View
API Only
GCP Compute Engine
compute.nodeGroups.setIamPolicy
Create
API Only
GCP Compute Engine
compute.nodeGroups.testIamPermissions
Create
API Only
GCP Compute Engine
compute.nodeTypes.list
View
API Only
GCP Compute Engine
compute.nodeTypes.get
View
API Only
GCP Compute Engine
compute.zoneOperations.list
View
API Only
GCP Compute Engine
compute.zoneOperations.delete
Delete
API Only
GCP Compute Engine
compute.zoneOperations.get
View
API Only
GCP Compute Engine
compute.zoneOperations.wait
Create
API Only
GCP Compute Engine
compute.reservations.list
View
API Only
GCP Compute Engine
compute.reservations.insert
Create
API Only
GCP Compute Engine
compute.reservations.delete
Delete
API Only
GCP Compute Engine
compute.reservations.get
View
API Only
GCP Compute Engine
compute.reservations.update
Edit
API Only
GCP Compute Engine
compute.reservations.resize
Edit
API Only
GCP Compute Engine
compute.reservations.getIamPolicy
View
API Only
GCP Compute Engine
compute.reservations.setIamPolicy
Create
API Only
GCP Compute Engine
compute.reservations.testIamPermissions
Create
API Only
GCP Compute Engine
compute.targetInstances.list
View
API Only
GCP Compute Engine
compute.targetInstances.insert
Create
API Only
GCP Compute Engine
compute.targetInstances.delete
Delete
API Only
GCP Compute Engine
compute.targetInstances.get
View
API Only
GCP Recommender
recommender.projects.locations.recommenders.recommendations.get
View
API Only
GCP Recommender
recommender.projects.locations.recommenders.updateConfig
Edit
API Only
GCP Recommender
recommender.projects.locations.insightTypes.insights.markAccepted
Create
API Only
GCP Recommender
recommender.projects.locations.recommenders.recommendations.markClaimed
Create
API Only
GCP Recommender
recommender.projects.locations.recommenders.recommendations.markDismissed
Create
API Only
GCP Recommender
recommender.projects.locations.recommenders.recommendations.markFailed
Create
API Only
GCP Recommender
recommender.projects.locations.recommenders.recommendations.markSucceeded
Create
API Only
GCP Recommender
recommender.projects.locations.insightTypes.insights.list
View
API Only
GCP Recommender
recommender.projects.locations.recommenders.recommendations.list
View
API Only
GCP SQL Admin
sql.flags.list
View
API Only
GCP SQL Admin
sql.instances.list
View
API Only
GCP SQL Admin
sql.instances.insert
Create
API Only
GCP SQL Admin
sql.instances.delete
Delete
API Only
GCP SQL Admin
sql.instances.get
View
API Only
GCP SQL Admin
sql.instances.patch
Edit
API Only
GCP SQL Admin
sql.instances.update
Edit
API Only
GCP SQL Admin
sql.instances.addServerCa
Create
API Only
GCP SQL Admin
sql.backupRuns.list
View
API Only
GCP SQL Admin
sql.backupRuns.insert
Create
API Only
GCP SQL Admin
sql.backupRuns.delete
Delete
API Only
GCP SQL Admin
sql.backupRuns.get
View
API Only
GCP SQL Admin
sql.instances.clone
Create
API Only
GCP SQL Admin
sql.connect.get
View
API Only
GCP SQL Admin
sql.sslCerts.createEphemeral
Create
API Only
GCP SQL Admin
sql.databases.list
View
API Only
GCP SQL Admin
sql.databases.insert
Create
API Only
GCP SQL Admin
sql.databases.delete
Delete
API Only
GCP SQL Admin
sql.databases.get
View
API Only
GCP SQL Admin
sql.databases.patch
Edit
API Only
GCP SQL Admin
sql.databases.update
Edit
API Only
GCP SQL Admin
sql.instances.demoteMaster
Create
API Only
GCP SQL Admin
sql.instances.export
View
API Only
GCP SQL Admin
sql.instances.failover
Create
API Only
GCP SQL Admin
sql.projects.instances.getDiskShrinkConfig
View
API Only
GCP SQL Admin
sql.instances.import
Create
API Only
GCP SQL Admin
sql.instances.listServerCas
View
API Only
GCP SQL Admin
sql.projects.instances.performDiskShrink
Create
API Only
GCP SQL Admin
sql.instances.promoteReplica
Create
API Only
GCP SQL Admin
sql.instances.reencrypt
Create
API Only
GCP SQL Admin
sql.projects.instances.rescheduleMaintenance
Create
API Only
GCP SQL Admin
sql.projects.instances.resetReplicaSize
Edit
API Only
GCP SQL Admin
sql.instances.resetSslConfig
Edit
API Only
GCP SQL Admin
sql.instances.restart
Reboot
API Only
GCP SQL Admin
sql.instances.restoreBackup
Create
API Only
GCP SQL Admin
sql.instances.rotateServerCa
Create
API Only
GCP SQL Admin
sql.sslCerts.list
View
API Only
GCP SQL Admin
sql.sslCerts.insert
Create
API Only
GCP SQL Admin
sql.sslCerts.delete
Delete
API Only
GCP SQL Admin
sql.sslCerts.get
View
API Only
GCP SQL Admin
sql.projects.instances.startExternalSync
Start
API Only
GCP SQL Admin
sql.instances.startReplica
Start
API Only
GCP SQL Admin
sql.instances.stopReplica
Stop
API Only
GCP SQL Admin
sql.instances.truncateLog
Create
API Only
GCP SQL Admin
sql.users.delete
Delete
API Only
GCP SQL Admin
sql.users.list
View
API Only
GCP SQL Admin
sql.users.insert
Create
API Only
GCP SQL Admin
sql.users.update
Edit
API Only
GCP SQL Admin
sql.users.get
View
API Only
GCP SQL Admin
sql.projects.instances.verifyExternalSyncSettings
Create
API Only
GCP SQL Admin
sql.connect.generateEphemeral
Create
API Only
GCP SQL Admin
sql.operations.list
View
API Only
GCP SQL Admin
sql.operations.get
View
API Only
GCP SQL Admin
sql.operations.cancel
Delete
API Only
GCP SQL Admin
sql.tiers.list
View
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.delete
Delete
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.get
View
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.updateCredential
Edit
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.list
View
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.create
Create
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.getIamPolicy
View
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.setIamPolicy
Create
API Only
GCP BigQuery Connection
bigqueryconnection.projects.locations.connections.testIamPermissions
Create
API Only
GCP Search
cloudsearch.debug.datasources.items.searchByViewUrl
Search
API Only
GCP Search
cloudsearch.debug.datasources.items.checkAccess
Create
API Only
GCP Search
cloudsearch.debug.identitysources.items.listForunmappedidentity
View
API Only
GCP Search
cloudsearch.debug.identitysources.unmappedids.list
View
API Only
GCP Search
cloudsearch.indexing.datasources.items.delete
Delete
API Only
GCP Search
cloudsearch.indexing.datasources.items.get
View
API Only
GCP Search
cloudsearch.indexing.datasources.items.list
View
API Only
GCP Search
cloudsearch.indexing.datasources.items.deleteQueueItems
Delete
API Only
GCP Search
cloudsearch.indexing.datasources.items.poll
Create
API Only
GCP Search
cloudsearch.indexing.datasources.items.unreserve
Create
API Only
GCP Search
cloudsearch.indexing.datasources.deleteSchema
Delete
API Only
GCP Search
cloudsearch.indexing.datasources.getSchema
View
API Only
GCP Search
cloudsearch.indexing.datasources.updateSchema
Edit
API Only
GCP Search
cloudsearch.indexing.datasources.items.index
Create
API Only
GCP Search
cloudsearch.indexing.datasources.items.push
Create
API Only
GCP Search
cloudsearch.indexing.datasources.items.upload
Upload
API Only
GCP Search
cloudsearch.media.upload
Upload
API Only
GCP Search
cloudsearch.query.search
Search
API Only
GCP Search
cloudsearch.query.sources.list
View
API Only
GCP Search
cloudsearch.query.suggest
Create
API Only
GCP Search
cloudsearch.query.removeActivity
Delete
API Only
GCP Search
cloudsearch.settings.getCustomer
View
API Only
GCP Search
cloudsearch.settings.updateCustomer
Edit
API Only
GCP Search
cloudsearch.settings.datasources.list
View
API Only
GCP Search
cloudsearch.settings.datasources.create
Create
API Only
GCP Search
cloudsearch.settings.searchapplications.list
View
API Only
GCP Search
cloudsearch.settings.searchapplications.create
Create
API Only
GCP Search
cloudsearch.settings.searchapplications.delete
Delete
API Only
GCP Search
cloudsearch.settings.searchapplications.get
View
API Only
GCP Search
cloudsearch.settings.searchapplications.patch
Edit
API Only
GCP Search
cloudsearch.settings.searchapplications.update
Edit
API Only
GCP Search
cloudsearch.settings.searchapplications.reset
Edit
API Only
GCP Search
cloudsearch.stats.getIndex
View
API Only
GCP Search
cloudsearch.stats.index.datasources.get
View
API Only
GCP Search
cloudsearch.stats.getQuery
View
API Only
GCP Search
cloudsearch.stats.query.searchapplications.get
View
API Only
GCP Search
cloudsearch.stats.getSearchapplication
View
API Only
GCP Search
cloudsearch.stats.getSession
View
API Only
GCP Search
cloudsearch.stats.session.searchapplications.get
View
API Only
GCP Search
cloudsearch.stats.getUser
View
API Only
GCP Search
cloudsearch.stats.user.searchapplications.get
View
API Only
GCP Search
cloudsearch.operations.get
View
API Only
GCP Search
cloudsearch.operations.lro.list
View
API Only
GCP Search
cloudsearch.initializeCustomer
Create
API Only
GCP Binary Authorization
binaryauthorization.projects.attestors.validateAttestationOccurrence
Create
API Only
GCP Binary Authorization
binaryauthorization.projects.attestors.delete
Delete
API Only
GCP Binary Authorization
binaryauthorization.systempolicy.getPolicy
View
API Only
GCP Binary Authorization
binaryauthorization.projects.attestors.update
Edit
API Only
GCP Binary Authorization
binaryauthorization.projects.attestors.list
View
API Only
GCP Binary Authorization
binaryauthorization.projects.attestors.create
Create
API Only
GCP Binary Authorization
binaryauthorization.projects.policy.getIamPolicy
View
API Only
GCP Binary Authorization
binaryauthorization.projects.policy.setIamPolicy
Create
API Only
GCP Binary Authorization
binaryauthorization.projects.policy.testIamPermissions
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.checkDataAccess
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.evaluateUserConsents
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.queryAccessibleData
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.messages.delete
Delete
API Only
GCP Healthcare
healthcare.projects.locations.datasets.operations.get
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.messages.patch
Edit
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.update
Edit
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.Patient_everything
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.Resource_purge
Delete
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.history
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.capabilities
View
API Only
GCP Healthcare
healthcare.projects.locations.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.operations.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.activate
Activate
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.userDataMappings.archive
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.operations.cancel
Delete
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.deleteRevision
Delete
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.export
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.getFHIRStoreMetrics
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.import
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.listRevisions
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.reject
Reject
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.revoke
Delete
API Only
GCP Healthcare
healthcare.projects.locations.services.nlp.analyzeEntities
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.attributeDefinitions.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.attributeDefinitions.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consentArtifacts.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consentArtifacts.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.consents.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.dicomStores.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.dicomStores.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.dicomStores.studies.series.instances.delete
Delete
API Only
GCP Healthcare
healthcare.projects.locations.datasets.dicomStores.studies.series.instances.frames.retrieveRendered
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.dicomStores.studies.storeInstances
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.executeBundle
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.search
Search
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.search_type
Search
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.fhir.Resource_validate
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.messages.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.messages.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.messages.ingest
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.userDataMappings.list
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.consentStores.userDataMappings.create
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.getIamPolicy
View
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.setIamPolicy
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.hlVStores.testIamPermissions
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.deidentify
Create
API Only
GCP Healthcare
healthcare.projects.locations.datasets.fhirStores.deidentify
Create
API Only
GCP Data Fusion
datafusion.projects.locations.operations.delete
Delete
API Only
GCP Data Fusion
datafusion.projects.locations.operations.get
View
API Only
GCP Data Fusion
datafusion.projects.locations.instances.patch
Edit
API Only
GCP Data Fusion
datafusion.projects.locations.list
View
API Only
GCP Data Fusion
datafusion.projects.locations.operations.list
View
API Only
GCP Data Fusion
datafusion.projects.locations.operations.cancel
Delete
API Only
GCP Data Fusion
datafusion.projects.locations.instances.restart
Reboot
API Only
GCP Data Fusion
datafusion.projects.locations.instances.dnsPeerings.list
View
API Only
GCP Data Fusion
datafusion.projects.locations.instances.dnsPeerings.create
Create
API Only
GCP Data Fusion
datafusion.projects.locations.instances.list
View
API Only
GCP Data Fusion
datafusion.projects.locations.instances.create
Create
API Only
GCP Data Fusion
datafusion.projects.locations.versions.list
View
API Only
GCP Data Fusion
datafusion.projects.locations.instances.getIamPolicy
View
API Only
GCP Data Fusion
datafusion.projects.locations.instances.setIamPolicy
Create
API Only
GCP Data Fusion
datafusion.projects.locations.instances.testIamPermissions
Create
API Only
GCP Vault
vault.matters.list
View
API Only
GCP Vault
vault.matters.create
Create
API Only
GCP Vault
vault.matters.delete
Delete
API Only
GCP Vault
vault.matters.get
View
API Only
GCP Vault
vault.matters.update
Edit
API Only
GCP Vault
vault.matters.exports.list
View
API Only
GCP Vault
vault.matters.exports.create
Create
API Only
GCP Vault
vault.matters.exports.delete
Delete
API Only
GCP Vault
vault.matters.exports.get
View
API Only
GCP Vault
vault.matters.holds.list
View
API Only
GCP Vault
vault.matters.holds.create
Create
API Only
GCP Vault
vault.matters.holds.delete
Delete
API Only
GCP Vault
vault.matters.holds.get
View
API Only
GCP Vault
vault.matters.holds.update
Edit
API Only
GCP Vault
vault.matters.holds.accounts.list
View
API Only
GCP Vault
vault.matters.holds.accounts.create
Create
API Only
GCP Vault
vault.matters.holds.accounts.delete
Delete
API Only
GCP Vault
vault.matters.holds.addHeldAccounts
Create
API Only
GCP Vault
vault.matters.holds.removeHeldAccounts
Delete
API Only
GCP Vault
vault.matters.savedQueries.list
View
API Only
GCP Vault
vault.matters.savedQueries.create
Create
API Only
GCP Vault
vault.matters.savedQueries.delete
Delete
API Only
GCP Vault
vault.matters.savedQueries.get
View
API Only
GCP Vault
vault.matters.addPermissions
Create
API Only
GCP Vault
vault.matters.close
Create
API Only
GCP Vault
vault.matters.count
Create
API Only
GCP Vault
vault.matters.removePermissions
Delete
API Only
GCP Vault
vault.matters.reopen
Create
API Only
GCP Vault
vault.matters.undelete
Create
API Only
GCP Vault
vault.operations.delete
Delete
API Only
GCP Vault
vault.operations.list
View
API Only
GCP Vault
vault.operations.cancel
Delete
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.detachLun
Delete
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instanceProvisioningSettings.fetch
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.networks.listNetworkUsage
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.snapshots.delete
Delete
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.snapshots.get
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.patch
Edit
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.disableInteractiveSerialConsole
Edit
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.enableInteractiveSerialConsole
Enable
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.luns.evict
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.rename
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.reset
Edit
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.start
Start
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.stop
Stop
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.instances.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.luns.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.networks.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.nfsShares.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.nfsShares.create
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.provisioningConfigs.create
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.provisioningConfigs.submit
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.provisioningQuotas.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.snapshots.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.snapshots.create
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.sshKeys.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.sshKeys.create
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.list
View
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.snapshots.restoreVolumeSnapshot
Create
API Only
GCP Bare Metal Solution
baremetalsolution.projects.locations.volumes.resize
Edit
API Only
GCP Billing Budget
billingbudgets.billingAccounts.budgets.delete
Delete
API Only
GCP Billing Budget
billingbudgets.billingAccounts.budgets.get
View
API Only
GCP Billing Budget
billingbudgets.billingAccounts.budgets.patch
Edit
API Only
GCP Billing Budget
billingbudgets.billingAccounts.budgets.list
View
API Only
GCP Billing Budget
billingbudgets.billingAccounts.budgets.create
Create
API Only
GCP DNS
dns.projects.get
View
API Only
GCP DNS
dns.managedZones.list
View
API Only
GCP DNS
dns.managedZones.create
Create
API Only
GCP DNS
dns.managedZones.delete
Delete
API Only
GCP DNS
dns.managedZones.get
View
API Only
GCP DNS
dns.managedZones.patch
Edit
API Only
GCP DNS
dns.managedZones.update
Edit
API Only
GCP DNS
dns.changes.list
View
API Only
GCP DNS
dns.changes.create
Create
API Only
GCP DNS
dns.changes.get
View
API Only
GCP DNS
dns.dnsKeys.list
View
API Only
GCP DNS
dns.dnsKeys.get
View
API Only
GCP DNS
dns.managedZoneOperations.list
View
API Only
GCP DNS
dns.managedZoneOperations.get
View
API Only
GCP DNS
dns.resourceRecordSets.list
View
API Only
GCP DNS
dns.resourceRecordSets.create
Create
API Only
GCP DNS
dns.resourceRecordSets.delete
Delete
API Only
GCP DNS
dns.resourceRecordSets.get
View
API Only
GCP DNS
dns.resourceRecordSets.patch
Edit
API Only
GCP DNS
dns.policies.list
View
API Only
GCP DNS
dns.policies.create
Create
API Only
GCP DNS
dns.policies.delete
Delete
API Only
GCP DNS
dns.policies.get
View
API Only
GCP DNS
dns.policies.patch
Edit
API Only
GCP DNS
dns.policies.update
Edit
API Only
GCP DNS
dns.responsePolicies.list
View
API Only
GCP DNS
dns.responsePolicies.create
Create
API Only
GCP DNS
dns.responsePolicies.delete
Delete
API Only
GCP DNS
dns.responsePolicies.get
View
API Only
GCP DNS
dns.responsePolicies.patch
Edit
API Only
GCP DNS
dns.responsePolicies.update
Edit
API Only
GCP DNS
dns.responsePolicyRules.list
View
API Only
GCP DNS
dns.responsePolicyRules.create
Create
API Only
GCP DNS
dns.responsePolicyRules.delete
Delete
API Only
GCP DNS
dns.responsePolicyRules.get
View
API Only
GCP DNS
dns.responsePolicyRules.patch
Edit
API Only
GCP DNS
dns.responsePolicyRules.update
Edit
API Only
GCP DNS
dns.managedZones.getIamPolicy
View
API Only
GCP DNS
dns.managedZones.setIamPolicy
Create
API Only
GCP DNS
dns.managedZones.testIamPermissions
Create
API Only
GCP Filestore
file.projects.locations.operations.delete
Delete
API Only
GCP Filestore
file.projects.locations.operations.get
View
API Only
GCP Filestore
file.projects.locations.instances.snapshots.patch
Edit
API Only
GCP Filestore
file.projects.locations.list
View
API Only
GCP Filestore
file.projects.locations.operations.list
View
API Only
GCP Filestore
file.projects.locations.operations.cancel
Delete
API Only
GCP Filestore
file.projects.locations.instances.restore
Create
API Only
GCP Filestore
file.projects.locations.instances.revert
Create
API Only
GCP Filestore
file.projects.locations.backups.list
View
API Only
GCP Filestore
file.projects.locations.backups.create
Create
API Only
GCP Filestore
file.projects.locations.instances.list
View
API Only
GCP Filestore
file.projects.locations.instances.create
Create
API Only
GCP Filestore
file.projects.locations.instances.snapshots.list
View
API Only
GCP Filestore
file.projects.locations.instances.snapshots.create
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.packages.versions.delete
Delete
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.pythonPackages.get
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.packages.tags.patch
Edit
API Only
GCP Artifact Registry
artifactregistry.projects.locations.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.aptArtifacts.upload
Upload
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.aptArtifacts.import
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.dockerImages.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.files.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.googetArtifacts.upload
Upload
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.googetArtifacts.import
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.kfpArtifacts.upload
Upload
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.mavenArtifacts.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.npmPackages.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.packages.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.pythonPackages.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.create
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.packages.tags.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.packages.tags.create
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.packages.versions.list
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.yumArtifacts.upload
Upload
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.yumArtifacts.import
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.getIamPolicy
View
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.setIamPolicy
Create
API Only
GCP Artifact Registry
artifactregistry.projects.locations.repositories.testIamPermissions
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.backups.delete
Delete
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.metadataImports.get
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.metadataImports.patch
Edit
API Only
GCP Dataproc Metastore
metastore.projects.locations.list
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.operations.list
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.operations.cancel
Delete
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.backups.list
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.backups.create
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.federations.list
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.federations.create
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.metadataImports.list
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.metadataImports.create
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.list
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.create
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.backups.getIamPolicy
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.backups.setIamPolicy
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.testIamPermissions
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.alterLocation
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.exportMetadata
View
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.moveTableToDatabase
Move
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.queryMetadata
Create
API Only
GCP Dataproc Metastore
metastore.projects.locations.services.restore
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.delete
Delete
API Only
GCP Bigtable Admin
bigtableadmin.projects.locations.get
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.patch
Edit
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.update
Edit
API Only
GCP Bigtable Admin
bigtableadmin.projects.locations.list
View
API Only
GCP Bigtable Admin
bigtableadmin.operations.projects.operations.list
View
API Only
GCP Bigtable Admin
bigtableadmin.operations.cancel
Delete
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.checkConsistency
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.dropRowRange
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.generateConsistencyToken
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.modifyColumnFamilies
Edit
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.undelete
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.appProfiles.list
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.appProfiles.create
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.backups.list
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.backups.create
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.backups.copy
Copy
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.list
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.create
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.clusters.hotTablets.list
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.list
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.create
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.list
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.create
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.restore
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.getIamPolicy
View
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.setIamPolicy
Create
API Only
GCP Bigtable Admin
bigtableadmin.projects.instances.tables.testIamPermissions
Create
API Only
GCP Resource Manager
cloudresourcemanager.effectiveTags.list
View
API Only
GCP Resource Manager
cloudresourcemanager.folders.list
View
API Only
GCP Resource Manager
cloudresourcemanager.folders.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.folders.search
Search
API Only
GCP Resource Manager
cloudresourcemanager.liens.list
View
API Only
GCP Resource Manager
cloudresourcemanager.liens.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.organizations.search
Search
API Only
GCP Resource Manager
cloudresourcemanager.projects.list
View
API Only
GCP Resource Manager
cloudresourcemanager.projects.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.projects.search
Search
API Only
GCP Resource Manager
cloudresourcemanager.tagBindings.list
View
API Only
GCP Resource Manager
cloudresourcemanager.tagBindings.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.tagKeys.list
View
API Only
GCP Resource Manager
cloudresourcemanager.tagKeys.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.tagKeys.getNamespaced
View
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.list
View
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.getNamespaced
View
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.tagHolds.delete
Delete
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.get
View
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.patch
Edit
API Only
GCP Resource Manager
cloudresourcemanager.projects.move
Move
API Only
GCP Resource Manager
cloudresourcemanager.projects.undelete
Create
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.tagHolds.list
View
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.tagHolds.create
Create
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.getIamPolicy
View
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.setIamPolicy
Create
API Only
GCP Resource Manager
cloudresourcemanager.tagValues.testIamPermissions
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.disableMigration
Edit
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.domainJoinMachine
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.enableMigration
Enable
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.extendSchema
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.delete
Delete
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.get
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.patch
Edit
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.getLdapssettings
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.updateLdapssettings
Edit
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.list
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.attachTrust
Attach
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.operations.cancel
Delete
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.detachTrust
Delete
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.reconfigureTrust
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.resetAdminPassword
Edit
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.restore
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.validateTrust
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.backups.list
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.backups.create
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.list
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.create
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.list
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.create
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.domains.sqlIntegrations.list
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.getIamPolicy
View
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.setIamPolicy
Create
API Only
GCP Managed Service for Microsoft Active Directory
managedidentities.projects.locations.global.peerings.testIamPermissions
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.infoTypes.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.storedInfoTypes.delete
Delete
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.storedInfoTypes.get
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.storedInfoTypes.patch
Edit
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.jobTriggers.activate
Activate
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.dlpJobs.cancel
Delete
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.dlpJobs.finish
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.jobTriggers.hybridInspect
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.content.deidentify
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.content.inspect
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.content.reidentify
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.deidentifyTemplates.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.deidentifyTemplates.create
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.dlpJobs.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.dlpJobs.create
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.image.redact
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.locations.infoTypes.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.inspectTemplates.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.inspectTemplates.create
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.jobTriggers.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.locations.jobTriggers.create
Create
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.storedInfoTypes.list
View
API Only
GCP Data Loss Prevention (DLP)
dlp.projects.storedInfoTypes.create
Create
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.retrieveLegacySecretKey
View
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.delete
Delete
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.getMetrics
View
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.patch
Edit
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.assessments.annotate
Create
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.migrate
Create
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.assessments.create
Create
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.firewallpolicies.list
View
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.firewallpolicies.create
Create
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.list
View
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.keys.create
Create
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.relatedaccountgroups.memberships.list
View
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.relatedaccountgroups.list
View
API Only
GCP reCAPTCHA Enterprise
recaptchaenterprise.projects.relatedaccountgroupmemberships.search
Search
API Only
GCP Workflow Executions
workflowexecutions.projects.locations.workflows.executions.get
View
API Only
GCP Workflow Executions
workflowexecutions.projects.locations.workflows.executions.cancel
Delete
API Only
GCP Workflow Executions
workflowexecutions.projects.locations.workflows.executions.list
View
API Only
GCP Workflow Executions
workflowexecutions.projects.locations.workflows.executions.create
Create
API Only
GCP Workflow Executions
workflowexecutions.projects.locations.workflows.triggerPubsubExecution
Create
API Only
GCP Firebase Cloud Messaging Data
fcmdata.projects.androidApps.deliveryData.list
View
API Only
GCP Datastream
datastream.projects.locations.streams.delete
Delete
API Only
GCP Datastream
datastream.projects.locations.streams.objects.get
View
API Only
GCP Datastream
datastream.projects.locations.streams.patch
Edit
API Only
GCP Datastream
datastream.projects.locations.list
View
API Only
GCP Datastream
datastream.projects.locations.operations.list
View
API Only
GCP Datastream
datastream.projects.locations.operations.cancel
Delete
API Only
GCP Datastream
datastream.projects.locations.fetchStaticIps
View
API Only
GCP Datastream
datastream.projects.locations.streams.objects.startBackfillJob
Start
API Only
GCP Datastream
datastream.projects.locations.streams.objects.stopBackfillJob
Stop
API Only
GCP Datastream
datastream.projects.locations.connectionProfiles.list
View
API Only
GCP Datastream
datastream.projects.locations.connectionProfiles.create
Create
API Only
GCP Datastream
datastream.projects.locations.connectionProfiles.discover
Create
API Only
GCP Datastream
datastream.projects.locations.streams.objects.list
View
API Only
GCP Datastream
datastream.projects.locations.streams.objects.lookup
Create
API Only
GCP Datastream
datastream.projects.locations.privateConnections.list
View
API Only
GCP Datastream
datastream.projects.locations.privateConnections.create
Create
API Only
GCP Datastream
datastream.projects.locations.privateConnections.routes.list
View
API Only
GCP Datastream
datastream.projects.locations.privateConnections.routes.create
Create
API Only
GCP Datastream
datastream.projects.locations.streams.list
View
API Only
GCP Datastream
datastream.projects.locations.streams.create
Create
Yes
GCP Storage
storage.buckets.list
View
Yes
GCP Storage
storage.buckets.insert
Create
Yes
GCP Storage
storage.buckets.delete
Delete
Yes
GCP Storage
storage.buckets.get
View
Yes
GCP Storage
storage.buckets.patch
Edit
Yes
GCP Storage
storage.buckets.update
Edit
Yes
GCP Storage
storage.bucketAccessControls.list
View
Yes
GCP Storage
storage.bucketAccessControls.insert
Create
Yes
GCP Storage
storage.bucketAccessControls.delete
Delete
Yes
GCP Storage
storage.bucketAccessControls.get
View
Yes
GCP Storage
storage.bucketAccessControls.patch
Edit
Yes
GCP Storage
storage.bucketAccessControls.update
Edit
Yes
GCP Storage
storage.defaultObjectAccessControls.list
View
Yes
GCP Storage
storage.defaultObjectAccessControls.insert
Create
Yes
GCP Storage
storage.defaultObjectAccessControls.delete
Delete
Yes
GCP Storage
storage.defaultObjectAccessControls.get
View
Yes
GCP Storage
storage.defaultObjectAccessControls.patch
Edit
Yes
GCP Storage
storage.defaultObjectAccessControls.update
Edit
Yes
GCP Storage
storage.buckets.getIamPolicy
View
Yes
GCP Storage
storage.buckets.setIamPolicy
Create
Yes
GCP Storage
storage.buckets.testIamPermissions
View
Yes
GCP Storage
storage.buckets.lockRetentionPolicy
Create
Yes
GCP Storage
storage.notifications.list
View
Yes
GCP Storage
storage.notifications.insert
Create
Yes
GCP Storage
storage.notifications.delete
Delete
Yes
GCP Storage
storage.notifications.get
View
Yes
GCP Storage
storage.objects.list
View
Yes
GCP Storage
storage.objects.insert
Create
Yes
GCP Storage
storage.objects.watchAll
View
Yes
GCP Storage
storage.objects.delete
Delete
Yes
GCP Storage
storage.objects.get
View
Yes
GCP Storage
storage.objects.patch
Edit
Yes
GCP Storage
storage.objects.update
Edit
Yes
GCP Storage
storage.objectAccessControls.list
View
Yes
GCP Storage
storage.objectAccessControls.insert
Create
Yes
GCP Storage
storage.objectAccessControls.delete
Delete
Yes
GCP Storage
storage.objectAccessControls.get
View
Yes
GCP Storage
storage.objectAccessControls.patch
Edit
Yes
GCP Storage
storage.objectAccessControls.update
Edit
Yes
GCP Storage
storage.objects.getIamPolicy
View
Yes
GCP Storage
storage.objects.setIamPolicy
Create
Yes
GCP Storage
storage.objects.testIamPermissions
View
Yes
GCP Storage
storage.objects.compose
Create
Yes
GCP Storage
storage.objects.copy
Copy
Yes
GCP Storage
storage.objects.rewrite
Create
Yes
GCP Storage
storage.channels.stop
Stop
Yes
GCP Storage
storage.projects.hmacKeys.list
View
Yes
GCP Storage
storage.projects.hmacKeys.create
Create
Yes
GCP Storage
storage.projects.hmacKeys.delete
Delete
Yes
GCP Storage
storage.projects.hmacKeys.get
View
Yes
GCP Storage
storage.projects.hmacKeys.update
Edit
Yes
GCP Storage
storage.projects.serviceAccount.get
View
Yes
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.calculateCoverage
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.versions.compareVersions
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.deployFlow
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.runContinuousTest
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.securitySettings.delete
Delete
API Only
GCP Dialogflow
dialogflow.projects.operations.get
View
API Only
GCP Dialogflow
dialogflow.projects.locations.securitySettings.patch
Edit
API Only
GCP Dialogflow
dialogflow.projects.locations.list
View
API Only
GCP Dialogflow
dialogflow.projects.operations.list
View
API Only
GCP Dialogflow
dialogflow.projects.operations.cancel
Delete
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.export
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.versions.load
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.lookupEnvironmentHistory
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.restore
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.run
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.experiments.start
Start
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.experiments.stop
Stop
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.train
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.validate
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.changelogs.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.continuousTestResults.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.deployments.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.sessions.entityTypes.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.sessions.entityTypes.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.experiments.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.environments.experiments.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.import
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.intents.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.intents.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.pages.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.pages.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.results.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.securitySettings.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.securitySettings.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.Delete
Delete
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.Run
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.export
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.testCases.import
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.transitionRouteGroups.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.transitionRouteGroups.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.versions.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.flows.versions.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.webhooks.list
View
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.webhooks.create
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.sessions.detectIntent
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.sessions.fulfillIntent
Create
API Only
GCP Dialogflow
dialogflow.projects.locations.agents.sessions.matchIntent
Create
API Only
GCP Vision
vision.files.annotate
Create
API Only
GCP Vision
vision.files.asyncAnnotate
Create
API Only
GCP Vision
vision.images.annotate
Create
API Only
GCP Vision
vision.images.asyncAnnotate
Create
API Only
GCP Vision
vision.projects.locations.productSets.delete
Delete
API Only
GCP Vision
vision.projects.operations.get
View
API Only
GCP Vision
vision.projects.locations.productSets.patch
Edit
API Only
GCP Vision
vision.projects.locations.productSets.products.list
View
API Only
GCP Vision
vision.projects.locations.productSets.addProduct
Create
API Only
GCP Vision
vision.operations.cancel
Delete
API Only
GCP Vision
vision.projects.locations.productSets.removeProduct
Delete
API Only
GCP Vision
vision.projects.locations.files.annotate
Create
API Only
GCP Vision
vision.projects.locations.files.asyncAnnotate
Create
API Only
GCP Vision
vision.projects.locations.images.annotate
Create
API Only
GCP Vision
vision.projects.locations.images.asyncAnnotate
Create
API Only
GCP Vision
vision.projects.locations.productSets.list
View
API Only
GCP Vision
vision.projects.locations.productSets.create
Create
API Only
GCP Vision
vision.projects.locations.productSets.import
Create
API Only
GCP Vision
vision.projects.locations.products.list
View
API Only
GCP Vision
vision.projects.locations.products.create
Create
API Only
GCP Vision
vision.projects.locations.products.purge
Create
API Only
GCP Vision
vision.projects.locations.products.referenceImages.list
View
API Only
GCP Vision
vision.projects.locations.products.referenceImages.create
Create
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.delete
Delete
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.get
View
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.patch
Edit
API Only
GCP Talent Solution
jobs.projects.tenants.clientEvents.create
Create
API Only
GCP Talent Solution
jobs.projects.tenants.companies.list
View
API Only
GCP Talent Solution
jobs.projects.tenants.companies.create
Create
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.list
View
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.create
Create
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.Create
Create
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.Delete
Delete
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.Update
Edit
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.search
Search
API Only
GCP Talent Solution
jobs.projects.tenants.jobs.searchForAlert
Search
API Only
GCP Talent Solution
jobs.projects.tenants.list
View
API Only
GCP Talent Solution
jobs.projects.tenants.create
Create
API Only
GCP Talent Solution
jobs.projects.tenants.completeQuery
View
API Only
GCP Asset
cloudasset.savedQueries.delete
Delete
API Only
GCP Asset
cloudasset.savedQueries.get
View
API Only
GCP Asset
cloudasset.savedQueries.patch
Edit
API Only
GCP Asset
cloudasset.assets.list
View
API Only
GCP Asset
cloudasset.feeds.list
View
API Only
GCP Asset
cloudasset.feeds.create
Create
API Only
GCP Asset
cloudasset.savedQueries.list
View
API Only
GCP Asset
cloudasset.savedQueries.create
Create
API Only
GCP Asset
cloudasset.GetAssetsHistory
View
API Only
GCP Asset
cloudasset.exportAssets
View
API Only
GCP Asset
cloudasset.queryAssets
Create
API Only
GCP Asset
cloudasset.analyzeMove
View
API Only
GCP Asset
cloudasset.effectiveIamPolicies.Get
View
API Only
GCP Asset
cloudasset.analyzeIamPolicy
View
API Only
GCP Asset
cloudasset.analyzeIamPolicyLongrunning
Create
API Only
GCP Asset
cloudasset.analyzeOrgPolicies
View
API Only
GCP Asset
cloudasset.analyzeOrgPolicyGovernedAssets
View
API Only
GCP Asset
cloudasset.analyzeOrgPolicyGovernedContainers
View
API Only
GCP Asset
cloudasset.searchAllIamPolicies
Search
API Only
GCP Asset
cloudasset.searchAllResources
Search
API Only
GCP Firebase Dynamic Links
firebasedynamiclinks.installAttribution
Create
API Only
GCP Firebase Dynamic Links
firebasedynamiclinks.managedShortLinks.create
Create
API Only
GCP Firebase Dynamic Links
firebasedynamiclinks.reopenAttribution
Create
API Only
GCP Firebase Dynamic Links
firebasedynamiclinks.shortLinks.create
Create
API Only
GCP Firebase Dynamic Links
firebasedynamiclinks.getLinkStats
View
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.delete
Delete
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.get
View
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.patch
Edit
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.run
Create
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.stop
Stop
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.jobs.list
View
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.list
View
API Only
GCP Data pipelines
datapipelines.projects.locations.pipelines.create
Create
API Only
GCP Document AI
documentai.projects.locations.processors.humanReviewConfig.reviewDocument
Create
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.delete
Delete
API Only
GCP Document AI
documentai.projects.operations.get
View
API Only
GCP Document AI
documentai.projects.locations.list
View
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.Process
Create
API Only
GCP Document AI
documentai.projects.locations.operations.cancel
Delete
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.deploy
Create
API Only
GCP Document AI
documentai.projects.locations.processors.disable
Edit
API Only
GCP Document AI
documentai.projects.locations.processors.enable
Enable
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.process
Create
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.undeploy
Create
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.evaluations.list
View
API Only
GCP Document AI
documentai.projects.locations.processorTypes.list
View
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.list
View
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.train
Create
API Only
GCP Document AI
documentai.projects.locations.processors.list
View
API Only
GCP Document AI
documentai.projects.locations.processors.create
Create
API Only
GCP Document AI
documentai.projects.locations.fetchProcessorTypes
View
API Only
GCP Document AI
documentai.projects.locations.processors.processorVersions.evaluateProcessorVersion
Create
API Only
GCP Document AI
documentai.projects.locations.processors.setDefaultProcessorVersion
Create
API Only
GCP Translation
translate.projects.locations.datasets.exportData
View
API Only
GCP Translation
translate.projects.locations.datasets.importData
Create
API Only
GCP Translation
translate.projects.locations.operations.delete
Delete
API Only
GCP Translation
translate.projects.locations.operations.get
View
API Only
GCP Translation
translate.projects.locations.glossaries.glossaryEntries.patch
Edit
API Only
GCP Translation
translate.projects.locations.list
View
API Only
GCP Translation
translate.projects.locations.operations.list
View
API Only
GCP Translation
translate.projects.locations.operations.cancel
Delete
API Only
GCP Translation
translate.projects.locations.operations.wait
Create
API Only
GCP Translation
translate.projects.locations.datasets.list
View
API Only
GCP Translation
translate.projects.locations.datasets.create
Create
API Only
GCP Translation
translate.projects.locations.datasets.examples.list
View
API Only
GCP Translation
translate.projects.locations.glossaries.list
View
API Only
GCP Translation
translate.projects.locations.glossaries.create
Create
API Only
GCP Translation
translate.projects.locations.glossaries.glossaryEntries.list
View
API Only
GCP Translation
translate.projects.locations.glossaries.glossaryEntries.create
Create
API Only
GCP Translation
translate.projects.locations.models.list
View
API Only
GCP Translation
translate.projects.locations.models.create
Create
API Only
GCP Translation
translate.projects.locations.getSupportedLanguages
View
API Only
GCP Translation
translate.projects.locations.TranslateDocument
Create
API Only
GCP Translation
translate.projects.locations.TranslateText
Create
API Only
GCP Translation
translate.projects.locations.detectLanguage
Create
API Only
GCP Translation
translate.projects.locations.romanizeText
Create
API Only
GCP Translation
translate.projects.locations.translateDocument
Create
API Only
GCP Translation
translate.projects.locations.translateText
Create
API Only
GCP Redis
redis.projects.locations.operations.delete
Delete
API Only
GCP Redis
redis.projects.locations.operations.get
View
API Only
GCP Redis
redis.projects.locations.instances.patch
Edit
API Only
GCP Redis
redis.projects.locations.instances.getAuthString
View
API Only
GCP Redis
redis.projects.locations.list
View
API Only
GCP Redis
redis.projects.locations.operations.list
View
API Only
GCP Redis
redis.projects.locations.operations.cancel
Delete
API Only
GCP Redis
redis.projects.locations.instances.export
View
API Only
GCP Redis
redis.projects.locations.instances.failover
Create
API Only
GCP Redis
redis.projects.locations.instances.import
Create
API Only
GCP Redis
redis.projects.locations.instances.rescheduleMaintenance
Create
API Only
GCP Redis
redis.projects.locations.instances.upgrade
Create
API Only
GCP Redis
redis.projects.locations.instances.list
View
API Only
GCP Redis
redis.projects.locations.instances.create
Create
API Only
GCP Run Admin
run.projects.locations.services.revisions.delete
Delete
API Only
GCP Run Admin
run.projects.locations.services.revisions.get
View
API Only
GCP Run Admin
run.projects.locations.services.patch
Edit
API Only
GCP Run Admin
run.projects.locations.operations.list
View
API Only
GCP Run Admin
run.projects.locations.jobs.run
Create
API Only
GCP Run Admin
run.projects.locations.operations.wait
Create
API Only
GCP Run Admin
run.projects.locations.jobs.executions.list
View
API Only
GCP Run Admin
run.projects.locations.jobs.list
View
API Only
GCP Run Admin
run.projects.locations.jobs.create
Create
API Only
GCP Run Admin
run.projects.locations.services.revisions.list
View
API Only
GCP Run Admin
run.projects.locations.services.list
View
API Only
GCP Run Admin
run.projects.locations.services.create
Create
API Only
GCP Run Admin
run.projects.locations.jobs.executions.tasks.list
View
API Only
GCP Run Admin
run.projects.locations.services.getIamPolicy
View
API Only
GCP Run Admin
run.projects.locations.services.setIamPolicy
Create
API Only
GCP Run Admin
run.projects.locations.services.testIamPermissions
Create
API Only
GCP Workflows
workflows.projects.locations.workflows.delete
Delete
API Only
GCP Workflows
workflows.projects.locations.workflows.get
View
API Only
GCP Workflows
workflows.projects.locations.workflows.patch
Edit
API Only
GCP Workflows
workflows.projects.locations.list
View
API Only
GCP Workflows
workflows.projects.locations.operations.list
View
API Only
GCP Workflows
workflows.projects.locations.workflows.list
View
API Only
GCP Workflows
workflows.projects.locations.workflows.create
Create
API Only
In this Topic
Supported GCP Entities for Real-time Protection

---
## Configuring Real-time Protection Policies
**URL:** https://docs.netskope.com/en/configuring-real-time-protection-policies/
**Last Modified:** 2026-06-09T21:38:48+00:00
**Scraped:** 2026-06-25T09:21:40.297042+00:00

Configuring Real-time Protection Policies - Netskope Knowledge Portal
Configuring Real-time Protection Policies
With Real-time Protection (RTP), you can define policies with a wide range of variables to enforce access control or inspect traffic with DLP or Threat Protection. When creating an RTP policy, you can configure the traffic criteria (i.e., source and destination), the profile applied to the policy, and the action performed when the traffic criteria and policy are matched.
To create an RTP policy:
Go to
Policies
>
Real-time Protection
.
Click
New Policy
and then select the template that most resembles your goal for the policy. You can choose
DLP
,
Threat Protection
, or an access-control type policy template like
Cloud App Access
,
Web Access
, or P
rivate App Segment Access
.
The system will show the most appropriate criteria based on your policy template selection and some fields are auto-populated. However, you can edit any field as you work through the policy creation workflow, no matter the choice of template.
Note that many criteria are set as
Any
by default. This means the policy engine will not match against the criteria. When you see a text box during the policy workflow, click in the text box to view your additional options or to edit your selections. These options dynamically display based on your initial template choice.
Source
For
Source
, click
User
,
User Group
, or
Organizational Unit
to select the sources to include in the policy. Optionally, click
Unknown
to select
unauthenticated users
.
Tip
For users that are unknown or were not authenticated for any reason, create a policy specifically for “unknown” users and extend threat and DLP protection to unauthenticated users.
This applies to:
all GRE/IPSEC and CEP access methods
when SAML auth is not configured
unknown cookie surrogates traffic
For cookie surrogate traffic, Netskope can ingest and apply policies to unknown user traffic. Previously, unknown traffic was bypassed.
In addition, the SkopeIT Events user field displays “unknown” to reflect unknown traffic. If this feature is not enabled, the user field displays “IP Address”.
Contact Support to enable this feature in your account.
(Optional) Click
Exclusions
to select the sources to exclude from the policy. Keep in mind that if you choose to include a user in the policy, but exclude a user group that the user belongs to, then the user is excluded from the policy.
Click
Add Criteria
to add match criteria for the sources, including:
Source IP
: The IP address for the source.
Source IP (Egress)
: The egress IP address for the source.
Source Country
: The country from where queries originate.
OS
: The operating system type (e.g., Linux).
Note
The OS criterion will be deprecated and replaced with the OS Family Criteria. You must update any policies that use OS to use OS Family instead. To learn more:
OS Family Criteria
.
Browser
: The browser type (e.g., Chrome).
Access Method
: The access method type (e.g., Client).
Tip
When you create a Real-time Protection policy with Access Method defined for a domain that’s also part of an
SSL Do Not Decrypt policy
, Real-time Protection policy evaluation still takes place. If this Real-time Protection policy’s action is Block, then the domain will be blocked. As a workaround, Netskope recommends that you create a
custom category
for the domains in the SSL policy, and then create a Real-time Protection policy with Allow as the action for this custom category. Ensure to place this policy above the policy that blocks domains.
Device Classification
: The managed or unmanaged devices based on classifications created in
Device Classification
. This option is only applicable to the following access methods: Client, Enterprise Browser, Mobile Profile, Reverse Proxy.
HTTP Header
: The
HTTP header profile
.
Custom Attribute
: The custom user attributes from the Active Directory (AD) if user information was synced.
Note
The Custom Attribute option is a Beta feature. Contact Netskope Support or your sales representative to enable this feature.
Destination
For
Destination
, select one of the following traffic types for the policy:
Cloud App
: If selected, you can choose individual cloud apps (e.g., Dropbox) or
cloud app suites
(e.g., AWS).
Category
: If selected, you can choose between
predefined
or
custom categories
.
App Instance
: If selected, you can choose app instances. Multiple SaaS app instances can exist at the same time (e.g., a corporate app instance versus a personal app instance). Existing app instance labels appear in this list. To learn more:
App Instance Profile
.
Service
: If selected, you can choose
service profiles
.
Destination Profile
: If selected, you can choose
destination profiles
.
Private App Segment
: If selected, you can choose private app segments.
Email Outbound App
: For matching against
MPIP Sensitivity Labels
, an Email Outbound instance and the Associated Activity, Send, must be selected.
Any Web Traffic
: If selected, the policy is applied to all web traffic. You can create “Any Web Traffic” policies without source criteria. If you create an “Any Web Traffic” policy without a profile, selecting an Activity is not required.
Note
When creating an “Any Web Traffic” policy for Threat Protection, you must choose at least one Activity for the policy. Additionally, only the Upload and Download activities are supported for Threat Protection.
(Optional) Select activities and constraints. After selecting an app, you can further narrow your policy by selecting specific activities and constraints. The
Activities
list is the union of activities supported by the app or categories you select. It’s possible not all activities are supported by all of your selected apps, categories, and object types.
Note
As part of file activity, a user can add a comment to a file in Microsoft Office 365 OneDrive. In OneDrive account, hover over a file and click
See details
>
Activity
. In Netskope, this activity translates to a post. Microsoft allows commenting for non-Microsoft Office file types only like .zip, .pdf, .txt, .png, .pem, and more. Netskope reports post activity for such file types. However, Microsoft does not allow commenting for .docx, xlsx, and .pptx file types. Due to this limitation from Microsoft, Netskope does not report post activity for such file types.
Click the
Activities icon >
View activity support
link to open the Activity Support dialog.
This dialog shows the app or category you’ve selected and the available activities. This is informational only.
Tip
Admins can configure a policy with a combination of different Activity Constraints. Contact Support to enable this feature in your account. To learn more:
File Type Detection
Click
Add Criteria & Constraints
to add more match criteria for the destinations. The criteria and constraints you can configure depends on the traffic type you selected.
Activity Constraints
: What users are allowed to do for a specified activity (e.g., allowing sharing only within the organization). Constraints are shown only for the activities that support each constraint. You can define constraint profiles in
Policies
>
Constraint
. To learn more:
Constraint Profile
.
File Constraints
: Specify the
File Name or Extension
,
File Type
, and
File Size
.
CCI App Tag
: This option is only applicable if
Any Web Traffic
or
Category
is selected.
App Instance Tag
: This option is only applicable if
Any Web Traffic
,
Category
, or
Cloud App
is selected. There are two predefined app instance tags: Sanctioned and Unsanctioned. The Untagged option matches app instances that Netskope identified but are not yet tagged.
Service
: For matching against specific TCP ports or ranges. To learn more:
Service Profile
.
Destination Profile
: Specify the
destination profile
.
CCL
: This option is only applicable when
Category
is selected. A CCI Level can be applied when certain app categories, like Application Suite, are chosen. CCI measures the enterprise readiness of the cloud apps taking into consideration their security, auditability, and business continuity. Each app is assigned a score of 0-100, and based on the score, placed into one of five cloud confidence levels: Excellent, High, Medium, Low, or Poor. CCI can be used as a matching criteria in the policy. For example, you can choose to not let users share content in cloud storage apps rated Medium or below.
Destination Country
: The country where queries are sent.
Profile & Action
To perform additional content inspection on the traffic, add a profile. The action you specify in this step is performed when the traffic criteria and profile are both matched.
For
Profile & Action
, select the
Action
taken when a violation is detected. Select the action you would like to take such as Alert, Block, Quarantine, Forward to Proxy, and so on. Some actions allow you to choose a default template for the notification sent to the user when the policy detects a violation.
Note
Netskope matches a Real-time Protection policy with an
SSL Do Not Decrypt
policy when the Real-time Protection policy’s Action is Block, User Alert, Allow, or Alert.
Contact your sales team to enable policy matching when the Real-time Protection policy’s Action is Alert.
Alert
: Inspects the session and performs deep analytics but no action is taken. It will generate an alert under the Alert tab. The alert action allows the traffic.
Tip
Alert events are not generated for Real-time Protection Policies with the “Alert” action selected for “Browse” activity.
Allow
: All activities will be permitted on managed devices.
Block
: Blocks the specified app session if all criteria are matched. For example, if the policy is configured to block only a download activity for cloud storage, only the download will be blocked. All other activities will be permitted. You can specify a default block page or a custom block page to be displayed when a block action is taken.
Block Template
options include the following but you may see other templates in your set up that are unique to your account:
Default Template
: Default template for Block and User Alert which is available when the account is set up.
No Notification (Mute)
: No notifications are displayed when this option is selected. Additionally, this option is available for all categories, apps, and instances.
Block Template with URL
: URL the user is redirected to automatically or after clicking the Stop Button. Admins can add this URL while designing the template. In addition, admins can add variable tags for the redirect URL(s).
Block with Justification Box
: Justification box option provides a text box within the notification window where the user can enter a justification message.
Block with UA Action
: User Alert action is configured with an option the user selects to “Proceed” or “Block” the activity.
Tip
Except the Default Template and No Notification (Mute) options noted above, all other other templates are created and maintained by account admins.
Idle Timeout:
Enter the amount of minutes to trigger a session timeout.
Bypass
: Bypasses the detection when the criteria are matched. For example, if you want to bypass all activities from being detected except for login and logout, then choose all the activities except Login Successful and Logout, and then set the action as Bypass.
Redirect
: Automatically redirect users to a specific URL using HTTP 307 headers. Note that this action is only applicable to native HTTP or decrypted HTTPS traffic. Non-decrypted traffic will skip the redirect and move to the next policy. In addition, Redirect is unavailable for DLP Content Inspection, Threat Protection, File Type Detection, and Activity Constraints. You can enter an exact URL (e.g., netskope.com) or a URL with variables from the Insert Variable menu (e.g., http://netskope.com/{{x-cs-uri-path}}/{{cs-uri-query}). A maximum of 1,024 characters, including variables, is supported before variable substitution. After substitution, the URL is truncated at 8,192 characters.
User Alert
: When a user alert action is chosen, you can specify a default user alert page or custom page to be displayed to the user as defined in the policy. The user justification page for a user alert action will have Proceed and Stop Action buttons. The Proceed button will allow the activity and generates an activity event with the user’s justification reason, whereas the Stop Action just blocks the activity. The user’s justification reason for the activity is cached for 30 minutes.
Quarantine
: If a user uploads a document that has a DLP violation, you can quarantine the file, which moves the file to a quarantine folder for you to review and take appropriate action. You can then choose to allow the file to be uploaded or block the file from being uploaded. This option is available only when DLP is included in a policy. Also the action can be taken only for the upload activity.
Encryption
: You can encrypt files in the named instances of cloud apps that are sanctioned if it matches certain policy criteria. Encryption is available only when an app instance of a cloud app is chosen. To learn how to create an app instance, refer to
App Instance Profile
. The encryption action can be applied to an upload activity. If any other activity is chosen, like download, encryption will not show under the list of actions.
(Optional) If you select
Block
as the action, you can also choose to suppress alerts with the
Don’t Generate Alerts
option. When an alert is suppressed, application or page events are still generated.
Note
Netskope appliance versions 128.0.0 and older don’t support the Don’t Generate Alerts option. If this option is selected while using an older version of Netskope appliances, alerts will not be suppressed. In addition, using this option with firewall policies is not supported.
Click
Add Profile
to add a
DLP Profile
or
Threat Protection Profile
to the policy for additional content inspection.
A
DLP profile
detects violations like PCI (which identifies credit card information). You can configure DLP profiles and rules in
Policies
>
DLP
.
A
threat protection
profile detects malware files and malicious sites. You can configure threat protection profiles in
Settings
>
Threat Protection
.
(Optional) If you’re configuring a Threat Protection policy and chose a
Block
action, you can see the
Block till benign verdict by dynamic threat analysis
option. Select to block users from uploading or downloading a file until Netskope dynamic threat analysis provides a benign verdict. The analysis can take up to 10 minutes. To learn more:
Creating a Threat Protection Policy for Patient Zero
.
(Optional) You may see the
Set action for each profile
checkbox. This option is visible based on your initial template selection. This is an optional feature to help you consolidate policies. If you have multiple DLP profiles in one policy, you can set an action for each profile.
(Optional) The
Continue policy evaluation after match
checkbox is available if you selected
Alert
as the action for one or more DLP profiles. When this option is enabled, the
Add Traffic Action
option is unavailable. Note that this Alert and Continue functionality is also supported for Email DLP.
This feature allows the Netskope cloud to continue evaluating your policies after a policy match and detect additional DLP violations, instead of ending the evaluation after a match. If your policy includes multiple DLP profiles, this only applies to the profiles with the Alert action configured. When a match occurs for a profile with an action other than Alert, Netskope stops processing your policies.
Note
When the Continue policy evaluation after match option is enabled and multiple policy matches occur, the
generated DLP incident
lists all matched policies and DLP profiles. The
generated alert
for the transaction uses the last matched policy as the Alert Name and lists all matched policies in the Policy Name field. The Action is the last matched policy’s configured action. If all matched policies’ actions are Alert (and Continue policy evaluation after match), then the Action is listed as None.
(Optional) The
Add Traffic
Action
option allows you to consolidate a DLP policy and an access control (Cloud App Access, Web Access, or Private App Segment Access) policy that have the same traffic criteria. When the traffic criteria matches but the DLP profile does not, the traffic action will be taken.
Policy Name
Enter a policy name.
Important
When creating policy names, only use alphanumeric characters and symbols such as underscores (
_
), dashes (
-
), and square brackets (
[]
). You cannot use the greater than (
>
) and less than (
<
) symbols in policy names.
Select a
Group
for the policy.
(Optional) Click
Policy Description
to enter a description.
Configure the
Email Notification
:
Note
When multiple events (i.e., policy matches) occur within one minute, only one email notification is sent. The email notification will contain information for all the events that occurred in that minute.
Select the notification frequency.
Select who will receive the email notifications. You can choose to send notifications to users or admins. The
Imported Custom Attribute
option allows you to send notifications based on user information synced from the Active Directory. Note that the imported custom attribute must contain the email address value, and not a directory pointer or another user’s directory ID. The
Selected Users
option allows you to add the email addresses for specific users you want to notify.
(Optional) Enter an email address that will appear as the sender in the email notification.
Once finished, click
Done
to save your email notification setting and exit the window.
Status
Click to
Enable
the policy.
(Optional) Click
Policy Schedule
to enable a time-based policy schedule. To learn more:
Time Based Policies
. If you do not see this option, contact Support to enable it in your account.
If a policy schedule is configured, you will see a clock
icon beside the policy name in the list of policies on the Real-time Protection page. If a time range has expired, you will see a grayed out
clock icon and policy name. The policy is still enabled but it requires your attention. In both cases, you can hover over the clock icon for details.
Click
Save
in the upper right corner to save your new policy.
Related Topics
Unknown Users
Inline App Connectors
Cloud App Suite Membership
File Type Detection
OS Family Criteria
API-enriched Real-time Controls for Slack Enterprise
Enforcing DLP and TSS Policies on E2E Encrypted Apps
In this Topic
Configuring Real-time Protection Policies

---
## Real-time Protection for IaaS
**URL:** https://docs.netskope.com/en/real-time-protection-for-iaas/
**Last Modified:** 2025-08-31T01:50:20+00:00
**Scraped:** 2026-06-25T09:21:42.581506+00:00

Real-time Protection for IaaS - Netskope Knowledge Portal
Real-time Protection for IaaS
You can define granular
Real-time Protection policies
to monitor API and browser traffic to sanctioned and unsanctioned accounts.
For AWS, you can include all supported AWS services in a single Real-time Protection policy with the Cloud App Suite grouping feature. Real-time Protection leverages Netskope’s Cloud Security Posture Management (CSPM) capabilities to synchronize AWS account IDs as app instances of the “Amazon Web Services Console” app, which covers the AWS Console Login. When the policies are applied, Netskope refers to these account IDs to identify the destination of traffic. To learn more about supported AWS services, see:
Supported AWS Entities for Real-time Protection
.
For GCP, the Cloud App Suite feature and CSPM-based synchronization are unsupported. The Instance ID mapping for GCP traffic is the project ID. In cases where API calls don’t have project IDs in the traffic transaction, the instance ID is mapped to the user domain or service account email. To learn more about supported GCP services, see
Supported GCP Entities for Real-time Protection
.
Rest APIs for adding app instances programmatically are available. To learn more, see
Add an App Instance
.
To create a Real-time Protection policy for IaaS:
In the Netskope tenant, navigate to
Policies
>
Real-time Protection
.
Click
New Policy
and select
Cloud App Access
.
On the
Real-time Protection Policy
page, select the
Source
from the list of users, user groups, organizational units, or unknown users.
For
Destination
:
To apply this policy to all AWS or GCP services, select
Cloud App
and click
AWS
or
GCP
to select individual apps for granular match. For AWS, you can also select
Amazon Web Services
under
Cloud App Suite
to select all AWS apps as a group.
To create a policy to control console logins for your AWS accounts onboarded through CSPM, select
App Instance
and then select
All Amazon Web Services
to include all the existing and future AWS instances. Alternatively, select specific instances under
Amazon Web Services
.
To create a policy when not using CSPM for AWS, you must create an app instance
using REST API
, and then select the instances under
App Instances
>
App
.
In the previous step, if you selected
Cloud App
and
Amazon Web Services
suite or individual AWS or GCP cloud apps, you can apply additional criteria (e.g., App Instance Tag)
using REST API
.
Under
Profile & Action
, you can select multiple DLP profiles and set an action for each profile.
Provide a policy name, set the status as
Enabled
, and set the policy schedule.
Click
Save
.
In this Topic
Real-time Protection for IaaS

---
## Real-time Protection Policies for MCP Security
**URL:** https://docs.netskope.com/en/real-time-protection-policies-for-mcp-security/
**Last Modified:** 2026-06-11T19:08:31+00:00
**Scraped:** 2026-06-25T09:37:34.736181+00:00

Real-time Protection Policies for MCP Security - Netskope Knowledge Portal
Real-time Protection Policies for MCP Security
Contact your Netskope account team to enable Agentic Broker in your account. Additional licensing is required for Agentic Broker and DLP. Note, to create a DLP policy, the DLP add-on license is required if you do not have DLP enabled in your account.
You can now create sophisticated Real-time Protection (RTP) Policies specifically for MCP traffic to allow, alert, or block communications based on predefined criteria.
HTTP Header based policy
To create policies based on fields in HTTP headers such as mcp-session-id and mcp-protocol-version
Policy Destinations:
MCP servers are now a dedicated destination category in the “App” dropdown menu. You can select:
Remote/GitHub Servers:
Remote MCP Servers or Servers available in code repositories that have not yet been deployed. You can create real-time policies for specific remote MCP Servers.
Flexible Policy Creation:
Event based policies:
Select an MCP server and one or more events to create a policy or select an “MCP Server” category and one or more events to create a policy.
Data Loss Prevention (DLP):
You can apply content inspection to specific MCP activities to prevent sensitive data leakage. This involves selecting the relevant MCP activity and adding the necessary DLP policy action (e.g., PII).
Notes:
In the RTP Policy page, the Threat Protection Profile is currently not supported for securing MCP communications in the Agentic Broker.
When creating an RTP policy for an MCP Server, if the destination is selected as an “Application,” select only the MCP Server you want to create the policy for. Do not add other applications or cloud app suites in the same policy.
When creating an RTP policy for the MCP Category, if the destination is selected as “Category,”  select only the MCP Server category and do not include any other categories in the same policy.
To learn more:
Configuring HTTP Header-Based Policies
Configuring RTP Policies to Block Events
Granular Control and Data Loss Prevention (DLP)
Granular Access Control to Block a Specific MCP Server
Broad Access Control to Block all MCP Traffic with RTP
In this Topic
Real-time Protection Policies for MCP Security

---
## Creating an AI Guardrails Policy for Real-time Protection
**URL:** https://docs.netskope.com/en/creating-an-ai-security-guardrails-policy-for-real-time-protection/
**Last Modified:** 2026-05-07T16:02:42+00:00
**Scraped:** 2026-06-25T09:38:54.855139+00:00

Creating an AI Guardrails Policy for Real-time Protection - Netskope Knowledge Portal
Creating an AI Guardrails Policy for Real-time Protection
After creating an
AI guardrails profile
to regulate and control the use of generative AI apps across your organization so users are using them securely and responsibly, you must then add it to a Real-time Protection policy so you can apply the policy to the users across your organization.
You can also configure scanning limits and fallback action via API in case the limit exceeded or AI Security is down.
To create an AI Guardrails policy for Real-time Protection:
Go to
Policies
>
Real-time Protection
.
Click
New Policy
and then
AI Guardrails
.
On the
Real-time Protection
Policy
page:
Source
: Select the users, user groups, or organizational units you want to apply the AI guardrails policy to. Click
Add Criteria
to add other sources.
Destination
: Select the traffic destination you want to apply the AI guardrails policy to.
Category
: Choose Cloud App, and select from the following
Gen AI apps
.
Activities
: Select the activities you want to moderate.
Post
: A question/prompt that a user posts to a standalone AI application, which is any standalone gen AI app that can be accessed independently (e.g., ChatGPT, Google Gemini).
Response
: An answer/response to the user’s question/prompt from the standalone AI application.
AI Post
: A question/prompt that a user posts to an embedded AI assistant, which is any gen AI assistant embedded within a SaaS app (e.g., Copilot within Microsoft Word).
AI Response
: An answer/response to the user’s question/prompt from the embedded AI assistant.
Some activities aren’t available for certain apps.
Profile & Action
: Configure the following.
AI Guardrails
: Choose the
AI guardrails profiles
you want to add to the Real-time Protection policy. You can add multiple profiles to a Real-time Protection policy.
Profile Action
: Select the action you want Netskope to take when users trigger the policy.
Alert
Allow
Block
User Alert
If you select
Block
or
User Alert
, you can also choose a default or custom notification template to send to the end user if Netskope detects a policy violation for user coaching.
Optionally, you can click
Set action for each profile
to help you consolidate the profiles within your policy. For example, if you have multiple AI guardrails profiles in this policy, you can set an action for each profile. If multiple matching profiles have a different action within a single policy, Netskope takes the one with the most restrictive action.
Policy Name
: Enter a policy name. You can only use alphanumeric characters and symbols such as underscore (_), dash (-), and square brackets ([ ]). You cannot use the greater-than (>) or less-than (<) symbols in policy names.
+ Policy Description
: Click to add notes or information.
+ Email Notification
: Netskope doesn’t send email-based notifications for AI guardrail events.
Status
: Ensure it’s
Enabled
so the policy is active.
Click
Save
.
In the
Move Policy
window, move the AI guardrails policy based on your interpretation of the severity of the content moderation.
Click
Save
.
Click
Apply Changes
.
After creating an AI guardrails policy, you can view the matched policy alerts and events in Skope IT. To learn more:
Viewing AI Guardrails Alerts
.
In this Topic
Creating an AI Guardrails Policy for Real-time Protection

---
## Netskope Secure Web Gateway
**URL:** https://docs.netskope.com/en/netskope-secure-web-gateway/
**Last Modified:** 2025-08-31T06:20:00+00:00
**Scraped:** 2026-06-25T09:41:52.868130+00:00

Netskope Secure Web Gateway
Netskope Secure Web Gateway  provides next generation secure web gateway (NG SWG) capabilities to prevent malware, detect advanced threats, filter websites by category, protect data, enable remote browser isolation, and control apps and cloud services for any user, location, or device. Single-pass inline proxy is unmatched for its ability to decode cloud and web traffic including instance and activity.
About Netskope Secure Web Gateway
Choose a Traffic Steering Method
Create Custom Categories
Create a Real-time Protection Policy for Web Categories
Security Cloud Platform Configuration
Web Usage Summary
Addressing SSL Error while Accessing AWS Services via the AWS CLI with the Netskope Client Enabled
Netskope Root Certificate Rotation Guide
Netskope Tenant Certificate Rotation Guide
About Predefined Categories
In this Topic
Netskope Secure Web Gateway

---
## Real-time Protection
**URL:** https://docs.netskope.com/en/real-time-protection/
**Last Modified:** 2026-01-06T21:31:53+00:00
**Scraped:** 2026-06-25T09:41:56.266923+00:00

Real-time Protection - Netskope Knowledge Portal
Real-time Protection
Real-time Protection allows you to enforce granular access control (like block) based on the cloud apps, cloud app categories, website categories, users and groups, app activity, and so on in a policy. In addition to this, you can also define data loss prevention (DLP) and threat protection profiles to inspect traffic to prevent sensitive and critical data leaks and exposure. Real-time Protection policies also provide broad, risk-based access control for websites and malware and malicious sites protection.
Best Practices for Real-time Protection Policies
Configuring Real-time Protection Policies
Insider Threats & Advanced Compromise Policies
Real-time Protection for Public Cloud
Time Based Policies
Best Practices for User Alert Policies
SSL Decryption
Policy Notification Templates
Profiles
Migrating URL Lists to Destination Profiles
In this Topic
Real-time Protection
