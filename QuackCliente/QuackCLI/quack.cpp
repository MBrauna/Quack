#include "quack.h"
#include "ui_quack.h"

Quack::Quack(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Quack)
{
    ui->setupUi(this);

    // Permite que o fundo fique transparente.
    setAttribute(Qt::WA_TranslucentBackground);
    setWindowFlags(Qt::Window | Qt::FramelessWindowHint);

    // ALtera a logo do projeto
    setWindowIcon(QIcon("Quack/Logo/QUACKCli.png"));
}

Quack::~Quack()
{
    delete ui;
}
