import React, { useState } from "react";
import { Button, Layout, Modal } from "antd";
import { useRef } from "react";
import { useEffect } from "react";
const { Header } = Layout;
// import "./plot.js";
const gen = ["C", "L", "C", "R"];
const mode = ["+", "-", "+"];

const Headers = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const plot = useRef();
  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    setIsModalOpen(false);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  useEffect(() => {
    if (plot.current) {
      const height = plot.current.offsetHeight;
      const width = plot.current.offsetWidth;
      const size = 10;
      var ctx = plot.current.getContext("2d");
      // ctx.moveTo(10,5);
      // ctx.lineTo(20,15);
      // ctx.stroke();
      // ctx.moveTo(10,25);
      // ctx.lineTo(20,15);
      // ctx.stroke();
      // let point = [0, 0];
      // ctx.fillStyle = "#FF0000";
      // for (let index = 0; index < gen.length-1; index+2) {
      //   const el1 = gen[index];
      //   const el2 = gen[index+1];
      //   const m = mode[index/2];
      //   ctx.fillRect(point[0], point[1], size, size);
      //   if (m == "+") {
      //     ctx.fillRect(point[0], point[1]+2*size, size, size);
      //     point = [point[0]+2*size,point[1]+size]
      //   }
      //   else{
      //     ctx.fillRect(point[0]+2*size, point[1], size, size);
      //     point = [point[0]+2*size,point[1]+size]
      //   }
      // }
      // ctx.fillStyle = "#FF0000";
      // ctx.fillRect(0, 20, 10, 10);
      // ctx.fillStyle = "#FF0000";
      // ctx.fillRect(20, 10, 10, 10);
    }
  });

  return (
    <Header
      className="site-layout-background"
      style={{
        padding: 0,
      }}
    >
      <Button type="primary" onClick={showModal}>
        Plot
      </Button>
      <Modal
        title="Plot"
        open={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
        width="50vw"
        bodyStyle={{ height: "50vh", overflow: "auto" }}
      >
        <canvas style={{ height: 500, width: 1000 }} ref={plot}></canvas>
      </Modal>
    </Header>
  );
};

export default Headers;
