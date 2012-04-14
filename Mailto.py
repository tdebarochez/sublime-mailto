import sublime
import sublime_plugin
import os
import sys
import subprocess
import locale

class MailtoCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    try:
        settings = sublime.load_settings('Mailto.sublime-settings')
        self.run_bin(settings.get('command'))

    except (Exception) as (exception):
        sublime.error_message(__name__ + ': ' + str(exception))

  def run_bin(self, parameters):
    try:
        if not parameters:
            raise NotFoundError('parameters not found')
        for k, v in enumerate(parameters):
            parameters[k] = v.replace('%d', self.getCurrentDirectory())
            parameters[k] = v.replace('%f', self.getCurrentFileName())
        args = parameters
        encoding = locale.getpreferredencoding(do_setlocale=True)
        subprocess.Popen(args, cwd=self.getCurrentDirectory())

    except (OSError) as (exception):
        print str(exception)
        sublime.error_message(__name__ + ': command was not found')
    except (Exception) as (exception):
        sublime.error_message(__name__ + ': ' + str(exception))

  def getCurrentFileName(self):
    return self.view.file_name()

  def getCurrentDirectory(self):
    return os.path.dirname(self.view.file_name())