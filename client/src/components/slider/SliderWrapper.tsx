import React from 'react';

interface SliderWrapperProps extends React.HTMLAttributes<HTMLDivElement> {
  value: number[];
  min: number;
  max: number;
  name: string;
}

const SliderWrapper = ({
  children,
  name,
  min,
  max,
  value,
  ...rest
}: SliderWrapperProps) => {
  return (
    <div className="flex flex-col gap-3" {...rest}>
      <div className="flex justify-between mb-4">
        <label className="text-xl">{name}</label>
        {/* <div className="text-xl">Current: {value}</div> */}
      </div>
      {children}
      <div className="flex justify-between text-black/50">
        <div>{min}</div>
        <div>{max}</div>
      </div>
    </div>
  );
};

export default SliderWrapper;
