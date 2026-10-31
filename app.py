from mitmproxy import http, ctx
import requests
import os
import json
import re
import hashlib
import gzip

TRENDRAFT_TG = "https://t.me/MDZCHEATS"
TRENDRAFT_SERVER = "http://trendraft-proxy-2-production.up.railway.app/"
AllClient = "ClientUsingVersion_NONE,ClientUsingVersion_NORMAL,ClientUsingVersion_MAX,ClientUsingVersion_FFI,ClientUsingVersion_MAX_HPE,ClientUsingVersion_FFVN"
AllRegion = "US,CN,TW,TH,VN,ID,PT,ES,RU,KR,FR,DE,TR,IN,JP,RO,SA,MM,PK,BD,MY"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

gamevar = []

ตัวคูณดาเมจ = 10000
ความเร็วการหมุนตัว = 100000

ยิงแรง = False
ขยายดาเมจ = True
ดีดไกล = True
วิ่งไว = True
สลับปืนไว = True
ไม่มีดีเลย์จากการตก = True
หันจอไว = True
จอยสติ๊กหมุนตัวไว = True

def เรียกคำขอเดิม(flow: http.HTTPFlow, url):
    params = dict(flow.request.query)
    response = requests.get(url, params=params, timeout=15)
    headers = dict(response.headers)
    flow.response = http.Response.make(response.status_code, response.content, headers)
    return

def ค้นหาชื่อ(flow: http.HTTPFlow, ชื่อ):
    if flow.request.path.startswith(ชื่อ) or ชื่อ  in flow.request.path:
        return True
    return False

def PrintInfo(flow: http.HTTPFlow):
    print("\n" + "=" * 70)
    print("[INFO]")
    print("=" * 70)

    print(f"Method : {flow.request.method}")
    print(f"URL    : {flow.request.pretty_url}")

    print("=" * 70)
    print("\n[PARAMS]")

    params = "\n".join(f"{key}: {value}" for key, value in flow.request.query.items())
    print(f"{params}")

    print("=" * 70)
    print("\n[HEADERS]")

    headers = "\n".join(f"{key}: {value}" for key, value in flow.request.headers.items())
    print(f'▶️ "{headers}" ◀️')

    print("=" * 70)
    print("\n[BODY LENGTH]")
    print(len(flow.request.content))

    print("\n[BODY HEX]")
    print(flow.request.content.hex())

    print("=" * 70)

def AddGameVar(name, var_type, value, comment=None):
    if comment is None:
        comment = name
    gamevar.append(f"{name},{comment},{var_type},{value},,\n")

def decode_hex(hex_str):
    try:
        cleaned = ''.join(c for c in hex_str if c in '0123456789abcdefABCDEF')
        if len(cleaned) < 2 or (len(cleaned) % 2) != 0:
            return b''
        bytes_data = bytes.fromhex(cleaned)
        return bytes_data
    except Exception as e:
        return b''

def _looks_like_hex_blob(text: str) -> bool:
    if text is None:
        return False
    s = str(text).strip()
    if not s:
        return False
    if not re.fullmatch(r"[0-9a-fA-F\s]+", s):
        return False
    cleaned = re.sub(r"\s+", "", s)
    return len(cleaned) >= 2 and (len(cleaned) % 2) == 0
   
def load_local_patch(filepath):
    try:
        with open(filepath, "rb") as f:
            data = f.read()

        if "avatar" in filepath.lower() and False:
            data = gzip.compress(data)

        return data

    except Exception as e:
        print(f"[LOAD ERROR] {filepath}: {e}")
        return None
        
