import os.path
#import pdflatex
import pandas as pd
import numpy as np
import datetime
import json
import statsmodels.api as sm
import re
import shutil
import warnings
#import jqdatasdk
#from jqdatasdk import *
import pymysql
# import calender
# import dataframe_image
import pylatex
import datetime
#from pylatex import Document, Section, Subsection, Command,Package
#from pylatex.utils import italic, NoEscape
from pylatex import Document,Section,Subsection,Command,Package,Tabular, LongTabu,LongTable, MultiColumn, HFill,Figure
from pylatex.utils import italic, NoEscape
import math
#import multiprocessing

warnings.filterwarnings("ignore")
from statsmodels.regression.rolling import RollingOLS

def get_path(path):
    path_to_get = path
    if not os.path.exists(path_to_get):
        os.makedirs(path_to_get)
        return path_to_get
    else:
        return path_to_get
class py_latex():
    with open('parameters.json','r') as f:
        parameters = json.load(f)

    def get_resume_english(self):
        print(" start creating english resume tex file in pylatex")
        root_path = os.path.abspath(os.path.dirname(__file__))
        # 由于Mac系统的限制，无法直接使用相对路径添加模式，需要使用os.path.join
        path_temp = os.path.dirname(root_path)
        path_report = get_path(os.path.join(path_temp, "resume", "english"," "))
        # path_report = get_path(os.path.dirname(root_path) + '\\resume\\yuchen\\')

        doc = Document(default_filepath=path_report, documentclass='article')

        # 加载会用到的包
        # doc.packages.append(Package( "amssymb, latexsym, amsmath, amsthm, verbatim, graphicx, epstopdf, epsfig")
        # 调整页面边距
        doc.packages.append(Package("geometry"))
        doc.packages.append(NoEscape(r"\geometry{a4paper,total={170mm,257mm},left=20mm,top=20mm}"))

        doc.packages.add(Package("latex"))  # 更换解释器
        # doc.packages.append(Package("ctex"))

       

        doc.append(NoEscape(r"\begin{center}"))  # 居中
        doc.append(NoEscape(r"\MakeUppercase{\huge\textbf{resume}}"))  # 简历title
        doc.append(NoEscape(r"\\"))
        doc.append(NoEscape(r"\end{center}"))

        doc.append(NoEscape(r"\begin{flushleft}"))  # 开始左对齐
        doc.append(NoEscape(r"\large name\\xxxx@xxxx.com\\+xx xxxxxxxxxxx"))  # 姓名/电话/邮箱方式
        doc.append(NoEscape(r"\end{flushleft}"))

        doc.append(NoEscape(r"\\"))  # pylatex grammar needs another line

        doc.append(NoEscape(r"\rule[4pt]{18cm}{0.5pt}"))  # 下划线
        doc.append(NoEscape(r"\\"))
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{Job Intention: xxxxxxx}}"))  # 求职意向
        doc.append(NoEscape(r"\\"))

        doc.append(NoEscape(r"\rule[4pt]{18cm}{0.5pt}"))  # 下划线
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{Work Experience}}"))  # 工作经验
        doc.append(NoEscape(r"\end{flushleft}"))  # 结束左对齐
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行

        # 工作 1
        doc.append(NoEscape(

            r"\MakeUppercase{\small\textbf{title 1}}" 
            r"\hfill"
            r"\MakeUppercase{\footnotesize\textbf{company 1}}"
            r"\hfill"
            r"\MakeUppercase{\small\textbf{working period}}"))
        # itemsize 会自动空行 开始bullet point
        doc.append(NoEscape(r"\begin{itemize}"))
        # 工作职责
        doc.append(NoEscape(
            r"\item{\normalsize{work 1}}"
            r"\item{\normalsize{work 2}}"
            r"\item{\normalsize{work 3}}"
            r"\item{\normalsize{work 4}}"
        ))
        doc.append(NoEscape(r"\end{itemize}")) # 结束bullet point
        doc.append(NoEscape(r"\\"))  # 空行
        # 工作 2
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{title 2}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\footnotesize\textbf{company 2}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\small\textbf{working period}}"))

        doc.append(NoEscape(r"\begin{itemize}"))
        # 工作职责 2
        doc.append(NoEscape(
            r"\item{\normalsize{work 1}}"
            r"\item{\normalsize{work 2}}"
            r"\item{\normalsize{work 3}}"
            r"\item{\normalsize{work4}}"
        ))
        doc.append(NoEscape(r"\end{itemize}"))

        doc.append(NoEscape(r"\\"))  # 空行

        # 工作 3
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{title 3}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\footnotesize\textbf{company 3}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\small\textbf{working period}}"))

        doc.append(NoEscape(r"\begin{itemize}"))
        # 工作职责 3
        doc.append(NoEscape(
            r"\\"
            r"\item{\normalsize{work 1}}"
            r"\item{\normalsize{work 2}}"
        ))
        doc.append(NoEscape(r"\end{itemize}"))

        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行

        doc.append(NoEscape(r"\begin{flushleft}"))  # 左对齐环境
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{education}}"))  # 学习经历
        doc.append(NoEscape(r"\end{flushleft}"))  # 结束左对齐
        doc.append(NoEscape(r"\\"))  # 空行

        # 学校 1
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{diploma 1}}"
            r"\hfill"
            r"\MakeUppercase{\small\textbf{xxxx University}}"
            r"\hfill"
            r"\\"
            r"\MakeUppercase{\normalsize\textbf{study time}}"
            r"\hfill\MakeUppercase{\small\textbf{GPA: /4.0}}"
        ))
        # 左对齐环境
        doc.append(NoEscape(r"\begin{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\normalsize\textbf{main course}}")) #主要课程
        doc.append(NoEscape(r"\end{flushleft}")) # 结束左对齐环境

        # 课程
        doc.append(NoEscape(
            r"\parskip{course 1, course 2, course 3}"))
        # 翻页
        doc.append(NoEscape(r"\newpage"))

        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行

        # 学校 2
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{diploma 2}}}"
            r"\hfill"
            r"\MakeUppercase{\small\textbf{xxxx University}}"
            r"\hfill"
            r"\\"
            r"\MakeUppercase{\normalsize\textbf{study time}}"
            r"\hfill\MakeUppercase{\small\textbf{GPA:  /4.0}}"

        ))

        doc.append(NoEscape(r"\begin{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\normalsize\textbf{main course}}"))
        doc.append(NoEscape(r"\end{flushleft}"))
        doc.append(NoEscape(
            r"\parskip{course 1, course 2, course 3}"))

        doc.append(NoEscape(r"\\\hspace*{\fill}\\")) # 空行
        doc.append(NoEscape(r"\begin{flushleft}"))  # 左对齐
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{research}}"))  # 研究
        doc.append(NoEscape(r"\end{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\small\textbf{theme}}"))
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))
        doc.append(NoEscape(
            r"\the theme of your research"
            r"\\"
            r"\parskip{details of your research}"
        ))
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行
        doc.append(NoEscape(r"\begin{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{skill}}"))  # 技能
        doc.append(NoEscape(r"\end{flushleft}"))

        # 技能相关
        doc.append(NoEscape(r"\begin{itemize}"))
        doc.append(NoEscape(
            r"\item{\normalsize{skill 1-- Skillful}\hfill{ Time of use: xx months}}"
            r"\item{\normalsize{skill 2-- Proficient}\hfill{Time of use: xx months}}"
            r"\item{\normalsize{skill 3-- Skillful}\hfill{Time of use: xxx months}}"

        ))

        doc.append(NoEscape(r"\end{itemize}"))
        doc.append(NoEscape(r"\end{documnet}"))

        doc.generate_pdf(filepath=path_report, compiler='pdfLaTex', clean_tex=False)
        # doc.generate_pdf(filepath=path_report)
        doc.generate_tex(filepath=path_report)
        # doc.generate_pdf(filepath=path_report,compiler='xelatex',clean_tex=False)

        print('...')

    def get_resume_chinese(self):
        print(" start creating chinese resume tex file in pylatex")
        root_path = os.path.abspath(os.path.dirname(__file__))
        # 由于Mac系统的限制，无法直接使用相对路径添加模式，需要使用os.path.join
        path_temp = os.path.dirname(root_path)
        path_report = get_path(os.path.join(path_temp, "resume", "chinese"," "))
        # path_report = get_path(os.path.dirname(root_path) + '\\resume\\yuchen\\')

        doc = Document(default_filepath=path_report, documentclass='article')

        # 加载会用到的包
        # doc.packages.append(Package( "amssymb, latexsym, amsmath, amsthm, verbatim, graphicx, epstopdf, epsfig")
        # 调整页面边距
        doc.packages.append(Package("geometry"))
        doc.packages.append(NoEscape(r"\geometry{a4paper,total={170mm,257mm},left=20mm,top=20mm}"))

       

        #doc.packages.add(Package("latex"))  # 更换解释器
        doc.packages.append(Package("ctex"))

        # 主体部分

        doc.append(NoEscape(r"\begin{center}"))  # 居中
        doc.append(NoEscape(r"\MakeUppercase{\Huge\textbf{简历}}"))  # 简历title
        doc.append(NoEscape(r"\\"))
        doc.append(NoEscape(r"\end{center}"))

        doc.append(NoEscape(r"\begin{flushleft}"))  # 开始左对齐
        doc.append(NoEscape(r"\large name\\xxxx@xxxx.com\\+xx xxxxxxxxxxx"))  # 姓名/电话/邮箱方式
        doc.append(NoEscape(r"\end{flushleft}"))

        doc.append(NoEscape(r"\\"))  # pylatex grammar needs another line

        doc.append(NoEscape(r"\rule[4pt]{18cm}{0.5pt}"))  # 下划线
        doc.append(NoEscape(r"\\"))
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{求职意向: xxxxxxx}}"))  # 求职意向
        doc.append(NoEscape(r"\\"))

        doc.append(NoEscape(r"\rule[4pt]{18cm}{0.5pt}"))  # 下划线
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{工作经验}}"))  # 工作经验
        doc.append(NoEscape(r"\end{flushleft}"))  # 结束左对齐
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行

        # 工作 1
        doc.append(NoEscape(

            r"\MakeUppercase{\small\textbf{title 1}}"
            r"\hfill"
            r"\MakeUppercase{\footnotesize\textbf{company 1}}"
            r"\hfill"
            r"\MakeUppercase{\small\textbf{working period}}"))
        # itemsize 会自动空行 开始bullet point
        doc.append(NoEscape(r"\begin{itemize}"))
        # 工作职责
        doc.append(NoEscape(
            r"\item{\normalsize{work 1}}"
            r"\item{\normalsize{work 2}}"
            r"\item{\normalsize{work 3}}"
            r"\item{\normalsize{work 4}}"
        ))
        doc.append(NoEscape(r"\end{itemize}"))  # 结束bullet point
        doc.append(NoEscape(r"\\"))  # 空行
        # 工作 2
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{title 2}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\footnotesize\textbf{company 2}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\small\textbf{working period}}"))

        doc.append(NoEscape(r"\begin{itemize}"))
        # 工作职责 2
        doc.append(NoEscape(
            r"\item{\normalsize{work 1}}"
            r"\item{\normalsize{work 2}}"
            r"\item{\normalsize{work 3}}"
            r"\item{\normalsize{work4}}"
        ))
        doc.append(NoEscape(r"\end{itemize}"))

        doc.append(NoEscape(r"\\"))  # 空行

        # 工作 3
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{title 3}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\footnotesize\textbf{company 3}}"
            r"\hfill"  # 同一行
            r"\MakeUppercase{\small\textbf{working period}}"))

        doc.append(NoEscape(r"\begin{itemize}"))
        # 工作职责 3
        doc.append(NoEscape(
            r"\\"
            r"\item{\normalsize{work 1}}"
            r"\item{\normalsize{work 2}}"
        ))
        doc.append(NoEscape(r"\end{itemize}"))

        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行

        doc.append(NoEscape(r"\begin{flushleft}"))  # 左对齐环境
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{学习经历}}"))  # 学习经历
        doc.append(NoEscape(r"\end{flushleft}"))  # 结束左对齐
        doc.append(NoEscape(r"\\"))  # 空行

        # 学校 1
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{diploma 1}}"
            r"\hfill"
            r"\MakeUppercase{\small\textbf{xxxx University}}"
            r"\hfill"
            r"\\"
            r"\MakeUppercase{\normalsize\textbf{study time}}"
            r"\hfill\MakeUppercase{\small\textbf{GPA: /4.0}}"
        ))
        # 左对齐环境
        doc.append(NoEscape(r"\begin{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\normalsize\textbf{main course}}"))  # 主要课程
        doc.append(NoEscape(r"\end{flushleft}"))  # 结束左对齐环境

        # 课程
        doc.append(NoEscape(
            r"\parskip{course 1, course 2, course 3}"))
        # 翻页
        doc.append(NoEscape(r"\newpage"))

        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行

        # 学校 2
        doc.append(NoEscape(
            r"\MakeUppercase{\small\textbf{diploma 2}}}"
            r"\hfill"
            r"\MakeUppercase{\small\textbf{xxxx University}}"
            r"\hfill"
            r"\\"
            r"\MakeUppercase{\normalsize\textbf{study time}}"
            r"\hfill\MakeUppercase{\small\textbf{GPA:  /4.0}}"

        ))

        doc.append(NoEscape(r"\begin{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\normalsize\textbf{main course}}"))
        doc.append(NoEscape(r"\end{flushleft}"))
        doc.append(NoEscape(
            r"\parskip{course 1, course 2, course 3}"))

        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行
        doc.append(NoEscape(r"\begin{flushleft}"))  # 左对齐
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{学术研究}}"))  # 研究
        doc.append(NoEscape(r"\end{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\small\textbf{theme}}"))
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))
        doc.append(NoEscape(
            r"\the theme of your research"
            r"\\"
            r"\parskip{details of your research}"
        ))
        doc.append(NoEscape(r"\\\hspace*{\fill}\\"))  # 空行
        doc.append(NoEscape(r"\begin{flushleft}"))
        doc.append(NoEscape(r"\MakeUppercase{\Large\textbf{技能}}"))  # 技能
        doc.append(NoEscape(r"\end{flushleft}"))

        # 技能相关
        doc.append(NoEscape(r"\begin{itemize}"))
        doc.append(NoEscape(
            r"\item{\normalsize{skill 1-- Skillful}\hfill{ Time of use: xx months}}"
            r"\item{\normalsize{skill 2-- Proficient}\hfill{Time of use: xx months}}"
            r"\item{\normalsize{skill 3-- Skillful}\hfill{Time of use: xxx months}}"

        ))

        doc.append(NoEscape(r"\end{itemize}"))
        doc.append(NoEscape(r"\end{documnet}"))

        doc.generate_pdf(filepath=path_report, compiler='pdfLaTex', clean_tex=False)
        # doc.generate_pdf(filepath=path_report)
        doc.generate_tex(filepath=path_report)
        # doc.generate_pdf(filepath=path_report,compiler='xelatex',clean_tex=False)

        print('...')

        print('...')
