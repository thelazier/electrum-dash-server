from setuptools import setup

setup(
    name="electrum-dash-server",
    version="1.0",
    scripts=['run_electrum_dash_server.py','electrum-dash-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0', 'x11_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="Bitcoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum Lightweight Bitcoin Wallet"""
)
