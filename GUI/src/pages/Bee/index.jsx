import { Button, Image, Select, Slider, Tooltip } from "antd";
import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";
import { getRequest } from "../../hooks/api";

const fake_data = [
  {
    population: 1,
    generation: 1,
    quantity: 20,
    individuals: [
      {
        id: 123,
        genv: "c+c",
        image_gen: ".png",
        epoch_train: [
          {
            loss_train: 0.1,
            loss_test: 0.23,
            acc: 0.9,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.3,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.3,
          },
        ],
      },
      {
        id: 124,
        genv: "c+c",
        image_gen: ".png",
        epoch_train: [
          {
            loss_train: 0.1,
            loss_test: 0.23,
            acc: 0.2,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.5,
          },
        ],
      },
    ],
  },
  {
    population: 1,
    generation: 2,
    quantity: 20,
    individuals: [
      {
        id: 123,
        genv: "c+c",
        image_gen: ".png",
        epoch_train: [
          {
            loss_train: 0.1,
            loss_test: 0.23,
            acc: 0.9,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.3,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.3,
          },
        ],
      },
      {
        id: 124,
        genv: "c+c",
        image_gen: ".png",
        epoch_train: [
          {
            loss_train: 0.1,
            loss_test: 0.23,
            acc: 0.2,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.5,
          },
        ],
      },
      {
        id: 125,
        genv: "c+c",
        image_gen: ".png",
        epoch_train: [
          {
            loss_train: 0.1,
            loss_test: 0.23,
            acc: 0.9,
          },
          {
            loss_train: 0.2,
            loss_test: 0.22,
            acc: 0.5,
          },
        ],
      },
    ],
  },
];

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
  const [generation, setGeneration] = useState(1);
  const [datachart, setDataChart] = useState(
    fake_data[generation].individuals.map((individual) => ({
      name: individual.id,
      data: individual.epoch_train.map((e) => e.acc),
    }))
  );
  console.log(datachart);
  const fakeData = (index) =>
    new Promise((resolve, reject) => {
      setTimeout(() => {
        setDataChart((prev) => [
          ...prev,
          {
            name: "series" + index,
            data: [9 * index, 4 * index, 42, 32, 42, 62, 72, 21],
          },
        ]);
        resolve();
      }, 2000);
    });

  const [loading, setLoading] = useState(false);
  const [image, setImage] = useState()

  useEffect(() => {
    try {
      (async () => {
        const data = await getRequest("get_images");
        setImage(data.image)
        console.log(data.image)
      })();
    } catch (error) {
      console.log(error);
    }
  }, []);

  return (
    <div
      className="grid grid-cols-2 gap-4 h-full p-4"
      style={{ height: "100vh", width: "calc(100vw - 200px)" }}
    >
      <div className="col-span-1 flex flex-col">
        <div className="flex-1 pb-4">
          <p className="font-bold text-3xl">
            Generation {fake_data[0].generation}
          </p>
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
            value={fake_data[generation].generation}
            max={10}
            onChange={(e) => {
              setGeneration(e - 1);
              setDataChart(
                fake_data[e - 1].individuals.map((individual) => ({
                  name: individual.id,
                  data: individual.epoch_train.map((e) => e.acc),
                }))
              );
            }}
          />
        </div>
        <div className="bg-white rounded-lg p-2 flex-auto h-full w-full">
          <Chart
            options={{
              chart: {
                id: "basic-bar",
              },
              // xaxis: {
              //   categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
              // },
            }}
            series={datachart}
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
            loading={loading}
            onClick={async () => {
              for (let index = 1; index < 10; index++) {
                setLoading(true);
                await fakeData(index);
                setLoading(false);
              }
            }}
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
            <div
              className="bg-white col-span-1 rounded-lg p-2 w-full shadow-xl shadow-primary transition ease-in-out delay-100 hover:scale-105 cursor-pointer"
              style={{ aspectRatio: 1 / 1 }}
            >
              <Image
                src={`data:image/jpeg;base64,${image}`}
                style={{ height: "90%" }}
                className="object-contain rounded-lg"
              />
              <p className="font-bold">low</p>
            </div>
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
            <div className="flex flex-row gap-4 items-center" key={l.color}>
              <div
                className="h-6 w-6 rounded-lg shadow-xl shadow-primary"
                style={{ backgroundColor: l.color }}
              ></div>
              <p className="font-bold">{l.label}</p>
            </div>
          ))}
        </div>
        <div className="bg-white rounded-lg p-2 flex-auto h-full">
          <Chart
            options={{
              chart: {
                id: "basic-bar",
              },
              xaxis: {
                categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
              },
            }}
            series={datachart}
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
