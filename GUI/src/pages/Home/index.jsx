import React, { Suspense, useEffect, useState } from "react";
import { Box, Plane, Sky, Sphere, Torus } from "@react-three/drei";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import {
  Physics,
  RigidBody,
  Debug,
  CuboidCollider,
  BallCollider,
} from "@react-three/rapier";
import Creature from "./Creature";

const Home = () => {
  return (
    <Canvas shadows camera={{ position: [0, 50, 50] }}>
      <Sky sunPosition={[100, 20, 100]} />
      <ambientLight intensity={0.25} />
      <pointLight castShadow intensity={0.7} position={[100, 100, 100]} />
      <Physics>
        {/* <RigidBody colliders={"cuboid"} position={[0, 10, 0]}>
          <Box castShadow>
            <meshStandardMaterial color="red" transparent/>
          </Box>
        </RigidBody> */}
        <Creature />
        <RigidBody type="fixed" rotation={[-Math.PI / 2, 0, 0]}>
          <Plane args={[200, 200]} receiveShadow>
            <meshStandardMaterial color="gray" />
          </Plane>
        </RigidBody>
      </Physics>
    </Canvas>
  );
};
export default Home;
