//
// Created by localuser on 6/6/26.
//

#ifndef FRONTEND_EVENT_H
#define FRONTEND_EVENT_H
#include <QJsonArray>
#include "ApiObject.h"
#include "Emergency.h"

class Event : public ApiObject {
public:
    enum EventType {
        putBlock, putEmergency, disableEmergency
    };

private:
    EventType type;
    QJsonArray blocks;
    Emergency emergency;

public:
    void set_type(const EventType &type_) {
        type = type_;
    }

    EventType get_type() {
        return type;
    }

    void set_blocks(const QJsonArray &blocks_) {
        blocks = blocks_;
    };

    QJsonArray get_blocks() {
        return blocks;
    };

    void set_emergency(const Emergency &emergency_) {
        emergency = emergency_;
    }

    Emergency get_emergency() {
        return emergency;
    }

    QByteArray marshall() {
        QJsonObject obj;
        switch (type) {
            case putBlock:
                obj["type"] = "putBlock";
                break;
            case putEmergency:
                obj["type"] = "putEmergency";
                break;
            case disableEmergency:
                obj["type"] = "disableEmergency";
                break;
        }

        obj["blocks"] = blocks;
        obj["emergency"] = QString::fromStdString(emergency.marshall().toStdString());

        return QJsonDocument(obj).toJson();
    };

    void unmarshall(const QByteArray &data) {
        QJsonDocument doc;
        doc.fromBinaryData(data);

        if (doc["type"].toString() == "putBlock")
            type = putBlock;
        if (doc["type"].toString() == "putEmergency")
            type = putEmergency;
        if (doc["type"].toString() == "disableEmergency")
            type = disableEmergency;

        blocks = doc["blocks"].toArray();
        emergency.unmarshall(QByteArray::fromStdString(doc["emergency"].toString().toStdString()));
    };
};


#endif //FRONTEND_EVENT_H
