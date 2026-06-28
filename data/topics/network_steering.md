# Netskope Docs — Network Steering
_Generated: 2026-06-28 09:51 UTC_
_Pages: 43_

---
## Apply policies based on the source of traffic, forward, or reverse proxy
**URL:** https://docs.netskope.com/en/apply-policies-based-on-the-source-of-traffic-forward-or-reverse-proxy/
**Last Modified:** 2025-12-11T04:03:12+00:00
**Scraped:** 2026-06-28T08:47:18.798270+00:00

Apply policies based on the source of traffic, forward, or reverse proxy - Netskope Knowledge Portal
Apply policies based on the source of traffic, forward, or reverse proxy
To apply inline policies based on security needs and various constraints such as AD/user groups/Organizational unit, Source of traffic/Trusted or untrusted, networks/Forward or reverse proxy, Application instance, Constraint profile or augmenting authentication (Multifactor authentication),  follow the steps as shown below:
Navigate to
Policies
>
Real time Protection
>
New Policy
>
Cloud App access
.
Under ‘Source’ section, select Users/User groups or Organizational Unit. Options selected here will apply in the policy being created.
Under ‘Source’ section, select ‘
ADD CRITERIA
’ drop down option.
Select the ‘
Access method
’ option and select the required source of traffic and proxy type (forward, reverse).
For trusted or untrusted networks, select ‘Source IP’ and provide the details.
To apply policies based on application  instance, navigate to ‘Destination’ section of the policy creation template, and select the ‘
App Instance
’ option.
Selection of a cloud app or an app instance activates the ‘Activities and Constraints’ section where activities that have to act as constraints can be placed in the policy.
To include multi factor authentication in policies, ensure that Multifactor authentication is enabled for the tenant.
Under the Profiles & Action section in the policy creation template, select the Action = Multifactor authentication. This will help to provide layered security for higher risk activity.
To learn more:
Real-time Protection Policies
In this Topic
Apply policies based on the source of traffic, forward, or reverse proxy

---
## Apply policies based on the source of traffic
**URL:** https://docs.netskope.com/en/apply-policies-based-on-the-source-of-traffic/
**Last Modified:** 2025-09-01T13:08:32+00:00
**Scraped:** 2026-06-28T08:47:21.029842+00:00

Apply policies based on the source of traffic - Netskope Knowledge Portal
Apply policies based on the source of traffic
To apply inline policies based on security needs and various constraints such as AD/user groups/Organizational unit, Source of traffic/Trusted or untrusted, networks/Forward or reverse proxy, Application instance, Constraint profile or augmenting authentication (Multifactor authentication),  follow the steps as shown below:
Navigate to
Policies
>
Real time Protection
>
New Policy
>
Cloud App access
.
Under ‘Source’ section, select Users/User groups or Organizational Unit. Options selected here will apply in the policy being created.
Under ‘Source’ section, select ‘
ADD CRITERIA
’ drop down option.
Select the ‘
Access method
’ option and select the required source of traffic and proxy type (forward, reverse).
For trusted or untrusted networks, select ‘Source IP’ and provide the details.
To apply policies based on application  instance, navigate to ‘Destination’ section of the policy creation template, and select the ‘
App Instance
’ option.
Selection of a cloud app or an app instance activates the ‘Activities and Constraints’ section where activities that have to act as constraints can be placed in the policy.
To include multi factor authentication in policies, ensure that Multifactor authentication is enabled for the tenant.
Under the Profiles & Action section in the policy creation template, select the Action = Multifactor authentication. This will help to provide layered security for higher risk activity.
To learn more:
Real-time Protection Policies
In this Topic
Apply policies based on the source of traffic

---
## Apply policies based on the source of traffic, trusted, or untrusted networks
**URL:** https://docs.netskope.com/en/apply-policies-based-on-the-source-of-traffic-trusted-or-untrusted-networks/
**Last Modified:** 2025-09-01T13:08:34+00:00
**Scraped:** 2026-06-28T08:47:23.241583+00:00

Apply policies based on the source of traffic, trusted, or untrusted networks - Netskope Knowledge Portal
Apply policies based on the source of traffic, trusted, or untrusted networks
To apply inline policies based on security needs and various constraints such as AD/user groups/Organizational unit, Source of traffic/Trusted or untrusted, networks/Forward or reverse proxy, Application instance, Constraint profile or augmenting authentication (Multifactor authentication),  follow the steps as shown below:
Navigate to
Policies
>
Real time Protection
>
New Policy
>
Cloud App access
.
Under ‘Source’ section, select Users/User groups or Organizational Unit. Options selected here will apply in the policy being created.
Under ‘Source’ section, select ‘
ADD CRITERIA
’ drop down option.
Select the ‘
Access method
’ option and select the required source of traffic and proxy type (forward, reverse).
For trusted or untrusted networks, select ‘Source IP’ and provide the details.
To apply policies based on application  instance, navigate to ‘Destination’ section of the policy creation template, and select the ‘
App Instance
’ option.
Selection of a cloud app or an app instance activates the ‘Activities and Constraints’ section where activities that have to act as constraints can be placed in the policy.
To include multi factor authentication in policies, ensure that Multifactor authentication is enabled for the tenant.
Under the Profiles & Action section in the policy creation template, select the Action = Multifactor authentication. This will help to provide layered security for higher risk activity.
To learn more:
Real-time Protection Policies
In this Topic
Apply policies based on the source of traffic, trusted, or untrusted networks

---
## Configure a Steering Profile
**URL:** https://docs.netskope.com/en/configure-a-steering-profile/
**Last Modified:** 2026-01-30T20:41:32+00:00
**Scraped:** 2026-06-28T08:47:38.756865+00:00

Configure a Steering Profile
A Steering Profile tells the Netskope Client
what
traffic it needs to capture and send towards Netskope, and what traffic it needs to bypass and let through directly.
Steering Profiles can be global (applied for all users) or targeted to specific user groups. The latter can be useful for testing, or for use with specific groups of users that may require more granular configuration ( like developers).
Every Netskope tenant has a
default steering configuration
that is used as a fallback should no other Steering Profiles be present or matched on. You can simply continue to use the default steering profile if you wish (with a few small tweaks), or create your own from scratch.
To start, go to
Settings > Security Cloud Platform > Steering Configuration
Note
On the Steering Configuration page, change the Bypassed Traffic setting to
Log
. This ensures that you retain visibility on traffic that is not sent to Netskope for inspection.
The Steering Configuration page is where you manage what traffic should be sent to Netskope for inspection.
Create or Edit a Steering Profile
Using the Existing Default Configuration
If you wish to leverage the existing default steering profile, click the
Default tenant config profile
to edit its configuration, and then click
Edit
.
To edit the settings of the default steering configuration, select the profile and click
Edit
at the top-right.
Create a New Steering Configuration
You may want to create a separate profile and target your IT team (or the team will be managing the Netskope platform) as a way of testing traffic steering changes in isolation before pushing them to the rest of your organization.
To create a new profile, click
New Configuration
, and if prompted, select
User Group
. Configure the new steering profile by giving it a name (like
Testing
), and assigning a user group.
The User Group field is a list of Active Directory/Security Groups that have been synchronized from the identity provider.
Configure the Steering Profile
Select the type of traffic that you would like the Netskope Client to capture and and send to the Netskope Cloud.
Depending on your subscription, some options may not be visible to you:
Cloud Apps Only
: Steer only selected applications to Netskope for deep analysis. You can make exceptions and allow special accommodations for custom applications. If you are a Cloud Inline or CASB-only customer, you should select this option.
Web Traffic
: Steer all
web
traffic (HTTP and HTTPS) to Netskope for deep analysis. You can make exceptions for traffic that have personal or private content. Most organizations should select this option.
All Traffic
: Steer
all
traffic (web and non-web) to Netskope for deep analysis. You can make exceptions for traffic that have personal or private content. If you are subscribed to Cloud Firewall, you should select this option.
If you subscribed to Netskope Private Access (NPA), select All or Specific Private App Segments from the dropdown, and then ensure that the
Steer
option is selected.
Change the Status to
Enabled
and click
Save
.
Note
You can click the Non-Standard Ports tab to specify ports other than 80 and 443 to be forwarded to the Netskope proxy.
The Dynamic Steering setting can be used to change the way traffic is forwarded by the Netskope Client based on whether the user is working from within the company network, or remotely.
If you selected the Cloud-Apps Only option above, then you now need to specify the cloud applications (like Dropbox, Teams, Sharepoint, etc) that the Netskope Client should intercept and send to Netskope.
Click
Add Steered Item
, and specify the applications required.
Bypassing Traffic
Traffic can also be explicitly bypassed from being sent to Netskope entirely under the
Exceptions
tab of the steering profile. RFC1918 traffic (
10.0.0.0/8
,
172.16.0.0/12
,
192.168.0.0/16
) is always bypassed from Netskope by default, and Netskope also maintains a list of applications that usually need to be bypassed (typically due to certificate-pinning) like CrowdStrike.
Enable the Steering Profile
If you created a new steering profile, you will need to enable it before it can be used. On the
Steering Configuration
page (
Settings > Security Cloud Platform > Steering Configuration
), click the “…” menu next to the steering profile you wish to enable, and select
Enable
.
Note
The default steering configuration profile is always enabled.
Important
You must enable a new steering profile for it to be actively used.
When a steering profile is enabled, it will be made available to all targeted users in production. You should always ensure that you have tested your steering profile with a smaller set of users before enabling it more broadly across the organization.
In this Topic
Configure a Steering Profile

---
## Filtering Traffic to High-Risk Countries
**URL:** https://docs.netskope.com/en/filtering-traffic-to-high-risk-countries/
**Last Modified:** 2025-08-31T01:51:22+00:00
**Scraped:** 2026-06-28T08:48:11.152488+00:00

Filtering Traffic to High-Risk Countries - Netskope Knowledge Portal
Filtering Traffic to High-Risk Countries
Some organizations have regulations to block traffic to any web servers hosted in specific countries that are considered “High Risk”. These countries can be deemed “High Risk” by the customer’s organization, or through regulations such as:
EAR – Export Administration Regulations
OFAC – Office of Foreign Assets Control
ITAR – International Traffic In Arms Regulations
Netskope utilizes Geo-IP mapping to determine where the destination server is hosted, and you can then create a policy to block traffic if it matches specific countries. Netskope utilizes multiple 3rd party feeds for Geo-IP mapping (such as Maxmind, IP2Location, NetAcuity, Netstar) and the feeds are updated regularly. Any Geo-IP mismatches can be reported to Netskope Support.
To create inline web policies that are meant to filter traffic to high-risk countries, follow the steps as shown below:
Navigate to
Policies
>
Real time Protection
>
New Policy
>
Web access
.
Set the values as shown below:
Source – Any
Destination – Any
Destination Country = Specified (e.g., China)
Activity – Browse
Action-  Block
Name – Customer Discretion
In this Topic
Filtering Traffic to High-Risk Countries

---
## Protect against network-based attacks
**URL:** https://docs.netskope.com/en/protect-against-network-based-attacks/
**Last Modified:** 2025-08-31T01:51:25+00:00
**Scraped:** 2026-06-28T08:48:42.233495+00:00

Protect against network-based attacks - Netskope Knowledge Portal
Protect against network-based attacks
Netskope’s Client Traffic Exploitation Protection (CTEP) is a signature-based Intrusion Protection System (IPS) that analyzes network traffic flows and continuously compares the bitstream with its internal signature database for known attack patterns.
When an attack is initiated that matches one of these signatures or patterns CTEP can either alert or block depending on how it has been configured.
In blocking mode, CTEP prevents bad actors from gaining control of vital applications or systems, causing distributed denial of service (DDoS) attacks, or obtaining access to the rights and permissions of applications.
To learn more:
Intrusion Prevention System
.
In this Topic
Protect against network-based attacks

---
## Validate Traffic Steering
**URL:** https://docs.netskope.com/en/validate-traffic-steering/
**Last Modified:** 2025-08-31T01:50:51+00:00
**Scraped:** 2026-06-28T08:49:12.163778+00:00

Validate Traffic Steering
Now that the Netskope Client has been deployed, check to confirm it is enabled, working, and correctly forwarding traffic to the Netskope Cloud.
Desktop Operating Systems
For Windows, macOS, ChromeOS, and Linux, if the Netskope client is running, you will see it located in the device’s system tray or Menu Bar (look for the Netskope logo).
If the client is enabled and connected, the client icon will be colored
If the client is disabled and disconnected, the client icon will be grayed out
There are also variations of the icon may be displayed to indicate an error or fail close scenario. If the icon is missing, check the Start Menu or Application list on your device and check to see if the Netskope client is installed.
If the client is disabled, you can right-click on the icon and click Enable Netskope Client to have it connect and start forwarding traffic. Likewise, when connected, you can right-click and select Disable Netskope Client to turn the client off (depending on the Netskope Client settings you configured, this option (along with others) may not be present).
The right-click menu of the Netskope Client. Certain options may not be present based on your settings.
To check information about the Netskope connection and device profile, right-click on the Netskope Client icon and select Configuration. Here you will be able to see:
The authenticated user (traffic will be tracked as coming from this username) The Netskope gateway IP address and Netskope POP the user is connected to. Whether the device is currently marked as
managed
or
unmanaged
.
The Steering Configuration and Client Configuration profiles currently in use on the device.
The protocol used to tunnel traffic to the Netskope Cloud (like TLS, DTLS).
The last time the configuration of the Netskope client was updated. The Netskope Client will periodically phone home to check for updated configurations (this includes the notification messaged displayed to the user when a destination or activity is blocked).
The Configuration panel of the Netskope Client shows relevant settings and connection information.
Mobile Operating Systems
For iOS and Android devices, check that a Netskope VPN profile has been installed and is enabled on the device.
If you wish to enforce the use of the profile and prevent users from disabling it, you will need to ensure to roll out the Netskope Client using a Mobile Device Manager (MDM), like Intune.
Tip
If you installed Netskope on the mobile device using an Email Invite, the Netskope certificate (required for SSL inspection) will be present on the device, but untrusted. You will need to tell the device to trust the certificate before browsing the web.
Failure to do will result in your browser throwing
Insecure Connection
or
This Connection is not Private
errors.
On iOS, go to
Settings > General > About > Certificate Trust Settings
and enable the certificate.
You will not need to do this if you installed Netskope via MDM.
Validate that the Netskope Client is forwarding traffic.
Open a new browser window and navigate to
http://notskope.com
or
https://notskope.com
(accessible over both HTTP and HTTPS). This website will tell you whether you are passing through the Netskope Cloud or not, and if so, which POP you are connected to.
Netskope.com will tell you whether or not your traffic is reaching the Netskope Cloud, and the POP you are connected to.
If your connection does not load, try opening the page in a Private Browser or Incognito window to bypass the browser cache and try again.
To check whether content is being SSL inspected correctly, examine the certificate of
https://notskope.com
(or any other HTTPS site that isn’t bypassed, like
https://www.wikipedia.org
). If the connection is being correctly SSL inspected, you will see an intermediate certificate with the name
ca.
<tenant-name>
.goskope.com
.
You can validate that a connection was SSL inspected by reviewing the certificate. If you see
ca.
<tenant-name>
.goskope.com
, en your connection was SSL inspected.
If this isn’t present, then the connection is not being SSL inspected. You should check that there is not a steering bypass or SSL decryption bypass in place preventing this.
Installation and management of the Netskope root certificate is required for SSL inspection into the system certificate trust store, and the Firefox trust store is automated by the Netskope Client.
Important
Some thick/native applications (namely apps and tools used for development) use their own certificate trust stores to check certificate validity (like Git CLI, Azure Storage Manager, etc).
Internet connections over HTTPS using these apps will fail due to an untrusted SSL error; even through the Netskope root certificate is installed in the system trust.
In these scenarios, you need to manually install the Netskope root into the trust store used by the application. There is a community script available to assist with installation for the most common tools
available here
.
The Netskope certificate can be downloaded for distribution from Netskope tenant under
Settings > Manage > Certificates
. Click the
Signing CA
tab and download the Netskope Root Certificate (first option listed).
In this Topic
Validate Traffic Steering

---
## Add New Network Location for SSL Decryption
**URL:** https://docs.netskope.com/en/add-new-network-location-for-ssl-decryption/
**Last Modified:** 2025-08-31T01:50:23+00:00
**Scraped:** 2026-06-28T08:49:50.861791+00:00

Add New Network Location for SSL Decryption - Netskope Knowledge Portal
Add New Network Location for SSL Decryption
Select
Source Network Location
from the Add Match Criteria dropdown list. Click
+New
to add a new network location. The New Network Location dialog box opens.
You can add a new IP Address or Import from a CSV file. Enter a single IP address, IP address range, or CIDR netmask. When finished, click the adjacent
+
button, and then click
Next
.
Note
You must specify at least one application and at least one platform.
Enter a name for this new network location. and click
Save Network Location
.
Click
Add Another
to add more than one new network location.
Define a match against field:
User IP Address
Egress Source IP Address
Optionally, click the X beside the network location name to delete it.
In this Topic
Add New Network Location for SSL Decryption

---
## Choose a Traffic Steering Method
**URL:** https://docs.netskope.com/en/choose-a-traffic-steering-method/
**Last Modified:** 2025-09-01T13:20:09+00:00
**Scraped:** 2026-06-28T08:50:57.071924+00:00

Choose a Traffic Steering Method - Netskope Knowledge Portal
Choose a Traffic Steering Method
There are notable differences between Netskope Cloud Access Security Broker and Netskope Secure Web Gateway traffic steering modes.
For CASB mode, enforcement points (for example, Client, Secure Forwarder, data plane on-premises, etc.) check if the traffic is destined to any of the applications that Netskope tracks in the CCI database. If yes, the steering mechanisms either steers it towards Netskope’s cloud or processes it (data plane on-premises). If no, Netskope passes the traffic to the regular next-hop/destination based on your environment.
Netskope Secure Web Gateway views all web traffic regardless if it’s CASB or not and processes it according to your environment. Web traffic is any traffic that uses the HTTP protocol.
Traffic steering mode is controlled by a global tenant flag. Netskope Secure Web Gateway must be provisioned for a tenant. When it is provisioned, the Default Tenant config can be set to steer Web and Cloud Apps. A custom Steering Configuration can be specific to an OU or User Group.
Netskope offers the following steering options:
Netskope Client Overview
IPSec
GRE
Explicit Proxy
Proxy Chaining
Steering Configuration
In this Topic
Choose a Traffic Steering Method

---
## Integrating Palo Alto Networks WildFire for Cloud Sandbox
**URL:** https://docs.netskope.com/en/integrating-palo-alto-networks-wildfire-for-cloud-sandbox/
**Last Modified:** 2025-09-03T18:23:13+00:00
**Scraped:** 2026-06-28T08:55:01.653526+00:00

Integrating Palo Alto Networks WildFire for Cloud Sandbox - Netskope Knowledge Portal
Integrating Palo Alto Networks WildFire for Cloud Sandbox
Note
Contact your Netskope representative to enable this integration.
You must have the Advanced Threat Protection license to integrate Palo Alto Networks WildFire with Netskope Cloud Sandbox.
To integrate Cloud Sanbox with Palo Alto Networks WildFire, go to
Settings
>
Threat Protection
>
Integration
. In the Palo Alto Networks Wildfire Integration window:
API-Key
: Enter the WildFire API subscription key. To learn more on how to get a WildFire API token with read and write permissions so you can provide it to Netskope:
Palo Alto Networks WildFire documentation
.
Rate-Limit-Per-Hour
: Choose to limit per hour on Netskope. For example, for a subscription of 1000 files per day, you can choose to send 50 per hour limit or use up the entire limit for the first 1000 files sent.
Type
: Only Cloud API is supported not on-prem.
Limit Files
: Choose to:
Send all files supported by WildFire, which is the default mode.
Send only the files Netskope detects as malicious to WildFire, which occurs when you select
Limit Files
.
Server
: Enter the Server IP address.
Instance Name
: Enter a unique name for the WildFire server instance.
Choosing whether to send all files or only malicious ones can depend on the rate limits imposed by your third-party threat engine license (e.g., WildFire, Sky ATP, Check Point, etc.). If you only send malicious files to WildFire, the Netskope threat detection engine essentially functions as an initial filter for malicious files.
Sending All Files to WildFire
After undergoing Netskope fast scan, the file is sent for Netskope deep scan.
Netskope deep scan checks the file type and then the rate limit for each third-party threat engine (e.g., WildFire, Sky ATP, Check Point, etc.), whichever your organization has integrated with. For Wildfire integrations, the API query allows Netskope to confirm the number of files and rate limits for file submission.
Netskope deep scan sends the file to the third-party threat engine (e.g., WildFire) and generates an alert in Skope IT if the third-party engine detects any malware. The alert appears as a
Malware
alert type in RESTful API logs and Skope IT. The third-party service also reports on all files and file hashes that are shared, regardless whether or not there was a malicious object detected.
Sending Only Malicious Files to WildFire
After undergoing Netskope fast scan, the file is sent for Netskope deep scan.
If any of the Netskope deep scanning engines (e.g., Cloud Sandbox, Advanced Heuristic Analysis, etc.) detect the file as malicious then:
Netskope deep scan checks the file type and then the rate limit for each third-party threat engine (e.g., WildFire, Sky ATP, Check Point, etc.), whichever your organization has integrated with.
Netskope deep scan sends the file to the third-party threat engine (e.g., WildFire) and generates an alert in Skope IT if the third-party engine detects it as malicious as well.
Note
If a third-party threat detection engine detects any file as malicious, then Netskope deep scan raises the alert in both modes.
Netskope also queries if the MD5 is classified as a known malicious file and obtains the WildFire report, so you can view it in Netskope.
Viewing the Malware Incidents
On the
Malware page
, you can see the detection name called “Gen.Detect.By.PAN_Widfire”.
In
Skope IT Alerts
, you can see the
Alert Type
as
Malware
.
In the
Alert Details
, you can see the following information:
In this Topic
Integrating Palo Alto Networks WildFire for Cloud Sandbox

---
## Network Location Profile
**URL:** https://docs.netskope.com/en/network-location-profile/
**Last Modified:** 2025-09-23T06:05:00+00:00
**Scraped:** 2026-06-28T08:56:01.905928+00:00

