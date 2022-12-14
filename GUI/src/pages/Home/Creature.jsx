import { Box,Sphere } from "@react-three/drei";
import { useFrame } from "@react-three/fiber";
import { RigidBody } from "@react-three/rapier";
import React, { useRef } from "react";

const Creature = () => {
  const myMesh = useRef();
//   useFrame(({ clock }) => {
//     myMesh.current.position.x +=0.05
//   });

  return (
    <RigidBody  colliders={"cuboid"} position={[0,10,0]} restitution={2}>
      <Sphere castShadow ref={myMesh}>
        <meshStandardMaterial color="red" transparent />
      </Sphere>
    </RigidBody>
  );
};

export default Creature;
