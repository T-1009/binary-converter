# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"进制转换器", pos=wx.DefaultPosition, size=wx.Size(390, 350),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        gSizer1 = wx.GridSizer(5, 2, 0, 0)

        self.m_staticText_1_2 = wx.StaticText(self, wx.ID_ANY, u"2 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_1_2.Wrap(-1)

        self.m_staticText_1_2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        gSizer1.Add(self.m_staticText_1_2, 0, wx.ALL, 5)

        self.m_textCtrl_1 = wx.TextCtrl(self, wx.ID_ANY, u"请输入2进制", wx.DefaultPosition, wx.Size(120, -1), 0)
        self.m_textCtrl_1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        gSizer1.Add(self.m_textCtrl_1, 0, wx.ALL, 5)

        self.m_staticText_2_8 = wx.StaticText(self, wx.ID_ANY, u"8 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_2_8.Wrap(-1)

        self.m_staticText_2_8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        gSizer1.Add(self.m_staticText_2_8, 0, wx.ALL, 5)

        self.m_textCtrl_2 = wx.TextCtrl(self, wx.ID_ANY, u"请输入8进制", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer1.Add(self.m_textCtrl_2, 0, wx.ALL, 5)

        self.m_staticText_3_8 = wx.StaticText(self, wx.ID_ANY, u"10 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_3_8.Wrap(-1)

        self.m_staticText_3_8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        gSizer1.Add(self.m_staticText_3_8, 0, wx.ALL, 5)

        self.m_textCtrl_3 = wx.TextCtrl(self, wx.ID_ANY, u"请输入10进制", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer1.Add(self.m_textCtrl_3, 0, wx.ALL, 5)

        self.m_staticText_4_16 = wx.StaticText(self, wx.ID_ANY, u"16 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_4_16.Wrap(-1)

        self.m_staticText_4_16.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        gSizer1.Add(self.m_staticText_4_16, 0, wx.ALL, 5)

        self.m_textCtrl_4 = wx.TextCtrl(self, wx.ID_ANY, u"请输入16进制", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer1.Add(self.m_textCtrl_4, 0, wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.transform = wx.Button(self, wx.ID_ANY, u"转换", wx.DefaultPosition, wx.DefaultSize, 0)
        self.transform.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer4.Add(self.transform, 0, wx.ALL, 5)

        self.reduction = wx.Button(self, wx.ID_ANY, u"还原", wx.DefaultPosition, wx.DefaultSize, 0)
        self.reduction.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        bSizer4.Add(self.reduction, 0, wx.ALL, 5)

        gSizer1.Add(bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.transform.Bind(wx.EVT_BUTTON, self.answer)
        self.reduction.Bind(wx.EVT_BUTTON, self.red_answer)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def answer(self, event):
        event.Skip()

    def red_answer(self, event):
        event.Skip()
