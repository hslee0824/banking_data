import React from 'react';
import { AiFillGithub } from 'react-icons/ai';

const Credits = () => {
  return (
    <div className="font-bold text-2xl flex">
      <p>
        Made by&nbsp;
        <a className="hover:text-yellow-700 transition-colors duration-300 cursor-pointer">
          hslee0824
        </a>{' '}
        &{' '}
        <a className="hover:text-yellow-700 transition-colors duration-300 cursor-pointer">
          ipod1g
        </a>
      </p>
      <a className="text-4xl ml-3 -mt-1 hover:text-yellow-700 transition-colors duration-300 cursor-pointer">
        <AiFillGithub />
      </a>
    </div>
  );
};

export default Credits;
