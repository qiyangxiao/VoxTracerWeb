import React, { useState } from "react";
import { Button, Form, Input, Row, Col } from 'antd';
import { RegisterFormItemLayout, RegisterTailFormItemLayout } from "../style";
import { handleSendCaptcha } from "../router";

export default function RegisterForm({ handleRegister }) {

    const [email, setEmail] = useState('');
    const [form] = Form.useForm();

    return (   
        <Form
            {...RegisterFormItemLayout}
            form={form}
            name="register"
            onFinish={handleRegister}
        >
            <Form.Item
                name="email"
                label="电子邮箱"
                rules={[
                    {
                        type: 'email',
                        message: '输入的电子邮箱无效！',
                    },
                    {
                        required: true,
                        message: '请输入你的电子邮箱！',
                    }
                ]}
                hasFeedback
            >
                <Input
                    value={email}
                    onChange={(e) => setEmail(e.target.value)} 
                />
            </Form.Item>

            <Form.Item
                name="pwd"
                label="密码"
                rules={[
                    {
                        required: true,
                        message: '请设置你的密码！',
                    }
                ]}
                hasFeedback
            >
                <Input.Password />
            </Form.Item>

            <Form.Item
                name="cpwd"
                label="确认密码"
                rules={[
                    {
                        required: true,
                        message: '请确认你的密码！',
                    },
                    ({ getFieldValue }) => ({
                        validator(_, value) {
                            if (!value || getFieldValue('pwd') === value) {
                                return Promise.resolve();
                            }
                            return Promise.reject(new Error('两次输入的密码不一致！'));
                        },
                    }),
                ]}
            >
                <Input.Password />
            </Form.Item>
            
            <Form.Item
                label="验证码"
            >
                <Row gutter={8}>
                    <Col span={12}>
                        <Form.Item
                            name="captcha"
                            rules={[
                                {
                                    required: true,
                                    message: '请输入收到的验证码！',
                                }
                            ]}
                        >
                            <Input />
                        </Form.Item>
                    </Col>
                    <Col span={12}>
                        <Button
                            onClick={() => handleSendCaptcha(email)}
                        >
                            获取验证码
                        </Button>
                    </Col>
                </Row>
            </Form.Item>

            
            <Form.Item {...RegisterTailFormItemLayout}>
                <Button
                    type="primary"
                    size="large"
                    htmlType="submit"
                    className="register-form-button"
                >
                    注册
                </Button>
            </Form.Item>
        </Form>
    );
}