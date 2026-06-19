# Door-Camera
Using Raspberry Pi Zero 2W to create a live stream door camera

[Set up guide for Raspberry pi 2W](https://youtu.be/iYhmq2X2RbY?si=JlnEOvKoJYm1JwLa)




Hardware:
    
-[Raspberry Pi Zero 2W](https://www.amazon.com/gp/product/B0GQLZ79X7/ref=ox_sc_act_title_3?smid=A162CA6IT8O3HK&psc=1)
	
-[Pi Camera Module V3](https://www.amazon.com/gp/product/B0BRY6MVXL/ref=ox_sc_saved_title_1?smid=A7OUC2NYX9CZ5&th=1)
   
-MicroSD card
    
-[PiSugar 3 1200mAh Raspberry Pi Zero Battery](https://www.pisugar.com/products/pisugar-3-raspberry-pi-zero-battery)

-[5V/3A USB-C wall charger](https://www.amazon.com/Security-01-Supply-Adapter-Type-C-MLF-C060503000CU/dp/B09JW4QQJ2/ref=sr_1_4?crid=1YJ29VLFE84HJ&dib=eyJ2IjoiMSJ9.JaGr0MwNdfMiot8xTIqi3XfrP2gUp7byW1RfTvoGLIXrHw3r8i0faNYAjs_6FbArNYTBGlK5TgJmV3O07PsuQKZSwEnYtAJjGALuqd0qiGTPM4jGkNGRexeuFg9wQVhHuTOczCAtr6fbH5PTV9gN2EsK4wItajlHV3xkr9-T2ozWtZ3KcHAa9Is49ILPbymKTunngO2fkVqegCEtQDESp0ztLY-ZQPtmpO1fA3NOHJR2Go7J9yAc61F9Gk0gH5UJCS2UOGTmIlQWzpy61yRvBe3XfIR8b1Ot8HK5GtLUz4U.FatTxyPwcbVLG4Wrvmuy72KghwgRrTNowTKdxK9zWIU&dib_tag=se&keywords=5V%2F3A%2BUSB-C%2Bwall%2Bcharger&qid=1781871763&s=electronics&sprefix=%2Celectronics%2C417&sr=1-4&th=1)
    
-[5V/3A LED wall charger](https://www.amazon.com/Belker-Adapter-Supply-Charger-Devices/dp/B08ZSTRDM8/ref=sr_1_25?crid=1YJ29VLFE84HJ&dib=eyJ2IjoiMSJ9.NeIlwrjx4Yk_uYVGwycXr8mjZEANMhgM5vkNdTlZPxI1NDKD4T0OL5jZrQ0ytvLgVZzC8ZnoQZidx3BcJwLcVqD31ri3GEy3UwDk2yhfNXl8TRwUscYjnMb726YxkkMc7sclopYzpqp5FSOAzCFC6sqQMLLqxYBOrCs10kylY0pg4XbTeeyoNS_TgHGEeTgZmAChs2Jk9cL098KTij0jkApq6mKmrEdP6pnt2ecbYiD4jxc4PFB4CN_McBYlYe37Hoh2YR5W3Y2GUKVwajdFl8aMePTvVA3bQu5wYEkgSmw.BK7XZIh77ZHIM3ZKKRhh9-1IsWxAGZXe_p9eejNXJSY&dib_tag=se&keywords=5V%2F3A%2BUSB-C%2Bwall%2Bcharger&qid=1781872172&s=electronics&sprefix=%2Celectronics%2C417&xpid=cI__07ZRsfwm9&th=1)

-(USB-C Pigtail cable)[https://www.amazon.com/Vovucai-USB-Pigtail-Cable-Connector/dp/B0F31YWTMF/ref=sr_1_1?crid=1RXQQ2EZ76NCP&dib=eyJ2IjoiMSJ9.yyjKrLNPQ4Wdq5RnwHoek245IVgjFG8n1iztcM-Ym4VwS-_U2UUXfrBoRNkN2BWY8cXcdICQR2KUNG_lTAA-5rXNFhr-jXZvmLSDBVDODbiZC0OzXdMSgrKDr_cwk3WsxxijoRiEh8cY8kbyw4LVsaHSNlM4Fh4qoMy-w_m1lRk_8zkASVMQQKvZdJgXj6wL0O4QPGELIZ2MiP6Bkx7Vjo6IB3SeebSSYbPPit5MyETFLU8U13DZol4s6p14ts_CnNjYCnd1c_zz-rO_sm68x4Wafp9YclCn0nBwHVaGjPA.-Skt563I0eEZNAuy-rFlMaZvZyd1cWROdzKyuweaItw&dib_tag=se&keywords=LED%2Bterminal%2Bto%2Busbc&qid=1781877367&s=electronics&sprefix=led%2Bterminal%2Bto%2Bu%2Celectronics%2C648&sr=1-1&th=1]

-(Micro USB Pigtail cable)[https://www.amazon.com/Jxiwfvl-Micro-Pigtail-Power-Cable/dp/B0G29MJ8XR/ref=sr_1_2?crid=1W8J4ZO59SIUN&dib=eyJ2IjoiMSJ9.nZXEPtF3nylkFBEfrjXk01WGw9xAxQfQ7t_RRYHuiDYGVaDteLU2I6-FrDYWKfFaeQULepPl-ai1PTeCE7Yc3EyLvxrEle-nb8O2WsawoWZEE7jznyJZFOP4gz-qpvURWbNw5da-3tDkeWNSJjT3HuAgFZy39Oe-zcL2BAN8hVecbnSyo_pXTgjqx046nmeM6mx9SjbZ7ZE76IBWBI2RoNHhtj_vWjxqTqXuGOKZCos._2NQsQg0UpRX7Ie-i4aGyokqTYHi125kbA__LIXb_1Q&dib_tag=se&keywords=Micro+usb+pigtail+wire&qid=1781879866&sprefix=micro+usb+pigtail+%2Caps%2C682&sr=8-2]


Software:
    
-Raspberry pi 2 W:
    
----[Raspberry Pi Imager to download Raspberry Pi OS Lite](https://www.raspberrypi.com/software/)
        
----[Picamera2](https://pip-assets.raspberrypi.com/categories/652-raspberry-pi-camera-module-2/documents/RP-008156-DS-2-picamera2-manual.pdf)

----[MediaMTX](https://mediamtx.org/)


	
-App:

----[VLC media player](https://apps.apple.com/us/app/vlc-media-player/id650377962)


