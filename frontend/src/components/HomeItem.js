import React, { useState, useEffect } from 'react';
import { Flex, Button, Upload, Typography } from 'antd';
import { HomeOutlined, InboxOutlined } from '@ant-design/icons';
import * as Utils from '../utils';
import { Link } from 'react-router-dom';
import { baseStyle } from '../style';
import { checkLoginStatus, handleLogout, dragUpload } from '../router';



export function HomeHeader() {

    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [userId, setUserId] = useState('');

    useEffect(() => {
        checkLoginStatus(setIsLoggedIn, setUserId);
    }, []);

    return (
        <>
            <Flex
                justify='space-between'
                align='center'
            >
                <Link to='/'>
                    <HomeOutlined
                        style={{
                            fontSize: '35px',
                            verticalAlign: 'middle',
                            color: '#05668d',
                        }}

                    />
                </Link>
                {isLoggedIn ? `你好，用户${userId}！` : '你暂未登录······'}
                {!isLoggedIn && (
                    <Button 
                        onClick={() => Utils.redirectTo('/onlogin')}
                        size='large'
                    >
                        登录
                    </Button>
                )}
                {isLoggedIn && (
                    <Button 
                        onClick={() => Utils.openConfirm([() => handleLogout(setIsLoggedIn, setUserId)])}
                        size='large'
                    >
                        登出
                    </Button>
                )}
            </Flex>
        </>
    );
}

export function HomeContent() {
    return (
        <Flex gap="middle">
            <Flex
                justify='space-between'
                vertical
                style={{
                    ...baseStyle,
                    backgroundColor: '#ccdbfd',
                }}

            >
                <Content1/>
            </Flex>

            <Flex
                justify='space-between'
                vertical
                style={{
                    ...baseStyle,
                    backgroundColor: '#d7e3fc'
                }}
            >
                <Content1/>
            </Flex>

            <Flex
                justify='space-between'
                vertical
                style={{
                    ...baseStyle,
                    backgroundColor: '#ccdbfd',
                }}
            >
                <Content1/>
            </Flex>
        </Flex>
    );
}

function Content1(){
    const { Dragger } = Upload;
    const { Title } = Typography; // 文字排版

    return (
        <>
            <Flex
                vertical
            >
                <Title
                    level={2}
                >
                    Voice Convert Here
                </Title>
                <Dragger {...dragUpload}>
                    <p className="ant-upload-drag-icon">
                        <InboxOutlined />
                    </p>
                    <p className="ant-upload-text">
                        点击上传音频文件或拖拽文件到该区域
                    </p>
                    <p className="ant-upload-hint">
                        每次仅支持上传一个文件。严禁上传违规音频，对于违法行为将保存记录并追究法律责任。
                    </p>
                </Dragger>
            </Flex>

        </>
    );
}

function Content2() {
    return (
        <>
        12132442141231
        </>
    );
}

function Content3() {
    return (
        <>
        12132442141231
        </>
    );
}