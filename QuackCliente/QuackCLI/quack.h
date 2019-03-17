#ifndef QUACK_H
#define QUACK_H

#include <QWidget>

namespace Ui {
class Quack;
}

class Quack : public QWidget
{
    Q_OBJECT

public:
    explicit Quack(QWidget *parent = 0);
    ~Quack();

private slots:
    void on_quack_btn_fechar_pressed();

    void on_quack_btn_minimizar_pressed();

private:
    Ui::Quack *ui;
};

#endif // QUACK_H
