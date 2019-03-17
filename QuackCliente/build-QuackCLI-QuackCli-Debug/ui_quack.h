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
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Quack
{
public:
    QPushButton *quack_btn_site;
    QGroupBox *quack_gb_acesso;
    QLineEdit *quack_senha;
    QLineEdit *quack_usuario;
    QPushButton *quack_btn_acesso;

    void setupUi(QWidget *Quack)
    {
        if (Quack->objectName().isEmpty())
            Quack->setObjectName(QStringLiteral("Quack"));
        Quack->setWindowModality(Qt::NonModal);
        Quack->setEnabled(true);
        Quack->resize(478, 139);
        Quack->setWindowTitle(QStringLiteral("Quack"));
        Quack->setStyleSheet(QStringLiteral("background-color: none;"));
        Quack->setLocale(QLocale(QLocale::Portuguese, QLocale::Brazil));
        quack_btn_site = new QPushButton(Quack);
        quack_btn_site->setObjectName(QStringLiteral("quack_btn_site"));
        quack_btn_site->setGeometry(QRect(10, 30, 111, 101));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(quack_btn_site->sizePolicy().hasHeightForWidth());
        quack_btn_site->setSizePolicy(sizePolicy);
        QIcon icon;
        icon.addFile(QStringLiteral(":/Quack/Logo/QuackLogo/QUACKCli.png"), QSize(), QIcon::Normal, QIcon::Off);
        quack_btn_site->setIcon(icon);
        quack_btn_site->setIconSize(QSize(110, 110));
        quack_gb_acesso = new QGroupBox(Quack);
        quack_gb_acesso->setObjectName(QStringLiteral("quack_gb_acesso"));
        quack_gb_acesso->setGeometry(QRect(130, 9, 341, 121));
        quack_gb_acesso->setStyleSheet(QStringLiteral("border-color: rgb(52, 101, 164);"));
        quack_senha = new QLineEdit(quack_gb_acesso);
        quack_senha->setObjectName(QStringLiteral("quack_senha"));
        quack_senha->setGeometry(QRect(170, 50, 156, 25));
        quack_senha->setAlignment(Qt::AlignCenter);
        quack_usuario = new QLineEdit(quack_gb_acesso);
        quack_usuario->setObjectName(QStringLiteral("quack_usuario"));
        quack_usuario->setGeometry(QRect(10, 50, 157, 25));
        quack_usuario->setAlignment(Qt::AlignCenter);
        quack_btn_acesso = new QPushButton(quack_gb_acesso);
        quack_btn_acesso->setObjectName(QStringLiteral("quack_btn_acesso"));
        quack_btn_acesso->setGeometry(QRect(10, 80, 319, 25));

        retranslateUi(Quack);

        QMetaObject::connectSlotsByName(Quack);
    } // setupUi

    void retranslateUi(QWidget *Quack)
    {
        quack_btn_site->setText(QString());
        quack_gb_acesso->setTitle(QApplication::translate("Quack", "Acesso", nullptr));
        quack_senha->setPlaceholderText(QApplication::translate("Quack", "Senha de acesso", nullptr));
        quack_usuario->setInputMask(QString());
        quack_usuario->setPlaceholderText(QApplication::translate("Quack", "Usu\303\241rio Quack", nullptr));
        quack_btn_acesso->setText(QApplication::translate("Quack", "Acessar", nullptr));
        Q_UNUSED(Quack);
    } // retranslateUi

};

namespace Ui {
    class Quack: public Ui_Quack {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QUACK_H
