from flask import request
import requests

r = requests.get('https://media.twiliocdn.com/fax/AC83e3c0d39086dfbc88a3be57c9d53639/c2caf8802c1c7736b8ed9e091908e8df6a40caec1b65caa5572315b23e424c5650186ee042919a0a3291513bd11f025e00fd67f522176c4485abeeb77de5b4f8?x-amz-security-token=FQoDYXdzEGUaDIPeLH0S1gqe9irYEyK3A8YKOWjv728OGcYKvwYmBLLg7LkhIJfrWQCmjY94tXHkAT0nL7x1D%2FknCepfGoXeYgrp7DfWDWUtbGatb0T49JdEQTZ%2FkBTTPHAxjGbfqAPbjD%2BgyNDNRDXrEuKbttFWKPf%2FuJ2dCu2Gxib0yZYugWxw2aCMB30w4fexYsgaXogz63NHqxgatxfXX1iNluaEZZNPfmggdNhd1KgXmBnbpTi0o1MUbrL1dkn%2FAuP6vecaf9dux4puNdkOG5iOwru4KcPTTLjb7s7TNgLaEJZZq7GdwF6WNicevQvFUq4BQ%2FKWhz5I3ZBuBAzIpMaoNyysLjBO607e8qCPFHwJfFOLl160fQ2Y2REEi1fgcpmxInqzpmJ8uO2Yajb2cZm9VnhSZdAWZnY8IaaOKkSkjWHsi%2B1SpeEcF9zGXc2xciesNYdcCgjyUn218zKIBTtNEyPiYRz9L2gervtySk7rZlOVIkmkOmUYCMaHJqZ%2FkjK2HgVTHca8xV7XhALD3gvooViK5XW9ppmkCa2GkCIOrj%2BLXaQjDOCdyzwjsTkryxh6P%2BSJfvoFyCKSmcH4mHOLJVWpLu3m6qrZmyco0vab0QU%3D&AWSAccessKeyId=ASIAIVKTZRK5XYOP23BQ&Expires=1512516501&Signature=QjcX1cWKCxr5fbL%2FuGq5oPIZ6Hc%3D')

with open('media1.pdf', 'wb') as f:
    f.write(r.content)