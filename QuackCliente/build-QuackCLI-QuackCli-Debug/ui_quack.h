/********************************************************************************
** Form generated from reading UI file 'quack.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QUACK_H
#define UI_QUACK_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Quack
{
public:
    QFrame *frame_2;
    QWidget *widget;
    QHBoxLayout *horizontalLayout_2;
    QHBoxLayout *horizontalLayout;
    QLineEdit *quack_usuario;
    QLineEdit *quack_senha;
    QPushButton *quack_iniciar;
    QPushButton *quack_btn_minimizar;
    QPushButton *quack_btn_fechar;
    QToolBox *quack_frame;
    QWidget *page;
    QWidget *page_2;
    QComboBox *quack_cb_aplicacao;

    void setupUi(QWidget *Quack)
    {
        if (Quack->objectName().isEmpty())
            Quack->setObjectName(QStringLiteral("Quack"));
        Quack->setWindowModality(Qt::NonModal);
        Quack->setEnabled(true);
        Quack->resize(523, 632);
        Quack->setWindowTitle(QStringLiteral("Quack"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/Quack/Logo/QuackLogo/QUACKCli.png"), QSize(), QIcon::Normal, QIcon::Off);
        Quack->setWindowIcon(icon);
        Quack->setStyleSheet(QStringLiteral(""));
        Quack->setLocale(QLocale(QLocale::Portuguese, QLocale::Brazil));
        frame_2 = new QFrame(Quack);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setGeometry(QRect(10, 10, 501, 71));
        frame_2->setStyleSheet(QStringLiteral("background-color: qlineargradient(spread:pad, x1:0.607, y1:0.0626364, x2:0.637, y2:0.609, stop:0.840796 rgba(0, 0, 0, 169), stop:1 rgba(25, 25, 25, 169));"));
        frame_2->setFrameShape(QFrame::WinPanel);
        frame_2->setFrameShadow(QFrame::Plain);
        widget = new QWidget(frame_2);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(10, 30, 481, 32));
        horizontalLayout_2 = new QHBoxLayout(widget);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        quack_usuario = new QLineEdit(widget);
        quack_usuario->setObjectName(QStringLiteral("quack_usuario"));
        quack_usuario->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        quack_usuario->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(quack_usuario);

        quack_senha = new QLineEdit(widget);
        quack_senha->setObjectName(QStringLiteral("quack_senha"));
        quack_senha->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));

        horizontalLayout->addWidget(quack_senha);


        horizontalLayout_2->addLayout(horizontalLayout);

        quack_iniciar = new QPushButton(widget);
        quack_iniciar->setObjectName(QStringLiteral("quack_iniciar"));
        quack_iniciar->setStyleSheet(QLatin1String("border: none;\n"
"background-color: none;"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/Quack/Logo/QuackLogo/Icones/Button Next.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon1.addFile(QStringLiteral(":/Quack/Logo/QuackLogo/Icones/Button Refresh.png"), QSize(), QIcon::Active, QIcon::Off);
        quack_iniciar->setIcon(icon1);
        quack_iniciar->setIconSize(QSize(30, 30));

        horizontalLayout_2->addWidget(quack_iniciar);

        quack_btn_minimizar = new QPushButton(Quack);
        quack_btn_minimizar->setObjectName(QStringLiteral("quack_btn_minimizar"));
        quack_btn_minimizar->setGeometry(QRect(470, 0, 21, 21));
        quack_btn_minimizar->setStyleSheet(QStringLiteral("border: none;"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/Quack/Logo/QuackLogo/Icones/Button Delete.png"), QSize(), QIcon::Normal, QIcon::Off);
        quack_btn_minimizar->setIcon(icon2);
        quack_btn_fechar = new QPushButton(Quack);
        quack_btn_fechar->setObjectName(QStringLiteral("quack_btn_fechar"));
        quack_btn_fechar->setGeometry(QRect(490, 0, 21, 21));
        quack_btn_fechar->setStyleSheet(QStringLiteral("border: none;"));
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/Quack/Logo/QuackLogo/Icones/Button Close.png"), QSize(), QIcon::Normal, QIcon::Off);
        quack_btn_fechar->setIcon(icon3);
        quack_frame = new QToolBox(Quack);
        quack_frame->setObjectName(QStringLiteral("quack_frame"));
        quack_frame->setGeometry(QRect(10, 120, 501, 431));
        quack_frame->setStyleSheet(QLatin1String("background-color: qlineargradient(spread:pad, x1:0.607, y1:0.0626364, x2:0.637, y2:0.609, stop:0.840796 rgba(0, 0, 0, 169), stop:1 rgba(25, 25, 25, 169));\n"
"color: rgb(255, 255, 255);"));
        quack_frame->setLineWidth(1);
        page = new QWidget();
        page->setObjectName(QStringLiteral("page"));
        page->setGeometry(QRect(0, 0, 501, 369));
        quack_frame->addItem(page, QStringLiteral("Page 1"));
        page_2 = new QWidget();
        page_2->setObjectName(QStringLiteral("page_2"));
        page_2->setGeometry(QRect(0, 0, 501, 369));
        quack_frame->addItem(page_2, QStringLiteral("Page 2"));
        quack_cb_aplicacao = new QComboBox(Quack);
        QIcon icon4;
        icon4.addFile(QStringLiteral(":/Quack/Icones/QuackLogo/Icones/QuackServer.png"), QSize(), QIcon::Normal, QIcon::Off);
        quack_cb_aplicacao->addItem(icon4, QString());
        QIcon icon5;
        icon5.addFile(QStringLiteral(":/Quack/Icones/QuackLogo/Icones/QuackCli.png"), QSize(), QIcon::Normal, QIcon::Off);
        quack_cb_aplicacao->addItem(icon5, QString());
        quack_cb_aplicacao->setObjectName(QStringLiteral("quack_cb_aplicacao"));
        quack_cb_aplicacao->setGeometry(QRect(10, 90, 501, 25));
        quack_cb_aplicacao->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"));
        QWidget::setTabOrder(quack_btn_minimizar, quack_btn_fechar);
        QWidget::setTabOrder(quack_btn_fechar, quack_usuario);
        QWidget::setTabOrder(quack_usuario, quack_cb_aplicacao);
        QWidget::setTabOrder(quack_cb_aplicacao, quack_iniciar);
        QWidget::setTabOrder(quack_iniciar, quack_senha);

        retranslateUi(Quack);

        quack_frame->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(Quack);
    } // setupUi

    void retranslateUi(QWidget *Quack)
    {
        quack_usuario->setPlaceholderText(QApplication::translate("Quack", "Usu\303\241rio Quack", nullptr));
        quack_senha->setPlaceholderText(QApplication::translate("Quack", "Senha Quack", nullptr));
        quack_iniciar->setText(QString());
        quack_btn_minimizar->setText(QString());
        quack_btn_fechar->setText(QString());
        quack_frame->setItemText(quack_frame->indexOf(page), QApplication::translate("Quack", "Page 1", nullptr));
        quack_frame->setItemText(quack_frame->indexOf(page_2), QApplication::translate("Quack", "Page 2", nullptr));
        quack_cb_aplicacao->setItemText(0, QApplication::translate("Quack", "Quack Servidor", nullptr));
        quack_cb_aplicacao->setItemText(1, QApplication::translate("Quack", "Quack Cliente", nullptr));

        Q_UNUSED(Quack);
    } // retranslateUi

};

namespace Ui {
    class Quack: public Ui_Quack {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QUACK_H
