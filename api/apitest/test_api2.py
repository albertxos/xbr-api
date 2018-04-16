import asyncio

from autobahn.wamp.interfaces import ISession

from xbr.hub.mobility import IRoadTracker


async def run(session: ISession = None) -> None:
    call = await IRoadTracker.welcome.call(session, IRoadTracker.welcome.Params('Joe', 9, .3))
    result = await call.result

    print('msg="{}", duration={}'.format(result.msg, result.duration))

    call = await IRoadTracker.welcome.call(session, IRoadTracker.welcome.Params('Jack', 3))
    result = await call.result  # type: IRoadTracker.welcome.Result

    print('msg="{}", duration={}'.format(result.msg, result.duration))


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
