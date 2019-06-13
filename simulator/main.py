import asyncio
import atdome.simulator as atdome
import emitters.simulator as emitters

if __name__=='__main__':
    print('main simulator')
    loop = asyncio.get_event_loop()
    asyncio.get_event_loop().run_until_complete(asyncio.wait([
        emitters.main(loop),
        atdome.main()
    ]))