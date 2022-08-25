import wx
from base_transf import MainFrame


class transFrame(MainFrame):
    # 进制转换
    def answer(self, event):
        base_2 = ''
        base_8 = ''
        base_10 = ''
        base_16 = ''
        # 2 进制转 8,10,16
        if self.m_textCtrl_1.Value != '请输入2进制':
            # print(type(self.m_textCtrl_1.Value))
            # <class 'str'>
            # 2 转 8
            base_8 = oct(int(self.m_textCtrl_1.Value, 2))[2:]
            self.m_textCtrl_2.Clear()
            self.m_textCtrl_2.AppendText(base_8)

            # 2 转 10
            base_10 = str(int(self.m_textCtrl_1.Value, 2))
            self.m_textCtrl_3.Clear()
            self.m_textCtrl_3.AppendText(base_10)
            # 2 转 16
            base_16 = hex(int(self.m_textCtrl_1.Value, 2))[2:]
            self.m_textCtrl_4.Clear()
            self.m_textCtrl_4.AppendText(base_16)

        # 8 转 2, 10, 16
        elif self.m_textCtrl_2.Value != '请输入8进制':
            # 8 转 2
            base_2 = bin(int(self.m_textCtrl_2.Value, 8))[2:]
            self.m_textCtrl_1.Clear()
            self.m_textCtrl_1.AppendText(base_2)
            # 8 转 10
            base_10 = str(int(self.m_textCtrl_2.Value, 8))
            self.m_textCtrl_3.Clear()
            self.m_textCtrl_3.AppendText(base_10)
            # 8 转 16
            base_16 = hex(int(self.m_textCtrl_2.Value, 8))[2:]
            self.m_textCtrl_4.Clear()
            self.m_textCtrl_4.AppendText(base_16)

        # 10 转 2, 8, 16
        elif self.m_textCtrl_3.Value != '请输入10进制':
            # 10 转 2
            base_2 = bin(int(self.m_textCtrl_3.Value))[2:]
            self.m_textCtrl_1.Clear()
            self.m_textCtrl_1.AppendText(base_2)
            # 10 转 8
            base_8 = oct(int(self.m_textCtrl_3.Value))[2:]
            self.m_textCtrl_2.Clear()
            self.m_textCtrl_2.AppendText(base_8)
            # 10 转 16
            base_16 = hex(int(self.m_textCtrl_3.Value))[2:]
            self.m_textCtrl_4.Clear()
            self.m_textCtrl_4.AppendText(base_16)

        # 16 转 2, 8, 10
        elif self.m_textCtrl_4.Value != '请输入16进制':
            # 16 转 2
            base_2 = bin(int(self.m_textCtrl_4.Value, 16))[2:]
            self.m_textCtrl_1.Clear()
            self.m_textCtrl_1.AppendText(base_2)
            # 16 转 8
            base_8 = oct(int(self.m_textCtrl_4.Value, 16))[2:]
            self.m_textCtrl_2.Clear()
            self.m_textCtrl_2.AppendText(base_8)
            # 16 转 10
            base_10 = str(int(self.m_textCtrl_4.Value, 16))
            self.m_textCtrl_3.Clear()
            self.m_textCtrl_3.AppendText(base_10)

    # 还原
    def red_answer(self, event):
        self.m_textCtrl_1.Clear()
        self.m_textCtrl_1.AppendText('请输入2进制')

        self.m_textCtrl_2.Clear()
        self.m_textCtrl_2.AppendText('请输入8进制')

        self.m_textCtrl_3.Clear()
        self.m_textCtrl_3.AppendText('请输入10进制')

        self.m_textCtrl_4.Clear()
        self.m_textCtrl_4.AppendText('请输入16进制')


app = wx.App()
transFrame(None).Show()
app.MainLoop()
