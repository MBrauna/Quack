#include "quackvisual.h"
#include "ui_quackvisual.h"

QuackVisual::QuackVisual(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QuackVisual)
{
    ui->setupUi(this);
}

QuackVisual::~QuackVisual()
{
    delete ui;
}