Network Location Profile - Netskope Knowledge Portal
Network Location Profile
You can add a single object or multiple object network location.
Go to
Policies > Profiles > Network Location > New Network Location
and select either
Single Object
or
Multiple Objects
.
To add a single object, provide an IP address, IP address range, or a CIDR netmask, When finished, click the adjacent
+
button, and then click
Next
. Enter a name for the network location, and then click
Save Network Location
.
IP address range and CIDR netmask examples:
10.0.0.1-10.0.0.100
,
10.0.0.0/22
To add multiple objects, upload a CSV file with multiple IP addresses or ranges. Enter a name for the network locations, and then click
Save Network Location
.
When finished, click
Apply Changes
.
Best Practices
Supported Formats
This section provides the supported formats:
Use a number sign (#) or a semicolon (;) for comments.
IP Address
CIDR
RANGE
The following are considerations to make for IP/CIDR ranges and examples are provided.
IP address range is specified as A.B.C.D-W.X.Y.Z. IP address with CIDR is specified as A.B.C.D/<bits>
Error is flagged if IP range is followed by other URL components such as path and query. If IP address/CIDR is followed by path/query, it will be interpreted as exact URL.
IP address cannot be 0.0.0.0. In an IP address range, start address must be less than end address. IP address in CIDR notation must have host portion zero.
Overlapping ranges are supported. If such ranges are associated with different categories, lookup of IP address in overlapping range would result in multiple categories. For example considering the following two ranges, a lookup of 192.186.1.2 would result in deriving “Category A” and “Category B”.
192.186.1.1 – 192.168.1.4 (Category A)
192.186.1.1 – 192.168.1.20 (Category B)
Valid Examples
#this is a single host
10.0.0.1
#this is CIDR
10.0.0.0/24
#this is a range
10.0.0.1-10.0.0.100
Invalid Examples
# Invalid ip ranges and CIDR
"http://1.2.3.20-1.2.3.10
"http://1.2.3.10-1.2.3.20/some/path"
"http://1.2.3.4/24"
In this Topic
Network Location Profile

---
## Network Location
**URL:** https://docs.netskope.com/en/network-location/
**Last Modified:** 2025-08-31T01:50:40+00:00
**Scraped:** 2026-06-28T08:56:04.131024+00:00

Network Location - Netskope Knowledge Portal
Network Location
You can add a single object or multiple object network location.
Go to
Policies
>
Profiles
>
Network Location
>
New Network Location
and select either
Single Object
or
Multiple Objects
.
To add a single object, provide an IP address, IP address range, or a CIDR netmask, When finished, click the adjacent + button, and then click
Next
. Enter a name for the network location, and then click
Save Network Location
.
To add multiple objects, upload a CSV file with multiple IP addresses or ranges. Enter a name for the network locations, and then click
Save Network Location
.
When finished, click
Apply Changes
.
In this Topic
Network Location

---
## Steer Traffic through the Appliance
**URL:** https://docs.netskope.com/en/steer-traffic-through-the-appliance/
**Last Modified:** 2026-01-14T19:00:11+00:00
**Scraped:** 2026-06-28T08:58:23.557620+00:00

Steer Traffic through the Appliance
The Dataplane On-Premises Virtual Appliance can integrate with the DNS servers or explicit proxy servers in your network to manage requests from client machines. Configure the virtual appliance in one of the following modes to steer the network traffic through the virtual appliance.
Configure the Appliance in Explicit Proxy Mode
In this Topic
Steer Traffic through the Appliance

---
## View Private App Segments and Network Events in Skope IT
**URL:** https://docs.netskope.com/en/view-private-apps-and-network-events-in-skope-it/
**Last Modified:** 2026-01-29T22:53:15+00:00
**Scraped:** 2026-06-28T08:59:39.602091+00:00

View Private App Segments and Network Events in Skope IT - Netskope Knowledge Portal
View Private App Segments and Network Events in Skope IT
Skope IT provides insight into private app usage by tracking Private Apps and Network Events, which can be compiled into a report. Skope IT pages have filters to refine search results, and you can save a filter for future use. There’s also a dropdown to sort by, plus a button to export data.
The options on Skope IT pages vary. For example, you can create an app and a policy, plus see events on the Private App Skope IT page, but not on the Network Events page. To learn more, go to
Skope IT
.
Private App Segments
Private App Segments in Skope IT enable you to monitor private apps and view relevant details. Go to
Skope IT >
Private App Segments
.
This page shows:
Application Segment Names
Destinations
Ports
Publishers
Number of users
Bytes Uploaded
Bytes Downloaded
Network Events
Network events enable you to monitor private app traffic and view relevant details, like who has access to what, from where, and for how long. To view Network Events, go to
Skope IT > Network Events
.
To view detailed information about a network event, click the icon.
Note
Publisher IP and Publisher Port were added in Release 128. Publisher IP and Publisher Port refers to the source IP and source port respectively for traffic sourcing from the Publisher to Private Apps.
You can also filter network events to show only Private Apps.
In this Topic
View Private App Segments and Network Events in Skope IT

---
## Adding Steering Exceptions for macOS Upgrade
**URL:** https://docs.netskope.com/en/adding-steering-exceptions-for-macos-upgrade/
**Last Modified:** 2025-08-31T01:49:06+00:00
**Scraped:** 2026-06-28T09:00:15.602848+00:00

Adding Steering Exceptions for macOS Upgrade - Netskope Knowledge Portal
Adding Steering Exceptions for macOS Upgrade
If you’re Netskope account isn’t updated to the most recent steering configuration, the macOS upgrade process might be interrupted. Apple uses a set of URLs for OS upgrades, and if these URLs are not bypassed by the Netskope Client, the OS upgrade process fails. If you add Apple URLs as domain exceptions in your steering configuration, the Netskope Client bypasses the URLs. These exceptions are only applicable for Apple Devices (from M1 Big Sur version 11.3.1 to latest). Any new and updated steering configurations contain these exceptions so you don’t have to add the macOS exceptions.
To add Apple URLs as domain exceptions in your steering configuration:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
for
Default tenant config
.
Click
View Exceptions
.
Click
New Exception
and then
Domains
.
In the
New Exception
window, under
Exception Type
, enter the following URLs:
ws-ee-maidsvc.icloud.com
*.cdn-apple.com
cdn-apple.com
mzstatic.com
p37-caldav.icloud.com
gateway.icloud.com
metrics.icloud.com
setup.icloud.com
*.apple.com
apple.com
You can encounter one of the following alerts while accessing Apple websites from the Safari browser if in case you do not add Apple domain exceptions in the steering configuration:
Certificate alert. To proceed further, click
OK
.
Page not available alert. Add exceptions to access the website again.
Click
Add
.
The Netskope Client syncs steering configuration updates every 60 minutes. After the Netskope Client syncs the updates, Netskope bypasses the Apple URLs and allows the device OS upgrades.
In this Topic
Adding Steering Exceptions for macOS Upgrade

---
## Configuring the Steering Preferences
**URL:** https://docs.netskope.com/en/configuring-the-steering-preferences/
**Last Modified:** 2025-08-31T01:49:06+00:00
**Scraped:** 2026-06-28T09:00:28.873096+00:00

Configuring the Steering Preferences - Netskope Knowledge Portal
Configuring the Steering Preferences
To configure the traffic steering preferences:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
Preferences
. The
Preferences
window appears.
In the
Preferences
window, for
Certificate-Pinned Apps Updates
, choose the action you want to take when Netskope adds any new predefined certificate pinned apps:
Ask me
: Receive a notification to review the new predefined certificate pinned app in a release. This is the default setting.
Skip
: Add the certificate pinned app to the default steering configuration. If you want the app added to the custom steering configurations, you must manually add it.
Bypass
: Bypass the certificate pinned app by adding it as an exception to all steering configurations.
Revert to Defaults
: Click to change to the default setting of
Ask me
.
Click
Save
.
Reviewing Predefined Certificate Pinned App Updates
If you choose
Ask me
for certificate pinned app updates, Netskope notifies you of new apps when you log in to your account. This notification displays to all admins logging in unless an admin bypasses or blocks the new apps.
To review the predefined certificate pinned app updates:
Log in to the Netskope UI. A notification appears regarding new updates to the predefined certificate pinned apps.
Click
Review updates
to configure an action for the new certificate pinned app. The
Review Updates For Certificate-Pinned Apps
appears.
Default Only (Bypass):
Bypass the certificate pinned app in the default steering configuration.
Bypass:
Bypass the certificate pinned app traffic from Netskope inspection. Netskope bypasses the app for all steering configurations.
Block:
Block traffic from this certificate pinned app. Netskope blocks traffic from the app for all steering configurations.
Click the certificate pinned app name to view platform and definition information. You can click
Cancel
to go back to the review window.
Click
Update
.
After reviewing the certificate pinned app updates, Netskope records your decision in the Audit Log page (
Settings
>
Administration
>
Audit Log
).
In this Topic
Configuring the Steering Preferences

---
## Downloading Steering Configurations
**URL:** https://docs.netskope.com/en/downloading-steering-configurations/
**Last Modified:** 2025-08-31T01:49:07+00:00
**Scraped:** 2026-06-28T09:00:35.532012+00:00

Downloading Steering Configurations - Netskope Knowledge Portal
Downloading Steering Configurations
To download a CSV file with all the information of a steering configuration:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
).
Click
for the steering configuration you want to download its details.
Click
View Steered Items
or
View Exceptions
.
Click
Download
.
Select any of following options:
PAC File
: Download the PAC file associated with the steering configuration.
Desktop Domains
: Download a CSV file with the desktop domains associated with the steering configuration.
Android Domains
: Download a CSV file with the Android domains associated with the steering configuration.
SFDR Domains
: Download a CSV file with the SFDR domains associated with the steering configuration.
IOS Domains
: Download a CSV file with the iOS domains associated with the steering configuration.
Create Perimeter Policy
: Create and download a perimeter policy as a TXT file. In the
Perimeter Policy
window:
Vendor
: Download a text file based on the following vendors.
BlueCoat
Juniper Networks
Palo Alto Networks
Websense (Forcepoint)
Policy Name
: Enter a name for the perimeter policy.
You can use the Download option for Android, SFDR, and iOS domains only with the Cloud Apps mode.
In this Topic
Downloading Steering Configurations

---
## Editing the Default Steering Configuration
**URL:** https://docs.netskope.com/en/editing-the-default-steering-configuration/
**Last Modified:** 2025-08-31T01:49:05+00:00
**Scraped:** 2026-06-28T09:00:37.717514+00:00

Editing the Default Steering Configuration - Netskope Knowledge Portal
Editing the Default Steering Configuration
The default steering configuration (i.e., Default tenant config) applies to all users in your organization. If some users in your organization require a different configuration, you can
create
a new steering configuration for those specific OUs or user groups.
To edit the default steering configuration and specify which traffic it steers:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
for
Default tenant config
.
Do the following:
View Steered Items
: Click to go to the
Steered Traffic
tab where you can add applications and steer their traffic to Netskope for deep analysis via Real-time Protection policies. To learn more:
Adding Steered Items
.
View Exceptions
: Click to go to the
Exceptions
tab where you can add
exceptions
for the default steering configuration and bypass the traffic from Netskope.
Edit Configuration
: Modify the default steering configuration and its settings. To learn more:
Creating a Steering Configuration
.
Clone
: Create a copy of the default steering configuration.
In this Topic
Editing the Default Steering Configuration

---
## Netskope GRE with Palo Alto Networks NGFW
**URL:** https://docs.netskope.com/en/netskope-gre-with-palo-alto-networks-ngfw/
**Last Modified:** 2026-05-26T19:51:16+00:00
**Scraped:** 2026-06-28T09:03:40.662725+00:00

Netskope GRE with Palo Alto Networks NGFW - Netskope Knowledge Portal
Netskope GRE with Palo Alto Networks NGFW
Generic Routing Encapsulation (GRE) is a tunneling protocol for encapsulating packets inside a transport protocol. GRE is a direct point-to-point connection across a network, but without encryption. It transports packets from one endpoint to another endpoint. Netskope supports using GRE with Palo Alto Networks Next-Generation Firewall (NGFW).
GRE is ideal for steering HTTP and HTTPS traffic to the Netskope cloud. The Netskope GRE gateway validates the source IP address of the tunnel configured in the Netskope UI.
Always create at least two GRE tunnels for each egress location in your network. Having multiple GRE tunnels ensures that connectivity is maintained in the event of an outage on the primary tunnel. The second GRE tunnel takes over until the first GRE tunnel gets restored. The second tunnel should be connected to a different Netskope data center than the first tunnel.
Netskope GRE Configuration
To create the GRE tunnels for Palo Alto Networks NGFW in the Netskope UI, see
Creating a GRE Site
.
Palo Alto Networks NGFW Configuration
Before making any changes, create a backup and export the current running configuration on each NGFW. The configuration steps below are specific to the Example Configuration and will need to be modified to suit your environment.
The following tables detail the example configuration used for the Palo Alto NGFW in this guide.
Interfaces
Name
Virtual Router
Zone
Network
Interface IP
ethernet 1/1
default
public
10.254.1.0/24
10.254.1.253
ethernet 1/2
default
private
10.254.2.0/24
10.254.2.253
tunnel.1
default
public
10.1.1.0/30
10.1.1.1
tunnel.2
default
public
10.1.2.0/30
10.1.2.1
Routing
Virtual Router
Interfaces
Name
Destination
Next Hop
default
ethernet 1/1
ethernet 1/2
default
0.0.0.0/0
10.254.1.1
default
ethernet 1/1
ethernet 1/2
private
10.254.0.0/16
10.254.2.1
Rules
Name
Source Zone
Source Address
Destination Zone
Destination Address
Application
Service
allow_icmp
private
10.254.0.0/16
public
any
icmp
application-default
allow_dns
private
10.254.0.0/16
public
any
dns
application-default
allow_ntp
private
10.254.0.0/16
public
any
ntp
application-default
allow_http_https
private
10.254.0.0/16
public
any
any
service-http
service-https
NAT
Original Packet
Translated Packet
Name
Source Zone
Destination Zone
Destination Interface
Source Address
Destination Address
Service
Source Translation
snat_private
private
public
ethernet1/1
10.254.0.0/16
any
any
dynamic-ip
10.254.1.253
Configure Tunnel Interfaces
To perform these steps, first log in to your Palo Alto Networks admin account. If you want to skip over the UI steps, CLI commands are provided at the end of this section to speed up the configuration tasks.
Go to
Network > Interfaces > Tunnels
. Click
Add
to configure the 1st tunnel interface.
The read-only Interface Name is set to tunnel. In the adjacent field, enter a numeric suffix (1-9999) to identify the interface.
Assign a virtual router to the interface, or click
Virtual Router
to define a new one.
Select a security zone for the interface, or click
Zone
to define a new zone.
Select the
IPv4
tab, and click
Add
.
Assign a tunnel interface IP and subnet mask. This IP subnet is only locally significant to the tunnel.
Select
OK
to save the tunnel interface.
Repeat the above steps to configure a 2nd tunnel interface: Change the
tunnel suffix
and the tunnel interface
IP
and subnet mask.
CLI Commands
Use these CLI commands to speed up the configuration.
# set network interface tunnel units tunnel.1 ip 10.1.1.1/30
    # set network virtual-router default interface tunnel.1
    # set zone public network layer3 tunnel.1
    # set network interface tunnel units tunnel.2 ip 10.1.2.1/30
    # set network virtual-router
default
interface
tunnel.2
# set zone
public
network layer3
tunnel.2
Configure the GRE Tunnels
If you want to skip over the UI steps, CLI commands are provided at the end of this section to speed up the configuration tasks.
Go to
Network > GRE Tunnels
. Click
Add
to configure the 1st GRE tunnel
Use
GRE Gateway IP
from 1st Netskope POP selected in step 1.5 as the
Peer Address
. In this example MEL1 will be used for the 1st tunnel (
tunnel.1
).
Enable
Keep Alive
so the GRE tunnel stays connected when/if the User traffic is idle.
Select
OK
to save.
Configure the 2nd GRE tunnel.
Repeat the above steps using the GRE Gateway IP from the 2nd Netskope POP selected as the Peer Address. In this example SY4 will be used for the 2nd tunnel (
tunnel.2
).
Commit the configuration.
The GRE tunnels should establish and can be verified using the CLI. Please refer to
Verify GRE Tunnels are Established
.
CLI Commands
Use these CLI commands to speed up the configuration.
# set network tunnel gre
netskope_mel1
tunnel-interface
tunnel.1
peer-address ip
163.116.198.36
# set network tunnel gre
netskope_mel1
tunnel-interface
tunnel.1
local-address interface
ethernet1/1
ip
10.254.1.253/24
# set network tunnel gre
netskope_mel1
tunnel-interface
tunnel.1
keep-alive enable yes
# set network tunnel gre
netskope_sy4
tunnel-interface
tunnel.2
peer-address ip
45.250.160.32
# set network tunnel gre
netskope_sy4
tunnel-interface
tunnel.2
local-address interface
ethernet1/1
ip
10.254.1.253/24
# set network tunnel gre
netskope_sy4
tunnel-interface
tunnel.2
keep-alive enable yes
# commit
Policy Based Forwarding (PBF)
PBF will steer the relevant traffic to the Netskope POP over the GRE tunnel. It’s recommended to forward Web Traffic (TCP 80/443 etc.) only. When creating PBF rules, it is recommended to be as specific as possible to ensure the correct traffic is sent to Netskope Cloud. If you want to skip over the UI steps, CLI commands are provided at the end of this section to speed up the configuration tasks.
Go to
Objects > Services > Add
.
Configure a custom service for Netskope traffic. This provides the flexibility to easily add additional custom ports at a later date.
Your
TCP 80 and 443
traffic should be steered to Netskope by default.
Select
OK
to save.
Go to
Network > Network Profiles > Monitor > Add
.
This monitor will be used to check the GRE tunnel connectivity is established using ICMP. If the monitor fails, the tunnel should failover to the 2nd GRE tunnel.
Give the monitor a Name and change the Action to
Fail Over
. Adjust the
Interval
and
Threshold
to your liking.
Select
OK
to save.
Go to
Policies > Policy Based Forwarding > Add
.
Configure the PBF Rule to steer traffic over the 1st GRE tunnel (
tunnel.1
interface), which corresponds to MEL1 POP.
Give the PBF Rule a
Name
Select the
Source
tab and enter the criteria specific to your environment.
Select the
Destination/Application/Service
tab.
Add the SERVICE
service-netskope
that was configured in step 1 of this section.
Select the
Forwarding
tab
Set the Action to
Forward
Select
tunnel.1
as the Egress Interface
Enable the
Monitor
and select the
netskope_gre
Profile created in step 5 of this section.
The IP Address is the Probe IP Address of the 1st Netskope POP selected. In this example
MEL1
, will be used for the 1st tunnel.
Select
OK
to save.
Configure the PBF Rule to steer traffic over the 2nd GRE tunnel (
tunnel.2
interface), which corresponds to SY4 POP.
Repeat the above steps: Change the Name, Egress Interface to
tunnel.2
and the Monitor IP Address.
CLI Commands
Use these CLI commands to speed up the configuration.
# set service service-netskope protocol tcp port 80,443
# set network profiles monitor-profile netskope_gre interval
3
threshold
5
action fail-over
# set rulebase pbf rules
pbf_to_netskope_mel1
action forward egress-interface
tunnel.1
monitor ip-address
10.198.6.209
profile netskope_gre
# set rulebase pbf rules
pbf_to_netskope_mel1
source
10.254.2.0/24
destination any service service-netskope from zone
private
# set rulebase pbf rules
pbf_to_netskope_sy4
action forward egress-interface
tunnel.2
monitor ip-address
172.24.16.13
profile netskope_gre
# set rulebase pbf rules
pbf_to_netskope_sy4
source
10.254.2.0/24
destination any service service-netskope from zone
private
NAT Settings
Once a packet matches the criteria of a single NAT rule, the packet is not subjected to additional NAT rules. Therefore, your list of NAT rules should be in order from most specific to least specific so that packets are subjected to the most specific rule you created for them.
When steering traffic to a Netskope POP via GRE, Secure NAT (SNAT) needs to be disabled. This allows the Netskope Cloud XD the “engine” of Netskope’s platform to see the real Source IP of the traffic for Policy and Logging purposes. In this example more specific SNAT rules need to be created to disable SNAT.
The SNAT/NAT configuration in this example prior to adding the specific SNAT rules for Netskope GRE is detailed below for reference. The current SNAT configuration will SNAT all traffic going from private to public zone with a source address of 10.254.0.0/16 to 10.254.1.253 (ethernet1/1 interface IP).
If you want to skip over the UI steps, CLI commands are provided at the end of this section to speed up the configuration tasks.
Go to
Polices > NAT
and click
Add
.
Configure the NAT Policy Rule to disable SNAT for traffic steered to 1st GRE tunnel (
tunnel.1
interface).
Give the NAT Policy Rule a
Name
Select the
Original Packet
tab.
Configure the Source Zone, Destination Zone, Source Address to be as specific as possible. In this example, only be concerned with Source Addresses in the
10.254.2.0/24
network.
Set the Destination Interface to
tunnel.1
.
Set the Service to
service-netskope
.
Select
OK
to save.
Select the
Translated Packet
tab.
Leave the defaults to
None
.
Select
OK
to Save.
Configure the NAT Policy Rule to disable SNAT for traffic steered to 2nd GRE tunnel (
tunnel.2
interface).
Repeat the above steps: Change the Name and change the Destination Interface to
tunnel.2
Re-Order the NAT Policy Rules.
Depending on your environment, the SNAT/NAT rules will need to be re-ordered so the most specific rules are at the top. In this example I have placed the NAT Policy Rule to disable SNAT at the top.
Commit the final configuration and test.
CLI Commands
Use these CLI commands to speed up the configuration.
# set rulebase nat rules
dont_snat_netskope_mel1
from
private
to
public
source
10.254.2.0/24
destination any service service-netskope to-interface
tunnel.1
# set rulebase nat rules
dont_snat_netskope_sy4
from
private
to
public
source
10.254.2.0/24
destination any service service-netskope to-interface
tunnel.2
# move rulebase nat rules dont_snat_netskope_mel1 top
# move rulebase nat rules dont_snat_netskope_sy4 after dont_snat_netskope_mel1
# commit
Verify GRE Tunnels are Established
Run the show interface commands and check to ensure tunnel interface state is up.
> show interface tunnel.1
--------------------------------------------------------------------------------
Name: tunnel.1, ID: 256
Operation mode: layer3
Virtual router default
Interface MTU 1500
Interface IP address: 10.1.1.1/30
Interface management profile: N/A
Service configured: 
Zone: public, virtual system: vsys1
Adjust TCP MSS: no
Policing: no
--------------------------------------------------------------------------------
GRE tunnel name:               netskope_mel1
tunnel interface state:        Up
disabled:                      False
copy-tos:                      False
keep alive enabled:            True
local-ip:                      10.254.1.253
peer-ip:                       163.116.198.36
stats:
   ka-id:                      295
   ka-send:                    295
   ka-recv:                    295
   ka-curr-retry:              0
   ka-last-timestamp:          8874
   ka-recv-map:                0
   ka-owner:                   0
--------------------------------------------------------------------------------
Logical interface counters read from CPU:
--------------------------------------------------------------------------------
bytes received                           0
bytes transmitted                        14076
packets received                         0
packets transmitted                      306
receive errors                           0
packets dropped                          0
packets dropped by flow state check      0
forwarding errors                        0
no route                                 0
arp not found                            0
neighbor not found                       0
neighbor info pending                    0
mac not found                            0
packets routed to different zone         0
land attacks                             0
ping-of-death attacks                    0
teardrop attacks                         0
ip spoof attacks                         0
mac spoof attacks                        0
ICMP fragment                            0
layer2 encapsulated packets              0
layer2 decapsulated packets              0
tcp cps                                  0
udp cps                                  0
sctp cps                                 0
other cps                                0
--------------------------------------------------------------------------------
> show interface tunnel.2
--------------------------------------------------------------------------------
Name: tunnel.2, ID: 257
Operation mode: layer3
Virtual router default
Interface MTU 1500
Interface IP address: 10.1.2.1/30
Interface management profile: N/A
Service configured:
Zone: public, virtual system: vsys1
Adjust TCP MSS: no
Policing: no
--------------------------------------------------------------------------------
GRE tunnel name:               netskope_sy4
tunnel interface state:        Up
disabled:                      False
copy-tos:                      False
keep alive enabled:            True
local-ip:                      10.254.1.253
peer-ip:                       45.250.160.32
stats:
ka-id:                      295
ka-send:                    295
ka-recv:                    295
ka-curr-retry:              0
ka-last-timestamp:          8874
ka-recv-map:                0
ka-owner:                   0
--------------------------------------------------------------------------------
Logical interface counters read from CPU:
--------------------------------------------------------------------------------
bytes received                           0
bytes transmitted                        14076
packets received                         0
packets transmitted                      306
receive errors                           0
packets dropped                          0
packets dropped by flow state check      0
forwarding errors                        0
no route                                 0
arp not found                            0
neighbor not found                       0
neighbor info pending                    0
mac not found                            0
packets routed to different zone         0
land attacks                             0
ping-of-death attacks                    0
teardrop attacks                         0
ip spoof attacks                         0
mac spoof attacks                        0
ICMP fragment                            0
layer2 encapsulated packets              0
layer2 decapsulated packets              0
tcp cps                                  0
udp cps                                  0
sctp cps                                 0
other cps                                0
--------------------------------------------------------------------------------
In this Topic
Netskope GRE with Palo Alto Networks NGFW

---
## Send Traffic from Netskope back to Exchange
**URL:** https://docs.netskope.com/en/send-traffic-from-netskope-back-to-exchange/
**Last Modified:** 2026-05-19T18:16:30+00:00
**Scraped:** 2026-06-28T09:04:25.412583+00:00

Send Traffic from Netskope back to Exchange - Netskope Knowledge Portal
Send Traffic from Netskope back to Exchange
This guide details how to route outbound email traffic from Microsoft 365 Exchange Online to the Netskope SMTP Proxy for Data Loss Prevention (DLP) and policy inspection, and safely route it back to Exchange for external delivery. This architecture is known as a loopback deployment.
Mail Flow Process Overview
When your environment does not utilize a third-party Mail Transfer Agent (MTA), you must configure Microsoft 365 Exchange Online to enable Netskope to route inspected traffic back to your primary mail server.
The following lifecycle outlines the end-to-end loopback mail flow
Outbound Initiation
: An user sends an email from their corporate account to an external recipient.
Proxy Redirection
: Exchange Online intercepts the outbound email and routes it via SMTP to the Netskope SMTP Proxy for inspection.
Policy & Inspection
: The Netskope platform applies configured Data Loss Prevention (DLP) and compliance policies.
Loopback Handoff
: Once validated, Netskope routes the traffic back to Exchange Online (the Next Hop) via SMTP.
External Resolution & Delivery
: Exchange Online performs an MX lookup via DNS to locate the recipient’s mail server and delivers the message via the Internet.
Deployment Prerequisites
To establish the loopback configuration, you must execute administrative changes across both the Netskope tenant and the Microsoft Exchange admin center (EAC):
Netskope Tenant Configuration
Configure Microsoft 365 Exchange Online as the authoritative Next Hop gateway.
Microsoft Exchange Admin Center (EAC) Configuration
Outbound Connector
: Directs designated outbound corporate email traffic to the Netskope SMTP Proxy.
Inbound Connector
: Explicitly trusts and accepts the incoming SMTP traffic returning from the Netskope SMTP Proxy.
Mail Flow Rule
(
Loop Prevention
): Activates the outbound connector and stops infinite routing loops by checking for specific inspection headers.
Connection Filtering Protection
: Configures underlying perimeters to allow Exchange to accept traffic from designated Netskope SMTP Proxy IP ranges.
Configure Exchange Online as the Next Hop in Netskope
To configure the Netskope tenant to route inspected mail back to your environment, you must retrieve your unique Exchange Online domain name (FQDN)
Log in to the Microsoft 365 admin center.
In the left navigation menu, click …
Show All
, then proceed to
Settings
>
Domains
.
Click on your
Default Domain
and select the
DNS records
tab.
Under the
Exchange Online
section, click on the
MX
record to display the MX record pane on the right.
Locate the string under
Points to address
or Value and copy it.
Log in to your
Netskope Tenant
, navigate to the
Edit Microsoft Office 365 Exchange Settings
workspace, and paste the copied FQDN value into the Next Hop field.
Explicitly define the Next Hop port as
25
and save your changes.
Sender Policy Framework (SPF) Alignment
If you are running SPF checks on your Exchange server, then you must add the Netskope domain to your Exchange server’s DNS TXT record. To add a new TXT record:
1. In the Microsoft 365 admin center page, click … Show All to view all the options and navigate to Settings > Domains.
2. Click on the default domain, select the
DNS records
tab, and click
Add record
.
3. In the Add a custom DNS record right pane, specify a name for the TXT record and specify the TXT value as:
_spf.goskope.com
. When finished, click Save.
Establish the Inbound Connector in Exchange Online
You must establish an inbound connector that allows Microsoft 365 Exchange Online to accept and trust returning mail streams from the Netskope SMTP Proxy:
Navigate to the Exchange admin center (EAC), click
mail flow
in the left navigation pane, and select the
connectors
tab.
Click the
+
(Add) icon to launch the New Connector setup wizard.
In the
Select your mail flow scenario
window, map the routing boundaries precisely:
From
: Your organization’s email server (
Do not select Partner Organization
) and
To
: Office 365. Click
Next
.
Provide a clear identifier name (e.g.,
Netskope-to-Exchange
) and add an operational description.
Ensure that both
Turn it on
and
Retain internal Exchange email headers (recommended)
are checked, then click Next.
On the next screen, select the radio button option: “
By verifying that the IP address of the sending server matches one of these IP addresses that belong to your organization
“.
Click the
+
icon to input the operational CIDR IP blocks of the Netskope SMTP Proxy servers sending traffic back to Exchange.
Review your configured settings and click
Save
to create the connector.
Establish the Outbound Connector & Loop Prevention Rule
To route outbound traffic cleanly to Netskope, you must deploy an outbound connector and pairing mail flow rule.
In the Exchange admin center, create an
Outbound Connector
designed to deliver messages from Office 365 to a Partner organization (representing the Netskope SMTP Proxy gateway).
Deploy a
Mail Flow Transport Rule
to govern this outbound connector. The rule enforces inspection policies while acting as a critical loop prevention system:
The rule checks for the presence of the
x-netskope-inspected: true
string inside the SMTP headers.
If the header is present, Exchange recognizes the mail stream has already been processed by Netskope and bypasses the outbound connector to prevent an infinite loop.
If the header is absent, Exchange routes the uninspected mail directly to the Netskope SMTP Proxy.
Configure Connection Filtering (Allowlisting)
Ensure that traffic returning from Netskope is not throttled or erroneously blocked by Exchange Online anti-spam security filters:
In the
Exchange admin center
, select
protection
and click the
connection filter
tab.
If your tenant has migrated to Microsoft’s modern security architecture, configure these settings in the
Microsoft Defender Security and Compliance Center
via the
Anti-spam
policies workspace
.
Highlight the
Default
connection filter policy and click the
Edit (Pencil)
icon.
Inside the spam filter policy window, choose
connection filtering
in the sub-menu.
Under the
IP Allow list
section, click the
+
icon.
Add the complete list of authorized Netskope SMTP Proxy IP ranges.
Click
Save
to apply the configuration change.
IP Ranges for Allowlisting
For a complete and updated list of IP addresses, go to the Netskope Email DLP (SMTP) List for Allowlisting section in this article:
NewEdge Consolidated List of IP Ranges for Allowlisting
.
In this Topic
Send Traffic from Netskope back to Exchange

