from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

address_to = "0x9e6a2A5Ac4D55eE0952aC3c09e6144353DD3d8DE"

s=Service('./driver/chromedriver')

adresses = {"0x14d3Ba683D7Ae58e8BF75232e9629AaD470c3E3c": "0xebf81d7524561064cb906c8de641e45e774f7707437aae0c8397a188ee81e155", "0xa41DD82f7c27f12BC4347fff1cd9e7CFdb1aD08A": "0xce14c8f029888b5aec2d9aeaf4649eadf642325aee430111fc2ae5b5bffce74f", "0x37f0E564D07A74A3E06eD5F28607a654cb6c2a3D": "0x2c2474edd5b6a7a390d49094cf6c1c2f35583a63326ffb5ed0da38bf9d4d4e94", "0x00750Cc834EA34704b3cb6652a685455Fe039A38": "0xd1c3b07efeff0895104ea6f86da7a83d006c79e46246d85ef8e3c614c5f820b0", "0x494459f14ff81532d9680a3771B3197bd56D6073": "0x986fb8ebac6d928b3593f57e2069173b540f7a72f36fe1363ccd01a3dcebfc26", "0x5e45Dd592863f8B34E7F7F6a4f79d97797576d05": "0xcb518693e28e0c0ce766c85f8b6abb0aee278c61c4080c8d9a2e695f1f2fde38", "0x119c9cfC3Cdbc2ab497f6917022bdE3683a75fD3": "0xb4edc6611930b02345f233393d5fbe616bfccd7e46a4d444bcf86bdafc041604", "0xe172c2986C0E933831e6CE35A351e29003A70d0b": "0x04d0c2b355e6eedf391fa21820c802a8813273b417f6f3b852dadb441391be4e", "0x61B1331876061283956EB13eFb6aDC2D923D28E2": "0xc50635b23ee2d64fdd090bd61ffed6d5249a5b871d22b75976e42ca582b91548", "0xbf42c115f7Ed6F3d238f3803F1b6A859b1e627Dc": "0x44f1ed317cc33f155c6aae7ab00afd6c4f47f05799fd2060a2ee51cdd7fcfe33", "0x763C5f856CeD2FB3180DD760Eb9b2326c5F58455": "0xd72e81456a3fe52d0609e48e42b8cbc4dd46da21192d75e10d3f3feb4424759d", "0x934227ed451C1C15FB8c0e229Ea10bE60530c5D7": "0x44f977471f26a046f475f6382ee214b1b723d7227b4442c1ec6727d0e4c7b0d2", "0xdB35fC5A491A1c8dde3dE54F18E10027Ee90fC95": "0xb62e92a7153bc921d877f67c396a09eaf8ddd6febe050b8f63fa928ff0e1f82c", "0xF73E304B4Ee5599d6B1f8cAbac96C716e0F8f40D": "0x5a8f04d59dd55feabf73841f14f21f5e33d088268e61b48c82c35ab3caefc217", "0x97C76f11a0227c35747492a85591818953CD6Bf7": "0x705de5c4e2bd9ac6ba8383d7d1bc393719a8a25a457465ccd93096e93f98d642", "0x774090EB85CDCBc8366A1Fcf3df47616f5759B19": "0x9e1c9604743ac4c0441820004ec9e83b5377f08bbc021d028bc98fae3e0bb695", "0xD6B517aC2b10E6CEbb91FA16b3A09fd6A24ee6Cd": "0x41b15d35349475bef292e050d0ff6e7b81bf6706f83d98277110997a88cb526c", "0x9Bbd7d38a12CCadbDBa57Bf6695f68d3F0F3bd13": "0xe4a829f3d0b5e7c3bfb73039d432f73e82d21b1da2a237274daefd84b6efb8f7", "0x4B8F92EA12a4c3070EFde148fFc3E8fef0a0c32F": "0x8fcd4a7a16d7f83096fbcbe3a60a834000716b01cef5a64fc254bf6786afa02d", "0xe331F6B9F543D1B6F3a29c563CA4d42716E15eb0": "0x9e7049c8102a87371652d4ce82869b756827cd61879a49959870f96c07b631a5", "0x6B9e0Bb5E72dcF7088F6EC0B1a7238f343B66feC": "0x5d40769e0e42d7baff6f61d36e06c12450da945cadc4b9bd7a98bd0796beadb1", "0x7e9Cb1095C50C88D7dBC1EE5a35Db1eEb6639434": "0x6ab0049078bb22cf79679f45d603e45c04ddd2865a6799f57189efe5b86aaa4d", "0x17C36E8E99CDDa5cF5023Ec305c330551BE4e4BA": "0x9ce02704d6fc4937b5a9df49805a6947da02cbfd24e5a99a3430f85be7c9afb1", "0x9841BAe45f0F43158FDB1A220da46BA2692f832c": "0x2d2d12422a317360c4e5dea66b4c4764b7c0e49a586f82019223ef665f0e3c59", "0xA56CfE816333e063eA627B864ab75cf5B5aaD70f": "0x7b50e52025b3788f8a723192a4ab626cb402843bc4a2dfdd263861d282faf04d", "0x9E9Fc97082e183C67eF395A9e3C5B87F7697a38a": "0xfab82008b2af03abe0174d95dff6ea12b1e7ba795364eb8650b4aeceb5e9926e", "0xc03C99218122Ac8B8A66915BDdE1d150C405BA91": "0x20e23677298e9890da3257e4a4b4992f2ff849b3bc32b46147dccadc9501f589", "0x6A758077fec5Bd172DE79726501Adcc3cd782c7b": "0x3586ffcd94aade94ff23e812a74d3d264ff4484fc61152fb046fee2c932a98b1", "0x78D9D47843acb0E89b01514602D494323920Ce49": "0x7c50c0d5693be92031d1c11c95c6f4cf7113104457fecb8ad44f85d20c479c07", "0x3CC5Dc036069f8bE310C10ed665a2E4479857d37": "0x39ebf9963d06cbdfb52351cb65beaa4905ca422626c09344a41b62ee8d50e117", "0x38267753823e71f4247EFe967D24e528093f2dF5": "0x9722364ae1f1a5465ef1a78f5c96e2dbbded896a256afb20c2b7f4e93a48e023", "0x24f133B668c2f450c9311Acf87EAC0E245CF6a37": "0xac6657677199375422439421b9b9d10954394d14bb09e17a69fa620c32cd005b", "0x9D83DfAb45E2B8F805ed9eba82698697d4520937": "0xcb150f931dac958826f6067de9c23efa0f727081b847ff3990e67c6951900ffb", "0x010e5F7f821d98e9bFDD3d7f94b35D49bAE4AD87": "0x41798a7e2e4fea09146e98f64b1f9a511d02471228499c4f793684c2aefba5d1", "0xdaA1E4766126A5e0014cEacF078Be7e7Eb3452f1": "0x58a47b7c52035f56360fc34f6a58a3d3dd7d05fc2846646e2be93bb7b9a31cce", "0x5a32F71443c92AEbC073c40Dfe21423236eb69cE": "0x852c7cb4920d7f4c3ab27d74e4b9bc37d80ba1d5fe1618e092ec5ef6f4b6441b", "0x2E799bec7433fc9712cE938fea16340C89bE7a32": "0xce2f992db1d1ccc66945bb61aba5794b054400f19be1f694eeb710a1d702b01e", "0x9Ba3F2DeF2C08fFF936bB2eb20E5D73653f7c2DC": "0xaf676ab451dab8b19273c74f2beefc844bd90c45b3d4519df3b628e4a623c725", "0x6427Fab9F9cfa47E3A95F94011B6C17bE0504F3A": "0xa1d0ad5973ce83d206edf94f4e1e821ad9f8a54fb9061a7fc1f1b3eb41bc003e", "0xD60464B648C804ED0DE574c7cDa6fa5AC407bcbc": "0x2646932e5f6b4203983ec2c7a33c9eb05143cbf663dfd244e759d107b418a2f1", "0x6a089Ed0CFC2D69973797f632dCF292EB30E4CFe": "0x69d38c15a27472d1710c0b0d7d50196614251ec909e15f79f98429c7a00820bc", "0x24C43C45f5a4a059464959C67F3785F72580e893": "0xff4ca214ef96011f0a294555da15d056a23adbd90d1954699f3d0be9ded8ba53", "0xDf43EFCDE94Fa718ca91A7fa2a61900F99D095F1": "0x7429b0c6cb209b5fbb2255ff4c991236fff6943087126bf8b380549ece055ac0", "0xD4827e77471EB50f24941652f59dD82205285087": "0x58522379a3392e442fff5a2b574cfd00803697b74caa84bcfbbbd38f5e796fe2", "0x8E35f728ee492bc557Bb200Abe17FCDb9720E317": "0x5a2642f9fb74363cb87e74cff745d2b0a2491230f2e1bedc126f7f982821e9af", "0x4aDb836b9670fBf9A56964ccF31b5F0fcB15fdC3": "0x92a2c7892b6331b0a6e703857815901106a406d3f2a1d46cefffd3ac3238a1d3", "0x777e2FC3486883143Ad4ae884afC7a103451Fdfb": "0x328644478bec8778d2e809497f1c662b1c073fe47904c116a744c6ef3ac7f2bb", "0x8388C6fa744767825cd7CE26478fBFCE23101A35": "0x3da449f15cec640871775298e306d81b295f20ad277386fda1918a01487ebf88", "0x45a70e7E5FAefFF0fff8329E1Bf06c40673dEeD7": "0xdd2f920defa7458ff8088e64a40745646015dd03e31ec63d281ea605d13896c3", "0x900309412597a0EE2E7312Af40171a7B0d1f7b1F": "0x994c7f5cd4053b54268d91547565d4a59d9f2de24a338bd8c1f280a5acbd5aad", "0xe843D5969AcE1aB48335754109102AcEB5BaB8E4": "0x502a9b6ae4ef77a407568d419852b6102b21fe8084c6cb636472bb9a10d111b9", "0x430f361fF5B7860b835667cf2c3fa1028B1E380f": "0x369fd711693df26e3ab793a07d11f44040c80612f74fcbd67c47f8429fc1952b", "0x040a1457bE73512Fca0fA45b1283c9102c8cc967": "0x93f4520c967c2074bd19d1ad5989822c2dc79915b4216b2d1cce711c95adcfa4", "0xacb422Fb3878dF6918fd9b2FC63c7c6fbEFDac5D": "0xb1cafbce9437d1eeea1191be4060bd8bbbb804f244cd18a38d11da676106f7a4", "0x8e71F680e0dC35bc90fbb0169c4ed2bBaC39f7d5": "0x4935ae4b1094075a2166b02bf581ff1ef225ecd6cba49e22de4af2ea07530ef4", "0x1Ca688d9FD83F2D43899C13123EbaDAedE2ca7Bc": "0xcedc376ccf9647ee43e8f0b5375355343adebf5851d9bdc3edbd670e49424fcb", "0x8303f145857D70Fb0cC5470719419Cb3972c9C83": "0x46ca93bf9496b0487638da60f84f724bfc980222fa696804362cff4e6edf2e05", "0xA4cbf3f339e85F2F98EF51e9C36C7Cc832F6819D": "0x80375f711c26cbaee09f7b773924dfc733cfd2ba2d24633d2dd62b31bdb5c0c2", "0x2733198C701AEC239A5518A36Cf219d0bE28e913": "0x53ae0792fde288382daf3eae441b6daeebbd39d196dbd22451f0ff34f15c1189", "0x6F6C387D3a1A0F4603Bb07f527b8b4CfdaF09B40": "0xf5b86c0a2ea8a2b556a50439419a4f479ca4b7cb6d868ff8a5d40d74f2d498a6", "0xaB3056358aCb52B771B94953667520a4c1A7c7FD": "0xb51c80b0feb87a2aa2231c6a4c414b6b64fc74c3899edd680962b8a367226b1c", "0xFeb3fE3ae4E8Da4Bf042281B49C74D127AF4d4B9": "0x91fa6ada95259edbdf28b41b9909f3bab81f5cedf655a644626914cd660ce125", "0x0715d94f9FE82F608D5815C4f9115195A37B206e": "0x640e3913e104e85d83a386feef3bb5b2793a3714647fd26b59d7ad421ec8513e", "0x68E6ae104b413ECC08fBe4d3698b2Dd1F196D18A": "0xdc0628b2522129ab1bb8807f1df870e26dcbd8bb17d3271cd60cf85e24a1adf4", "0x5AC59Cf1Bfa1fA16b29d08807D19f3B24b9b8e8a": "0xdab87b6bc54452e83a6d97799233a550636e4022a785a675cdb281f10a4aeba1", "0x0bD2b4a57a9298b609c062FD6454221b8bBa3730": "0xd170ac09c5ae935373abadf15e2ec51884d42dc31c16afcddceadf3a78538690", "0xe2CE9D4BdBf26CC721a3C6C3D0bBd8a24191725c": "0x845538a20709f896a6cf17b8c8454402240ba8da36ab8ec175dcdc071442f00f", "0xa0989787D80685EAe3a5D9bDc9A1e83A4a80206d": "0xe67beae768fffe4f38c327b4a7e0fc86d4993fdadae6f47cef3592e7e2956460", "0x9e756073967b45355BfF98F04fAE0321BF2D390a": "0xbc38d246284401856e4e0392c02e5481cab24d1394c97bfb0a6a3c7ad8879958", "0x21D76E0f500874D38ed80C34D9557b158C6Def92": "0x540e29d574bcda5af3eafe0647249196a78037c5d38299c2ca3471122abfba95", "0x70b8c985e6dE4813BFbE9F169F165F1F2c6744F5": "0x8effdffba1329175f7698709fc9408ebb0813d4bc0ae97c1b6d8cc4ade9d7871", "0x6a7ecB2e26997B8C71F4cec9480c8ACe8aDF0f55": "0xa855de3f46cc2128ce4cf8453d6bbef86ad0d3ef02bd6e28f62feb5341194db9", "0x42C7d4C6b06fA53085CCf5e265fbC62E146A1C0f": "0xd2b22c348794fa74ea2503f28b06ac31b1171132b5e04a755d9b96f14d63b269", "0x59ab381712Da2013f2Da09a925B8A2BEa6dBBE65": "0xfebaca90c02cea4f07354f4a06ccc45bc3980b5b03249ac09925822149e8d23e", "0x6334DB41F44fEc84Ea0E957Ba2BF082628768132": "0xce64482fb4a24c274394a2c2a06170109579eb8c69fa814b85b6201486c2d8f5", "0x627210066A60533C79cD244439dF66deB2884389": "0x3f42b751ac9177440016f32589c8f090da3d183d68a13c9c4ce729994a04b455", "0x33a9BA975559C13056391b7916556B9DA76376c7": "0x94c1b773926fd3f3c6a3c3e59952fae053e0150e618b2deb84035203643ceb91", "0xA1c7F3be60dEaCb36e15A39E22bb690f6EfA74D6": "0x35fd4cd962cabb57a89e4b25d3013710b70e2efe2ee97e8a72a20f034950af13", "0x72F1490dFCc7874539803aA0fF3C803fE04d3022": "0xc1534af4fb1c1ba019ce78a493ba83a5f8275140155dabbada070d490c9b83c5", "0x5F09DDf848335b451d5679ad9D183ECBe78a7ed2": "0xa37a4aa5ba1f9542b1620ac14ceed6b701480225868a6c1a330d5645bf46ef3e", "0xDD522752fC288f3902Da8EaeEf0A4A0abDeFCF53": "0x0b7d02697e46777b60af9a20e867f12f2c096e8ba461efd2cfff0f5aa4479e5c", "0x2e74ec05109EDFBbcB89927e29e853895D7e5C9C": "0x7aa0c090b021bb264677f4acc3535e17707af1318a1cb2ba1f6ab36d82b8f864", "0xb5874bAD7Fb623DCa4aeA93C2C45478C5e66ef78": "0xdb96eb820c8d9e953f1b6096cf2694a43757baea7e9454561c2cb7c24d51a60d", "0x38C432dD3f737d890F90183f0DF6c614B923a6Fb": "0x7bd75a4a05fa4ffe7a2440a1fba608e75f8d1e01282f398d2bb995a954effb56", "0x6cfAE51bbaC6108ec1914f505861B09CAD2FFE57": "0x36e2f2f4af62b588e20eb71eac9c7ae7dfb12ed2719a0ea59c4884522661639a", "0xbE85e5Ee928Cc12c4C513188D0C1E5eD51fF8A72": "0x2bf570ce44caec2dddad8738f0cc82753088e373dc4f04ed9d9613d2e38bc6ff", "0xccB99194E8658be881aEA3C34f3F0E5b3fC946aC": "0xf6002dd62e016e9a40cb0ccf2e974f1950910c22aaf42c357eac9ae2df1f29cf", "0x3da9E8574E51Fbb73818853cFb57009aB135a62a": "0xf41bb3fdc449d791695114409824419e33dea787a1227375cdc75f8b03689be1", "0x8F1Be53AA3D2A67eAEb60E92C20535e30d0C0B27": "0x82264915865f4395dd7357ddad96974a1a7a1cd0ef7c0ee4f75f4c7e2dcf27d3", "0xADF0dabF8EeE99cf4f1C87CD50AB1346a1bbc6Ba": "0xbe0f96fb9298d0446587b74d39c5871cfca6ea29d0e4bdfcb1e7f5aa07670634", "0x2fb53475562610fd0DeF878d03Deafba4f89A1D4": "0x4b13174e9bd036f330f71d1c5ce37780e432b8ec294343baf16a71ef57e439d7", "0x3cC822B3347F6e77309bcDcE2EaD4ea3E97B19CB": "0x84b737736ac3db063050fa6b8afa1810f4f25da80ba85c9221a669244ed897a4", "0xa0f46F244C2F10B0C622E61B0dDC53Da4b7DBF1c": "0x191cced5ea4a4ff14267932d23208a550efb138ef30c847a9837b1e278126cf6", "0x28F407D4418DC08F151FeF0f36D419b96294dE24": "0x54d5b384d4c2d86a52ea647d4ace3d2ef902ecdf5a0faded183d6a63a951143c", "0xb5FFCCb96Fcde4cC4d979C22c619bC27197BC235": "0x4e6e2caa5348c26b38e0d95c7c32a36a02ccf591ea83ccc35e7b3f50899344d0", "0xdacf3B210d530D7d226dcbD63d46b4674b8ea013": "0x1f58541959ae8e4bfa69f687eeb7a7f6221758265abe1980e856cafa2113156b", "0xbcAD8E6a8Ad05AD0F0C9bB95159e854DeD4a8361": "0x84d3e4ffa7a4950d303feb1007b1a5f5baec42e49eacb769cdce08f6964f756c", "0x23AE6D87e14De8E3ed337acdF54c5aF67817aAC1": "0x866064837acf35cc6466789850734b1d1bf610944879351ac38dfa6312f84e96", "0x78555EE882108c941Fa268B040B13074E54c2056": "0x38ea5420a1cfe4ef4013adac36c0167b7f18b1b656cf09a5dabfbe81b6c9e953"}


for address, key in adresses.items():
    driver = webdriver.Chrome(service=s)

    driver.get('https://faucet.polygon.technology/')
    driver.maximize_window()
    time.sleep(2)

    button = driver.find_element(By.CSS_SELECTOR, 'input')
    button.send_keys(address)

    button2 = driver.find_element(By.CSS_SELECTOR, '[type=button]:not(:disabled)')
    button2.click()
    time.sleep(1)

    button3 = driver.find_element(By.XPATH, '//button[text()="Confirm"]')
    button3.click()

    time.sleep(1)
    driver.close()
    driver.quit()
