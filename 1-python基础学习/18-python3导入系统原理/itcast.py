import sys
from importlib.abc import MetaPathFinder
from importlib.abc import Loader
from importlib.machinery import ModuleSpec

import os

# sys.path
# sys.meta_path


class Myloader(Loader):

    def create_module(self, spec):
        #print(spec.name)
        return None


    def exec_module(self, module):
        """
        需要我们自己设置 模块的 __path__ __file__ __loader__
        __package__ 属性 解释器会自动帮我们设置好
        """
        load_path = module.__spec__.origin

        sys.modules.setdefault(module.__spec__.name, module)

        module.__file__ = load_path  # 必须设置
        module.__loader__ = self

        if load_path.endswith("__init__.py"):
            # 如果是包, 必须设置 __path__，如果是模块，不能设置
            module.__path__ = [load_path[:-12]]


        code = self.get_code(load_path)

        print('模块的__package__值：', module.__package__)
        #print('模块的__name__值：', module.__name__)
        #print('模块的__file__值：', module.__file__)

        exec(code, module.__dict__)


    def get_code(self, file_path):

        with open(file_path, 'r') as f:
            code = f.read()

        return code


loader = Myloader()

class Myfinder(MetaPathFinder):


    def find_spec(self, fullname, path, target=None):
        # print('------分割---------')
        # print("fullname:", fullname)
        # print("path:", path)

        # 如果 fullname 是 pack 那么 last_mile 就是 'pack'
        # 如果 fullname 是 pack.music 那么 last_mile 就是 'music'
        last_mile = fullname.split('.')[-1]


        if path == None:
            # 导入的是 顶级包，例如：import pack
            serach_path = sys.path

        else:
            # 如果导入的是模块或者子包
            serach_path = path

        for path_temp in serach_path:
            full_path = os.path.join(path_temp, last_mile)
            init_full_path = os.path.join(full_path, '__init__.py')
            module_full_path = full_path + '.py'

            if os.path.exists(full_path) and os.path.isfile(init_full_path):
                # 导入 包
                return ModuleSpec(fullname, loader=loader, origin=init_full_path, is_package=True)


            if os.path.isfile(module_full_path):
                # 导入 模块
                return ModuleSpec(fullname, loader=loader, origin=module_full_path, is_package=False)


#sys.meta_path.append(Hehe)
# sys.meta_path.clear()
sys.meta_path.insert(0,Myfinder())
#print(sys.meta_path)
#print(sys.path_hooks)

#import pack.start

import pack.music.beyond

#pack.music.beyond.xihuanni()




