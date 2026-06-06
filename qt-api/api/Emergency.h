//
// Created by localuser on 6/6/26.
//

#ifndef FRONTEND_EMERGENCY_H
#define FRONTEND_EMERGENCY_H
#include <QJsonDocument>
#include <QJsonObject>

#include "ApiObject.h"

class Emergency : public ApiObject {
    QString text = "";
    QDateTime timeout;

public:
    void set_text(const QString &text_);

    QString get_text();

    void set_timeout(const QDateTime &timeout_);

    QDateTime get_timeout();

    QByteArray marshall();

    void unmarshall(const QByteArray &data);
};

#endif //FRONTEND_EMERGENCY_H
