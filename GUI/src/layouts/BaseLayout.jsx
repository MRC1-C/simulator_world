import React from "react";
import { Layout } from "antd";
const { Content } = Layout;
// import { Canvas } from "@react-three/fiber";
// import Box from "../../components/Box";
import { Outlet } from "react-router-dom";
import Sibar from "./Sibar";
import Headers from "./Header";
const BaseLayout = () => {
  return (
    <Layout
      style={{
        height: "100vh",
      }}
    >
      <Sibar />
      <Layout style={{ overflow: "auto" }}>
        {/* <Headers /> */}
        <Content
          style={{
            overflow: "auto",
          }}
        >
          <div
            className="site-layout-background"
            style={{
              // padding: 24,
            //   minHeight: 360,
              height: "100%",
              // backgroundColor: 'red'
            }}
          >
            {/* <Canvas>
              <ambientLight />
              <pointLight position={[10, 10, 10]} />
              <Box position={[-1.2, 0, 0]} />
              <Box position={[1.2, 0, 0]} />
            </Canvas> */}
            <Outlet />
          </div>

          {/* <Footer
          style={{
            textAlign: "center",
          }}
        ><Canvas>
    <ambientLight />
    <pointLight position={[10, 10, 10]} />
    <Box position={[-1.2, 0, 0]} />
    <Box position={[1.2, 0, 0]} />
  </Canvas>,

          Ant Design ©2018 Created by Ant UED
        </Footer> */}
        </Content>
      </Layout>
    </Layout>
  );
};

export default BaseLayout;
