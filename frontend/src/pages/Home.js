import React from 'react';
import { Layout } from 'antd';
import { HomeContent, HomeHeader} from '../components/HomeItem';
import { headerStyle, contentStyle } from '../style';


const { Header, Content } = Layout; // 布局

export default function Home() {
    return (
        <>
            <Layout>
                <Header style={headerStyle}>
                    <HomeHeader/>
                </Header>
                <Content style={contentStyle}>
                    <HomeContent/>
                </Content>
            </Layout>
        </>
    );
}

