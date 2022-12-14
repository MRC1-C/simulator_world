import { Button, Select, Slider, Tooltip } from "antd";
import React, { useState } from "react";
import Chart from "react-apexcharts";

const legent = [
  {
    label: "Start",
    color: "pink",
  },
  {
    label: "Finish",
    color: "black",
  },
  {
    label: "CNN",
    color: "blue",
  },
  {
    label: "RNN",
    color: "red",
  },
  {
    label: "Joint",
    color: "gray",
  },
];

const Bee = () => {
  const [datachart, setDataChart] = useState({
    options: {
      chart: {
        id: "basic-bar",
      },
      xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
      },
    },
    series: [
      {
        name: "series-1",
        data: [30, 40, 45, 50, 49, 60, 70, 91],
      },
    ],
  });
  // const state = {

  // };
  return (
    <div
      className="grid grid-cols-2 gap-4 h-full p-4"
      style={{ height: "100vh", width: "calc(100vw - 200px)" }}
    >
      <div className="col-span-1 flex flex-col">
        <div className="flex-1 pb-4">
          <p className="font-bold text-3xl">Generation 0</p>
          <div className="flex justify-between text-lg font-bold">
            <p>Medium</p>
            <p>89%</p>
          </div>
          <div className="flex justify-between text-lg font-bold">
            <p>Loss</p>
            <p>1.5000</p>
          </div>
        </div>
        <div className="flex-1">
          <p>Slider</p>
          <Slider
            onChange={(e) =>
              setDataChart((prev) => ({
                ...prev,
                series: [
                  ...prev.series,
                  {
                    name: "series"+e,
                    data: [9*e, 4*e, 42, 32, 42, 62, 72, 21],
                  },
                ],
              }))
            }
          />
        </div>
        <div className="bg-white rounded-lg p-2 flex-auto h-full w-full">
          <Chart
            options={datachart.options}
            series={datachart.series}
            type="line"
            width="100%"
            height="100%"
          />
        </div>
      </div>
      <div className="col-span-1 flex flex-col">
        <div className="flex-1 flex gap-4">
          <Select
            size="large"
            defaultValue="Population 1"
            style={{
              width: 200,
              fontWeight: 700,
            }}
            options={[
              {
                value: "Population 1",
                label: "Population 1",
              },
              {
                value: "Population 2",
                label: "Population 2",
              },
            ]}
          />
          <Button
            type="primary"
            size="large"
            style={{ backgroundColor: "#1677ff" }}
            className="shadow-sm shadow-primary font-bold"
          >
            Create
          </Button>
          <Button
            type="primary"
            size="large"
            style={{ backgroundColor: "#1677ff" }}
            className="shadow-sm shadow-primary font-bold"
          >
            Start
          </Button>
          <Button
            type="primary"
            size="large"
            style={{ backgroundColor: "#1677ff" }}
            className="shadow-sm shadow-primary font-bold"
          >
            Stop
          </Button>
        </div>
        <div className="grid grid-cols-3 gap-7 p-4 flex-1">
          <Tooltip
            placement="bottom"
            title={
              <div>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
              </div>
            }
            color="rgb(22, 119, 255)"
          >
            <div
              className="bg-white col-span-1 rounded-lg p-2 w-full shadow-xl shadow-primary transition ease-in-out delay-100 hover:scale-105 cursor-pointer"
              style={{ aspectRatio: 1 / 1 }}
            >
              <img
                src="https://i.ibb.co/4ft10jr/Figure-1.png"
                style={{ height: "90%" }}
                className="object-contain rounded-lg"
              />
              <p className="font-bold">low</p>
            </div>
          </Tooltip>
          <Tooltip
            placement="bottom"
            title={
              <div>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
              </div>
            }
            color="rgb(22, 119, 255)"
          >
            <div
              className="bg-white col-span-1 rounded-lg p-2 w-full shadow-xl shadow-primary transition ease-in-out delay-100 hover:scale-105 cursor-pointer"
              style={{ aspectRatio: 1 / 1 }}
            >
              <img
                src="https://i.ibb.co/4ft10jr/Figure-1.png"
                style={{ height: "90%" }}
                className="object-contain rounded-lg"
              />
              <p className="font-bold">mid</p>
            </div>
          </Tooltip>
          <Tooltip
            placement="bottom"
            title={
              <div>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
                <p>id: 12</p>
              </div>
            }
            color="rgb(22, 119, 255)"
          >
            <div
              className="bg-white col-span-1 rounded-lg p-2 w-full shadow-xl shadow-primary transition ease-in-out delay-100 hover:scale-105 cursor-pointer"
              style={{ aspectRatio: 1 / 1 }}
            >
              <img
                src="https://i.ibb.co/4ft10jr/Figure-1.png"
                style={{ height: "90%" }}
                className="object-contain rounded-lg"
              />
              <p className="font-bold">hight</p>
            </div>
          </Tooltip>
        </div>
        <div className="flex gap-4 p-4 flex-1">
          {legent.map((l) => (
            <div className="flex flex-row gap-4 items-center">
              <div
                className="h-6 w-6 rounded-lg"
                style={{ backgroundColor: l.color }}
              ></div>
              <p className="font-bold">{l.label}</p>
            </div>
          ))}
        </div>
        <div className="bg-white rounded-lg p-2 flex-auto h-full">
          <Chart
            options={datachart.options}
            series={datachart.series}
            type="bar"
            width="100%"
            height={"100%"}
          />
        </div>
      </div>
    </div>
  );
};

export default Bee;
