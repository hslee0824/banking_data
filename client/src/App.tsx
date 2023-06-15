import PrimaryButton from './components/common/PrimaryButton';
import { processedModel } from './controller';
import HousePicture from './components/common/HousePicture';
import Credits from './components/common/Credits';
import { SiKaggle } from 'react-icons/si';

function App() {
  function handleReset() {
    // resetCheckStatus();
    // resetChosenValue();
    // setSliderValue(sliderDefaultValue);
  }

  return (
    <main className="p-8 w-full h-screen overflow-hidden bg-[#ECEBE8]">
      <div className="bg-[#FFFCF8] w-full h-full flex flex-col items-start justify-center gap-10 pl-[10vw]">
        <Credits />
        <HousePicture />
        {/* <img
        className="-z-10 fixed inset-0 w-screen h-screen object-cover md:object-top"
        // src="https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png"
        src="/images/preview.jpg"
      /> */}

        <div className="leading-tight">
          <h2 className="font-normal text-[64px]">House Price</h2>
          <h1 className="font-bold text-[64px]">Prediction App</h1>
          <h3 className="text-2xl mt-2">A machine learning based prediction</h3>
          <div className="mt-8">
            <PrimaryButton>Try it now</PrimaryButton>
          </div>
        </div>
        <div className="flex flex-col mb-12">
          <div className="text-2xl">Our data source</div>
          <a className="text-[64px] font-bold -mt-2 cursor-pointer">
            <SiKaggle />
          </a>
        </div>
      </div>
    </main>
  );
}

export default App;
