import json
import requests

def handler(request):
    if request.method != 'POST':
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "POST only"})
        }
    
    try:
        body = json.loads(request.body)
        vpa = body.get('vpa')
        if not vpa:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "VPA required"})
            }

        url = "https://www.amazon.in/apay/money-transfer/verify-vpa/v2"
        
        payload = {
            "recipientVpa": vpa,
            "clientContext": {
                "pageType": "EAP",
                "useCase": "SEND_MONEY"
            }
        }
        
        headers = {
            'User-Agent': "Amazon.com/30.22.0.300 (Android/15/V2509)",
            'Accept': "application/json; charset=utf-8",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua-full-version-list': "",
            'sec-ch-ua-platform': "\"Android\"",
            'viewport-width': "384",
            'device-memory': "8",
            'sec-ch-ua': "\"Not:A-Brand\";v=\"99\", \"Android WebView\";v=\"145\", \"Chromium\";v=\"145\"",
            'sec-ch-dpr': "1.875",
            'sec-ch-ua-mobile': "?1",
            'content-type': "application/json; charset=utf-8",
            'sec-ch-viewport-width': "384",
            'downlink': "10",
            'ect': "4g",
            'sec-ch-device-memory': "8",
            'dpr': "1.875",
            'rtt': "0",
            'sec-ch-ua-platform-version': "\"\"",
            'origin': "https://www.amazon.in",
            'x-requested-with': "in.amazon.mShop.android.shopping",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.amazon.in/apay/money-transfer/assets/ap4-eap/index.html",
            'accept-language': "en-IN,en-US;q=0.9,en;q=0.8",
            'priority': "u=1, i",
            'Cookie': "lc-acbin=en_IN; mobile-device-info=dpi:300.0|w:720|h:1600; amzn-app-id=Amazon.com/30.22.0.300/18.0.582129.0; i18n-prefs=INR; ubid-acbin=258-0293424-2815116; session-id=259-7081962-2819512; sid=; at-acbin=\"Atza|gQCtzrCGAwEBAj49e4rnUxcUPwvI2iGLbEpdA2TZmORJoNtuoVI4bq7YczbLfVb1sw4ku49PYoCBe2_DE8JOgp2SRoQ0DSvjCd-1bFprgBOFEnSLIGO7LQ5ze1THDDMbNE6JkaPTpjeMgVzct-JQR3r3rzvuZ9_rPI2IcLbhcUvpgo1Zx6kAfqmXDb0EutA4DFCEIoDYCQ__-1Jm_UHKjRXJrcI36_ta1BQxnaV6YdRbL81yl7MncrK8iQ-VjpRZO7iDplMPu5PNoFU9ucSDOdecTzGQvuwTChlmkomp_Cr9IuEJll0wMAx3eQxenjzQ-HdgKsZaoGeP9bp_NI3ad3uRUpsLW7A7x5q2ZLiSHL2p6D4ZLAvciQwwazwwdR49QTAEd8KpVjPfi4xi7pS05aOUx2a0QMUbpYuGDvtXvBlaQp3HV0dEtyS1wWaRqpVMmFLFlC3FFliuK-p1HGkaNs8fS3_RGEvlGKM9QQq8-GBztRfRe-Y\"; sess-at-acbin=\"V+DhprjkoLO3Zz1mR+qA0d9sR0cXrZwygqY8yE44xcw=\"; session-id-time=2082787201l; Domain=.amazon.in; Path=/; panch-token=eyJ0IjoxNzY2MDU5NTMwLCJ1bCI6W10sImlkIjoiNThjZDk4YWNlZDIxZThjMjc1MzZkNTcwZjc0MmJhMmUiLCJ2IjoxfQ==; privacy-consent=%7B%22avlString%22%3A%22%22%2C%22gvlString%22%3A%22%22%2C%22amazonAdvertisingPublisher%22%3Atrue%7D; Version=1; Max-Age=31536000; Expires=Tue, 19-Jan-2027 18:06:52 GMT; x-acbin=\"CcMttnTrHM3wwpWBRZ6ILOkk0qCbXfFOjjsSsnvxQhXCssMo@nEDbpR3YRAbG61z\"; amzn-app-ctxt=1.8%20%7B%22an%22%3A%22Amazon.com%22%2C%22av%22%3A%2230.22.0.300%22%2C%22xv%22%3A%221.16.0%22%2C%22os%22%3A%22Android%22%2C%22ov%22%3A%2215%22%2C%22cp%22%3A788760%2C%22uiv%22%3A4%2C%22ast%22%3A3%2C%22nal%22%3A%221%22%2C%22di%22%3A%7B%22pr%22%3A%22V2446iC%22%2C%22md%22%3A%22V2509%22%2C%22v%22%3A%22V2446%22%2C%22mf%22%3A%22vivo%22%2C%22dsn%22%3A%222df8901a9ca34ef48e1fc70480e942d4%22%2C%22dti%22%3A%22A1MPSLFC7L5AFK%22%2C%22ca%22%3A%22%22%2C%22ct%22%3A%22MOBILE%22%2C%22mct%22%3A13%7D%2C%22dm%22%3A%7B%22w%22%3A720%2C%22h%22%3A1600%2C%22ld%22%3A1.875%2C%22dx%22%3A265.7669982910156%2C%22dy%22%3A259.02099609375%2C%22pt%22%3A0%2C%22pb%22%3A78%7D%2C%22is%22%3A%22com.google.android.packageinstaller%22%2C%22msd%22%3A%22.amazon.in%22%7D; rxc=ADj0AqUSZ7ON8r3yYZU; session-token=VpKpW0kkLbYhCoH1IhYgmDkVGerV0YsBvBnJhU+htecJbmO/H63b5h47CLNlcmJKqGchAMtJc6MogIeX1VrPksfceSO2yaFeJIyNNnWBdIh6lzAnkTvb6AzWCFsRhM7D/5aDvO1TuJWeOLgw6O5Ub0ufrA41u3eoWKwi4cpH+DzA28S0eriPIT6a4+zKHYT5aeFAlWd62sv8sy54SY4F/OvI/FOvDv8KlLOC2z3DN4FNsCZod3IqtRbYr8vmruH8mx+oSrz+y5FK9sh+lJmbXrU1y6j4UfasRr2sb3qTEkeRCWuS1+ualjstAre1Tn+nBNCKkD5GcsIPcQOGNE8kBlhWi7WieKjewdGS6bhp03XFSUkxpg2MIUspWD8xDk7Q; csm-hit=tb:s-078D2AD48965425EBB54|1769320210453&t:1769320210662&adb:adblk_no"
        }
        
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        data = response.json()
        data["developer"] = "@Oriss01"
        
        return {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e), "developer": "@Oriss01"})
        }
