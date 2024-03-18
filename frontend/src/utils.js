import { notification, message, Modal } from "antd";
import { ExclamationCircleOutlined } from '@ant-design/icons';


export function redirectTo(url, delay) {
    setTimeout(() => {
        window.location.replace(url);
    }, delay);
}

export function openNotification(message, description, type) {

    if (type === 'success') {
        notification.success({
            message: message,
            description: description,
            placement: 'topRight',
        });
    }
    else if (type === 'error') {
        notification.error({
            message: message,
            description: description,
            placement: 'top',
        });
    }
    else {
        notification.info({
            message: message,
            description: description,
            placement: 'topRight',
        });
    }
}

export function openMessage(content, type) {
    
    if (type === 'success') {
        message.open({
            type: 'success',
            content: content,
        });
    }
    else if (type === 'error') {
        message.open({
            type: 'error',
            content: content,
        });
    }
    else {
        message.open({
            type: 'info',
            content: content,
        });
    }
}

export function openConfirm(callbacks) {
    Modal.confirm({
        title: '登出操作',
        icon: <ExclamationCircleOutlined />,
        content: '你确定要退出账号吗？',
        async onOk() {
          for (const callback of callbacks) {
            await callback();
          }
        },
        onCancel() {
          console.log('取消登出');
        },
      });
}