---
## Send Traffic from Netskope back to Gmail
**URL:** https://docs.netskope.com/en/send-traffic-from-netskope-back-to-gmail/
**Last Modified:** 2026-06-25T19:19:26+00:00
**Scraped:** 2026-06-28T09:04:28.831686+00:00

Send Traffic from Netskope back to Gmail - Netskope Knowledge Portal
Send Traffic from Netskope back to Gmail
Netskope offers a loopback solution to send traffic from the Netskope SMTP proxy back to the Gmail server.
To enable this solution, you must configure the following:
In your Netskope tenant, configure Gmail as the next hop. For detailed instructions, see
Configure the Gmail server as the Next Hop in the Netskope tenant
.
In the Google admin console, configure the Netskope SMTP Proxy and then configure content compliance to send traffic from Gmail to Netskope. For detailed instructions, see the sections, “
Configure Netskope SMTP Proxy in Google admin center
” and ”
Configure content compliance to send traffic from Gmail to Netskope
” in
Configure Netskope SMTP Proxy with Gmail
.
Note
When configuring content compliance in Gmail, you can use the Netskope SMTP Proxy header to setup a rule to reject messages in case of a DLP profile match.
In the Google admin console, configure SMTP relay service so that Gmail can accept traffic from Netskope. For detailed instructions, see
Configure SMTP relay service to send traffic from Netskope back to Gmail
.
Configure the Gmail Server as the Next Hop in the Netskope Tenant
Follow the instructions up to step 4 in the “
Configure the Gmail server and the upstream MTA in the Netskope tenant
” section of
Configure Netskope SMTP Proxy with Gmail
.
In the Next Hop section, specify the Gmail server’s IP/FQDN as
smtp-relay.gmail.com
and Port as
587
. Click
Save
.
Configure SMTP Relay Service to Send Traffic from Netskope back to Gmail
Note
When using the SMTP relay service, Each Gmail user account has a limit of 10,000 emails that can be sent over a 24-hour period to the relay service.
For more information about SMTP relay service in Gmail and the limitations, refer to the
Gmail support article
.
On the Settings for Gmail page, click
Advanced settings
.
On the General Settings page, go to the Routing section.
Mouseover SMTP relay service and click
Add Another
to add a new entry.
In the Add setting dialog box, set the following:
Under step1, Allowed senders, select
Only addresses in my domains
.Under step2, Authentication, select
Only accept mail from the specified IP addresses
. Click Add IP range to add the list of IP addresses of Netskope SMTP proxy servers in CIDR notation that will be sending traffic to the Gmail server.
For a complete and updated list of IP addresses, go to the Netskope Email DLP (SMTP) List for Allowlisting section in this article:
NewEdge Consolidated List of IP Ranges for Allowlisting
(A Netskope Support account is required.).
Under step 3, Encryption, select
Require TLS encryption
. Click
Add Setting
.
In this Topic
Send Traffic from Netskope back to Gmail

---
## Network Events
**URL:** https://docs.netskope.com/en/about-network-events/
**Last Modified:** 2025-08-31T01:39:05+00:00
**Scraped:** 2026-06-28T09:05:17.269604+00:00

Network Events
About Network Events
Network events enable you to monitor private app traffic and view relevant details, like who has access to what, from where, and for how long. To view Network Events, go to
Skope IT
>
Events & Alerts
>
Network Events
.
To view detailed information about a network event, click the  icon. Under General, Traffic Type (Private Apps), Access Method (Client or Browser Access), and Tunnel Type (NPA) are shown.
This Network Events page has the following components:
You can select from a wide range of filter options. Your most recent filter selection will be displayed when you revisit the page.
Network Events table
: Displays specified page events information. To change the information displayed, use the Customize Columns dialog box. Use the Sort By list in the table header row to arrange the listings in the table. Time is when the event occurred in the cloud platform.
Refresh Page button
: To update the page with the most current information, click
next to the page title.
Customize Columns dialog box
: To customize the columns shown for each event, click
located at the far right of the table column header row, and then select the columns you want to see. For more details, refer to
Customize Columns
below.
Date Range list
: In the top right corner of the page is a date range filter. Click the toggle and select one of these date ranges.
Application search filter
: This search field helps you find applications and then filter results. Enter a name and then select from the list.
Add Filter lists
: To create a filter, click
+ Add Filter
, select what to include what to find in the search, and then click
Apply
.
Tip
You can choose multiple items for some options. The options with the
icon allows you to search.
Save Filter button
: After adding a filter, you can save it for future searches by clicking
Save Filter
.
Add to Watchlist button
: To add filter values or query strings to a watchlist, click
Add to Watchlist
.
Query Mode button
: Optionally, switch to query mode
and enter a query in the search field. For example, to specify which app to search for, the domain, and the user’s email address, enter the following query.
app eq 'Google Drive' and instance_id eq '
<yourcompany.com>
' and user eq '
<user@yourcompany.com>
'
You can pin the query by clicking the pin icon
to remember the query across the Application Events, Page Events, and Alerts pages.
To change back to the filter view, click
Filter Mode
.
Export button
: Click
Export
to get the entire list of application events. First select the columns to export (those displayed, or specify which columns), and the number of rows, then click
Export
again. Your column and row selections are retained for future exports.
You will be sent an email with a link that allows you to download the list in CSV format.
Event Details button
: Click the magnifying glass icon
besides any listing to view more details about the page event. The default view shows the page events for the last 7 days unless you change the date range setting.
Rows per page list
: At the bottom right corner of the page, the Rows per page list allows you to display 10, 20, 30, 50, or 100 rows per page.
In this Topic
Network Events

---
## Get a Steering Configuration List
**URL:** https://docs.netskope.com/en/get-a-steering-configuration-list/
**Last Modified:** 2025-08-31T01:39:21+00:00
**Scraped:** 2026-06-28T09:07:00.972104+00:00

Get a Steering Configuration List - Netskope Knowledge Portal
Get a Steering Configuration List
This endpoint returns all the Steering Configuration names and the Steering Config IDs associated to them. Use this API to get the Steering Config name or Steering Config ID so you can get values about your steering configuration(s) to use in the
Get Steering Configuration Information
endpoint.
Request Endpoint
https://
<tenant-URL>
/api/v1/steeringconfiglist
Example Request with Response
curl -X GET https://
<tenant-URL>
/api/v1/steeringconfiglist?token=
<token>
{
  status: "success",
  msg: "",
  data: [
    {
      config_id: 0,
      config_name: "Default tenant config"
    },
    {
      config_id: 2,
      config_name: "cloud based"
    },
    {
      config_id: 3,
      config_name: "web based"
    },
    {
      config_id: 4,
      config_name: "location based steering"
    }
  ]
}
In this Topic
Get a Steering Configuration List

---
## Get Steering Configuration Information
**URL:** https://docs.netskope.com/en/get-steering-configuration-information/
**Last Modified:** 2025-08-31T01:39:21+00:00
**Scraped:** 2026-06-28T09:07:12.437356+00:00

Get Steering Configuration Information - Netskope Knowledge Portal
Get Steering Configuration Information
Use this endpoint to get these details about your steering configuration(s):
Steering Configuration information
Exceptions for the Steering Configuration
On-Premises and Off-Premises Steering Configuration and Exceptions information if the configuration has Location-Based Steering enabled.
Request Endpoint
https://
<tenant-URL>
/api/v1/steeringconfig
Valid query parameters are:
Key
Value
Description
token
string
Required. The token obtained from the REST API page in the Netskope UI (
Settings > Tools > Rest API v1
) is required. We recommend that you place the token in the body of the request, not in the endpoint URL.
config
URL-encoded string
Filters results by the Steering Configuration name. Use a
config
(name) value from the
steeringconfiglist
API.
config_id
Positive Integer (specific to a steering configuration)
Filters results by the Steering Configuration ID. Use a
config_id
value from the
steeringconfiglist
API.
limit
Positive integer less than 10000
REST API responses can return up to 10000 records in a single response. You can use pagination to retrieve more results.
skip
Positive integer
Skip over some of the records (useful for pagination in combination with
limit
).
Note
Not using
config
or
config_id
will return all steering configurations information.
Request Example with Response using Location Based Steering
Note that the config name passed in the parameters is URL-encoded.
POST 'https://
<tenant-URL>
/api/v1/steeringconfig?config=location%20based%20steering
{    
    "token": "f32a973eddd7bc1602fc0f48dc0a"
}
{
  "status": "success",
  "msg": "",
  "data": [
    {
      "steering_config": "location based steering",
      "enabled": true,
      "location_based_steering": true,
      "private_apps_enabled": false,
      "priority": "2",
      "on_prem": {
        "steered_traffic": {
          "data": [
            {
              "app_id": "101",
              "app_name": "Adrenalin",
              "disabled": "0",
              "app_domains": "adrenalin.com",
              "app_category": "HR",
              "modify_time": "2019-08-19 17:38:15",
              "app_cci": "31",
              "app_ccl": "poor"
            },
            {
              "app_id": "105",
              "app_name": "ProcessManagement",
              "disabled": "0",
              "app_domains": "processmanagement.com",
              "app_category": "Business Process Management",
              "modify_time": "2019-08-19 17:38:15",
              "app_cci": "63",
              "app_ccl": "medium"
            }
          ],
          "count": 2
        },
        "exceptions": {
          "applictions": {
            "data": [
            ],
            "count": 0
          },
          "domains": {
            "data": [
            ],
            "count": 0
          },
          "src_netloc": {
            "data": [
            ],
            "count": 0
          },
          "dst_netloc": {
            "data": [
              {
                "notes": "on-prem: [default destination location]",
                "dst_netloc": [
                  "Local IP address range"
                ]
              }
            ],
            "count": 1
          },
          "countries": {
            "data": [
            ],
            "count": 0
          },
          "cert_pinned_apps": {
            "data": [
              {
                "notes": "on-prem: [default ssl pinned app]",
                "app_name": "Amazon CloudDrive",
                "enabled": true,
                "data": {
                  "custom": false,
                  "appName": "Amazon CloudDrive",
                  "android": {
                    "action": "1",
                    "processes": [
                      "com.amazon.clouddrive",
                      "com.amazon.clouddrive"
                    ],
                    "enabled": true,
                    "domains": [
                      "drive.amazonaws.com",
      "us-east-1.amazonaws.com",
      "us-west-2.amazonaws.com",
      "drive.amazon.com",
      "amazon.ca",
      "amazon.in",
                      "amazon.co.uk"
                    ]
                  },
                  "mac": {
                    "action": "1",
                    "processes": [
                      "Amazon Cloud Dr",
                      "Amazon Cloud Drive Sync Service",
                      "Amazon Cloud Drive"
                    ],
                    "enabled": true,
                    "managed_device": false,
                    "tunnel": false,
                    "tunnel_domains": [
                    ]
                  },
                  "windows": {
                    "action": "1",
                    "processes": [
                      "AmazonCloudDriveW.exe",
                      "AmazonCloudDrive.exe"
                    ],
                    "enabled": true,
                    "managed_device": false,
                    "tunnel": false,
                    "tunnel_domains": [
                    ]
                  },
                  "ios": {
                    "action": "1",
                    "processes": [
                    ],
                    "enabled": false,
                    "domains": [
                      "drive.amazonaws.com",
      "us-east-1.amazonaws.com",
      "us-west-2.amazonaws.com",
      "drive.amazon.com",
      "amazon.ca",
      "amazon.in",
                      "amazon.co.uk"
                    ]
                  }
                }
              }
            ],
            "count": 1
          }
        }
      },
      "off_prem": {
        "steered_traffic": {
          "data": [
          ],
          "count": 0
        },
        "exceptions": {
          "categories": {
            "data": [
              {
                "categories": [
                  "Finance/Accounting",
                  "Internet Telephony",
                  "Streaming & Downloadable Audio",
                  "Streaming & Downloadable Video",
                  "Telecom and Call Center",
                  "Web Conferencing"
                ],
                "notes": "off-prem: [default categories]"
              }
            ],
            "count": 1
          },
          "domains": {
            "data": [
              {
                "domains": [
                  "android.clients.google.com",
                  "apple.com",
                  "gs.apple.com",
                  "itunes.apple.com",
                  "play.google.com",
                  "webex.com",
                  "youtube.com"
                ],
                "notes": "off-prem: [default domains]"
              }
            ],
            "count": 1
          },
          "src_netloc": {
            "data": [
            ],
            "count": 0
          },
          "dst_netloc": {
            "data": [
              {
                "notes": "off-prem: [default destination location]",
                "dst_netloc": [
                  "Local IP address range"
                ]
              }
            ],
            "count": 1
          },
          "countries": {
            "data": [
            ],
            "count": 0
          },
          "cert_pinned_apps": {
            "data": [
              {
                "notes": "off-prem: [default ssl pinned app]",
                "app_name": "Amazon CloudDrive",
                "enabled": true,
                "data": {
                  "custom": false,
                  "appName": "Amazon CloudDrive",
                  "android": {
                    "action": "1",
                    "processes": [
                      "com.amazon.clouddrive",
                      "com.amazon.clouddrive"
                    ],
                    "enabled": true,
                    "domains": [
                      "drive.amazonaws.com",
      "us-east-1.amazonaws.com",
      "us-west-2.amazonaws.com",
      "drive.amazon.com",
      "amazon.ca",
      "amazon.in",
                      "amazon.co.uk"
                    ]
                  },
                  "mac": {
                    "action": "1",
                    "processes": [
                      "Amazon Cloud Dr",
                      "Amazon Cloud Drive Sync Service",
                      "Amazon Cloud Drive"
                    ],
                    "enabled": true,
                    "managed_device": false,
                    "tunnel": false,
                    "tunnel_domains": [
                    ]
                  },
                  "windows": {
                    "action": "1",
                    "processes": [
                      "AmazonCloudDriveW.exe",
                      "AmazonCloudDrive.exe"
                    ],
                    "enabled": true,
                    "managed_device": false,
                    "tunnel": false,
                    "tunnel_domains": [
                    ]
                  },
                  "ios": {
                    "action": "1",
                    "processes": [
                    ],
                    "enabled": false,
                    "domains": [
                      "drive.amazonaws.com",
                      "us-east-1.amazonaws.com",
                      "us-west-2.amazonaws.com",
                      "drive.amazon.com",
                      "amazon.ca",
                      "amazon.in",
                      "amazon.co.uk"
                    ]
                  }
                }
              }
            ],
            "count": 1
          }
        }
      }
    }
  ]
}
Request Example with Response using Config ID
POST 'https://
<tenant-URL>
/api/v1/steeringconfig?config_id=2
{    
    "token": "f32a973eddd7bc1602fc0f48dc0a"
}
{
  status: "success",
  msg: "",
  data: [
    {
      steering_config: "web",
      enabled: true,
      location_based_steering: false,
      private_apps_enabled: false,
      priority: "1",
      traffic_type: "web",
      steered_traffic: {
        data: [
        ],
        count: 0
      },
      exceptions: {
        categories: {
          data: [
            {
              categories: [
                "Adult Content - Other",
                "Advocacy Groups & Trade Associations"
              ],
              notes: "bypass categories"
            }
          ],
          count: 1
        },
        domains: {
          data: [
            {
              domains: [
              ],
              notes: null
            },
            {
              domains: [
                "www.facebook.com",
                "www.google.com"
              ],
              notes: "bypass google and facebook"
            }
          ],
          count: 2
        },
        src_netloc: {
          data: [
            {
              notes: "bypass source locations",
              src_netloc: [
                "Any network 2",
                "Lab Subnet"
              ]
            }
          ],
          count: 1
        },
        dst_netloc: {
          data: [
            {
              notes: "default destination location",
              dst_netloc: [
                "Local IP address range"
              ]
            },
            {
              notes: "bypass destination locations",
              dst_netloc: [
                "162.16.192.65-range OUTside",
                "nw_location"
              ]
            }
          ],
          count: 2
        },
        countries: {
          data: [
            {
              notes: "bypass traffic from these countries",
              countries: [
                "Andorra",
                "American Samoa"
              ]
            }
          ],
          count: 1
        },
        cert_pinned_apps: {
          data: [
            {
              notes: "default ssl pinned app",
              app_name: "Amazon CloudDrive",
              enabled: true,
              data: {
                custom: false,
                appName: "Amazon CloudDrive",
                android: {
                  action: "1",
                  processes: [
                    "com.amazon.clouddrive",
                    "com.amazon.clouddrive"
                  ],
                  enabled: true,
                  domains: [
                    "drive.amazonaws.com",
    "us-east-1.amazonaws.com",
    "us-west-2.amazonaws.com",
    "drive.amazon.com",
    "amazon.ca",
    "amazon.in",
                    "amazon.co.uk"
                  ]
                },
                mac: {
                  action: "1",
                  processes: [
                    "Amazon Cloud Dr",
                    "Amazon Cloud Drive Sync Service",
                    "Amazon Cloud Drive"
                  ],
                  enabled: true,
                  managed_device: false,
                  tunnel: false,
                  tunnel_domains: [
                  ]
                },
                windows: {
                  action: "1",
                  processes: [
                    "AmazonCloudDriveW.exe",
                    "AmazonCloudDrive.exe"
                  ],
                  enabled: true,
                  managed_device: false,
                  tunnel: false,
                  tunnel_domains: [
                  ]
                },
                ios: {
                  action: "1",
                  processes: [
                  ],
                  enabled: false,
                  domains: [
                    "drive.amazonaws.com",
    "us-east-1.amazonaws.com",
    "us-west-2.amazonaws.com",
    "drive.amazon.com",
    "amazon.ca",
    "amazon.in",
                    "amazon.co.uk"
                  ]
                }
              }
            },
            {
              notes: "default ssl pinned app",
              app_name: "Ablaze",
              enabled: true,
              data: {
                custom: false,
                appName: "Adrenalin",
                windows: {
                  action: "1",
                  processes: [
                    "Adrnln.exe"
                  ],
                  enabled: true,
                  managed_device: false,
                  tunnel: false,
                  tunnel_domains: [
                  ]
                },
                mac: {
                  action: "1",
                  managed_device: false,
                  tunnel: false,
                  tunnel_domains: [
                  ],
                  processes: [
                  ],
                  enabled: false,
                  domains: [
                    "adrenalin.com"
                  ]
                },
                android: {
                  action: "1",
                  processes: [
                  ],
                  enabled: false,
                  domains: [
                    "adrenalin.com"
                  ]
                },
                ios: {
                  action: "1",
                  processes: [
                  ],
                  enabled: false,
                  domains: [
                    "adrenalin.com"
                  ]
                }
              }
            }
          ],
          count: 2
        }
      }
    }
  ]
}
In this Topic
Get Steering Configuration Information

---
## Network Steering
**URL:** https://docs.netskope.com/en/network-steering/
**Last Modified:** 2026-06-25T17:39:25+00:00
**Scraped:** 2026-06-28T09:07:50.058420+00:00

Network Steering - Netskope Knowledge Portal
Network Steering
The Network Steering page provides information about all the Internet Protocol Security (IPSec) and Generic Routing Encapsulation (GRE) tunnels in your infrastructure. This includes the following information:
Currently connected POP per tunnel
: See where traffic is flowing.
Tunnel status
: See whether the tunnel is up or down.
Tunnel Throughput
: The volume of traffic that is going through each tunnel.
Tunnel Configured State
: If the tunnel is configured in the Netskope UI.
Tunnel Flow Count
: The number of flows that are being seen per tunnel.
Tunnel Endpoint Count
: The number of endpoints that are seen per tunnel.
Netskope Service Status
: The current state of the Netskope Service.
These tunnels steer HTTP and HTTPS traffic from SaaS apps to the Netskope cloud. To learn more about IPSec and GRE, see
IPSec
and
GRE
.
Filter Menu
You can use the filter menu to make filter selections.
Tunnel Type
: Filter the tunnel type by selecting this filter.
GRE Tunnel Site Name
: Filter by GRE site name.
IPSec Tunnel Site Name
: Filter by tunnel site name.
Event Timestamp
: You can use this filter to view the activities that occurred within a specific time range.
Refresh Button
: Click this button to apply your filter selections and refresh the data that is displayed on the page.
Hide Filters Icon
: Click the hide filters icon to hide the filter menu.
Ellipsis Icon
: Click the ellipsis icon to view the following additional dashboard options:
Clear Cache and Refresh
: Clicking this button will clear the cache and cause the page to refresh.
Reset Filters Button
: Clicking this button will cause the filters to reset to the default settings.
Time Zone Dashboard
: You can use this dashboard to change the time zone.
The Merged Results feature displays a maximum of 5,000 rows of data for each of the merged queries. If you include queries that return more than 5,000 rows of data, only the first 5,000 rows that are returned will be included in the merged results.
You must click the refresh
icon to apply your filter selections.
Global Tunnel Map
The Global Tunnel Map displays all the IPSec and GRE tunnels in your network. Using the map, you can immediately see the number of tunnels in any geographic region. Each green circle indicates the Netskope POP to which the tenant sends IPSec or GRE traffic. Larger circles indicate a greater number of unique tunnels sending traffic to the specific POP. When you mouse over the green circles, you can see the name of the POP to which the tunnel is sending traffic, and the number of unique tunnels.
IPSec Tunnel Details
The IPSec Tunnel Details widget displays the near real-time status and throughput of all IPSec tunnels configured to send traffic for the tenant. The widget displays the timestamp for when the UP or DOWN tunnel event was observed.
Source Identity
: The IKE identifier on the router that originates the tunnel. For example, 1.1.1.1., sourcelocation.company.com, or sourcelocation@company.com.
Source IP
: The public source IP Address of the IPSec Tunnel, indicating the source seen by the Netskope Service.
POP Name
: The Point of Presence (POP) where the tunnel terminates.
Tunnel Status
: The status of the tunnel.
Throughput
: The volume of traffic observed through the IPSec tunnel per second which is computed by analyzing the traffic flowing in a tunnel on a per minute basis.
Configured State
: The status of the tunnel that indicates whether it is Enabled or Disabled in the Netskope UI.
Event Timestamp
: The time of the last tunnel status change.
Timestamp For Last Seen Flow Count
: The time when the last active flow count (in the “Flow Count Last Seen” column) was seen.
Flow Count Last Seen
: The number of active flows seen for each IPSec Tunnel on a per minute basis.
Netskope Service Status
:The status of the Netskope Service at the POP where the tunnel is terminated.
IPSec Tunnel Status
The IPSec Tunnel Status widget displays the historical status of all IPSec tunnels configured to send traffic for the tenant. The tunnel status display will show any changes in the status of a tunnel over a period of time. The status changes based on the tunnel being up or down.
IPSec Tunnel Active Flow Count
The IPSec Tunnel Active Flow Count widget displays the number of active flows seen in a tunnel every minute. This active flow count is displayed as a time series view to show the change in activity in a tunnel over a period of time. By default, it will show the Flow Count for all tunnels unless filtered above in the “IPSec Tunnel Name” Drop down.
IPSec Tunnel Active Endpoint Count
The IPSec Tunnel Active Endpoint Count widget displays the number of unique devices that connect over a tunnel every minute.
IPSec Tunnel Throughput Widget
The IPSEC Tunnel Throughput Widget displays the throughput of every configured IPSec tunnel where traffic is seen. The IPSec Tunnel Throughput is displayed as a time series view to show the change in throughput in an IPSec tunnel over a period of time. This throughput is displayed in Megabits per second (Mbps). By default, it will show the throughput for all IPSec tunnels unless filtered in the “IPSec Tunnel Name” dropdown.
GRE Tunnel Details
The GRE Tunnel Details widget displays the near real-time status and throughput of all GRE tunnels configured to send traffic for the tenant. The widget displays the timestamp for when the UP or DOWN tunnel event was observed. The tunnel status is shown as UNKNOWN when no traffic is detected through the tunnel. The widget also displays the status and timestamp for when the last keep alive event was observed.
Tunnel Name
: The name of the tunnel.
Source IP
: The source IP Address of the GRE Tunnel.
POP Name
: The Point of Presence (POP) where the tunnel terminates.
Tunnel Status
: The status of the tunnel.
Throughput
: The volume of traffic observed through the GRE tunnel per second which is computed by analyzing the traffic flowing in a tunnel on a per minute basis.
Configured State
: The status of the tunnel that indicates whether it is Enabled or Disabled in the Netskope UI.
Event Timestamp
: The time of the last GRE tunnel status change.
KeepAlive Status
: Indicates whether the Netskope Service has received a keepalive from the respective tunnel.
KeepAlive Last Seen Time
: The most recent time the Netskope Service has seen a keepalive from the GRE tunnel.
Timestamp for Last Seen Flow Count
: The time when the last active flow count (in the “Flow Count Last Seen” column) was seen.
Last Seen Flow Count
:The number of active flows seen for each GRE Tunnel on a per minute basis.
Netskope Service Status
:The status of the Netskope Service at the POP where the GRE tunnel is terminated.
GRE Tunnel Status
The GRE Tunnel Status widget displays the historical status of all GRE tunnels configured to send traffic for the tenant. The tunnel status display will show any changes in the status of a tunnel over a period of time. The status changes based on the tunnel being up or down.
GRE Tunnel Active Flow Count
The GRE Tunnel Active Flow Count widget displays the number of active flows seen in a GRE tunnel every minute. This active flow count is displayed as a time series view to show the change in activity in a GRE tunnel over a period of time. By default, it will show the Flow Count for all GRE tunnels unless filtered in the “GRE Tunnel Name” dropdown.
GRE Tunnel Active Endpoint Count
The GRE Tunnel Active Endpoint Count widget displays the number of unique devices that connect over a GRE tunnel every minute. This active endpoint count is displayed as a time series view to show the change in activity in a GRE tunnel over a period of time. By default, it will show the Endpoint Count for all GRE tunnels unless filtered above in the “GRE Tunnel Name” dropdown.
GRE Tunnel Throughput Widget
The Tunnel Throughput Widget displays the throughput of every configured GRE tunnel where traffic is seen. The GRE Tunnel Throughput is displayed as a time series view to show the change in throughput in a GRE tunnel over a period of time. This throughput is displayed in Megabits per second (Mbps). By default, it will show the throughput for all GRE tunnels unless filtered above in the “GRE Tunnel Name” dropdown.
In this Topic
Network Steering

