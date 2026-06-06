//
// Created by localuser on 6/6/26.
//

#include "Emergency.h"

inline void Emergency::set_text(const QString& text_) {
    text = text_;
}

QString Emergency::get_text() {
    return text;
}

inline void Emergency::set_timeout(const QDateTime &timeout_) {
    timeout = timeout_;
}

QDateTime Emergency::get_timeout() {
    return timeout;
}

QByteArray Emergency::marshall() {
    QJsonObject obj;
    obj["text"] = text;
    obj["timeout"] = timeout.toString();
    return QJsonDocument(obj).toJson();
}

void Emergency::unmarshall(const QByteArray &data) {
    QJsonDocument doc;
    doc.fromBinaryData(data);
    text = doc["text"].toString();
    timeout = QDateTime::fromString(doc["timeout"].toString());
}
