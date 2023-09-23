# Disclaimer
Notwithstanding anything that may be contained to the contrary in your agreement(s) with Sysdig, Sysdig provides no support, no updates, and no warranty or guarantee of any kind with respect to these script(s), including as to their functionality or their ability to work in your environment(s). Sysdig disclaims all liability and responsibility with respect to any use of these scripts.

# report-download
A simple script to demonstrate how to query the Sysdig API to download the latest vulnerability report.

# Configuration
report-download does not require a configuration file but does take a few parameters

| Parameter | Description | Example |
| - | - | - |
| --api / -a | The API url of your instance | --api https://app.au1.sysdig.com |
| --token / -t | The user / service apI token to use | --token 538346ca-ce3a-4327-bffb-7be45b7dfffe |
| --id / -i | The ID of the report you wish to download the latest one of | --id MRHbmCyvuxidG3Y49RNmFfHihER |

** API token can also be specified via the `SECURE_API_TOKEN` environment variable

** APi URL can also be specified via the `API_URL` environment variable

# Execution Example
By executing
`python3 report-download.py --api <API URL> --token <api token>` you will be presented with a list of reports and their ID's

```
Name: 'SockShop Vulns', Id: '2VnL4sChV0yXfsCxc3rocjUUmje'
Name: 'Sample Report - New', Id: '2RH6mDy9uxinG3Yq9RNmcfHihEN'
```

From here we can get the ID od the report that we wnat to download and run it again with the `--id` specified
`python3 report-download.py --api <API URL> --token <api token> --id 2RH6mDy9uxinG3Yq9RNmcfHihEN`

and we are presented with the CSV report in question having downloaded it in gzip format, decompressed it, then displayed it to the terminal.  You can of course redirect this output to a file and process further if you wish

```
Vulnerability ID, Severity, Package name, Package version, Package type, Package path, Image, OS Name, CVSS version, CVSS score, CVSS vector, Vuln link, Vuln Publish date, Vuln Fix date, Fix version, Public Exploit, K8S cluster name, K8S namespace name, K8S workload type, K8S workload name, K8S container name, Image ID, K8S POD count, Package suggested fix, In use, Risk accepted
CVE-2017-8046, Critical, org.springframework.boot:spring-boot, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-actuator, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-actuator-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-autoconfigure, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-autoconfigure-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter-actuator, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-actuator-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter-aop, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-aop-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter-data-mongodb, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-data-mongodb-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter-data-rest, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-data-rest-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter-logging, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-logging-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2017-8046, Critical, org.springframework.boot:spring-boot-starter-tomcat, 1.4.4.RELEASE, java, /usr/src/app/app.jar:BOOT-INF/lib/spring-boot-starter-tomcat-1.4.4.RELEASE.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.0, 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2017-8046, 2017-09-08, 2017-09-11, 2.0.0M4, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.0.0M4, true, false
CVE-2020-8840, Critical, com.fasterxml.jackson.core:jackson-databind, 2.8.6, java, /usr/src/app/app.jar:BOOT-INF/lib/jackson-databind-2.8.6.jar, weaveworksdemos/carts:0.4.8, alpine 3.4.6, 3.1, 9.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, https://nvd.nist.gov/vuln/detail/CVE-2020-8840, 2020-02-09, 2020-02-09, 2.8.11.5, true, kubernetes, sock-shop, deployment, carts, carts, sha256:c004737361182d3cd7f38e6d9ce4a44f2a349b8dc996834e2cba0defcd0cb522, 1, 2.9.10.4, true, false

```