---
## Additional Network Configurations
**URL:** https://docs.netskope.com/en/additional-network-configurations/
**Last Modified:** 2025-08-31T01:43:24+00:00
**Scraped:** 2026-06-28T09:08:56.042158+00:00

Additional Network Configurations - Netskope Knowledge Portal
Additional Network Configurations
The default network configuration described previously is for a single interface deployment, where all production and management traffic flow over a single 10GbE interface (single-arm mode). However, you can segregate the management traffic from production traffic by configuring a management interface.
You can use the dedicated management interface as a secondary path for accessing the system over SSH and other ancillary services. You can also create a redundant inbound interface by bonding the management appliance to the inbound logical interface, or create an outbound interface.
Configure the Management Interface
To configure the management interface:
Access the appliance console using ssh. Log in with the credentials
nsadmin/nsappliance
.
To go into configuration mode, enter
configure
:
configure
Entering configuration mode
Set the management interface on the appliance by entering these commands:
set interface inbound ip
<IP address>
set interface inbound gw
<gateway address>
set interface inbound netmask
<subnet mask>
Note
Make sure the management interface is on a separate subnet than the data-bearing interface. The nsshell does not enforce this requirement and unexpected results may occur if both interfaces are on the same subnet .
To review your entries, enter
show interface
.
Enter
save
and wait for the prompt to return.
Enter
exit
to leave the config mode.
Enter
exit
to leave the management plane console.
Important
Make sure the management interface is on a separate subnet than the data-bearing interface. The nsshell does not enforce this requirement and unexpected results may occur if both interfaces are on the same subnet.
Configure Inbound Interface Bonding
You can configure physical redundancy for the inbound interface by designating the physical management port as a secondary port for the inbound logical interface.
To configure inbound interface bonding:
Access the appliance using ssh.
Log in to the appliance using the
nsadmin/nsappliance
credentials.
Enter
configure
to enter the nsshell configure mode.
Enter
set interface inbound enable-bonding true
Enter
show interface
to check your work.
Enter
save
to activate your changes.
Enter
exit
to leave the configure mode.
Enter
exit
to leave the nsshell and exit the appliance console.
Configure Network Destinations per Interface
You can route DNS, SNMP, and RADIUS traffic destined for a specific server IP or network to the inbound or management plane of an appliance.
To configure network destinations per interface:
Access the appliance using ssh.
Log in to the appliance using the
nsadmin/nsappliance
credentials.
Enter
configure
to enter the nsshell configure mode.
Enter
add interface management destination-networks
.
Enter
set interface management destination-networks 0 network
IP address
.
Enter
show interface management
, which should return:
{
  "gw": "
<gateway>
",
  "ip": "
<IP address>
",
  "netmask": "
<subnet>
",
  "destination-networks": [
    {
      "network": "
<management IP address>
"
    }
  ]
}
Enter
save
to activate your changes.
Enter
exit
to leave the configure mode.
Enter
exit
to leave the nsshell and exit the appliance console.
Configure an Outbound Interface
You can configure an appliance so that all connections to external servers initiated by services running are shown on one interface.
To configure an outbound interface:
Access the appliance console using ssh.
Log in to the appliance using the
nsadmin/nsappliance
credentials.
Enter
configure
to enter the nsshell configure mode.
Enter these commands:
set interface outbound ip
<IP address>
set interface outbound gw
<Gateway IP>
set interface outbound netmask
<Netmask>
Enter
save
to activate your changes.
Enter
exit
to leave the configure mode.
Enter
exit
to leave the nsshell and exit the appliance console.
View the Status of the Interfaces
You can view the status of the network interfaces by running the following command in operation mode.
snmpwalk -v 2c -c appliancecom <
appliance-IP
>
The IF-MIB provides details about all the interfaces. In the output, the network interfaces eth0, eth4, and eth5 are connected to the appliance interfaces mp, inbound, and outbound. The appliance interface mp connects to eth0, inbound connects to eth5, and outbound connects to eth4.
Sample Output
The following is a sample output that shows the index value, type, physical address, admin status, operation status and so on.
SNMPv2-MIB::sysDescr.0 = STRING: Linux lcsnmp 4.4.0-141-generic #167-Ubuntu SMP Wed Dec 5 10:40:15 UTC 2018 x86_64
SNMPv2-MIB::sysObjectID.0 = OID: SNMPv2-SMI::enterprises.48007
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (2058) 0:00:20.58
SNMPv2-MIB::sysContact.0 = STRING: nauman@netskope.com
SNMPv2-MIB::sysName.0 = STRING: "securecloud"
SNMPv2-MIB::sysLocation.0 = STRING: "hq"
IF-MIB::ifNumber.0 = INTEGER: 14
IF-MIB::ifIndex.1 = INTEGER: 1
IF-MIB::ifIndex.2 = INTEGER: 2
IF-MIB::ifIndex.3 = INTEGER: 3
IF-MIB::ifIndex.4 = INTEGER: 4
IF-MIB::ifIndex.5 = INTEGER: 5
IF-MIB::ifIndex.6 = INTEGER: 6
IF-MIB::ifIndex.7 = INTEGER: 7
IF-MIB::ifIndex.8 = INTEGER: 8
IF-MIB::ifIndex.435 = INTEGER: 435
IF-MIB::ifIndex.437 = INTEGER: 437
IF-MIB::ifIndex.439 = INTEGER: 439
IF-MIB::ifIndex.441 = INTEGER: 441
IF-MIB::ifIndex.445 = INTEGER: 445
IF-MIB::ifIndex.447 = INTEGER: 447
IF-MIB::ifDescr.1 = STRING: lo
IF-MIB::ifDescr.2 = STRING: eth0
IF-MIB::ifDescr.3 = STRING: eth1
IF-MIB::ifDescr.4 = STRING: eth2
IF-MIB::ifDescr.5 = STRING: eth3
IF-MIB::ifDescr.6 = STRING: eth4
IF-MIB::ifDescr.7 = STRING: eth5
IF-MIB::ifDescr.8 = STRING: docker0
IF-MIB::ifDescr.435 = STRING: bond0
IF-MIB::ifDescr.437 = STRING: vethf288e04
IF-MIB::ifDescr.439 = STRING: vethae371bc
IF-MIB::ifDescr.441 = STRING: vethbef553b
IF-MIB::ifDescr.445 = STRING: veth2df6fc1
IF-MIB::ifDescr.447 = STRING: veth2fccd1c
IF-MIB::ifType.1 = INTEGER: softwareLoopback(24)
IF-MIB::ifType.2 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.3 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.4 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.5 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.6 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.7 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.8 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.435 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.437 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.439 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.441 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.445 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.447 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifMtu.1 = INTEGER: 65536
IF-MIB::ifMtu.2 = INTEGER: 1500
IF-MIB::ifMtu.3 = INTEGER: 1500
IF-MIB::ifMtu.4 = INTEGER: 1500
IF-MIB::ifMtu.5 = INTEGER: 1500
IF-MIB::ifMtu.6 = INTEGER: 1500
IF-MIB::ifMtu.7 = INTEGER: 1500
IF-MIB::ifMtu.8 = INTEGER: 1500
IF-MIB::ifMtu.435 = INTEGER: 1500
IF-MIB::ifMtu.437 = INTEGER: 1500
IF-MIB::ifMtu.439 = INTEGER: 1500
IF-MIB::ifMtu.441 = INTEGER: 1500
IF-MIB::ifMtu.445 = INTEGER: 1500
IF-MIB::ifMtu.447 = INTEGER: 1500
IF-MIB::ifSpeed.1 = Gauge32: 10000000
IF-MIB::ifSpeed.2 = Gauge32: 1000000000
IF-MIB::ifSpeed.3 = Gauge32: 1000000000
IF-MIB::ifSpeed.4 = Gauge32: 1000000000
IF-MIB::ifSpeed.5 = Gauge32: 0
IF-MIB::ifSpeed.6 = Gauge32: 4294967295
IF-MIB::ifSpeed.7 = Gauge32: 4294967295
IF-MIB::ifSpeed.8 = Gauge32: 0
IF-MIB::ifSpeed.435 = Gauge32: 4294967295
IF-MIB::ifSpeed.437 = Gauge32: 4294967295
IF-MIB::ifSpeed.439 = Gauge32: 4294967295
IF-MIB::ifSpeed.441 = Gauge32: 4294967295
IF-MIB::ifSpeed.445 = Gauge32: 4294967295
IF-MIB::ifSpeed.447 = Gauge32: 4294967295
IF-MIB::ifPhysAddress.1 = STRING:
IF-MIB::ifPhysAddress.2 = STRING: 0:1e:67:bc:1e:b0
IF-MIB::ifPhysAddress.3 = STRING: 0:1e:67:bc:1e:b1
IF-MIB::ifPhysAddress.4 = STRING: 0:1e:67:bc:1e:b2
IF-MIB::ifPhysAddress.5 = STRING: 0:1e:67:bc:1e:b3
IF-MIB::ifPhysAddress.6 = STRING: 0:e0:ed:52:88:4e
IF-MIB::ifPhysAddress.7 = STRING: 0:e0:ed:52:88:4f
IF-MIB::ifPhysAddress.8 = STRING: 2:42:ee:f5:18:33
IF-MIB::ifPhysAddress.435 = STRING: 0:e0:ed:52:88:4f
IF-MIB::ifPhysAddress.437 = STRING: e6:6e:50:4a:f9:c3
IF-MIB::ifPhysAddress.439 = STRING: a:52:ad:5f:b3:a7
IF-MIB::ifPhysAddress.441 = STRING: 6a:9e:e9:5c:a6:72
IF-MIB::ifPhysAddress.445 = STRING: 52:d6:2b:b8:c5:3b
IF-MIB::ifPhysAddress.447 = STRING: c2:9:d8:83:2b:a9
IF-MIB::ifAdminStatus.1 = INTEGER: up(1)
IF-MIB::ifAdminStatus.2 = INTEGER: up(1)
IF-MIB::ifAdminStatus.3 = INTEGER: down(2)
IF-MIB::ifAdminStatus.4 = INTEGER: up(1)
IF-MIB::ifAdminStatus.5 = INTEGER: down(2)
IF-MIB::ifAdminStatus.6 = INTEGER: up(1)
IF-MIB::ifAdminStatus.7 = INTEGER: up(1)
IF-MIB::ifAdminStatus.8 = INTEGER: up(1)
IF-MIB::ifAdminStatus.435 = INTEGER: up(1)
IF-MIB::ifAdminStatus.437 = INTEGER: up(1)
IF-MIB::ifAdminStatus.439 = INTEGER: up(1)
IF-MIB::ifAdminStatus.441 = INTEGER: up(1)
IF-MIB::ifAdminStatus.445 = INTEGER: up(1)
IF-MIB::ifAdminStatus.447 = INTEGER: up(1)
IF-MIB::ifOperStatus.1 = INTEGER: up(1)
IF-MIB::ifOperStatus.2 = INTEGER: up(1)
IF-MIB::ifOperStatus.3 = INTEGER: down(2)
IF-MIB::ifOperStatus.4 = INTEGER: up(1)
IF-MIB::ifOperStatus.5 = INTEGER: down(2)
IF-MIB::ifOperStatus.6 = INTEGER: up(1)
IF-MIB::ifOperStatus.7 = INTEGER: up(1)
IF-MIB::ifOperStatus.8 = INTEGER: up(1)
IF-MIB::ifOperStatus.435 = INTEGER: up(1)
IF-MIB::ifOperStatus.437 = INTEGER: up(1)
IF-MIB::ifOperStatus.439 = INTEGER: up(1)
IF-MIB::ifOperStatus.441 = INTEGER: up(1)
IF-MIB::ifOperStatus.445 = INTEGER: up(1)
IF-MIB::ifOperStatus.447 = INTEGER: up(1)
IF-MIB::ifLastChange.1 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.2 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.3 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.4 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.5 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.6 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.7 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.8 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.435 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.437 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.439 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.441 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.445 = Timeticks: (0) 0:00:00.00
IF-MIB::ifLastChange.447 = Timeticks: (0) 0:00:00.00
IF-MIB::ifInOctets.1 = Counter32: 450968667
IF-MIB::ifInOctets.2 = Counter32: 236332
IF-MIB::ifInOctets.3 = Counter32: 0
IF-MIB::ifInOctets.4 = Counter32: 737746681
IF-MIB::ifInOctets.5 = Counter32: 0
IF-MIB::ifInOctets.6 = Counter32: 114969261
IF-MIB::ifInOctets.7 = Counter32: 3913275716
IF-MIB::ifInOctets.8 = Counter32: 41464012
IF-MIB::ifInOctets.435 = Counter32: 431052
IF-MIB::ifInOctets.437 = Counter32: 46237
IF-MIB::ifInOctets.439 = Counter32: 1983432
IF-MIB::ifInOctets.441 = Counter32: 369579
IF-MIB::ifInOctets.445 = Counter32: 3429165
IF-MIB::ifInOctets.447 = Counter32: 161
IF-MIB::ifInUcastPkts.1 = Counter32: 4919465
IF-MIB::ifInUcastPkts.2 = Counter32: 4277256647
IF-MIB::ifInUcastPkts.3 = Counter32: 0
IF-MIB::ifInUcastPkts.4 = Counter32: 90857908
IF-MIB::ifInUcastPkts.5 = Counter32: 0
IF-MIB::ifInUcastPkts.6 = Counter32: 772091
IF-MIB::ifInUcastPkts.7 = Counter32: 8032797
IF-MIB::ifInUcastPkts.8 = Counter32: 376167
IF-MIB::ifInUcastPkts.435 = Counter32: 4277258742
IF-MIB::ifInUcastPkts.437 = Counter32: 616
IF-MIB::ifInUcastPkts.439 = Counter32: 14723
IF-MIB::ifInUcastPkts.441 = Counter32: 1754
IF-MIB::ifInUcastPkts.445 = Counter32: 28438
IF-MIB::ifInUcastPkts.447 = Counter32: 3
IF-MIB::ifInNUcastPkts.1 = Counter32: 0
IF-MIB::ifInNUcastPkts.2 = Counter32: 17714528
IF-MIB::ifInNUcastPkts.3 = Counter32: 0
IF-MIB::ifInNUcastPkts.4 = Counter32: 19679284
IF-MIB::ifInNUcastPkts.5 = Counter32: 0
IF-MIB::ifInNUcastPkts.6 = Counter32: 31018
IF-MIB::ifInNUcastPkts.7 = Counter32: 43244
IF-MIB::ifInNUcastPkts.8 = Counter32: 0
IF-MIB::ifInNUcastPkts.435 = Counter32: 17714528
IF-MIB::ifInNUcastPkts.437 = Counter32: 0
IF-MIB::ifInNUcastPkts.439 = Counter32: 0
IF-MIB::ifInNUcastPkts.441 = Counter32: 0
IF-MIB::ifInNUcastPkts.445 = Counter32: 0
IF-MIB::ifInNUcastPkts.447 = Counter32: 0
IF-MIB::ifInDiscards.1 = Counter32: 0
IF-MIB::ifInDiscards.2 = Counter32: 3869
IF-MIB::ifInDiscards.3 = Counter32: 0
IF-MIB::ifInDiscards.4 = Counter32: 129774
IF-MIB::ifInDiscards.5 = Counter32: 0
IF-MIB::ifInDiscards.6 = Counter32: 1953
IF-MIB::ifInDiscards.7 = Counter32: 2021
IF-MIB::ifInDiscards.8 = Counter32: 0
IF-MIB::ifInDiscards.435 = Counter32: 3891
IF-MIB::ifInDiscards.437 = Counter32: 0
IF-MIB::ifInDiscards.439 = Counter32: 0
IF-MIB::ifInDiscards.441 = Counter32: 0
IF-MIB::ifInDiscards.445 = Counter32: 0
IF-MIB::ifInDiscards.447 = Counter32: 0
IF-MIB::ifInErrors.1 = Counter32: 0
IF-MIB::ifInErrors.2 = Counter32: 0
IF-MIB::ifInErrors.3 = Counter32: 0
IF-MIB::ifInErrors.4 = Counter32: 0
IF-MIB::ifInErrors.5 = Counter32: 0
IF-MIB::ifInErrors.6 = Counter32: 0
IF-MIB::ifInErrors.7 = Counter32: 0
IF-MIB::ifInErrors.8 = Counter32: 0
IF-MIB::ifInErrors.435 = Counter32: 0
IF-MIB::ifInErrors.437 = Counter32: 0
IF-MIB::ifInErrors.439 = Counter32: 0
IF-MIB::ifInErrors.441 = Counter32: 0
IF-MIB::ifInErrors.445 = Counter32: 0
IF-MIB::ifInErrors.447 = Counter32: 0
IF-MIB::ifInUnknownProtos.1 = Counter32: 0
IF-MIB::ifInUnknownProtos.2 = Counter32: 0
IF-MIB::ifInUnknownProtos.3 = Counter32: 0
IF-MIB::ifInUnknownProtos.4 = Counter32: 0
IF-MIB::ifInUnknownProtos.5 = Counter32: 0
IF-MIB::ifInUnknownProtos.6 = Counter32: 0
IF-MIB::ifInUnknownProtos.7 = Counter32: 0
IF-MIB::ifInUnknownProtos.8 = Counter32: 0
IF-MIB::ifInUnknownProtos.435 = Counter32: 0
IF-MIB::ifInUnknownProtos.437 = Counter32: 0
IF-MIB::ifInUnknownProtos.439 = Counter32: 0
IF-MIB::ifInUnknownProtos.441 = Counter32: 0
IF-MIB::ifInUnknownProtos.445 = Counter32: 0
IF-MIB::ifInUnknownProtos.447 = Counter32: 0
IF-MIB::ifOutOctets.1 = Counter32: 450969766
IF-MIB::ifOutOctets.2 = Counter32: 126
IF-MIB::ifOutOctets.3 = Counter32: 0
IF-MIB::ifOutOctets.4 = Counter32: 0
IF-MIB::ifOutOctets.5 = Counter32: 0
IF-MIB::ifOutOctets.6 = Counter32: 13525764
IF-MIB::ifOutOctets.7 = Counter32: 1342618225
IF-MIB::ifOutOctets.8 = Counter32: 212431135
IF-MIB::ifOutOctets.435 = Counter32: 186482
IF-MIB::ifOutOctets.437 = Counter32: 44233
IF-MIB::ifOutOctets.439 = Counter32: 3436917
IF-MIB::ifOutOctets.441 = Counter32: 367769
IF-MIB::ifOutOctets.445 = Counter32: 1994437
IF-MIB::ifOutOctets.447 = Counter32: 460
IF-MIB::ifOutUcastPkts.1 = Counter32: 4919477
IF-MIB::ifOutUcastPkts.2 = Counter32: 3
IF-MIB::ifOutUcastPkts.3 = Counter32: 0
IF-MIB::ifOutUcastPkts.4 = Counter32: 0
IF-MIB::ifOutUcastPkts.5 = Counter32: 0
IF-MIB::ifOutUcastPkts.6 = Counter32: 322042
IF-MIB::ifOutUcastPkts.7 = Counter32: 7073820
IF-MIB::ifOutUcastPkts.8 = Counter32: 406501
IF-MIB::ifOutUcastPkts.435 = Counter32: 1350
IF-MIB::ifOutUcastPkts.437 = Counter32: 623
IF-MIB::ifOutUcastPkts.439 = Counter32: 28469
IF-MIB::ifOutUcastPkts.441 = Counter32: 2070
IF-MIB::ifOutUcastPkts.445 = Counter32: 14864
IF-MIB::ifOutUcastPkts.447 = Counter32: 10
IF-MIB::ifOutNUcastPkts.1 = Counter32: 0
IF-MIB::ifOutNUcastPkts.2 = Counter32: 0
IF-MIB::ifOutNUcastPkts.3 = Counter32: 0
IF-MIB::ifOutNUcastPkts.4 = Counter32: 0
IF-MIB::ifOutNUcastPkts.5 = Counter32: 0
IF-MIB::ifOutNUcastPkts.6 = Counter32: 0
IF-MIB::ifOutNUcastPkts.7 = Counter32: 0
IF-MIB::ifOutNUcastPkts.8 = Counter32: 0
IF-MIB::ifOutNUcastPkts.435 = Counter32: 0
IF-MIB::ifOutNUcastPkts.437 = Counter32: 0
IF-MIB::ifOutNUcastPkts.439 = Counter32: 0
IF-MIB::ifOutNUcastPkts.441 = Counter32: 0
IF-MIB::ifOutNUcastPkts.445 = Counter32: 0
IF-MIB::ifOutNUcastPkts.447 = Counter32: 0
IF-MIB::ifOutDiscards.1 = Counter32: 0
IF-MIB::ifOutDiscards.2 = Counter32: 0
IF-MIB::ifOutDiscards.3 = Counter32: 0
IF-MIB::ifOutDiscards.4 = Counter32: 0
IF-MIB::ifOutDiscards.5 = Counter32: 0
IF-MIB::ifOutDiscards.6 = Counter32: 0
IF-MIB::ifOutDiscards.7 = Counter32: 0
IF-MIB::ifOutDiscards.8 = Counter32: 0
IF-MIB::ifOutDiscards.435 = Counter32: 0
IF-MIB::ifOutDiscards.437 = Counter32: 0
IF-MIB::ifOutDiscards.439 = Counter32: 0
IF-MIB::ifOutDiscards.441 = Counter32: 0
IF-MIB::ifOutDiscards.445 = Counter32: 0
IF-MIB::ifOutDiscards.447 = Counter32: 0
IF-MIB::ifOutErrors.1 = Counter32: 0
IF-MIB::ifOutErrors.2 = Counter32: 0
IF-MIB::ifOutErrors.3 = Counter32: 0
IF-MIB::ifOutErrors.4 = Counter32: 0
IF-MIB::ifOutErrors.5 = Counter32: 0
IF-MIB::ifOutErrors.6 = Counter32: 0
IF-MIB::ifOutErrors.7 = Counter32: 0
IF-MIB::ifOutErrors.8 = Counter32: 0
IF-MIB::ifOutErrors.435 = Counter32: 0
IF-MIB::ifOutErrors.437 = Counter32: 0
IF-MIB::ifOutErrors.439 = Counter32: 0
IF-MIB::ifOutErrors.441 = Counter32: 0
IF-MIB::ifOutErrors.445 = Counter32: 0
IF-MIB::ifOutErrors.447 = Counter32: 0
IF-MIB::ifOutQLen.1 = Gauge32: 0
IF-MIB::ifOutQLen.2 = Gauge32: 0
IF-MIB::ifOutQLen.3 = Gauge32: 0
IF-MIB::ifOutQLen.4 = Gauge32: 0
IF-MIB::ifOutQLen.5 = Gauge32: 0
IF-MIB::ifOutQLen.6 = Gauge32: 0
IF-MIB::ifOutQLen.7 = Gauge32: 0
IF-MIB::ifOutQLen.8 = Gauge32: 0
IF-MIB::ifOutQLen.435 = Gauge32: 0
IF-MIB::ifOutQLen.437 = Gauge32: 0
IF-MIB::ifOutQLen.439 = Gauge32: 0
IF-MIB::ifOutQLen.441 = Gauge32: 0
IF-MIB::ifOutQLen.445 = Gauge32: 0
IF-MIB::ifOutQLen.447 = Gauge32: 0
IF-MIB::ifSpecific.1 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.2 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.3 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.4 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.5 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.6 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.7 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.8 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.435 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.437 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.439 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.441 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.445 = OID: SNMPv2-SMI::zeroDotZero
IF-MIB::ifSpecific.447 = OID: SNMPv2-SMI::zeroDotZero
In the the sample output you can check that the eth0 interface as up and running based on the status of
ifAdminStatus.2
and
ifOperStatus.2
.
IF-MIB::ifIndex.2 = INTEGER: 2
IF-MIB::ifDescr.2 = STRING: eth0
IF-MIB::ifPhysAddress.2 = STRING: 0:1e:67:bc:1e:b0
IF-MIB::ifAdminStatus.2 = INTEGER: up(1)
IF-MIB::ifOperStatus.2 = INTEGER: up(1)
Configure an HTTP Proxy for the Management Plane
To configure an explicit HTTP proxy the management plane in the cloud, enter these commands:
set management-plane upstream-proxy-server hostname
<hostname or IP>
set management-plane upstream-proxy-server port
<port>
Make sure these services are allowed in the proxy:
https://config.
<tenant-domain>
:443
https://download.
<tenant-domain>
:443
https://messenger.
<tenant-domain>
:443
Configure a Serial Console Port
You can connect to the serial console port of an appliance to manage it using the command line interface (CLI). Connect the serial console using an RJ45 to USB or RJ45 to Serial cable. The RJ45 end of the cable goes into the serial port of the appliance, and the other end can be connected to a terminal server or a laptop directly. On a laptop, you can use putty on Windows or minicom on Linux to connect to the serial console. The settings to connect are:
Speed(baud):
115200
Data bits:
8
Stop bits:
1
Parity:
None
Flow Control:
XON/XOFF
In this Topic
Additional Network Configurations

