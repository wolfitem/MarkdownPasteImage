import sublime, sublime_plugin
import re,os,datetime, sys, platform

# 配置文件
SETTING="markdown_paste_image.sublime-settings"
class MarkdownPasteImageCommand(sublime_plugin.WindowCommand):
  def run(self):

    settings=sublime.load_settings(SETTING)

    clip=settings.get('default_clip')

    proj=settings.get('current_proj')

    img_dir=settings.get(proj+'_img_dir')

    root_dir=settings.get(proj+'_root_dir')

    filename=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
   
  
    if os.name == "posix":
       path=img_dir+ "/"+filename
       result=(self.run_shell(clip+" "+path,"UTF-8"))
       img_tag=path.replace(root_dir+"/",'');
       self.insert_img_tag(img_tag)
    else:
       print(os.name)
       path=img_dir+ "\\"+filename
       result=(self.run_shell_win(clip+" "+path,"GB2312"))
       img_tag=result.replace(root_dir+"\\",'').replace("\\","/");
       self.insert_img_tag(img_tag)
    

  def insert_img_tag(self,file_path):
    # 获取Sublime环境
    syntax=self.get_syntax()
    settings=sublime.load_settings(SETTING)

    proj=settings.get('current_proj')

    default_desc=settings.get('default_desc')
    key=proj+"_"+syntax+'_tag'
    if settings.has(key):
        img_tag = settings.get(key)
    else:
        img_tag = settings.get('default_tag')

    img_tag = img_tag.format(src=file_path,desc=default_desc)
    self.window.active_view().run_command('insert', {'characters': img_tag})

  # 获取当前视图的文档类型
  def get_syntax(self):
    result = self.window.active_view().settings().get('syntax')
    print('syntax:'+result)
    # old version
    result2 = re.sub('^.*\/(.*)\.tmLanguage', r'\1', result)

    # 当版本为 Build 3103 时，syntax返回值：Packages/Markdown/Markdown.sublime-syntax
    if (result2 is result):
      result2=result.split('/')[1]
    return result2

  # 执行Shell
  @staticmethod
  def run_shell(cmd,codetype):
    print("cmd:"+cmd)
    from subprocess import Popen, PIPE
    result= Popen(cmd, shell=True,universal_newlines=True,  stdout=PIPE).stdout.read()
    if len(result)>0:
      return  result.decode(codetype)
    return ""

  @staticmethod
  def run_shell_win(cmd,codetype):
    from subprocess import Popen, PIPE
    result= Popen(cmd, shell=True, stdout=PIPE).stdout.read().decode(codetype).splitlines()
    return result[0]

