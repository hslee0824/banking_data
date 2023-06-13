import React from 'react';

type PrimaryButtonProps = React.HTMLAttributes<HTMLButtonElement>;

const PrimaryButton = ({ children, ...rest }: PrimaryButtonProps) => {
  return (
    <button
      className="bg-black px-8 py-4 rounded-md text-white text-2xl"
      {...rest}
    >
      {children}
    </button>
  );
};

export default PrimaryButton;
