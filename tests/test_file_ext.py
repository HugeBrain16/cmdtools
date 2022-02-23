import cmdtools
from unittest import IsolatedAsyncioTestCase
from cmdtools.ext.file import ModuleLoader


class TestFileExt(IsolatedAsyncioTestCase):
    async def test_load_module(self):
        mod = ModuleLoader("tests.assets.cmdmod", load_classes=False)
        out = await mod.run(cmdtools.Cmd("/cmdmod"))

        self.assertEqual(out, 1234)
    
    async def test_load_class(self):
        mod = ModuleLoader("tests.assets.cmdmod")
        out = await mod.run(cmdtools.Cmd("/cmdmod"))
        
        self.assertEqual(out, 1234)
