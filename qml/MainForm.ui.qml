import QtQuick 2.4
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.6
import QtQuick.Dialogs.qml 1.0
import QtQuick.Layouts 1.3
import QtMultimediaKit 5.11

Item {
    id: itembilmemkac
    width: 1000
    height: 600

    Item {
        id: state11
        visible: true
        width: 1000
        height: 600
        Login {
        }
    }

    Item {
        id: state22
        visible: false
        width: 1000
        height: 600

        RowLayout {
            id: rowid2
            width: 990
            height: 590
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

            ColumnLayout {
                id: columnLayout
                width: 1000
                height: 600
                Layout.alignment: Qt.AlignLeft | Qt.AlignTop

                TabView {
                    id: tabView00
                    y: 0
                    height: 250
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    currentIndex: 0
                    tabPosition: 1
                    tabsVisible: true
                    //frameVisible: true
                    width: 1000
                    Layout.minimumWidth: 480
                    visible: true

                    Tab {
                        height: 230
                        title: qsTr("Takip Edenler")
                        MyTakipEdenler {
                        }
                    }
                    Tab {
                        height: 230
                        title: qsTr("Takip Ettiklerim")
                        MyTakipEdilenler {
                        }
                    }
                }
                TabView {
                    id: tabView11
                    y: 280
                    width: 1000
                    height: 250
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    visible: true
                    Tab {
                        height: 230
                        title: qsTr("Takip Listesi")
                        MyFavourite {
                        }
                    }

                    Layout.minimumWidth: 480
                }
				Button {
                    id: takedata_button2
                    x: 125
                    y: 550
                    width: 350
                    height: 30
                    text: qsTr("Takip Listesine Al")
                    Layout.fillHeight: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: false
                    onClicked: {
                        asagi_indir()
                    }
                }
                Button {
                    id: takedata_button
                    x: 325
                    y: 550
                    width: 350
                    height: 30
                    text: qsTr("Verileri Al")
                    Layout.fillHeight: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: false
                    onClicked: {
						xxxx()
						if(degervarmi === 1){
							state11.visible = false
							state22.visible = false
							tabView2.visible = true
						}
                    }
                }
                
            }
        }
    }

    TabView {
        id: tabView2
        height: 600
        width: 1000
        Layout.minimumWidth: 600
        visible: false

        Tab {
            height: 580
            title: qsTr("Takip Edenler")
            source: "TakipEdenler.qml"
        }
        Tab {
            //height: 580
            title: qsTr("Takip Ettikleri")
            source: "TakipEdilenler.qml"
        }
        Tab {
            //height: 580
            title: qsTr("Eklenen Followers")
            source: "FollowersEklenen.qml"
        }
        Tab {
            height: 580
            title: qsTr("Silenen Followers")
            source: "FollowersSilinen.qml"
        }
        Tab {
            height: 580
            title: qsTr("Eklenen Followings")
            source: "FollowingsEklenen.qml"
        }
        Tab {
            height: 580
            title: qsTr("Silenen Followings")
            source: "FollowingsSilinen.qml"
        }
    }
}

/*##^## Designer {
    D{i:1;invisible:true}
}
 ##^##*/