---
## Configure Network Destinations per Interface
**URL:** https://docs.netskope.com/en/configure-network-destinations-per-interface/
**Last Modified:** 2025-08-31T01:42:57+00:00
**Scraped:** 2026-06-28T09:09:26.135067+00:00

Configure Network Destinations per Interface - Netskope Knowledge Portal
Configure Network Destinations per Interface
You can route DNS, SNMP, and RADIUS traffic destined for a specific server IP or network to the management plane of a virtual appliance.
To configure network destinations per interface:
Access the appliance using ssh.
Log in using the
nsadmin/nsappliance
credentials. An nsshell opens.
Enter the command
nsshell
.
Enter
configure
to enter the nsshell configure mode.
Enter
add interface mp destination-networks
.
Enter
set interface mp destination-networks 0 network
<IP address>
.
Enter
show interface mp
, which should return:
{
  "gw": "
<gateway>
",
  "ip": "
<IP address>
",
  "netmask": "
<subnet>
",
  "destination-networks": [
    {
      "network": "
<mp IP address>
"
    }
  ]
}
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
Configure Network Destinations per Interface

---
## Configure Palo Alto Networks Decrypt Mirror
**URL:** https://docs.netskope.com/en/configure-palo-alto-networks-decrypt-mirror/
**Last Modified:** 2025-08-31T01:43:30+00:00
**Scraped:** 2026-06-28T09:09:28.342976+00:00

Configure Palo Alto Networks Decrypt Mirror - Netskope Knowledge Portal
Configure Palo Alto Networks Decrypt Mirror
The Palo Alto Networks configuration is built upon objects that come together in a Policy. This section describes one possible configuration; under the assumption the device is already inspecting SSL traffic correctly. Please note that this configuration relies on a free license available for most PAN devices running PAN-OS 6.0 or later; and that you can either configure it directly on the device or via Panorama.
Create a Target Interface
Decrypted traffic will be mirrored to a dedicated interface on your Palo Alto Networks device, which needs to be of type Decrypt Mirror.
Create a Decryption Profile
Mirroring is configured at the Decryption Profile level under the Objects tab. You can use the Clone button to copy the profile you are currently using instead of modifying it directly.
When cloned, you can rename it appropriately. The critical configuration option is to select the interface you configured earlier in the Decryption Mirroring section. You can leave the default Forwarded Only option selected.
Create a Custom URL Category
You can create a custom URL Category for the traffic of interest by importing the file with the Managed Apps domains obtained from the Netskope UI into a new URL Category, in the Objects tab under Custom Objects > URL Category.
Create a Decryption Policy
In order to selectively mirror traffic, you can clone the existing Decryption policy and adjust it using the objects created previously.
Decryption policies are found under Decryption in the Policies tab. Using the Clone button you can create a copy of the exiting policy, and you can move it up with the Move UP button so it won’t be shadowed by the original policy
Finally, you can set the URL Category and Decryption Profile to those you created in the previous sections.
In this Topic
Configure Palo Alto Networks Decrypt Mirror

---
## EOL for the Secure Forwarder Steering Function
**URL:** https://docs.netskope.com/en/eol-for-the-secure-forwarder-steering-function-440153/
**Last Modified:** 2025-09-01T12:49:26+00:00
**Scraped:** 2026-06-28T09:10:00.551697+00:00

EOL for the Secure Forwarder Steering Function - Netskope Knowledge Portal
EOL for the Secure Forwarder Steering Function
Netskope announces the end-of-life and support for the Secure Forwarder steering function. The Secure Forwarder steering function will not be available on physical and virtual appliances effective October 31, 2023.
Netskope recommends that you migrate to other steering mechanisms that are suitable for your use case as outlined in Netskope’s Traffic Steering documentation. Please contact your Customer Success Manager to discuss your migration plans or for any guidance. We value your feedback and are happy to learn about your migration plan and provide assistance.
For the most current information, refer to:
End of Support for Secure Forwarder Steering Function
on our Support site.
In this Topic
EOL for the Secure Forwarder Steering Function

---
## Steer Traffic through the Appliance
**URL:** https://docs.netskope.com/en/steer-traffic-through-the-appliance-115992/
**Last Modified:** 2026-01-14T18:59:26+00:00
**Scraped:** 2026-06-28T09:10:46.496017+00:00

Steer Traffic through the Appliance - Netskope Knowledge Portal
Steer Traffic through the Appliance
The Dataplane On-Premises Virtual Appliance can integrate with the DNS servers or explicit proxy servers in your network to manage requests from client machines. Configure the virtual appliance in one of the following modes to steer the network traffic through the virtual appliance.
Explicit Proxy Mode
In this Topic
Steer Traffic through the Appliance

---
## EOL for the Secure Forwarder Steering Function
**URL:** https://docs.netskope.com/en/eol-for-the-secure-forwarder-steering-function-440154/
**Last Modified:** 2025-09-01T12:49:04+00:00
**Scraped:** 2026-06-28T09:11:42.998011+00:00

EOL for the Secure Forwarder Steering Function - Netskope Knowledge Portal
EOL for the Secure Forwarder Steering Function
Netskope announces the end-of-life and support for the Secure Forwarder steering function. The Secure Forwarder steering function will not be available on physical and virtual appliances effective October 31, 2023. After this date, all support services for the product are unavailable and the product becomes obsolete. Netskope Appliance version 103.0.0.338 is the last version to support the Secure Forwarder steering function.
Netskope recommends that you migrate to other steering mechanisms that are suitable for your use case as outlined in Netskope’s Traffic Steering documentation. Please contact your Customer Success Manager to discuss your migration plans or for any guidance. We value your feedback and are happy to learn about your migration plan and provide assistance.
For the most current information, refer to:
End of Support for Secure Forwarder Steering Function
on our Support site.
In this Topic
EOL for the Secure Forwarder Steering Function

---
## Allowing Unauthenticated Traffic from IP Addresses
**URL:** https://docs.netskope.com/en/allowing-unauthenticated-traffic-from-ip-addresses-1/
**Last Modified:** 2025-08-31T01:49:14+00:00
**Scraped:** 2026-06-28T09:13:24.191206+00:00

Allowing Unauthenticated Traffic from IP Addresses - Netskope Knowledge Portal
Allowing Unauthenticated Traffic from IP Addresses
For
Cloud Explicit Proxy
, you can configure an allowlist where you add any source egress IP addresses for your on-premises users. Netskope allow the traffic from the added user and IP address without authenticating.
To add an IP address to the Explicit Proxy allowlist:
Go to
Settings
>
Security Cloud Platform
>
Explicit Proxy
.
Under the
IP Address Allowlist & User Identity
section, click
Add IP Address
.
In
Add IP Address
:
Name
: Enter a name for the user and IP address you want to exempt from authenticating via Explicit Proxy.
IP Address
: Enter the source egress IP address for the user or office location you want to exempt from authenticating via Explicit Proxy. Netskope will allow the traffic from devices behind the IP address or CIDR. You can enter multiple IP addresses separated by a comma.
(Optional) Click
Add Another
to add multiple IP addresses separately.
Click
Add
.
In this Topic
Allowing Unauthenticated Traffic from IP Addresses

---
## Steering Configuration
**URL:** https://docs.netskope.com/en/steering-configuration/
**Last Modified:** 2026-03-17T09:43:06+00:00
**Scraped:** 2026-06-28T09:13:44.283709+00:00

Steering Configuration - Netskope Knowledge Portal
Steering Configuration
Steering Configurations control what kind of traffic gets steered to Netskope for real-time deep analysis and what kind of traffic gets bypassed. Moreover admins can configure a set of firewall apps to bypass processing using the Exceptions feature. It’s for endpoints using the Netskope Client and directs traffic from end users to the Netskope Cloud. A Netskope account steers thousands of apps by default, but to ensure the correct type of traffic is steered, you can modify the
default steering configuration
or create a new steering configuration. You can assign these configurations to either user groups or Organizational Units (OUs) for granular steering within your organization. Steering configurations apply to all platforms, but OU and Group settings are applied to the Netskope Client only.
When enabling
Dynamic Steering
on a Steering Configuration, the behavior of the “On-Premise” steering changes depending on the enablement of the “Flexible Dynamic Steering” backend option, starting from R112.
If Flexible Dynamic steering is enabled, Customers can configure the Steering Configuration to send “All Traffic” when the Netskope Client is “On-Premise”.
If Flexible Dynamic Steering is not enabled, Customers are not able to send “All Traffic” when the Netskope Client in “On Premise”. If the option to send “All Traffic” on the “On-Premise” Steering Configuration section is unavailable please contact support@netskope.com.
The Netskope Client offers comprehensive coverage when installed on managed devices and provides visibility and policy enforcement for devices that are both on- and off-premises (remote). The Netskope Client:
Performs posture checks to classify devices as managed or unmanaged based on admin-defined configurations.
Detects if a user is on-premises or remote and applies different steering configurations based on the location.
Provisions certificates to help with user identification when used with other traffic steering methods, such as GRE or IPSec.
Detects the presence of other traffic steering methods.
Generates user-facing notifications for security policy violations.
General Guidelines
When the Steering Configuration that applies to the Netskope Client is configured to steer “All Traffic”, the Netskope Client will be configured to steer the following traffic:
Port TCP 80 and 443, which will be sent directly to the Netskope Proxy
Any non-standard TCP port configured on the Steering Configuration under the “Non-Standard Ports” section for Web Traffic, which will be sent directly to the Netskope Proxy (remember that the traffic destined to those ports will not be inspected by Netskope Cloud Firewall, so ensure that the traffic sent to those ports is indeed web or proxied traffic, more info on
/en/creating-a-steering-configuration/
)
Any TCP and UDP port with the exception of default DNS and mDNS traffic (TCP/UDP 53 and UDP 5353). In order to steer and inspect DNS traffic a valid license for Netskope DNS Security, and a separate Steering Configuration option must be enabled, which goes beyond the scope of this document
When creating or editing steering configurations, consider the following:
When creating a custom steering configuration, you can enable Dynamic Steering, and the default exceptions are populated in both on- and off-premise steering configurations.
When editing the default steering configuration (i.e., Default tenant config), there is no restore defaults functionality, so you must create or remove exceptions in on- or off-premises mode based on where you left off before enabling Dynamic Steering.
If you’re editing a configuration that steers
All Traffic
, note the following:
When you enable Dynamic Steering, the off-premises configuration, which steers
All Traffic
by default, inherits the exceptions.
When you enable Dynamic Steering, the on-premises configuration, which steers
Cloud Apps Only
by default, doesn’t inherit the exceptions. Netskope assumes you create exceptions differently when a user is on-premises.
When you disable Dynamic Steering, Netskope preserves the steering configuration based on the traffic type.
If you’re editing a configuration that steers
Cloud Apps Only
, note the following:
When you enable Dynamic Steering, the on-premises configuration, which steers
Cloud Apps Only
by default, inherits the exceptions.
When you enable Dynamic Steering, the off-premises configuration, which is
All Traffic
by default, doesn’t inherit the exceptions. Netskope assumes you create exceptions differently when a user is off-premises.
When you disable Dynamic Steering, Netskope preserves the steering configuration based on the traffic type.
If Dynamic Steering is enabled on an existing Steering Configuration, all default exceptions are reinstated automatically. You need to reconfigure the exceptions according to your requirements after enabling Dynamic Steering.
Steering Exceptions
It is very important to understand that once the non-web traffic is steered to the Netskope Cloud and it reaches the Netskope Cloud Firewall, the latter ignores any Steering Exception defined in any Steering Configuration, with the exception of 2 Steering Exceptions types defined on the Default Steering Configuration (and only on the Default Steering Configuration):
Destination Locations – If the destination IP of the non-web traffic matches a Destination Location steering exception, the traffic is “bypassed” by the Netskope Cloud Firewall, so it will be egressing the Netskope Cloud bypassing any Policy evaluation
Application – If the non-web traffic matches a Custom Firewall Application defined as Application Steering Bypass (see
/en/creating-a-firewall-app-definition-449298/
), the traffic is “bypassed” by the Netskope Cloud Firewall, so it will be egressing the Netskope Cloud bypassing any Policy evaluation
It is possible to log the non-web traffic that is “bypassed” in the Cloud, please refer to
Configuring Cloud Firewall Steering Exceptions
.
About the Steering Configuration Page
On the Steering Configuration page (
Settings
>
Security Cloud Platform
>
Steering Configuration
), you can:
Choose whether all traffic steering configurations must apply to Organizational Units (OUs) or user groups. When configuring OUs and user groups, consider the following:
If a user is a member of multiple groups, the order placement of User Group steering configurations determines what’s used to resolve conflicts. The first group determines which group steering configuration Netskope uses when there is a group conflict. Conflict resolution is only applicable to User Groups.
In a multi-user deployment mode, if the logged in users belong to different OUs or user groups, the Netskope Client applies the steering configuration corresponding to the first logged in user.
Ensure all the users belong to a single OU or User Group for a multi-user machine.
For users in OUs or user groups that aren’t included in a custom steering configuration, Netskope applies the default steering configuration (i.e., Default tenant config). If you want to steer different types of traffic for different OUs or User Groups, create multiple custom steering configurations.
Choose whether you want to log bypassed traffic (i.e., steering exceptions) in Skope IT Events. This setting applies to all steering configurations.
– If you enabled dynamic steering and Netskope detects that the user is off-premises, Netskope client bypasses the traffic and doesn’t log it.
– If you bypassed traffic locally on the device, then the traffic won’t be sent to Netskope and logged in Skope IT events. You can only see logs for traffic bypassed in Netskope Cloud.
Manage how certain errors that Netskope observes in HTTP/HTTPS traffic are handled by blocking or bypassing them. To learn more:
Managing Error Settings
.
Choose the action taken when Netskope adds new predefined certificate pinned apps or updates to existing ones. To learn more:
Configuring the Steering Preferences
.
Search the steering configurations by a name, OU, or user group.
Create a new
steering configuration
.
View a list of steering configurations. For each configuration, you can see the OU or user group and the steering settings.
Click
to move the steering configuration. The steering configuration placed at the top takes priority over all other configurations.
Click
to choose one of the following options:
View Steered Items
: Click to go to the
Steered Traffic
tab where you can add applications and steer their traffic to Netskope for deep analysis via Real-time Protection policies. To learn more:
Adding Steered Items
.
View Exceptions
: Click to go to the
Exceptions
tab where you can add
exceptions
for the steering configuration and bypass the traffic from Netskope.
Edit Configuration
: Modify the steering configuration and its settings. To learn more:
Creating a Steering Configuration
.
Clone
: Create a copy of the steering configuration.
Disable
/
Enable
: Enable or disable the steering configuration. You can’t disable the
Default tenant config
.
Delete
: Delete the steering configuration. You can’t delete the
Default tenant config
.
Audit Logs for Steering Configuration
Navigate to
Audit Logs
under
Settings
>
Administration
to check logs for all intentional or accidental changes such as create, modify, or delete performed in Steering Configuration.
On the Audit Log page, click the
View Details
option and it displays
Audit Log Details
.
A few examples:
If you edit a few details in
Steering Configuration
, the
Audit Log Details
window displays:
When you create a new
Steering Configuration
:
When you delete an existing
Steering Configuration
:
In this Topic
Steering Configuration

---
## Netskope IPSec with F5 BIG-IP Local Traffic Manager
**URL:** https://docs.netskope.com/en/netskope-ipsec-with-f5-big-ip-local-traffic-manager/
**Last Modified:** 2025-08-31T01:55:25+00:00
**Scraped:** 2026-06-28T09:13:50.979993+00:00

Netskope IPSec with F5 BIG-IP Local Traffic Manager - Netskope Knowledge Portal
Netskope IPSec with F5 BIG-IP Local Traffic Manager
Netskope supports Internet Protocol Security (IPSec) tunnels as a traffic steering method. IPSec tunnels allow you to route web traffic (port 80 and 443) to Netskope using logical tunnel interfaces that terminate to a Netskope IPSec gateway. When you create IPSec tunnels in the Netskope UI, Netskope provides parameters for configuring the tunnels on your firewall.
This guide illustrates how to configure IPSec tunnels between Netskope and the F5 BIG-IP system running version 15.1.10.2 and using the 2-Arm deployment mode. To learn more about the CLI steps in F5 BIG-IP TMOS, see the
F5 Documentation
.
Following is an overview of the F5 BIG-IP Local Traffic Manager (LTM):
VLAN
external (interface 1.1/untagged)
internal (interface 1.2/untagged)
Subnet/Self IPs
external: 10.0.10.245/24
internal: 10.0.20.245/24
Routes: default (0.0.0.0/0): 10.0.10.1
Prerequisites
Before configuring IPSec, review the
Netskope guidelines
. On the F5 BIG-IP LTM:
Ensure F5 BIG-IP has the routes to reach the Netskope POPs.
Ensure Ports 500 and 4500 for UDP are allowed on the firewall.
Depending on your architecture, you might have to create a Forwarding IP Virtual Server on F5 BIG-IP LTM to receive the traffic from the internal segment.
Creating IPSec Tunnels in Netskope
To create the IPSec VPN tunnels for the F5 BIG-IP system in the Netskope UI, see
Creating an IPSec Site
.
Creating the Traffic Selector in F5 BIG-IP LTM
Go to
Network
>
IPsec
>
Traffic Selector
>
Create
.
Enter a name for the traffic selector.
In
Configuration
:
Source IP Address or CIDR
: Enter the source. This can be any IP address or subnet. In this example, it’s 10.0.20.0/24.
Source Port
: (Optional) Enter any source ports.
Destination IP Address or CIDR
: Enter the destination. This can be any IP address or subnet. In this example, it’s any (0.0.0.0/0).
Destination Port
: (Optional) Enter any destination ports. If you want to send only the web traffic to Netskope, you can set the destination port as 80 and then create another traffic selector with the destination port set to 443.
Protocol
: Choose the protocols you want to send through the IPSec tunnel. In this example, it’s
All Protocols
. If you want to send only web traffic to Netskope, choose
TCP
.
Direction
: Choose
Both
.
Action
: Use the default option.
IPsec Policy Name
: Click the
+
sign to create an IPSec policy. See the next section for the steps.
Creating the IPSec Policy
Enter a name for the IPSec policy.
In
Configuration
:
IPsec Protocol
: Choose
ESP
.
Mode
: Choose
Tunnel
.
Tunnel Local Address
: Enter the self IP address from which the IPSec tunnel will be created. Usually, it’s an RFC 1918 IP address; however, if a public IP is assigned as the self IP, then it’s the public IP.
Tunnel Remote Address
: Enter the IPSec Gateway IP address of the primary Netskope POP you copied in the Netskope UI.
In
IKE Phase 2
, configure the parameters below. To see a list of the Netskope supported IPSec parameters:
IPSec
.
Authentication Algorithm
: Choose
SHA-256
.
Encryption Algorithm
: Choose
AES-256
.
Perfect Forward Secrecy
: Choose
NONE
.
IPComp
: Choose
NONE
.
Lifetime
: Enter
1440
minutes.
KBLifetime
: Enter
0
kilobytes.
Click
Save
.
On the
Traffic Selector
page,  for the
IPsec Policy Name
, choose the IPSec policy you just created.
Click
Save
.
Creating the IKE Peer
TBD
Go to
Network
>
IPsec
>
IKE Peers
>
Create
.
Enter a name for the IKE Peer.
In
General Properties
:
Remote Address
: Enter the IPSec Gateway IP address of the primary Netskope POP you copied in the Netskope UI.
State
: Choose
Enabled
.
Version
: Choose
Version 2.
In
IKE Phase 1 Algorithms
, configure the parameters below. To see a list of the Netskope supported IPSec parameters:
IPSec
.
Authentication Algorithm
: Choose
SHA-256
.
Encryption Algorithm
: Choose
AES256
.
Pseudo-Random Function v2 only
: Choose
SHA-256
.
Perfect Forward Secrecy
: Netskope doesn’t support PFS in IKE Phase 1.
Lifetime
: Enter
1440
minutes.
In
IKE Phase 2 Credentials
:
Authentication Method
: Choose
Preshared Key
.
Preshared Key
: Enter the same pre-shared key you entered in the Netskope UI.
Verified Preshared Key
: Renter the pre-shared key.
In
Common Settings
:
Traffic Selector
: Choose the traffic selector you created above.
NAT Traversal
: Choose
On
.
Passive
: Leave unselected.
Presented ID Type
: Choose
Address
.
Presented ID
: Choose
Override
:
Presented ID Value
: Enter the public IP address with which F5 BIG-IP tries connecting to Netskope. It should be the NAT’ted public IP.
Verified ID Type
: Choose
Address
.
Verified ID
: Choose
Override
.
Verified ID Value
: Enter the IPSec Gateway IP address of the primary Netskope POP you copied in the Netskope UI.
Proxy Support
: Choose
Enabled
.
DPD Delay
: Enter
30
seconds.
Replay Window Size
: Enter
64
packets.
Click
Save
.
Verifying the IPSec Tunnel Status
On Netskope:
On the F5 BIG-IP LTM:
Troubleshooting
To troubleshoot on Netskope:
Contact Netskope Support to check the Sumo Logs to see if there are any errors when the IKE Phase 1 request hits Netskope.
Review the recorded session referred in the related article.
To troubleshoot on the F5 BIG-IP LTM:
Go to
Network
>
IPsec
>
IKE Daemon
>
Set Log Level
to
Debug2
. Logs will be in the
/var/log/racoon.log
file.
Generate traffic that matches the traffic selector. Run
tcpdump
to check if the traffic generated from the client to Netskope is hitting F5.
Wait a couple of minutes. If the tunnel isn’t up tmipsecd daemon might need a restart:
# tmsh restart /sys service tmipsecd
Verify if the
Local Tunnel Address
and
Remote Tunnel Address
in the
IPsec Policy
are correct.
Verify the
Presented ID Value
and
Verified ID Value
in the
IPsec Policy
are correct.
Check if the cipher suites in
IPsec Policy
and
IKE Peers
configuration are the same as the ones in the Netskope UI.
In this Topic
Netskope IPSec with F5 BIG-IP Local Traffic Manager

---
## Steer Traffic for Private App Segments
**URL:** https://docs.netskope.com/en/steer-traffic-for-private-apps/
**Last Modified:** 2026-03-03T01:17:24+00:00
**Scraped:** 2026-06-28T09:19:44.300628+00:00

Steer Traffic for Private App Segments - Netskope Knowledge Portal
Steer Traffic for Private App Segments
To steer traffic for Private App Segments, you can add users or create a steering configuration that specifies an Organizational Unit (OU) or User Group.
Create a Steering Configuration for an OU or User Group
OUs or User Groups are specified in the Real-time Protection policy that grants access to private apps.
If you do not already have a steering configuration that specifies the Organization Unit (OU) or User Group you want to steer to a private apps, follow these steps.
If you already have such a steering configuration, you can simply enable private apps for that steering configuration. For more details, refer to
Change Steering Configurations to Include Private Apps
.
Go to
Settings > Security Cloud Platform > Steering Configuration
and click
Create a New Configuration
.
In the New Configuration dialog box, enter and select the following settings:
Configuration Name
: Enter a meaningful name for this steering configuration.
Organizational Unit (OU)/User Group
: The dropdown/search field allows you to select and search for an OU or User Group.
Traffic
: Select
Cloud Apps Only
or
Web Traffic
.
Private App Segments
: Change to
All Private App Segments
.
Status
: Change to
Enabled
.
Click
Save
.
Change Steering Configurations to Include Private Apps
To update a steering configuration for private apps, follow these steps:
Go to
Settings > Security Cloud Platform > Steering Configuration
. Complete the following steps for each steering configuration that you want to steer to private apps. There are two methods:
If you have just one Default steering configuration, you can use the
Edit
button in the top right corner.
If you have multiple steering configurations, click the
icon on the right side of each configuration and select
Edit Configuration
.
For Private Apps, change to
Private App Segments
and enable the Status toggle.
Click
Save
.
In this Topic
Steer Traffic for Private App Segments

---
## DNSaaS Steering Configurations Cases
**URL:** https://docs.netskope.com/en/dnsaas-steering-configurations-cases/
**Last Modified:** 2025-08-31T01:50:35+00:00
**Scraped:** 2026-06-28T09:19:46.479232+00:00