def request(flow: http.HTTPFlow):
    url = flow.request.pretty_url
    url_lower = url.lower()
            
    if ค้นหาชื่อ(flow, "/fileinfo") and ค้นหาชื่อ(flow, "/android_astc/1.") and not ค้นหาชื่อ(flow, "gameassetbundles"):
        # เรียกคำขอเดิม(flow, "https://core-gmc.freefiremobile.com/live/ABHotUpdates/")
        data = load_local_patch("data/fileinfo.txt")
        
        if data:
            headers = {"Connection": "close"}

            flow.response = http.Response.make(200, data, {"Content-Type": "application/json; charset=utf-8", **headers})
            
    if ค้นหาชื่อ(flow, "/cache_res") and False:
        data = load_local_patch("data/cache_res.txt")
        
        if data:
            headers = {"Connection": "close"}
            print("\n" + "=" * 70)
            print("[✅✅✅ CACHE_RES INJECT] ✅✅✅")
            print("=" * 70)
            print(f"File      : data/cache_res")
            print(f"Size      : {len(data)} bytes")
            print("\n[DATA HEX]")
            print("=" * 70)

            flow.response = http.Response.make(200, data, {"Content-Type": "application/octet-stream", **headers})
            
    if ค้นหาชื่อ(flow, "/Ping"):
        เรียกคำขอเดิม(flow, "https://loginbp.ggpolarbear.com/MajorLogin")
        flow.request.host = "loginbp.ggpolarbear.com"
        flow.request.port = 443
        flow.request.scheme = "https"

        flow.request.headers["User-Agent"] = (
            "UnityPlayer/2022.3.47f1 "
            "(UnityWebRequest/1.0, libcurl/8.5.0-DEV)"
        )
        flow.request.headers["Accept"] = "*/*"
        flow.request.headers["Accept-Encoding"] = "deflate, gzip"
        flow.request.headers["Authorization"] = "Bearer"
        flow.request.headers["Content-Type"] = "application/x-www-form-urlencoded"
        flow.request.headers["Releaseversion"] = "OB54"
        flow.request.headers["X-Unity-Version"] = "2022.3.47f1"

        flow.request.content = b""
        
    if ค้นหาชื่อ(flow, "/MajorLogin"):
        target_url = "https://loginbp.ggpolarbear.com/MajorLogin"
        เรียกคำขอเดิม(flow, target_url)

        headers = {
            "User-Agent": "UnityPlayer/2022.3.47f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
            "Accept": "*/*",
            "Accept-Encoding": "deflate, gzip",
            "Authorization": "Bearer",
            "Content-Type": "application/x-www-form-urlencoded",
            "Releaseversion": "OB54",
            "X-Unity-Version": "2022.3.47f1",
        }

        response = requests.post(target_url, headers=headers, data=flow.request.content, timeout=30)

        flow.response = http.Response.make(response.status_code, response.content, dict(response.headers))

    if ค้นหาชื่อ(flow, "/avatar"):
        data = load_local_patch("data/avatar.txt")
        if data:
            headers = {"Connection": "close"}
            print("\n" + "=" * 70)
            print("[🥋🥋🥋 AVATAR INJECT] 🥋🥋🥋")
            print("=" * 70)
            print(f"File      : data/avatar")
            print(f"Size      : {len(data)} bytes")
            # print(f"Text      : {data}")
            print(f"DATA TYPE   : {type(data)}")
            print(f"DATA LEN    : {len(data)}")
            print(f"DATA HEX  : {data[:32].hex(' ').upper()}")
            print("=" * 70)

            # data = gzip.compress(data)
            # headers["Content-Encoding"] = "gzip"
            
            flow.response = http.Response.make(200, data, {"Content-Type": "application/octet-stream", **headers})
            sent_data = flow.response.content

            print("\n[📤 ACTUAL RESPONSE]")
            print(f"Size      : {len(sent_data)} bytes")
            print(f"First 32B : {sent_data[:32].hex(' ').upper()}")
            print(f"Text      : {sent_data[:32].decode('utf-8', errors='replace')}")

            expected = b"UnityFS"
    
            if sent_data.startswith(expected):
                print("✅ HEADER OK: เริ่มต้นด้วย UnityFS")
            else:
                print("❌ HEADER ERROR: ไม่ได้เริ่มต้นด้วย UnityFS")

            print("=" * 70)
            
    if ค้นหาชื่อ(flow, "/ver.php"):
        params = dict(flow.request.query)
        headers = "\n".join(f"{key}: {value}" for key, value in flow.request.headers.items())
        print(f'▶️ "{headers}" ◀️')
    
        gamevar.clear()
        gamevar.append("var_name,comment,var_type,var_value,var_region,var_platform\nvar_name,comment,var_type,var_value,var_region,var_platform\n")
    
        try:
            response = requests.get("https://version.ggwhitehawk.com/live/ver.php", params=params, timeout=15)
            data = response.json()

            """data["client_ip"] = "49.230.193.100"
            data["country_code"] = "TH"
            data["cdn_url"] = "https://dl.gmc.freefiremobile.com/live/ABHotUpdates/"
            data["backup_cdn_url"] = "https://dl.gmc.freefiremobile.com/live/ABHotUpdates/"
            data["img_cdn_url"] = "https://dl.gmc.freefiremobile.com/common/"
            data["abhotupdate_cdn_url"] = "https://core-gmc.freefiremobile.com/live/ABHotUpdates/"
            """
            # data["code"] = 0
            data["quality_level"] = 5
            data["graphic_level"] = 5
            data["show_high_framerate_UI"] = True
            data["is_server_open"] = True
            data["billboard_msg"] = "เซิร์ฟปิดอยู่ไอสัส แปปนึง / This server is currently down for maintenance."
            data["force_to_restart_app"] = False
            data["web_url"] = TRENDRAFT_TG
            data["patchnote_url"] = "https://www.instagram.com/thanakorn_hyper?igsh=MTIzcmxrOHFjd2I5eA=="
            data["appstore_url"] = TRENDRAFT_TG
            data["backup_appstore_url"] = TRENDRAFT_TG
            data["is_update_btn_show"] = False
            data["billboard_bg_url"] = "https://raw.githubusercontent.com/TRENDRAFT/THE-TRENDRAFT-PROJECT/main/Logo/LOW_TRENDRAFT_BG_PROXY.png"
            # data["server_url"] = TRENDRAFT_SERVER
            # data["cdn_url"] = TRENDRAFT_SERVER + "con/live/ABHotUpdaters/"
            # data["backup_cdn_url"] = TRENDRAFT_SERVER + "con/live/ABHotUpdaters/"
            # data["abhotupdate_cdn_url"] = "http://187.77.225.94:2587/live/ABHotUpdates/"
            # data["abhotupdate_cdn_url"] = TRENDRAFT_SERVER + "live/ABHotUpdates/"
            data["country_code"] = "DE"
            # data["remote_version"] = "1.130.20 [c][b][i][7A00FF]TRENDRAFT [FFFFFF]X [FF0000]MOD [/c][/b][/i][FFFFFF]"
            data["abhotupdate_check"] = "cache_res;assetindexer;SH-Gpp"
            data["latest_release_version"] = "OB54"
            # data["ggp_url"] = "http://trendraft-proxy-2-production.up.railway.app"
            data["force_refresh_restype"] = "optionalavatarres"
            
            if วิ่งไว:
                AddGameVar("RunSpeed", "float", 3)
                AddGameVar("DashSpeedScale", "float", 10)
                AddGameVar("CrouchSpeed", "float", 2.5)
                AddGameVar("DieingSpeed", "float", 1)
                # AddGameVar("ShoalSpeedScale", "float", 1.2) # ความเร็วการเดินบนน้ำ
                AddGameVar("SwimSpeed", "float", 4.2)
                AddGameVar("ResetRotationSpeed", "float", 100)
                AddGameVar("CarryingWalkSpeedScale", "float", 100)
        
            if สลับปืนไว:
                AddGameVar("SwapWeaponCD", "float", 0.2)
        
            if ไม่มีดีเลย์จากการตก:
                AddGameVar("HighFallActionSpeed", "float", 100)
        
            if ดีดไกล:
                AddGameVar("CatapultSpeed", "float", 100)
            
            AddGameVar("StropUseCooldown", "float", 100)
            AddGameVar("CrossOverJumpHorizontalSpeed", "float", 100)
        
            if หันจอไว:
                """AddGameVar("AimRotationSensitivityMax", "float", 30)
                AddGameVar("AimRotationSensitivityMin", "float", 500)"""
                AddGameVar("SensitivityMaxSetting", "float", 5)
                AddGameVar("Sensitivity1PMaxSetting", "float", 5)
                AddGameVar("X1ScopeMaxSetting", "float", 5)
                AddGameVar("X2ScopeMaxSetting", "float", 5)
                AddGameVar("X4ScopeMaxSetting", "float", 5)
                AddGameVar("X8ScopeMaxSetting", "float", 5)
                AddGameVar("FreeLookMaxSetting", "float", 5)
                AddGameVar("UseSniperCollider", "bool", True)
        
            if ยิงแรง:
                AddGameVar("HitDamageRatioHead", "float", ตัวคูณดาเมจ)
                AddGameVar("HitDamageRatioBody", "float", ตัวคูณดาเมจ)
                AddGameVar("HitDamageRatioLimb", "float", ตัวคูณดาเมจ)
                AddGameVar("HitDamageRatioVehicle", "float", ตัวคูณดาเมจ)
                AddGameVar("HitDamageRatioSniperExtension", "float", ตัวคูณดาเมจ)
            
            if ขยายดาเมจ:
                AddGameVar("SniperStandingColliderRadius", "float", 1)
                AddGameVar("SniperCrouchingColliderRadius", "float", 1)
                AddGameVar("SniperCreepingColliderRadius", "float", 1)
        
            AddGameVar("HighFPSSetting", "bool", True)
            AddGameVar("MAXQualityAB", "bool", True)
            AddGameVar("EnableOptimizeByQuality", "bool", False)
            AddGameVar("EnableQualityRenderer", "bool", True)
            AddGameVar("ForceShowHighQuality", "bool", True)
            AddGameVar("ForceShowHighInQualityHigh", "bool", True)
            AddGameVar("CharacterRecvShadow", "bool", True)
            AddGameVar("HDShowShadowOption", "bool", True)
            AddGameVar("LobbyCloserShadow", "bool", True)
            AddGameVar("LobbyCloserShadowHD", "bool", True)
            AddGameVar("EnableBloom", "bool", True)
            AddGameVar("EnableShibuyaFogAndBloom", "bool", True)
        
            if จอยสติ๊กหมุนตัวไว:
                AddGameVar("FreeMoveAngularSpeed", "float", ความเร็วการหมุนตัว)
                AddGameVar("FreeMoveAngularSpeedStand", "float", ความเร็วการหมุนตัว)
                AddGameVar("FreeMoveAngularSpeedCrouch", "float", ความเร็วการหมุนตัว)
                AddGameVar("FreeMoveAngularSpeedCreep", "float", ความเร็วการหมุนตัว)
                AddGameVar("FreeMoveAngularSpeedKnockDown", "float", ความเร็วการหมุนตัว)
        
            AddGameVar("CanReloadContinueShoot", "bool", True)
            AddGameVar("LessIsMoreMinReloadInterval", "uint32", 1)
            AddGameVar("LessIsMorePendingReloadInterval", "uint32", 1)
            AddGameVar("NoResetUplayerAnimationWhenReloading", "bool", True)
        
            AddGameVar("EnableShowPlayerOutline", "bool", True)
            AddGameVar("ShowPlayerOutlineMaxDistance", "uint32", 500)
            AddGameVar("EnableOutlineFuncInScript", "bool", True)
            AddGameVar("OutlineVisibleJudgeInUpDate", "bool", True)
        
            AddGameVar("PlayerOutlineWidthSpecial", "float", 50)
            AddGameVar("IngameCustomOpen", "bool", True)
            AddGameVar("IceWallModuleDefaultID", "int32", 907104212)
            AddGameVar("KeepFallingLandAnim", "bool", True)
            AddGameVar("PlayerOnSlopeCheckByRaycast", "bool", False)
            AddGameVar("CallStopEmoteAtPlayFireAnim", "bool", False)
            AddGameVar("BanFastRunWhenFire", "bool", False)
            AddGameVar("AlwaysCanShowEmotePanel", "bool", True)
            AddGameVar("FixFireOpenWhenSniperCloseNextFireAction", "bool", False)
            AddGameVar("EnableShaderRuntimeReload", "bool", True)
            AddGameVar("EnableClanNameAndLogoCapture", "bool", True)
            AddGameVar("StartDashWhenFallingApplySpeedDown", "bool", False)
            AddGameVar("PCBooyahV2", "bool", True)
            AddGameVar("EnableFallingDashOptimize", "bool", True)
            AddGameVar("InCarColliderHeight", "float", 2)
            AddGameVar("NickNameMaxLength", "int32", 30)
            AddGameVar("EnableCustomRoom", "bool", True)
            AddGameVar("EnableCustomRoomAuthority", "bool", True)
            AddGameVar("EnableCustom", "bool", True)
            AddGameVar("EnableFireFastWeaponStateFixed", "bool", True)
            
            AddGameVar("SkySurfingRotationSpeed", "float", 10000)
            AddGameVar("SkyDashingRotationSpeed", "float", 10000)
            AddGameVar("SkyDivingRotationSpeed", "float", 10000)   
               
            AddGameVar("FixCrouchFireAnim", "bool", False)
            AddGameVar("OpenNewPlayerHud", "bool", False)
            AddGameVar("OpenNewDownloadHandlerWay", "bool", False)
            AddGameVar("EnableCollectionEffect", "bool", True)
            AddGameVar("EnableQualityNewIsEffect", "bool", True)

            AddGameVar("VehicleKillPersonMinSpeedSqr", "float", 0.1)
            AddGameVar("CarCrashDamageScaleToPlayer", "float", 10000)
            AddGameVar("CarCrashDamageScaleWhenHitWall", "float", 0)
               
            AddGameVar("StropFallingDamageMax", "int32", 0)
            AddGameVar("EnableVibrateFeature", "bool", True)
            AddGameVar("ObserverCanThumbUp", "bool", True)
            # AddGameVar("PingMaxValue", "int32", 500)
            AddGameVar("CanSwimSurfing", "bool", True)
            AddGameVar("ShowHighFrameRateSetting", "bool", True)
            AddGameVar("InGameFrameSetting", "bool", True)
            AddGameVar("EnableSnowFlake", "bool", True)
            AddGameVar("EnableShowTargetOnMap", "bool", True)
            AddGameVar("EnableShowTargetprint", "bool", True)
            AddGameVar("EnableNewLocFix", "bool", False)
            AddGameVar("UseLiveScreen", "bool", True)
            AddGameVar("NicknameLengthMin", "int32", 1)
            
            AddGameVar("EnableVariableFFVoiceIDC", "bool", "false")
            AddGameVar("EnableYieldMutexDuringAsyncLoad", "bool", "false")
            AddGameVar("NinthProgressLoadingDuration", "float", "0")
            AddGameVar("EnableUGCScrollViewCulling", "bool", "false")
            AddGameVar("EnableUGCScrollViewCulling", "bool", "false")
            AddGameVar("ReservedInt01", "int", "5")
            AddGameVar("NinthLevelPortalRadius", "float", "20")
            AddGameVar("Enable2018ABstreamed", "bool", "false")
            AddGameVar("EnableAsyncCullResultsRelease", "bool", "false")
            AddGameVar("ReservedInt02", "int", "30")
            AddGameVar("EnableUGCHalfwayJoin", "bool", "false")
            
            AddGameVar("EnableIceWallHacker", "bool", False)
            AddGameVar("EnableIceWallHackerKill", "bool", False)
            AddGameVar("EnableHipHackerKill", "bool", False)
            AddGameVar("EnableSendHackStoreLog", "bool", False)
            AddGameVar("CameraHackRuntimeCheckIsWaitingCabinPhase", "bool", False)
            AddGameVar("DisableErrorLog", "bool", True)
            AddGameVar("EnableCheckSandModeBySwitchFunc", "bool", False)
            AddGameVar("CleanFFAntiState", "bool", True)
            AddGameVar("SaveLocationInPlatform", "bool", False)
            AddGameVar("EnableGGPDecryptFailureProtection", "bool", False)
            AddGameVar("EnableFileInfoEncryptionAndroid", "bool", False)
            AddGameVar("EnableFileInfoEncryptionIOS", "bool", False)
            AddGameVar("OptionalDeepFileCheck", "bool", False)
            AddGameVar("EnableOBBCheck", "bool", False)
            AddGameVar("ModifyAvatarCode", "bool", True)
            AddGameVar("ModifyAvatarDataCode", "bool", True)
            AddGameVar("NeedSignatureInfo", "bool", True)
            AddGameVar("EnableFirebase_Crashlytics", "bool", False)
            
            AddGameVar("FFAntihackDisabledRegions", "string", AllRegion)
            AddGameVar("FFAntihackDisabledClientVariant", "string", AllClient)
            AddGameVar("EnableMtpLiteDataRegion", "string", "")
            AddGameVar("FFAntihackEmulatorCheckDisbaledClientVariant", "string", AllClient)
            AddGameVar("ForceTutorial_ChangeHudABTest", "float", -1)
            AddGameVar("EnableFFAntihackInfoExtra", "bool", False)
            AddGameVar("EnableTrustItemCountFromServer", "bool", False)
            AddGameVar("EnableNativeCheck", "bool", False)
            AddGameVar("EnablePlatformCheck", "bool", False)
            AddGameVar("EnableMMKPlatformCheck", "bool", False)
            AddGameVar("EnableSupCheck", "bool", False)
            AddGameVar("EnableCheckFileStates", "bool", False)
            AddGameVar("OptionalDeepFileCheck", "bool", False)
            AddGameVar("OptionalDownloadHashCheckOpen", "bool", False)
            AddGameVar("MemoryCheckString", "string", "")
            AddGameVar("AgeCtrlAndroidBanCheckByInstallID", "bool", False)
            AddGameVar("ReturnToLobbyCheckAlbumOverTimeFile", "bool", False)
            AddGameVar("EnableCheckOverlapWithSantioDummy", "bool", False)
            AddGameVar("EnableIngameQuickReport", "bool", False)
            AddGameVar("AgeCtrl_iOSPrecheckForMinor", "bool", False)
            AddGameVar("AgeCtrl_CheckForThirdPartyBuild", "bool", False)
            AddGameVar("AgeCtrl_PromptWhenBannedByStrategy_iOS", "bool", False)
            AddGameVar("AgeCtrl_PromptWhenBannedByStrategy_Android", "bool", False)
            AddGameVar("BanStateDisabledArea", "string", AllRegion)
            AddGameVar("EnableCheckMatchEndDelayWhenDisconnect", "bool", False)
            AddGameVar("IsOpenRightScopeNearWallOpt", "bool", False)
            AddGameVar("IsOpenRightScopeInWallOpt", "bool", False)
            AddGameVar("IsOpenRightScopeDelayPlayerShowOpt", "bool", False)
            AddGameVar("ChatReportMaxTimes", "uint32", 0)
            AddGameVar("ClanReportMaxTimes", "uint32", 0)
            AddGameVar("BlocklistMaxNum", "Int32", 0)

            AddGameVar("DisableKillRefreshGetTime", "Int32", 0)
            AddGameVar("DisableDeviceIdentifier_iOS", "bool", False)
            AddGameVar("DisableDeviceIdentifier_Android", "bool", False)
            AddGameVar("FFAntihackDefenceLevel", "string", "0")
            AddGameVar("FFAntihackLightInitOnThread", "bool", False)
            AddGameVar("GGPLoginOnce", "bool", False)
            AddGameVar("EarlyInitGGP", "bool", False)
            AddGameVar("DisableGinInfoSend", "int", 1)
            AddGameVar("GinInfoBRAliveThreshold", "int", 0)
            AddGameVar("AntiHackResetSubgameInterval", "int", 0)
            AddGameVar("GGPUpdateFlag", "int", 0)
            AddGameVar("FFANTIHACKEXT_SPLIT_THRESHOLD", "int", 0)
            AddGameVar("ReleaseMemForMatchEndFor3I3A", "bool", False)
            AddGameVar("EnableReportIOFailedLogs", "bool", False)
            AddGameVar("EnableFFOPortingHDAnimation", "bool", False)
            AddGameVar("AutoEnemyMarkSwitch", "int", 2)
            AddGameVar("IsUseMedkitForceStand", "bool", False)
            AddGameVar("SimpleDamageCheckForAI", "bool", False)
            AddGameVar("UseResolveDNS", "bool", False)
            AddGameVar("EnableCheckBuf", "bool", False)
            AddGameVar("BanEnemyFlight", "bool", False)
            AddGameVar("BanFastRunWhenFire", "bool", False)
            AddGameVar("EnableInGameReturnToLobbyPopupMsg", "bool", False)
            AddGameVar("CSBanPickClientDelay", "float", 100000000000)
            AddGameVar("CoinCountChangeTime", "float", 100000000000)
            AddGameVar("CSShopNeedCoinCheckNum", "int", 0)
            AddGameVar("AutoPingSyncToBackend", "bool", False)
            AddGameVar("BanInuptInSlider", "bool", False)
            AddGameVar("CSBPRequestBanTime", "float", 10000000000000000000)
            AddGameVar("MultipleLobbyPing", "bool", False)
            AddGameVar("BanMoveInputForExecution", "bool", False)
            AddGameVar("EnableABHotUpdatesFileExistOptimize", "bool", False)
            AddGameVar("LoadGppLibSOToABHotUpdate", "bool", False)
            AddGameVar("EnableLobbySocialAreaStartGGP", "bool", False)
            AddGameVar("EnableLobbySocialAreaSubGameGGP", "bool", False)
            AddGameVar("EnableLoginQueue", "bool", False)
            AddGameVar("MinIntervalForRequestQueueInfo", "uint", 999999999999999)
            AddGameVar("MaxIntervalForRequestQueueInfo", "uint", 999999999999999)
            AddGameVar("ReportInstantiateJank", "bool", False)
            AddGameVar("ReportProtoTypeJank", "bool", False)
            AddGameVar("AutoEnemyMarkDuration", "bool", 999999999999999999)
            AddGameVar("IsOpenCSTeamGoal", "bool", True)
            AddGameVar("NetworkDetectionCDTime", "float", 999999999999999999)
            
            data["gamevar"] = "".join(gamevar)
            body = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            body = body.replace("/", r"\/")
            body = body.encode("utf-8")

            flow.response = http.Response.make(response.status_code, body, {"Content-Type": response.headers.get("Content-Type", "application/json")})
            
        except Exception as e:
            # print(f"    [ERROR] {e}")
            flow.response = http.Response.make(502, b'{"error":"upstream request failed"}', {"Content-Type": "application/json"})

    # print("\n" + "=" * 70 + "\n")

"""def response(flow: http.HTTPFlow):
    pass
"""
addons = []

# mitmdump --quiet -s h.py -p 8282
# mitmdump -s r.py --listen-host 0.0.0.0 --listen-port $PORT --quiet
