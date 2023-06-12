import React from 'react';

type SubmitButtonProps = React.HTMLAttributes<HTMLButtonElement>;

const SubmitButton = ({ children, ...rest }: SubmitButtonProps) => {
  return (
    <button
      className="bg-black px-6 py-2 rounded-sm uppercase text-white"
      {...rest}
    >
      {children}
    </button>
  );
};

export default SubmitButton;
