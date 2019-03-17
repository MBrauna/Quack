#ifndef QUACKVISUAL_H
#define QUACKVISUAL_H

#include <QMainWindow>

namespace Ui {
class QuackVisual;
}

class QuackVisual : public QMainWindow
{
    Q_OBJECT

public:
    explicit QuackVisual(QWidget *parent = 0);
    ~QuackVisual();

private:
    Ui::QuackVisual *ui;
};

#endif // QUACKVISUAL_H