DNSaaS Steering Configurations Cases - Netskope Knowledge Portal
DNSaaS Steering Configurations Cases
These configurations are required to ensure DNSaaS will work properly in different scenarios.
For machines without the Netskope Client and/or DNS Servers, not behind a Netskope Tunnel (IPSec/GRE) where the DNSaaS Anycast IPs have been configured as DNS Servers (for Clients) or Forwarders (for DNS Servers)
In this scenario, which is the most typical for DNSaaS, we’ll consider the minimum configurations required to make DNSaaS to work properly.
In this scenario we are dealing with:
Clients (any possible device, Server, IoT) that don’t have the Netskope Client deployed, where the DNSaaS Anycast IPs are configured as DNS Servers
DNS Server machines that are responsible for the DNS resolution of Clients in the Network, where the DNSaaS Anycast IPs are configured as DNS Forwarders for all the non-authoritative domains
DNSaaS Service Configuration
Since the connections to the Netskope Anycast IPs will be coming from the Internet, some configurations are needed to ensure that the DNSaaS service will accept the queries (Netskope DNSaaS is not a Public Resolver opened to the Internet !), and that the traffic is attributed to the correct customer’s tenant, and the customer’s policies will be applied.
To do so, customers must configure all the public egress IPs belonging to them that will be used by the clients and DNS Servers (as forwarders) when sending the DNS query to the Netskope DNSaaS service. This will ensure that the queries coming from those public egress IPs will be accepted by the DNSaaS service, and that they will be associated, and managed by the customer’s tenant.
Steering Configurations
There are no specific Steering Configurations settings for this use case, as Steering Configurations apply at the Netskope Client
Steering Exceptions
There are no specific Steering Exceptions settings for this use case, as Steering Exceptions apply at the Netskope Client.
For machines with the Netskope Client where the DNSaaS Anycast IPs have been configured as DNS Servers
In this scenario, which is not the most typical for DNSaaS, we’ll consider the minimum configurations required to make DNSaaS to work properly.
In this scenario we are dealing with Clients (generally user Desktops/Laptops) that have the Netskope Client deployed, where the DNSaaS Anycast IPs are also configured as DNS Servers.
DNSaaS Service Configuration
In this use case we want to send the DNS query towards the Anycast IPs inside the Netskope Client tunnel. For this reason we don’t need to configure DNSaaS with the customer’s public IPs to accept the queries via the Public Internet and associate them to the customer’s tenant, as the connections towards the Anycast IP will already come from the Netskope Client tunnel.
Steering Configurations
To ensure the DNS queries towards the Anycast IP are sent via the Netskope Client tunnel, customers must enable DNS Security on the Steering Configuration applied to the user enrolled by the Netskope Client
Steering Exceptions
To ensure the DNS queries towards the Anycast IP are sent via the Netskope Client tunnel, customers must avoid Destination Locations Steering Bypasses that are configured as “Bypass” (as opposed to just “Bypass, except for DNS traffic”) for the DNSaaS Anycast IPs.
To note that it’s always a best practice for any customer using DNS Security to configure DNS Steering Bypasses for their internal domain. Let’s note that in this use case any DNS query for any non-public domain is not resolvable by default.
Having specific internal domains configured as DNS Steering Exceptions will make the DNS query for those domains to be sent to the DNSaaS Anycast IPs directly via the Internet. Such queries will either be rejected by DNSaaS (depending on the DNSaaS Service Configuration and the Egress IP used by the Client), or they will be accepted by DNSaaS and resolved as NXDOMAIN.
Netskope Client and Tunnels interoperability
When the Netskope Client starts in a network where a Tunnel (IPSec/GRE) has been established with  the Netskope Cloud it is possible to configure the client  to  disable itself due to the sensing of the Tunnel (how to enable or disable this sensing goes beyond this document). When the Netskope Client is disabled due to the sensing of a Tunnel it will provide user identification and notifications, but it doesn’t steer the traffic itself, so the traffic will go direct and it will be steered by the edge Tunnel created towards the Netskope Cloud depending on the routing/PBR configuration of the Edge device establishing the tunnel. For this reason it’s important to understand that the Steering Configurations and the Steering Exceptions no longer determine what traffic is steered towards the Netskope Cloud.
The Steering Configuration traffic type will no longer determine what traffic is steered towards the Netskope Cloud, and the Steering Exceptions will no longer determine what traffic should go direct, as all traffic will go direct. By all means, a part for what concerns user identification and notifications, when the Client is disabled due to the sensing of a Tunnel, the traffic will follow the same flow of a Device behind a Netskope Tunnel where the Netskope Client is not installed.
For machines with the Netskope Client where the DNS Servers configured are not the DNSaaS Anycast IPs
In this scenario, which can be very typical for DNSaaS, we’ll consider the minimum configurations required to make DNSaaS to work properly.
In this scenario we are dealing with Clients (generally user Desktops/Laptops) that have the Netskope Client deployed, where the DNS Servers configured on the Client are either internal DNs Servers or Public resolvers, most likely configured via DHCP. This is the most typical scenario for remote users, where the Customer can’t control the network the clients connect to.
DNSaaS Service Configuration
In this use case we want to send the DNS Query towards whatever DNS Server IP configured on the Client inside the Netskope Client tunnel. For this reason we don’t need to configure DNSaaS with the customer’s public IPs to accept the queries via the Public Internet and associate them to the customer’s tenant, as the Client will not try to use the DNSaaS Anycast IP in any circumstance.
In order to force the DNS resolution to be served by DNSaaS, customers must configure the “Custom DNS Server” in any DNS profile affecting the users enrolled by the Clients, to point to the DNSaaS Anycast IPs.
Steering Configurations
To ensure the DNS queries towards any DNS server configured on the Client are sent via the Netskope Client tunnel (and they are resolved by DNSaaS due to DNSaaS configured as Custom DNS Server on the DNS Profile), customers must enable DNS Security on the Steering Configuration applied to the user enrolled by the Netskope Client
Steering Exceptions
To ensure the DNS queries towards any DNS server configured on the Client are sent via the Netskope Client tunnel (and they are resolved by DNSaaS due to DNSaaS configured as Custom DNS Server on the DNS Profile), customers must avoid Destination Locations Steering Bypasses that are configured as “Bypass” (as opposed to just “Bypass, except for DNS traffic”) for any possible destination, including “Local IP address ranges” (RFC1918 destinations).
To note that it’s always a best practice for any customer using DNS Security to configure DNS Steering Bypasses for their internal domain. Let’s note that in this use case the Clients may be able to resolve internal domains using the DNS Server configured on the machine.
Having specific internal domains configured as DNS Steering Exceptions will make the DNS query for those domains to be sent to the original DNS server configured on the Client, allowing the Client to resolve local domains that are authoritative on the DNS Server configured on the Client.
Netskope Client and Tunnels interoperability
When the Netskope Client starts in a network where a Tunnel (IPSec/GRE) has been created towards the Netskope Cloud it is possible to configure it to disable itself due to the sensing of the Tunnel (how to enable or disable this sensing goes beyond this document). When the Netskope Client is disabled due to the sensing of a Tunnel it will provide user identification and notifications, but it doesn’t steer the traffic itself, so the traffic will go direct and it will be steered by the edge Tunnel created towards the Netskope Cloud depending on the routing/PBR configuration of the Edge device establishing the tunnel. For this reason it’s important to understand that the Steering Configurations and the Steering Exceptions no longer determine what traffic is steered towards the Netskope Cloud.
The Steering Configuration traffic type will no longer determine what traffic is steered towards the Netskope Cloud, and the Steering Exceptions will no longer determine what traffic should go direct, as all traffic will go direct. By all means, a part for what concerns user identification and notifications, when the Client is disabled due to the sensing of a Tunnel, the traffic will follow the same flow of a Device behind a Netskope Tunnel where the Netskope Client is not installed.
For machines and/or DNS Servers behind a Netskope Tunnel (IPSec/GRE) where the DNSaaS Anycast IPs have been configured as DNS Servers (for Clients) or Forwarders (for DNS Servers)
In this scenario, which can be quite typical for DNSaaS, we’ll consider the minimum configurations required to make DNSaaS to work properly.
In this scenario we are dealing with:
Clients (any possible device, Server, IoT) that don’t have the Netskope Client deployed but are in a network that has a Tunnel (IPSec/GRE) towards Netskope, where the DNSaaS Anycast IPs are configured as DNS Servers
DNS Server machines that are responsible for the DNS resolution of Clients in the Network that are in a network that has a Tunnel (IPSec/GRE) towards Netskope, where the DNSaaS Anycast IPs are configured as DNS Forwarders for all the non-authoritative domains
DNSaaS Service Configuration
In this use case we want to send the DNS query towards the Anycast IPs inside the Netskope Tunnel (IPsec/GRE). For this reason we don’t need to configure DNSaaS with the customer’s public IPs to accept the queries via the Public Internet and associate them to the customer’s tenant, as the connections towards the Anycast IP will already come from the Netskope Tunnel (IPSec/GRE).
Steering Configurations
There are no specific Steering Configurations settings for this use case, as Steering Configurations apply at the Netskope Client. Of course, customers must ensure that the PBR on their edge device that establishes the Tunnels with Netskope sends the traffic for the DNSaaS Anycast IPs inside the tunnel.
Steering Exceptions
There are no specific Steering Exceptions settings for this use case, as Steering Exceptions apply at the Netskope Client. Of course, customers must ensure that the PBR on their edge device that establishes the Tunnels with Netskope sends the traffic for the DNSaaS Anycast IPs inside the tunnel.
For machines and/or DNS Servers behind a Netskope Tunnel (IPSec/GRE) where the configured DNS Servers (for Clients) or Forwarders (for DNS Servers) are not the DNSaaS Anycast IPs
In this scenario, which can be quite rare DNSaaS, we’ll consider the minimum configurations required to make DNSaaS to work properly.
In this scenario we are dealing with:
Clients (any possible device, Server, IoT) that don’t have the Netskope Client deployed but are in a network that has a Tunnel (IPSec/GRE) towards Netskope, where the DNS Servers configured on the Clients are Public resolvers
DNS Server machines that are responsible for the DNS resolution of Clients in the Network that are in a network that has a Tunnel (IPSec/GRE) towards Netskope, where the DNS Forwarders configured are Public resolvers/DNS Root
To note that in this use case Netskope can’t capture and serve any DNS query sent to any local network, as that traffic cannot be sent to the Netskope Tunnels, which exist between a customer’s edge device and Netskope.
DNSaaS Service Configuration
In this use case we want to send the DNS query towards any Public Resolver/DNS Root IPs inside the Netskope Tunnel (IPsec/GRE). For this reason we don’t need to configure DNSaaS with the customer’s public IPs to accept the queries via the Public Internet and associate them to the customer’s tenant, as the connections towards the Anycast IP will already come from the Netskope Tunnel (IPSec/GRE).
In order to force the DNS resolution to be served by DNSaaS, customers must configure the “Custom DNS Server” in any DNS profile affecting the users enrolled by the Clients, to point to the DNSaaS Anycast IPs.
Steering Configurations
There are no specific Steering Configurations settings for this use case, as Steering Configurations apply at the Netskope Client. Of course, customers must ensure that the PBR on their edge device that establishes the Tunnels with Netskope sends the traffic for the Public Resolver/DNS Root IPs inside the tunnel.
Steering Exceptions
There are no specific Steering Exceptions settings for this use case, as Steering Exceptions apply at the Netskope Client. Of course, customers must ensure that the PBR on their edge device that establishes the Tunnels with Netskope sends the traffic for the Public Resolver/DNS Root IPs inside the tunnel.
In this Topic
DNSaaS Steering Configurations Cases

---
## Palo Alto Networks Cortex XDR Plugin for Risk Exchange
**URL:** https://docs.netskope.com/en/palo-alto-networks-cortex-xdr-v1-0-0-plugin-for-risk-exchange/
**Last Modified:** 2026-05-28T22:41:22+00:00
**Scraped:** 2026-06-28T09:21:03.049634+00:00

Palo Alto Networks Cortex XDR Plugin for Risk Exchange - Netskope Knowledge Portal
Palo Alto Networks Cortex XDR Plugin for Risk Exchange
This document explains how to configure the Palo Alto Networks Cortex XDR v1.0.0 plugin with the Risk Exchange module of the Netskope Cloud Exchange platform. This plugin fetches Endpoints and Users data from Palo Alto Networks Cortex XDR platform. This plugin retrieves the endpoints from the
Endpoint > All Endpoints
page. This plugin also supports Isolate Endpoint, Un-Isolate Endpoint, Run Scan on Endpoint, Cancel Running Scan on Endpoint actions in the Palo Alto Networks Cortex XDR platform.
Netskope normalization score calculation for Endpoints and Users => 1000 * (1 – RiskScore/100)
Prerequisites
To complete this integration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Risk Exchange
plugin already configured.
Connectivity to Palo Alto Networks Cortex XDR platform.
Subscriptions for these licenses with respective purposes:
License
Purpose
Identity Threat Module
For fetching risky users and hosts
Cortex XDR Prevent
For fetching endpoints and all 4 actions
Cortex XDR Pro per Endpoint
For fetching endpoints and all 4 actions
Cortex XDR Pro per GB
For scan and cancel scan actions
Access to generate API Base URL, API Key ID, API Key and pull Users, Endpoints and Hosts.
Connectivity to the following host:
https://api-**.xdr.**.paloaltonetworks.com
.
Palo Alto Networks Cortex XDR Plugin Support
This plugin fetches Endpoints and Users data from Palo Alto Networks Cortex XDR platform. It retrieves the Endpoints from the
Endpoint > All Endpoints
page. This plugin also supports Isolate Endpoint, Un-Isolate Endpoint, Run Scan on Endpoint, Cancel Running Scan on Endpoint actions on Palo Alto Networks Cortex XDR platform.
Types of Data Pulled
Actions Supported
Users
Endpoints
Isolate Endpoint
Un-Isolate Endpoint
Run Scan on Endpoint
Cancel Running Scan on Endpoint
Mappings
Mappings are used to view the pulled Users and Endpoints and their respective details. Fields mapped during plugin configuration will be visible on the Records page after the data is pulled. Here are the suggested mappings to use while configuring the plugin.
Pull Mappings for Users
Plugin Field
Expected Datatype
Suggested Field Name
Suggested Field Aggregate Strategy
User ID
String
User ID
Unique
Risk Score
Number
Risk Score
Unique
Email
String
Email
Overwrite
Risk Level
String
Risk Level
Overwrite
Netskope Normalized Risk Score
Number
Netskope Normalized Risk Score
Overwrite
Normalized Risk Score
Number
Normalized Risk Score
Overwrite
Pull Mappings for Endpoints
Plugin Field
Expected Datatype
Suggested Field Name
Suggested Field Aggregate Strategy
Endpoint ID
String
Endpoint ID
Unique
Endpoint name
String
Endpoint name
Unique
Risk Score
Number
Risk Score
Unique
Endpoint Type
String
Endpoint Type
Overwrite
Endpoint Status
String
Endpoint Status
Overwrite
Operating System Type
String
Operating System Type
Overwrite
Operating System name
String
Operating System name
Overwrite
Operating System version
String
Operating System version
Overwrite
IPv4 Address
List
IPv4 Address
Overwrite
IPv6 Address
List
IPv6 Address
Overwrite
Public IP Address
String
Public IP Address
Overwrite
Users
List
Users
Overwrite
Domain
String
Domain
Overwrite
MAC Address
List
MAC Address
Overwrite
Server Tags
List
Server Tags
Overwrite
Endpoint Tags
List
Endpoint Tags
Overwrite
Risk Level
String
Risk Level
Overwrite
Netskope Normalized Risk Score
Number
Netskope Normalized Risk Score
Overwrite
Normalised Risk Score
Number
Normalised Risk Score
Overwrite
Isolation Status
String
Isolation Status
Overwrite
Operational Status
String
Operational Status
Overwrite
Scan Status
String
Scan Status
Overwrite
Group Name
List
Group Name
Overwrite
Permissions
For fetching Users and Endpoints and performing actions using the plugin the user will need is role: Privileged Responder Role.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/api_keys/validate/
POST
Validate connectivity using the provided configuration parameters
/public_api/v1/get_risky_users
POST
Fetch users and their risk score
/public_api/v1/endpoints/get_endpoint
POST
Fetch endpoints (devices) data
/public_api/v1/get_risky_hosts
POST
Fetch risk score for endpoints (devices)
/public_api/v1/endpoints/isolate
POST
Isolate endpoint
/public_api/v1/endpoints/unisolate
POST
Un-isolate endpoint
/public_api/v1/endpoints/scan
POST
Run scan on endpoint
/public_api/v1/endpoints/abort_scan
POST
Cancel running scan on endpoint
Authorization
API Endpoint:
/api_keys/validate/
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Sample API Response
true
Fetch Users
API Endpoint:
/oauth2/authorize/central/api
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Sample API Response
{
    "reply": [
        {
            "type": "user",
            "id": "xyz\\abc",
            "score": 0,
            "norm_risk_score": 0,
            "risk_level": "LOW",
            "reasons": [],
            "email": "string"
        }
    ]
}
Fetch Endpoints
API Endpoint:
/public_api/v1/endpoints/get_endpoint
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Body Parameters
Key
Value
Description
search_from
Integer
Pagination offset
search_to
Integer
Pagination limit
Sample Request Body
{
  "request_data": {
    "search_from": 0,
    "search_to": 100
  }
}
Sample API Response
{
    "reply": {
        "total_count": 4,
        "result_count": 1,
        "endpoints": [
            {
                "endpoint_id": "9713c1f5e2f8487e8d6783ee9e0987b8",
                "endpoint_name": "Win2k16-7-148",
                "endpoint_type": "AGENT_TYPE_SERVER",
                "endpoint_status": "CONNECTED",
                "os_type": "AGENT_OS_WINDOWS",
                "os_version": "10.0.14393",
                "ip": [
                    "10.50.7.148"
                ],
                "ipv6": [
                    "fda7:e6ee:2e09:0:809c:1627:e7e4:adcb"
                ],
                "public_ip": "140.246.76.125",
                "users": [
                    "xyz\\abc"
                ],
                "domain": "xyz.com",
                "alias": "",
                "first_seen": 1743498903224,
                "last_seen": 1743507983054,
                "content_version": "1730-14274",
                "installation_package": "",
                "active_directory": [],
                "install_date": 1743498903234,
                "endpoint_version": "8.7.0.7735",
                "is_isolated": "AGENT_UNISOLATED",
                "isolated_date": null,
                "group_name": [],
                "operational_status": "PROTECTED",
                "operational_status_description": "[]",
                "operational_status_details": [],
                "scan_status": "SCAN_STATUS_NONE",
                "content_release_timestamp": 1743502658000,
                "last_content_update_time": 1743503174008,
                "operating_system": "Windows Server 2016",
                "mac_address": [
                    "00:50:56:81:fc:fc"
                ],
                "assigned_prevention_policy": "Windows Default",
                "assigned_extensions_policy": "Windows Default",
                "token_hash": "",
                "tags": {
                    "server_tags": [],
                    "endpoint_tags": []
                },
                "content_status": "UP_TO_DATE"
            }
        ]
    }
}
Fetch Risk Score for Endpoints
API Endpoint:
/public_api/v1/get_risky_hosts
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Sample API Response
{
    "reply": [
        {
            "type": "host",
            "id": "Win2k16-7-148",
            "score": 0,
            "norm_risk_score": 0,
            "risk_level": "LOW",
            "reasons": []
        }
    ]
}
Isolate an Endpoint
API Endpoint:
/public_api/v1/endpoints/isolate
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Body Parameters:
Key
Value
Description
value
<endpoint_id_list>
List of endpoint IDs to be isolated
incident_id
<incident_id>
(Optional) When included in the request, the Scan Endpoints action will appear in the Cortex XDR Incident View Timeline tab.
Sample Request Body
{
            "request_data": {
                "filters": [
                    {
                        "field": "endpoint_id_list",
                        "operator": "in",
                        "value": endpoint_id_list,
                    }
                ],
                "incident_id": incident_id,
            }
        }
Un-Isolate an Endpoint
API Endpoint:
/public_api/v1/endpoints/unisolate
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Body Parameters
Key
Value
Description
value
<endpoint_id_list>
List of endpoint IDs to be isolated
incident_id
<incident_id>
(Optional) When included in the request, the Scan Endpoints action will appear in the Cortex XDR Incident View Timeline tab.
Sample Request Body
{
            "request_data": {
                "filters": [
                    {
                        "field": "endpoint_id_list",
                        "operator": "in",
                        "value": endpoint_id_list,
                    }
                ],
                "incident_id": incident_id,
            }
        }
Run a Scan on an Endpoint
API Endpoint:
/public_api/v1/endpoints/scan
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Body Parameters
Key
Value
Description
value
<endpoint_id_list>
List of endpoint IDs to be isolated
incident_id
<incident_id>
(Optional) When included in the request, the Scan Endpoints action will appear in the Cortex XDR Incident View Timeline tab.
Sample Request Body
{
            "request_data": {
                "filters": [
                    {
                        "field": "endpoint_id_list",
                        "operator": "in",
                        "value": endpoint_id_list,
                    }
                ],
                "incident_id": incident_id,
            }
        }
Cancel Running a Scan on an Endpoint
API Endpoint:
/public_api/v1/endpoints/abort_scan
Method:
POST
Headers (Authentication Method: Standard)
Key
Value
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
x-xdr-auth-id
<api_key_id>
Authorization
<api_key>
Headers (Authentication Method: Advanced)
Key
Value
Description
User-Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
User Agent
x-xdr-nonce
<nonce>
Randomly generated 64 character long alpha numeric string
x-xdr-timestamp
<timestamp>
Current unix timestamp in millisecond
x-xdr-auth-id
<api_key_id>
API key ID
Authorization
<api_key_hash>
Hash of API key + Nonce + Timestamp string
Body Parameters
Key
Value
Description
value
<endpoint_id_list>
List of endpoint IDs to be isolated
incident_id
<incident_id>
(Optional) When included in the request, the Scan Endpoints action will appear in the Cortex XDR Incident View Timeline tab.
Sample Request Body
{
            "request_data": {
                "filters": [
                    {
                        "field": "endpoint_id_list",
                        "operator": "in",
                        "value": endpoint_id_list,
                    }
                ],
                "incident_id": incident_id,
            }
        }
