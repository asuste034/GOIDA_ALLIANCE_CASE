#include <QApplication>
#include <QPushButton>

#include "api/Emergency.h"
#include "api/Block.h"
#include "api/Event.h"
#include <iostream>

int main(int argc, char *argv[]) {
    Block kal;
    const QString Q = "qwertyuip";
    QDate now = QDate::currentDate();
    kal.set_date(now);
    kal.set_text(Q);
    auto b = kal.marshall();
    for (auto i : b) {
        std::cout << i;
    }
    QApplication a(argc, argv);
    QPushButton button("Hello world!", nullptr);
    button.resize(200, 100);
    button.show();
    return QApplication::exec();
}
