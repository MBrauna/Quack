/********************************************************************************
** Form generated from reading UI file 'quackvisual.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QUACKVISUAL_H
#define UI_QUACKVISUAL_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QuackVisual
{
public:
    QWidget *centralWidget;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *QuackVisual)
    {
        if (QuackVisual->objectName().isEmpty())
            QuackVisual->setObjectName(QStringLiteral("QuackVisual"));
        QuackVisual->resize(793, 596);
        centralWidget = new QWidget(QuackVisual);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        QuackVisual->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QuackVisual);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 793, 22));
        QuackVisual->setMenuBar(menuBar);
        mainToolBar = new QToolBar(QuackVisual);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        QuackVisual->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(QuackVisual);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        QuackVisual->setStatusBar(statusBar);

        retranslateUi(QuackVisual);

        QMetaObject::connectSlotsByName(QuackVisual);
    } // setupUi

    void retranslateUi(QMainWindow *QuackVisual)
    {
        QuackVisual->setWindowTitle(QApplication::translate("QuackVisual", "QuackVisual", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QuackVisual: public Ui_QuackVisual {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QUACKVISUAL_H