Performance Matrix
Here are the performance readings conducted on a Large CE Stack with these VM specifications by pulling 500K Users and Endpoints from the Palo Alto Networks Cortex XDR plugin.
Description
Specification
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Users fetched from the Palo Alto Networks Cortex XDR
~6 minutes
Endpoints fetched from the Palo Alto Networks Cortex XDR
~15 minutes
User Agent
netskope-ce-5.1.1-cre-palo-alto-networks-cortex-xdr-v1.0.0
Workflow
Get your API Base URL, API Key ID and API Key
Configure the Palo Alto Networks Cortex XDR plugin
Add a Business Rule
Add Actions.
Validate the plugin
Watch a Video
Click play to watch a video:
Get your API Base URL, API Key ID, and API Key
To add permissions to a role:
Log in to your Palo Alto Networks Cortex XDR account.
Go to
Settings > Configuration
.
Go to
Roles
under
Access Management
.
Click
+ New Role
, and enter a Role Name, Description, and select the required permissions. For the minimum requirement of the API Key Role, refer to
Permissions
.
Click
Save
.
To get your API Base URL, API Key ID, and API Key:
Go to
API Keys
under
Integrations
.
Click
Copy API URL
to get the API Base URL.
Click
+ New Key
and add the Security level, Role, and Expiration Date fields.
Clicking
Generate
and copy the API Key and API Key ID.
Configure the Palo Alto Networks Cortex XDR Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and select the
Palo Alto Networks Cortex XDR v1.0.0 (CRE)
plugin box.
Add a plugin configuration name, and change the sync interval if needed.
Click Next and enter the configuration parameters:
API Base URL:
The API Base URL of your Palo Alto Networks Cortex XDR tenant. For example: https://api-
<tenant-name>
.xdr.
<region>
.paloaltonetworks.com.
API Key ID:
The API Key ID you copied previously.
API Key:
The API Key you copied previously.
Authentication Method:
Select the authentication method chosen while creating the API Key.
Click
Next
. Select the Entity from the Entity dropdown. The Entity fields can be created from the Schema Editor page, or click
+ Add Field
from the field dropdown. Provide the field mapping. For the suggested mappings, refer to Mappings.
Click
Save
.
Add a Risk Exchange Business Rule for Palo Alto Networks Cortex XDR
In Risk Exchange, go to
Business Rules
.
Click
Create New Rule
in the top right corner.
Enter a Rule Name. Select the Entity Fields use to configure for the Palo Alto Networks Cortex XDR plugin, and configure the query based on your requirements. Click
Save
.
Add Risk Exchange Actions for Palo Alto Networks Cortex XDR
The Palo Alto Networks Cortex XDR plugin supports these actions for Endpoints:
Isolate Endpoint will isolate the endpoint on Palo Alto Networks Cortex XDR.
Un-isolate Endpoint will un-isolate the endpoint on Palo Alto Networks Cortex XDR.
Run Scan on Endpoint will start scanning the endpoint on Palo Alto Networks Cortex XDR.
Cancel Running Scan on Endpoint will stop running scans on the endpoint on Palo Alto Networks Cortex XDR.
No Action will not perform any action on Users/Endpoints.
Note that you can perform the Netskope related actions on the Users and Endpoints pulled from Palo Alto Networks Cortex XDR. Refer to
Risk Exchange
in order to configure the actions and their validations.
To configure these actions, follow the steps in the appropriate section.
Isolate Endpoint
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select a Business Rule, and for Target Plugin Configuration, select your configured plugin.
In the Actions dropdown, select
Isolate Endpoint
.
For Action Parameters, select the option for Endpoint ID, if users need to filter out endpoints using business rules.
Provide a static Incident ID, which can be created for an Incident on Palo Alto Networks Cortex XDR Incident ViewTimeline tab.
Enable the
Require Approval
toggle if Approval is needed before performing action on the users.
Click
Save
.
Un-isolate Endpoint
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select a Business Rule, and for Target Plugin Configuration, select your configured plugin.
In the Actions dropdown, select
Un-isolate Endpoint
.
For Action Parameters, select the option for Endpoint ID, if users need to filter out endpoints using business rules.
Provide a static Incident ID, which can be created for an Incident on Palo Alto Networks Cortex XDR Incident ViewTimeline tab.
Enable the
Require Approval
toggle if Approval is needed before performing action on the users.
Click
Save
.
Run a Scan on an Endpoint
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select a Business Rule, and for Target Plugin Configuration, select your configured plugin.
In the Actions dropdown, select
Run Scan on Endpoint
.
For Action Parameters, select the option for Endpoint ID, if users need to filter out endpoints using business rules.
Provide a static Incident ID, which can be created for an Incident on Palo Alto Networks Cortex XDR Incident ViewTimeline tab.
Enable the
Require Approval
toggle if Approval is needed before performing action on the users.
Click
Save
.
Cancel Running a Scan on an Endpoint
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select a Business Rule, and for Target Plugin Configuration, select your configured plugin.
In the Actions dropdown, select
Cancel Running Scan on Endpoint
.
For Action Parameters, select the option for Endpoint ID, if users need to filter out endpoints using business rules.
Provide a static Incident ID, which can be created for an Incident on Palo Alto Networks Cortex XDR Incident ViewTimeline tab.
Enable the
Require Approval
toggle if Approval is needed before performing action on the users.
Click
Save
.
No Action
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select a Business Rule, and for Target Plugin Configuration, select your configured plugin.
In the Actions dropdown, select
No Actions
and enable the “Generate Alert” toggle button to generate alerts in the Ticket Orchestrator.
Enable the
Require Approval
toggle if Approval is needed before performing action on the users.
Click
Save
.
The Palo Alto Networks Cortex XDR plugin supports following actions for Users: No Action will not perform any action on Users.
Validate the Palo Alto Networks Cortex XDR Plugin
Validate in Palo Alto Networks Cortex XDR
We pull Users and Endpoints from Palo Alto Networks Cortex XDR. The Endpoints are pulled from the
Endpoint > All Endpoints
page.
The logs for all the performed actions can be seen in the
Incident Response > Response > Action Center
page.
Note for Un-isolate endpoint, Run scan on endpoint, and Cancel Run scan on endpoint actions, Cancel Isolation, Malware scan, and Abort Malware scan, are the respective labels on the Palo Alto Networks Cortex XDR platform.
Validate in Cloud Exchange
To verify the Users and Endpoints pulled from Palo Alto Networks Cortex XDR, go to
Logging
and search for the logs from the Palo Alto Networks Cortex XDR plugin. You can search with a query like
message Like “CRE Palo Alto Networks Cortex XDR”
To check the execution of actions, check the logs.
To check the records pulled and stored in Risk Exchange, go to
Records
. Select the entity that you used while adding the mappings in the plugin configuration.
Also, you can verify the Action logs for performed actions.
Troubleshooting the Palo Alto Networks Cortex XDR Plugin
Receiving error in the plugin workflow
CRE Palo Alto Networks Cortex XDR [configuration_name]: Validation error occurred, Received exit code 401, Unauthorized, Verify API Key and API Key ID provided in the configuration parameters.
What to do:
Verify the API Key and API Key ID for Palo Alto Networks Cortex XDR.
Endpoints are not pulled from Palo Alto Networks Cortex XDR
If no data for the Endpoints are pulled, it might be due to one of these reasons:
No Endpoint data is available on the platform to pull
Mapping is not added in the plugin
What to do:
Go to Palo Alto Networks Cortex XDR and check if the Endpoints are available to pull from the
Endpoint > All Endpoints
page.
Edit the plugin configuration and check the Entity Source page, there should be some fields mapped in order to pull the same.
Unable to perform action on Palo Alto Networks Cortex XDR
If the Endpoint fails to perform any of the actions, it might be due to one of these reasons:
The Endpoint does not exist on Palo Alto Networks Cortex XDR
Due to an API Limitation in Palo Alto Cortex XDR. If one of the following scenarios occur, you will not be able to perform these actions:
If endpoint is already isolated and we perform Isolate Endpoint action on the same endpoint
If endpoint is already un-isolated and we perform Un-isolate Endpoint action on the same endpoint
If scan is already running and we perform Run Scan on Endpoint action on the same endpoint
If scan in not running on endpoint and we perform Cancel Running Scan on Endpoint action on the same endpoint
Netskope Normalized Score is not calculated
If the Netskope Normalized Score is not calculated for any of the records, it might be due to the record not having any of the required fields. If so, tt will not calculate the Netskope Normalized Score for that record.
Known Behavior
It has been noticed that, if any of the actions performed twice on the same endpoint, the API is giving error code 500, and we will not be able to perform the action a second time.
In this Topic
Palo Alto Networks Cortex XDR Plugin for Risk Exchange

---
## IPv6 Traffic Steering
**URL:** https://docs.netskope.com/en/ipv6-traffic-steering/
**Last Modified:** 2025-10-07T15:00:07+00:00
**Scraped:** 2026-06-28T09:24:29.725721+00:00

IPv6 Traffic Steering - Netskope Knowledge Portal
IPv6 Traffic Steering
Netskope supports enterprises who have dual stack (IPv6 and IPv4) environments where internal networks have IPv6 and IPv4 implemented. All native IPv6 enterprises can use Netskope’s client steering technology to reach the Netskope Cloud Platform. Users who want to connect to an IPv6 website will have their IPv6 traffic steered by the Netskope Client to the Netskope cloud where v6 to v4 translation is done and policies are applied to that traffic. After policy enforcement is done, any allowed traffic is forwarded to its destination using IPv4 address.
Netskope supports websites resolving to IPv6 and IPv4 addresses. It doesn’t support websites that only resolve to IPv6 addresses.
For traffic steered via IPSec or GRE tunnels, Netskope doesn’t support IPv6 traffic over the IPv4 tunnels.
In the above diagram, the Netskope Client steers the enterprise and remote user traffic.
For Cloud Firewall, since it doesn’t support IPv6 traffic including the translation, it bypasses any non-web Cloud Firewall traffic locally. This leads to end users bypassing the Cloud Firewall policies when dual stack is enabled on the device. The end-users can access cloud content on IPv6 that can lead to a security threat. To avoid this, from version 119.0.0, you can block the IPv6 non-web traffic from an application by forcing the application to transition to IPv4(The application must support IPv4 fallback). The IPv4 traffic is then tunneled to Cloud Firewall and thereafter the admin can apply the real-time policies.
Supported OS:
Windows and macOS
ICMP6 and DNS6 are not blocked.
If the application does not support fallback to IPv4, you can bypass the IPv6 traffic using Destination Location or Domain exceptions.
Netskope Private Access doesn’t support IPv6 traffic. For IPv6 DNS queries over TCP, if the hostname in the DNS query is a Private App, the Netskope Client will block the DNS request.
Network Location Objects
can be used for IPv6 Client steering exceptions. However, Network Locations when using IPv6 are not supported in
Real-Time Protection
policy as a standard Source IP attribute; there is no validation in Real-time Policy to prevent this invalid configuration.
In this Topic
IPv6 Traffic Steering

---
## Broad Access Control to Block all MCP Traffic with RTP
**URL:** https://docs.netskope.com/en/broad-access-control-to-block-all-mcp-traffic-with-rtp/
**Last Modified:** 2026-06-11T19:07:51+00:00
**Scraped:** 2026-06-28T09:27:53.373336+00:00

Broad Access Control to Block all MCP Traffic with RTP - Netskope Knowledge Portal
Broad Access Control to Block all MCP Traffic with RTP
Contact your Netskope account team to enable Agentic Broker in your account. Additional licensing is required for Agentic Broker and DLP. Note, to create a DLP policy, the DLP add-on license is required if you do not have DLP enabled in your account.
An administrator can create an RTP Policy to block all MCP traffic by creating a policy for the category “MCP Server”. Create a new policy. In the source dropdown select Category and select “MCP Server”. Set the Profile & Action to Block. Give it a name and save. Apply the changes.
Policy Configuration Interface:
The “Create Policy” screen. The Source dropdown is set to “Category” and the Category is set to “MCP Server”. Not selecting any activity applies the policy to all activities. “Profile & Action” field is set to Block.
To block a specific activity of all MCP Servers, in the Destination section select the specific Activity. The supported list of activities for MCP Server category are:
CallToolRequest
CallToolResult
CreateMessageRequest
CreateMessageResult
ElicitResult
GetPromptRequest
GetPromptResult
InitializeRequest
InitializeResult
ListPromptsResult
ListResourcesResult
ListResourceTemplatesResult
ListToolsResult
ReadResourceRequest
ReadResourceResult
Upload, Logout, Login Successful, Login Failed, Login Attempt, Browse and Download activities do not apply to MCP Communications. They apply to cloud applications. Do not select these when creating a DLP policy for MCP traffic.
Refresh the Application Events page to view that all MCP server traffic is now blocked.
Application Events Page:
Every MCP server event is blocked.
In this Topic
Broad Access Control to Block all MCP Traffic with RTP

---
## Enabling Dynamic Steering
**URL:** https://docs.netskope.com/en/enabling-dynamic-steering/
**Last Modified:** 2026-05-04T14:35:29+00:00
**Scraped:** 2026-06-28T09:30:03.695849+00:00

Enabling Dynamic Steering - Netskope Knowledge Portal
Enabling Dynamic Steering
Dynamic steering enables location-based steering capabilities via on-premises or off-premises. Depending on the location, you can set up the
steering configuration
to steer or bypass configured traffic.
Create On-Premises Detection Profile
On-premise detection profiles enable location-based steering policies. Dynamic steering facilitates diverse traffic modes and exceptions for devices, contingent upon their location (on-premise or roaming). A singular steering configuration is capable of incorporating multiple on-premise profiles.
If the endpoint is on-premises or off-premises, the Client tunnels the traffic based on the traffic mode configured for dynamic steering.
Prerequisites:
Enable
Dynamic Steering
Provide
Match Criteria
in Steering Configuration
To create a new On-Premises Detection Profile:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
In
Steering Configuration
, click
On-Premises Detection Profile
.
In
On-Premises Detection Profile
, perform the following:
Enter the profile name.
Select one of the following methods:
Egress IP:
This option provides the ability to detect location of users (On vs Off Premises) using egress public IP address of the user location. Netskope Client detects egress public IP of the user connecting to the Netskope cloud. If the egress IP matches the entry configured in Client Configuration created by the user, then the user is marked as On-Premises.
Maximum allowed IP address entries:
100
Additional options:
CSV:
You can upload or download IP addresses in the .csv format. Use Download Sample CSV to check get the sample .csv file.
Find:
Use this option to search for any specific IP address.
Clear:
Use this option to remove the added IP addresses.
DNS:
If the FQDN entered resolves to the provided IP Address, the Netskope client is considered to be on-premises. Ensure that this is a valid DNS record that is resolvable only when on your network. You can enter up to 16 IP addresses.
HTTP:
If the Client looks for the HTTP response code 200, and if successful, the device is deemed to be on-premises. Also enter a connection timeout value. The default is 10 seconds, and the max is 60 seconds. You can enter up to a maximum of 16 FQDN or IP addresses.
– Don’t use a .local hostname for the DNS check because the mDNS responder on Mac OSX might interfere with the resolution of local hostnames.
– Don’t use hostnames or IP addresses that are defined for Netskope Private Access in DNS or HTTP checks because they cause flapping in the On-Premises check. Netskope recommends you use a separate domain name that does not overlap with NPA app definitions. You can configure a dedicated forward lookup or separate entry in your enterprise DNS for the on-prem detection.
Click
Save
.
After adding your On-Premises details, the On-Premises Detection Profiles displays the configured profiles in a tabular format.This table displays the On-premises method chosen for each profile, the count of steering profiles using the On-premises profile, and the last modified details.
Dynamic Steering From Version 112.0.0
With release 112.0.0, Netskope adds more flexibility to the dynamic steering feature. In the new flexible dynamic steering:
For the steering traffic mode, you can switch traffic mode between On-Prem, Off-Prem and the new mode
None
. When the traffic mode is None, the Client does not establish a tunnel or steer traffic. Exceptions will not be processed as they are only applicable for steered traffic.
For the steering exception rules:
Firewall app exceptions contain separate sets of rules between On-Prem and Off-Prem in All steering traffic mode.
Category exceptions contain a set of rules between On-Prem and Off-Prem in Web or All mode.
– Contact Support to enable the new Dynamic Steering Configuration for the existing tenants. This feature is automatically enabled for the new tenants.
– This section is about the new Dynamic Steering option that is available from version 112.0.0. If you want to know about the legacy dynamic steering configurations, view
Creating a Steering Configuration
.
– After enabling dynamic steering, Netskope recommends avoiding disabling dynamic steering since it provides better flexibility in terms of choosing the traffic mode and bypass options. Continuous toggling of dynamic steering can cause data inconsistency.
About Dynamic Steering
With the introduction of flexible dynamic steering in version 112.0.0, you can switch traffic mode between On-Prem, Off-Prem and the new mode None.
The following are the supported steering modes when a managed device is on-premises or off-premises.
On And Off -Premises Steering Modes
When the managed device is On-Prem or Off-prem, you can set up the steering configuration to steer the following traffic modes:
Traffic Mode
Steering Exception
Cloud Apps Only
The Netskope cloud application exceptions are bypassed from the Netskope Cloud. If domain exceptions are part of a steered cloud application, they are bypassed by the Netskope cloud. If the domain exceptions aren't part of a steered cloud application, then the following behavior occurs:
For Windows devices, traffic is only sent locally and not to the Netskope Cloud.
For Mac devices, traffic is bypassed from the Netskope Cloud. If you don't want traffic to be sent to the Netskope Cloud, ensure the domain doesn't exist in the steered cloud application and exceptions list.
Web Traffic
All exceptions are bypassed from the Netskope Cloud.
All Traffic
Steer all traffic (web and non-web) to Netskope for deep analysis. You can make exceptions for traffic that have personal or private content.
None
Client does not establish any tunnel and continues to monitor On-Prem status change. The Client establishes a tunnel if the On-Prem status changes and a tunnel is needed for the new traffic steering mode.
For flexible dynamic steering to work seamlessly, disable steering configuration in NS Proxy. Steering exceptions are no longer part of the SSL or Real-time Protection bypasses for any access method. Create separate SSL and Real-Time Protection Policies for these access methods.
In addition,
non-standard port
steering configuration is no longer used to control the TCP ports allowed for HTTPS requests. All ports are allowed by default in the proxy. Use the Service objects to control access for each port.
Legacy Dynamic Steering vs Flexible Dynamic Steering
Steering Type
Location
Bypass Exception At
Cloud Apps Only
Web Traffic
All Traffic
None
Legacy Dynamic Steering(Prior to version 112.0.0)
On-Premises
Netskope Cloud
Yes
Yes
Yes
No
Off-Premises
Client
Yes
Yes
Yes
No
Flexible Dynamic Steering
On-Premises
Either at Netskope Cloud or Client
Yes
Yes
Yes
Yes
Off-Premises
Either at Netskope Cloud or Client
Yes
Yes
Yes
Yes
Enabling On-Premises Detection
Before enabling dynamic steering, you must enable On-premises detection for the Netskope Client. To enable
On-premises Detection
in
Client Configuration
, view
Tunnel Settings
.
From version 131.0.0, you can enable the new On-Premises Detection option from Steering Configuration. To learn more, view
On-Premises Detection
.
Enabling Dynamic Steering for On- or Off-Premises Devices
To enable dynamic steering for on- or off-prem devices:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
New Configuration
, or click
and choose
Edit Configuration
to select one of the existing steering configurations you want to enable dynamic steering.
In the
Edit Configuration
window, select
Enable Dynamic Steering
. You can steer traffic for Netskope Client through the On- or Off-prem configurations in the drop-down menu.
You can choose one of the following steering options for
On-Premises
and
Off-Premises
:
Cloud Apps Only:
Only steer specific cloud applications to the Netskope cloud for deep analysis. You can create exceptions and allow special accommodations for custom applications.
Web Traffic:
Steer all web traffic (HTTP and HTTPS) to the Netskope cloud for deep analysis. You can create exceptions for traffic that have personal or private content. You must have a SWG/NG SWG license to select this option.
All traffic:
Steer all HTTP(S) and non-HTTP(S) to the Netskope cloud for deep analysis. You must have the Cloud Firewall license to select this option.
Non-HTTP (s) TCP Cloud Firewall traffic is bypassed at Netskope Client even when configured to Bypass at Netskope Cloud.
None:
The Client does not establish any tunnel and continues to monitor On-Prem status change. The Client establishes a tunnel if the On-Prem status changes and a tunnel is needed for the new traffic steering mode.
Bypass exception traffic at Netskope Client or Netskope Cloud. If you choose:
Client:
Traffic bypass on the local device.
Netskope Cloud:
Traffic bypasses the firewall.
DNS traffic:
Select to steer DNS traffic to the Netskope cloud for deep analysis. This option is only available for Web Traffic and All Traffic types as well as Off-Premises configurations. You must have the Cloud Firewall and DNS licenses to select this option.
Private App Segments:
Steer Private App Segments for On-Premises and Off-Premises configurations. You can steer:
All Private App Segments:
Choose if the Netskope Client must steer or not steer when other steering modes are present, like GRE, IPSec, and Explicit Proxy.
Specific Private App Segments:
Steer specific Private App Segments. For example, if your existing VPN is active and allows access to all on-prem apps in your private data center, you can deselect those apps and only select apps hosted in AWS, Azure, or GCP. This allows your existing VPN to provide access to on-prem apps, but Netskope Private Access can access apps in the public cloud.
Status:
Enable or disable the steering configuration. Netskope recommends disabling until you configure the
steered items
and
exceptions
.
Click
Save
.
Dynamic Steering Prior To Version 112.0.0
When a managed device is detected to be on-premises, only cloud applications are steered and when the device is detected to be off-premises, all web traffic is steered. Dynamic steering also extends the capability to steer traffic from all or specific private applications.
For example, ACME Inc. uses a firewall in their on-prem network to manage web traffic, but they don’t want to change this setup and use Netskope to steer cloud traffic. However, for off-prem users, they want to configure Netskope to steer both cloud and web traffic. In this situation, dynamic steering can detect user location and use appropriate steering modes.
Irrespective of the user location all exceptions types are supported. However, when using the
Destination Location
(with public IP address only) exception type, select the
Treat like local IP address
option. To learn more about exception types:
Adding Exceptions
.
About Dynamic Steering
The following are the supported steering modes when a managed device is on-premises or off-premises.
On-Premises Steering Modes
When the managed device is on-premises, you can set up the steering configuration to steer either web or cloud traffic:
Traffic Mode
Steering Exceptions
Cloud (Default)
The Netskope cloud application exceptions are bypassed from the Netskope Cloud. If domain exceptions are part of a steered cloud application, they are bypassed by the Netskope cloud. If the domain exceptions aren’t part of a steered cloud application, then the following behavior occurs:
For Windows devices, traffic is only sent locally and not to the Netskope Cloud.
For Mac devices, traffic is bypassed from the Netskope Cloud. If you don’t want traffic to be sent to the Netskope Cloud, ensure the domain doesn’t exist in the steered cloud application and exceptions list.
Web
All exceptions are bypassed from the Netskope Cloud. Contact Netskope Support to enable this mode.
Note
The steering bypasses are aggregated at the Netskope Proxy level, so if traffic is steered/sent to the Netskope Cloud when the Netskope Client is on-premises, the domain exceptions specified in off-premises steering configurations are allowed.
Off-Premises Steering Modes
When the managed device is off-premises, all web traffic is steered by the Netskope Client.
Traffic Mode
Steering Exceptions
Web (Default)
All exceptions are bypassed locally by the Netskope Client.
Netskope doesn’t support
Cloud
mode for managed devices off-premises.
Note
The steering bypasses are aggregated at the Netskope Proxy level, so if traffic is steered/sent to the Netskope Cloud when the Netskope Client is off-premises, the domain exceptions specified in on-premises steering configurations are allowed.
Enabling On-Premises Detection
Before enabling dynamic steering, you must enable on-premises detection for the Netskope Client. To learn more about on-prem detection:
Tunnel Settings
.
When dynamic steering is enabled, the Netskope Client Client checks the On-premises status every three to five minutes.
Enabling Dynamic Steering for On- or Off-Premises Devices
Note: Refer
Create Steering Configuration
to understand the new options available for Dynamic Steering.
To enable dynamic steering for on- or off-prem devices:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
New Configuration
, or click
and
Edit Configuration
to choose one of the existing steering configurations you want to enable dynamic steering for.
In the
Edit Configuration
window, select
Enable Dynamic Steering
. You can optionally enable traffic steering for all or specific private applications or DNS traffic (if you have Cloud Firewall).
Note
If dynamic steering is not enabled for on-prem, then all exceptions configured for off-prem will be bypassed by the Netskope Cloud instead of locally when the managed device is on-prem.
Click
Save
.
On the steering configuration page, select
On-Premises
or
Off-Premises
for the device location.
In this Topic
Enabling Dynamic Steering

---
## Creating a Steering Configuration
**URL:** https://docs.netskope.com/en/creating-a-steering-configuration/
**Last Modified:** 2026-05-04T17:00:26+00:00
**Scraped:** 2026-06-28T09:30:15.871792+00:00

