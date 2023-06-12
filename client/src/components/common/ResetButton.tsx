import React from 'react';

type ResetButtonProps = React.HTMLAttributes<HTMLButtonElement>;

const ResetButton = ({ children, ...rest }: ResetButtonProps) => {
  return (
    <button
      className="px-6 py-2 rounded-sm uppercase font-semibold border"
      {...rest}
    >
      {children}
    </button>
  );
};

export default ResetButton;