Creating a Steering Configuration
The
default steering configuration
(Default tenant config) applies to all users in your organization. However, if some users in your organization require a different configuration, you can create a custom steering configuration for those specific OUs or user groups. Netskope also provides options that bring more flexibility while creating Steering Configuration.
Creating Steering Configuration From Version 124.0.0
This section describes the steps to create a steering configuration for the selected OUs/ User Groups.
To create a custom Steering Configuration:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
New Configuration
.
Or, click
…
and click
Edit Configuration
to choose one of the existing steering configurations.
In the
New Configuration
window, enter a name for the steering configuration. It cannot exceed 40 characters.
Click the
Match Criteria
tab. With version 124.0.0, you can use the enhanced
Match Criteria
functionality to differentiate steering profiles using the following options:
User Group/ OU:
With version 124.0.0, Netskope added the ability to select multiple User Groups/OUs while configuring Steering profiles. The multi-selection option provides flexibility in configuring the steering profiles per group of users identified by their group, OU, or a custom user attribute (LDAP attribute) to define what application or traffic needs to be steered or bypassed.
OS Family:
With version 124.0.0, you can differentiate steering profiles based on different operating systems (Windows, MacOS, Linux, Android, and iOS). This option provides flexibility in configuring steering profiles by choosing the OS type as the match criteria.
Device Tags:
With version 134.0.5, you can use these device tags to associate the steering policies to a device. You can add up to five device tags from the options provided in the dropdown and at least one tag must match to enforce steering. This list displays all device tags created in
Manage Tags
.
– Device Tags is a beta feature. Contact Netskope Support team or your Sales Representative to enable this feature for your tenant.
– The maximum number of steering policies supported using the new Match Criteria associated with the selected User group/OU and OS Family  is 100.
Netskope Client checks for all the choices made in the three criteria and if it matches, applies the steering configuration to that device.
Click the
Traffic Steering
tab. This option allows you to configure your steering profile using the following options:
Enable Dynamic Steering
:
Enable Netskope Client to use
On-premises detection
and determine if the user’s device is On-premises or Off-premises. If enabled, the On-Premises and Off-Premises settings appear.
After enabling dynamic steering, Netskope recommends to avoid disabling dynamic steering since it provides better flexibility in terms of choosing the traffic mode and bypass options. Continuous toggling of dynamic steering can lead to the loss of exceptions in the steering configuration.
On-Premises Detection Profile:
Select up to three on-premises configurations created in this
section
.
Specify the match criteria for this steering configuration:
You can steer traffic for Netskope Client through the On or Off-prem configurations in the drop-down menu. Choose one of the following steering options for On-Prem and Off-Prem:
Cloud Apps Only:
Only steer specific cloud applications to the Netskope cloud for deep analysis. You can create exceptions and allow special accommodations for custom applications.
Web Traffic:
Steer all web traffic (HTTP and HTTPS) to the Netskope cloud for deep analysis. You can create exceptions for traffic that have personal or private content. You must have a SWG/NG SWG license to select this option.
All traffic:
Steer all HTTP(S) and non-HTTP(S) to the Netskope cloud for deep analysis. You must have the Cloud Firewall license to select this option.
Non-HTTP (s) TCP Cloud Firewall traffic is bypassed at Netskope Client even when configured to Bypass at Netskope Cloud.
None:
The Client does not establish any tunnel and continues to monitor On-Prem status change. The Client establishes a tunnel if the On-Prem status changes and a tunnel is needed for the new traffic steering mode.
Bypass exception traffic at:
Choose one of the following:
Client – Traffic bypass on the local device.
Netskope Cloud – Traffic bypasses the firewall.
DNS traffic:
Select to steer DNS traffic to the Netskope cloud for deep analysis. This option is only available for Web Traffic and All Traffic types as well as Off-Premises configurations. You must have the Cloud Firewall and DNS licenses to select this option.
Private App Segments:
Steer Private App Segments for On-Premises and Off-Premises configurations. You can steer:
All Private App Segments:
Choose if the Netskope Client must steer or not steer when other steering modes are present, like GRE, IPSec, and Explicit Proxy.
Specific Private App Segments:
Steer specific Private App Segments. For example, if your existing VPN is active and allows access to all on-prem apps in your private data center, you can deselect those apps and only select apps hosted in AWS, Azure, or GCP. This allows your existing VPN to provide access to on-prem apps, but Netskope Private Access can access apps in the public cloud.
None:
Disables the private access in the Client.
Go to
App Definitions
to select the private apps you want to steer with this configuration.
Click the Private App Segments tab, click
for the private app, click Select Steering Config, and then choose a steering config for the app. Click Save.
In presence of other steering methods:
Netskope Client will Steer/Not Steer private apps in presence of other steering methods. Choose one of the following options:
Steer:
Netskope Client steers NPA traffic over GRE/IPsec tunnel.
Not Steer:
Netskope Client disables automatically if it detects other steering methods such as IPSec, GRE, or Explicit Proxy in the network.
Status:
Enable or disable the steering configuration. Netskope recommends disabling until you configure the
steered items
and
exceptions
.
Click the
Non-Standard Ports
tab:
Steer non-standard ports:
Allows the Netskope Client to steer web traffic (HTTP/HTTPS) on any port. Enter the ports or domains to steer. Click + New to add multiple ports. Click More to see the following options:
Enter the Ports or Domain/IP address to steer.
Click
+ New
to add multiple ports.
Click
More
to see the following options:
Import from CSV:
Import a CSV file containing the ports and domains you want to steer.
Download Sample CSV:
Download a sample CSV template to use to add multiple ports or domains and import the CSV file.
Delete All:
Delete all listed ports.
The port number appears in the Domain, Page, and App columns on the Skope IT Page Events page.
If FQDN is configured in the
Steer non-standard port
setting, and the server is accessed over IP address; Netskope Client treats this request as non-web traffic since Netskope Client does not maintain FQDN to IP address mapping. To avoid this, specify both FQDN and IP address in the
Non-Standard Web Port
setting.
Click the
Fail Close
tab: Fail Close blocks all traffic when Internet Security tunnel to Netskope is not established.  Domain-based, IP-based, and Cert-pinned exceptions will be applied, but category-based exceptions will be blocked.
– Starting with version 136.0.0, Netskope moved Fail Close setting to
Steering Configuration
>
Fail Close
from
Client Configuration
>
Tunnel Settings
on the webUI.
– This is a Beta feature. Contact Netskope Support team or your Sales Representative to enable this feature for your tenant.
– Supported OS: Windows
– To enable Fail Close for macOS and iOS devices, the administrator must use
Client Configuration
.
In a multi-user environment, Fail-Close blocks all traffic for a non-provisioned user; only if at least one user has enrolled successfully to the multi-user device and mapped to a Client Configuration with the Fail-Close option enabled.
If a Netskope Internet Services tunnel fails to come up, Netskope recommends that you block the steered traffic from that device.
With Client version 136.0.0, Netskope enhanced Fail Close functionality that allows administrators to enable or disable Fail-Close settings based on whether a user is on or off-premises. Previously, Fail-Close was a global setting that could not be differentiated by location.
The Netskope Client bypasses RFC-1918 IP addresses/subnets by default when in Fail-Close mode.
– Reach out to Netskope Support to enable “Block Private IP address in Fail Close”. This is supported from Netskope Client version 130.0.0.
– Remove the steering exception for
Local IP address range
in
Destination Location
from all Steering Configurations to be used with Fail-Close.
This configuration does not apply to the Private Access traffic. It is applicable only for Internet Security.
With Fail Close enabled, you can:
Show Notification:
A fail-close notification is displayed instantly when Internet Security tunnel to Netskope is not established. You can also set the time interval in seconds to delay the display of notification. For example, when users move from one network to another,  generally it takes some time for  the machine to get connected to the Wi-Fi. This transition can disconnect the Internet Security  tunnel and result in a Fail Close notification. With the
Show Notification
option, administrator can configure a timer to delay the Fail Close notification pop-up and provide enough time for the user to connect back to the Wi-Fi.
Private App Traffic:
Use this option to allow  private access traffic while fail close is enabled.
Captive Portal Detection Timeout (Minutes):
A captive portal is a web page displayed, whenever a user tries to access the network where captive portal is enabled, to let the users authenticate prior to accessing the network. For example, if you are trying to connect to the free Wi-Fi or hotspot in an airport or restaurant where captive portals are enabled, you need to complete a set of actions to access the network.
This option enables the administrator to define captive portal grace period. If the tunnel is disconnected or cannot be established and fail close is enabled, this triggers captive portal detection. If Netskope Client is detecting or detects a captive portal, it does not enforce fail close for the configured duration to enable captive portal detection to complete. If captive portal is not detected after the detection completes, it enforces fail close again. This supports Windows OS native captive portal detection and allows user to perform captive portal authentication.
Netskope Client performs captive portal detection on Windows and macOS platforms. Admin can enter a value between 1-10 (minutes) in the Captive Portal Detection Timeout input box.
Click the
Enforce Enrollment
tab: Use this tab to
enforce Netskope Client enrollment
for end-users.
Steering Profile ID:
The ID is automatically generated. The administrator can copy the steering profile ID and pass it as an argument during Netskope Client installation.
Allowed destinations without enrollment:
The configured destinations are allowed to go DIRECT on TCP ports 80 and 443 when the user is not enrolled to Netskope Client. All other traffic on TCP ports 80 and 443 are blocked until user enrolls to Netskope Client.
FQDN
Wildcard
IPv4 address
IPv4 subnet
IPv4 range
IPv6 address
IPv6 subnet
IPv6 range
Do not support short-hand notations in IPv6 range. For example,
1234:5678:9abc:def1:2345:6789:abcd::-1234:5678:9abc:def1:2345:6789:abcd:100
Instead, use the following format:
1234:5678:9abc:def1:2345:6789:abcd:0-1234:5678:9abc:def1:2345:6789:abcd:100
Message:
Enter the message that gets displayed in the pop-up reminder for end-users who are yet to complete the Client enrollment process. You can add up to 1024 characters in the Message text-box.
Admins can also add their company logo in the notification message. To customize company logo, use Templates under Settings > Tools in the webUI.
Click
Save
.
Add
steered items
(i.e., applications).
Add steering
exceptions
.
Review the steering
error settings
.
Click
for your custom steering configuration and then Enable, Disable, or Edit Configuration.
Creating Steering Configuration Prior To Version 124.0.0
This section describes the various options available to create a steering configuration.
To create a custom steering configuration:
Go to
Settings
>
Security Cloud Platform
>
Steering Configuration
.
Click
New Configuration
, or click
and choose
Edit Configuration
to select one of the existing steering configurations you want to enable dynamic steering.
In the
New Configuration
window, enter a name for the steering configuration. It cannot exceed 40 characters.
Name:  Enter a name for the steering configuration. It can’t exceed 40 characters.
User Group/ OU: Choose whether all custom traffic steering configurations must apply to Organizational Units (OUs) or user groups. This option only appears when you create your first custom steering configuration.
Click the
Traffic Steering
tab:  This option allows you to configure your steering profile using the following options.
Enable Dynamic Steering:
You can steer traffic for Netskope Client through the On- or Off-prem configurations in the drop-down menu. You can choose one of the following steering options for
On-Premises
and
Off-Premises
:
Cloud Apps Only:
Only steer specific cloud applications to the Netskope cloud for deep analysis. You can create exceptions and allow special accommodations for custom applications.
Web Traffic:
Steer all web traffic (HTTP and HTTPS) to the Netskope cloud for deep analysis. You can create exceptions for traffic that have personal or private content. You must have a SWG/NG SWG license to select this option.
All traffic:
Steer all HTTP(S) and non-HTTP(S) to the Netskope cloud for deep analysis. You must have the Cloud Firewall license to select this option.
Non-HTTP (s) TCP Cloud Firewall traffic is bypassed at Netskope Client even when configured to Bypass at Netskope Cloud.
None:
The Client does not establish any tunnel and continues to monitor On-Prem status change. The Client establishes a tunnel if the On-Prem status changes and a tunnel is needed for the new traffic steering mode.
When configuring, note the following:
You can only use dynamic steering for the OUs and user groups configured in your
Netskope Client configuration
.
To use dynamic steering, ensure you enable
On-Premises Detection
for your
Netskope Client configuration
.
You can steer traffic for Netskope Client through the On-Premises or Off-premises configurations in the drop-down menu
Bypass exception traffic at Netskope Client or Netskope Cloud. If you choose:
Client:
Traffic bypass on the local device.
Netskope Cloud:
Traffic bypasses the firewall.
DNS traffic:
Select to steer DNS traffic to the Netskope cloud for deep analysis. This option is only available for Web Traffic and All Traffic types as well as Off-Premises configurations. You must have the Cloud Firewall and DNS licenses to select this option.
Private App Segments:
Steer Private App Segments for On-Premises and Off-Premises configurations. You can steer:
All Private App Segments:
Choose if the Netskope Client must steer or not steer when other steering modes are present, like GRE, IPSec, and Explicit Proxy.
Specific Private App Segments:
Steer specific Private App Segments. For example, if your existing VPN is active and allows access to all on-prem apps in your private data center, you can deselect those apps and only select apps hosted in AWS, Azure, or GCP. This allows your existing VPN to provide access to on-prem apps, but Netskope Private Access can access apps in the public cloud.
Status:
Enable or disable the steering configuration. Netskope recommends disabling until you configure the
steered items
and
exceptions
.
Click the
Non-Standard Ports
tab.
Select
Steer non-standard ports
. This allows Netskope Client to steer web traffic (HTTP/HTTPS) on any port. Enter the ports or domains to steer. Click + New to add multiple ports. Click More to see the following options:
Enter the Ports or Domain/IP address to steer.
Click
+ New
to add multiple ports.
Click
More
to see the following options:
Import from CSV:
Import a CSV file containing the ports and domains you want to steer.
Download Sample CSV:
Download a sample CSV template to use to add multiple ports or domains and import the CSV file.
Delete All:
Delete all listed ports.
The port number appears in the Domain, Page, and App columns on the Skope IT Page Events page.
If FQDN is configured in the
Steer non-standard port
setting, and the server is accessed over IP address; Netskope Client treats this request as non-web traffic since Netskope Client does not maintain FQDN to IP address mapping. To avoid this, specify both FQDN and IP address in the
Non-Standard Web Port
setting.
Click
Save
.
In this Topic
Creating a Steering Configuration

---
## Adding Network Targets to Destination Profiles
**URL:** https://docs.netskope.com/en/adding-network-targets-to-destination-profiles/
**Last Modified:** 2026-06-01T21:09:12+00:00
**Scraped:** 2026-06-28T09:30:59.609165+00:00

Adding Network Targets to Destination Profiles - Netskope Knowledge Portal
Adding Network Targets to Destination Profiles
When adding network targets under
Definition
in a destination profile, you can use exact or regex patterns for matching. Each line in this list must be a comment or a destination.
Comments
Comments are completely ignored during processing. Note that if a comment is included in the same line as a destination, the entry is invalid. UTF-8 is supported for comments.
To add a comment, start a line with a number sign (
#
) or semicolon (
;
). An empty line is also considered a comment. To create a multi-lined comment, add a number sign or semicolon to the start of each line.
Exact Matching
This section describes best practices and supported syntax for exact matching, including examples.
Tip
Domain matching is always case insensitive. Configuring the case sensitivity only applies to paths and queries.
IP, CIDR, or Range matching always evaluates the target IP. For proxied traffic, the proxy resolves the IP, which might differ from the client-side destination IP.
Best Practices for Exact Match
Consider the following best practices when adding destinations for exact matching:
To match an original URL (e.g.,
https://www.netskope.com/
), enter it in the following syntax:
www.netskope.com
or
*.netskope.com
(to match subdomains). While
www.netskope.com/
is valid, using this syntax to match is not best practice.
Add ports only when your policies must target specific ports. For some use cases, using a
service profile
is more suitable.
Destination profiles do not support schemes (
http://
and
https://
) and you must specify the port instead. For example, to restrict matches to HTTPS only, add port
443
to the destination (e.g.,
www.netskope.com:443
).
Add paths to your destinations only when necessary as this limits matches to decrypted traffic.
Avoid query strings as reordered parameters prevent matching. For query matching, using regex is recommended. Query strings restrict matches to specific URLs if the parameters and order match.
Supported Syntax for Exact Match
Ensure that you use the correct syntax when adding destinations to the destination profile for exact matching.
FQDNs
Enter a valid domain name (e.g.,
www.netskope.com
). This only matches requests to the specified domain and does not match subdomains. International domain name (IDN) encoding is supported.
PQDNs
Enter an asterisk (
*
) before a valid domain name (e.g.,
*.netskope.com
). This matches requests to the specified top-level domain (TLD) and all subdomains. For example,
*.netskope.com
matches the TLD netskope.com and all subdomains. IDN encoding is supported.
IPs
Enter a valid IPv4 address (e.g.,
163.116.128.1
). This matches requests targeting the specified IP address.
CIDR
Enter a valid IPv4 CIDR with the prefix
CIDR
(e.g.,
CIDR:163.116.128.1/24
). This matches requests targeting the IP addresses in the specified CIDR.
Ranges
Enter a valid IPv4 range with the prefix
RANGE
(e.g.,
RANGE:163.116.128.10-163.116.128.19
). This matches requests targeting the IP addresses in the specified range.
Ports
(Optional) Add a port to the end of a destination to limit matching to the specified port (e.g.,
www.netskope.com:80
). Valid values for TCP and UDP ports are between
1
and
65535
. However, note that port ranges are
not
supported.
A destination with a specified port does not override
service profile
matches. If a rule includes destinations with port 80 and a service profile with port 443, then the destinations will never match this rule.
Paths & Queries
(Optional) Add a path or query to the end of a destination to limit matching to the specified path or query (e.g.,
www.netskope.com/path?q=value
).
A path or query only applies to proxy processing after SSL interception. They never match in SSL decryption or Cloud Firewall policy evaluation, NSClient steering, or when HTTPS is not decrypted.
Paths and queries use a “start with” operator while wildcards are unsupported (i.e., the asterisk is treated as a normal character).
Special characters are supported for paths and queries:
The following non-encoded characters are supported:
!$&'()*+,-/:;=@[]_~
The question mark (
?
) separates the path and query. A query can include an additional question mark.
A number sign (
#
) marks a URL segment, which only the HTTP client processes. It isn’t sent to the proxy as destination profiles reject it to prevent misconfiguration.
Other special characters must be URL encoded.
The proxy evaluates the exact syntax the HTTP client sends.
To match a folder, add a trailing slash (
/
) after the path. For example,
www.netskope.com/path/
matches only the
path
folder such as
www.nestkope.com/path/
and
www.netskope.com/path/file.html
. It doesn’t match the following:
www.netskope.com/path
or
www.netskope.com/path2/
.
In contrast,
www.netskope.com/path
matches any URL starting with this path such as
www.netskope.com/path
,
www.netskope.com/path/
,
www.netskope.com/path2/
,
www.netskope.com/path/file.html
, and
www.netskope.com/path_description.html
.
Examples for Exact Match
The following are examples of valid exact match patterns.
# Examples of destinations supported in Destination Profiles
# Lines starting with # or ; are comments; empty lines are also comments.
# Syntax for exact match: (FQDN|PQDN|IP|CIDR|Range)[:Port][/Path[?Query]]
## Details for the main section (FQDN|PQDN|IP|CIDR|Range)
# FQDN (Fully Qualified Domain Name) matches the exact domain only
www.example.com
# PQDN (Partially Qualified Domain Name) starts with *.
# Matches the top domain and any subdomain
*.example.com
# IP based (also evaluates resolved domain)
163.116.128.80
# Range based (also evaluates resolved domain)
RANGE:163.116.128.10-163.116.128.19
# CIDR based (also evaluates resolved domain)
CIDR:163.116.128.0/17
## Options can be added to the main section
# [:Port] Option: restricts destination to a single port:
www.example.com:8080
*.example.com:8080
163.116.128.80:8080
RANGE:163.116.128.10-163.116.128.19:8080
CIDR:163.116.128.0/17:8080
# [/Path[?Query]] Option: restricts to HTTP Path and Query string
# Warning 1: Path and Query apply only to decrypted HTTP
# Warning 2: Query matches exact parameters in order; best to use regex
www.example.com/path
www.example.com/path?q=value
*.example.com/path
*.example.com/path?q=value
163.116.128.80/path
163.116.128.80/path?q=value
RANGE:163.116.128.10-163.116.128.19/path
RANGE:163.116.128.10-163.116.128.19/path?q=value
CIDR:163.116.128.0/17/path
CIDR:163.116.128.0/17/path?q=value
# Options can be combined, for example
www.example.com:8080/path?q=value
*.example.com:8080/path?q=value
163.116.128.80:8080/path?q=value
RANGE:163.116.128.10-163.116.128.19:8080/path?q=value
CIDR:163.116.128.0/17:8080/path?q=value
Regex
This section describes best practices, supported syntax, and unsupported syntax for regex matching, including examples.
Keep in mind that the regex patterns used for destination profiles are only supported in Netskope Proxy. Additionally, regex only evaluates the URL, not the resolved IP. If the domain is unknown, then the IP serves as the FQDN.
The key differences for evaluation are as follows. Before SSL decryption (with an SSL policy) and when traffic is not decrypted (with a Real-time Protection policy), the regex engine evaluates the FQDN string. After SSL decryption and if the port is standard (i.e., 80 for HTTP or 443 for HTTPS), the proxy evaluates the FQDN, path, and query. Otherwise, the proxy evaluates the FQDN, port, path, and query.
Best Practices for Regex
Consider the following best practices when adding destinations for regex matching:
Use regex only when exact matching is impossible. For example, to match domains with subdomains, exact match (
*.netskope.com
) works best. To match requests with paths starting with
/search
, use exact matching.
Regex is efficient for matching domains with multiple TLDs and matching query parameters.
When writing regex, keep in mind that:
Periods (
.
) in domain names must be escaped.
Escaping slashes (
/
) in paths is not required.
Regex evaluates the full URL, including domain, path, and query parameters. To match only the domain, isolate it in the syntax.
Supported Syntax for Regex
Ensure that you use the correct syntax when adding destinations to the destination profile for regex. Netskope partially supports syntax from PCRE (Perl Compatible Regular Expressions) 8.41 or higher.
Literals & Escapes
Syntax
Description
Example
Literal characters
Plain characters
abc
,
foo
Escape sequences
Special character escapes
\.
,
\*
,
\+
,
\?
,
\[
,
\]
Hexadecimal
\xhh
\x41
(character “A”)
Octal
\ooo
\101
(character “A”)
Unicode
\x{hhh...}
\x{1F600}
(emoji)
Control characters
\n
,
\r
,
\t
\n
(newline)
The following are valid examples:
foo\.com          # Matches "foo.com"
\d+\.\d+\.\d+     # Matches IP format
file\x2Etxt       # Matches "file.txt"
Character Classes
Syntax
Description
Example
.
Any character (except newlines)
a.c
to
abc
,
a1c
[abc]
Character set
[aeiou]
[^abc]
Negated character class
[^0-9]
[a-z]
Character range
[A-Za-z0-9]
\d
Digit
[0-9]
\d+
\D
Non-digit
[^0-9]
\D+
\w
Word character
[A-Za-z0-9_]
\w+
\W
Non-word character
\W+
\s
Whitespace
\s+
\S
Non-whitespace
\S+
\h
Horizontal whitespace
\h+
\H
Non-horizontal whitespace
\H+
\v
Vertical whitespace
\v+
\V
Non-vertical whitespace
\V+
The following are valid examples:
[0-9]{1,3}\.[0-9]{1,3}    # Matches first two octets of IP
\w+@\w+\.\w+              # Simple email matching
\d{4}-\d{2}-\d{2}         # Date format YYYY-MM-DD
Quantifiers
Syntax
Description
Equivalent
*
Zero or more times
{0,}
+
One or more times
{1,}
?
Zero or one time
{0,1}
{n}
Exactly
n
times
N/A
{n,}
At least
n
times
N/A
{n,m}
n
to
m
times
N/A
*?
Non-greedy zero or more
N/A
+?
Non-greedy one or more
N/A
??
Non-greedy zero or one
N/A
{n,m}?
Non-greedy range
N/A
The following are valid examples:
a*                # Matches "", "a", "aa", "aaa"
a+                # Matches "a", "aa", "aaa"
a?                # Matches "", "a"
a{3}              # Matches "aaa"
a{2,4}            # Matches "aa", "aaa", "aaaa"
a*?               # Non-greedy, prefers shortest match
<.*?>             # Matches HTML tags (non-greedy)
Anchors
Syntax
Description
^
Start of a string or line
$
End of a string or line
\A
Start of an absolute string
\Z
End of an absolute string
\z
End of a strict string
\b
Word boundary
\B
Non-word boundary
The following are valid examples:
^https://         # Must start with https://
\.com$            # Must end with .com
\bword\b          # Matches complete word "word"
^[a-z]+$          # Entire string must be lowercase letters
Groups and Alternation
Important
Groups in Hyperscan are non-capturing and don’t extract matched content.
Syntax
Description
Limitation
(abc)
Non-capturing group
This doesn’t capture content.
(?:abc)
Explicit non-capturing
N/A
a|b
Alternation (OR)
N/A
(a|b|c)
Grouped alternation
N/A
The following are valid examples:
(http|https|ftp)://       # Matches multiple protocols
(foo|bar)\.com            # Matches foo.com or bar.com
(?:www\.)?example\.com    # Optional www.
Inline Modifiers
Syntax
Description
(?i)
Case insensitivity
(?-i)
Turn off case insensitivity.
(?m)
Multi-line mode
(?s)
Single-line mode, i.e.,
.
matches a newline.
(?x)
Extended mode, i.e., ignore whitespaces.
The following are valid examples:
foo(?i)bar(?-i)baz      # Only bar is case-insensitive
(?i)case-insensitive    # Entire expression is case-insensitive
(?x) \d+ \. \d+         # Extended mode, spaces ignored
Unicode
Syntax
Description
\x{hhh}
Unicode code point
\p{L}
Unicode letters
\p{N}
Unicode numbers
\p{S}
Unicode symbols
\p{Z}
Unicode separators
\P{L}
Non-unicode letters
HS_FLAG_UTF8
UTF-8 mode
The following are valid examples:
\p{L}+                  # Matches letters in any language
\p{Han}+                # Matches Chinese characters
\x{1F600}               # Matches specific emoji
Special Constructs
Syntax
Description
\Q...\E
Literal block
(?#comment)
Comment
Unsupported Syntax for Regex
The following is not supported in destination profiles.
Syntax
Description
(?=abc)
Positive lookahead
(?!abc)
Negative lookahead
(?<=abc)
Positive lookbehind
(?<!abc)
Negative lookbehind
(abc)
capture
Extract matched content
\1
,
\2
Backreferences
(?<name>...)
Named capturing groups
\k<name>
Named backreferences
\g{n}
Relative backreferences
(?(condition)yes|no)
Conditional matching
(?(1)yes|no)
Group-based conditional
(?(R)yes|no)
Recursion conditional
(?R)
Recurse entire pattern
(?1)
Call subpattern
(?&name)
Call named subpattern
(?P>name)
Python-style recursion
\G
Last match end position
\K
Keep to left side
(*UTF)
UTF mode declaration
(*UCP)
Unicode properties
(*ACCEPT)
Accept match immediately
(*FAIL)
Force failure
(*SKIP)
Skip
(*PRUNE)
Prune
(*COMMIT)
Commit
Examples for Regex
The following are examples of valid regex patterns.
Example Regex Patterns for Multiple TLDs
The following are examples of regex expressions for matching Google searches on any supported TLD from the
Google list of supported domains
.
Example 1
This is an example of matching to all domains with an OR condition.
^(www\.)?google\.(com|ad|ae|al|am|as|at|az|ba|be|bf|bg|bi|bj|bs|bt|by|ca|cd|cf|cat|cg|ch|ci|cl|cm|cn|cv|cz|de|dj|dk|dm|dz|ee|es|fi|fm|fr|ga|ge|gg|gl|gm|gp|gr|gy|hn|hr|ht|hu|ie|im|iq|is|it|je|jo|ki|kg|kz|la|li|lk|lt|lu|lv|md|me|mg|mk|ml|mn|mu|mv|mw|ne|nl|no|nr|nu|pl|pn|pt|ro|ru|rw|sc|se|sh|si|sk|sn|so|sm|sr|st|td|tg|tl|tm|tn|to|tt|vg|vu|ws|com\.(af|ag|ai|ar|au|bd|bh|bn|bo|br|bz|cu|cy|do|ec|eg|et|fj|gh|gi|gt|hk|jm|kh|kw|lb|lc|ly|mm|mt|mx|my|na|ng|ni|np|om|pa|pe|pg|ph|pk|pr|py|qa|sa|sb|sg|sl|sv|tr|ua|uy|vc|ve|vn)|co\.(ao|bw|ck|cr|id|il|in|jp|ke|kr|ls|ma|mz|nz|th|tz|ug|uk|uz|ve|za|zm|zw))(/|$)
Example 2
This is an example of a broader TLD match.
^(www\.)?google\.(com?\.)?[a-z]{2,3}(/|$)
To match only the
/search
path:
^(www\.)?google\.(com?\.)?[a-z]{2,3}/search
Example Regex Pattern for Query
This is an example of blocking the keyword
forbidden
from a Google search.
^(www\.)?google\.(com?\.)?[a-z]{2,3}/search\?([^&]*&)*q=[^&]*forbidden([^&]*)
Example Regex Pattern for Keyword in Domain Name
This is an example of blocking the keyword
forbidden
anywhere in a domain name.
^[^/?]*forbidden[^/?]*(/|$)
In this Topic
Adding Network Targets to Destination Profiles

---
## Traffic Steering
**URL:** https://docs.netskope.com/en/traffic-steering/
**Last Modified:** 2026-06-02T04:03:25+00:00
**Scraped:** 2026-06-28T09:32:10.276938+00:00

Traffic Steering - Netskope Knowledge Portal
Traffic Steering
To direct end-user traffic to the Netskope Cloud, go to
Settings > Security Cloud Platform > Traffic Steering
in the Netskope UI to create and manage cloud application and web traffic steering configurations.
Netskope Client
App Definitions
Steering Configuration
Borderless SD-WAN
IPSec
GRE
NewEdge Express Connect
Explicit Proxy
Explicit Proxy over IPSec and GRE Tunnels
Proxy Chaining
IPv6 Traffic Steering
Locating Your Netskope NewEdge Data Center
NewEdge IP Ranges for Allowlisting
Enterprise Browser
In this Topic
Traffic Steering
